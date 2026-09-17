#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
IMPLEMENTATION = ROOT / "ShadowByzantine" / "04_construction.per"
CONSTANTS = ROOT / "ShadowByzantine" / "01_constants.per"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
EXPECTED_DONOR_RULES = 1956
FIRST = 1794
LAST = 1956
R07_LAST = 1896
KNOWN_JUMPS = {1795: 1, 1850: 4, 1891: 5}
COMPAT_CONSTANTS = (
    "with-escrow", "without-escrow", "place-control", "place-point",
    "MILL", "ESKIRMS", "FletchingNumber", "goal", "gl-enemy-strategy",
    "gl-town-safe", "DRUSH", "SIEGE"
)
STATE_SYMBOLS = (
    "gl-current-build-item", "gl-build-progress", "gl-progression-pause",
    "gl-escrow-state", "SPLIT", "gl-strategy", "gl-target-age",
    "gl-target-age-checking", "gl-target-score1", "gl-target-score2",
)


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
        depth=0; end=None
        for i in range(s,len(m)):
            if m[i]=='(': depth+=1
            elif m[i]==')':
                depth-=1
                if depth==0: end=i+1; break
        if end is None: raise SystemExit(f"UNBALANCED_RULE_AT={s}")
        out.append(text[s:end])
    return out


def norm(rule: str) -> str:
    return re.sub(r"\s+", " ", mask(rule)).strip()


def jumps(rule: str) -> list[int]:
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", norm(rule))]


def jump_edges(rule_list: list[str], first: int) -> list[tuple[int,int,int]]:
    edges=[]
    for i,rule in enumerate(rule_list):
        rid=first+i
        for delta in jumps(rule): edges.append((rid,rid+delta,delta))
    return edges


def consts(text: str) -> dict[str,str]:
    found={}
    for m in re.finditer(r"\(defconst\s+([^\s()]+)\s+([^()\s]+)\)", mask(text)):
        found[m.group(1)] = m.group(2)
    return found


def const_locations(root: Path) -> dict[str,list[tuple[str,str]]]:
    result={}
    for path in root.rglob("*.per"):
        if path.name == "ShadowSource.per": continue
        try: text=path.read_text(encoding="utf-8")
        except UnicodeDecodeError: continue
        for name,value in consts(text).items():
            result.setdefault(name,[]).append((str(path.relative_to(root)),value))
    return result


def halves(rule: str) -> tuple[str,str]:
    masked = mask(rule)
    if "=>" not in masked:
        return norm(rule), ""
    left, right = rule.split("=>", 1)
    return norm(left), norm(right)


def disable_self(rule: str) -> bool:
    return "(disable-self)" in norm(rule)


def state_touches(rule: str) -> dict[str,str]:
    n = norm(rule)
    out={}
    for symbol in STATE_SYMBOLS:
        reads = bool(re.search(rf"\b{re.escape(symbol)}\b", n))
        writes = bool(re.search(rf"\((?:set-goal|up-modify-goal)\s+{re.escape(symbol)}\b", n))
        if reads or writes:
            out[symbol] = f"read={'YES' if reads else 'NO'},write={'YES' if writes else 'NO'}"
    return out


