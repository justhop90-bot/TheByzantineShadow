#!/usr/bin/env python3
"""Build a source-order forensic matrix for the historical Shadow DC7 AI.

The historical source was preserved in commit 1d9f45b3b9ac03adc24103df2b21c84b92a45fb6
as a JSON wrapper whose `content` field contains the original .per text.  This script
extracts every defrule in source order and records control/state/economic effects.
It deliberately does not promote command issuance to world-state completion.
"""
from __future__ import annotations
import json, re, subprocess
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
    out = list(s)
    i = 0
    in_string = False
    while i < len(s):
        c = s[i]
        if c == '"' and (i == 0 or s[i-1] != '\\'):
            in_string = not in_string
            i += 1
            continue
        if not in_string and c == ';':
            j = s.find('\n', i)
            if j < 0: j = len(s)
            for k in range(i, j): out[k] = ' '
            i = j
            continue
        i += 1
    return ''.join(out)


def matching_paren(masked: str, start: int) -> int:
    depth = 0
    for i in range(start, len(masked)):
        if masked[i] == '(':
            depth += 1
        elif masked[i] == ')':
            depth -= 1
            if depth == 0: return i
    raise ValueError(f"unbalanced rule beginning at {start}")


def top_forms(text: str):
    m = mask_comments_strings(text)
    forms = []
    i = 0
    while i < len(m):
        if m[i] == '(':
            j = matching_paren(m, i)
            forms.append(text[i:j+1].strip())
            i = j + 1
        else:
            i += 1
    return forms


def head(form: str) -> str:
    m = re.match(r'\(\s*([^\s()]+)', form)
    return m.group(1) if m else ''


def extract_rules(src: str):
    masked = mask_comments_strings(src)
    rules = []
    pos = 0
    pat = re.compile(r'\(\s*defrule\b')
    while True:
        m = pat.search(masked, pos)
        if not m: break
        end = matching_paren(masked, m.start())
        raw = src[m.start():end+1]
        before = src[:m.start()]
        start_line = before.count('\n') + 1
        end_line = src[:end+1].count('\n') + 1
        inner = raw[raw.find('defrule') + len('defrule'): -1]
        im = mask_comments_strings(inner)
        # Locate top-level => token.
        depth = 0; arrow = None; i = 0
        while i < len(im):
            if im[i] == '(' : depth += 1
            elif im[i] == ')' : depth -= 1
            elif depth == 0 and im.startswith('=>', i):
                arrow = i; break
            i += 1
        if arrow is None:
            cond_text, act_text = inner, ''
        else:
            cond_text, act_text = inner[:arrow], inner[arrow+2:]
        rules.append({
            'raw': raw, 'start': start_line, 'end': end_line,
            'conditions': top_forms(cond_text), 'actions': top_forms(act_text),
        })
        pos = end + 1
    return rules

STATE_WRITES = {
    'set-goal','up-modify-goal','set-strategic-number','up-modify-sn','set-timer',
    'set-escrow-percentage','up-modify-escrow','release-escrow','disable-self',
    'up-set-offense-priority','up-set-defense-priority','up-modify-flag','up-modify-sn',
}
ESCROW = {'set-escrow-percentage','up-modify-escrow','release-escrow','up-release-escrow'}
COMMAND_HEADS = {
    'up-train','train','up-research','research','up-build','build','up-construct',
    'up-attack-now','up-attack-move','up-retreat-now','up-retreat-to','up-guard-unit',
    'up-garrison','up-send-flare','up-move-formation','up-assign-builders',
    'up-set-offense-priority','up-set-defense-priority','up-find-player','up-find-local',
    'up-find-remote','up-get-object-data','up-get-point','up-full-reset-search',
    'up-set-target-object','up-jump-rule','up-jump-direct','up-jump-dynamic',
}
OBSERVERS = {
    'up-get-fact','up-get-threat-data','up-get-object-data','up-get-point','up-get-focus-fact',
    'up-get-target-fact','up-find-player','up-find-local','up-find-remote','up-full-reset-search',
    'up-set-target-object','up-pending-objects','up-research-status','up-timer-status',
}


def compact(forms):
    return '<br>'.join(f.replace('|','\\|').replace('\n',' ') for f in forms) or '—'


def find_goal_refs(forms):
    refs = []
    for f in forms:
        h = head(f)
        if h in {'goal','up-compare-goal','set-goal','up-modify-goal'}:
            refs.append(f.replace('\n',' '))
    return refs


