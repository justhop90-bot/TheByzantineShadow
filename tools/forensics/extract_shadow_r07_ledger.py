#!/usr/bin/env python3
import csv, hashlib, re, sys
from pathlib import Path

SRC=Path(sys.argv[1] if len(sys.argv)>1 else 'ShadowSource.per')
OUT=Path(sys.argv[2] if len(sys.argv)>2 else 'shadow-r07-ledger.csv')
EXPECTED='70a18a3b69e8ea46bd5132673fe9fcf8a36595ee'
raw=SRC.read_bytes(); text=raw.decode('utf-8')
gitsha=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
if gitsha!=EXPECTED: raise SystemExit(f'authenticated Git blob SHA mismatch: {gitsha} != {EXPECTED}')

def mask(s):
    a=list(s); i=0; ins=False; esc=False
    while i<len(s):
        c=s[i]
        if ins:
            if c=='\\' and not esc: a[i]=' '; esc=True
            elif c=='"' and not esc: a[i]=' '; ins=False
            elif c not in '\r\n': a[i]=' '
            esc=False; i+=1; continue
        if c=='"': a[i]=' '; ins=True; i+=1; continue
        if c==';':
            while i<len(s) and s[i] not in '\r\n': a[i]=' '; i+=1
            continue
        i+=1
    return ''.join(a)
masked=mask(text)
starts=[m.start() for m in re.finditer(r'\(defrule\b',masked)]
def endrule(p):
    d=0
    for i in range(p,len(masked)):
        if masked[i]=='(': d+=1
        elif masked[i]==')':
            d-=1
            if d==0:return i+1
    raise SystemExit('unbalanced rule')
def ln(p): return text.count('\n',0,p)+1
def byte(p): return len(text[:p].encode())
def split(body):
    m=re.match(r'^\(defrule\s*(.*?)\s*=>\s*(.*?)\)$',body,re.S)
    return (m.group(1).strip(),m.group(2).strip()) if m else (body,'')
rules=[]
for n,p in enumerate(starts,1):
    e=endrule(p); pred,act=split(text[p:e]);
    jumps=re.findall(r'\(up-jump-rule\s+([^\)]+)\)',text[p:e])
    rules.append(dict(id=n,start=ln(p),end=ln(e),byte_start=byte(p),byte_end=byte(e),pred=pred,act=act,jumps=jumps,disable=bool(re.search(r'\(disable-self\b',act))))
if len(rules)!=1956: raise SystemExit(f'rule count {len(rules)} != 1956')
by={r['id']:r for r in rules}

def hits(r,rx): return sorted(set(re.findall(rx,r['pred']+'\n'+r['act'])))
def lines(rx,s): return [x.strip() for x in s.splitlines() if re.search(rx,x)]
state_rx=r'\((?:goal|up-compare-goal|set-goal|up-modify-goal)\s+([^\s\)]+)'
obj_rx=r'\((?:building-type-count-total|building-type-count|up-pending-objects|can-build|can-build-with-escrow)\s+([^\s\)]+)'
for r in rules[1793:1896]:
    r['fall']=r['id']+1 if r['id']<1956 else ''
    r['jtargets']=[]
    for rawdelta in r['jumps']:
        delta=int(float(rawdelta)); r['jtargets'].append(r['id']+delta)
    r['states']=hits(r,state_rx)
    r['objects']=hits(r,obj_rx)
    r['writes']=lines(r'\((?:set-goal|up-modify-goal|set-escrow-percentage|up-modify-escrow|release-escrow|set-strategic-number|set-goal)',r['act'])
    r['commands']=lines(r'^\s*\((?:build|up-build|up-assign-builders|up-set-placement-data|up-full-reset-search|up-find-|up-set-target-object|up-get-|up-remove-|set-strategic-number)',r['act'])
    r['escrow']=lines(r'\((?:set-escrow-percentage|up-modify-escrow|release-escrow|up-build[^\n]*gl-escrow-state)',r['act'])
    r['placement']=lines(r'\((?:up-build\s+place-|up-set-placement-data|set-strategic-number\s+sn-placement)',r['act'])
    r['completion']=lines(r'\((?:building-type-count-total|building-type-count|research-status|research-completed|up-pending-objects)',r['pred'])
    r['milestone']=lines(r'\((?:building-type-count-total|building-type-count)\s+[^\n]*\s*(?:>=|==)',r['pred'])

fields=['rule_id','source_lines','byte_range','predicates','writes','commands','jump_targets','fall_through_successor','state_dependencies','object_dependencies','milestones','completion_observers','escrow_operations','placement_operations','disable_self']
with OUT.open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=fields); w.writeheader()
    for r in rules[1793:1896]:
        w.writerow({'rule_id':r['id'],'source_lines':f"{r['start']}-{r['end']}",'byte_range':f"{r['byte_start']}-{r['byte_end']}",'predicates':r['pred'].replace('\n',' | '),'writes':' || '.join(r['writes']),'commands':' || '.join(r['commands']),'jump_targets':';'.join(map(str,r['jtargets'])),'fall_through_successor':r['fall'],'state_dependencies':';'.join(r['states']),'object_dependencies':';'.join(r['objects']),'milestones':' || '.join(r['milestone']),'completion_observers':' || '.join(r['completion']),'escrow_operations':' || '.join(r['escrow']),'placement_operations':' || '.join(r['placement']),'disable_self':r['disable']})
print(f'R07 ledger: rules=103, source=20920-22200, git_blob_sha={gitsha}, output={OUT}')
