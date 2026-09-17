#!/usr/bin/env python3
from __future__ import annotations
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
TARGET = ROOT / "ShadowByzantine" / "04_construction.per"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
FIRST, LAST = 1850, 1874

DOC = {
1850: "Control-flow jump: reads no persistent state; writes none; command is up-jump-rule 4; no pending/placement/completion observer; explicit jump target resolves to 1854.",
1851: "Reads gl-progression-pause, gl-current-build-item, can-build-with-escrow(lumber-camp); writes wood escrow percentage=0; escrow releases wood; command build lumber-camp; no pending guard or placement operation; no completion observer in this rule.",
1852: "Reads gl-strategy, gl-build-progress, lumber-camp count; writes gl-build-progress=LC4Number for skipped-state reconciliation; no escrow, pending, placement, or command; lumber-camp<4 is reconciliation evidence.",
1853: "Reads gl-strategy, gl-current-build-item, gl-build-progress; writes gl-current-build-item=LC4 and wood escrow percentage=LOW-ESCROW; no pending/placement/command; no completion observer.",
1854: "Reads gl-current-build-item and lumber-camp count; writes gl-build-progress+=1; no escrow/pending/placement/command; lumber-camp>=4 is the completion/progression observer.",
1855: "Reads time, gl-strategy, lumber-camp timer status/distance and gl-escrow-state via up-can-build; writes dropsite separation, placement mode through up-build, adjacent-dropsite policy, and timer t-lc; placement operation is place-normal lumber-camp; no pending guard; command is up-build place-normal; no completion observer.",
1856: "Reads food amount, commodity-buy feasibility, gold amount and gl-build-progress; writes no persistent AI state; command buy-commodity food; no pending, placement, or completion observer.",
1857: "Reads commodity-buy feasibility, food/gold thresholds and gl-current-build-item=CUP; writes no persistent state; command buy-commodity food; no pending, placement, or completion observer.",
1858: "Reads wood amount, gold amount, gl-current-build-item and commodity-buy feasibility; writes no persistent state; command buy-commodity wood; no pending, placement, or completion observer.",
1859: "Reads gold/food amounts, commodity-sell feasibility and castle-age research status; writes no persistent state; command sell-commodity food; no pending, placement, or completion observer.",
1860: "Reads commodity-sell feasibility, gold/food thresholds and gl-current-build-item=CUP; writes no persistent state; command sell-commodity food; no pending, placement, or completion observer.",
1861: "Reads wood amount, gl-strategy=FLUSH, commodity-sell feasibility and gl-build-progress; writes no persistent state; command sell-commodity wood; no pending, placement, or completion observer.",
1862: "Reads wood amount, commodity-sell feasibility and gl-current-build-item=EXTRA-STABLES; writes no persistent state; command sell-commodity wood; no pending, placement, or completion observer.",
1863: "Reads commodity-sell feasibility, gl-current-build-item, food/gold/wood thresholds and gl-build-progress; writes no persistent state; command sell-commodity wood; no pending, placement, or completion observer.",
1864: "Reads wood/food/gold amounts, commodity-sell feasibility and gl-current-build-item=CUP; writes no persistent state; command sell-commodity wood; no pending, placement, or completion observer.",
1865: "Reads disabled false predicate, commodity-sell feasibility and food/wood/stone thresholds; writes no persistent state; command sell-commodity stone is unreachable while false remains false; no pending, placement, or completion observer.",
1866: "Reads can-build-with-escrow(mill), food resource/time, gl-current-build-item=MILL1, mill count and build-delay timer; writes adjacent-dropsite policy, wood escrow percentage=0, and timer t-build-delay; escrow releases wood; command build mill; no pending/placement; no completion observer in this rule.",
1867: "Reads gl-current-build-item=MILL1 and mill count; writes gl-build-progress+=1; no escrow/pending/placement/command; mill>=1 is the completion/progression observer.",
1868: "Reads gl-dark-build=MillFirst, mill count and gl-build-progress; writes gl-build-progress=1 for skipped-state reconciliation; no escrow/pending/placement/command; mill<1 is reconciliation evidence.",
1869: "Reads gl-dark-build=LumberFirst, mill count and gl-build-progress; writes gl-build-progress=2 for skipped-state reconciliation; no escrow/pending/placement/command; mill<1 is reconciliation evidence.",
1870: "Reads gl-current-build-item, gl-dark-build and gl-build-progress; writes wood escrow percentage=LOW-ESCROW and gl-current-build-item=MILL1; no pending/placement/command; no completion observer.",
1871: "Reads can-build(mill), food resource-found, current age and mill count; writes none persistently; command build mill followed by disable-self; no pending/placement; mill<1 is an entry guard, not completion proof.",
1872: "Reads no persistent state; writes generic goal=-12; no escrow/pending/placement/command/completion observer.",
1873: "Reads mill count; writes generic goal=-10; no escrow/pending/placement/command/completion observer.",
1874: "Reads mill count; writes generic goal=10; no escrow/pending/placement/command; mill==3 is an observed world-state threshold used to write the goal, not completion of a command in this rule.",
}