def classify(rule, idx, n):
    conds, acts = rule['conditions'], rule['actions']
    heads = [head(x) for x in acts]
    condheads = [head(x) for x in conds]
    writes = [x for x in acts if head(x) in STATE_WRITES]
    escrow = [x for x in acts if head(x) in ESCROW]
    commands = [x for x in acts if head(x) in COMMAND_HEADS]
    observers = [x for x in acts if head(x) in OBSERVERS]
    jumps = [x for x in acts if head(x) == 'up-jump-rule']
    if any('taunt-detected' in c for c in conds) and not any(h in {'up-train','up-research','train','research'} for h in heads):
        status = 'DEBUG/CHAT'
    elif any(h == 'disable-self' for h in heads) and all(h in {'set-goal','up-modify-goal','set-strategic-number','up-modify-sn','set-timer','disable-self'} for h in heads):
        status = 'INITIALIZER/LATCH'
    elif jumps:
        status = 'CONTROL-FLOW'
    elif escrow:
        status = 'ECONOMIC/ESCROW'
    elif commands:
        status = 'EXECUTION'
    elif writes or observers:
        status = 'STATE/OBSERVATION'
    else:
        status = 'LOGIC/NO-OP'
    if any(h in {'chat-to-all','chat-to-player','up-chat-data-to-all','up-chat-data-to-player','up-chat-data-to-self','acknowledge-taunt'} for h in heads):
        status = 'DEBUG/CHAT'
    # Creator-intent is deliberately phrased as an interpretation, not a claimed quote.
    if status == 'DEBUG/CHAT': intent = 'Diagnostic or operator-facing instrumentation; not core strategic authority unless another path proves otherwise.'
    elif status == 'INITIALIZER/LATCH': intent = 'Set a one-time baseline/latch so the rest of the script can treat the value as initialized instead of repeatedly recomputing it.'
    elif status == 'CONTROL-FLOW': intent = 'Manipulate the rule interpreter’s execution path: skip irrelevant work or loop until a stateful condition changes.'
    elif status == 'ECONOMIC/ESCROW': intent = 'Protect or release scarce resources around a temporary strategic commitment; the escrow is economic fencing, not proof of completion.'
    elif status == 'EXECUTION': intent = 'Translate an already-established condition into an engine action; issuance is not treated as observed world-state success.'
    elif status == 'STATE/OBSERVATION': intent = 'Maintain the internal model or sample engine state so later rules can make decisions without recomputing the same fact.'
    else: intent = 'Glue logic or a no-op used to shape the reactive rule pass; significance depends on neighboring rules and control-flow reachability.'
    return writes, escrow, commands, observers, jumps, status, intent


def main():
    src = git_source()
    rules = extract_rules(src)
    lines = []
    lines += ['# Shadow Source-Order Forensic Matrix v0.3', '',
              '> Historical baseline: `Shadow DC7.per` at commit `1d9f45b3b9ac03adc24103df2b21c84b92a45fb6`. ',
              '> This artifact is generated from the Git object, not from a truncated connector excerpt.', '',
              f'**Extracted rules:** {len(rules)}', '',
              '## Semantics and evidence discipline', '',
              '- Source order is the numbered rule order in the preserved `.per` text.',
              '- `up-jump-rule Δ` is modeled as a relative jump from the next rule: target = current + 1 + Δ. This matches the documented “skip 1 rule” and loop examples.',
              '- Command issuance is **not** completion. Completion is recorded only where the source itself supplies an observable condition; otherwise the matrix says `not established here`.',
              '- Creator intent is an engineering interpretation of the code path, not a claimed statement of author intent.',
              '- The original author explicitly warned that unused experimental code may remain; therefore reachability/status is not inferred solely from source presence.', '',
              '## Matrix', '',
              '| # | Source | Entry predicates | Writes | Escrow mutations | Commands | Jump | Normal successor | Jump successor | Completion condition | Status | Creator-intent interpretation |',
              '|---:|---|---|---|---|---|---|---:|---|---|---|---|']
    for i, r in enumerate(rules, 1):
        writes, escrow, commands, observers, jumps, status, intent = classify(r, i, len(rules))
        jump = compact(jumps)
        jump_succ = '—'
        if jumps:
            vals=[]
            for j in jumps:
                m=re.search(r'up-jump-rule\s+(-?\d+)', j)
                if m:
                    t=i+1+int(m.group(1)); vals.append(str(t) if 1 <= t <= len(rules) else f'{t} (out of range)')
                else: vals.append('dynamic/unknown')
            jump_succ=', '.join(vals)
        # Direct evidence only: research-completed / observed counts are completion predicates.
        completion=[]
        for c in r['conditions']:
            h=head(c)
            if h in {'research-completed','up-research-status','unit-type-count','unit-type-count-total','building-type-count','building-type-count-total','up-pending-objects'}:
                completion.append(c)
        comp=compact(completion) if completion else 'not established in this rule'
        lines.append(f'| {i} | L{r["start"]}-L{r["end"]} | {compact(r["conditions"])} | {compact(writes)} | {compact(escrow)} | {compact(commands)} | {jump} | {i+1 if i<len(rules) else "—"} | {jump_succ} | {comp} | {status} | {intent} |')
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(f'wrote {OUT} with {len(rules)} rules')

if __name__ == '__main__':
    main()
