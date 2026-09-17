#!/usr/bin/env python3
"""Generate the authenticated R07 control-flow edge matrix.

Evidence discipline:
- DIRECT: literal donor source text / source location / jump delta.
- MECHANICALLY DERIVED: jump target = source rule + delta; fall-through = rule + 1.
- MECHANICALLY CLASSIFIED: region membership, direction, boundary status.

The canonical ShadowSource.per Git blob SHA is verified before any graph is emitted.
"""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
OUT = ROOT / "docs" / "forensics" / "SHADOW_R07_EDGE_MATRIX_v0.1.csv"
EXPECTED_BLOB_SHA = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
R07_START = 1794
R07_END = 1896


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def parse_rules(text: str):
    """Parse top-level defrule forms using balanced parentheses."""
    starts = [m.start() for m in re.finditer(r"(?m)^\s*\(defrule\b", text)]
    rules = []
    for rid, start in enumerate(starts, 1):
        depth = 0
        end = None
        i = start
        in_string = False
        escaped = False
        while i < len(text):
            ch = text[i]
            if in_string:
                if escaped:
                    escaped = False
                elif ch == "\\":
                    escaped = True
                elif ch == '"':
                    in_string = False
            else:
                if ch == '"':
                    in_string = True
                elif ch == '(':
                    depth += 1
                elif ch == ')':
                    depth -= 1
                    if depth == 0:
                        end = i + 1
                        break
            i += 1
        if end is None:
            raise SystemExit(f"unbalanced defrule #{rid}")
        raw = text[start:end]
        line_start = text.count("\n", 0, start) + 1
        line_end = text.count("\n", 0, end) + 1
        rules.append((rid, line_start, line_end, raw))
    return rules


def main() -> None:
    raw = SOURCE.read_bytes()
    actual = git_blob_sha(raw)
    if actual != EXPECTED_BLOB_SHA:
        raise SystemExit(
            f"AUTHENTICATION FAILURE: ShadowSource.per blob SHA {actual} != {EXPECTED_BLOB_SHA}"
        )

    text = raw.decode("utf-8")
    rules = parse_rules(text)
    if len(rules) != 1956:
        raise SystemExit(f"DONOR RULE COUNT FAILURE: expected 1956, got {len(rules)}")

    by_id = {r[0]: r for r in rules}
    r07_ids = set(range(R07_START, R07_END + 1))
    rows = []

    def add_edge(direction, source_id, target_id, kind, delta, source_line, source_text, evidence):
        source_region = source_id in r07_ids
        target_region = target_id in r07_ids
        boundary = source_region != target_region
        rows.append({
            "direction": direction,
            "source_rule": source_id,
            "target_rule": target_id,
            "edge_kind": kind,
            "jump_delta": "" if delta is None else delta,
            "source_line": source_line,
            "source_region": "R07" if source_region else "OUTSIDE_R07",
            "target_region": "R07" if target_region else "OUTSIDE_R07",
            "cross_boundary": "YES" if boundary else "NO",
            "source_fact_evidence": evidence,
            "target_resolution_evidence": "MECHANICALLY_DERIVED" if kind == "up-jump" else "MECHANICALLY_DERIVED",
            "boundary_classification_evidence": "MECHANICALLY_CLASSIFIED",
            "raw_jump_or_successor": source_text,
        })

    # Outgoing edges for every R07 rule: normal fall-through plus every explicit jump.
    for rid in range(R07_START, R07_END + 1):
        _, line_start, _, body = by_id[rid]
        fall = rid + 1 if rid < len(rules) else None
        if fall is not None:
            add_edge(
                "OUTGOING", rid, fall, "fall-through", None, line_start,
                f"rule {rid} -> rule {fall}", "DIRECT_SOURCE_RULE_ID + SOURCE_ORDER"
            )
        for m in re.finditer(r"\(\s*up-jump-rule\s+([+-]?\d+)\s*\)", body):
            delta = int(m.group(1))
            target = rid + delta
            if not (1 <= target <= len(rules)):
                raise SystemExit(f"OUT-OF-RANGE JUMP: rule {rid} delta {delta} -> {target}")
            add_edge(
                "OUTGOING", rid, target, "up-jump", delta, line_start,
                m.group(0), "DIRECT_DONOR_TEXT"
            )

    # Incoming explicit jumps from the complete authenticated donor, including cross-boundary jumps.
    for rid, line_start, _, body in rules:
        for m in re.finditer(r"\(\s*up-jump-rule\s+([+-]?\d+)\s*\)", body):
            delta = int(m.group(1))
            target = rid + delta
            if not (1 <= target <= len(rules)):
                raise SystemExit(f"OUT-OF-RANGE JUMP: rule {rid} delta {delta} -> {target}")
            if target in r07_ids and rid not in r07_ids:
                add_edge(
                    "INCOMING", rid, target, "up-jump", delta, line_start,
                    m.group(0), "DIRECT_DONOR_TEXT"
                )

    # Cross-boundary fall-through at the R07 edges (entry/exit boundaries).
    if R07_START > 1:
        add_edge(
            "INCOMING", R07_START - 1, R07_START, "fall-through", None,
            by_id[R07_START - 1][1], f"rule {R07_START - 1} -> rule {R07_START}",
            "MECHANICALLY_DERIVED_SOURCE_ORDER"
        )
    add_edge(
        "OUTGOING", R07_END, R07_END + 1, "fall-through", None,
        by_id[R07_END][1], f"rule {R07_END} -> rule {R07_END + 1}",
        "MECHANICALLY_DERIVED_SOURCE_ORDER"
    )

    # De-duplicate exact edge records (the R07 entry edge is intentionally represented once).
    unique = {}
    for row in rows:
        key = (row["direction"], row["source_rule"], row["target_rule"], row["edge_kind"], row["jump_delta"])
        unique[key] = row
    rows = sorted(unique.values(), key=lambda r: (r["source_rule"], r["direction"] != "OUTGOING", r["target_rule"], r["edge_kind"]))

    OUT.parent.mkdir(parents=True, exist_ok=True)
    fields = [
        "direction", "source_rule", "target_rule", "edge_kind", "jump_delta", "source_line",
        "source_region", "target_region", "cross_boundary", "source_fact_evidence",
        "target_resolution_evidence", "boundary_classification_evidence", "raw_jump_or_successor",
    ]
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    outgoing_r07 = [r for r in rows if r["direction"] == "OUTGOING" and r["source_rule"] in r07_ids]
    incoming_r07 = [r for r in rows if r["direction"] == "INCOMING" and r["target_rule"] in r07_ids]
    cross = [r for r in rows if r["cross_boundary"] == "YES"]
    jumps = [r for r in rows if r["edge_kind"] == "up-jump"]
    print(f"authenticated_blob_sha={actual}")
    print(f"donor_rule_count={len(rules)}")
    print(f"r07_rules={R07_START}-{R07_END} ({len(r07_ids)})")
    print(f"outgoing_r07_edges={len(outgoing_r07)}")
    print(f"incoming_r07_edges={len(incoming_r07)}")
    print(f"all_r07_boundary_edges={len(cross)}")
    print(f"jump_edges_in_matrix={len(jumps)}")
    print(f"output={OUT}")


if __name__ == "__main__":
    main()
