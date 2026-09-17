#!/usr/bin/env python3
"""Consolidated static qualification pipeline for ShadowByzantine modules.

Evidence boundary: this tool proves source/static properties only. It never
promotes parser acceptance, command issuance, pending state, or static
reachability into runtime/world-state qualification.
"""
from __future__ import annotations
import argparse, hashlib, json, re, sys
from dataclasses import dataclass, asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CONFIG = ROOT / "tools" / "forensics" / "module_qualification.json"

BUILTIN_WORDS = {
    "defrule","defconst","up-jump-rule","disable-self","true","false","and","or","not",
    "goal","set-goal","up-modify-goal","strategic-number","set-strategic-number",
    "up-build","build","up-research","research","up-modify-escrow","set-escrow-percentage",
    "release-escrow","can-build","can-build-with-escrow","can-train-with-escrow",
    "can-research-with-escrow","research-pending","up-pending-objects","up-pending-placement",
}
STATE_DEFAULTS = [
    "gl-current-build-item","gl-build-progress","gl-progression-pause","gl-escrow-state","SPLIT",
    "gl-strategy","gl-target-age","gl-target-age-checking","gl-target-score1","gl-target-score2",
]

@dataclass
class Rule:
    id: int
    text: str
    line: int


def mask(text: str) -> str:
    out=list(text); i=0; quoted=False; escaped=False
    while i < len(text):
        c=text[i]
        if quoted:
            if c=="\\" and not escaped: out[i]=" "; escaped=True
            elif c=='"' and not escaped: out[i]=" "; quoted=False; escaped=False
            else:
                if c not in "\r\n": out[i]=" "
                escaped=False
            i+=1; continue
        if c=='"': out[i]=" "; quoted=True; i+=1; continue
        if c==';':
            while i<len(text) and text[i] not in "\r\n": out[i]=" "; i+=1
            continue
        i+=1
    return "".join(out)


def parse_rules(text: str) -> list[Rule]:
    m=mask(text); starts=[x.start() for x in re.finditer(r"\(defrule\b",m)]; result=[]
    for rid,s in enumerate(starts,1):
        depth=0; end=None
        for i in range(s,len(m)):
            if m[i]=='(': depth+=1
            elif m[i]==')':
                depth-=1
                if depth==0: end=i+1; break
        if end is None: raise ValueError(f"unbalanced defrule at byte {s}")
        line=m.count("\n",0,s)+1
        result.append(Rule(rid,text[s:end],line))
    return result


def norm(s: str) -> str: return re.sub(r"\s+"," ",mask(s)).strip()

def blob_sha1(data: bytes) -> str: return hashlib.sha1(f"blob {len(data)}\0".encode()+data).hexdigest()

def consts(text: str) -> dict[str,str]:
    return {m.group(1):m.group(2) for m in re.finditer(r"\(defconst\s+([^\s()]+)\s+([^()\s]+)\)",mask(text))}

def jumps(rule: Rule) -> list[int]:
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)",norm(rule.text))]

def symbols_in_rule(rule: Rule) -> set[str]:
    return set(re.findall(r"\b[A-Za-z_][A-Za-z0-9_-]*\b",mask(rule.text)))

def state_touch(text: str, symbol: str) -> tuple[bool,bool]:
    n=norm(text); read=bool(re.search(rf"\b{re.escape(symbol)}\b",n))
    write=bool(re.search(rf"\((?:set-goal|up-modify-goal)\s+{re.escape(symbol)}\b",n))
    return read,write

def rule_slice(rules: list[Rule], first: int, last: int) -> list[Rule]:
    return [Rule(i, rules[i-1].text, rules[i-1].line) for i in range(first,last+1)]

