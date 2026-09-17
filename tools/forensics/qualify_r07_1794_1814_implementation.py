#!/usr/bin/env python3
from __future__ import annotations
import hashlib,re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
SOURCE=ROOT/'ShadowSource.per'; IMPLEMENTATION=ROOT/'ShadowByzantine'/'04_construction.per'
EXPECTED_BLOB='70a18a3b69e8ea46bd5132673fe9fcf8a36595ee'; FIRST=1794; LAST=1849

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
        if end is None: out.append((start,None,text[start:start+160])); continue
        out.append((start,end,text[start:end]))
    return out
def norm(rule): return re.sub(r'\s+',' ',mask_source(rule)).strip()
def jumps(rule): return [int(x) for x in re.findall(r'\(up-jump-rule\s+(-?\d+)\)',norm(rule))]
def main():
    sb=SOURCE.read_bytes();
    if blob(sb)!=EXPECTED_BLOB: raise SystemExit('DONOR SHA MISMATCH')
    sr=extract(sb.decode()); impl_text=IMPLEMENTATION.read_text(); ir=extract(impl_text)
    raw=len(re.findall(r'\(defrule\b',impl_text))
    print(f'SOURCE_PARSED={len(sr)} IMPLEMENTATION_PARSED={len(ir)} IMPLEMENTATION_RAW_DEFRULE={raw}')
    if len(ir)!=LAST-FIRST+1:
        for n,(start,end,text) in enumerate(ir,1):
            first=re.sub(r'\s+',' ',text[:100]).strip()
            print(f'IMPL_PARSED_{n}: end={end} {first}')
        raise SystemExit('IMPLEMENTATION RULE COUNT MISMATCH')
    ds=sr[FIRST-1:LAST]; bad=[]
    for o,(d,i) in enumerate(zip(ds,ir),FIRST):
        if d[1] is None or i[1] is None or norm(d[2])!=norm(i[2]): bad.append(o)
    if bad: raise SystemExit(f'RULE BODY MISMATCHES: {bad}')
    dj=[j for r in ds for j in jumps(r[2])]; ij=[j for r in ir for j in jumps(r[2])]
    if dj!=ij: raise SystemExit(f'JUMP MISMATCH: donor={dj}, implementation={ij}')
    print(f'AUTHENTICATED_DONOR_SHA={blob(sb)}'); print(f'IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}'); print(f'IMPLEMENTED_RULE_COUNT={len(ir)}'); print('RULE_BODY_EQUIVALENCE=PASS'); print(f'UP_JUMP_EQUIVALENCE=PASS ({len(ij)} jumps)'); print('SOURCE_ORDER=PASS'); print('STATIC_R07_1794_1849_QUALIFICATION=PASS')
if __name__=='__main__': main()