def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()

def mask(text: str) -> str:
    out=list(text); i=0; n=len(text); ins=False; esc=False
    while i<n:
        c=text[i]
        if ins:
            if c=='\\' and not esc: out[i]=' '; esc=True
            elif c=='"' and not esc: out[i]=' '; ins=False; esc=False
            else:
                if c not in '\r\n': out[i]=' '
                esc=False
            i+=1; continue
        if c=='"': out[i]=' '; ins=True; i+=1; continue
        if c==';':
            while i<n and text[i] not in '\r\n': out[i]=' '; i+=1
            continue
        i+=1
    return ''.join(out)

def extract(text: str) -> list[str]:
    m=mask(text); starts=[x.start() for x in re.finditer(r'\(defrule\b',m)]; out=[]
    for start in starts:
        depth=0
        for i in range(start,len(m)):
            if m[i]=='(': depth+=1
            elif m[i]==')':
                depth-=1
                if depth==0:
                    out.append(text[start:i+1]); break
        else: raise SystemExit(f"unbalanced defrule at {start}")
    return out

def normalize(rule: str) -> str:
    return re.sub(r'\s+',' ',mask(rule)).strip()

def main() -> None:
    sb=SOURCE.read_bytes()
    actual=blob_sha(sb)
    if actual != EXPECTED_BLOB: raise SystemExit(f"DONOR SHA MISMATCH: {actual}")
    donor=extract(sb.decode())
    if len(donor) != 1956: raise SystemExit(f"DONOR RULE COUNT MISMATCH: {len(donor)}")
    if set(DOC) != set(range(FIRST,LAST+1)): raise SystemExit("documentation map is incomplete")
    existing=TARGET.read_text()
    if "R07 RULE 1850" in existing or "R07 RULE 1874" in existing:
        print("R07 1850-1874 already present; no-op")
        return
    impl=extract(existing)
    if not impl: raise SystemExit("TARGET HAS NO DEFRULES")
    # The requested slice must attach directly to the already implemented 1849 region.
    if "R07 RULE 1849" not in existing: raise SystemExit("TARGET DOES NOT END WITH AUTHENTICATED R07 1849 REGION")
    selected=donor[FIRST-1:LAST]
    if len(selected) != LAST-FIRST+1: raise SystemExit("DONOR SLICE COUNT MISMATCH")
    block=[]
    for rid,rule in zip(range(FIRST,LAST+1),selected):
        if not rule.startswith("(defrule"): raise SystemExit(f"BAD DONOR RULE {rid}")
        block += ["", "; ============================================================", f"; R07 RULE {rid}", "; ============================================================", f"; {DOC[rid]}", rule]
    block += ["", "; ============================================================", "; R07 1850-1874 SOURCE-ORDER NOTE", "; ============================================================", "; Rules are appended in authenticated donor order. Rule 1850 is an explicit", "; up-jump-rule (+4) whose positional target is rule 1854. Rules 1851-1874", "; then proceed by normal source-order fall-through. Command issuance remains", "; distinct from world-state completion; observed building counts are the", "; completion/progression evidence where explicitly used by the donor.", ""]
    TARGET.write_text(existing.rstrip()+"\n"+"\n".join(block))
    # Exact executable equivalence against authenticated donor slice.
    new=extract(TARGET.read_text())
    new_slice=new[-(LAST-FIRST+1):]
    bad=[rid for rid,(d,i) in enumerate(zip(selected,new_slice),FIRST) if normalize(d)!=normalize(i)]
    if bad: raise SystemExit(f"RULE BODY MISMATCHES AFTER APPEND: {bad}")
    print(f"AUTHENTICATED_DONOR_SHA={actual}")
    print(f"IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}")
    print(f"IMPLEMENTED_RULE_COUNT={len(new_slice)}")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print("UP_JUMP_EQUIVALENCE=PASS (1 jump: 1850 -> 1854)")
    print("SOURCE_ORDER=PASS")

if __name__ == "__main__": main()