def report_module(name: str, impl_path: Path, impl_text: str, donor_rules: list[Rule], spec: dict, repo_consts: dict[str,list[tuple[str,str]]]) -> dict:
    ir=parse_rules(impl_text)
    ic=consts(impl_text)
    duplicate_consts={k:v for k,v in repo_consts.items() if len(v)>1}
    local_jumps=[]; bad_jumps=[]
    for r in ir:
        for d in jumps(r):
            target=r.id+d; local_jumps.append([r.id,target,d])
            if target < 1 or target > len(ir): bad_jumps.append([r.id,target,d])
    undefined=[]
    # Conservative symbol audit: only flag calls/known declarations that are
    # locally declared or explicitly configured. Generic engine primitives are ignored.
    declared=set(ic)
    for r in ir:
        for token in symbols_in_rule(r):
            if token in BUILTIN_WORDS or token in declared: continue
            if token.startswith("gl-") or token in STATE_DEFAULTS:
                if token not in declared: undefined.append(token)
    undefined=sorted(set(undefined))
    out={
        "module":name,"implementation":str(impl_path.relative_to(ROOT)),
        "implementation_sha256":hashlib.sha256(impl_text.encode()).hexdigest(),
        "implementation_rule_count":len(ir),
        "parser_balance":"PASS",
        "duplicate_defconst_repository_count":len(duplicate_consts),
        "undefined_state_symbols":undefined,
        "local_jump_edges":local_jumps,
        "out_of_module_jumps":bad_jumps,
        "static_checks":{"parser":"PASS","jump_targets":"PASS" if not bad_jumps else "FAIL","symbol_state":"PASS" if not undefined else "FAIL"},
        "donor_mapping":spec or None,
        "evidence_class":"STATIC_FORENSIC_EXTRACTION",
        "runtime_qualification":"NOT_PROVEN",
    }
    if spec:
        first,last=spec["donor_start"],spec["donor_end"]
        ds=rule_slice(donor_rules,first,last)
        mismatches=[]
        count_match=len(ir)==len(ds)
        if count_match:
            mismatches=[first+i for i,(d,x) in enumerate(zip(ds,ir)) if norm(d.text)!=norm(x.text)]
        donor_edges=[]; impl_edges=[]
        for r in ds:
            donor_edges += [[r.id,r.id+d,d] for d in jumps(r)]
        for r in ir:
            impl_edges += [[r.id+first-1,r.id+first-1+d,d] for d in jumps(r)]
        state_parity={}
        for s in spec.get("state_symbols",STATE_DEFAULTS):
            dt=sum(1 for r in ds if s in symbols_in_rule(r)); it=sum(1 for r in ir if s in symbols_in_rule(r))
            state_parity[s]={"donor":dt,"implementation":it,"pass":dt==it}
        out.update({
            "donor_mapping":{"donor_start":first,"donor_end":last,"label":spec.get("label","")},
            "donor_rule_count":len(ds),"rule_count_match":count_match,
            "rule_body_mismatches":mismatches,
            "predicate_action_equivalence":"PASS" if not mismatches and count_match else "FAIL",
            "donor_jump_edges":donor_edges,"implementation_jump_edges":impl_edges,
            "jump_topology_equivalence":"PASS" if donor_edges==impl_edges else "FAIL",
            "state_touch_parity":state_parity,
            "state_touch_equivalence":"PASS" if all(x["pass"] for x in state_parity.values()) else "FAIL",
            "static_donor_equivalence":"PASS" if count_match and not mismatches and donor_edges==impl_edges and all(x["pass"] for x in state_parity.values()) else "FAIL",
        })
    return out


