import os,json
from mgz.fast.header import parse
from mgz.fast import meta
from mgz.fast import operation
from mgz.fast.enums import Operation
P=r'C:\Users\justh\Games\Age of Empires 2 DE\76561198093432383\savegame\rec.aoe2record'; O=r'C:\Users\justh\Desktop\AiByz\docs\forensics'; os.makedirs(O,exist_ok=True)
U={4:'Archer',7:'Skirmisher',38:'Berserk',83:'Villager',93:'Spearman',125:'Monk',128:'Trade Cart',329:'Camel Rider',448:'Scout Cavalry',1258:'Battering Ram',1755:'Camel Scout'}; B={12:'Barracks',49:'Siege Workshop',50:'Farm',70:'House',79:'Watch Tower',82:'Castle',87:'Archery Range',101:'Stable',103:'Blacksmith',109:'Town Center',209:'University'}
def S(x):
 if isinstance(x,(bytes,bytearray)): return x.hex()
 if isinstance(x,dict): return {str(k):S(v) for k,v in x.items()}
 if isinstance(x,(list,tuple)): return [S(v) for v in x]
 try: json.dumps(x); return x
 except: return repr(x)
def T(m): return f'{m//60000}:{m%60000//1000:02d}.{m%1000:03d}'
r=[]; f=open(P,'rb'); parse(f); meta(f); now=0
while f.tell()<os.path.getsize(P):
 try:o,p=operation(f)
 except:break
 if o is Operation.SYNC and isinstance(p,tuple): now+=p[0]
 elif o is Operation.ACTION and isinstance(p,tuple) and len(p)==2:
  a,d=p
  if isinstance(d,dict) and d.get('player_id') in (1,7):
   u=d.get('unit_id'); b=d.get('building_id'); r.append({'timestamp_ms':int(now),'player_id':d['player_id'],'event_type':getattr(a,'name',str(a)),'unit_id':u,'unit_name':U.get(u),'building_id':b,'building_name':B.get(b),'research_id':d.get('research_id'),'research_name':None,'raw_payload':S(d)})
json.dump(r,open(O+r'\2026-09-13_replay_45-57_raw_commands.json','w',encoding='utf8'),indent=2)
v=[x for x in r if x['player_id']==1 and x['event_type']=='MAKE' and x['unit_id']==83]
L=['# P1 Villager Production Timeline','', 'Evidence class: DIRECT.','', '| # | Timestamp | Interval (s) | Cumulative command-derived villagers | Classification |','|---:|---:|---:|---:|---|']; prev=None
for i,x in enumerate(v,1):
 q=None if prev is None else (x['timestamp_ms']-prev)/1000; c='UNKNOWN' if q is None else 'NORMAL_25S' if q<=25.5 else 'GAP_MINOR' if q<=40 else 'GAP_MAJOR' if q<=90 else 'GAP_CRITICAL'; L.append(f"|{i}|{T(x['timestamp_ms'])}|{'—' if q is None else f'{q:.3f}'}|{3+i}|{c}|"); prev=x['timestamp_ms']
L+=['','## Summary',f'- Villager MAKE commands: **{len(v)}**','- Starting villagers: **3**','- Statistics high-water mark: **71**','- Command-derived total: **{3+len(v)}**; discrepancy: **2**','', '## GAP_MAJOR/GAP_CRITICAL']
prev=None
for i,x in enumerate(v,1):
 q=None if prev is None else (x['timestamp_ms']-prev)/1000
 if q and q>40:L.append(f'- #{i}: {T(prev)} → {T(x["timestamp_ms"])} = {q:.3f}s')
 prev=x['timestamp_ms']
L+=['','## INTENTIONAL_AGEUP','- Feudal completion ~20:28.16; Castle completion ~39:51.00.','- No gap is automatically classified INTENTIONAL_AGEUP without direct research evidence.']
open(O+r'\2026-09-13_p1_villager_timeline.md','w',encoding='utf8').write('\n'.join(L)+'\n')

b=[x for x in r if x['player_id']==1 and x['event_type']=='BUILD']; L=['# P1 Building Event Timeline','', 'Evidence class: DIRECT. Completion/destruction/peak simultaneous state is ABSENT.','', '|#|Timestamp|ID|Building|Action|x|y|Cumulative placements|','|---:|---:|---:|---|---|---:|---:|---:|']; C={}
for i,x in enumerate(b,1):
 n=x['building_name'] or 'UNRESOLVED'; C[n]=C.get(n,0)+1; p=x['raw_payload']; L.append(f"|{i}|{T(x['timestamp_ms'])}|{x['building_id']}|{n}|PLACED|{p.get('x','—')}|{p.get('y','—')}|{C[n]}|")
L+=['','## Summary']+[f'- {n}: placements {q}; completions ABSENT; destructions ABSENT; peak simultaneous ABSENT.' for n,q in sorted(C.items())]
open(O+r'\2026-09-13_p1_building_timeline.md','w',encoding='utf8').write('\n'.join(L)+'\n')
open(O+r'\2026-09-13_p1_resource_trajectory.csv','w',encoding='utf8').write('timestamp_ms,timestamp_readable,food,wood,gold,stone,population,population_cap\n# ABSENT: replay parse exposes command stream, not historical resource/population snapshots; no interpolation.\n')
open(O+r'\2026-09-13_p1_hunting_evidence.md','w',encoding='utf8').write('# P1 Hunting Evidence\n\nEvidence class: ABSENT. No reliable huntable kill/carcass/assignment events are exposed by this parse.\n')
rr=[x for x in r if x['player_id']==1 and x['event_type'] in ('RESEARCH','RESEARCH_START','RESEARCH_COMPLETE','AGE_UP')]; L=['# P1 Research and Age-Up Timeline','', 'Evidence class: DIRECT/ABSENT.','', '|#|Timestamp|Research ID|Research|Event|Food|Gold|Wood|','|---:|---:|---:|---|---|---:|---:|---:|']
for i,x in enumerate(rr,1):L.append(f"|{i}|{T(x['timestamp_ms'])}|{x['research_id'] or '—'}|{x['research_name'] or 'UNRESOLVED'}|{x['event_type']}|—|—|—|")
if not rr:L.append('|—|—|—|ABSENT|No native research events decoded|—|—|—|')
open(O+r'\2026-09-13_p1_research_timeline.md','w',encoding='utf8').write('\n'.join(L)+'\n')

