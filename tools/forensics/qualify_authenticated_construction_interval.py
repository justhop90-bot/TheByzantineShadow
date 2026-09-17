#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
IMPLEMENTATION = ROOT / "ShadowByzantine" / "04_construction.per"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
EXPECTED_DONOR_RULES = 1956
FIRST = 1794
LAST = 1949
R07_LAST = 1896
KNOWN_JUMPS = {1795: 1, 1850: 4, 1891: 5}


def blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask(text: str) -> str:
    out = list(text)
    i = 0
    quoted = False
    escaped = False
    while i < len(text):
        c = text[i]
        if quoted:
            if c == "\\" and not escaped:
                out[i] = " "
                escaped = True
            elif c == '"' and not escaped:
                out[i] = " "
                quoted = False
                escaped = False
            else:
                if c not in "\r\n":
                    out[i] = " "
                escaped = False
            i += 1
            continue
        if c == '"':
            out[i] = " "
            quoted = True
            i += 1
            continue
        if c == ';':
            while i < len(text) and text[i] not in "\r\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return "".join(out)


def rules(text: str) -> list[str]:
    m = mask(text)
    starts = [x.start() for x in re.finditer(r"\(defrule\b", m)]
    out: list[str] = []
    for s in starts:
        depth = 0
        end = None
        for i in range(s, len(m)):
            if m[i] == '(':
                depth += 1
            elif m[i] == ')':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise SystemExit(f"UNBALANCED_RULE_AT={s}")
        out.append(text[s:end])
    return out


def norm(rule: str) -> str:
    return re.sub(r"\s+", " ", mask(rule)).strip()


def jumps(rule: str) -> list[int]:
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", norm(rule))]


def jump_edges(rule_list: list[str], first: int) -> list[tuple[int, int, int]]:
    edges: list[tuple[int, int, int]] = []
    for i, rule in enumerate(rule_list):
        rid = first + i
        for delta in jumps(rule):
            edges.append((rid, rid + delta, delta))
    return edges


def main() -> None:
    sb = SOURCE.read_bytes()
    ib = IMPLEMENTATION.read_text(encoding="utf-8")
    sha = blob(sb)
    if sha != EXPECTED_BLOB:
        raise SystemExit(f"DONOR_SHA_MISMATCH={sha}")

    sr = rules(sb.decode("utf-8"))
    ir = rules(ib)
    if len(sr) != EXPECTED_DONOR_RULES:
        raise SystemExit(f"DONOR_RULE_COUNT_MISMATCH={len(sr)}")

    expected = LAST - FIRST + 1
    if len(ir) != expected:
        raise SystemExit(
            f"IMPLEMENTATION_RULE_COUNT_MISMATCH={len(ir)} EXPECTED={expected}"
        )

    donor = sr[FIRST - 1 : LAST]
    mismatches: list[int] = []
    for rid, (d, i) in enumerate(zip(donor, ir), FIRST):
        if norm(d) != norm(i):
            mismatches.append(rid)
    if mismatches:
        raise SystemExit(f"RULE_BODY_MISMATCHES={mismatches}")

    donor_jumps = jump_edges(donor, FIRST)
    impl_jumps = jump_edges(ir, FIRST)
    if donor_jumps != impl_jumps:
        raise SystemExit(
            f"JUMP_MISMATCH_DONOR={donor_jumps}_IMPLEMENTATION={impl_jumps}"
        )

    if [x[:2] for x in donor_jumps] != [
        (rid, rid + delta) for rid, delta in KNOWN_JUMPS.items()
    ]:
        raise SystemExit(f"UNEXPECTED_DONOR_JUMP_TOPOLOGY={donor_jumps}")

    if any(src < FIRST or src > LAST or dst < FIRST or dst > LAST for src, dst, _ in donor_jumps):
        raise SystemExit(f"JUMP_TARGET_OUTSIDE_INTERVAL={donor_jumps}")

    fallthrough = [(rid, rid + 1) for rid in range(FIRST, LAST)]
    cross_in = (FIRST - 1, FIRST)
    cross_out = (LAST, LAST + 1)
    cross_jump_edges = [
        (src, dst, delta)
        for src, dst, delta in donor_jumps
        if src < FIRST or src > LAST or dst < FIRST or dst > LAST
    ]

    if cross_jump_edges:
        raise SystemExit(f"CROSS_BOUNDARY_JUMP_PRESENT={cross_jump_edges}")

    print(f"AUTHENTICATED_DONOR_SHA={sha}")
    print(f"DONOR_RULE_COUNT={len(sr)}")
    print(f"DONOR_INTERVAL={FIRST}-{LAST}")
    print(f"R07_BOUNDARY={FIRST}-{R07_LAST}")
    print(f"POST_R07_INTERVAL={R07_LAST + 1}-{LAST}")
    print(f"IMPLEMENTATION_RULE_COUNT={len(ir)}")
    print("RULE_IDENTITY=PASS (source-order identity)")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print("PREDICATE_ACTION_SEQUENCE=PASS")
    print("UP_JUMP_EQUIVALENCE=PASS")
    print(f"EXPLICIT_JUMP_EDGE_COUNT={len(donor_jumps)}")
    print(f"EXPLICIT_JUMP_EDGES={donor_jumps}")
    print(f"FALL_THROUGH_EDGE_COUNT={len(fallthrough)}")
    print(f"CROSS_BOUNDARY_FALL_THROUGH={cross_in},{cross_out}")
    print("CROSS_BOUNDARY_EXPLICIT_JUMPS=NONE")
    print("SOURCE_ORDER=PASS")
    print("NO_MISSING_RULES=PASS")
    print("NO_UNEXPECTED_RULES=PASS")
    print("DUPLICATE_RULE_IDS=NONE")
    print("PARSER_BALANCE=PASS")
    print("STATIC_DONOR_EQUIVALENCE=PASS")
    print("RUNTIME_SEMANTICS=NOT_PROVEN")
    print("RUNTIME_QUALIFICATION=PENDING")


if __name__ == "__main__":
    main()
