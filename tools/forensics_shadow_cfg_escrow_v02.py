#!/usr/bin/env python3
"""Corrected v0.2 generator for the Shadow CFG/escrow forensic artifact.

The v0.1 classifier intentionally used broad token detection. This pass tightens
command detection so up-research-status/up-train-status are not misclassified as
command issuance. It reuses the independently generated source parser and CFG.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
sys.path.insert(0, str(TOOLS))
import forensics_shadow_cfg_escrow as base  # noqa: E402

base.MD_OUT = base.REPO / "docs/forensics/SHADOW_LIVE_CONTROL_FLOW_AND_ESCROW_v0.2.md"
base.SVG_OUT = base.REPO / "docs/forensics/SHADOW_LIVE_CONTROL_FLOW_v0.2.svg"


def classify(rule):
    body = rule['raw']
    masked = base.mask_comments_strings(body)
    esc = any(x in masked for x in ('escrow', 'release-escrow', 'up-modify-escrow'))
    progression = any(x in masked for x in ('gl-progression-pause', 'gl-current-build-item', 'gl-build-progress'))
    # Exact command forms only. This deliberately excludes up-research-status and
    # up-train-status predicates, which are observations rather than commands.
    command = bool(re.search(r'\(\s*up-(?:research|train)\s+', masked))
    jump = base.jumps(masked)
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


base.classify = classify

if __name__ == '__main__':
    src = base.git_source()
    rules = base.extract_rules(src)
    if len(rules) != 1956:
        raise SystemExit(f'Historical baseline changed: expected 1956 rules, got {len(rules)}')
    base.MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    report = base.build_report(src, rules).replace(
        '# Shadow DC7 — Live Control-Flow Graph + Escrow Path Trace v0.1',
        '# Shadow DC7 — Live Control-Flow Graph + Escrow Path Trace v0.2',
        1,
    )
    base.MD_OUT.write_text(report, encoding='utf-8')
    base.SVG_OUT.write_text(base.make_svg(rules), encoding='utf-8')
    print(f'generated {base.MD_OUT}')
    print(f'generated {base.SVG_OUT}')
