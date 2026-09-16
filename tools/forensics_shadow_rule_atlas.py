#!/usr/bin/env python3
"""Build a forensic rule atlas from ShadowSource.per.

This tool is deliberately boring. It does not interpret AoE2 semantics; it
records source evidence so later analyses can disagree without rewriting the
corpus. Run it from the repository root:

    python tools/forensics_shadow_rule_atlas.py ShadowSource.per artifacts/forensics

Outputs are deterministic JSON/CSV/Markdown artifacts. The parser is tolerant
of comments and strings but fails loudly on unbalanced rule/constant blocks.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

RULE_START = re.compile(r"^\s*\(defrule\b", re.I)
CONST_START = re.compile(r"^\s*\(defconst\b", re.I)
RULE_ID = re.compile(r"^\s*\(defrule\s*$", re.I)
JUMP = re.compile(r"\(up-jump-rule\s+([^\)]+)\)", re.I)
GOAL_READ = re.compile(r"\(goal\s+([^\s\)]+)", re.I)
GOAL_WRITE = re.compile(r"\((?:set-goal|up-modify-goal)\s+([^\s\)]+)", re.I)
SN_READ = re.compile(r"\((?:up-compare-sn|up-get-sn|sn-)[^\)]*\b(sn-[A-Za-z0-9_-]+)", re.I)
SN_WRITE = re.compile(r"\((?:set-strategic-number|up-modify-sn)\s+(sn-[A-Za-z0-9_-]+)", re.I)
ESCROW = re.compile(r"\((set-escrow-percentage|release-escrow|can-build-with-escrow)\b([^\)]*)\)", re.I)
COMMAND_HEADS = {
    "build", "up-build", "train", "research", "up-research", "release-escrow",
    "set-escrow-percentage", "up-jump-rule", "up-assign-builders",
}
SEARCH_HEADS = {
    "up-full-reset-search", "up-set-target-point", "up-filter-distance",
    "up-find-remote", "up-clean-search", "up-remove-objects", "up-set-target-object",
    "up-get-point", "up-modify-sn",
}

@dataclass
class Block:
    kind: str
    ordinal: int
    start_line: int
    end_line: int
    start_byte: int
    end_byte: int
    raw_sha256: str
    raw: str


def strip_comments_preserving_strings(s: str) -> str:
    out=[]; i=0; quote=False
    while i < len(s):
        c=s[i]
        if c=='"':
            quote=not quote; out.append(c); i+=1; continue
        if c==';' and not quote:
            j=s.find('\n', i)
            if j < 0: break
            out.append('\n'); i=j+1; continue
        out.append(c); i+=1
    return ''.join(out)


def balanced_end(text: str, start: int) -> int:
    depth=0; quote=False; comment=False; i=start
    while i < len(text):
        c=text[i]
        if comment:
            if c=='\n': comment=False
            i+=1; continue
        if c==';' and not quote:
            comment=True; i+=1; continue
        if c=='"': quote=not quote; i+=1; continue
        if not quote:
            if c=='(': depth+=1
            elif c==')':
                depth-=1
                if depth==0: return i+1
                if depth < 0: raise ValueError(f"negative parenthesis depth at byte {i}")
        i+=1
    raise ValueError(f"unbalanced block beginning at byte {start}")


def line_and_byte_maps(raw: bytes):
    starts=[0]
    for m in re.finditer(b'\n', raw): starts.append(m.end())
    return starts


def locate_line(starts, byte_offset):
    import bisect
    return bisect.bisect_right(starts, byte_offset)


def extract_blocks(raw: bytes) -> list[Block]:
    text=raw.decode('utf-8')
    starts=line_and_byte_maps(raw)
    blocks=[]
    ordinal=0
    for m in re.finditer(r"(?m)^\s*\((?:defrule|defconst)\b", text, re.I):
        # Ignore a nested-looking match that lies inside an already captured block.
        if blocks and m.start() < blocks[-1].end_byte: continue
        end=balanced_end(text, m.start())
        kind='rule' if text[m.start():].lstrip().lower().startswith('(defrule') else 'const'
        if kind=='rule': ordinal += 1
        chunk=text[m.start():end]
        blocks.append(Block(kind, ordinal if kind=='rule' else 0,
            locate_line(starts,m.start()), locate_line(starts,end), m.start(), end,
            hashlib.sha256(chunk.encode()).hexdigest(), chunk))
    return blocks


def heads(body: str) -> list[str]:
    return re.findall(r"\(([A-Za-z][A-Za-z0-9_-]*)\b", body)


def classify(body: str) -> list[str]:
    b=body.lower(); tags=[]
    if 'set-goal' in b or 'modify-goal' in b or '(goal ' in b: tags.append('state/goal')
    if 'strategic-number' in b or 'compare-sn' in b: tags.append('state/sn')
    if 'escrow' in b: tags.append('escrow')
    if 'jump-rule' in b: tags.append('control/jump')
    if any(f'({x}' in b for x in SEARCH_HEADS): tags.append('search/placement')
    if any(f'({x}' in b for x in ('build','up-build','up-assign-builders')): tags.append('construction')
    if any(f'({x}' in b for x in ('train','research','up-research')): tags.append('production/research')
    if 'timer' in b or 'game-time' in b or 'fifth-turn' in b: tags.append('temporal')
    return tags or ['other']


def rule_record(block: Block) -> dict:
    raw=block.raw
    code=strip_comments_preserving_strings(raw)
    # The first top-level split is intentionally lexical rather than semantic.
    parts=re.split(r"\n\s*=>\s*\n", code, maxsplit=1)
    predicates=parts[0] if parts else code
    actions=parts[1] if len(parts)>1 else ''
    jumps=JUMP.findall(actions)
    goals_r=sorted(set(GOAL_READ.findall(predicates)))
    goals_w=sorted(set(GOAL_WRITE.findall(actions)))
    sns_w=sorted(set(SN_WRITE.findall(actions)))
    escrow_ops=[{'operation':m.group(1).lower(),'arguments':m.group(2).strip()} for m in ESCROW.finditer(code)]
    command_names=sorted(set(h.lower() for h in heads(actions) if h.lower() in COMMAND_HEADS))
    search_ops=sorted(set(h.lower() for h in heads(actions) if h.lower() in SEARCH_HEADS))
    return {
        'rule_ordinal': block.ordinal,
        'source_line_start': block.start_line,
        'source_line_end': block.end_line,
        'source_byte_start': block.start_byte,
        'source_byte_end_exclusive': block.end_byte,
        'raw_sha256': block.raw_sha256,
        'predicate_text': predicates.strip(),
        'action_text': actions.strip(),
        'goal_reads': goals_r,
        'goal_writes': goals_w,
        'strategic_number_writes': sns_w,
        'jumps': jumps,
        'escrow': escrow_ops,
        'commands': command_names,
        'search_operations': search_ops,
        'semantic_tags': classify(code),
    }


def main(argv: list[str]) -> int:
    if len(argv) not in (2,3):
        print('usage: python tools/forensics_shadow_rule_atlas.py SOURCE [OUTDIR]', file=sys.stderr); return 2
    src=Path(argv[1]); out=Path(argv[2]) if len(argv)==3 else Path('artifacts/forensics')
    raw=src.read_bytes(); blocks=extract_blocks(raw)
    rules=[rule_record(b) for b in blocks if b.kind=='rule']
    consts=[asdict(b) | {'raw': None} for b in blocks if b.kind=='const']
    out.mkdir(parents=True, exist_ok=True)
    manifest={
        'source': str(src), 'source_sha256': hashlib.sha256(raw).hexdigest(),
        'source_sha1': hashlib.sha1(raw).hexdigest(), 'source_bytes': len(raw),
        'rule_count': len(rules), 'constant_block_count': len(consts),
        'parser': 'tools/forensics_shadow_rule_atlas.py', 'schema_version':'0.1',
        'notes':['Lexical inventory only; no engine semantics are asserted.','Source order and byte offsets are preserved.']
    }
    (out/'shadow_rule_atlas.json').write_text(json.dumps({'manifest':manifest,'rules':rules},indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
    with (out/'shadow_rule_atlas.csv').open('w',newline='',encoding='utf-8') as f:
        fields=['rule_ordinal','source_line_start','source_line_end','source_byte_start','source_byte_end_exclusive','raw_sha256','semantic_tags','goal_reads','goal_writes','strategic_number_writes','jumps','commands','search_operations','escrow']
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
        for r in rules:
            row=r.copy()
            for k in fields:
                if isinstance(row.get(k),list): row[k]=json.dumps(row[k],ensure_ascii=False)
            w.writerow({k:row.get(k,'') for k in fields})
    summary=['# Shadow Rule Atlas v0.1','',f"- Source bytes: `{manifest['source_bytes']}`",f"- SHA-1: `{manifest['source_sha1']}`",f"- SHA-256: `{manifest['source_sha256']}`",f"- Rules parsed: `{manifest['rule_count']}`",f"- Constant blocks parsed: `{manifest['constant_block_count']}`",'', '## Important','', '- This artifact is a source index, not a behavioral proof.', '- A rule being indexed does not establish that it fires in runtime.', '- A command being present does not establish completion.', '- Escrow presence does not establish commitment semantics by itself.', '- All later semantic claims must cite these source offsets and rule ordinals.','']
    (out/'shadow_rule_atlas_summary.md').write_text('\n'.join(summary),encoding='utf-8')
    print(json.dumps(manifest,indent=2)); return 0

if __name__=='__main__': raise SystemExit(main(sys.argv))