def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument("--config",default=str(DEFAULT_CONFIG)); ap.add_argument("--out",default="artifacts/module-qualification"); args=ap.parse_args()
    cfg=json.loads(Path(args.config).read_text(encoding="utf-8")); outdir=ROOT/args.out; outdir.mkdir(parents=True,exist_ok=True)
    source=ROOT/cfg.get("donor_source","ShadowSource.per"); donor_text=source.read_text(encoding="utf-8"); donor_rules=parse_rules(donor_text)
    expected_sha=cfg.get("donor_blob_sha"); actual_sha=blob_sha1(donor_text.encode())
    if expected_sha and expected_sha!=actual_sha: raise SystemExit(f"DONOR_BLOB_SHA_MISMATCH expected={expected_sha} actual={actual_sha}")
    if cfg.get("donor_rule_count") and len(donor_rules)!=cfg["donor_rule_count"]: raise SystemExit(f"DONOR_RULE_COUNT_MISMATCH expected={cfg['donor_rule_count']} actual={len(donor_rules)}")
    all_consts={}
    for p in ROOT.rglob("*.per"):
        if p==source: continue
        try: cs=consts(p.read_text(encoding="utf-8"))
        except UnicodeDecodeError: continue
        for k,v in cs.items(): all_consts.setdefault(k,[]).append((str(p.relative_to(ROOT)),v))
    modules=cfg.get("modules",[])
    seen=[]; summaries=[]
    for spec in modules:
        p=ROOT/spec["implementation"]
        if not p.exists():
            summaries.append({"module":spec["name"],"implementation":spec["implementation"],"status":"MISSING_IMPLEMENTATION"}); continue
        seen.append(spec["implementation"]); summaries.append(report_module(spec["name"],p,p.read_text(encoding="utf-8"),donor_rules,spec,all_consts))
    # Auto-discover every .per under the implementation tree, even if no donor interval is known.
    impl_root=ROOT/"ShadowByzantine"
    mapped={x["implementation"] for x in modules}
    for p in sorted(impl_root.glob("*.per")):
        rel=str(p.relative_to(ROOT))
        if rel in mapped: continue
        summaries.append(report_module(p.stem,p,p.read_text(encoding="utf-8"),donor_rules,{},all_consts))
    donor_extract=outdir/"donor_rule_index.json"
    donor_extract.write_text(json.dumps({"source":str(source.relative_to(ROOT)),"git_blob_sha1":actual_sha,"rule_count":len(donor_rules),"rules":[{"id":r.id,"line":r.line,"normalized":norm(r.text)} for r in donor_rules]},indent=2)+"\n",encoding="utf-8")
    (outdir/"repository_symbol_index.json").write_text(json.dumps({k:v for k,v in sorted(all_consts.items())},indent=2)+"\n",encoding="utf-8")
    for s in summaries: (outdir/f"{s['module'].replace('/','_')}.json").write_text(json.dumps(s,indent=2)+"\n",encoding="utf-8")
    failed=[s for s in summaries if s.get("status")=="MISSING_IMPLEMENTATION" or any(v=="FAIL" for v in s.get("static_checks",{}).values()) or s.get("static_donor_equivalence")=="FAIL"]
    md=["# Module Qualification Report v0.1","","## Evidence boundary","Static qualification only. Runtime command acceptance, pending state, world-state completion, progression, escrow release, recovery, and replay equivalence remain unproven unless independently supplied by runtime evidence.","",f"Donor: `{source.relative_to(ROOT)}`",f"Donor Git blob SHA-1: `{actual_sha}`",f"Donor rules: `{len(donor_rules)}`","", "## Modules","", "| Module | Rules | Static | Donor parity | Runtime |", "|---|---:|---|---|---|"]
    for s in summaries: md.append(f"| {s['module']} | {s.get('implementation_rule_count','-')} | {'FAIL' if s in failed else 'PASS'} | {s.get('static_donor_equivalence','UNMAPPED')} | {s.get('runtime_qualification','NOT_PROVEN')} |")
    md += ["",f"**Pipeline status:** {'FAIL' if failed else 'PASS'}","", "Generated artifacts:","- `donor_rule_index.json` — authenticated donor extraction","- `repository_symbol_index.json` — repository-wide `defconst` index","- one JSON report per module"]
    (outdir/"MODULE_QUALIFICATION_REPORT.md").write_text("\n".join(md)+"\n",encoding="utf-8")
    print("DONOR_BLOB_SHA1="+actual_sha); print("DONOR_RULE_COUNT="+str(len(donor_rules))); print("MODULE_COUNT="+str(len(summaries))); print("FAILED_MODULES="+str(len(failed))); print("REPORT="+str(outdir/"MODULE_QUALIFICATION_REPORT.md"))
    return 1 if failed else 0

if __name__=="__main__": sys.exit(main())
