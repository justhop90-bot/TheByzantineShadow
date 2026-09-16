#!/usr/bin/env python3
"""Build a source-order forensic matrix for the historical Shadow DC7 AI."""
from __future__ import annotations
import hashlib, json, re, subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE_REF = "1d9f45b3b9ac03adc24103df2b21c84b92a45fb6"
SOURCE_PATH = "Shadow DC7.per"
OUT = REPO / "docs/forensics/SHADOW_SOURCE_ORDER_MATRIX_v0.3.md"


def git_source() -> str:
    raw = subprocess.check_output(["git", "show", f"{SOURCE_REF}:{SOURCE_PATH}"], cwd=REPO)
    text = raw.decode("utf-8")
    try:
        obj = json.loads(text)
        if isinstance(obj, dict) and "content" in obj:
            return obj["content"]
    except json.JSONDecodeError:
        pass
    return text


def mask_comments_strings(s: str) -> str:
    out = list(s); i = 0; in_string = False
    while i < len(s):
        c = s[i]
        if c == '"' and (i == 0 or s[i-1] != '\\'):
            in_string = not in_string; i += 1; continue
        if not in_string and c == ';':
            j = s.find('\n', i)
            if j < 0: j = len(s)
            for k in range(i, j): out[k] = ' '
            i = j; continue
        i += 1
    return ''.join(out)


def matching_paren(masked: str, start: int) -> int:
    depth = 0
    for i in range(start, len(masked)):
        if masked[i] == '(': depth += 1
        elif masked[i] == ')':
            depth -= 1
            if depth == 0: return i
    raise ValueError(f"unbalanced rule beginning at {start}")


def top_forms(text: str):
    m = mask_comments_strings(text); forms = []; i = 0
    while i < len(m):
        if m[i] == '(':
            j = matching_paren(m, i); forms.append(text[i:j+1].strip()); i = j + 1
        else: i += 1
    return forms


def head(form: str) -> str:
    m = re.match(r'\(\s*([^\s()]+)', form)
    return m.group(1) if m else ''


def extract_rules(src: str):
    masked = mask_comments_strings(src); rules = []; pos = 0
    pat = re.compile(r'\(\s*defrule\b')
    while True:
        m = pat.search(masked, pos)
        if not m: break
        end = matching_paren(masked, m.start())
        raw = src[m.start():end+1]
        start_line = src[:m.start()].count('\n') + 1
        end_line = src[:end+1].count('\n') + 1
        inner = raw[raw.find('defrule') + len('defrule'): -1]
        im = mask_comments_strings(inner); depth = 0; arrow = None; i = 0
        while i < len(im):
            if im[i] == '(': depth += 1
            elif im[i] == ')': depth -= 1
            elif depth == 0 and im.startswith('=>', i): arrow = i; break
            i += 1
        cond_text, act_text = (inner, '') if arrow is None else (inner[:arrow], inner[arrow+2:])
        rules.append({'raw': raw, 'start': start_line, 'end': end_line,
                      'conditions': top_forms(cond_text), 'actions': top_forms(act_text)})
        pos = end + 1
    return rules

STATE_WRITES = {'set-goal','up-modify-goal','set-strategic-number','up-modify-sn','set-timer',
                'set-escrow-percentage','up-modify-escrow','release-escrow','disable-self',
                'up-set-offense-priority','up-set-defense-priority','up-modify-flag'}
ESCROW = {'set-escrow-percentage','up-modify-escrow','release-escrow','up-release-escrow'}
COMMAND_HEADS = {'up-train','train','up-research','research','up-build','build','up-construct',
                 'up-attack-now','up-attack-move','up-retreat-now','up-retreat-to','up-guard-unit',
                 'up-garrison','up-send-flare','up-move-formation','up-assign-builders',
                 'up-set-offense-priority','up-set-defense-priority','up-find-player','up-find-local',
                 'up-find-remote','up-get-object-data','up-get-point','up-full-reset-search',
                 'up-set-target-object','up-jump-rule','up-jump-direct','up-jump-dynamic'}
OBSERVERS = {'up-get-fact','up-get-threat-data','up-get-object-data','up-get-point','up-get-focus-fact',
             'up-get-target-fact','up-find-player','up-find-local','up-find-remote','up-full-reset-search',
             'up-set-target-object','up-pending-objects','up-research-status','up-timer-status'}


def compact(forms):
    return '<br>'.join(f.replace('|','\\|').replace('\n',' ') for f in forms) or '—'


