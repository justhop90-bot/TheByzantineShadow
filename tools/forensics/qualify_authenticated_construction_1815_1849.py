#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
IMPLEMENTATION = ROOT / "ShadowByzantine" / "04_construction.per"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
EXPECTED_RULES = 1956
FIRST = 1815
LAST = 1849


def blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask_source(text: str) -> str:
    out = list(text); i = 0; n = len(text); ins = False; esc = False
    while i < n:
        c = text[i]
        if ins:
            if c == "\\" and not esc: out[i] = " "; esc = True
            elif c == '"' and not esc: out[i] = " "; ins = False; esc = False
            else:
                if c not in "\r\n": out[i] = " "
                esc = False
            i += 1; continue
        if c == '"': out[i] = " "; ins = True; i += 1; continue
        if c == ';':
            while i < n and text[i] not in "\r\n": out[i] = " "; i += 1
            continue
        i += 1
    return "".join(out)


def extract(text: str) -> list[str]:
    masked = mask_source(text); starts = [m.start() for m in re.finditer(r"\(defrule\b", masked)]; out = []
    for start in starts:
        depth = 0; end = None
        for i in range(start, len(masked)):
            if masked[i] == '(': depth += 1
            elif masked[i] == ')':
                depth -= 1
                if depth == 0: end = i + 1; break
        if end is None: raise SystemExit(f"UNBALANCED_DEFRULE_AT={start}")
        out.append(text[start:end])
    return out


def norm(rule: str) -> str:
    return re.sub(r"\s+", " ", mask_source(rule)).strip()


def jumps(rule: str) -> list[int]:
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", norm(rule))]


def main() -> None:
    sb = SOURCE.read_bytes(); source_sha = blob(sb)
    if source_sha != EXPECTED_BLOB: raise SystemExit(f"DONOR_SHA_MISMATCH={source_sha}")
    sr = extract(sb.decode("utf-8")); ir = extract(IMPLEMENTATION.read_text(encoding="utf-8"))
    if len(sr) != EXPECTED_RULES: raise SystemExit(f"DONOR_RULE_COUNT_MISMATCH={len(sr)}")
    expected = LAST - FIRST + 1
    impl_slice = ir[21:21 + expected]
    if len(impl_slice) != expected: raise SystemExit(f"IMPLEMENTATION_SLICE_COUNT_MISMATCH={len(impl_slice)} EXPECTED={expected}")
    ds = sr[FIRST - 1:LAST]
    bad = [rid for rid, (d, i) in enumerate(zip(ds, impl_slice), FIRST) if norm(d) != norm(i)]
    if bad: raise SystemExit(f"RULE_BODY_MISMATCHES={bad}")
    dj = [j for r in ds for j in jumps(r)]; ij = [j for r in impl_slice for j in jumps(r)]
    if dj != ij: raise SystemExit(f"JUMP_MISMATCH_DONOR={dj}_IMPLEMENTATION={ij}")
    print(f"AUTHENTICATED_DONOR_SHA={source_sha}")
    print(f"DONOR_RULE_COUNT={len(sr)}")
    print(f"IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}")
    print(f"IMPLEMENTED_RULE_COUNT={len(impl_slice)}")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print(f"UP_JUMP_EQUIVALENCE=PASS count={len(ij)}")
    print("SOURCE_ORDER=PASS")
    print("STATIC_CONSTRUCTION_1815_1849_QUALIFICATION=PASS")
    print("RUNTIME_QUALIFICATION=PENDING")


if __name__ == "__main__": main()
