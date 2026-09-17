#!/usr/bin/env python3
from __future__ import annotations
import hashlib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'ShadowSource.per'; IMPLEMENTATION=ROOT/'ShadowByzantine'/'04_construction.per'
EXPECTED_BLOB='70a18a3b69e8ea46bd5132673fe9fcf8a36595ee'; EXPECTED_RULES=1956; FIRST=1925; LAST=1949

def blob(data): return hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()
def mask_source(text):
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
def extract(text):
    masked=mask_source(text); starts=[m.start() for m in re.finditer(r'\(defrule\b',masked)]; out=[]
    for start in starts:
        depth=0; end=None
        for i in range(start,len(masked)):
            if masked[i]=='(': depth+=1
            elif masked[i]==')':
                depth-=1
                if depth==0: end=i+1; break
        if end is None: raise SystemExit(f'unbalanced defrule at {start}')
        out.append(text[start:end])
    return out
def norm(rule): return re.sub(r'\s+',' ',mask_source(rule)).strip()
def jumps(rule): return [int(x) for x in re.findall(r'\(up-jump-rule\s+(-?\d+)\)',norm(rule))]
def main():
    sb=SOURCE.read_bytes(); sha=blob(sb)
    if sha!=EXPECTED_BLOB: raise SystemExit(f'DONOR SHA MISMATCH: {sha}')
    sr=extract(sb.decode()); ir=extract(IMPLEMENTATION.read_text())
    if len(sr)!=EXPECTED_RULES: raise SystemExit(f'DONOR RULE COUNT MISMATCH: {len(sr)}')
    n=LAST-FIRST+1; impl=ir[-n:]; donor=sr[FIRST-1:LAST]
    if len(impl)!=n: raise SystemExit(f'IMPLEMENTATION SLICE COUNT MISMATCH: expected {n}, got {len(impl)}')
    bad=[r for r,(d,i) in enumerate(zip(donor,impl),FIRST) if norm(d)!=norm(i)]
    if bad: raise SystemExit(f'RULE BODY MISMATCHES: {bad}')
    dj=[j for r in donor for j in jumps(r)]; ij=[j for r in impl for j in jumps(r)]
    if dj!=ij: raise SystemExit(f'JUMP MISMATCH: donor={dj}, implementation={ij}')
    print(f'AUTHENTICATED_DONOR_SHA={sha}')
    print(f'IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}')
    print(f'IMPLEMENTED_RULE_COUNT={len(impl)}')
    print('RULE_BODY_EQUIVALENCE=PASS')
    print(f'UP_JUMP_EQUIVALENCE=PASS ({len(ij)} jumps)')
    print('SOURCE_ORDER=PASS')
    print('STATIC_R07_1925_1949_QUALIFICATION=PASS')
if __name__=='__main__': main()
