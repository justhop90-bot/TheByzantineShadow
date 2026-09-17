#!/usr/bin/env python3
"""Static qualification of the authenticated R07 1794-1849 transplant."""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
IMPLEMENTATION = ROOT / "ShadowByzantine" / "04_construction.per"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
EXPECTED_RULES = 1956
FIRST = 1794
LAST = 1849


def git_blob_sha1(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask_source(text: str) -> str:
    out = list(text)
    i = 0
    n = len(text)
    in_string = False
    escaped = False
    while i < n:
        c = text[i]
        if in_string:
            if c == "\\" and not escaped:
                out[i] = " "
                escaped = True
            elif c == '"' and not escaped:
                out[i] = " "
                in_string = False
                escaped = False
            else:
                if c not in "\r\n":
                    out[i] = " "
                escaped = False
            i += 1
            continue
        if c == '"':
            out[i] = " "
            in_string = True
            i += 1
            continue
        if c == ';':
            while i < n and text[i] not in "\r\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return "".join(out)


def extract_rules(text: str):
    masked = mask_source(text)
    starts = [m.start() for m in re.finditer(r"\(defrule\b", masked)]
    rules = []
    for start in starts:
        depth = 0
        end = None
        for i in range(start, len(masked)):
            if masked[i] == "(":
                depth += 1
            elif masked[i] == ")":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise SystemExit(f"unbalanced defrule beginning at offset {start}")
        rules.append(text[start:end])
    return rules


def normalize(rule: str) -> str:
    return re.sub(r"\s+", " ", mask_source(rule)).strip()


def jump_deltas(rule: str):
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", normalize(rule))]


def main() -> int:
    source_bytes = SOURCE.read_bytes()
    source_sha = git_blob_sha1(source_bytes)
    if source_sha != EXPECTED_BLOB:
        raise SystemExit(f"DONOR SHA MISMATCH: expected {EXPECTED_BLOB}, got {source_sha}")

    source_rules = extract_rules(source_bytes.decode("utf-8"))
    impl_rules = extract_rules(IMPLEMENTATION.read_text(encoding="utf-8"))

    if len(source_rules) != EXPECTED_RULES:
        raise SystemExit(f"DONOR RULE COUNT MISMATCH: expected {EXPECTED_RULES}, got {len(source_rules)}")

    expected_count = LAST - FIRST + 1
    if len(impl_rules) != expected_count:
        raise SystemExit(
            f"IMPLEMENTATION RULE COUNT MISMATCH: expected {expected_count}, got {len(impl_rules)}"
        )

    donor_slice = source_rules[FIRST - 1 : LAST]
    mismatches = []
    for ordinal, (donor, impl) in enumerate(zip(donor_slice, impl_rules), start=FIRST):
        if normalize(donor) != normalize(impl):
            mismatches.append(ordinal)

    if mismatches:
        raise SystemExit(f"RULE BODY MISMATCHES: {mismatches}")

    donor_jumps = [j for r in donor_slice for j in jump_deltas(r)]
    impl_jumps = [j for r in impl_rules for j in jump_deltas(r)]
    if donor_jumps != impl_jumps:
        raise SystemExit(f"JUMP MISMATCH: donor={donor_jumps}, implementation={impl_jumps}")

    print(f"AUTHENTICATED_DONOR_SHA={source_sha}")
    print(f"DONOR_RULE_COUNT={len(source_rules)}")
    print(f"IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}")
    print(f"IMPLEMENTED_RULE_COUNT={len(impl_rules)}")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print(f"UP_JUMP_EQUIVALENCE=PASS ({len(impl_jumps)} jumps)")
    print("SOURCE_ORDER=PASS")
    print("STATIC_R07_1794_1849_QUALIFICATION=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