def main() -> None:
    sb=SOURCE.read_bytes(); ib=IMPLEMENTATION.read_text(encoding="utf-8"); cb=CONSTANTS.read_text(encoding="utf-8")
    sha=blob(sb)
    if sha != EXPECTED_BLOB: raise SystemExit(f"DONOR_SHA_MISMATCH={sha}")
    sr=rules(sb.decode("utf-8")); ir=rules(ib)
    if len(sr)!=EXPECTED_DONOR_RULES: raise SystemExit(f"DONOR_RULE_COUNT_MISMATCH={len(sr)}")
    expected=LAST-FIRST+1
    if len(ir)!=expected: raise SystemExit(f"IMPLEMENTATION_RULE_COUNT_MISMATCH={len(ir)} EXPECTED={expected}")

    donor=sr[FIRST-1:LAST]
    mismatches=[rid for rid,(d,i) in enumerate(zip(donor,ir),FIRST) if norm(d)!=norm(i)]
    if mismatches: raise SystemExit(f"RULE_BODY_MISMATCHES={mismatches}")

    predicate_mismatches=[]; action_mismatches=[]; disable_mismatches=[]
    for rid,(d,i) in enumerate(zip(donor,ir),FIRST):
        dp,da=halves(d); ip,ia=halves(i)
        if dp != ip: predicate_mismatches.append(rid)
        if da != ia: action_mismatches.append(rid)
        if disable_self(d) != disable_self(i): disable_mismatches.append(rid)
    if predicate_mismatches: raise SystemExit(f"PREDICATE_MISMATCHES={predicate_mismatches}")
    if action_mismatches: raise SystemExit(f"ACTION_MISMATCHES={action_mismatches}")
    if disable_mismatches: raise SystemExit(f"DISABLE_SELF_MISMATCHES={disable_mismatches}")

    donor_jumps=jump_edges(donor,FIRST); impl_jumps=jump_edges(ir,FIRST)
    if donor_jumps!=impl_jumps: raise SystemExit(f"JUMP_MISMATCH_DONOR={donor_jumps}_IMPLEMENTATION={impl_jumps}")
    expected_jumps=[(rid,rid+delta,delta) for rid,delta in KNOWN_JUMPS.items()]
    if donor_jumps!=expected_jumps: raise SystemExit(f"UNEXPECTED_DONOR_JUMP_TOPOLOGY={donor_jumps}")
    if any(src<FIRST or src>LAST or dst<FIRST or dst>LAST for src,dst,_ in donor_jumps): raise SystemExit(f"JUMP_TARGET_OUTSIDE_INTERVAL={donor_jumps}")
    fallthrough=[(rid,rid+1) for rid in range(FIRST,LAST)]
    cross_in=(FIRST-1,FIRST); cross_out=(LAST,LAST+1)
    if [x for x in donor_jumps if x[0]<FIRST or x[0]>LAST or x[1]<FIRST or x[1]>LAST]: raise SystemExit("CROSS_BOUNDARY_JUMP_PRESENT")

    donor_consts=consts(sb.decode("utf-8")); impl_consts=consts(ib); registry_consts=consts(cb); locations=const_locations(ROOT)
    print("COMPATIBILITY_CONSTANT_AUDIT_BEGIN")
    for name in COMPAT_CONSTANTS:
        if name not in impl_consts: raise SystemExit(f"MISSING_IMPLEMENTATION_COMPAT_CONSTANT={name}")
        iv=impl_consts[name]; dv=donor_consts.get(name); rv=registry_consts.get(name); loc=locations.get(name,[])
        if dv is not None and iv==dv: classification="DIRECT_DONOR_TEXT"
        elif dv is not None: classification="ERROR_VALUE_DIFFERS_FROM_DONOR"
        elif rv is not None and iv==rv: classification="REGISTRY_MATCH_NO_DIRECT_DONOR_DEFINITION"
        else: classification="UNRESOLVED_ENGINE_OR_PROJECT_SYMBOL"
        print(f"COMPAT_CONSTANT {name} implementation={iv} donor={dv if dv is not None else 'ABSENT'} registry={rv if rv is not None else 'ABSENT'} class={classification} repository_defs={loc}")
    print("COMPATIBILITY_CONSTANT_AUDIT_END")

    duplicate_defs={name:vals for name,vals in locations.items() if len(vals)>1}
    print(f"PROJECT_DUPLICATE_DEFCONST_NAMES={len(duplicate_defs)}")
    for name in sorted(duplicate_defs): print(f"DUPLICATE_DEFCONST {name} definitions={duplicate_defs[name]}")

    for symbol in STATE_SYMBOLS:
        d_count=sum(symbol in state_touches(r) for r in donor)
        i_count=sum(symbol in state_touches(r) for r in ir)
        if d_count != i_count: raise SystemExit(f"STATE_TOUCH_COUNT_MISMATCH {symbol} donor={d_count} implementation={i_count}")
        print(f"STATE_TOUCH_COUNT {symbol} donor={d_count} implementation={i_count}")

    print(f"AUTHENTICATED_DONOR_SHA={sha}")
    print(f"DONOR_RULE_COUNT={len(sr)}")
    print(f"DONOR_INTERVAL={FIRST}-{LAST}")
    print(f"R07_BOUNDARY={FIRST}-{R07_LAST}")
    print(f"POST_R07_INTERVAL={R07_LAST+1}-{LAST}")
    print(f"IMPLEMENTATION_RULE_COUNT={len(ir)}")
    print("RULE_IDENTITY=PASS (source-order identity)")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print("PREDICATE_EQUIVALENCE=PASS")
    print("ACTION_EQUIVALENCE=PASS")
    print("DISABLE_SELF_EQUIVALENCE=PASS")
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

if __name__ == "__main__": main()
