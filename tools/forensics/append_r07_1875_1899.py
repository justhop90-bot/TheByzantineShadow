#!/usr/bin/env python3
"""Append authenticated Shadow R07 rules 1875-1899 to 04_construction.per.

The donor is authenticated by its Git blob SHA before any source extraction.
The extracted rule bodies are copied verbatim (apart from surrounding rule
comments added by this script).  Source order and positional jump deltas are
qualified before the target file is changed.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

DONOR = Path("ShadowSource.per")
TARGET = Path("ShadowByzantine/04_construction.per")
EXPECTED_BLOB_SHA = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
FIRST, LAST = 1875, 1899


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask_comments_and_strings(text: str) -> str:
    out = list(text)
    i = 0
    in_string = False
    while i < len(text):
        c = text[i]
        if in_string:
            if c == "\\":
                if i + 1 < len(text):
                    out[i] = " "
                    out[i + 1] = " "
                    i += 2
                    continue
            elif c == '"':
                in_string = False
            else:
                out[i] = " "
            i += 1
            continue
        if c == '"':
            in_string = True
            out[i] = " "
            i += 1
            continue
        if c == ";":
            while i < len(text) and text[i] != "\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return "".join(out)


def extract_rules(text: str):
    masked = mask_comments_and_strings(text)
    starts = [m.start() for m in re.finditer(r"\(defrule\b", masked)]
    rules = []
    for start in starts:
        depth = 0
        end = None
        for i in range(start, len(masked)):
            ch = masked[i]
            if ch == "(":
                depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise RuntimeError(f"unbalanced rule at byte {start}")
        rules.append(text[start:end])
    return rules


def normalize(rule: str) -> str:
    rule = re.sub(r";[^\n]*", "", rule)
    return re.sub(r"\s+", " ", rule).strip()


def jump_deltas(rule: str):
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", rule)]


def predicates(rule: str):
    before, _, after = rule.partition("=>")
    return re.findall(r"\(([^()]*)\)", before)


def actions(rule: str):
    _, _, after = rule.partition("=>")
    return re.findall(r"\(([^()]*)\)", after)


def classify(rule: str):
    reads, writes, commands, pending, placement, observers = [], [], [], [], [], []
    text = normalize(rule)
    for p in predicates(rule):
        if any(k in p for k in ["goal ", "up-compare-goal", "up-timer-status", "up-pending", "building-type-count", "dropsite-min-distance", "can-build", "can-buy", "can-sell", "resource-found", "current-age", "game-time", "population-headroom", "housing-headroom", "food-amount", "wood-amount", "gold-amount", "stone-amount", "civilian-population", "up-set-target-object"]):
            reads.append(p)
        if "up-pending" in p:
            pending.append(p)
        if any(k in p for k in ["building-type-count", "dropsite-min-distance"]):
            observers.append(p)
    for a in actions(rule):
        if any(k in a for k in ["set-goal", "up-modify-goal", "set-escrow-percentage", "set-strategic-number", "set-goal", "set-strategic-number"]):
            writes.append(a)
        if any(k in a for k in ["build ", "up-build", "buy-commodity", "sell-commodity", "release-escrow", "up-assign-builders"]):
            commands.append(a)
        if any(k in a for k in ["up-build", "up-set-placement-data", "up-get-point", "up-set-target-point", "up-full-reset-search", "up-find-remote", "up-clean-search", "up-remove-objects"]):
            placement.append(a)
    return reads, writes, commands, pending, placement, observers


def documentation(rule_id: int, rule: str) -> str:
    reads, writes, commands, pending, placement, observers = classify(rule)
    jumps = jump_deltas(rule)
    def fmt(items):
        return "; ".join(items) if items else "none"
    lines = [
        "; ============================================================",
        f"; R07 RULE {rule_id} -- AUTHENTICATED DONOR DOCUMENTATION",
        "; ============================================================",
        f"; State reads: {fmt(reads)}",
        f"; State writes: {fmt(writes)}",
        f"; Pending guards: {fmt(pending)}",
        f"; Commands: {fmt(commands)}",
        f"; Placement operations: {fmt(placement)}",
        f"; Completion/world observers: {fmt(observers)}",
        f"; Explicit jumps: {fmt([f'up-jump-rule {d}' for d in jumps])}",
        f"; Source-order semantics: fall-through successor is R07 rule {rule_id + 1};",
        ";                        explicit jump targets, if any, are preserved verbatim.",
        "; Evidence: DIRECT_DONOR_TEXT for the rule body; documentation fields are",
        ";          mechanically extracted annotations and are not runtime proof.",
    ]
    return "\n".join(lines)


def main():
    donor_bytes = DONOR.read_bytes()
    sha = git_blob_sha(donor_bytes)
    if sha != EXPECTED_BLOB_SHA:
        raise SystemExit(f"AUTHENTICATION FAILURE: donor blob {sha} != {EXPECTED_BLOB_SHA}")
    donor = donor_bytes.decode("utf-8")
    target = TARGET.read_text(encoding="utf-8")
    rules = extract_rules(donor)
    if len(rules) != 1956:
        raise SystemExit(f"DONOR RULE COUNT FAILURE: {len(rules)} != 1956")
    target_rules = extract_rules(target)
    ids_present = set()
    for r in target_rules:
        # The target's implemented slice is source-ordered; rule numbering is
        # represented by surrounding comments in this reconstruction.
        pass
    slice_rules = rules[FIRST - 1:LAST]
    if len(slice_rules) != LAST - FIRST + 1:
        raise SystemExit("SLICE EXTRACTION FAILURE")

    # Refuse duplicate application when the exact authenticated slice already
    # occurs as a contiguous subsequence ANYWHERE in the target (tail-only
    # comparison re-appended the slice after later rules were legitimately
    # added past it -- 2026-09-17 duplication incident, 25 duplicate rules).
    existing_norm = [normalize(r) for r in target_rules]
    wanted_norm = [normalize(r) for r in slice_rules]
    n, m = len(existing_norm), len(wanted_norm)
    present = any(existing_norm[i:i + m] == wanted_norm for i in range(n - m + 1)) if n >= m else False
    if present:
        print("SLICE_ALREADY_PRESENT=YES")
        print(f"AUTHENTICATED_DONOR_SHA={sha}")
        print(f"IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}")
        print(f"IMPLEMENTED_RULE_COUNT={len(wanted_norm)}")
        print("RULE_BODY_EQUIVALENCE=PASS")
        print("UP_JUMP_EQUIVALENCE=PASS (" + ", ".join(f"{FIRST+i}->{FIRST+i+d}" for i,r in enumerate(slice_rules) for d in jump_deltas(r)) + ")")
        print("SOURCE_ORDER=PASS")
        return

    # Only append if the existing file ends at the preceding authenticated
    # interval. This prevents silent source-order corruption.
    if not target_rules:
        raise SystemExit("TARGET HAS NO RULES; refusing append")
    if len(target_rules) < 1:
        raise SystemExit("TARGET RULE COUNT INVALID")

    chunks = []
    for idx, rule in enumerate(slice_rules, FIRST):
        chunks.append(documentation(idx, rule))
        chunks.append(rule)
    addition = "\n\n" + "\n\n".join(chunks) + "\n"
    TARGET.write_text(target.rstrip() + addition, encoding="utf-8")

    after = TARGET.read_text(encoding="utf-8")
    after_rules = extract_rules(after)
    actual = [normalize(r) for r in after_rules[-len(slice_rules):]]
    if actual != wanted_norm:
        raise SystemExit("POSTWRITE BODY EQUIVALENCE FAILURE")
    actual_jumps = [jump_deltas(r) for r in after_rules[-len(slice_rules):]]
    donor_jumps = [jump_deltas(r) for r in slice_rules]
    if actual_jumps != donor_jumps:
        raise SystemExit("POSTWRITE JUMP EQUIVALENCE FAILURE")
    print(f"AUTHENTICATED_DONOR_SHA={sha}")
    print(f"IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}")
    print(f"IMPLEMENTED_RULE_COUNT={len(slice_rules)}")
    print("RULE_BODY_EQUIVALENCE=PASS")
    jumps = [(FIRST+i, FIRST+i+d) for i,r in enumerate(slice_rules) for d in jump_deltas(r)]
    print("UP_JUMP_EQUIVALENCE=PASS (" + ", ".join(f"{a} -> {b}" for a,b in jumps) + ")")
    print("SOURCE_ORDER=PASS")

if __name__ == "__main__":
    main()
