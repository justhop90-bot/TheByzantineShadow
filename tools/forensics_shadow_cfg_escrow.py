#!/usr/bin/env python3
"""Generate a source-order live CFG and escrow-path forensic report for Shadow DC7.

This is deliberately static. It models the .per rule-set as a sequential rule
machine with explicit up-jump-rule edges. It does not claim that predicates fire
at runtime, and it never treats command issuance as world-state completion.
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import subprocess
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SOURCE_REF = "1d9f45b3b9ac03adc24103df2b21c84b92a45fb6"
SOURCE_PATH = "Shadow DC7.per"
MD_OUT = REPO / "docs/forensics/SHADOW_LIVE_CONTROL_FLOW_AND_ESCROW_v0.1.md"
SVG_OUT = REPO / "docs/forensics/SHADOW_LIVE_CONTROL_FLOW_v0.1.svg"


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
        if c == '"' and (i == 0 or s[i - 1] != '\\'):
            in_string = not in_string
            out[i] = ' '
            i += 1
            continue
        if not in_string and c == ';':
            j = s.find('\n', i)
            if j < 0:
                j = len(s)
            for k in range(i, j):
                out[k] = ' '
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
            if depth == 0:
                return i
    raise ValueError(f"unbalanced form at {start}")


def extract_rules(src: str):
    masked = mask_comments_strings(src)
    pat = re.compile(r'\(\s*defrule\b')
    rules = []
    pos = 0
    while True:
        m = pat.search(masked, pos)
        if not m:
            break
        end = matching_paren(masked, m.start())
        raw = src[m.start():end + 1]
        start_line = src[:m.start()].count('\n') + 1
        end_line = src[:end + 1].count('\n') + 1
        inner = raw[raw.find('defrule') + len('defrule'):-1]
        im = mask_comments_strings(inner)
        depth = 0
        arrow = None
        i = 0
        while i < len(im):
            if im[i] == '(':
                depth += 1
            elif im[i] == ')':
                depth -= 1
            elif depth == 0 and im.startswith('=>', i):
                arrow = i
                break
            i += 1
        if arrow is None:
            lhs, rhs = inner, ''
        else:
            lhs, rhs = inner[:arrow], inner[arrow + 2:]
        rules.append({
            'raw': raw,
            'lhs': lhs.strip(),
            'rhs': rhs.strip(),
            'start_line': start_line,
            'end_line': end_line,
        })
        pos = end + 1
    return rules


def jumps(text: str):
    vals = []
    for m in re.finditer(r'\(\s*up-jump-rule\s+(-?\d+)\s*\)', text):
        vals.append(int(m.group(1)))
    return vals


def classify(rule):
    body = rule['raw']
    masked = mask_comments_strings(body)
    esc = any(x in masked for x in ('escrow', 'release-escrow', 'up-modify-escrow'))
    progression = any(x in masked for x in ('gl-progression-pause', 'gl-current-build-item', 'gl-build-progress'))
    command = any(x in masked for x in ('up-research', 'up-train'))
    jump = jumps(masked)
    tags = []
    if 'up-modify-escrow' in masked:
        tags.append('RESERVE/MODIFY')
    if 'set-escrow-percentage' in masked:
        tags.append('ESCROW-POLICY')
    if 'release-escrow' in masked:
        tags.append('RELEASE')
    if command:
        tags.append('COMMAND')
    if progression:
        tags.append('PROGRESSION')
    if 'disable-self' in masked:
        tags.append('SELF-DISABLE')
    if jump:
        tags.append('JUMP')
    return esc, progression, command, jump, tags


def compact(s, n=180):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[: n - 3] + '...'


def svg_escape(s):
    return html.escape(str(s), quote=True)


def make_svg(rules):
    # Six source-order lanes. Sequential edges remain visible; explicit jumps are
    # overlaid. The result is intentionally a zoomable forensic artifact.
    cols = 6
    rows = (len(rules) + cols - 1) // cols
    cw, rh = 220, 15
    margin_x, margin_y = 20, 28
    width = margin_x * 2 + cols * cw
    height = margin_y * 2 + rows * rh + 24
    relevant = []
    for idx, r in enumerate(rules, 1):
        esc, prog, cmd, js, tags = classify(r)
        relevant.append((esc, prog, cmd, js, tags))

    def xy(idx):
        z = idx - 1
        c = z // rows
        rr = z % rows
        return margin_x + c * cw + 2, margin_y + rr * rh

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<title>Shadow DC7 live source-order control-flow graph</title>',
        '<desc>All 1956 extracted defrule blocks. Thin gray edges are sequential source-order evaluation. Red edges are explicit up-jump-rule transfers. Escrow/progression/command rules are enlarged and color-coded by class.</desc>',
        '<style>text{font-family:monospace;font-size:8px}.n{fill:white;stroke:#777}.e{stroke:#bbb;stroke-width:.5}.j{stroke:#c00;stroke-width:1.3}.esc{fill:#ffe6cc;stroke:#c60}.cmd{fill:#e6f0ff;stroke:#357}.prog{fill:#eee6ff;stroke:#704}.both{fill:#ffe0f0;stroke:#a25}.hdr{font-size:11px;font-weight:bold}</style>',
        f'<text x="20" y="14" class="hdr">Shadow DC7 live CFG — {len(rules)} rules — normal source order + explicit jumps</text>',
        '<text x="20" y="25">Red = up-jump-rule; orange = escrow; blue = train/research command; purple = progression state; pink = combined.</text>'
    ]
    # normal edges
    for i in range(1, len(rules)):
        x1, y1 = xy(i); x2, y2 = xy(i + 1)
        out.append(f'<line class="e" x1="{x1+5}" y1="{y1+6}" x2="{x2+5}" y2="{y2+6}"/>')
    # jumps
    for i, r in enumerate(rules, 1):
        for d in jumps(mask_comments_strings(r['raw'])):
            target = i + 1 + d
            if 1 <= target <= len(rules):
                x1, y1 = xy(i); x2, y2 = xy(target)
                out.append(f'<line class="j" x1="{x1+10}" y1="{y1+5}" x2="{x2+10}" y2="{y2+5}"/>')
    # nodes
    for i, r in enumerate(rules, 1):
        esc, prog, cmd, js, tags = relevant[i - 1]
        x, y = xy(i)
        cls = 'n'
        if esc and prog:
            cls = 'both'
        elif esc:
            cls = 'esc'
        elif prog:
            cls = 'prog'
        elif cmd:
            cls = 'cmd'
        out.append(f'<rect class="{cls}" x="{x}" y="{y}" width="18" height="11" rx="1"><title>Rule {i}, source lines {r["start_line"]}-{r["end_line"]}: {svg_escape(compact(r["lhs"], 220))}</title></rect>')
        out.append(f'<text x="{x+21}" y="{y+9}">{i}</text>')
    out.append('</svg>')
    return '\n'.join(out)


def build_report(src, rules):
    source_sha256 = hashlib.sha256(src.encode('utf-8')).hexdigest()
    escrow_rows = []
    for i, r in enumerate(rules, 1):
        esc, prog, cmd, js, tags = classify(r)
        if esc or prog or cmd:
            escrow_rows.append((i, r, esc, prog, cmd, js, tags))

    reserve = [x for x in escrow_rows if 'RESERVE/MODIFY' in x[6]]
    release = [x for x in escrow_rows if 'RELEASE' in x[6]]
    commands = [x for x in escrow_rows if 'COMMAND' in x[6]]
    prog = [x for x in escrow_rows if 'PROGRESSION' in x[6]]
    jumps_used = [(i, j) for i, r, *_ in escrow_rows for j in jumps(mask_comments_strings(r['raw']))]

    lines = [
        '# Shadow DC7 — Live Control-Flow Graph + Escrow Path Trace v0.1', '',
        '## Forensic basis',
        f'- Historical source commit: `{SOURCE_REF}`',
        f'- Historical Git blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`',
        f'- Extracted source SHA-256: `{source_sha256}`',
        f'- Source size: {len(src.encode("utf-8")):,} UTF-8 bytes; {src.count(chr(10)) + 1:,} lines.',
        f'- Extracted rule blocks: **{len(rules):,} `defrule` blocks**.',
        '',
        '## Interpretation boundary',
        'This is a static control-flow/dataflow reconstruction. Every rule has a normal source-order successor because the engine evaluates the rule set sequentially. Explicit `(up-jump-rule Δ)` transfers are modeled as `current rule + 1 + Δ`, consistent with the scripting semantics already documented in the repository. A predicate being reachable in this graph does **not** prove that it fires in a particular game. Likewise, issuing `up-train` or `up-research` is not treated as completion.',
        '',
        '## What “live CFG” means here',
        'The graph is the executable source-order machine, not a fantasy semantic graph. It preserves the awkwardness that makes Shadow interesting: long sequential runs, targeted jumps, self-disabling rules, and state-dependent re-entry. The graph therefore answers **where control can move**, while the escrow trace answers **which state/resource mechanisms participate in the economic interruption path**.',
        '',
        '## Escrow architecture recovered from the source',
        'The evidence does not support treating `gl-escrow-state` as an escrow owner. It is used as a command accounting mode (`with-escrow` / `without-escrow`) passed to `up-train` and `up-research`. The physical reservation mechanism is instead expressed through `up-modify-escrow`, `set-escrow-percentage`, and `release-escrow`, coordinated by progression state such as `gl-progression-pause`, `gl-current-build-item`, and `gl-build-progress`.',
        '',
        'The recurring control pattern is therefore:',
        '```text',
        'strategic/progression condition',
        '        ↓',
        'identify current subobjective / interruption',
        '        ↓',
        'configure physical escrow',
        '        ↓',
        'issue escrow-aware research/train command',
        '        ↓',
        'observe/advance progression state',
        '        ↓',
        'disable/reset interruption state',
        '        ↓',
        'zero/release the temporary escrow components',
        '        ↓',
        'return to the broader strategy/progression machine',
        '```',
        '',
        'This is the key transplant insight: **escrow is not the strategy. Escrow is Shadow’s resource-protection actuator for temporary strategic interruption.**',
        '',
        '## Static escrow-path inventory',
        f'- Rules containing escrow/progression/command signals: **{len(escrow_rows)}**.',
        f'- Explicit escrow reservation/modification rules: **{len(reserve)}**.',
        f'- Explicit release rules: **{len(release)}**.',
        f'- Escrow-aware train/research command rules: **{len(commands)}**.',
        f'- Progression-state rules participating in the same static neighborhood: **{len(prog)}**.',
        f'- Explicit jumps encountered on those relevant rules: **{len(jumps_used)}**.',
        '',
        '### Relevant rule trace',
        '| Rule | Source lines | Class | Jump(s) | LHS / trigger excerpt | RHS / effect excerpt |',
        '|---:|---:|---|---|---|---|',
    ]
    for i, r, esc, pr, cmd, js, tags in escrow_rows:
        lhs = compact(r['lhs']).replace('|', '\\|')
        rhs = compact(r['rhs']).replace('|', '\\|')
        jump_text = ', '.join(str(j) for j in js) if js else '—'
        lines.append(f'| {i} | {r["start_line"]}-{r["end_line"]} | {", ".join(tags) or "STATE"} | {jump_text} | `{lhs}` | `{rhs}` |')

    lines += [
        '',
        '## End-to-end escrow trace model',
        'The source supports several concrete variants rather than one universal transaction routine. The common skeleton is:',
        '',
        '1. **Detect an interruptible progression requirement.** Shadow uses strategy/progression predicates and a current-build cursor rather than constructing an isolated transaction object.',
        '2. **Arm the interruption.** `gl-progression-pause` becomes the selected temporary subobjective (for example, a blacksmith technology).',
        '3. **Reserve only the required resources.** `up-modify-escrow` adds a bounded physical reservation; `set-escrow-percentage` can reshape which resource streams are protected.',
        '4. **Execute through the engine’s own command path.** `up-research` / `up-train` receive `gl-escrow-state` as the accounting mode. This is execution authorization/accounting, not ownership identity.',
        '5. **Reconcile progression.** Completion is inferred only through the relevant observed research/progression predicates and then the progression cursor is advanced/reset. Command issuance itself is not completion.',
        '6. **Release the temporary reservation.** Shadow explicitly sets the affected escrow percentages to zero and calls `release-escrow` for the resources being returned to the general economy.',
        '7. **Re-enter the broader progression machine.** The temporary interruption clears and the strategic build/progression state resumes or advances.',
        '',
        '### Important asymmetry',
        'The source contains strong evidence for **reservation + execution + release + restoration**, but it does not expose a clean, modern logical “commitment ledger” separating requirement identity from physical engine escrow. That is precisely where AEGIS can add governance without replacing Shadow’s proven economic substrate.',
        '',
        '## Byzantine reconstruction consequence',
        'For the Byzantine bot, do not copy Shadow’s Vikings-specific objectives. Transplant the **mechanism**: capability gap → temporary requirement → physical reservation → escrow-aware executor → observed completion → release → strategic restoration. Byzantine policy should decide why the interruption exists (anti-cavalry, anti-archer, anti-infantry, defensive survival, siege response, Imperial transition, map-control, or another verified capability gap); Shadow-style economic machinery should decide how to protect the resources while the proven executor performs the action.',
        '',
        'The clean boundary is therefore:',
        '```text',
        'AEGIS: requirement / capability rationale / arbitration / authorization / verification',
        '                 ↓',
        'SHADOW SUBSTRATE: progression / escrow / interruption / execution / release / restoration',
        '                 ↓',
        'WORLD STATE',
        '                 ↓',
        'AEGIS VERIFICATION + REASSESSMENT',
        '```',
        '',
        '## What this rules out',
        '- `gl-escrow-state` as a logical transaction owner.',
        '- Treating `set-escrow-percentage` as proof that the economic operation completed.',
        '- Treating `up-train` / `up-research` issuance as completion.',
        '- Replacing Shadow’s dynamic escrow mechanism with a static Byzantine build-order table.',
        '- Moving physical escrow into AEGIS merely because AEGIS owns strategic arbitration.',
        '',
        '## Next forensic step',
        'Use this graph to isolate the **reachable escrow families** and transplant them as preserved donor slices. Each candidate slice should retain source-order neighborhood, prerequisite predicates, escrow allocation, command mode, observed completion, release, and restoration together. Do not transplant an isolated `up-modify-escrow` call and call that “Shadow escrow.” The behavioral unit is the whole interruption/reconciliation path.',
        '',
        '## Artifact',
        f'- Zoomable SVG: `SHADOW_LIVE_CONTROL_FLOW_v0.1.svg`',
        f'- Generated from the same historical source and rule extractor; no manual rule transcription.',
    ]
    return '\n'.join(lines) + '\n'


def main():
    src = git_source()
    rules = extract_rules(src)
    if len(rules) != 1956:
        raise SystemExit(f'Expected the verified 1,956-rule historical baseline; extracted {len(rules)} instead.')
    MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    MD_OUT.write_text(build_report(src, rules), encoding='utf-8')
    SVG_OUT.write_text(make_svg(rules), encoding='utf-8')
    print(f'generated {MD_OUT}')
    print(f'generated {SVG_OUT}')


if __name__ == '__main__':
    main()
