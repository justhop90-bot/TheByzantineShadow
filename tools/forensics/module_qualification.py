#!/usr/bin/env python3
"""Consolidated static qualification pipeline for ShadowByzantine modules."""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "tools" / "forensics" / "module_qualification.json"
BUILTINS={"defrule","defconst","up-jump-rule","disable-self","true","false","and","or","not","goal","set-goal","up-modify-goal","strategic-number","set-strategic-number","up-build","build","up-research","research","up-modify-escrow","set-escrow-percentage","release-escrow","can-build","can-build-with-escrow","can-train-with-escrow","can-research-with-escrow","research-pending","up-pending-objects","up-pending-placement"}
STATE=["gl-current-build-item","gl-build-progress","gl-progression-pause","gl-escrow-state","SPLIT","gl-strategy","gl-target-age","gl-target-age-checking","gl-target-score1","gl-target-score2"]
ESCROW=["can-build-with-escrow","can-train-with-escrow","can-research-with-escrow","set-escrow-percentage","up-modify-escrow","release-escrow"]
@dataclass
class Rule:
    id:int; text:str; line:int

def mask(text):
    out=list(text); i=0; q=False; e=False
    while i<len(text):
        c=text[i]
        if q:
            if c=="\\" and not e: out[i]=" "; e=True
            elif c=='"' and not e: out[i]=" "; q=False
            else:
                if c not in "\r\n": out[i]=" "
                e=False
            i+=1; continue
        if c=='"': out[i]=" "; q=True; i+=1; continue
        if c==';':
            while i<len(text) and text[i] not in "\r\n": out[i]=" "; i+=1
            continue
        i+=1
    return "".join(out)

def parse_rules(text):
    m=mask(text); starts=[x.start() for x in re.finditer(r"\(defrule\b",m)]; out=[]
    for rid,s in enumerate(starts,1):
        depth=0; end=None
        for i in range(s,len(m)):
            if m[i]=='(': depth+=1
            elif m[i]==')':
                depth-=1
                if depth==0: end=i+1; break
        if end is None: raise ValueError(f"UNBALANCED_RULE_AT={s}")
        out.append(Rule(rid,text[s:end],m.count("\n",0,s)+1))
    return out

def norm(s): return re.sub(r"\s+"," ",mask(s)).strip()
def sha_blob(data): return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()
def sha256(text): return hashlib.sha256(text.encode()).hexdigest()
def consts(text): return {m.group(1):m.group(2) for m in re.finditer(r"\(defconst\s+([^\s()]+)\s+([^()\s]+)\)",mask(text))}
def jumps(r): return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)",norm(r.text))]
def tokens(r): return set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_-]*\b",mask(r.text)))
def state_counts(rs): return {s:sum(s in tokens(r) for r in rs) for s in STATE}
def escrow_counts(rs): return {s:sum(s in norm(r.text) for r in rs) for s in ESCROW}
def slice_rules(rs,a,b): return [Rule(i,rs[i-1].text,rs[i-1].line) for i in range(a,b+1)]