L=['# Transition Window 26:41.850 → 27:07.192','', 'Evidence class: COMPOSED.','', '## P1 events 26:30–27:30','', '|Timestamp|Event|Unit|Building|','|---:|---|---|---|']
for x in r:
 if x['player_id']==1 and 1590000<=x['timestamp_ms']<=1650000:L.append(f"|{T(x['timestamp_ms'])}|{x['event_type']}|{x['unit_name'] or '—'} ({x['unit_id'] or '—'})|{x['building_name'] or '—'} ({x['building_id'] or '—'})|")
L+=['','## P7 cross-reference','', '|Timestamp|Event|Unit|Building|','|---:|---|---|---|']
for x in r:
 if x['player_id']==7 and 1590000<=x['timestamp_ms']<=1650000:L.append(f"|{T(x['timestamp_ms'])}|{x['event_type']}|{x['unit_name'] or '—'} ({x['unit_id'] or '—'})|{x['building_name'] or '—'} ({x['building_id'] or '—'})|")
L+=['','## Classification','**UNKNOWN** — required historical resource, completion, and TC-state snapshots are absent.']
open(O+r'\2026-09-13_transition_26-41_to_27-07.md','w',encoding='utf8').write('\n'.join(L)+'\n')
def cnt(p,e,u=None,b=None):return sum(1 for x in r if x['player_id']==p and x['event_type']==e and (u is None or x['unit_id']==u) and (b is None or x['building_id']==b))
M=[('Villager MAKE events','MAKE',83,None),('Archer MAKE events','MAKE',4,None),('Skirmisher MAKE events','MAKE',7,None),('Spearman MAKE events','MAKE',93,None),('Trade cart MAKE events','MAKE',128,None),('Farm BUILD events','BUILD',None,50),('House BUILD events','BUILD',None,70),('Barracks BUILD events','BUILD',None,12),('Archery Range BUILD events','BUILD',None,87),('Stable BUILD events','BUILD',None,101)]; L=['# P1 vs Japanese Comparative Summary','', 'Evidence class: COMPOSED.','', '|Metric|P1|P7|Ratio|','|---|---:|---:|---:|']
for n,e,u,bid in M:
 a,z=cnt(1,e,u,bid),cnt(7,e,u,bid);L.append(f'|{n}|{a}|{z}|{a/z:.3f}| ' if z else f'|{n}|{a}|{z}|—|')
L+=['','## Age progression','|Age|P1|P7|Delta|','|---|---:|---:|---:|','|Feudal|20:28.16|11:46.38|+8:41.78|','|Castle|39:51.00|24:05.43|+15:45.57|','|Imperial|not observed|not observed|—|','', 'Resource collection: ABSENT from replay parse; statistics values not fabricated.']
open(O+r'\2026-09-13_p1_vs_japanese_summary.md','w',encoding='utf8').write('\n'.join(L)+'\n')

open(O+r'\2026-09-13_discrepancies.md','w',encoding='utf8').write('# Replay Reconciliation Report\n\nEvidence class: DIRECT/COMPOSED.\n\n- Villagers: 66 MAKE; +3 start = 69; statistics high-water mark 71; difference 2.\n- Archer unit_id=4; Skirmisher unit_id=7; both preserved separately.\n- Player 1 Archery Range BUILD commands: 3; House BUILD commands: 12. BUILD is cumulative placement command count, not simultaneous state.\n- Earlier 12-range figure was an ID attribution error: 70=House, 87=Archery Range.\n')
open(O+r'\2026-09-13_evidence_index.md','w',encoding='utf8').write('# AEGIS 45:57 Replay Evidence Index\n\n|Artifact|Location|Evidence Class|Supports|\n|---|---|---|---|\n|Raw command stream|./2026-09-13_replay_45-57_raw_commands.json|DIRECT|All downstream analyses|\n|Villager timeline|./2026-09-13_p1_villager_timeline.md|DIRECT|Gap classification|\n|Resource trajectory|./2026-09-13_p1_resource_trajectory.csv|ABSENT|Resource classification|\n|Building timeline|./2026-09-13_p1_building_timeline.md|DIRECT|Infrastructure timing|\n|Research timeline|./2026-09-13_p1_research_timeline.md|DIRECT/ABSENT|Age-up/research|\n|Hunting evidence|./2026-09-13_p1_hunting_evidence.md|ABSENT|Food-source diagnosis|\n|Transition analysis|./2026-09-13_transition_26-41_to_27-07.md|COMPOSED|Fix hypothesis|\n|Comparative summary|./2026-09-13_p1_vs_japanese_summary.md|COMPOSED|Diagnosis|\n|Discrepancies|./2026-09-13_discrepancies.md|DIRECT/COMPOSED|Evidence discipline|\n|This index|./2026-09-13_evidence_index.md|—|Navigation|\n\nNo .per files modified; no deployment; no test game.\n')
print('DONE',len(r),len(v),len(b),len(rr))