def classify(rule):
    conds, acts = rule['conditions'], rule['actions']; heads = [head(x) for x in acts]
    writes = [x for x in acts if head(x) in STATE_WRITES]
    escrow = [x for x in acts if head(x) in ESCROW]
    commands = [x for x in acts if head(x) in COMMAND_HEADS and head(x) not in OBSERVERS and head(x) != 'up-jump-rule']
    observers = [x for x in acts if head(x) in OBSERVERS]
    jumps = [x for x in acts if head(x) == 'up-jump-rule']
    if any('taunt-detected' in c for c in conds) and not any(h in {'up-train','up-research','train','research'} for h in heads): status = 'DEBUG/CHAT'
    elif any(h == 'disable-self' for h in heads) and all(h in {'set-goal','up-modify-goal','set-strategic-number','up-modify-sn','set-timer','disable-self'} for h in heads): status = 'INITIALIZER/LATCH'
    elif jumps: status = 'CONTROL-FLOW'
    elif escrow: status = 'ECONOMIC/ESCROW'
    elif commands: status = 'EXECUTION'
    elif writes or observers: status = 'STATE/OBSERVATION'
    else: status = 'LOGIC/NO-OP'
    if any(h in {'chat-to-all','chat-to-player','up-chat-data-to-all','up-chat-data-to-player','up-chat-data-to-self','acknowledge-taunt'} for h in heads): status = 'DEBUG/CHAT'
    if status == 'DEBUG/CHAT': intent = 'Diagnostic/operator instrumentation; not core strategic authority unless another path proves otherwise.'
    elif status == 'INITIALIZER/LATCH': intent = 'Establish a one-time baseline/latch so later passes can treat the value as initialized.'
    elif status == 'CONTROL-FLOW': intent = 'Manipulate interpreter control flow to skip irrelevant work or loop around a stateful condition.'
    elif status == 'ECONOMIC/ESCROW': intent = 'Fence scarce resources around a temporary strategic commitment; escrow is economic protection, not completion proof.'
    elif status == 'EXECUTION': intent = 'Translate an already-established condition into an engine action; issuance is not observed world-state success.'
    elif status == 'STATE/OBSERVATION': intent = 'Maintain the internal model or sample engine state so later rules can act on stored facts.'
    else: intent = 'Glue/no-op logic shaping the reactive rule pass; significance depends on neighboring rules and reachability.'
    return writes, escrow, commands, observers, jumps, status, intent


def main():
    src = git_source(); rules = extract_rules(src)
    wrapper_blob = subprocess.check_output(["git", "rev-parse", f"{SOURCE_REF}:{SOURCE_PATH}"], cwd=REPO).decode().strip()
    source_sha256 = hashlib.sha256(src.encode('utf-8')).hexdigest()
    release_heads = {'release-escrow','up-release-escrow'}
    lines = ['# Shadow Source-Order Forensic Matrix v0.3', '',
             f'> Historical baseline: `Shadow DC7.per` at commit `{SOURCE_REF}`.',
             f'> Preserved Git blob SHA-1: `{wrapper_blob}`. Extracted source SHA-256: `{source_sha256}`.',
             f'> Source lines: {src.count(chr(10))+1}; UTF-8 bytes: {len(src.encode("utf-8"))}; extracted `defrule` blocks: **{len(rules)}**.',
             '> This artifact is generated from the Git object, not from a truncated connector excerpt.', '',
             '## Semantics and evidence discipline', '',
             '- Source order is the numbered rule order in the preserved `.per` text.',
             '- `up-jump-rule Δ` is modeled as a relative jump from the next rule: target = current + 1 + Δ. The documented examples use `1` to skip one rule and `-1` to loop on the current rule.',
             '- Command issuance is **not** completion. Completion is recorded only where the source rule itself supplies an observable predicate; otherwise it says `not established in this rule`.',
             '- Release behavior is reported separately from escrow mutation so `release-escrow` cannot be mistaken for observed zero escrow.',
             '- Creator intent is an engineering interpretation of the code path, not a claimed quotation of FireBall37.',
             '- The original author explicitly warned that unused experimental code may remain; source presence therefore does not equal live reachability.', '',
             '## Matrix', '',
             '| # | Source | Entry predicates | Writes | Escrow mutations | Commands | Jump | Normal successor | Jump successor | Release behavior | Completion condition | Status | Creator-intent interpretation |',
             '|---:|---|---|---|---|---|---|---:|---|---|---|---|---|']
    for idx, r in enumerate(rules, 1):
        writes, escrow, commands, observers, jumps, status, intent = classify(r)
        jump = compact(jumps); jump_succ = '—'
        if jumps:
            vals=[]
            for j in jumps:
                m=re.search(r'up-jump-rule\s+(-?\d+)', j)
                if m:
                    t=idx+1+int(m.group(1)); vals.append(str(t) if 1 <= t <= len(rules) else f'{t} (out of range)')
                else: vals.append('dynamic/unknown')
            jump_succ=', '.join(vals)
        releases = [x for x in escrow if head(x) in release_heads or (head(x) == 'set-escrow-percentage' and re.search(r'\s0\s*\)', x))]
        release = compact(releases) if releases else 'none in this rule'
        completion = [c for c in r['conditions'] if head(c) in {'research-completed','up-research-status','unit-type-count','unit-type-count-total','building-type-count','building-type-count-total','up-pending-objects'}]
        comp = compact(completion) if completion else 'not established in this rule'
        if observers:
            writes = writes + [f'OBSERVED: {x}' for x in observers]
        lines.append(f'| {idx} | L{r["start"]}-L{r["end"]} | {compact(r["conditions"])} | {compact(writes)} | {compact(escrow)} | {compact(commands)} | {jump} | {idx+1 if idx<len(rules) else "—"} | {jump_succ} | {release} | {comp} | {status} | {intent} |')
    OUT.parent.mkdir(parents=True, exist_ok=True); OUT.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'wrote {OUT} with {len(rules)} rules; source_sha256={source_sha256}')

if __name__ == '__main__': main()
