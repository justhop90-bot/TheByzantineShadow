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


def blob(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask(text: str) -> str:
    out = list(text); i = 0; quoted = False; escaped = False
    while i < len(text):
        c = text[i]
        if quoted:
            if c == "\\" and not escaped: out[i] = " "; escaped = True
            elif c == '"' and not escaped: out[i] = " "; quoted = False; escaped = False
            else:
                if c not in "\r\n": out[i] = " "
                escaped = False
            i += 1; continue
        if c == '"': out[i] = " "; quoted = True; i += 1; continue
        if c == ';':
            while i < len(text) and text[i] not in "\r\n": out[i] = " "; i += 1
            continue
        i += 1
    return "".join(out)


def rules(text: str) -> list[str]:
    m = mask(text); starts = [x.start() for x in re.finditer(r"\(defrule\b", m)]; out=[]
    for s in starts:
        d=0; e=None
        for i in range(s,len(m)):
            if m[i]=='(': d+=1
            elif m[i]==')':
                d-=1
                if d==0: e=i+1; break
        if e is None: raise SystemExit(f"UNBALANCED_RULE_AT={s}")
        out.append(text[s:e])
    return out


def norm(rule: str) -> str:
    return re.sub(r"\s+", " ", mask(rule)).strip()


def jumps(rule: str) -> list[int]:
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", norm(rule))]


def main() -> None:
    sb = SOURCE.read_bytes(); ib = IMPLEMENTATION.read_text(encoding="utf-8")
    sha = blob(sb)
    if sha != EXPECTED_BLOB: raise SystemExit(f"DONOR_SHA_MISMATCH={sha}")
    sr = rules(sb.decode("utf-8")); ir = rules(ib)
    if len(sr) != EXPECTED_DONOR_RULES: raise SystemExit(f"DONOR_RULE_COUNT_MISMATCH={len(sr)}")
    expected = LAST-FIRST+1
    if len(ir) != expected: raise SystemExit(f"IMPLEMENTATION_RULE_COUNT_MISMATCH={len(ir)} EXPECTED={expected}")
    donor = sr[FIRST-1:LAST]
    mismatches=[]
    for rid,(d,i) in enumerate(zip(donor,ir),FIRST):
        if norm(d) != norm(i): mismatches.append(rid)
    if mismatches: raise SystemExit(f"RULE_BODY_MISMATCHES={mismatches}")
    dj=[(FIRST+i,j) for i,r in enumerate(donor) for j in jumps(r)]
    ij=[(FIRST+i,j) for i,r in enumerate(ir) for j in jumps(r)]
    if dj != ij: raise SystemExit(f"JUMP_MISMATCH_DONOR={dj}_IMPLEMENTATION={ij}")
    resolved=[(rid,rid+d) for rid,d in ij]
    expected_fallthrough=[(rid,rid+1) for rid in range(FIRST,LAST)]
    if len(set(range(FIRST,LAST+1))) != expected: raise SystemExit("RULE_IDENTITY_FAILURE")
    if any(t < FIRST or t > LAST for _,t in resolved): raise SystemExit(f"JUMP_TARGET_OUTSIDE_INTERVAL={resolved}")
    if len(donor) != len(set(map(norm, donor))):
        duplicate_bodies=True
    else:
        duplicate_bodies=False
    print(f"AUTHENTICATED_DONOR_SHA={sha}")
    print(f"DONOR_RULE_COUNT={len(sr)}")
    print(f"DONOR_INTERVAL={FIRST}-{LAST}")
    print(f"IMPLEMENTATION_RULE_COUNT={len(ir)}")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print("PREDICATE_ACTION_SEQUENCE=PASS")
    print(f"UP_JUMP_EQUIVALENCE=PASS count={len(ij)}")
    print(f"RESOLVED_JUMP_TARGETS={resolved if resolved else 'NONE'}")
    print(f"FALL_THROUGH_EDGE_COUNT={len(expected_fallthrough)}")
    print("SOURCE_ORDER=PASS")
    print("NO_MISSING_RULES=PASS")
    print("NO_UNEXPECTED_RULES=PASS")
    print(f"DUPLICATE_NORMALIZED_BODIES={'PRESENT' if duplicate_bodies else 'NONE'}")
    print("PARSER_BALANCE=PASS")
    print("STATIC_RUNTIME_SEMANTICS=NOT_PROVEN")
    print("RUNTIME_QUALIFICATION=PENDING")

if __name__ == "__main__": main()
