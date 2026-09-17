#!/usr/bin/env python3
import csv, hashlib, json, re, sys
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else 'ShadowSource.per')
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else 'shadow-jump-graph-out')
OUT.mkdir(parents=True, exist_ok=True)
raw = SRC.read_bytes()
text = raw.decode('utf-8')
EXPECTED_GIT_BLOB_SHA = '70a18a3b69e8ea46bd5132673fe9fcf8a36595ee'
git_blob_sha = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
raw_sha = hashlib.sha1(raw).hexdigest()
if git_blob_sha != EXPECTED_GIT_BLOB_SHA:
    raise SystemExit(f'authenticated Git blob SHA mismatch: {git_blob_sha} != {EXPECTED_GIT_BLOB_SHA}')

# up-jump-rule is a signed rule delta. For 1-based forensic ordinals:
# target = source ordinal + signed delta. Fall-through = source ordinal + 1.
def mask_source(s):
    out=list(s); i=0; n=len(s); in_str=False; escaped=False
    while i<n:
        c=s[i]
        if in_str:
            if c=='\\' and not escaped: out[i]=' '; escaped=True
            elif c=='"' and not escaped: out[i]=' '; in_str=False; escaped=False
            else:
                if c not in '\r\n': out[i]=' '
                escaped=False
            i+=1; continue
        if c=='"': out[i]=' '; in_str=True; i+=1; continue
        if c==';':
            while i<n and s[i] not in '\r\n': out[i]=' '; i+=1
            continue
        i+=1
    return ''.join(out)
masked=mask_source(text)
starts=[m.start() for m in re.finditer(r'\(defrule\b', masked)]
def end_of_rule(start):
    depth=0; i=start
    while i<len(masked):
        c=masked[i]
        if c=='(': depth+=1
        elif c==')':
            depth-=1
            if depth==0: return i+1
        i+=1
    raise ValueError(f'unbalanced defrule at char {start}')
def line(pos): return text.count('\n', 0, pos) + 1
def byte(pos): return len(text[:pos].encode('utf-8'))
def normalize(body):
    body = re.sub(r'\s+', ' ', body).strip()
    m = re.match(r'^\(defrule\s*(.*?)\s*=>\s*(.*?)\)$', body, re.S)
    return (m.group(1).strip(), m.group(2).strip()) if m else (body, '')
TARGETS = ['gl-build-progress','gl-current-build-item','gl-progression-pause','gl-strategy','SPLIT','set-escrow-percentage','up-modify-escrow','release-escrow','disable-self','building-type-count','building-type-count-total','research-completed','research-status','research-available','can-research-with-escrow','can-build-with-escrow','can-train-with-escrow']
rules=[]
for ordinal,start in enumerate(starts,1):
    end=end_of_rule(start); body=text[start:end]; pred,actions=normalize(body)
    jumps=re.findall(r'\(up-jump-rule\s+([^\)]+)\)', body)
    refs=[t for t in TARGETS if re.search(r'\b'+re.escape(t)+r'\b',body)]
    rules.append(dict(ordinal=ordinal,byte_start=byte(start),byte_end_exclusive=byte(end),source_line_start=line(start),source_line_end=line(end),jump_targets_raw=jumps,fall_through_ordinal=ordinal+1 if ordinal<len(starts) else None,keywords=refs,predicate=pred,actions=actions))
by={r['ordinal']:r for r in rules}
assert len(rules)==1956
jump_rules=[r for r in rules if r['jump_targets_raw']]
assert len(jump_rules)==188
edges=[]
for r in rules:
    if r['fall_through_ordinal'] is not None: edges.append((r['ordinal'],r['fall_through_ordinal'],'fall-through',''))
    for raw_delta in r['jump_targets_raw']:
        delta=int(float(raw_delta)); target=r['ordinal']+delta
        if not 1<=target<=len(rules): raise ValueError((r['ordinal'],delta,target))
        edges.append((r['ordinal'],target,'up-jump-rule',str(delta)))
seed={r['ordinal'] for r in rules if r['keywords']}
node_set=set(seed)
for o in seed:
    r=by[o]
    if r['fall_through_ordinal'] is not None: node_set.add(r['fall_through_ordinal'])
    for d in r['jump_targets_raw']: node_set.add(o+int(float(d)))