def qualify(name,path,text,donor,spec,repo_defs,external_state_symbols):
    rs=parse_rules(text); local=consts(text); declared=set(local)|set(repo_defs)|set(external_state_symbols)
    unresolved=sorted(t for r in rs for t in tokens(r) if (t.startswith("gl-") or t=="SPLIT") and t not in declared)
    edges=[]; bad=[]
    for r in rs:
        for d in jumps(r):
            edges.append([r.id,r.id+d,d])
            if r.id+d<1 or r.id+d>len(rs): bad.append([r.id,r.id+d,d])
    out={"module":name,"implementation":str(path.relative_to(ROOT)),"implementation_sha256":sha256(text),"implementation_rule_count":len(rs),"parser_balance":"PASS","jump_edges":edges,"out_of_module_jumps":bad,"symbol_audit":{"unresolved_state_symbols":unresolved,"status":"PASS" if not unresolved else "FAIL"},"state_touch_counts":state_counts(rs),"escrow_primitive_counts":escrow_counts(rs),"runtime_qualification":"NOT_PROVEN","evidence_class":"STATIC_FORENSIC_EXTRACTION"}
    if spec:
        a,b=spec["donor_start"],spec["donor_end"]; ds=slice_rules(donor,a,b)
        dev=set(spec.get("allowed_deviations",[]))
        body=[] if len(rs)==len(ds) else list(range(a,min(b,a+len(rs)-1)+1))
        if len(rs)==len(ds): body=[a+i for i,(x,y) in enumerate(zip(ds,rs)) if (a+i) not in dev and norm(x.text)!=norm(y.text)]
        de=[]
        for r in ds:
            for d in jumps(r): de.append([r.id,r.id+d,d])
        ie=[[x[0]+a-1,x[1]+a-1,x[2]] for x in edges]
        parity={s:{"donor":sum(s in tokens(r) for r in ds),"implementation":sum(s in tokens(r) for r in rs)} for s in spec.get("state_symbols",STATE)}
        for x in parity.values(): x["pass"]=x["donor"]==x["implementation"]
        out.update({"donor_mapping":{"start":a,"end":b,"label":spec.get("label","")},"donor_rule_count":len(ds),"rule_count_match":len(rs)==len(ds),"rule_body_mismatches":body,"predicate_action_equivalence":"PASS" if len(rs)==len(ds) and not body else "FAIL","donor_jump_edges":de,"implementation_jump_edges":ie,"jump_topology_equivalence":"PASS" if de==ie else "FAIL","state_touch_parity":parity,"state_touch_equivalence":"PASS" if all(x["pass"] for x in parity.values()) else "FAIL","static_donor_equivalence":"PASS" if len(rs)==len(ds) and not body and de==ie and all(x["pass"] for x in parity.values()) else "FAIL"})
    return out

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--config",default=str(DEFAULT_CONFIG)); ap.add_argument("--out",default="artifacts/module-qualification"); args=ap.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8")); out=ROOT/args.out; out.mkdir(parents=True,exist_ok=True)
    source=ROOT/cfg.get("donor_source","ShadowSource.per"); donor_text=source.read_text(encoding="utf-8"); donor=parse_rules(donor_text); actual=sha_blob(donor_text.encode())
    if cfg.get("donor_blob_sha") and cfg["donor_blob_sha"]!=actual: raise SystemExit(f"DONOR_BLOB_SHA_MISMATCH expected={cfg['donor_blob_sha']} actual={actual}")
    if cfg.get("donor_rule_count") and cfg["donor_rule_count"]!=len(donor): raise SystemExit(f"DONOR_RULE_COUNT_MISMATCH expected={cfg['donor_rule_count']} actual={len(donor)}")
    external_state_symbols=cfg.get("external_state_symbols",[])
    if not isinstance(external_state_symbols,list) or not all(isinstance(x,str) and x for x in external_state_symbols):
        raise SystemExit("INVALID_EXTERNAL_STATE_SYMBOLS: expected a list of non-empty strings")
    repo_defs={}
    for p in ROOT.rglob("*.per"):
        if p==source: continue
        try: cs=consts(p.read_text(encoding="utf-8"))
        except UnicodeDecodeError: continue
        for k,v in cs.items(): repo_defs.setdefault(k,[]).append((str(p.relative_to(ROOT)),v))
    summaries=[]; configured=set()
    if not isinstance(configured,set): raise SystemExit("INTERNAL_CONFIGURED_TYPE_REGRESSION: configured must be a set")
    for spec in cfg.get("modules",[]):
        if not isinstance(spec,dict) or "implementation" not in spec or "name" not in spec:
            raise SystemExit("INVALID_MODULE_SPEC: each configured module must be an object containing name and implementation")
        implementation=spec["implementation"]
        if not isinstance(implementation,str) or not implementation:
            raise SystemExit("INVALID_MODULE_SPEC: implementation must be a non-empty string")
        configured.add(implementation)
        p=ROOT/implementation
        if not p.exists(): summaries.append({"module":spec["name"],"implementation":implementation,"status":"MISSING_IMPLEMENTATION"}); continue
        summaries.append(qualify(spec["name"],p,p.read_text(encoding="utf-8"),donor,spec,repo_defs,external_state_symbols))
    root=ROOT/"ShadowByzantine"
    for p in sorted(root.glob("*.per")):
        rel=str(p.relative_to(ROOT))
        if rel not in configured: summaries.append(qualify(p.stem,p,p.read_text(encoding="utf-8"),donor,{},repo_defs,external_state_symbols))
    (out/"donor_rule_index.json").write_text(json.dumps({"source":str(source.relative_to(ROOT)),"git_blob_sha1":actual,"rule_count":len(donor),"rules":[{"id":r.id,"line":r.line,"normalized":norm(r.text)} for r in donor]},indent=2)+"\n",encoding="utf-8")
    (out/"repository_symbol_index.json").write_text(json.dumps(dict(sorted(repo_defs.items())),indent=2)+"\n",encoding="utf-8")
    for s in summaries: (out/(s["module"].replace('/','_')+".json")).write_text(json.dumps(s,indent=2)+"\n",encoding="utf-8")
    failed=[s for s in summaries if s.get("status")=="MISSING_IMPLEMENTATION" or s.get("symbol_audit",{}).get("status")=="FAIL" or s.get("out_of_module_jumps") or s.get("static_donor_equivalence")=="FAIL"]
    md=["# Module Qualification Report v0.1","","## Evidence boundary","Static qualification only. Runtime command acceptance, pending state, world-state completion, progression, escrow release, recovery, replay equivalence, and competitive performance remain unproven.","",f"Donor: `{source.relative_to(ROOT)}`",f"Git blob SHA-1: `{actual}`",f"Rule count: `{len(donor)}`","","## Modules","","| Module | Rules | Symbols | Jumps | Donor parity | Runtime |","|---|---:|---|---|---|---|"]
    for s in summaries: md.append(f"| {s['module']} | {s.get('implementation_rule_count','-')} | {s.get('symbol_audit',{}).get('status','-')} | {'FAIL' if s.get('out_of_module_jumps') else 'PASS'} | {s.get('static_donor_equivalence','UNMAPPED')} | {s.get('runtime_qualification','NOT_PROVEN')} |")
    md += ["",f"**Pipeline status:** {'FAIL' if failed else 'PASS'}","", "Artifacts: donor_rule_index.json, repository_symbol_index.json, one JSON report per module."]
    (out/"MODULE_QUALIFICATION_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print(f"DONOR_BLOB_SHA1={actual}"); print(f"DONOR_RULE_COUNT={len(donor)}"); print(f"MODULE_COUNT={len(summaries)}"); print(f"FAILED_MODULES={len(failed)}"); print(f"REPORT={out/'MODULE_QUALIFICATION_REPORT.md'}")
    return 1 if failed else 0
if __name__=="__main__": sys.exit(main())