def write_csv(path, rows, fields):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=fields); w.writeheader(); w.writerows(rows)
full_fields=['edge_id','source_ordinal','source_byte_start','source_byte_end_exclusive','source_line_start','source_line_end','source_predicate','source_actions','edge_type','jump_delta','target_ordinal','target_byte_start','target_byte_end_exclusive','target_line_start','target_line_end']
full_rows=[]
for i,(s,t,typ,d) in enumerate(edges,1):
    a,b=by[s],by[t]; full_rows.append(dict(edge_id=i,source_ordinal=s,source_byte_start=a['byte_start'],source_byte_end_exclusive=a['byte_end_exclusive'],source_line_start=a['source_line_start'],source_line_end=a['source_line_end'],source_predicate=a['predicate'],source_actions=a['actions'],edge_type=typ,jump_delta=d,target_ordinal=t,target_byte_start=b['byte_start'],target_byte_end_exclusive=b['byte_end_exclusive'],target_line_start=b['source_line_start'],target_line_end=b['source_line_end']))
write_csv(OUT/'ShadowSource_jump_fallthrough_graph.csv',full_rows,full_fields)
sub_fields=['edge_id','source_ordinal','source_is_target_seed','source_target_hits','source_byte_start','source_line_start','edge_type','jump_delta','target_ordinal','target_is_target_seed','target_target_hits','target_byte_start','target_line_start']
sub_rows=[]
for i,(s,t,typ,d) in enumerate([e for e in edges if e[0] in node_set],1):
    a,b=by[s],by[t]; sub_rows.append(dict(edge_id=i,source_ordinal=s,source_is_target_seed=s in seed,source_target_hits=';'.join(a['keywords']),source_byte_start=a['byte_start'],source_line_start=a['source_line_start'],edge_type=typ,jump_delta=d,target_ordinal=t,target_is_target_seed=t in seed,target_target_hits=';'.join(b['keywords']),target_byte_start=b['byte_start'],target_line_start=b['source_line_start']))
write_csv(OUT/'ShadowSource_targeted_subgraph.csv',sub_rows,sub_fields)

def q(s): return '"'+str(s).replace('\\','\\\\').replace('"','\\"').replace('\n','\\n').replace('\r','')+'"'
def dot(path,node_ids,edge_rows,targeted=False):
    with path.open('w',encoding='utf-8') as f:
        f.write('digraph ShadowSource {\n  rankdir=LR;\n  graph [label="ShadowSource rule control-flow graph", labelloc=t, fontsize=18];\n  node [shape=box, fontsize=8];\n')
        for o in sorted(node_ids):
            r=by[o]; label='R%s\\nL%s-%s\\nB%s-%s' % (o,r['source_line_start'],r['source_line_end'],r['byte_start'],r['byte_end_exclusive'])
            if targeted and o in seed: label += '\\nTARGET: '+','.join(r['keywords'])
            f.write('  r%d [label=%s%s];\n' % (o,q(label),',penwidth=2' if targeted and o in seed else ''))
        seen=set()
        for s,t,typ,d in edge_rows:
            if s not in node_ids: continue
            key=(s,t,typ)
            if key in seen: continue
            seen.add(key)
            attrs='style=bold,label='+q('jump '+d) if typ=='up-jump-rule' else 'label="fall-through"'
            f.write('  r%d -> r%d [%s];\n' % (s,t,attrs))
        f.write('}\n')
dot(OUT/'ShadowSource_jump_fallthrough_graph.dot',set(by),edges)
dot(OUT/'ShadowSource_targeted_subgraph.dot',node_set,[e for e in edges if e[0] in node_set],True)
meta=dict(expected_git_blob_sha1=EXPECTED_GIT_BLOB_SHA,actual_git_blob_sha1=git_blob_sha,raw_content_sha1=raw_sha,byte_length=len(raw),rule_count=len(rules),jump_bearing_rules=len(jump_rules),jump_edge_count=len(jump_rules),fall_through_edge_count=len(rules)-1,total_edge_count=len(edges),jump_target_min=min(o+int(float(d)) for o,t,typ,d in edges if typ=='up-jump-rule'),jump_target_max=max(o+int(float(d)) for o,t,typ,d in edges if typ=='up-jump-rule'),target_seed_rule_count=len(seed),targeted_node_count_with_1hop_context=len(node_set),targeted_edge_count=len([e for e in edges if e[0] in node_set]),resolution='target ordinal = source ordinal + signed up-jump-rule operand; fall-through = source ordinal + 1',target_keywords=TARGETS)
(OUT/'ShadowSource_jump_graph_metadata.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
print(json.dumps(meta,indent=2))
