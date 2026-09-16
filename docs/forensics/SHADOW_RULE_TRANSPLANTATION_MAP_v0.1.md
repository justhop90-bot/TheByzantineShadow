# Shadow Rule-Level Transplantation Map v0.1

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical donor:** `ShadowSource.per`  
**Donor SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Machine:** 1,956 rules

## 1. Mapping rule

This map is executable-mechanism-first. A mapping is not accepted merely because the current code and donor both "do production" or "do construction". The mapped unit is the actual rule path: predicates → state writes → jumps → escrow → search/placement → command → observer → progression/re-entry.

Classes:

- **PRESERVED** — same mechanism and topology.
- **ADAPTED** — donor mechanism retained while Byzantine object/policy changes.
- **MOVED** — mechanism retained but relocated in source topology.
- **CHANGED** — mechanism exists but control/state semantics differ.
- **ADDED** — no donor executable analogue.
- **LOST** — donor mechanism absent from current runtime.
- **UNKNOWN** — exact executable correspondence not yet proven.

## 2. Exact donor construction anchors

| Donor ordinal | Donor source | Executable mechanism | Current ShadowByzantine | Classification |
|---:|---|---|---|---|
| 1764 | L20529-L20538 | `gl-progression-pause RAX2` → `can-build-with-escrow barracks` → `sn-placement-zone-size 3` → clear pause → `up-build place-control 0 barracks` | `04_construction.per` barracks rule | ADAPTED / PARTIAL |
| 1765 | L20540-L20547 | timer `t-rax` + barracks world-state guard → `up-assign-builders barracks 3` | no `up-assign-builders` equivalent | LOST |
| 1769 | L20570-L20582 | FLUSH barracks execution → wood release → placement-zone configuration → `up-build place-control` | basic `build barracks` | CHANGED |
| 1770 | L20584-L20590 | barracks world-state observation → `gl-build-progress := BarracksNumber` | no progress cursor | LOST |
| 1771 | L20592-L20600 | current-item RAX + progress checkpoint + escrow wood | no current-item/progress/escrow construction state | LOST |
| 1772 | L20602-L20609 | `building-type-count-total barracks >= 1` → `gl-build-progress + 1` | `BASIC-BARRACKS-READY` observer | CHANGED |
| 1773 | L20612-L20624 | KRUSH barracks path → escrow release → placement configuration → `up-build place-control` | basic `build barracks` | CHANGED |
| 1774 | L20626-L20632 | KRUSH barracks world-state checkpoint | no progress cursor | LOST |
| 1775 | L20634-L20641 | KRUSH current-item RAX checkpoint | no current-item state | LOST |
| 1776 | L20643-L20650 | barracks completion → `gl-build-progress + 1` | no progress cursor | LOST |
| 1794 | L20842-L20849 | farm/stable/blacksmith predicate → `up-build place-normal gl-escrow-state farm` | `04_construction.per` farm rule | ADAPTED / CHANGED |
| 1795 | L20851-L20857 | `gl-current-build-item MARKET1` / pending blacksmith / strategy guard → `up-jump-rule 1` | no jump | LOST |
| 1796 | L20859-L20871 | farm arbitration → `SPLIT 1` | basic farm rule | CHANGED |
| 1797 | L20873-L20882 | `SPLIT 1` → `SPLIT 2` after blacksmith/farm thresholds | no SPLIT state | LOST |
| 1798 | L20884-L20892 | `SPLIT 2` → escrow-aware farm build | basic farm rule | CHANGED |
| 1799 | L20894-L20899 | `gl-escrow-state := with-escrow`, `SPLIT := 0` | no equivalent state transition | LOST |
| 1800 | L20902-L20911 | farm feasibility/pending/world-state gate → `SPLIT 1` | basic farm predicate | ADAPTED / CHANGED |
| 1801 | L20913-L20923 | farm command after age/strategy/resource guard | `build farm` | ADAPTED |

**Important:** source line 20842–20849 is the preceding donor rule visible immediately before ordinal 1795 in the source-order matrix; the matrix fragment establishes the command and topology. Exact ordinal labeling of that preceding row should be regenerated from the authenticated matrix generator before treating it as a permanent numbered anchor.

## 3. Exact donor research/progression anchors

| Donor ordinal | Donor source | Mechanism | Current ShadowByzantine | Classification |
|---:|---|---|---|---|
| 1172 | L14294-L14307 | FLUSH + time/age/strategy + no progression pause + blacksmith + enemy threat → `gl-progression-pause SCALEMAIL` | no equivalent | LOST |
| 1173 | L14309-L14313 | progression pause → `up-modify-escrow food max 100` | direct Pass-1 escrow mutation, but no progression cursor | CHANGED |
| 1174 | L14315-L14324 | `can-research-with-escrow ri-scale-mail` → clear pause → zero/release food → `up-research gl-escrow-state` | no research machine | LOST |
| 1175 | L14327-L14340 | CHAINMAIL interruption admission | no equivalent | LOST |
| 1176 | L14342-L14347 | chainmail escrow mutation | no research progression | LOST |
| 1177 | L14349-L14360 | chainmail escrow-aware research + release | no research progression | LOST |
| 1178 | L14364-L14372 | KRUSH iron-casting escrow-aware research command | no research machine | LOST |
| 1179 | L14374-L14380 | research pending → progress checkpoint | no progress cursor | LOST |
| 1180 | L14382-L14389 | progress checkpoint → current item IRONCASTING | no current-item state | LOST |
| 1181 | L14391-L14400 | iron-casting escrow reallocation/release | no research escrow topology | LOST |
| 1182 | L14402-L14409 | research-pending → progress increment | no progress cursor | LOST |
| 1183–1197 | L14412-L14557 | FLUSH/KRUSH iron-casting and forging progression, escrow, release, current-item mutation and completion observation | no equivalent | LOST |

## 4. Current ShadowByzantine rule inventory

### Root / loader

`ShadowByzantine.per` is a thin root entrypoint that loads `ShadowByzantine/ShadowByzantine`. The inner file currently loads `01_constants`, `01b_byz_constants`, `02_state`, `03_economy`, `04_construction`, and `16_pass1_transaction`.

This is not donor-equivalent source order. Donor has no runtime `(load ...)` graph and no module orchestrator; it is one ordered rule program.

### 02_state

| Current rule | Mechanism | Donor correspondence | Classification |
|---|---|---|---|
| state-01 | barracks world observation → `BASIC-BARRACKS-READY 1` | donor barracks world-state completion/progression family, including 1770/1772/1776 | CHANGED |
| state-02 | barracks absent → `BASIC-ATTACK-READY 0` | no exact donor writer | ADDED |

### 03_economy

| Current rule | Mechanism | Donor correspondence | Classification |
|---|---|---|---|
| economy-01 | `can-train villager` → `train villager` | donor production command idiom, exact ordinal not yet bound | UNKNOWN / ADAPTED |
| economy-02 | one-time 60/40/0/0 gatherer SN allocation | donor gatherer/economy SN writers exist, exact rule path not yet bound | ADAPTED / UNKNOWN |

### 04_construction

| Current rule | Mechanism | Donor correspondence | Classification |
|---|---|---|---|
| construction-01 | house headroom + can-build + pending guard → `build house` | donor housing construction family; exact ordinal not yet bound | ADAPTED / UNKNOWN |
| construction-02 | no barracks state + can-build + pending guard → `build barracks` | donor 1764–1776 construction/progression family | CHANGED |
| construction-03 | barracks exists → disable-self | donor distributed self-disabling/re-entry idiom | ADAPTED |
| construction-04 | pending barracks → disable-self | donor pending/construction guard family | ADAPTED |
| construction-05 | farm feasibility + pending/world guard → `build farm` | donor 1796–1801 | CHANGED |
| construction-06/07 | barracks world observation → basic readiness goals | donor world-state completion observers | CHANGED |

### 16_pass1_transaction

| Current rule | Mechanism | Donor correspondence | Classification |
|---|---|---|---|
| pass1-01 | initialize AEGIS transaction state | donor distributed initialization, exact ordinal not bound | CHANGED / ADDED STATE |
| pass1-02 | barracks + no Spearman → objective/transaction admission | donor QUNITS admission family | UNKNOWN |
| pass1-03/04 | resource feasibility gate | donor resource feasibility predicates | ADAPTED |
| pass1-05 | `up-modify-escrow` food/wood | donor escrow mutation topology; research anchor 1173 is exact but production ordinal unknown | ADAPTED |
| pass1-06 | observe escrow → logical COMMITTED | donor physical escrow + progression state, but logical carrier is newly invented | CHANGED |
| pass1-07 | authority grant | no exact donor authority state carrier | ADDED |
| pass1-08 | `up-get-fact unit-type-count` baseline | donor observation-before-command pattern | ADAPTED |
| pass1-09 | set escrow mode | donor `gl-escrow-state` idiom | ADAPTED but carrier changed |
| pass1-10 | `up-can-train` → `up-train` Spearman | donor `can-train-with-escrow` / `up-train` production family | ADAPTED; exact donor ordinal UNKNOWN |
| pass1-11/12 | execution-issued → world-state verification | donor command/completion separation | PRESERVED principle |
| pass1-13 | world count delta → transaction complete/release request | donor world-state completion + release/re-entry pattern | CHANGED |
| pass1-14 | release command | donor `release-escrow` paths | ADAPTED |
| pass1-15 | zero escrow observation → released | donor release observation | PRESERVED principle |
| pass1-16 | released + world state → idle | donor re-entry/reassessment | CHANGED |
| pass1-17 | capital failure → authority denied | no exact donor authority carrier | ADDED |

## 5. Rule-topology findings

1. The current runtime has **no `up-jump-rule` topology**. This is a direct LOSS of donor control flow, not merely a stylistic difference.
2. The current runtime has no distributed `gl-current-build-item` / `gl-build-progress` / `gl-progression-pause` construction cursor.
3. The current runtime replaces donor distributed state with a centralized AEGIS transaction state vector.
4. The current runtime has only a narrow escrow lifecycle; donor escrow is distributed through production, research, construction, and progression paths.
5. Search and placement are largely absent from the active runtime; donor construction depends on them.
6. World-state verification is correctly distinguished from command issuance in Pass 1 and should be retained.
7. The exact donor production ordinals for the Spearman adaptation remain an explicit UNKNOWN rather than being invented.

## 6. Transplantation gate

The map is sufficient to identify what must be preserved and what is currently lost. It is **not** sufficient to claim a complete rule-by-rule donor transplantation because the current runtime contains only a small vertical slice and the donor QUNITS production interval has not yet been mechanically bound to exact ordinals in this artifact.

Therefore no donor-exact jump, production, military, raid, scouting, search, or research rule is fabricated here. The next implementation pass must mechanically bind those remaining ordinals from the authenticated source-order matrix before code is promoted.

## 7. Required topology for implementation

The implementation target is:

```text
ordered donor rule stream
  + preserved source-order fall-through
  + preserved explicit jumps
  + distributed goal/SN/timer state
  + distributed escrow/progression state
  + donor search/placement loops
  + engine commands
  + world-state observers
  + distributed recovery/re-entry
  + bounded Byzantine policy substitutions
```

A conventional controller/orchestrator/transaction-manager replacement is not an acceptable substitute.

## 8. Exact QUNITS closure — authenticated source-order binding

The following interval is now mechanically bound from the authenticated `SHADOW_SOURCE_ORDER_MATRIX_v0.3.md` and the canonical `ShadowSource.per`. These are executable donor ordinals, not conceptual unit categories.

| Ordinal | Source | Donor executable mechanism | ShadowByzantine disposition |
|---:|---|---|---|
| 1259 | L15202-L15209 | `can-train monk` + total monk `< 3` → `disable-self` + `train monk` | UNKNOWN / ADAPTED: current Pass-1 has no monk path |
| 1260 | L15211-L15218 | second independent monk train rule; same world-count admission; self-disabling | UNKNOWN / ADAPTED |
| 1261 | L15220-L15227 | third independent monk train rule; same world-count admission; self-disabling | UNKNOWN / ADAPTED |
| 1262 | L15230-L15238 | town-unsafe observation → reset search → target home → distance filter → remote archery search | LOST: no active search machine |
| 1263 | L15240-L15250 | diagnostic-disabled mangonel escrow-aware train path (`false` predicate) | LOST / NON-EXECUTING donor path |
| 1264 | L15252-L15260 | SIEGE + scorpion-count condition → direct `train mangonel-line` | UNKNOWN / LOST |
| 1265 | L15262-L15269 | diagnostic-disabled SIEGE mangonel `can-train-with-escrow` → `up-train` | LOST / NON-EXECUTING donor path |
| 1266 | L15271-L15282 | diagnostic-disabled mangonel completion threshold → zero/release wood+gold and clear SIEGE | LOST / NON-EXECUTING donor path |
| 1267 | L15284-L15292 | diagnostic-disabled siege reservation → modify wood/gold escrow | LOST / NON-EXECUTING donor path |
| 1268 | L15294-L15301 | enemy composition predicate → `up-jump-rule 1`, skipping next siege rule when condition holds | LOST: no current jump topology |
| 1269 | L15303-L15318 | diagnostic-disabled mangonel admission under SIEGE, workshop, pending-count and enemy-ranged predicates → `SIEGE 3` | LOST / NON-EXECUTING donor path |
| 1270 | L15321-L15334 | SIEGE + scorpion production admission → direct `train scorpion-line` | UNKNOWN / LOST |
| 1271 | L15337-L15347 | SIEGE RAMS arbitration → `SPLIT 1` when ram investment should pause | LOST: no donor `SPLIT` topology |
| 1272 | L15349-L15359 | `SPLIT 1` → release wood/gold; clear SIEGE and SPLIT | LOST |
| 1273 | L15361-L15368 | SIEGE RAMS + no pending siege units → reserve wood/gold escrow | LOST |
| 1274 | L15370-L15378 | `can-train-with-escrow battering-ram-line` → release wood/gold → `train battering-ram-line` | UNKNOWN / LOST: exact Byzantine analogue not implemented |
| 1275 | L15380-L15393 | observed ram count/pending/workshop/army-damage conditions → enter `SIEGE RAMS` | LOST |
| 1276 | L15397-L15407 | KRUSH + no scout cavalry → `train scout-cavalry-line`, self-disable | ADAPTED / UNKNOWN |
| 1277 | L15411-L15419 | KRUSH + `can-train knight-line` + food/pending-villager guard → `train knight-line` | UNKNOWN / ADAPTED |
| 1278 | L15422-L15431 | FLUSH knight direct production gated by progression-pause/current-item exclusions | UNKNOWN / ADAPTED |
| 1279 | L15433-L15443 | FLUSH + knight count `<4` + `can-train-with-escrow knight-line` → `up-train gl-escrow-state knight-line` | ADAPTED mechanism candidate; current Spearman slice is not equivalent |
| 1280 | L15446-L15455 | resource shortage predicate → `up-jump-rule 1` | LOST: no current jump topology |
| 1281 | L15457-L15470 | archer feasibility + count composition + age/progression guard → `up-train gl-escrow-state archer-line` | UNKNOWN / LOST |
| 1282 | L15474-L15478 | castle age reached → `gl-escrow-state := without-escrow` | LOST / changed carrier |
| 1283 | L15480-L15490 | FLUSH skirmisher suppression predicate → `up-jump-rule 2` | LOST |
| 1284 | L15492-L15502 | second skirmisher suppression predicate → `up-jump-rule 1` | LOST |
| 1285 | L15504-L15518 | GeneralSkirm admission → `SPLIT 1` after housing/worker/blacksmith/time/training guards | LOST |
| 1286 | L15520-L15530 | `SPLIT 1` → `SPLIT 2` based on superiority/skirm total/castle and elite-skirm state | LOST |
| 1287 | L15532-L15540 | `SPLIT 2` → increment `gl-skirm-total`, set escrow mode, `up-train skirmisher-line`, clear SPLIT | LOST / current state not equivalent |
| 1288 | L15542-L15547 | unconditional recovery of escrow mode to `with-escrow` and clear SPLIT | LOST |
| 1289 | L15550-L15562 | MESO + swordsman tech + target-age + monk-count → direct militia train | UNKNOWN / LOST |
| 1290 | L15566-L15579 | FLUSH feudal anti-krush/pocket spear admission → direct spear train | ADAPTED candidate; exact current Pass-1 is not topology-equivalent |
| 1291 | L15581-L15594 | timed FLUSH NORMAL emergency spear → `up-train gl-escrow-state spearman-line` | ADAPTED candidate |
| 1292 | L15596-L15609 | castle FLUSH stable/camel/knight threat → direct spear train | UNKNOWN / ADAPTED |
| 1293 | L15611-L15623 | castle FLUSH non-pocket stable threat → direct spear train | UNKNOWN / ADAPTED |
| 1294 | L15626-L15632 | KRUSH → `up-jump-rule 4`, bypassing four following spear rules | LOST |
| 1295 | L15634-L15641 | non-pocket MESO with no monk/knight → `up-jump-rule 2` | LOST |
| 1296 | L15643-L15655 | stable/target-age emergency spear condition → `up-train gl-escrow-state spearman-line` | ADAPTED candidate |
| 1297 | L15657-L15669 | early military population/time + enemy condition → direct spear train | UNKNOWN / ADAPTED |
| 1298 | L15671-L15682 | spear count/monk/knight/scout threat → direct spear train | UNKNOWN / ADAPTED |

### QUNITS topology conclusions

1. **1259–1298 is an exact donor production/control interval**, including monks, siege, scout cavalry, knights, archers, skirmishers, militia, and spears.
2. `can-train-with-escrow` and `up-train` are not isolated executor idioms; they participate in production arbitration, resource fencing, progression exclusions, and jump-based preemption.
3. The donor uses both direct `train` and escrow-aware `up-train`; the distinction is part of the control machine.
4. Completion for this interval is generally observed through unit counts/pending state rather than inferred from command issuance. The matrix explicitly records command rules separately from observation/state rules.
5. `gl-skirm-total` is a donor production-side persistent counter mutated at ordinal 1287; it is not interchangeable with an external transaction status.
6. `SPLIT` is a donor scratch/control carrier reused to stage production arbitration. It is not evidence for a generic transaction manager.
7. Ordinals 1263, 1265–1269 contain `false`-guarded diagnostic/dead paths. They are preserved in the donor atlas as source facts but must not be promoted as active Byzantine behavior.
8. The exact Spearman donor anchors are now known: **1290–1298**, with **1291 and 1296** using `up-train gl-escrow-state c: spearman-line` and **1294–1295** providing explicit preemption jumps.

## 9. QUNITS transplantation gate

The QUNITS donor interval is now closed at static source level. The current ShadowByzantine implementation remains incomplete: only the narrow Spearman Pass-1 vertical slice exists, and it does not reproduce the donor's production arbitration, `SPLIT` staging, distributed escrow, jump topology, or multi-unit production paths. Therefore QUNITS is **not yet runtime-transplanted** merely because its donor ordinals are now known.

The next code gate is to transplant these exact executable paths into the recovered ordered machine, preserving donor rule order and jump topology while replacing only unit/object choices required by the Byzantine roster. Any rule whose donor mechanism has no Byzantine analogue must be explicitly classified rather than silently replaced by a generic controller.

### A.0. Donor declaration regions (non-rule state namespace)

| Declaration region | Ordinal | Source offsets | Evidence role |
|---|---:|---|---|
| QID'S | — (declaration) | L1347–L1357 | no `defrule` ordinal; declaration/state-carrier namespace |
| QGENERAL | — (declaration) | L1358–L1400 | no `defrule` ordinal; declaration/state-carrier namespace |
| QPOSITION | — (declaration) | L1401–L1457 | no `defrule` ordinal; declaration/state-carrier namespace |
| QECONOMY | — (declaration) | L1566–L1623 | no `defrule` ordinal; declaration/state-carrier namespace |

<!-- BEGIN GENERATED RULE-LEVEL ATLAS -->

## Generated executable-mechanism atlas

Generated directly from `ShadowSource.per` (1956 rules) and the current `ShadowByzantine/**/*.per` tree (194 rules).
No donor ordinal or source offset is hard-coded in this artifact.

### A. Exact donor region boundaries

| Region | Donor ordinals | Donor source offsets |
|---|---:|---|
| UNHEADED @ L1 | 1–1 | L1–L5 |
| UNHEADED @ L7 | 2–2 | L7–L13 |
| QPOSITION @ L1401 | 3–3 | L1451–L1456 |
| QEAGOL @ L1723 | 4–11 | L1791–L1877 |
| QSETUP @ L1924 | 12–26 | L1925–L2055 |
| QADVANTAGE @ L2057 | 27–74 | L2058–L2531 |
| QNA @ L2534 | 75–87 | L2536–L2664 |
| QTARGET STUFF @ L2666 | 88–117 | L2667–L2962 |
| QUICKIES @ L2964 | 118–125 | L2967–L3040 |
| QUICKIES @ L3042 | 126–148 | L3045–L3244 |
| QMISC @ L3246 | 149–201 | L3247–L3749 |
| QMPOINTS @ L3751 | 202–234 | L3752–L4130 |
| QMINIS @ L4132 | 235–253 | L4134–L4381 |
| QHOUSES @ L4383 | 254–260 | L4384–L4472 |
| QLC @ L4474 | 261–293 | L4476–L4797 |
| QANTI-TRUSH @ L4799 | 294–299 | L4803–L4861 |
| QGARRISONING TC @ L4863 | 300–311 | L4864–L4968 |
| QVILLS @ L4970 | 312–377 | L4972–L5683 |
| QSHEEP @ L5685 | 378–390 | L5687–L5826 |
| QNEWSCOUTING @ L5828 | 391–447 | L5829–L6404 |
| QCIRCLE SCOUTING @ L6406 | 448–471 | L6407–L6713 |
| QFORAGE @ L6715 | 472–475 | L6716–L6765 |
| QCOUNTING SHEEP @ L6767 | 476–479 | L6768–L6793 |
| QDLURING @ L6795 | 480–508 | L6796–L7173 |
| QBH @ L7174 | 509–554 | L7175–L7682 |
| QRETARGETING @ L7684 | 555–580 | L7685–L7947 |
| QFORCEDROP @ L7949 | 581–592 | L7950–L8085 |
| QCLAIMING SHEEP @ L8087 | 593–606 | L8089–L8220 |
| QFARMS @ L8222 | 607–609 | L8224–L8265 |
| QARCHERS @ L8267 | 610–615 | L8269–L8336 |
| QSKIRMS @ L8338 | 616–621 | L8341–L8403 |
| QDEFENSE @ L8405 | 622–628 | L8406–L8483 |
| QMANGOS @ L8485 | 629–629 | L8486–L8499 |
| QSPEARS @ L8501 | 630–679 | L8504–L9066 |
| QSCOUT @ L9068 | 680–730 | L9070–L9608 |
| QSOD @ L9610 | 731–746 | L9611–L9763 |
| QKNIGHT GROUP @ L9765 | 747–751 | L9767–L9819 |
| QEVAL @ L9821 | 752–814 | L9822–L10479 |
| QRAIDING @ L10481 | 815–962 | L10483–L12038 |
| QRANGED MICRO @ L12040 | 963–979 | L12042–L12234 |
| QINITIALIZING GROUP @ L12236 | 980–986 | L12237–L12315 |
| QREGROUPING @ L12317 | 987–998 | L12318–L12472 |
| QMOVING @ L12474 | 999–1030 | L12480–L12795 |
| QCCR @ L12797 | 1031–1050 | L12799–L12970 |
| QTCR @ L12972 | 1051–1078 | L12974–L13229 |
| QMARCH TO ENEMY BASE @ L13231 | 1079–1131 | L13232–L13705 |
| QCOMBAT MODE @ L13707 | 1132–1140 | L13708–L13801 |
| QFAILSAFE @ L13810 | 1141–1141 | L13811–L13822 |
| QDARK @ L13824 | 1142–1144 | L13826–L13859 |
| QKRUSH @ L13861 | 1145–1153 | L13862–L13978 |
| QFLUSH @ L13980 | 1154–1163 | L13983–L14111 |
| QKNIGHTS @ L14113 | 1164–1168 | L14115–L14176 |
| QSIEGE @ L14178 | 1169–1171 | L14180–L14214 |
| QSCALEMAIL @ L14293 | 1172–1174 | L14294–L14324 |
| QCHAINMAIL @ L14326 | 1175–1177 | L14327–L14360 |
| QIRONCASTING @ L14362 | 1178–1187 | L14364–L14457 |
| QFORGING @ L14459 | 1188–1197 | L14461–L14557 |
| QCHAINBARDING @ L14559 | 1198–1207 | L14561–L14656 |
| QSCALEBARDING @ L14658 | 1208–1217 | L14660–L14760 |
| QXBOW @ L14762 | 1218–1219 | L14763–L14782 |
| QPIKES @ L14784 | 1220–1222 | L14785–L14821 |
| QAGE @ L14823 | 1223–1226 | L14825–L14866 |
| QCUP @ L14868 | 1227–1235 | L14870–L14971 |
| QFLTCH @ L14973 | 1236–1240 | L14974–L15022 |
| QLAA @ L15024 | 1241–1245 | L15025–L15070 |
| QPAA @ L15072 | 1246–1250 | L15073–L15119 |
| QBODKIN @ L15121 | 1251–1256 | L15122–L15173 |
| QLOOM @ L15175 | 1257–1258 | L15176–L15199 |
| QMONKS @ L15201 | 1259–1261 | L15202–L15227 |
| QMANGOS @ L15229 | 1262–1269 | L15230–L15318 |
| QSCORPS @ L15320 | 1270–1270 | L15321–L15334 |
| QRAMS @ L15336 | 1271–1275 | L15337–L15393 |
| QSCOUTS @ L15395 | 1276–1276 | L15397–L15407 |
| QKNIGHTS @ L15409 | 1277–1279 | L15411–L15443 |
| QARCHERS @ L15445 | 1280–1281 | L15446–L15470 |
| QSKIRMS @ L15472 | 1282–1288 | L15474–L15547 |
| QMILITIAMAN @ L15549 | 1289–1289 | L15550–L15562 |
| QSPEARS @ L15564 | 1290–1298 | L15566–L15682 |
| QTOWERS @ L15684 | 1299–1306 | L15686–L15762 |
| QSTABLE @ L15764 | 1307–1348 | L15766–L16166 |
| QMONASTERY @ L16168 | 1349–1355 | L16170–L16229 |
| QMARKET @ L16231 | 1356–1381 | L16233–L16476 |
| QANALYZING ENEMY ATTACK @ L16478 | 1382–1386 | L16479–L16525 |
| QRESIGNING @ L16527 | 1387–1395 | L16529–L16611 |
| QSUPERIORITY @ L16613 | 1396–1396 | L16614–L16622 |
| QCIVSUP @ L16624 | 1397–1397 | L16625–L16633 |
| QTSA @ L16636 | 1398–1403 | L16638–L16725 |
| QENEMY STRAT @ L16728 | 1404–1409 | L16729–L16794 |
| QCHAT @ L16797 | 1410–1415 | L16799–L16849 |
| QSTRATEGY @ L16851 | 1416–1420 | L16853–L16919 |
| QECO NUMBERS @ L16922 | 1421–1449 | L16923–L17247 |
| QUEUE @ L17245 | 1450–1463 | L17249–L17391 |
| QBECO @ L17393 | 1464–1483 | L17394–L17633 |
| QTOWN SAFETY @ L17636 | 1484–1513 | L17637–L17943 |
| QTARGET PLAYER @ L17945 | 1514–1602 | L17948–L18931 |
| QPRIORITY @ L18933 | 1603–1610 | L18934–L19030 |
| QSCOUTING @ L19032 | 1611–1615 | L19033–L19081 |
| QATTACK EFFICIENCY @ L19083 | 1616–1641 | L19084–L19297 |
| QDAMAGE POTENTIAL @ L19299 | 1642–1659 | L19300–L19459 |
| Q2BA @ L19462 | 1660–1667 | L19464–L19547 |
| QBOWSAW @ L19549 | 1668–1677 | L19551–L19647 |
| QGOLDMINING @ L19649 | 1678–1685 | L19651–L19734 |
| QGOLDSHAFT @ L19736 | 1686–1690 | L19737–L19781 |
| QHCOL @ L19784 | 1691–1698 | L19786–L19869 |
| QHEAVY PLOW @ L19871 | 1699–1703 | L19872–L19916 |
| QVILLAGERS @ L19918 | 1704–1710 | L19919–L19994 |
| QESCROW @ L19996 | 1711–1719 | L19998–L20095 |
| QTSB @ L20097 | 1720–1728 | L20100–L20186 |
| QRANGES @ L20188 | 1729–1738 | L20190–L20287 |
| QESKIRMS @ L20291 | 1739–1743 | L20292–L20337 |
| QSW @ L20339 | 1744–1757 | L20341–L20474 |
| QRAX @ L20476 | 1758–1776 | L20478–L20650 |
| QSMITH @ L20652 | 1777–1787 | L20653–L20763 |
| QCASTLES @ L20765 | 1788–1791 | L20767–L20798 |
| QFARMS @ L20800 | 1792–1814 | L20801–L21068 |
| QHOUSE @ L21070 | 1815–1827 | L21071–L21218 |
| QLC @ L21220 | 1828–1855 | L21222–L21522 |
| QTRADING @ L21524 | 1856–1865 | L21527–L21647 |
| QMILL @ L21649 | 1866–1876 | L21651–L21760 |
| QMC @ L21762 | 1877–1902 | L21766–L22095 |
| QUNIVERSITY @ L22097 | 1903–1907 | L22098–L22144 |
| QBALLISTICS @ L22146 | 1908–1912 | L22147–L22191 |
| QEND @ L22193 | 1913–1915 | L22195–L22218 |
| QMISC @ L22220 | 1916–1919 | L22221–L22261 |
| QENEMY STRATEGY @ L22263 | 1920–1926 | L22265–L22350 |
| QEAGOL @ L22352 | 1927–1948 | L22354–L22539 |
| QSPECIAL TIMERS @ L22541 | 1949–1956 | L22542–L22603 |

### B. Region control inventory

| Region | Writers | Readers / state carriers | Timers | Jumps | Escrow | Search / placement | Commands | Observers | Re-entry topology |
|---|---|---|---|---|---|---|---|---|---|
| UNHEADED @ L1 | — | — | — | — | — | — | — | — | — |
| UNHEADED @ L7 | — | — | — | — | — | — | — | — | — |
| QPOSITION @ L1401 | gl-scout-unit | gl-scout-unit | — | — | — | — | — | — | — |
| QEAGOL @ L1723 | gl-max-coordinate-value, net-food-amount, net-gold-amount, net-stone-amount, net-wood-amount, sn-focus-player-number | gl-fifth-turn, gl-max-coordinate-value, gl-privileged-player, gl-second-turn, net-food-amount, net-gold-amount, net-stone-amount, net-wood-amount, sn-focus-player-number | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | — | up-get-fact, up-get-object-data | — |
| QSETUP @ L1924 | gl-close-ranged-group-range, gl-current-group, gl-defend-town, gl-enemy-tower-range, gl-max-ranged-group-size, gl-my-tower-range, gl-raid-group-range, gl-range-advantage, gl-ranged-group-range, gl-tracking-range, sn-number-tasked-units | gl-close-ranged-group-range, gl-current-group, gl-defend-town, gl-enemy-tower-range, gl-max-ranged-group-size, gl-my-tower-range, gl-raid-group-range, gl-range-advantage, gl-ranged-group-range, gl-ranged-group-state, gl-town-safe, gl-tracking-range | — | 14:1 | — | — | research | research-completed | R14→1 |
| QADVANTAGE @ L2057 | gl-armor-advantage, gl-range-advantage, gl-ranged-eval, goal, goal1, goal5, goal6, goal7, goal8, goal9, lt, rt, sn-focus-player-number, split | gl-armor-advantage, gl-enemy-group-size, gl-fifth-turn, gl-range-advantage, gl-ranged-eval, gl-ranged-group-size, goal, goal1, goal5, goal6, goal7, goal8, goal9, lt, rt, sn-focus-player-number, split, up-first | — | 27:44, 45:-2, 59:-2, 69:-2 | — | up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research, up-research | research-completed, research-pending, up-get-object-data, up-get-search-state | R27→44, R45→-2, R59→-2, R69→-2 |
| QNA @ L2534 | gl-can-move | gl-can-fire, gl-can-move, gl-highest-next-attack, gl-target-distance | t-failsafe | 75:12 | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | — | up-get-object-data | R75→12 |
| QTARGET STUFF @ L2666 | gl-target-class, gl-target-distance, gl-target-hp, gl-target-type, goal, rt, sn-focus-player-number, split, target-id, target-x, target-y | gl-ranged-eval, gl-ranged-group-range, gl-ranged-group-state, gl-target-class, gl-target-distance, gl-target-hp, gl-target-type, gl-tracking-range, goal, rt, sn-focus-player-number, split, superiority, target-id, target-x, target-y | — | 102:-5, 108:-5, 113:-4, 117:-3, 88:56, 96:-5 | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | research | research-completed, up-get-search-state | R102→-5, R108→-5, R113→-4, R117→-3, R88→56, R96→-5 |
| QUICKIES @ L2964 | goal, sn-focus-player-number, split | gl-switch, gl-tracking-range, goal, rt, sn-focus-player-number, split, superiority | — | 125:-7 | — | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects, up-set-target-point | research | research-completed, up-get-search-state | R125→-7 |
| QUICKIES @ L3042 | goal, sn-focus-player-number, split | gl-fifth-turn, gl-switch, gl-tracking-range, goal, rt, sn-focus-player-number, split, superiority | — | 133:-7, 143:-9 | — | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research | research-completed, up-get-object-data, up-get-search-state | R133→-7, R143→-9 |
| QMISC @ L3246 | gl-cavalry-attacking, gl-enemy-group-size, gl-mangos-nearby, gl-melee-in-range, gl-total-military-in-range, gl-total-units-in-range, gl-units-in-close-range, goal, nearest-castle-x, nearest-castle-y, nearest-tc-x, nearest-tc-y, nearest-tower-x, nearest-tower-y, rt, sn-focus-player-number, split | gl-cavalry-attacking, gl-close-ranged-group-range, gl-enemy-group-size, gl-mangos-nearby, gl-melee-in-range, gl-ranged-group-range, gl-second-turn, gl-thirty-turn, gl-total-military-in-range, gl-total-units-in-range, gl-units-in-close-range, goal, lt, nearest-castle-x, nearest-castle-y, nearest-tc-x, nearest-tc-y, nearest-tower-x, nearest-tower-y, rt, sn-focus-player-number, split | — | 152:12, 153:5, 156:-2, 161:-2, 165:34, 166:5, 169:-2, 172:5, 175:-2, 180:-2, 183:-2, 186:-2, 197:-2, 200:-2 | — | up-clean-search, up-find-local, up-find-remote, up-find-status-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | — | up-get-search-state | R152→12, R153→5, R156→-2, R161→-2, R165→34, R166→5, R169→-2, R172→5, R175→-2, R180→-2, R183→-2, R186→-2, R197→-2, R200→-2 |
| QMPOINTS @ L3751 | gl-march-type, sn-focus-player-number, split | gl-attacking, gl-defend-town, gl-march-type, gl-tenth-turn, gl-thirty-turn, sn-focus-player-number, split | — | 221:12, 229:4, 231:2 | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | — | — | R221→12, R229→4, R231→2 |
| QMINIS @ L4132 | sn-focus-player-number | gl-current-build-item, gl-fifth-turn, gl-getting-sheep, gl-scout-stuck, gl-second-turn, gl-seventh-turn, gl-tenth-turn, gl-twenty-turn, goal, newscouting, scout-id, sn-focus-player-number | 28 | 237:6 | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research, up-research, up-target-objects | research-pending, up-get-search-state, up-pending-objects | R237→6 |
| QHOUSES @ L4383 | goal, goal1, split | goal, goal1, lt, rt, split | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-target-point | up-get-object-data, up-get-search-state | — |
| QLC @ L4474 | gl-lclerp, gl-trees-around, sn-focus-player-number, sn-lumber-camp-max-distance, split | gl-dark-build, gl-lclerp, gl-trees-around, goal, rt, sn-focus-player-number, sn-lumber-camp-max-distance, split | — | 275:-2, 281:1, 282:2, 289:-1 | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-build, up-target-point | up-get-search-state, up-pending-objects | R275→-2, R281→1, R282→2, R289→-1 |
| QANTI-TRUSH @ L4799 | gl-trushed, rt, sn-focus-player-number | gl-trushed, rt, sn-focus-player-number | — | 296:-2 | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-target-objects | up-get-search-state | R296→-2 |
| QGARRISONING TC @ L4863 | gl-saved-focus-player, goal, goal1, sn-focus-player-number, split | gl-garrison-tc, gl-saved-focus-player, goal, goal1, home-id, lt, rt, sn-focus-player-number, split | — | 303:1, 304:-3 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-target-objects | up-get-search-state | R303→1, R304→-3 |
| QVILLS @ L4970 | enemy-attack-x, enemy-attack-y, gl-enemy-attack-size, goal, goal1, goal2, lt, point-x, point-y, rt, sn-focus-player-number, split | enemy-attack-x, enemy-attack-y, gl-aggressive-vills, gl-enemy-attack-size, gl-fifth-turn, gl-ninety-turn, gl-second-turn, gl-skirm-vills, gl-tenth-turn, gl-threat-time, gl-town-safe, goal, goal1, goal2, home-id, lt, point-x, point-y, rt, sn-focus-player-number, split | t-infantry-attack | 312:9, 315:-2, 322:6, 329:8, 335:-2, 336:-4, 340:-2, 347:8, 350:-2, 359:-2, 363:5, 366:-2, 376:-2 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-target-objects | up-get-object-data, up-get-search-state | R312→9, R315→-2, R322→6, R329→8, R335→-2, R336→-4, R340→-2, R347→8, R350→-2, R359→-2, R363→5, R366→-2, R376→-2 |
| QSHEEP @ L5685 | — | gl-current-sheep-count, gl-fifth-turn, gl-sheep-scouting, goal2, sheep1-id | — | 379:11 | — | up-clean-search, up-find-local, up-full-reset-search, up-set-target-object | — | up-get-object-data | R379→11 |
| QNEWSCOUTING @ L5828 | cross, gl-inside-forest, gl-scouting-switch, goal1, goal2, goal3, goal4, newscouting, sn-focus-player-number, split | cross, explo-x, explo-y, gl-current-sheep-count, gl-fifth-turn, gl-getting-sheep, gl-inside-forest, gl-scouting-switch, gl-second-turn, gl-sighted-boar-count, goal, goal1, goal2, goal3, goal4, newscouting, scout-id, scout-x, scout-y, split, t-misc | 28, t-direction-switch, t-misc | 391:33, 422:1, 442:1 | — | up-find-local, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | up-target-point | — | R391→33, R422→1, R442→1 |
| QCIRCLE SCOUTING @ L6406 | goal, goal1, sn-focus-player-number, split | gl-circle-direcion, gl-dlure, gl-scout-added, gl-strategy, gl-tenth-turn, gl-twenty-turn, goal, goal1, sn-focus-player-number, split | 28 | 448:15, 449:4, 455:4, 460:3 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-set-target-object | up-target-point | — | R448→15, R449→4, R455→4, R460→3 |
| QFORAGE @ L6715 | sn-focus-player-number, split | bh, gl-killed-boar-count, gl-tenth-turn, sn-focus-player-number, split | — | — | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-target-objects | up-get-search-state | — |
| QCOUNTING SHEEP @ L6767 | gl-current-sheep-count, gl-new-sheep-count, gl-sheep-count-last | gl-current-sheep-count, gl-new-sheep-count, gl-sheep-count, gl-sheep-count-last | — | — | — | — | — | — | — |
| QDLURING @ L6795 | gl-killed-deer-count, goal2, goal3, goal4, sn-focus-player-number, sn-maximum-hunt-drop-distance, sn-number-explore-groups, sn-total-number-explorers, split | deer-id, gl-deer-distance, gl-deer-walking, gl-dlure, gl-fifth-turn, gl-killed-deer-count, gl-second-turn, gl-tenth-turn, goal, goal1, goal2, goal3, goal4, rt, sn-focus-player-number, split, t-misc | t-misc | — | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-research, up-target-objects | research-pending, unit-type-count-total, up-get-search-state | — |
| QBH @ L7174 | bh, gl-killed-boar-count, gl-sighted-boar-count, goal1, goal7, old-boar-id, sn-focus-player-number, split | bh, current-boar-id, gl-fifth-turn, gl-killed-boar-count, gl-sighted-boar-count, gl-town-safe, goal, goal1, goal7, home-id, lt, lurer-id, old-boar-id, rl, rt, sn-focus-player-number, split | — | 513:6 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research, up-research, up-target-objects | research-completed, unit-type-count-total, up-get-object-data, up-get-search-state | R513→6 |
| QRETARGETING @ L7684 | goal, sn-focus-player-number, split | bh, current-boar-id, gl-fifth-turn, gl-killed-boar-count, gl-second-turn, goal, home-id, lt, old-boar-id, retarget, sn-focus-player-number, split | t-kill-boar | — | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research, up-target-objects | research-completed, up-get-object-data, up-get-search-state | — |
| QFORCEDROP @ L7949 | force-res-drop-goal, goal | force-res-drop-goal, gl-current-build-item, gl-fifth-turn, gl-strategy, gl-tenth-turn, gl-twenty-turn, goal | t-vill-training, villager-timer | — | — | — | research, up-research | building-type-count-total, research-pending, up-get-fact, up-pending-objects | — |
| QCLAIMING SHEEP @ L8087 | gl-getting-sheep, goal, sn-focus-player-number, split | 28, gl-getting-sheep, goal, lt, rt, sn-focus-player-number, split | 28 | 593:4 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-target-point | up-get-search-state | R593→4 |
| QFARMS @ L8222 | split | split | — | — | — | up-set-target-point | — | — | — |
| QARCHERS @ L8267 | gl-enemy-skirms-nearby, rt, sn-focus-player-number | gl-enemy-skirms-nearby, rt, sn-focus-player-number | — | 610:2, 613:-2 | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | — | up-get-object-data, up-get-search-state | R610→2, R613→-2 |
| QSKIRMS @ L8338 | gl-enemy-archers, rt, sn-focus-player-number, split | gl-enemy-archers, gl-tenth-turn, gl-town-safe, rt, sn-focus-player-number, split | — | 619:-2 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-target-point | up-get-search-state | R619→-2 |
| QDEFENSE @ L8405 | rt, sn-focus-player-number | gl-archery-in-town, gl-cavalry-in-town, rt, sn-focus-player-number, split | — | 622:3, 625:-2 | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | — | up-get-search-state | R622→3, R625→-2 |
| QMANGOS @ L8485 | — | gl-ninety-turn, superiority | — | — | — | — | — | — | — |
| QSPEARS @ L8501 | goal, goal1, goal2, goal3, goal4, goal6, goal8, lt, point-x, point-y, rt, sn-focus-player-number, split | gl-second-turn, gl-thirty-turn, gl-town-safe, goal, goal1, goal2, goal3, goal4, goal5, goal6, goal8, lt, point-x, point-y, rt, sn-focus-player-number, split | — | 632:-2, 640:-2, 642:34, 649:-3, 652:-2, 655:-2, 658:-2, 664:-2, 669:-2 | — | up-clean-search, up-find-local, up-find-remote, up-find-status-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-target-objects, up-target-point | up-get-object-data, up-get-search-state | R632→-2, R640→-2, R642→34, R649→-3, R652→-2, R655→-2, R658→-2, R664→-2, R669→-2 |
| QSCOUT @ L9068 | gl-getting-sheep, goal, goal1, goal2, goal3, goal4, goal5, sn-focus-player-number, sn-number-explore-groups, sn-total-number-explorers, split | 28, gl-attacking, gl-fifth-turn, gl-getting-sheep, gl-ninety-turn, gl-position, gl-scout-added, gl-second-turn, gl-strategy, gl-total-units-in-range, goal, goal1, goal2, goal3, goal4, goal5, newscouting, rt, scout-id, sn-focus-player-number, sn-number-explore-groups, sn-total-number-explorers, sod, split | 28 | 687:36, 688:35, 692:31, 695:-2, 698:-2, 703:-4, 708:-2, 716:-2 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | — | up-get-object-data, up-get-search-state | R687→36, R688→35, R692→31, R695→-2, R698→-2, R703→-4, R708→-2, R716→-2 |
| QSOD @ L9610 | goal, goal1, goal2, sn-focus-player-number | gl-circle-direcion, gl-strategy, goal, goal1, goal2, rt, scout-id, sn-focus-player-number, sod, split | 28 | 732:14, 741:-3 | — | up-full-reset-search, up-set-target-object | — | up-get-object-data | R732→14, R741→-3 |
| QKNIGHT GROUP @ L9765 | goal, lt, point-x, point-y, sn-focus-player-number | gl-attacking, gl-strategy, gl-tenth-turn, gl-town-safe, goal, lt, point-x, point-y, sn-focus-player-number | — | 750:-2 | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object | — | up-get-object-data, up-get-search-state | R750→-2 |
| QEVAL @ L9821 | gl-knight-eval, gl-knight-group-state, gl-knight-retreat, goal, goal1, goal2, goal3, split | gl-fifth-turn, gl-knight-eval, gl-knight-group-size, gl-knight-group-state, gl-knight-retreat, gl-second-turn, gl-town-safe, goal, goal1, goal2, goal3, split, superiority | — | 755:10, 766:30, 782:1, 803:11 | — | up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | research, up-target-point | research-completed, up-get-search-state | R755→10, R766→30, R782→1, R803→11 |
| QRAIDING @ L10481 | gl-ancient-raid-target-id, gl-old-raid-target-id, gl-raid-status, goal, goal1, goal3, goal4, goal5, lt, point-x, point-y, rt, sn-focus-player-number, split | gl-ancient-raid-target-id, gl-enemy-group-size, gl-enemy-strategy, gl-fifth-turn, gl-highest-next-attack, gl-old-raid-target-id, gl-raid-can-fire, gl-raid-can-move, gl-raid-group-state, gl-raid-retreat-type, gl-raid-status, gl-ranged-style, gl-second-turn, gl-tenth-turn, gl-town-safe, gl-twenty-turn, goal, goal1, goal2, goal3, goal4, goal5, lt, point-x, point-y, rt, sn-focus-player-number, split, superiority, t-raid-target-reset, t-raid-waypoint-reevaluate | t-raid-retreat, t-raid-target-reset, t-raid-waypoint-reevaluate | 832:1, 833:-3, 835:4, 838:-2, 840:13, 853:1, 855:3, 859:4, 864:4, 870:1, 872:9, 882:44, 887:-2, 891:-2, 906:-2, 929:-2, 959:1 | — | up-clean-search, up-find-local, up-find-remote, up-find-status-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-target-point | up-get-object-data, up-get-search-state | R832→1, R833→-3, R835→4, R838→-2, R840→13, R853→1, R855→3, R859→4, R864→4, R870→1, R872→9, R882→44, R887→-2, R891→-2, R906→-2, R929→-2, R959→1 |
| QRANGED MICRO @ L12040 | goal, point-x, point-y, rt, sn-focus-player-number, split | gl-army-damage-potential, gl-defend-town, gl-fifty-turn, gl-town-safe, goal, point-x, point-y, rt, sn-focus-player-number, split, superiority | — | 965:4, 968:-2, 970:-2 | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research | research-completed, up-get-object-data, up-get-search-state | R965→4, R968→-2, R970→-2 |
| QINITIALIZING GROUP @ L12236 | split | gl-enemy-skirms-nearby, gl-ranged-group-state, split | — | 983:1 | — | up-find-local, up-remove-objects | research, up-research | research-completed | R983→1 |
| QREGROUPING @ L12317 | — | gl-second-turn, gl-town-safe, lt, split | — | 989:9 | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | up-target-point | — | R989→9 |
| QMOVING @ L12474 | goal, goal1, goal2, goal3, goal4, goal5, goal6, split | gl-army-damage-potential, gl-can-move, gl-enemy-group-size, gl-fifth-turn, gl-mangos-nearby, gl-ranged-eval, gl-ranged-group-size, gl-ranged-group-state, gl-ranged-retreat, gl-target-distance, goal, goal1, goal2, goal3, goal4, goal5, goal6, lt, split, superiority | t-ranged-retreat | 1017:13, 999:16 | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | research, up-research | research-completed, research-pending, up-get-search-state | R1017→13, R999→16 |
| QCCR @ L12797 | goal, goal1, goal2, goal3, goal4, goal5, goal6, split | gl-fifth-turn, gl-ninety-turn, gl-second-turn, goal, goal1, goal2, goal3, goal4, goal5, goal6, lt, split, superiority | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research, up-target-point | research-completed, up-get-object-data, up-get-search-state | — |
| QTCR @ L12972 | goal, goal1, goal2, goal3, goal4, goal5, goal6, sn-focus-player-number, split | gl-fifth-turn, gl-ninety-turn, gl-second-turn, gl-strategy, goal, goal1, goal2, goal3, goal4, goal5, goal6, lt, rt, sn-focus-player-number, split, superiority | — | 1056:-2 | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | research, up-research, up-target-point | research-completed, up-get-object-data, up-get-search-state | R1056→-2 |
| QMARCH TO ENEMY BASE @ L13231 | gl-direction, goal, goal1, goal2, goal3, goal4, goal5, goal6, goal7, goal8, split | gl-army-damage-potential, gl-can-move, gl-direction, gl-enemy-group-size, gl-fifth-turn, gl-melee-in-range, gl-ranged-group-state, gl-target-distance, gl-thirty-turn, goal, goal1, goal2, goal3, goal4, goal5, goal6, goal7, goal8, nearest-castle-x, nearest-tc-x, nearest-tower-x, split, superiority | t-failsafe, t-ranged-retreat | 1079:12 | — | up-full-reset-search | research | research-completed | R1079→12 |
| QCOMBAT MODE @ L13707 | split | gl-can-fire, gl-ranged-group-state, retreating, split | t-ranged-retreat | 1132:7, 1133:6 | — | — | — | up-get-object-data | R1132→7, R1133→6 |
| QFAILSAFE @ L13810 | sn-food-gatherer-percentage, sn-gold-gatherer-percentage | gl-fifth-turn, sn-food-gatherer-percentage, sn-gold-gatherer-percentage | — | — | — | — | up-research | research-pending, unit-type-count-total | — |
| QDARK @ L13824 | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-maximum-wood-drop-distance, sn-stone-gatherer-percentage, sn-wood-dropsite-distance, sn-wood-gatherer-percentage | — | — | — | — | — | — | — | — |
| QKRUSH @ L13861 | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | gl-strategy | — | 1145:8 | — | — | up-research | building-type-count-total, research-pending | R1145→8 |
| QFLUSH @ L13980 | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage, split | gl-age-loading, gl-current-sheep-count, gl-killed-boar-count, gl-killed-deer-count, gl-strategy, split | — | — | — | — | up-research | building-type-count-total, research-pending | — |
| QKNIGHTS @ L14113 | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | gl-age-loading, gl-build-progress, gl-strategy | — | — | — | — | — | — | — |
| QSIEGE @ L14178 | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | gl-age-loading, gl-strategy | — | — | — | — | — | — | — |
| QSCALEMAIL @ L14293 | gl-progression-pause | gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, set-escrow-percentage, up-modify-escrow | — | up-research | — | — |
| QCHAINMAIL @ L14326 | gl-progression-pause | gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, set-escrow-percentage, up-modify-escrow | — | research, up-research | research-completed, research-pending | — |
| QIRONCASTING @ L14362 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage, up-modify-escrow | — | up-research | research-pending | — |
| QFORGING @ L14459 | gl-build-progress | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QCHAINBARDING @ L14559 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QSCALEBARDING @ L14658 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QXBOW @ L14762 | gl-progression-pause | gl-build-progress, gl-progression-pause | — | — | — | — | up-research | research-pending, unit-type-count-total | — |
| QPIKES @ L14784 | gl-progression-pause, split | gl-build-progress, gl-enemy-civ, gl-progression-pause, gl-strategy, split | — | — | can-research-with-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QAGE @ L14823 | gl-age-loading, gl-need-vills | gl-age-loading, gl-need-vills, gl-strategy | — | — | — | — | research | unit-type-count-total | — |
| QCUP @ L14868 | gl-build-progress, gl-need-vills | gl-build-progress, gl-current-build-item, gl-enemy-strategy-type, gl-need-vills, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow | — | research, up-research | research-pending, unit-type-count-total | — |
| QFLTCH @ L14973 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage, up-modify-escrow | — | research, up-research | research-pending | — |
| QLAA @ L15024 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QPAA @ L15072 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage, up-modify-escrow | — | up-research | research-pending | — |
| QBODKIN @ L15121 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, set-escrow-percentage, up-modify-escrow | — | up-research | research-pending | — |
| QLOOM @ L15175 | gl-need-vills | gl-need-vills | t-relure | — | — | — | research | up-pending-objects | — |
| QMONKS @ L15201 | — | — | — | — | — | — | train | unit-type-count-total | — |
| QMANGOS @ L15229 | siege | gl-strategy, gl-town-safe, rt, siege, superiority | — | — | can-train-with-escrow, release-escrow, set-escrow-percentage, up-modify-escrow | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-train | unit-type-count-total, up-get-search-state, up-pending-objects | — |
| QSCORPS @ L15320 | — | gl-strategy, siege | — | — | — | — | — | unit-type-count-total | — |
| QRAMS @ L15336 | split | gl-army-damage-potential, siege, split | — | — | can-train-with-escrow, up-modify-escrow | — | — | unit-type-count-total, up-pending-objects | — |
| QSCOUTS @ L15395 | — | gl-strategy | — | — | — | — | — | up-pending-objects | — |
| QKNIGHTS @ L15409 | — | gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-train-with-escrow | — | up-train | up-pending-objects | — |
| QARCHERS @ L15445 | — | gl-progression-pause | — | — | — | — | research, up-research, up-train | research-completed, research-pending, unit-type-count-total | — |
| QSKIRMS @ L15472 | gl-escrow-state, gl-skirm-total, split | gl-escrow-state, gl-progression-pause, gl-skirm-total, split, superiority | — | — | — | — | up-research | research-pending | — |
| QMILITIAMAN @ L15549 | — | gl-enemy-civ, gl-target-age | — | — | — | — | research, train | research-completed, unit-type-count-total | — |
| QSPEARS @ L15564 | — | enemy-stable, gl-enemy-civ, gl-progression-pause, gl-strategy, gl-target-age | — | 1295:2 | — | — | research, up-train | research-completed, unit-type-count-total | R1295→2 |
| QTOWERS @ L15684 | gl-tower-control, sn-placement-zone-size | gl-enemy-strategy, gl-position, gl-tower-control, gl-town-safe | — | 1299:6 | — | — | up-build | building-type-count-total | R1299→6 |
| QSTABLE @ L15764 | gl-build-progress, goal, sn-placement-zone-size | gl-build-progress, gl-current-build-item, gl-enemy-strategy, gl-fifth-turn, gl-progression-pause, gl-strategy, gl-tenth-turn, gl-town-safe, goal | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | building-type-count-total, up-pending-objects, up-pending-placement | — |
| QMONASTERY @ L16168 | goal, sn-placement-zone-size | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy, gl-town-safe, goal | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | building-type-count-total, up-pending-objects, up-pending-placement | — |
| QMARKET @ L16231 | gl-build-progress, gl-progression-pause, goal, sn-placement-zone-size, split | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy, gl-tenth-turn, gl-town-safe, goal, net-food-amount, net-gold-amount, net-wood-amount, split, t-misc | t-misc | — | can-build-with-escrow, release-escrow, set-escrow-percentage, up-modify-escrow | — | research, up-build | building-type-count-total, up-pending-placement | — |
| QANALYZING ENEMY ATTACK @ L16478 | gl-archery-in-town, gl-cavalry-in-town, sn-focus-player-number | gl-archery-in-town, gl-cavalry-in-town, gl-tenth-turn, sn-focus-player-number | — | 1382:4, 1386:-3 | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | — | up-get-search-state | R1382→4, R1386→-3 |
| QRESIGNING @ L16527 | goal1 | 5, civsup, every-ally, goal1, superiority | 5 | 1387:2, 1390:6 | — | — | — | building-type-count-total, up-get-fact | R1387→2, R1390→6 |
| QSUPERIORITY @ L16613 | superiority | superiority | — | — | — | — | — | up-get-fact | — |
| QCIVSUP @ L16624 | civsup | civsup | — | — | — | — | — | up-get-fact | — |
| QTSA @ L16636 | sn-maximum-town-size | gl-attacking, gl-ninety-turn, gl-strategy | — | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | up-target-point | — | — |
| QENEMY STRAT @ L16728 | enemy-stable, gl-enemy-strategy-type | enemy-stable, gl-enemy-strategy, gl-enemy-strategy-type, gl-target-age | — | — | — | — | — | — | — |
| QCHAT @ L16797 | — | — | — | — | — | — | research | research-completed | — |
| QSTRATEGY @ L16851 | gl-enemy-strategy, gl-enemy-strategy-type, gl-position, gl-strategy, gl-strategy-type, sn-home-exploration-time | gl-enemy-strategy, gl-enemy-strategy-type, gl-position, gl-strategy, gl-strategy-type | — | — | — | — | — | — | — |
| QECO NUMBERS @ L16922 | gl-age-loading, gl-build-progress, gl-dark-build, gl-early-gar, gl-getting-sheep, gl-need-vills, gl-vills-under-tc, goal, sn-cap-civilian-builders, sn-cap-civilian-explorers, sn-enable-training-queue, sn-initial-exploration-required, sn-livestock-to-town-center, sn-maximum-gaia-attack-response, sn-mining-camp-max-distance, sn-percent-civilian-builders, sn-percent-civilian-explorers, sn-percent-civilian-gatherers, sn-percent-exploration-required, sn-preferred-mill-placement, sn-safe-town-size, sn-zero-priority-distance, split | gl-age-loading, gl-attack-efficiency, gl-build-progress, gl-current-sheep-count, gl-dark-build, gl-defend-town, gl-early-gar, gl-enemies-in-town, gl-enemy-strategy-type, gl-getting-sheep, gl-need-vills, gl-second-turn, gl-skirm-total, gl-target-age, gl-town-safe, gl-vills-under-tc, goal, split, superiority | t-relure | — | — | up-find-local, up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | — | building-type-count-total, up-get-fact, up-get-search-state | — |
| QUEUE @ L17245 | gl-boar-unit, sn-allow-adjacent-dropsites, sn-cap-civilian-builders, sn-disable-builder-assistance, sn-dropsite-separation-distance, sn-enable-new-building-system, sn-enable-training-queue, sn-food-dropsite-distance, sn-forage-defend-priority, sn-gold-defend-priority, sn-gold-dropsite-distance, sn-intelligent-gathering, sn-livestock-defend-priority, sn-maximum-food-drop-distance, sn-maximum-gold-drop-distance, sn-maximum-hunt-drop-distance, sn-maximum-stone-drop-distance, sn-maximum-wood-drop-distance, sn-minimum-boar-hunt-group-size, sn-preferred-mill-placement, sn-required-forest-tiles, sn-retask-gather-amount, sn-stone-defend-priority, sn-stone-dropsite-distance, sn-use-by-type-max-gathering, sn-wood-dropsite-distance | gl-boar-unit, gl-strategy | — | — | — | — | — | — | — |
| QBECO @ L17393 | goal, sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer, gl-current-build-item, gl-fifty-turn, gl-strategy, gl-threat-target, gl-threat-time, gl-town-safe, goal, gp, net-food-amount, net-gold-amount, net-stone-amount, net-wood-amount, sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | 1464:15, 1465:14, 1466:13 | — | — | research | — | R1464→15, R1465→14, R1466→13 |
| QTOWN SAFETY @ L17636 | gl-enemies-in-town, gl-enemy-civ, gl-escrow-state, gl-town-safe, gl-town-under-attack, goal, rt, sn-allow-civilian-offense, sn-disable-attack-groups, sn-do-not-scale-for-difficulty-level, sn-enable-offensive-priority, sn-enable-patrol-attack, sn-enemy-sighted-response-distance, sn-focus-player-number, sn-home-exploration-time, sn-ignore-tower-elevation, sn-maximum-explore-group-size, sn-number-attack-groups, sn-number-civilian-militia, sn-number-forward-builders, sn-percent-attack-soldiers, sn-percent-building-cancellation, sn-percent-enemy-sighted-response, sn-percentage-explore-exterminators, sn-relic-return-distance, sn-special-attack-influence1, sn-special-attack-type1, sn-target-evaluation-boat, sn-target-evaluation-continent, sn-target-evaluation-distance, sn-target-evaluation-in-progress, sn-target-evaluation-kills, sn-target-evaluation-siege-weapon | gl-attacking, gl-enemies-in-town, gl-enemy-civ, gl-enemy-strategy, gl-escrow-state, gl-town-safe, gl-town-under-attack, goal, rt, sn-focus-player-number, t-town-safe | t-town-safe | 1487:-2, 1490:-2, 1498:-2 | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | — | up-get-search-state | R1487→-2, R1490→-2, R1498→-2 |
| QTARGET PLAYER @ L17945 | gl-find-new-target, gl-last-target-player, rt, sn-focus-player-number, sn-target-player-number, split | focus-player, gl-fifth-turn, gl-find-new-target, gl-last-target-player, gl-position, gl-privileged-player, gl-strategy, goal, rt, sn-focus-player-number, sn-target-player-number, split, t-target-switch | t-target-switch | 1515:4, 1518:-2, 1555:19, 1575:15 | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | — | up-get-object-data | R1515→4, R1518→-2, R1555→19, R1575→15 |
| QPRIORITY @ L18933 | goal | gl-attacking, gl-strategy, goal, superiority | — | — | — | — | — | — | — |
| QSCOUTING @ L19032 | sn-number-explore-groups, sn-total-number-explorers | t-scout-enemy | t-scout-enemy | — | — | — | — | — | — |
| QATTACK EFFICIENCY @ L19083 | gl-attack-efficiency, goal, goal1, goal2, goal3, goal4, goal8, sn-focus-player-number | gl-attack-efficiency, gl-fifth-turn, goal, goal1, goal2, goal3, goal4, goal8, sn-focus-player-number | — | 1616:20 | — | up-find-remote, up-full-reset-search, up-get-search-state | — | up-get-fact, up-get-search-state | R1616→20 |
| QDAMAGE POTENTIAL @ L19299 | gl-army-damage-potential, goal, up-first | gl-army-damage-potential, gl-enemy-strategy-type, gl-target-age, goal, up-first | — | — | — | — | research, up-research | research-completed, research-pending, up-get-fact | — |
| Q2BA @ L19462 | — | gl-build-progress, gl-current-build-item, gl-strategy | — | — | can-research-with-escrow | — | up-research | research-pending | — |
| QBOWSAW @ L19549 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending, unit-type-count-total | — |
| QGOLDMINING @ L19649 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow | — | up-research | research-pending | — |
| QGOLDSHAFT @ L19736 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QHCOL @ L19784 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow | — | up-research | research-pending | — |
| QHEAVY PLOW @ L19871 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QVILLAGERS @ L19918 | — | gl-current-build-item, gl-need-vills, gl-strategy, t-vill-training | t-vill-training | 1707:1 | — | — | research, up-train | research-completed, unit-type-count-total, up-pending-objects | R1707→1 |
| QESCROW @ L19996 | — | gl-build-progress, gl-current-build-item | — | — | release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QTSB @ L20097 | gl-original-ts, sn-camp-max-distance, sn-maximum-town-size | gl-original-ts, gl-trushed, sn-maximum-town-size | — | — | — | — | — | — | — |
| QRANGES @ L20188 | gl-build-progress, gl-current-build-item, goal, sn-placement-zone-size | gl-build-progress, gl-current-build-item, gl-enemy-strategy, gl-progression-pause, gl-strategy, gl-town-safe, goal | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | building-type-count-total | — |
| QESKIRMS @ L20291 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | set-escrow-percentage | — | up-research | research-pending | — |
| QSW @ L20339 | gl-build-progress, goal, sn-placement-zone-size | gl-army-damage-potential, gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy, gl-tenth-turn, gl-town-safe, goal, sn-placement-zone-size, superiority | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage, up-modify-escrow | — | up-build | building-type-count-total, up-pending-placement | — |
| QRAX @ L20476 | gl-build-progress, gl-progression-pause, goal | gl-build-progress, gl-current-build-item, gl-enemy-strategy, gl-progression-pause, gl-strategy, gl-town-safe, goal | t-rax | — | can-build-with-escrow, up-modify-escrow | — | research | building-type-count-total, research-completed | — |
| QSMITH @ L20652 | gl-build-progress, goal | gl-build-progress, gl-current-build-item, gl-fifth-turn, gl-progression-pause, gl-strategy, gl-town-safe, goal | — | — | can-build-with-escrow, set-escrow-percentage | — | — | building-type-count-total | — |
| QCASTLES @ L20765 | goal, sn-placement-zone-size | gl-enemy-strategy, gl-town-safe, goal, superiority | — | — | — | — | up-build | — | — |
| QFARMS @ L20800 | gl-build-progress, gl-escrow-state, split | gl-build-progress, gl-current-build-item, gl-escrow-state, gl-ninety-turn, gl-second-turn, gl-strategy, mill, rt, split | — | 1795:1 | can-build-with-escrow | — | up-build, up-research | building-type-count-total, research-pending, up-get-fact, up-pending-objects, up-pending-placement | R1795→1 |
| QHOUSE @ L21070 | goal, sn-placement-fail-delta, sn-placement-zone-size, split | gl-enemy-strategy, gl-fifth-turn, gl-strategy, gl-town-safe, goal, housed, split | — | — | can-build-with-escrow | — | up-build | building-type-count-total, up-pending-objects | — |
| QLC @ L21220 | gl-build-progress, sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | gl-build-progress, gl-current-build-item, gl-dark-build, gl-fifth-turn, gl-progression-pause, gl-strategy | — | 1850:4 | can-build-with-escrow, release-escrow, set-escrow-percentage | — | build | building-type-count-total | R1850→4 |
| QTRADING @ L21524 | — | gl-build-progress, gl-current-build-item, gl-strategy | — | — | — | — | up-research | research-pending | — |
| QMILL @ L21649 | gl-build-progress, goal, sn-allow-adjacent-dropsites | gl-build-progress, gl-current-build-item, gl-dark-build, goal, mill, t-build-delay | t-build-delay | — | can-build-with-escrow, set-escrow-percentage | — | — | building-type-count-total, up-pending-placement | — |
| QMC @ L21762 | gl-build-progress, sn-focus-player-number, split | gl-build-progress, gl-current-build-item, gl-fifth-turn, gl-progression-pause, gl-strategy, gl-tenth-turn, sn-focus-player-number, split, t-build-delay | t-build-delay | 1891:5 | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | — | building-type-count-total | R1891→5 |
| QUNIVERSITY @ L22097 | gl-build-progress, sn-placement-zone-size | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy, goal | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | building-type-count-total | — |
| QBALLISTICS @ L22146 | — | gl-build-progress, gl-current-build-item, gl-progression-pause, gl-strategy | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | up-research | research-pending | — |
| QEND @ L22193 | — | gl-position | — | — | — | — | — | — | — |
| QMISC @ L22220 | gl-identity | gl-identity, gl-strategy | — | — | — | — | — | — | — |
| QENEMY STRATEGY @ L22263 | early-mining-notice, gl-enemy-strategy, gl-enemy-strategy-type | early-mining-notice, gl-enemy-strategy, gl-enemy-strategy-type, gl-target-age | — | — | — | — | — | — | — |
| QEAGOL @ L22352 | gl-target-age, gl-target-score1 | gl-target-age, gl-target-age-checking, gl-target-score1 | t-enemy-age-cancel | — | — | — | — | up-get-fact | — |
| QSPECIAL TIMERS @ L22541 | gl-fifth-turn, gl-fifty-turn, gl-ninety-turn, gl-second-turn, gl-seventh-turn, gl-switch, gl-tenth-turn, gl-thirty-turn, gl-turn-count, gl-twenty-turn | 30sec, five-seconds-timer, gl-fifth-turn, gl-fifty-turn, gl-ninety-turn, gl-second-turn, gl-seventh-turn, gl-switch, gl-tenth-turn, gl-thirty-turn, gl-turn-count, gl-twenty-turn, one-minute, three-minute, two-minute | 30sec, five-seconds-timer, one-minute, three-minute, two-minute | — | — | — | — | — | — |

### C. Donor-rule transplantation ledger

Each row is an executable donor rule. Current-rule references are only emitted where the current tree has a mechanism-level candidate; otherwise the rule is explicitly LOST. `UNKNOWN` is reserved for cases where static evidence is insufficient to distinguish two plausible mechanisms.

| Donor # | Source | Region | Predicate/state mechanism | Writers | Timers | Escrow | Search/placement | Commands/observers | Jump | Current candidate(s) | Classification |
|---:|---|---|---|---|---|---|---|---|---|---|---|
| 1 | L1–L5 | UNHEADED @ L1 | `(defrule     (false)` | — | — | — | — | — | — | — | **LOST** |
| 2 | L7–L13 | UNHEADED @ L7 | `(defrule     (taunt-detected my-player-number 7)` | — | — | — | — | — | — | — | **LOST** |
| 3 | L1451–L1456 | QPOSITION @ L1401 | `(defrule     (true)` | gl-scout-unit | — | — | — | — | — | — | **LOST** |
| 4 | L1791–L1800 | QEAGOL @ L1723 | `(defrule     (building-type-count town-center > 0)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 5 | L1802–L1810 | QEAGOL @ L1723 | `(defrule     (unit-type-count scout-cavalry-line > 0)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 6 | L1812–L1819 | QEAGOL @ L1723 | `(defrule     (true)` | gl-max-coordinate-value | — | — | — | — | — | — | **LOST** |
| 7 | L1821–L1832 | QEAGOL @ L1723 | `(defrule     (true)` | — | — | — | — | up-get-fact | — | — | **LOST** |
| 8 | L1834–L1845 | QEAGOL @ L1723 | `(defrule     (true)` | net-food-amount, net-gold-amount, net-stone-amount, net-wood-amount | — | — | — | up-get-fact | — | — | **LOST** |
| 9 | L1848–L1862 | QEAGOL @ L1723 | `(defrule     (taunt-detected me 100)     (goal gl-second-turn 1)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 10 | L1864–L1870 | QEAGOL @ L1723 | `(defrule     (goal gl-fifth-turn 1)     (taunt-detected me 100)` | — | — | — | — | — | — | — | **LOST** |
| 11 | L1872–L1877 | QEAGOL @ L1723 | `(defrule     (taunt-detected me 101)` | — | — | — | — | — | — | — | **LOST** |
| 12 | L1925–L1929 | QSETUP @ L1924 | `(defrule     (taunt-detected me 27)` | — | — | — | — | — | — | — | **LOST** |
| 13 | L1931–L1936 | QSETUP @ L1924 | `(defrule     (taunt-detected me 28)` | — | — | — | — | — | — | — | **LOST** |
| 14 | L1938–L1946 | QSETUP @ L1924 | `(defrule     (false)     (up-group-size c: RaidGroup > 0)     (goal gl-current-group RaidGroup)` | gl-current-group | — | — | — | — | 1 | — | **LOST** |
| 15 | L1948–L1955 | QSETUP @ L1924 | `(defrule     (false)     (up-group-size c: RangedGroup > 0)     (goal gl-current-group RangedGroup)` | gl-current-group | — | — | — | — | — | — | **LOST** |
| 16 | L1957–L1978 | QSETUP @ L1924 | `(defrule     (true)` | gl-current-group, gl-defend-town, gl-max-ranged-group-size, gl-range-advantage, sn-number-tasked-units | — | — | — | — | — | — | **LOST** |
| 17 | L1981–L1985 | QSETUP @ L1924 | `(defrule     (true)` | gl-tracking-range | — | — | — | — | — | — | **LOST** |
| 18 | L1987–L1991 | QSETUP @ L1924 | `(defrule     (true)` | gl-tracking-range | — | — | — | — | — | — | **LOST** |
| 19 | L1993–L1998 | QSETUP @ L1924 | `(defrule     (or	(goal gl-town-safe YES)     (up-point-distance home-x ranged-group-x >= 35))` | gl-tracking-range | — | — | — | — | — | — | **LOST** |
| 20 | L2000–L2004 | QSETUP @ L1924 | `(defrule     (research-completed ri-fletching)` | gl-tracking-range | — | — | — | research, research-completed | — | — | **LOST** |
| 21 | L2006–L2010 | QSETUP @ L1924 | `(defrule     (research-completed ri-bodkin-arrow)` | gl-tracking-range | — | — | — | research, research-completed | — | — | **LOST** |
| 22 | L2012–L2016 | QSETUP @ L1924 | `(defrule     (research-completed ri-elite-skirmisher)` | gl-tracking-range | — | — | — | research, research-completed | — | — | **LOST** |
| 23 | L2018–L2027 | QSETUP @ L1924 | `(defrule     (research-completed ri-fletching)` | gl-close-ranged-group-range, gl-enemy-tower-range, gl-my-tower-range, gl-raid-group-range, gl-ranged-group-range | — | — | — | research, research-completed | — | — | **LOST** |
| 24 | L2029–L2038 | QSETUP @ L1924 | `(defrule     (research-completed ri-bodkin-arrow)` | gl-close-ranged-group-range, gl-enemy-tower-range, gl-my-tower-range, gl-raid-group-range, gl-ranged-group-range | — | — | — | research, research-completed | — | — | **LOST** |
| 25 | L2040–L2046 | QSETUP @ L1924 | `(defrule     (research-completed ri-crossbow)` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 26 | L2048–L2055 | QSETUP @ L1924 | `(defrule     (research-completed ri-elite-skirmisher)` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 27 | L2058–L2064 | QADVANTAGE @ L2057 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (up-point-distance ranged-group-x enemy-group-x > 15))` | gl-ranged-eval | — | — | — | — | 44 | — | **LOST** |
| 28 | L2066–L2072 | QADVANTAGE @ L2057 | `(defrule     (true)` | gl-ranged-eval, goal, goal1 | — | — | — | — | — | — | **LOST** |
| 29 | L2075–L2088 | QADVANTAGE @ L2057 | `(defrule     (false)` | gl-ranged-eval, rt, sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 30 | L2091–L2096 | QADVANTAGE @ L2057 | `(defrule     (or	(up-research-status c: ri-fletching == research-pending)     (up-research-status c: ri-padded-archer-armor == research-pending))` | gl-ranged-eval | — | — | — | research-pending, up-research | — | — | **LOST** |
| 31 | L2099–L2103 | QADVANTAGE @ L2057 | `(defrule     (goal UP-FIRST 1)` | gl-ranged-eval | — | — | — | — | — | — | **LOST** |
| 32 | L2105–L2109 | QADVANTAGE @ L2057 | `(defrule     (goal UP-FIRST 0)` | gl-ranged-eval | — | — | — | — | — | — | **LOST** |
| 33 | L2112–L2118 | QADVANTAGE @ L2057 | `(defrule     (true)` | gl-ranged-eval, goal9 | — | — | — | — | — | — | **LOST** |
| 34 | L2121–L2132 | QADVANTAGE @ L2057 | `(defrule     (false)     (up-point-distance ranged-group-x enemy-group-x > 2)     (up-point-distance ranged-group-x enemy-group-x < 10)` | — | — | — | up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 35 | L2134–L2141 | QADVANTAGE @ L2057 | `(defrule     (false)     (up-compare-goal goal8 >= 1)` | gl-ranged-eval, goal8 | — | — | — | — | — | — | **LOST** |
| 36 | L2144–L2149 | QADVANTAGE @ L2057 | `(defrule     (true)` | gl-ranged-eval | — | — | — | — | — | — | **LOST** |
| 37 | L2152–L2161 | QADVANTAGE @ L2057 | `(defrule     (true)     (false)` | goal6, goal7 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 38 | L2163–L2177 | QADVANTAGE @ L2057 | `(defrule     (false)     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)     (up-get-object-data object-data-pierce-armor goal6)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 39 | L2179–L2184 | QADVANTAGE @ L2057 | `(defrule     (false)     (players-unit-type-count target-player skirmisher >= 6)` | goal | — | — | — | — | — | — | **LOST** |
| 40 | L2186–L2195 | QADVANTAGE @ L2057 | `(defrule     (false)     (goal SPLIT 1)     (up-compare-goal gl-armor-advantage >= 1)` | gl-armor-advantage, gl-ranged-eval | — | — | — | — | — | — | **LOST** |
| 41 | L2197–L2206 | QADVANTAGE @ L2057 | `(defrule     (false)     (goal SPLIT 1)     (up-compare-goal gl-armor-advantage < 1)` | gl-armor-advantage, gl-ranged-eval | — | — | — | — | — | — | **LOST** |
| 42 | L2208–L2213 | QADVANTAGE @ L2057 | `(defrule     (true)     (false)` | split | — | — | — | — | — | — | **LOST** |
| 43 | L2217–L2223 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal6, goal7, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 44 | L2226–L2234 | QADVANTAGE @ L2057 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 45 | L2237–L2243 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 46 | L2245–L2257 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)` | gl-range-advantage, goal7, split | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 47 | L2259–L2268 | QADVANTAGE @ L2057 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-range-advantage >= 1)` | gl-range-advantage | — | — | — | — | — | — | **LOST** |
| 48 | L2270–L2279 | QADVANTAGE @ L2057 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-range-advantage < 1)` | gl-range-advantage | — | — | — | — | — | — | **LOST** |
| 49 | L2281–L2285 | QADVANTAGE @ L2057 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 50 | L2288–L2297 | QADVANTAGE @ L2057 | `(defrule     (false)     (unit-type-count scout-cavalry-line > 0)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 51 | L2299–L2305 | QADVANTAGE @ L2057 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 52 | L2308–L2326 | QADVANTAGE @ L2057 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 53 | L2330–L2336 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal, goal6 | — | — | — | — | — | — | **LOST** |
| 54 | L2338–L2344 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal goal < 1)     (up-compare-goal gl-enemy-group-size < 5)` | gl-ranged-eval, goal6 | — | — | — | — | — | — | **LOST** |
| 55 | L2347–L2353 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal, goal5 | — | — | — | — | — | — | **LOST** |
| 56 | L2355–L2361 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal goal < 1)     (up-group-size c: RangedGroup < 5)` | gl-ranged-eval, goal5 | — | — | — | — | — | — | **LOST** |
| 57 | L2366–L2375 | QADVANTAGE @ L2057 | `(defrule     (players-unit-type-count any-ally knight-line > 0)` | goal1, rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 58 | L2378–L2385 | QADVANTAGE @ L2057 | `(defrule     (stance-toward focus-player ally)     (players-unit-type-count any-ally knight-line > 0)` | goal1 | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 59 | L2388–L2394 | QADVANTAGE @ L2057 | `(defrule     (player-valid focus-player)     (players-unit-type-count any-ally knight-line > 0)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 60 | L2396–L2402 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal goal1 > 0)     (players-unit-type-count any-ally knight-line > 0)` | gl-ranged-eval, goal1 | — | — | — | — | — | — | **LOST** |
| 61 | L2405–L2410 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal, lt | — | — | — | — | — | — | **LOST** |
| 62 | L2412–L2422 | QADVANTAGE @ L2057 | `(defrule     (unit-type-count knight-line > 0)` | goal | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 63 | L2424–L2430 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal lt > 0)     (unit-type-count knight-line > 0)     (research-completed ri-chain-barding)` | goal | — | — | — | research, research-completed | — | — | **LOST** |
| 64 | L2432–L2437 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal lt > 0)     (unit-type-count knight-line > 0)` | gl-ranged-eval | — | — | — | — | — | — | **LOST** |
| 65 | L2440–L2448 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal gl-enemy-group-size > 0)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 66 | L2450–L2455 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal lt > 0)` | gl-ranged-eval, lt | — | — | — | — | — | — | **LOST** |
| 67 | L2459–L2464 | QADVANTAGE @ L2057 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | — | **LOST** |
| 68 | L2467–L2473 | QADVANTAGE @ L2057 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-set-target-point | — | — | — | **LOST** |
| 69 | L2476–L2482 | QADVANTAGE @ L2057 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | up-get-search-state | up-get-search-state | -2 | — | **LOST** |
| 70 | L2484–L2488 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt < 1)` | rt | — | — | — | — | — | — | **LOST** |
| 71 | L2490–L2496 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt >= 1)` | gl-ranged-eval, rt | — | — | up-full-reset-search | — | — | — | **LOST** |
| 72 | L2499–L2517 | QADVANTAGE @ L2057 | `(defrule     (taunt-detected me 59)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 73 | L2519–L2524 | QADVANTAGE @ L2057 | `(defrule     (taunt-detected me 60)` | — | — | — | — | — | — | — | **LOST** |
| 74 | L2526–L2531 | QADVANTAGE @ L2057 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 75 | L2536–L2540 | QNA @ L2534 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 12 | — | **LOST** |
| 76 | L2542–L2551 | QNA @ L2534 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 77 | L2553–L2563 | QNA @ L2534 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 78 | L2565–L2572 | QNA @ L2534 | `(defrule     (false)     (goal gl-can-move NO)     (up-compare-goal gl-target-distance g:> gl-ranged-group-range)` | gl-can-move | — | — | — | — | — | — | **LOST** |
| 79 | L2574–L2581 | QNA @ L2534 | `(defrule     (false)     (goal gl-can-move YES)     (up-compare-goal gl-target-distance g:<= gl-ranged-group-range)` | gl-can-move | — | — | — | — | — | — | **LOST** |
| 80 | L2590–L2598 | QNA @ L2534 | `(defrule     (up-compare-goal gl-can-fire != YES)     (up-compare-goal gl-highest-next-attack <= firing-threshold-1)` | — | — | — | — | — | — | — | **LOST** |
| 81 | L2600–L2609 | QNA @ L2534 | `(defrule     (timer-triggered t-failsafe)     (up-compare-goal gl-can-fire != YES)     (up-compare-goal gl-target-distance g:<= gl-ranged-group-range)` | — | t-failsafe | — | — | — | — | — | **LOST** |
| 82 | L2611–L2618 | QNA @ L2534 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 83 | L2621–L2629 | QNA @ L2534 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 84 | L2631–L2639 | QNA @ L2534 | `(defrule     (timer-triggered t-failsafe)     (up-compare-goal gl-can-move != YES)` | — | t-failsafe | — | — | — | — | — | **LOST** |
| 85 | L2641–L2649 | QNA @ L2534 | `(defrule     (taunt-detected me 63)` | — | — | — | — | — | — | — | **LOST** |
| 86 | L2651–L2656 | QNA @ L2534 | `(defrule     (taunt-detected me 64)` | — | — | — | — | — | — | — | **LOST** |
| 87 | L2658–L2664 | QNA @ L2534 | `(defrule     (false)` | — | — | — | — | — | — | — | **LOST** |
| 88 | L2667–L2671 | QTARGET STUFF @ L2666 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 56 | — | **LOST** |
| 89 | L2673–L2686 | QTARGET STUFF @ L2666 | `(defrule     (true)` | gl-target-class, gl-target-distance, gl-target-hp, gl-target-type, goal, rt, target-id, target-x, target-y | — | — | up-full-reset-search | — | — | — | **LOST** |
| 90 | L2690–L2703 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)` | goal, sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 91 | L2707–L2711 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 92 | L2714–L2725 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)     (up-compare-goal gl-ranged-eval >= WinningFight)     (up-compare-goal gl-ranged-group-state != M...` | split | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 93 | L2727–L2734 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 94 | L2736–L2743 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 95 | L2745–L2750 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-get-search-state | up-get-search-state | — | — | **LOST** |
| 96 | L2753–L2759 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -5 | — | **LOST** |
| 97 | L2763–L2767 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 98 | L2770–L2778 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-set-target-point | — | — | — | **LOST** |
| 99 | L2780–L2787 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 100 | L2789–L2796 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 101 | L2798–L2805 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 102 | L2808–L2814 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -5 | — | **LOST** |
| 103 | L2818–L2822 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 104 | L2825–L2835 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | goal, split | — | — | up-find-remote, up-set-target-point | — | — | — | **LOST** |
| 105 | L2837–L2844 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 106 | L2846–L2853 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 107 | L2855–L2862 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 108 | L2865–L2871 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -5 | — | **LOST** |
| 109 | L2875–L2879 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 110 | L2882–L2895 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 111 | L2897–L2905 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (goal gl-ranged-group-state MINI-RETREAT)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 112 | L2907–L2915 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-ranged-group-state != MINI-RETREAT)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 113 | L2918–L2924 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -4 | — | **LOST** |
| 114 | L2928–L2932 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 115 | L2935–L2942 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-set-target-point | — | — | — | **LOST** |
| 116 | L2944–L2953 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 117 | L2956–L2962 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | — | **LOST** |
| 118 | L2967–L2971 | QUICKIES @ L2964 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 119 | L2974–L2992 | QUICKIES @ L2964 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 120 | L2994–L2998 | QUICKIES @ L2964 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 121 | L3000–L3004 | QUICKIES @ L2964 | `(defrule     (goal gl-switch 1)` | goal | — | — | — | — | — | — | **LOST** |
| 122 | L3006–L3013 | QUICKIES @ L2964 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 123 | L3015–L3022 | QUICKIES @ L2964 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 124 | L3024–L3031 | QUICKIES @ L2964 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 125 | L3034–L3040 | QUICKIES @ L2964 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -7 | — | **LOST** |
| 126 | L3045–L3049 | QUICKIES @ L3042 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 127 | L3052–L3062 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 128 | L3064–L3068 | QUICKIES @ L3042 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 129 | L3070–L3074 | QUICKIES @ L3042 | `(defrule     (goal gl-switch 1)` | goal | — | — | — | — | — | — | **LOST** |
| 130 | L3076–L3083 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 131 | L3085–L3092 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 132 | L3094–L3101 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 133 | L3104–L3110 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -7 | — | **LOST** |
| 134 | L3115–L3119 | QUICKIES @ L3042 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 135 | L3122–L3130 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-set-target-point | — | — | — | **LOST** |
| 136 | L3132–L3136 | QUICKIES @ L3042 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 137 | L3138–L3142 | QUICKIES @ L3042 | `(defrule     (goal gl-switch 1)` | goal | — | — | — | — | — | — | **LOST** |
| 138 | L3144–L3151 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 139 | L3153–L3160 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 140 | L3162–L3169 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 141 | L3171–L3178 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 142 | L3180–L3185 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)` | split | — | — | up-get-search-state | up-get-search-state | — | — | **LOST** |
| 143 | L3188–L3194 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -9 | — | **LOST** |
| 144 | L3197–L3202 | QUICKIES @ L3042 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-point | — | — | — | **LOST** |
| 145 | L3205–L3216 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 146 | L3219–L3224 | QUICKIES @ L3042 | `(defrule     (taunt-detected me 61)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 147 | L3226–L3237 | QUICKIES @ L3042 | `(defrule     (taunt-detected me 61)` | — | — | — | — | — | — | — | **LOST** |
| 148 | L3239–L3244 | QUICKIES @ L3042 | `(defrule     (taunt-detected me 62)` | — | — | — | — | — | — | — | **LOST** |
| 149 | L3247–L3257 | QMISC @ L3246 | `(defrule     (goal gl-thirty-turn 1)     (current-age >= feudal-age)` | split | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 150 | L3259–L3270 | QMISC @ L3246 | `(defrule     (goal SPLIT 1)     (up-compare-goal lt > 0)` | — | — | — | — | — | — | — | **LOST** |
| 151 | L3272–L3276 | QMISC @ L3246 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 152 | L3280–L3286 | QMISC @ L3246 | `(defrule     (players-building-type-count every-enemy town-center < 1)` | nearest-tc-x, nearest-tc-y | — | — | — | — | 12 | — | **LOST** |
| 153 | L3288–L3292 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 5 | — | **LOST** |
| 154 | L3295–L3304 | QMISC @ L3246 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 155 | L3307–L3313 | QMISC @ L3246 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 156 | L3316–L3322 | QMISC @ L3246 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 157 | L3324–L3329 | QMISC @ L3246 | `(defrule     (up-compare-goal rt >= 1)` | — | — | — | up-clean-search, up-set-target-point | — | — | — | **LOST** |
| 158 | L3331–L3339 | QMISC @ L3246 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 159 | L3343–L3349 | QMISC @ L3246 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | — | **LOST** |
| 160 | L3352–L3356 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | — | **LOST** |
| 161 | L3359–L3365 | QMISC @ L3246 | `(defrule     (false)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 162 | L3367–L3372 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | up-clean-search, up-set-target-point | — | — | — | **LOST** |
| 163 | L3374–L3379 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup >= 1)` | — | — | — | up-clean-search, up-set-target-point | — | — | — | **LOST** |
| 164 | L3381–L3386 | QMISC @ L3246 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 165 | L3388–L3392 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 34 | — | **LOST** |
| 166 | L3395–L3402 | QMISC @ L3246 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (players-building-type-count every-enemy castle < 1))` | nearest-castle-x, nearest-castle-y | — | — | — | — | 5 | — | **LOST** |
| 167 | L3405–L3411 | QMISC @ L3246 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | — | **LOST** |
| 168 | L3414–L3418 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | — | **LOST** |
| 169 | L3421–L3426 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 170 | L3428–L3433 | QMISC @ L3246 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-point | — | — | — | **LOST** |
| 171 | L3435–L3440 | QMISC @ L3246 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 172 | L3443–L3450 | QMISC @ L3246 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (players-building-type-count every-enemy watch-tower < 1))` | nearest-tower-x, nearest-tower-y | — | — | — | — | 5 | — | **LOST** |
| 173 | L3453–L3459 | QMISC @ L3246 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | — | **LOST** |
| 174 | L3462–L3466 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | — | **LOST** |
| 175 | L3469–L3474 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 176 | L3476–L3481 | QMISC @ L3246 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-point | — | — | — | **LOST** |
| 177 | L3483–L3488 | QMISC @ L3246 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 178 | L3492–L3498 | QMISC @ L3246 | `(defrule     (true)` | gl-mangos-nearby, goal, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 179 | L3501–L3510 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-mangos-nearby | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 180 | L3513–L3518 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 181 | L3522–L3527 | QMISC @ L3246 | `(defrule     (true)` | gl-units-in-close-range, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 182 | L3530–L3544 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-units-in-close-range | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 183 | L3547–L3552 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 184 | L3556–L3562 | QMISC @ L3246 | `(defrule     (true)` | gl-total-military-in-range, gl-total-units-in-range, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 185 | L3565–L3580 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-total-military-in-range, gl-total-units-in-range | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 186 | L3583–L3588 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 187 | L3590–L3603 | QMISC @ L3246 | `(defrule     (taunt-detected me 50)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 188 | L3605–L3610 | QMISC @ L3246 | `(defrule     (taunt-detected me 51)` | — | — | — | — | — | — | — | **LOST** |
| 189 | L3612–L3616 | QMISC @ L3246 | `(defrule     (false)` | goal | — | — | — | — | — | — | **LOST** |
| 190 | L3618–L3624 | QMISC @ L3246 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 191 | L3627–L3633 | QMISC @ L3246 | `(defrule     (true)` | gl-melee-in-range, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 192 | L3636–L3649 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-melee-in-range, split | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 193 | L3651–L3661 | QMISC @ L3246 | `(defrule     (goal SPLIT 1)` | gl-melee-in-range | — | — | up-find-remote, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 194 | L3664–L3671 | QMISC @ L3246 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | — | — | — | — | — | — | — | **LOST** |
| 195 | L3674–L3679 | QMISC @ L3246 | `(defrule     (true)` | gl-cavalry-attacking, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 196 | L3682–L3696 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 197 | L3699–L3704 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 198 | L3707–L3712 | QMISC @ L3246 | `(defrule     (true)` | gl-enemy-group-size, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 199 | L3715–L3728 | QMISC @ L3246 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 200 | L3731–L3736 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 201 | L3739–L3749 | QMISC @ L3246 | `(defrule     (game-time > 5)     (or	(taunt-detected me 19)     (taunt-detected any-enemy 19))` | — | — | — | — | — | — | — | **LOST** |
| 202 | L3752–L3763 | QMPOINTS @ L3751 | `(defrule     (goal gl-tenth-turn 1)     (taunt-detected me 89)` | — | — | — | — | — | — | — | **LOST** |
| 203 | L3765–L3770 | QMPOINTS @ L3751 | `(defrule     (taunt-detected me 90)` | — | — | — | — | — | — | — | **LOST** |
| 204 | L3773–L3778 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingFour)` | — | — | — | — | — | — | — | **LOST** |
| 205 | L3780–L3785 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingThree)` | — | — | — | — | — | — | — | **LOST** |
| 206 | L3787–L3792 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingTwo)` | — | — | — | — | — | — | — | **LOST** |
| 207 | L3794–L3799 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingOne)` | — | — | — | — | — | — | — | **LOST** |
| 208 | L3802–L3811 | QMPOINTS @ L3751 | `(defrule     (game-time < 1500)` | — | — | — | — | — | — | — | **LOST** |
| 209 | L3813–L3822 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (up-group-size c: RangedGroup > 0)     (up-point-distance march-x home-x < 3)` | — | — | — | — | — | — | — | **LOST** |
| 210 | L3825–L3836 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-march-type == DefendingLC)` | — | — | — | — | — | — | — | **LOST** |
| 211 | L3838–L3849 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-set-target-object search-local c: 0)     (up-compare-goal gl-march-type == DefendingLC)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 212 | L3851–L3862 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-march-type == DefendingMill)` | — | — | — | — | — | — | — | **LOST** |
| 213 | L3864–L3875 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-set-target-object search-local c: 0)     (up-compare-goal gl-march-type == DefendingMill)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 214 | L3878–L3890 | QMPOINTS @ L3751 | `(defrule     (game-time > 2)     (goal gl-tenth-turn 1)     (players-building-type-count target-player town-center > 0)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 215 | L3892–L3909 | QMPOINTS @ L3751 | `(defrule     (game-time > 5)     (goal gl-attacking YES)     (goal gl-thirty-turn 1)     (players-building-count target-player > 0)     (players-building-type-count target-playe...` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 216 | L3911–L3927 | QMPOINTS @ L3751 | `(defrule     (game-time > 5)     (goal gl-attacking NO)     (goal gl-thirty-turn 1)     (players-building-count target-player > 0)     (players-building-type-count target-player...` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 217 | L3930–L3941 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 218 | L3943–L3955 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 219 | L3957–L3969 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 220 | L3971–L3982 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 221 | L3984–L3992 | QMPOINTS @ L3751 | `(defrule     (or	(game-time < 5)     (or	(goal gl-defend-town YES)     (or	(goal gl-attacking NO)     (or	(players-building-type-count target-player town-center < 1)     (up-gro...` | — | — | — | — | — | 12 | — | **LOST** |
| 222 | L3995–L4006 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 223 | L4008–L4016 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type | — | — | — | — | — | — | **LOST** |
| 224 | L4018–L4029 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 225 | L4031–L4039 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 226 | L4041–L4049 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type | — | — | — | — | — | — | **LOST** |
| 227 | L4052–L4066 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 228 | L4068–L4079 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 229 | L4081–L4088 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type, split | — | — | — | — | 4 | — | **LOST** |
| 230 | L4091–L4097 | QMPOINTS @ L3751 | `(defrule     (goal gl-march-type MarchingTwo)     (or (taunt-detected me 85)     (up-point-distance ranged-group-x march-x < 5))` | split | — | — | — | — | — | — | **LOST** |
| 231 | L4099–L4106 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type, split | — | — | — | — | 2 | — | **LOST** |
| 232 | L4109–L4115 | QMPOINTS @ L3751 | `(defrule     (goal gl-march-type MarchingThree)     (or (taunt-detected me 85)     (up-point-distance ranged-group-x march-x < 5))` | split | — | — | — | — | — | — | **LOST** |
| 233 | L4117–L4123 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type, split | — | — | — | — | — | — | **LOST** |
| 234 | L4125–L4130 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 235 | L4134–L4148 | QMINIS @ L4132 | `(defrule     (true)     (goal gl-fifth-turn 1)     (up-group-size c: RangedGroup < 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 236 | L4150–L4165 | QMINIS @ L4132 | `(defrule     (false)` | — | — | — | — | — | — | — | **LOST** |
| 237 | L4171–L4178 | QMINIS @ L4132 | `(defrule     (or	(game-time < 10)     (or	(goal gl-getting-sheep YES)     (or	(unit-type-count scout-cavalry-line < 1)     (goal NEWSCOUTING FINISHED))))` | — | — | — | — | — | 6 | — | **LOST** |
| 238 | L4180–L4188 | QMINIS @ L4132 | `(defrule     (goal gl-seventh-turn 1)     (up-compare-goal NEWSCOUTING >= 45)     (unit-type-count scout-cavalry-line > 0)     (up-point-distance saved-scout-x scout-x < 1)` | — | — | — | — | — | — | — | **LOST** |
| 239 | L4190–L4201 | QMINIS @ L4132 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-scout-stuck 0)     (up-compare-goal NEWSCOUTING < 45)     (up-point-distance saved-scout-x scout-x < 2)` | — | — | — | — | — | — | — | **LOST** |
| 240 | L4203–L4217 | QMINIS @ L4132 | `(defrule     (goal gl-scout-stuck 2)     (up-timer-status 28 == timer-running)` | — | 28 | — | up-full-reset-search | — | — | — | **LOST** |
| 241 | L4219–L4227 | QMINIS @ L4132 | `(defrule     (goal gl-scout-stuck 2)     (or	(timer-triggered 28)     (up-point-distance scout-x saved-scout-x >= 3))` | — | 28 | — | — | — | — | — | **LOST** |
| 242 | L4229–L4238 | QMINIS @ L4132 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-scout-stuck 0)     (up-point-distance saved-scout-x scout-x >= 4)` | — | — | — | — | — | — | — | **LOST** |
| 243 | L4240–L4247 | QMINIS @ L4132 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-scout-stuck -1)` | — | — | — | — | — | — | — | **LOST** |
| 244 | L4250–L4256 | QMINIS @ L4132 | `(defrule     (taunt-detected me 103)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 245 | L4258–L4263 | QMINIS @ L4132 | `(defrule     (taunt-detected me 103)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 246 | L4265–L4270 | QMINIS @ L4132 | `(defrule     (taunt-detected me 104)` | — | — | — | — | — | — | — | **LOST** |
| 247 | L4277–L4283 | QMINIS @ L4132 | `(defrule     (building-type-count lumber-camp == 1)` | — | — | — | up-find-local, up-full-reset-search | — | — | — | **LOST** |
| 248 | L4285–L4297 | QMINIS @ L4132 | `(defrule     (building-type-count lumber-camp == 1)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 249 | L4299–L4316 | QMINIS @ L4132 | `(defrule     (building-type-count lumber-camp == 1)     (up-set-target-object search-local c: 0)` | sn-focus-player-number | — | — | up-clean-search, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 250 | L4319–L4326 | QMINIS @ L4132 | `(defrule     (false)     (building-type-count lumber-camp == 2)` | — | — | — | up-find-local, up-full-reset-search | — | — | — | **LOST** |
| 251 | L4328–L4341 | QMINIS @ L4132 | `(defrule     (false)     (building-type-count lumber-camp == 2)     (up-set-target-object search-local c: 0)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-set-target-object, up-set-target-point | — | — | — | **LOST** |
| 252 | L4343–L4361 | QMINIS @ L4132 | `(defrule     (false)     (building-type-count lumber-camp == 2)     (up-set-target-object search-local c: 0)` | sn-focus-player-number | — | — | up-clean-search, up-full-reset-search, up-set-target-object | up-target-objects | — | — | **LOST** |
| 253 | L4364–L4381 | QMINIS @ L4132 | `(defrule     (current-age == castle-age)     (goal gl-current-build-item ESKIRMS)     (building-type-count archery-range >= 1)     (research-available ri-elite-skirmisher)     (...` | — | — | — | up-full-reset-search | research, research-pending, up-pending-objects, up-research | — | — | **LOST** |
| 254 | L4384–L4391 | QHOUSES @ L4383 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 255 | L4393–L4398 | QHOUSES @ L4383 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | — | **LOST** |
| 256 | L4400–L4408 | QHOUSES @ L4383 | `(defrule     (goal goal -1)` | — | — | — | up-full-reset-search, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 257 | L4410–L4420 | QHOUSES @ L4383 | `(defrule     (goal goal -1)     (up-compare-goal lt >= 1)     (up-set-target-object search-local c: 0)` | split | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 258 | L4422–L4438 | QHOUSES @ L4383 | `(defrule     (goal goal -1)     (goal SPLIT 1)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 259 | L4440–L4453 | QHOUSES @ L4383 | `(defrule     (goal goal 0)     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | goal | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 260 | L4455–L4472 | QHOUSES @ L4383 | `(defrule     (goal goal 1)     (up-compare-goal rt >= 3)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object, up-set-target-point | up-target-point | — | — | **LOST** |
| 261 | L4476–L4483 | QLC @ L4474 | `(defrule     (true)` | split | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 262 | L4485–L4496 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-trees-around, sn-focus-player-number | — | — | up-get-search-state | up-get-search-state | — | — | **LOST** |
| 263 | L4498–L4503 | QLC @ L4474 | `(defrule     (true)` | sn-lumber-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 264 | L4505–L4516 | QLC @ L4474 | `(defrule     (game-time >= 90)     (goal gl-dark-build LumberFirst)     (up-compare-goal gl-trees-around < 12)` | — | — | — | — | — | — | — | **LOST** |
| 265 | L4518–L4523 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 1)` | sn-lumber-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 266 | L4525–L4531 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 3)` | sn-lumber-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 267 | L4533–L4539 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 4)` | sn-lumber-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 268 | L4541–L4547 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 5)` | sn-lumber-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 269 | L4549–L4556 | QLC @ L4474 | `(defrule     (taunt-detected me 97)` | — | — | — | — | — | — | — | **LOST** |
| 270 | L4558–L4563 | QLC @ L4474 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 271 | L4565–L4578 | QLC @ L4474 | `(defrule     (goal gl-lclerp -1)` | split | — | — | up-full-reset-search, up-set-target-object, up-set-target-point | — | — | — | **LOST** |
| 272 | L4580–L4596 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-lclerp, sn-focus-player-number, split | — | — | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-object | up-get-search-state | — | — | **LOST** |
| 273 | L4598–L4604 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)     (up-compare-goal rt < 7)` | gl-lclerp | — | — | — | — | — | — | **LOST** |
| 274 | L4606–L4611 | QLC @ L4474 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 275 | L4613–L4620 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (up-compare-goal goal >= 2)` | — | — | — | — | — | -2 | — | **LOST** |
| 276 | L4622–L4628 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (up-compare-goal goal < 2)` | gl-lclerp | — | — | — | — | — | — | **LOST** |
| 277 | L4630–L4635 | QLC @ L4474 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 278 | L4637–L4647 | QLC @ L4474 | `(defrule     (goal gl-lclerp -1)` | split | — | — | up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 279 | L4649–L4663 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-lclerp, sn-focus-player-number, split | — | — | up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 280 | L4665–L4671 | QLC @ L4474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 281 | L4673–L4680 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)     (building-type-count lumber-camp < 2)     (up-point-distance point-x home-x < 15)` | — | — | — | — | — | 1 | — | **LOST** |
| 282 | L4682–L4688 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)     (up-compare-goal rt < 7)` | — | — | — | — | — | 2 | — | **LOST** |
| 283 | L4690–L4694 | QLC @ L4474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 284 | L4696–L4703 | QLC @ L4474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 285 | L4705–L4717 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)` | sn-focus-player-number, split | — | — | up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 286 | L4719–L4730 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-lclerp, split | — | — | up-clean-search, up-remove-objects, up-set-target-object | — | — | — | **LOST** |
| 287 | L4732–L4740 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (up-can-build-line 0 point-x c: palisade-wall)` | — | — | — | — | — | — | — | **LOST** |
| 288 | L4742–L4747 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (not(up-can-build-line gl-escrow-state point-x c: house))` | gl-lclerp | — | — | — | — | — | — | **LOST** |
| 289 | L4749–L4756 | QLC @ L4474 | `(defrule     (goal gl-lclerp 2)     (not(up-can-build-line gl-escrow-state point-x c: house))` | — | — | — | — | — | -1 | — | **LOST** |
| 290 | L4758–L4764 | QLC @ L4474 | `(defrule     (goal gl-lclerp 2)     (up-can-build-line gl-escrow-state point-x c: house)` | gl-lclerp | — | — | — | — | — | — | **LOST** |
| 291 | L4766–L4780 | QLC @ L4474 | `(defrule     (goal gl-lclerp 3)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-target-point | — | — | **LOST** |
| 292 | L4782–L4789 | QLC @ L4474 | `(defrule     (goal gl-lclerp 3)` | — | — | — | — | up-build | — | — | **LOST** |
| 293 | L4791–L4797 | QLC @ L4474 | `(defrule     (goal gl-lclerp 4)     (up-pending-objects c: lumber-camp < 1)` | gl-lclerp | — | — | — | up-pending-objects | — | — | **LOST** |
| 294 | L4803–L4808 | QANTI-TRUSH @ L4799 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 295 | L4811–L4820 | QANTI-TRUSH @ L4799 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 296 | L4823–L4829 | QANTI-TRUSH @ L4799 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 297 | L4831–L4837 | QANTI-TRUSH @ L4799 | `(defrule     (goal gl-trushed YES)     (up-compare-goal rt < 1)` | gl-trushed | — | — | — | — | — | — | **LOST** |
| 298 | L4839–L4855 | QANTI-TRUSH @ L4799 | `(defrule     (game-time < 900)` | — | — | — | — | — | — | — | **LOST** |
| 299 | L4857–L4861 | QANTI-TRUSH @ L4799 | `(defrule     (goal gl-trushed YES)` | — | — | — | — | up-target-objects | — | — | **LOST** |
| 300 | L4864–L4869 | QGARRISONING TC @ L4863 | `(defrule     (false)` | — | — | — | — | — | — | — | **LOST** |
| 301 | L4871–L4877 | QGARRISONING TC @ L4863 | `(defrule     (true)` | goal, goal1, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 302 | L4879–L4889 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (stance-toward focus-player enemy)` | goal | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 303 | L4891–L4899 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (up-compare-goal goal > 0)     (up-set-target-object search-remote c: 0)` | gl-saved-focus-player, split | — | — | up-set-target-object | — | 1 | — | **LOST** |
| 304 | L4901–L4907 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | — | **LOST** |
| 305 | L4909–L4918 | QGARRISONING TC @ L4863 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects | — | — | — | **LOST** |
| 306 | L4920–L4925 | QGARRISONING TC @ L4863 | `(defrule     (goal SPLIT 1)     (unit-type-count sheep > 0)` | — | — | — | up-remove-objects | — | — | — | **LOST** |
| 307 | L4927–L4931 | QGARRISONING TC @ L4863 | `(defrule     (true)` | — | — | — | up-get-search-state | up-get-search-state | — | — | **LOST** |
| 308 | L4933–L4942 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (up-compare-goal lt >= 1)     (up-compare-goal goal >= 1)` | — | — | — | — | up-target-objects | — | — | **LOST** |
| 309 | L4944–L4953 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc 1)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 310 | L4955–L4962 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc 1)     (up-compare-goal rt < 1)` | — | — | — | — | — | — | — | **LOST** |
| 311 | L4964–L4968 | QGARRISONING TC @ L4863 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 312 | L4972–L4976 | QVILLS @ L4970 | `(defrule     (goal enemy-attack-x -1)` | — | — | — | — | — | 9 | — | **LOST** |
| 313 | L4978–L4984 | QVILLS @ L4970 | `(defrule     (true)` | gl-enemy-attack-size, sn-focus-player-number | — | — | up-set-target-point | — | — | — | **LOST** |
| 314 | L4986–L4997 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)` | gl-enemy-attack-size | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 315 | L4999–L5004 | QVILLS @ L4970 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 316 | L5006–L5011 | QVILLS @ L4970 | `(defrule     (true)` | goal, lt | — | — | — | — | — | — | **LOST** |
| 317 | L5013–L5018 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 318 | L5020–L5031 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 319 | L5033–L5041 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 320 | L5043–L5053 | QVILLS @ L4970 | `(defrule     (true)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 321 | L5055–L5064 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 322 | L5068–L5072 | QVILLS @ L4970 | `(defrule     (players-military-population every-enemy >= 17)` | — | — | — | — | — | 6 | — | **LOST** |
| 323 | L5075–L5081 | QVILLS @ L4970 | `(defrule     (true)` | goal, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 324 | L5084–L5093 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 325 | L5096–L5102 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 326 | L5104–L5114 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 327 | L5116–L5132 | QVILLS @ L4970 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt >= 1)     (up-point-distance point-x home-x < 25)` | — | — | — | up-clean-search, up-find-remote, up-remove-objects, up-set-target-point | up-target-objects | — | — | **LOST** |
| 328 | L5134–L5146 | QVILLS @ L4970 | `(defrule     (goal gl-skirm-vills 3)     (or	(goal gl-ninety-turn 1)     (or	(up-compare-goal lt < 1)     (up-point-distance point-x home-x >= 30)))` | — | — | — | — | — | — | — | **LOST** |
| 329 | L5149–L5154 | QVILLS @ L4970 | `(defrule     (false)     (goal gl-town-safe YES)` | — | — | — | — | — | 8 | — | **LOST** |
| 330 | L5158–L5169 | QVILLS @ L4970 | `(defrule     (true)` | enemy-attack-x, enemy-attack-y, goal, goal1, point-x, point-y, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 331 | L5171–L5175 | QVILLS @ L4970 | `(defrule     (current-age == feudal-age)` | goal | — | — | — | — | — | — | **LOST** |
| 332 | L5177–L5181 | QVILLS @ L4970 | `(defrule     (current-age >= castle-age)` | goal | — | — | — | — | — | — | **LOST** |
| 333 | L5183–L5191 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 334 | L5193–L5203 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)     (up-set-target-object search-remote c: 0)` | goal1, point-x, point-y | — | — | up-get-search-state, up-set-target-object | up-get-object-data, up-get-search-state | — | — | **LOST** |
| 335 | L5205–L5212 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt > 0)     (stance-toward focus-player enemy)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | — | **LOST** |
| 336 | L5214–L5219 | QVILLS @ L4970 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -4 | — | **LOST** |
| 337 | L5221–L5227 | QVILLS @ L4970 | `(defrule     (up-compare-goal goal1 > 0)` | point-x, point-y | — | — | — | — | — | — | **LOST** |
| 338 | L5231–L5238 | QVILLS @ L4970 | `(defrule     (true)` | goal, goal1, goal2, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 339 | L5241–L5250 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 340 | L5253–L5259 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 341 | L5261–L5276 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | goal, goal1, split | — | — | up-find-local, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 342 | L5278–L5287 | QVILLS @ L4970 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 343 | L5289–L5299 | QVILLS @ L4970 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal1 > 0)` | — | — | — | — | — | — | — | **LOST** |
| 344 | L5301–L5309 | QVILLS @ L4970 | `(defrule     (taunt-detected me 30)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 345 | L5311–L5316 | QVILLS @ L4970 | `(defrule     (taunt-detected me 31)` | — | — | — | — | — | — | — | **LOST** |
| 346 | L5318–L5322 | QVILLS @ L4970 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 347 | L5325–L5330 | QVILLS @ L4970 | `(defrule     (players-current-age-time every-enemy >= 60)     (players-current-age every-enemy >= castle-age)` | — | — | — | — | — | 8 | — | **LOST** |
| 348 | L5333–L5337 | QVILLS @ L4970 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 349 | L5340–L5353 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 350 | L5356–L5362 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 351 | L5364–L5379 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 352 | L5381–L5392 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt == 1)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 353 | L5394–L5405 | QVILLS @ L4970 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt >= 1)     (up-point-distance point-x home-x < 25)` | split | — | — | up-clean-search, up-find-remote, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 354 | L5407–L5421 | QVILLS @ L4970 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-point | up-target-objects | — | — | **LOST** |
| 355 | L5423–L5436 | QVILLS @ L4970 | `(defrule     (goal gl-aggressive-vills 3)     (or	(goal gl-ninety-turn 1)     (or	(up-point-distance point-x home-x >= 30)     (and(up-compare-goal lt < 1)     (up-timer-status ...` | — | t-infantry-attack | — | — | — | — | — | **LOST** |
| 356 | L5440–L5445 | QVILLS @ L4970 | `(defrule     (or	(goal gl-aggressive-vills 1)` | — | — | — | — | — | — | — | **LOST** |
| 357 | L5448–L5453 | QVILLS @ L4970 | `(defrule     (true)` | goal2, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 358 | L5456–L5466 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 359 | L5469–L5475 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 360 | L5477–L5490 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 361 | L5492–L5501 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 1)     (goal gl-aggressive-vills -1)` | — | — | — | up-clean-search, up-remove-objects | up-target-objects | — | — | **LOST** |
| 362 | L5503–L5513 | QVILLS @ L4970 | `(defrule     (up-compare-goal goal1 < 1)     (goal gl-aggressive-vills 0)` | — | — | — | — | — | — | — | **LOST** |
| 363 | L5516–L5520 | QVILLS @ L4970 | `(defrule     (players-current-age every-enemy >= castle-age)` | — | — | — | — | — | 5 | — | **LOST** |
| 364 | L5523–L5529 | QVILLS @ L4970 | `(defrule     (true)` | goal1, goal2, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 365 | L5532–L5541 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 366 | L5544–L5550 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 367 | L5552–L5565 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 368 | L5567–L5576 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 2)     (goal gl-aggressive-vills -1)` | — | — | — | up-clean-search, up-remove-objects | up-target-objects | — | — | **LOST** |
| 369 | L5578–L5588 | QVILLS @ L4970 | `(defrule     (up-compare-goal goal1 < 1)     (goal gl-aggressive-vills 1)` | — | — | — | — | — | — | — | **LOST** |
| 370 | L5590–L5597 | QVILLS @ L4970 | `(defrule     (taunt-detected me 95)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 371 | L5599–L5604 | QVILLS @ L4970 | `(defrule     (taunt-detected me 96)` | — | — | — | — | — | — | — | **LOST** |
| 372 | L5607–L5618 | QVILLS @ L4970 | `(defrule     (false)     (game-time > 5)     (up-compare-goal gl-threat-time < 1000)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 373 | L5620–L5632 | QVILLS @ L4970 | `(defrule     (false)     (game-time > 5)     (goal gl-tenth-turn 1)     (up-compare-goal gl-threat-time < 1000)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-objects | — | — | **LOST** |
| 374 | L5636–L5642 | QVILLS @ L4970 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 375 | L5645–L5655 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)     (players-unit-type-count focus-player battering-ram-line > 0)` | — | — | — | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 376 | L5658–L5664 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 377 | L5666–L5683 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)     (players-unit-type-count focus-player battering-ram-line > 0)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-search-state, up-target-objects | — | — | **LOST** |
| 378 | L5687–L5700 | QSHEEP @ L5685 | `(defrule     (game-time < 300)` | — | — | — | — | — | — | — | **LOST** |
| 379 | L5703–L5708 | QSHEEP @ L5685 | `(defrule     (or	(up-compare-goal gl-current-sheep-count < 3)     (goal gl-sheep-scouting FINISHED))` | — | — | — | — | — | 11 | — | **LOST** |
| 380 | L5710–L5721 | QSHEEP @ L5685 | `(defrule     (up-compare-goal gl-current-sheep-count >= 3)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 381 | L5723–L5728 | QSHEEP @ L5685 | `(defrule     (up-set-target-by-id g: sheep1-id)` | — | — | — | — | — | — | — | **LOST** |
| 382 | L5730–L5736 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal gl-sheep-scouting >= 0)` | — | — | — | — | — | — | — | **LOST** |
| 383 | L5738–L5746 | QSHEEP @ L5685 | `(defrule     (goal gl-sheep-scouting 0)     (up-point-distance point2-x home-x < 50)     (up-point-distance point2-x home-x >= 18)` | — | — | — | — | — | — | — | **LOST** |
| 384 | L5748–L5756 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 0)` | — | — | — | — | — | — | — | **LOST** |
| 385 | L5758–L5766 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 1)` | — | — | — | — | — | — | — | **LOST** |
| 386 | L5768–L5777 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 1)` | — | — | — | — | — | — | — | **LOST** |
| 387 | L5779–L5789 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 1)     (up-point-distance point-x point2-x < 3)` | — | — | — | — | — | — | — | **LOST** |
| 388 | L5791–L5803 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (up-set-target-by-id g: sheep1-id)     (up-compare-goal gl-sheep-scouting < 2)     (up-compare-goal gl-sheep-scouting >= 0)` | — | — | — | — | — | — | — | **LOST** |
| 389 | L5805–L5818 | QSHEEP @ L5685 | `(defrule     (game-time >= 60)     (up-set-target-by-id g: sheep1-id)     (or	(game-time >= 200)     (and(game-time >= 122)     (up-compare-goal gl-current-sheep-count == 4)))` | — | — | — | — | — | — | — | **LOST** |
| 390 | L5820–L5826 | QSHEEP @ L5685 | `(defrule     (false)     (goal gl-sheep-scouting 2)     (up-set-target-by-id g: sheep1-id)` | — | — | — | — | — | — | — | **LOST** |
| 391 | L5829–L5837 | QNEWSCOUTING @ L5828 | `(defrule     (true)     (or	(game-time < 2)     (or	(current-age > dark-age)     (or	(up-compare-goal NEWSCOUTING >= 50)     (up-timer-status 28 == timer-running))))` | — | 28 | — | — | — | 33 | — | **LOST** |
| 392 | L5839–L5844 | QNEWSCOUTING @ L5828 | `(defrule     (true)` | cross | — | — | — | — | — | — | **LOST** |
| 393 | L5846–L5855 | QNEWSCOUTING @ L5828 | `(defrule     (true)` | goal1, goal2, goal3, goal4 | — | — | — | — | — | — | **LOST** |
| 394 | L5857–L5862 | QNEWSCOUTING @ L5828 | `(defrule     (up-point-distance scout-x home-x >= 32)` | goal2, goal3 | — | — | — | — | — | — | **LOST** |
| 395 | L5865–L5870 | QNEWSCOUTING @ L5828 | `(defrule     (game-time < 60)     (unit-type-count sheep < 4)` | goal1 | — | — | — | — | — | — | **LOST** |
| 396 | L5872–L5883 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 200)     (up-gaia-type-count c: deer-class < 1)     (or	(game-time > 410)     (and(goal gl-sighted-boar-count 2)     (or (and(game-time > 320)     (up...` | — | — | — | — | — | — | — | **LOST** |
| 397 | L5885–L5894 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 398 | L5896–L5903 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 200)     (goal gl-sighted-boar-count 2)     (up-compare-goal gl-current-sheep-count < 7)` | — | — | — | — | — | — | — | **LOST** |
| 399 | L5905–L5911 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 400 | L5914–L5923 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 401 | L5925–L5938 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-scouting-switch -1)` | — | — | — | — | — | — | — | **LOST** |
| 402 | L5940–L5946 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal SPLIT 1)     (up-point-contains explo-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 403 | L5948–L5954 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal SPLIT 1)     (up-point-distance scout-x explo-x >= 50)` | — | — | — | — | — | — | — | **LOST** |
| 404 | L5956–L5962 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal SPLIT 1)     (up-point-explored explo-x != explored-no)` | — | — | — | — | — | — | — | **LOST** |
| 405 | L5964–L5972 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 406 | L5974–L5987 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-scouting-switch 0)` | — | — | — | — | — | — | — | **LOST** |
| 407 | L5989–L5994 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-scouting-switch 0)     (up-timer-status t-direction-switch != timer-running)` | gl-scouting-switch | t-direction-switch | — | — | — | — | — | **LOST** |
| 408 | L5996–L6006 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 409 | L6009–L6019 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING -1)` | — | — | — | — | — | — | — | **LOST** |
| 410 | L6022–L6029 | QNEWSCOUTING @ L5828 | `(defrule     (true)     (false)` | — | — | — | — | — | — | — | **LOST** |
| 411 | L6031–L6037 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal gl-inside-forest 1)` | gl-inside-forest | — | — | — | — | — | — | **LOST** |
| 412 | L6039–L6046 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal gl-inside-forest -1)     (up-point-distance scout-x home-x >= MaxDistance)` | gl-inside-forest | — | — | — | — | — | — | **LOST** |
| 413 | L6048–L6054 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal gl-inside-forest 2)` | gl-inside-forest | — | — | — | — | — | — | **LOST** |
| 414 | L6056–L6061 | QNEWSCOUTING @ L5828 | `(defrule     (game-time < 100)     (up-point-contains explo-x c: tree-class)` | — | t-misc | — | — | — | — | — | **LOST** |
| 415 | L6063–L6068 | QNEWSCOUTING @ L5828 | `(defrule     (up-point-distance scout-x home-x >= 33)     (up-point-contains explo-x c: tree-class)` | — | t-misc | — | — | — | — | — | **LOST** |
| 416 | L6070–L6076 | QNEWSCOUTING @ L5828 | `(defrule     (up-point-contains explo-x c: tree-class)     (up-timer-status t-misc == timer-running)` | — | t-misc | — | — | — | — | — | **LOST** |
| 417 | L6079–L6092 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 418 | L6094–L6103 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 419 | L6105–L6117 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 420 | L6119–L6126 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 0)     (up-compare-goal goal >= 6)` | — | — | — | up-full-reset-search | up-target-point | — | — | **LOST** |
| 421 | L6128–L6134 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 0)     (up-compare-goal goal < 6)` | — | — | — | — | — | — | — | **LOST** |
| 422 | L6136–L6143 | QNEWSCOUTING @ L5828 | `(defrule     (or	(up-compare-goal explo-x >= 116)     (or	(up-compare-goal explo-y >= 116)     (or	(up-compare-goal explo-x < 4)     (up-compare-goal explo-y < 4))))` | — | — | — | — | — | 1 | — | **LOST** |
| 423 | L6145–L6158 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 424 | L6160–L6168 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | newscouting, split | — | — | — | — | — | — | **LOST** |
| 425 | L6171–L6176 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-fifth-turn 1)     (taunt-detected me 33)` | — | — | — | — | — | — | — | **LOST** |
| 426 | L6178–L6183 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 34)` | — | — | — | — | — | — | — | **LOST** |
| 427 | L6185–L6193 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (game-time > 10)     (up-compare-goal NEWSCOUTING < 50)     (up-point-distance scout-x home-x >= MaxDistance)` | — | — | — | — | — | — | — | **LOST** |
| 428 | L6195–L6204 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (game-time > 10)     (up-compare-goal NEWSCOUTING < 50)     (up-point-distance explo-x home-x >= MaxDistance)` | — | — | — | — | — | — | — | **LOST** |
| 429 | L6206–L6222 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 430 | L6224–L6230 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-second-turn 1)     (up-point-explored explo-x != explored-no)` | — | — | — | — | — | — | — | **LOST** |
| 431 | L6232–L6238 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-second-turn 1)     (up-point-contains explo-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 432 | L6240–L6245 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 433 | L6247–L6252 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 82)` | — | — | — | — | — | — | — | **LOST** |
| 434 | L6254–L6263 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 300)     (up-compare-goal NEWSCOUTING < FINISHED)     (up-compare-goal gl-current-sheep-count < 5)` | — | — | — | — | — | — | — | **LOST** |
| 435 | L6265–L6272 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 47)     (up-compare-goal gl-current-sheep-count >= 5)` | — | — | — | — | — | — | — | **LOST** |
| 436 | L6274–L6284 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 80)     (up-gaia-type-count c: forage-bush < 5)     (up-gaia-type-count c: forage-bush >= 1)     (up-compare-goal NEWSCOUTING < FINISHED)` | — | — | — | — | — | — | — | **LOST** |
| 437 | L6286–L6301 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 48)     (goal gl-fifth-turn 1)` | sn-focus-player-number | — | — | up-find-local, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | up-target-point | — | — | **LOST** |
| 438 | L6303–L6310 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 48)     (up-gaia-type-count c: forage-bush >= 5)` | — | — | — | — | — | — | — | **LOST** |
| 439 | L6312–L6321 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 290)     (up-compare-goal NEWSCOUTING < FINISHED)     (up-compare-goal gl-sighted-boar-count < 2)` | — | — | — | — | — | — | — | **LOST** |
| 440 | L6323–L6330 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 49)     (up-compare-goal gl-sighted-boar-count >= 2)` | — | — | — | — | — | — | — | **LOST** |
| 441 | L6332–L6339 | QNEWSCOUTING @ L5828 | `(defrule     (up-compare-goal NEWSCOUTING < FINISHED)     (up-compare-goal gl-current-sheep-count >= 7)` | — | — | — | — | — | — | — | **LOST** |
| 442 | L6341–L6347 | QNEWSCOUTING @ L5828 | `(defrule     (or	(game-time < 200)     (or	(military-population > 5)     (up-timer-status 28 == timer-running)))` | — | 28 | — | — | — | 1 | — | **LOST** |
| 443 | L6349–L6360 | QNEWSCOUTING @ L5828 | `(defrule     (up-compare-goal NEWSCOUTING < 50)     (up-gaia-type-count c: deer-class > 0)     (or	(game-time > 410)     (and(goal gl-sighted-boar-count 2)     (or (and(game-tim...` | — | — | — | — | — | — | — | **LOST** |
| 444 | L6362–L6371 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 445 | L6373–L6387 | QNEWSCOUTING @ L5828 | `(defrule     (true)     (up-timer-status 28 != timer-running)     (up-compare-goal NEWSCOUTING != FINISHED)     (or	(up-compare-goal NEWSCOUTING == 50)     (game-time s:> sn-hom...` | — | 28 | — | — | — | — | — | **LOST** |
| 446 | L6389–L6397 | QNEWSCOUTING @ L5828 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-compare-goal NEWSCOUTING != FINISHED)` | — | — | — | — | — | — | — | **LOST** |
| 447 | L6399–L6404 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 448 | L6407–L6411 | QCIRCLE SCOUTING @ L6406 | `(defrule     (players-building-type-count target-player town-center > 0)` | — | — | — | — | — | 15 | — | **LOST** |
| 449 | L6414–L6418 | QCIRCLE SCOUTING @ L6406 | `(defrule     (up-compare-goal gl-strategy != FLUSH)` | — | — | — | — | — | 4 | — | **LOST** |
| 450 | L6420–L6436 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-tenth-turn 1)     (players-building-type-count target-player farm < 1)     (players-building-type-count target-player house < 1)     (or	(players-building-...` | — | — | — | — | — | — | — | **LOST** |
| 451 | L6438–L6451 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-find-remote, up-set-target-object | up-target-point | — | — | **LOST** |
| 452 | L6453–L6473 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-tenth-turn 1)     (players-building-type-count target-player farm < 1)     (players-building-type-count target-player house > 0)` | — | — | — | — | — | — | — | **LOST** |
| 453 | L6475–L6494 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-tenth-turn 1)     (military-population < 20)     (players-building-type-count target-player farm > 0)` | — | — | — | — | — | — | — | **LOST** |
| 454 | L6497–L6513 | QCIRCLE SCOUTING @ L6406 | `(defrule     (true)     (false)` | goal, sn-focus-player-number, split | — | — | up-find-remote, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 455 | L6516–L6521 | QCIRCLE SCOUTING @ L6406 | `(defrule     (or	(not(player-in-game any-ally))     (up-compare-goal gl-circle-direcion != -1))` | — | — | — | — | — | 4 | — | **LOST** |
| 456 | L6523–L6536 | QCIRCLE SCOUTING @ L6406 | `(defrule     (game-time > 5)` | goal, sn-focus-player-number, split | — | — | up-find-remote, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 457 | L6538–L6551 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 458 | L6553–L6561 | QCIRCLE SCOUTING @ L6406 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 459 | L6563–L6571 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal1 g:> goal)` | — | — | — | — | — | — | — | **LOST** |
| 460 | L6574–L6579 | QCIRCLE SCOUTING @ L6406 | `(defrule     (or	(player-in-game any-ally)     (up-compare-goal gl-circle-direcion != -1))` | — | — | — | — | — | 3 | — | **LOST** |
| 461 | L6581–L6599 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-dlure FINISHED)     (unit-type-count scout-cavalry > 0)     (up-timer-status 28 != timer-running)` | — | 28 | — | — | — | — | — | **LOST** |
| 462 | L6601–L6608 | QCIRCLE SCOUTING @ L6406 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 463 | L6610–L6617 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal1 g:> goal)` | — | — | — | — | — | — | — | **LOST** |
| 464 | L6620–L6624 | QCIRCLE SCOUTING @ L6406 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 465 | L6626–L6630 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-circle-direcion COUNTERCLOCKWISE)` | goal1 | — | — | — | — | — | — | **LOST** |
| 466 | L6632–L6636 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-circle-direcion CLOCKWISE)` | goal1 | — | — | — | — | — | — | **LOST** |
| 467 | L6638–L6651 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-dlure FINISHED)     (goal gl-strategy KRUSH)     (unit-type-count scout-cavalry > 0)     (up-timer-status 28 != timer-running) ...` | — | 28 | — | — | — | — | — | **LOST** |
| 468 | L6653–L6670 | QCIRCLE SCOUTING @ L6406 | `(defrule     (player-valid 3)     (game-time < 900)` | — | — | — | — | — | — | — | **LOST** |
| 469 | L6672–L6690 | QCIRCLE SCOUTING @ L6406 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 470 | L6692–L6699 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)     (up-point-distance scout-x center-x >= max-circle-scout-distance)` | — | — | — | — | — | — | — | **LOST** |
| 471 | L6701–L6713 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 472 | L6716–L6723 | QFORAGE @ L6715 | `(defrule     (building-type-count mill >= 1)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 473 | L6725–L6736 | QFORAGE @ L6715 | `(defrule     (goal gl-tenth-turn 1)     (up-compare-goal BH < 1)     (building-type-count mill >= 1)     (unit-type-count villager-forager < 1)     (or	(and(unit-type-count shee...` | split | — | — | up-full-reset-search | — | — | — | **LOST** |
| 474 | L6738–L6751 | QFORAGE @ L6715 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 475 | L6753–L6765 | QFORAGE @ L6715 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-remove-objects | up-target-objects | — | — | **LOST** |
| 476 | L6768–L6773 | QCOUNTING SHEEP @ L6767 | `(defrule     (true)` | gl-current-sheep-count, gl-new-sheep-count, gl-sheep-count-last | — | — | — | — | — | — | **LOST** |
| 477 | L6775–L6777 | QCOUNTING SHEEP @ L6767 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 478 | L6779–L6789 | QCOUNTING SHEEP @ L6767 | `(defrule     (up-compare-goal gl-sheep-count g:> gl-sheep-count-last)     (dropsite-min-distance livestock-class < 8)     (building-type-count town-center > 0)` | gl-current-sheep-count, gl-new-sheep-count, gl-sheep-count-last | — | — | — | — | — | — | **LOST** |
| 479 | L6791–L6793 | QCOUNTING SHEEP @ L6767 | `(defrule     (up-compare-goal gl-sheep-count g:< gl-sheep-count-last)` | gl-sheep-count-last | — | — | — | — | — | — | **LOST** |
| 480 | L6796–L6811 | QDLURING @ L6795 | `(defrule     (true)     (or	(up-compare-goal gl-dlure == -1)     (up-compare-goal gl-deer-distance >= 20))     (or	(up-group-size c: RangedGroup >= 1)     (game-time s:> sn-home...` | sn-maximum-hunt-drop-distance, sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | — | **LOST** |
| 481 | L6813–L6822 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 482 | L6824–L6837 | QDLURING @ L6795 | `(defrule     (true)` | goal4, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 483 | L6839–L6857 | QDLURING @ L6795 | `(defrule     (goal gl-deer-walking 3)` | goal4, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 484 | L6859–L6867 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 485 | L6869–L6879 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 486 | L6881–L6889 | QDLURING @ L6795 | `(defrule     (up-compare-goal gl-dlure >= 0)     (up-compare-goal gl-deer-walking == -1)     (up-point-distance point2-x saved-x < 7)` | — | — | — | — | — | — | — | **LOST** |
| 487 | L6891–L6899 | QDLURING @ L6795 | `(defrule     (goal gl-deer-walking 0)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 488 | L6901–L6914 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 489 | L6916–L6930 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 490 | L6932–L6942 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 491 | L6944–L6952 | QDLURING @ L6795 | `(defrule     (up-compare-goal goal1 > 0)     (up-set-target-by-id g: deer-id)` | split | — | — | — | — | — | — | **LOST** |
| 492 | L6954–L6963 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)     (or	(goal gl-fifth-turn 1)     (goal gl-fifth-turn 2))     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 493 | L6965–L6976 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 494 | L6979–L6984 | QDLURING @ L6795 | `(defrule     (true)` | goal2, goal3 | — | — | — | — | — | — | **LOST** |
| 495 | L6986–L7003 | QDLURING @ L6795 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 496 | L7005–L7015 | QDLURING @ L6795 | `(defrule     (true)` | — | — | — | up-full-reset-search | — | — | — | **LOST** |
| 497 | L7017–L7031 | QDLURING @ L6795 | `(defrule     (goal gl-tenth-turn 1)     (unit-type-count villager-forager >= 3)     (dropsite-min-distance live-boar >= 10)     (up-timer-status t-misc != timer-running)     (or...` | — | t-misc | — | — | research-pending, up-research | — | — | **LOST** |
| 498 | L7033–L7043 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-find-remote, up-remove-objects | up-target-objects | — | — | **LOST** |
| 499 | L7045–L7061 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | gl-killed-deer-count, split | t-misc | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-remove-objects | up-target-objects | — | — | **LOST** |
| 500 | L7063–L7068 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 501 | L7070–L7082 | QDLURING @ L6795 | `(defrule     (dropsite-min-distance live-boar >= 10)     (up-timer-status t-misc != timer-running)     (or	(up-compare-goal goal2 >= 1)     (and(up-compare-goal goal3 >= 1)     ...` | split | t-misc | — | — | research-pending, unit-type-count-total, up-research | — | — | **LOST** |
| 502 | L7084–L7102 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 503 | L7104–L7108 | QDLURING @ L6795 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 504 | L7110–L7122 | QDLURING @ L6795 | `(defrule     (up-compare-goal goal1 < 2)     (up-compare-goal gl-dlure >= 0)     (up-compare-goal gl-dlure != FINISHED)` | — | — | — | — | — | — | — | **LOST** |
| 505 | L7130–L7140 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 506 | L7142–L7158 | QDLURING @ L6795 | `(defrule     (taunt-detected me 73)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 507 | L7160–L7166 | QDLURING @ L6795 | `(defrule     (taunt-detected me 73)     (goal gl-tenth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 508 | L7168–L7173 | QDLURING @ L6795 | `(defrule     (taunt-detected me 74)` | — | — | — | — | — | — | — | **LOST** |
| 509 | L7175–L7180 | QBH @ L7174 | `(defrule     (true)` | goal1, goal7 | — | — | — | — | — | — | **LOST** |
| 510 | L7182–L7188 | QBH @ L7174 | `(defrule     (true)` | gl-killed-boar-count, gl-sighted-boar-count | — | — | — | — | — | — | **LOST** |
| 511 | L7190–L7201 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 512 | L7204–L7213 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 513 | L7215–L7223 | QBH @ L7174 | `(defrule     (or	(goal gl-town-safe NO)     (or	(up-compare-goal BH >= 2)     (or	(up-compare-goal lt > 0)     (or	(unit-type-count-total villager < 10)     (up-compare-goal gl-...` | — | — | — | — | unit-type-count-total | 6 | — | **LOST** |
| 514 | L7225–L7230 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 515 | L7232–L7241 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 516 | L7243–L7253 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 517 | L7255–L7263 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 518 | L7265–L7271 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 519 | L7273–L7279 | QBH @ L7174 | `(defrule     (true)     (false)` | — | — | — | — | — | — | — | **LOST** |
| 520 | L7281–L7285 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 521 | L7288–L7300 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 522 | L7302–L7315 | QBH @ L7174 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-hitpoints > 25)     (up-get-object-data object-data-target-id ...` | — | — | — | — | up-get-object-data | — | — | **LOST** |
| 523 | L7317–L7321 | QBH @ L7174 | `(defrule     (true)` | goal1 | — | — | — | — | — | — | **LOST** |
| 524 | L7323–L7327 | QBH @ L7174 | `(defrule     (research-completed ri-loom)` | goal1 | — | — | — | research, research-completed | — | — | **LOST** |
| 525 | L7329–L7341 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 526 | L7343–L7352 | QBH @ L7174 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-by-id g: current-boar-id)     (up-get-object-data object-data-target-id goal)     (up-set-target-by-id g: goal)` | — | — | — | — | up-get-object-data | — | — | **LOST** |
| 527 | L7354–L7362 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 528 | L7364–L7376 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | — | — | — | **LOST** |
| 529 | L7378–L7388 | QBH @ L7174 | `(defrule     (goal SPLIT 1)     (up-compare-goal lt > 0)     (or	(up-object-data object-data-hitpoints g:< goal1)     (and(up-point-distance point2-x point-x < 1)     (up-point-...` | — | — | — | — | up-target-objects | — | — | **LOST** |
| 530 | L7390–L7394 | QBH @ L7174 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 531 | L7397–L7410 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 532 | L7412–L7419 | QBH @ L7174 | `(defrule     (up-compare-goal rt == 1)     (goal gl-sighted-boar-count 0)` | — | — | — | — | — | — | — | **LOST** |
| 533 | L7421–L7430 | QBH @ L7174 | `(defrule     (goal gl-sighted-boar-count 1)     (or	(up-compare-goal rl == 2)     (and(up-compare-goal rl == 1)     (up-compare-goal gl-killed-boar-count > 0)))` | — | — | — | — | — | — | — | **LOST** |
| 534 | L7432–L7438 | QBH @ L7174 | `(defrule     (goal gl-town-safe NO)     (up-compare-goal BH > -1)` | — | — | — | — | — | — | — | **LOST** |
| 535 | L7440–L7450 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 536 | L7452–L7466 | QBH @ L7174 | `(defrule     (goal BH 0)` | bh, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data | — | — | **LOST** |
| 537 | L7468–L7474 | QBH @ L7174 | `(defrule     (goal old-boar-id -1)     (up-compare-goal current-boar-id != -1)` | old-boar-id | — | — | — | — | — | — | **LOST** |
| 538 | L7476–L7484 | QBH @ L7174 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal BH == 3)     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | up-get-object-data | — | — | **LOST** |
| 539 | L7486–L7495 | QBH @ L7174 | `(defrule     (up-set-target-by-id g: current-boar-id)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 540 | L7497–L7505 | QBH @ L7174 | `(defrule     (goal lt 0)     (or	(goal BH 2)     (goal BH 3))     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | — | — | — | **LOST** |
| 541 | L7507–L7514 | QBH @ L7174 | `(defrule     (goal goal1 -1)     (up-compare-goal BH == 3)     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | — | — | — | **LOST** |
| 542 | L7516–L7530 | QBH @ L7174 | `(defrule     (unit-type-count villager >= 9)     (up-compare-goal current-boar-id != -1)     (or	(goal BH 10)     (and(goal BH 1)     (dropsite-min-distance live-boar < 33)))   ...` | split | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | up-research | — | — | **LOST** |
| 543 | L7532–L7538 | QBH @ L7174 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal7 >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 544 | L7540–L7555 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-object | up-get-object-data, up-target-objects | — | — | **LOST** |
| 545 | L7557–L7572 | QBH @ L7174 | `(defrule     (research-completed ri-loom)     (or	(unit-type-count sheep < 1)     (unit-type-count villager >= 9))     (up-compare-goal current-boar-id != -1)     (or	(goal BH 1...` | split | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 546 | L7574–L7580 | QBH @ L7174 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal7 >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 547 | L7582–L7597 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-object | up-get-object-data, up-target-objects | — | — | **LOST** |
| 548 | L7599–L7608 | QBH @ L7174 | `(defrule     (goal BH 2)     (goal gl-killed-boar-count 0)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-action == actionid-attack)` | — | — | — | — | — | — | — | **LOST** |
| 549 | L7610–L7619 | QBH @ L7174 | `(defrule     (goal BH 2)     (goal gl-killed-boar-count 1)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-action == actionid-attack)` | — | — | — | — | — | — | — | **LOST** |
| 550 | L7621–L7636 | QBH @ L7174 | `(defrule     (goal gl-fifth-turn 1)     (dropsite-min-distance live-boar < 4)` | — | — | — | — | — | — | — | **LOST** |
| 551 | L7638–L7656 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | gl-killed-boar-count, sn-focus-player-number | — | — | up-find-remote, up-remove-objects | up-target-objects | — | — | **LOST** |
| 552 | L7658–L7663 | QBH @ L7174 | `(defrule     (goal BH 4)     (dropsite-min-distance live-boar > 10)` | bh | — | — | — | — | — | — | **LOST** |
| 553 | L7668–L7674 | QBH @ L7174 | `(defrule     (false)     (up-set-target-by-id g: lurer-id)     (dropsite-min-distance live-boar < 10)` | — | — | — | — | — | — | — | **LOST** |
| 554 | L7676–L7682 | QBH @ L7174 | `(defrule     (false)     (up-set-target-by-id g: current-boar-id)     (dropsite-min-distance live-boar < 10)` | — | — | — | — | — | — | — | **LOST** |
| 555 | L7685–L7692 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-carry < 10)     (up-compare-goal gl-killed-boar-count >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 556 | L7694–L7702 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: current-boar-id)` | — | — | — | up-find-local, up-full-reset-search | — | — | — | **LOST** |
| 557 | L7704–L7715 | QRETARGETING @ L7684 | `(defrule     (false)     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-carry >= 50)     (up-ob...` | split | — | — | — | — | — | — | **LOST** |
| 558 | L7717–L7725 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 1)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-hitpoints < 2)     (up-compare-goal...` | split | — | — | — | — | — | — | **LOST** |
| 559 | L7727–L7736 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (dropsite-min-distance live-boar < 10)     (up-set-target-by-id g: current-boar-id)     (up-compare-goal gl-...` | split | — | — | — | — | — | — | **LOST** |
| 560 | L7738–L7742 | QRETARGETING @ L7684 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 561 | L7744–L7748 | QRETARGETING @ L7684 | `(defrule     (research-completed ri-loom)` | goal | — | — | — | research, research-completed | — | — | **LOST** |
| 562 | L7750–L7759 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 563 | L7761–L7767 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)     (up-set-target-by-id g: current-boar-id)     (up-get-object-data object-data-target-id goal1)` | — | — | — | up-remove-objects | up-get-object-data | — | — | **LOST** |
| 564 | L7769–L7781 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-objects | — | — | **LOST** |
| 565 | L7783–L7790 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: old-boar-id)     (up-object-data object-data-carry < 10)     (up-compare-goal gl-killed-boar-count >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 566 | L7792–L7800 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: old-boar-id)     (up-compare-goal gl-killed-boar-count >= 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 567 | L7802–L7813 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (up-set-target-by-id g: old-boar-id)     (up-object-data object-data-carry >= 50)     (up-object-data object...` | — | t-kill-boar | — | — | — | — | — | **LOST** |
| 568 | L7815–L7824 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 1)     (up-set-target-by-id g: old-boar-id)     (up-object-data object-data-hitpoints < 2)     (up-compare-goal gl-...` | split | t-kill-boar | — | — | — | — | — | **LOST** |
| 569 | L7826–L7836 | QRETARGETING @ L7684 | `(defrule     (false)     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (dropsite-min-distance live-boar < 10)     (up-set-target-by-id g: current-boar-id)     (up-comp...` | split | — | — | — | — | — | — | **LOST** |
| 570 | L7838–L7842 | QRETARGETING @ L7684 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 571 | L7844–L7848 | QRETARGETING @ L7684 | `(defrule     (research-completed ri-loom)` | goal | — | — | — | research, research-completed | — | — | **LOST** |
| 572 | L7850–L7859 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 573 | L7861–L7867 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)     (up-set-target-by-id g: old-boar-id)     (up-get-object-data object-data-target-id goal1)` | — | — | — | up-remove-objects | up-get-object-data | — | — | **LOST** |
| 574 | L7869–L7880 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-objects | — | — | **LOST** |
| 575 | L7883–L7888 | QRETARGETING @ L7684 | `(defrule     (false)     (goal BH 10)` | — | — | — | — | — | — | — | **LOST** |
| 576 | L7890–L7907 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-second-turn 1)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | — | — | — | **LOST** |
| 577 | L7909–L7922 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 578 | L7924–L7931 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-fifth-turn 1)     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | — | — | — | **LOST** |
| 579 | L7933–L7940 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-fifth-turn 1)     (up-set-target-by-id g: old-boar-id)` | — | — | — | — | — | — | — | **LOST** |
| 580 | L7942–L7947 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 76)` | — | — | — | — | — | — | — | **LOST** |
| 581 | L7950–L7958 | QFORCEDROP @ L7949 | `(defrule     (wood-amount >= 70)     (goal gl-twenty-turn 1)     (building-type-count-total lumber-camp < 2)     (up-compare-goal gl-current-build-item == LC2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 582 | L7960–L7966 | QFORCEDROP @ L7949 | `(defrule     (current-age == feudal-age)` | — | — | — | — | — | — | — | **LOST** |
| 583 | L7968–L7977 | QFORCEDROP @ L7949 | `(defrule     (wood-amount > 130)     (wood-amount < 175)     (goal gl-tenth-turn 1)     (current-age == feudal-age)     (goal gl-current-build-item RANGES)` | — | — | — | — | — | — | — | **LOST** |
| 584 | L7979–L7984 | QFORCEDROP @ L7949 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 585 | L7986–L7994 | QFORCEDROP @ L7949 | `(defrule     (or	(and(food-amount >= 50)     (unit-type-count villager < FlushDarkAgeVills))     (or	(and(food-amount >= 500)     (current-age == dark-age))     (up-research-sta...` | force-res-drop-goal | — | — | — | research-pending, up-research | — | — | **LOST** |
| 586 | L7996–L8005 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal force-res-drop-goal -1)     (unit-type-count villager < 13)     (timer-triggered villager-timer)     (up-pending-objects c: villager == 1)` | — | villager-timer | — | — | up-pending-objects | — | — | **LOST** |
| 587 | L8007–L8023 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal force-res-drop-goal 0)     (timer-triggered villager-timer)     (up-pending-objects c: villager < 2)     (or	(unit-type-count villager ...` | goal | villager-timer | — | — | up-get-fact, up-pending-objects | — | — | **LOST** |
| 588 | L8025–L8035 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal force-res-drop-goal 0)     (current-age == dark-age)     (unit-type-count villager < 16)` | — | — | — | — | — | — | — | **LOST** |
| 589 | L8037–L8047 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 500)     (food-amount >= 410)     (goal gl-fifth-turn 1)     (current-age == dark-age)     (goal gl-strategy FLUSH)     (research-available feudal-age)` | — | — | — | — | research | — | — | **LOST** |
| 590 | L8049–L8060 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 500)     (food-amount < 410)     (food-amount >= 360)     (goal gl-tenth-turn 1)     (current-age == dark-age)     (goal gl-strategy FLUSH)     (rese...` | — | — | — | — | research | — | — | **LOST** |
| 591 | L8062–L8074 | QFORCEDROP @ L7949 | `(defrule     (food-amount >= 600)     (gold-amount >= 140)     (goal gl-twenty-turn 1)     (or	(gold-amount < 200)     (food-amount < 800))     (current-age == feudal-age)     (...` | — | — | — | — | — | — | — | **LOST** |
| 592 | L8076–L8085 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal gl-twenty-turn 1)     (current-age < feudal-age)     (timer-triggered t-vill-training)     (up-pending-objects c: villager < 2)` | — | t-vill-training | — | — | up-pending-objects | — | — | **LOST** |
| 593 | L8089–L8094 | QCLAIMING SHEEP @ L8087 | `(defrule     (or	(game-time < 2)     (game-time > 30))` | — | — | — | — | — | 4 | — | **LOST** |
| 594 | L8096–L8106 | QCLAIMING SHEEP @ L8087 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 595 | L8108–L8115 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-compare-goal rt > 0)` | split | — | — | up-clean-search, up-set-target-object | — | — | — | **LOST** |
| 596 | L8117–L8127 | QCLAIMING SHEEP @ L8087 | `(defrule     (goal SPLIT 1)` | split | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 597 | L8129–L8137 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-compare-goal lt > 0)` | — | — | — | up-clean-search, up-remove-objects | up-target-point | — | — | **LOST** |
| 598 | L8140–L8146 | QCLAIMING SHEEP @ L8087 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 599 | L8148–L8152 | QCLAIMING SHEEP @ L8087 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 600 | L8154–L8160 | QCLAIMING SHEEP @ L8087 | `(defrule     (current-age == dark-age)     (or	(current-age-time > 180)     (unit-type-count sheep < 1))` | goal | — | — | — | — | — | — | **LOST** |
| 601 | L8162–L8166 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal | — | — | — | — | — | — | **LOST** |
| 602 | L8168–L8178 | QCLAIMING SHEEP @ L8087 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 603 | L8180–L8193 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-compare-goal rt > 0)` | sn-focus-player-number, split | — | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 604 | L8195–L8206 | QCLAIMING SHEEP @ L8087 | `(defrule     (goal SPLIT 1)` | gl-getting-sheep | 28 | — | — | up-target-point | — | — | **LOST** |
| 605 | L8208–L8213 | QCLAIMING SHEEP @ L8087 | `(defrule     (false)     (timer-triggered 28)` | — | 28 | — | — | — | — | — | **LOST** |
| 606 | L8215–L8220 | QCLAIMING SHEEP @ L8087 | `(defrule     (false)     (up-timer-status 28 == timer-running)` | — | 28 | — | — | — | — | — | **LOST** |
| 607 | L8224–L8238 | QFARMS @ L8222 | `(defrule     (idle-farm-count > 0)` | — | — | — | — | — | — | — | **LOST** |
| 608 | L8240–L8258 | QFARMS @ L8222 | `(defrule     (goal SPLIT 1)` | — | — | — | up-set-target-point | — | — | — | **LOST** |
| 609 | L8260–L8265 | QFARMS @ L8222 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 610 | L8269–L8276 | QARCHERS @ L8267 | `(defrule     (false)     (or	(game-time < 10)     (or	(unit-type-count archer < 1)     (up-group-size c: RangedGroup < 1)))` | — | — | — | — | — | 2 | — | **LOST** |
| 611 | L8280–L8286 | QARCHERS @ L8267 | `(defrule     (true)` | gl-enemy-skirms-nearby, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 612 | L8289–L8298 | QARCHERS @ L8267 | `(defrule     (stance-toward focus-player enemy)` | gl-enemy-skirms-nearby | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 613 | L8301–L8306 | QARCHERS @ L8267 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 614 | L8308–L8317 | QARCHERS @ L8267 | `(defrule     (up-compare-goal rt >= 1)` | gl-enemy-skirms-nearby | — | — | up-clean-search, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 615 | L8320–L8336 | QARCHERS @ L8267 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 616 | L8341–L8346 | QSKIRMS @ L8338 | `(defrule     (players-unit-type-count target-player archer-line >= 4)` | gl-enemy-archers | — | — | — | — | — | — | **LOST** |
| 617 | L8349–L8354 | QSKIRMS @ L8338 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 618 | L8357–L8365 | QSKIRMS @ L8338 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 619 | L8368–L8374 | QSKIRMS @ L8338 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 620 | L8376–L8392 | QSKIRMS @ L8338 | `(defrule     (true)     (goal gl-tenth-turn 1)     (goal gl-enemy-archers YES)     (or	(goal gl-town-safe YES)     (up-compare-goal rt < 1))     (up-group-size c: RangedGroup > ...` | split | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 621 | L8394–L8403 | QSKIRMS @ L8338 | `(defrule     (goal SPLIT 1)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state, up-target-point | — | — | **LOST** |
| 622 | L8406–L8410 | QDEFENSE @ L8405 | `(defrule     (current-age < feudal-age)` | — | — | — | — | — | 3 | — | **LOST** |
| 623 | L8413–L8418 | QDEFENSE @ L8405 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 624 | L8421–L8429 | QDEFENSE @ L8405 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 625 | L8432–L8438 | QDEFENSE @ L8405 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 626 | L8440–L8455 | QDEFENSE @ L8405 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 627 | L8457–L8464 | QDEFENSE @ L8405 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-cavalry-in-town < 3)     (up-compare-goal gl-archery-in-town >= 4)` | — | — | — | up-remove-objects | — | — | — | **LOST** |
| 628 | L8466–L8483 | QDEFENSE @ L8405 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 629 | L8486–L8499 | QMANGOS @ L8485 | `(defrule     (goal gl-ninety-turn 1)     (unit-type-count mangonel > 0)     (up-compare-goal SUPERIORITY < 20)     (up-group-size c: RangedGroup > 0)` | — | — | — | — | — | — | — | **LOST** |
| 630 | L8504–L8515 | QSPEARS @ L8501 | `(defrule     (unit-type-count spearman-line >= 1)` | goal, lt, point-x, point-y | — | — | up-find-local, up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 631 | L8517–L8527 | QSPEARS @ L8501 | `(defrule     (unit-type-count spearman-line >= 1)     (up-set-target-object search-local c: 0)` | goal, point-x, point-y | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 632 | L8529–L8536 | QSPEARS @ L8501 | `(defrule     (up-compare-goal lt > 0)     (unit-type-count spearman-line >= 1)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | — | **LOST** |
| 633 | L8538–L8545 | QSPEARS @ L8501 | `(defrule     (up-compare-goal goal > 0)     (unit-type-count spearman-line >= 1)` | point-x, point-y | — | — | — | — | — | — | **LOST** |
| 634 | L8547–L8554 | QSPEARS @ L8501 | `(defrule     (goal gl-thirty-turn 1)     (up-group-size c: RangedGroup < 1)` | — | — | — | up-find-local, up-full-reset-search | up-target-point | — | — | **LOST** |
| 635 | L8556–L8560 | QSPEARS @ L8501 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 636 | L8562–L8569 | QSPEARS @ L8501 | `(defrule     (game-time >= 1020)` | — | — | — | — | — | — | — | **LOST** |
| 637 | L8571–L8576 | QSPEARS @ L8501 | `(defrule     (up-group-size c: RangedGroup < 1)     (unit-type-count skirmisher-line < 1)` | goal8 | — | — | — | — | — | — | **LOST** |
| 638 | L8580–L8588 | QSPEARS @ L8501 | `(defrule     (true)` | goal, goal1, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 639 | L8591–L8607 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal, goal1 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 640 | L8610–L8615 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 641 | L8617–L8633 | QSPEARS @ L8501 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 642 | L8636–L8641 | QSPEARS @ L8501 | `(defrule     (or (up-group-size c: RangedGroup < 1)     (unit-type-count spearman-line < 1))` | — | — | — | — | — | 34 | — | **LOST** |
| 643 | L8643–L8653 | QSPEARS @ L8501 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | — | **LOST** |
| 644 | L8655–L8660 | QSPEARS @ L8501 | `(defrule     (up-point-distance enemy-group-x ranged-group-x < 15)` | — | — | — | — | — | — | — | **LOST** |
| 645 | L8663–L8676 | QSPEARS @ L8501 | `(defrule     (true)` | goal1, sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 646 | L8680–L8689 | QSPEARS @ L8501 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 647 | L8693–L8708 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 648 | L8710–L8718 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal3 | — | — | up-find-remote, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 649 | L8721–L8726 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | — | **LOST** |
| 650 | L8731–L8737 | QSPEARS @ L8501 | `(defrule     (true)` | goal6, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 651 | L8740–L8750 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal6 | — | — | up-find-status-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 652 | L8753–L8758 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 653 | L8763–L8769 | QSPEARS @ L8501 | `(defrule     (true)` | goal4, rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 654 | L8772–L8784 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal4 | — | — | up-find-status-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 655 | L8787–L8792 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 656 | L8796–L8811 | QSPEARS @ L8501 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 657 | L8814–L8819 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | — | **LOST** |
| 658 | L8822–L8828 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 659 | L8830–L8839 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 660 | L8841–L8856 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 661 | L8858–L8862 | QSPEARS @ L8501 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 662 | L8866–L8880 | QSPEARS @ L8501 | `(defrule     (up-compare-goal goal6 < 1)` | — | — | — | — | — | — | — | **LOST** |
| 663 | L8883–L8888 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote | — | — | — | **LOST** |
| 664 | L8891–L8897 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 665 | L8899–L8909 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-set-target-point | — | — | — | **LOST** |
| 666 | L8911–L8923 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-remove-objects, up-set-target-point | up-target-objects, up-target-point | — | — | **LOST** |
| 667 | L8927–L8939 | QSPEARS @ L8501 | `(defrule     (goal gl-second-turn 1)     (or	(up-compare-goal goal1 >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 668 | L8942–L8950 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-set-target-point | — | — | — | **LOST** |
| 669 | L8953–L8959 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 670 | L8961–L8971 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data | — | — | **LOST** |
| 671 | L8973–L8985 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-remove-objects, up-set-target-point | up-target-objects, up-target-point | — | — | **LOST** |
| 672 | L8988–L8999 | QSPEARS @ L8501 | `(defrule     (goal gl-second-turn 1)     (up-compare-goal goal1 < 1)` | — | — | — | — | — | — | — | **LOST** |
| 673 | L9001–L9009 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 674 | L9011–L9018 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)     (up-point-distance ranged-group-x home-x >= 25)` | — | — | — | up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 675 | L9020–L9028 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 676 | L9030–L9035 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (up-point-distance spear-group-x nearest-tower-x < 9)` | — | — | — | — | — | — | — | **LOST** |
| 677 | L9037–L9045 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | split | — | — | — | up-target-point | — | — | **LOST** |
| 678 | L9048–L9059 | QSPEARS @ L8501 | `(defrule     (taunt-detected me 53)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 679 | L9061–L9066 | QSPEARS @ L8501 | `(defrule     (taunt-detected me 54)` | — | — | — | — | — | — | — | **LOST** |
| 680 | L9070–L9076 | QSCOUT @ L9068 | `(defrule     (game-time > 300)     (goal gl-ninety-turn 1)     (unit-type-count scout-cavalry-line > 0)` | — | — | — | — | — | — | — | **LOST** |
| 681 | L9079–L9084 | QSCOUT @ L9068 | `(defrule     (up-set-target-by-id g: scout-id)     (unit-type-count scout-cavalry-line >= 1)` | — | — | — | — | up-get-object-data | — | — | **LOST** |
| 682 | L9086–L9101 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 683 | L9103–L9115 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 684 | L9117–L9127 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | — | **LOST** |
| 685 | L9129–L9133 | QSCOUT @ L9068 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 686 | L9135–L9142 | QSCOUT @ L9068 | `(defrule     (game-time < 860)` | — | — | — | — | — | — | — | **LOST** |
| 687 | L9144–L9151 | QSCOUT @ L9068 | `(defrule     (or	(goal SOD 0)     (or	(goal gl-strategy KRUSH)     (or	(goal gl-position POCKET)     (unit-type-count scout-cavalry < 1))))` | — | — | — | — | — | 36 | — | **LOST** |
| 688 | L9153–L9163 | QSCOUT @ L9068 | `(defrule     (or	(goal gl-scout-added FINISHED)     (players-building-type-count target-player town-center < 1))     (or	(up-timer-status 28 == timer-running)     (or	(goal gl-s...` | — | 28 | — | — | — | 35 | — | **LOST** |
| 689 | L9165–L9174 | QSCOUT @ L9068 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5 | — | — | — | — | — | — | **LOST** |
| 690 | L9176–L9187 | QSCOUT @ L9068 | `(defrule     (goal gl-fifth-turn 1)     (strategic-number sn-total-number-explorers > 0)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | — | **LOST** |
| 691 | L9189–L9207 | QSCOUT @ L9068 | `(defrule     (goal gl-fifth-turn 1)     (current-age-time < 400)     (goal gl-strategy FLUSH)     (current-age < castle-age)     (goal NEWSCOUTING FINISHED)     (up-group-size c...` | — | — | — | — | — | — | — | **LOST** |
| 692 | L9209–L9213 | QSCOUT @ L9068 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 31 | — | **LOST** |
| 693 | L9216–L9221 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 694 | L9224–L9234 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | goal3 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 695 | L9237–L9243 | QSCOUT @ L9068 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 696 | L9246–L9253 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 697 | L9256–L9264 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | goal5 | — | — | up-find-remote, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 698 | L9267–L9272 | QSCOUT @ L9068 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 699 | L9275–L9281 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 700 | L9284–L9294 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 701 | L9296–L9302 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 702 | L9304–L9315 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)` | goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 703 | L9318–L9324 | QSCOUT @ L9068 | `(defrule     (player-valid focus-player)` | sn-focus-player-number, split | — | — | — | — | -4 | — | **LOST** |
| 704 | L9326–L9330 | QSCOUT @ L9068 | `(defrule     (up-set-target-by-id g: scout-id)` | — | — | — | — | up-get-object-data | — | — | **LOST** |
| 705 | L9333–L9340 | QSCOUT @ L9068 | `(defrule     (true)` | — | — | — | up-full-reset-search | — | — | — | **LOST** |
| 706 | L9343–L9357 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 707 | L9360–L9366 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote | — | — | — | **LOST** |
| 708 | L9369–L9375 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 709 | L9377–L9386 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-set-target-object | — | — | — | **LOST** |
| 710 | L9388–L9392 | QSCOUT @ L9068 | `(defrule     (up-point-distance nearest-tower-x scout-x < 7)` | — | — | — | — | — | — | — | **LOST** |
| 711 | L9394–L9398 | QSCOUT @ L9068 | `(defrule     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | — | **LOST** |
| 712 | L9400–L9410 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 713 | L9412–L9418 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 714 | L9421–L9429 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 715 | L9432–L9439 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-remove-objects | — | — | — | **LOST** |
| 716 | L9442–L9447 | QSCOUT @ L9068 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 717 | L9449–L9459 | QSCOUT @ L9068 | `(defrule     (true)` | goal4, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 718 | L9461–L9474 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 719 | L9477–L9483 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 720 | L9485–L9494 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 721 | L9496–L9503 | QSCOUT @ L9068 | `(defrule     (or	(up-compare-goal goal2 >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 722 | L9505–L9512 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 723 | L9515–L9530 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 724 | L9532–L9541 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 9)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 725 | L9543–L9548 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 10)` | — | — | — | — | — | — | — | **LOST** |
| 726 | L9551–L9563 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 69)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | — | — | — | **LOST** |
| 727 | L9565–L9573 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 70)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | — | **LOST** |
| 728 | L9575–L9583 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 71)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | — | **LOST** |
| 729 | L9586–L9597 | QSCOUT @ L9068 | `(defrule     (or	(timer-triggered 28)     (taunt-detected me 11))     (up-compare-goal gl-scout-added != FINISHED)` | — | 28 | — | — | — | — | — | **LOST** |
| 730 | L9599–L9608 | QSCOUT @ L9068 | `(defrule     (or	(timer-triggered 28)     (taunt-detected me 11))     (up-compare-goal gl-scout-added == FINISHED)` | gl-getting-sheep | 28 | — | — | — | — | — | **LOST** |
| 731 | L9611–L9619 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 732 | L9621–L9627 | QSOD @ L9610 | `(defrule     (or	(not(up-set-target-by-id g: scout-id))     (and(goal SOD -1)     (unit-type-count scout-cavalry-line < 1)))` | — | — | — | — | — | 14 | — | **LOST** |
| 733 | L9629–L9639 | QSOD @ L9610 | `(defrule     (true)` | goal, goal2 | — | — | — | — | — | — | **LOST** |
| 734 | L9642–L9647 | QSOD @ L9610 | `(defrule     (up-set-target-by-id g: scout-id)` | goal1 | — | — | — | up-get-object-data | — | — | **LOST** |
| 735 | L9649–L9654 | QSOD @ L9610 | `(defrule     (military-population < 6)     (current-age >= feudal-age)` | goal1 | — | — | — | — | — | — | **LOST** |
| 736 | L9656–L9660 | QSOD @ L9610 | `(defrule     (players-building-type-count every-enemy town-center < 1)` | goal1 | — | — | — | — | — | — | **LOST** |
| 737 | L9662–L9667 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 738 | L9669–L9674 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 739 | L9681–L9690 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 740 | L9692–L9701 | QSOD @ L9610 | `(defrule     (goal SOD -1)     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | — | **LOST** |
| 741 | L9703–L9709 | QSOD @ L9610 | `(defrule     (goal SOD -1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | — | **LOST** |
| 742 | L9712–L9718 | QSOD @ L9610 | `(defrule     (true)` | goal, goal1, goal2 | — | — | — | — | — | — | **LOST** |
| 743 | L9720–L9726 | QSOD @ L9610 | `(defrule     (goal gl-strategy KRUSH)` | goal, goal1, goal2 | — | — | — | — | — | — | **LOST** |
| 744 | L9728–L9733 | QSOD @ L9610 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-circle-direcion CLOCKWISE)` | goal2 | — | — | — | — | — | — | **LOST** |
| 745 | L9735–L9753 | QSOD @ L9610 | `(defrule     (goal SPLIT 1)` | — | — | — | up-full-reset-search | — | — | — | **LOST** |
| 746 | L9755–L9763 | QSOD @ L9610 | `(defrule     (goal SOD 0)     (or	(up-timer-status 28 != timer-running)     (unit-type-count scout-cavalry-line < 1))` | — | 28 | — | up-full-reset-search | — | — | — | **LOST** |
| 747 | L9767–L9776 | QKNIGHT GROUP @ L9765 | `(defrule     (goal gl-attacking -1)     (goal gl-tenth-turn 1)     (goal gl-town-safe YES)     (goal gl-strategy KRUSH)     (unit-type-count knight-line > 0)` | — | — | — | — | — | — | — | **LOST** |
| 748 | L9779–L9792 | QKNIGHT GROUP @ L9765 | `(defrule     (true)` | goal, lt, point-x, point-y, sn-focus-player-number | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 749 | L9794–L9803 | QKNIGHT GROUP @ L9765 | `(defrule     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 750 | L9805–L9811 | QKNIGHT GROUP @ L9765 | `(defrule     (up-compare-goal lt > 0)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | — | **LOST** |
| 751 | L9813–L9819 | QKNIGHT GROUP @ L9765 | `(defrule     (up-compare-goal goal > 0)` | point-x, point-y | — | — | — | — | — | — | **LOST** |
| 752 | L9822–L9834 | QEVAL @ L9821 | `(defrule     (true)` | goal1 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 753 | L9836–L9845 | QEVAL @ L9821 | `(defrule     (true)` | goal | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 754 | L9847–L9858 | QEVAL @ L9821 | `(defrule     (true)` | goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 755 | L9860–L9864 | QEVAL @ L9821 | `(defrule     (up-group-size c: KnightGroup < 1)` | — | — | — | — | — | 10 | — | **LOST** |
| 756 | L9867–L9873 | QEVAL @ L9821 | `(defrule     (true)` | gl-knight-eval | — | — | — | — | — | — | **LOST** |
| 757 | L9875–L9879 | QEVAL @ L9821 | `(defrule     (research-completed ri-scale-barding)` | gl-knight-eval | — | — | — | research, research-completed | — | — | **LOST** |
| 758 | L9882–L9886 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 759 | L9888–L9892 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 760 | L9894–L9898 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 761 | L9901–L9911 | QEVAL @ L9821 | `(defrule     (true)` | goal3 | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 762 | L9913–L9918 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 763 | L9921–L9926 | QEVAL @ L9821 | `(defrule     (research-completed ri-chain-barding)` | gl-knight-eval | — | — | — | research, research-completed | — | — | **LOST** |
| 764 | L9928–L9932 | QEVAL @ L9821 | `(defrule     (research-completed ri-forging)` | gl-knight-eval | — | — | — | research, research-completed | — | — | **LOST** |
| 765 | L9934–L9938 | QEVAL @ L9821 | `(defrule     (research-completed ri-iron-casting)` | gl-knight-eval | — | — | — | research, research-completed | — | — | **LOST** |
| 766 | L9941–L9945 | QEVAL @ L9821 | `(defrule     (up-group-size c: KnightGroup < 1)` | — | — | — | — | — | 30 | — | **LOST** |
| 767 | L9947–L9954 | QEVAL @ L9821 | `(defrule     (true)` | goal, goal1, goal2, goal3 | — | — | — | — | — | — | **LOST** |
| 768 | L9956–L9968 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 769 | L9970–L9979 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 770 | L9981–L9994 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 771 | L9996–L10006 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 772 | L10010–L10017 | QEVAL @ L9821 | `(defrule     (up-compare-goal goal3 >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 773 | L10019–L10035 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 774 | L10038–L10046 | QEVAL @ L9821 | `(defrule     (up-compare-goal goal3 < 1)` | — | — | — | — | — | — | — | **LOST** |
| 775 | L10048–L10057 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 776 | L10060–L10071 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 777 | L10073–L10088 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 778 | L10090–L10103 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 779 | L10106–L10111 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 780 | L10114–L10122 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (nand	(up-compare-goal SUPERIORITY >= 20)     (research-completed ri-chain-barding))     (up-point-distance knight-group-x nearest-c...` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 781 | L10124–L10131 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 4)     (up-point-distance knight-group-x point-x < 3)     (up-point-distance knight-group-x nearest-castle-x >= 18)` | — | — | — | — | — | — | — | **LOST** |
| 782 | L10134–L10140 | QEVAL @ L9821 | `(defrule     (up-compare-goal goal2 < 4)     (up-group-size c: KnightGroup >= 2)     (up-compare-goal gl-knight-group-state == SATTACKING)` | — | — | — | — | — | 1 | — | **LOST** |
| 783 | L10142–L10153 | QEVAL @ L9821 | `(defrule     (false)     (goal gl-knight-retreat -1)     (up-compare-goal goal2 >= 1)     (up-group-size c: KnightGroup < 5)     (or	(up-compare-goal goal2 >= 3)` | — | — | — | — | — | — | — | **LOST** |
| 784 | L10155–L10161 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 3)     (up-compare-goal goal2 < 1)` | gl-knight-retreat | — | — | — | — | — | — | **LOST** |
| 785 | L10164–L10174 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (up-group-size c: KnightGroup < 8)     (not(research-completed ri-chain-barding))     (or	(up-compare-goal goal >= 4)     (and(up-co...` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 786 | L10176–L10186 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (up-group-size c: KnightGroup < 7)     (research-completed ri-chain-barding)     (or	(up-compare-goal goal >= 6)     (and(up-compare...` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 787 | L10188–L10194 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 2)     (up-compare-goal goal < 1)` | — | — | — | — | — | — | — | **LOST** |
| 788 | L10197–L10207 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (up-group-size c: KnightGroup < 7)     (nand	(up-compare-goal SUPERIORITY >= 8)     (research-completed ri-chain-barding))     (up-p...` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 789 | L10209–L10216 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 1)     (up-point-distance knight-group-x point-x < 3)     (up-point-distance knight-group-x nearest-tc-x >= 12)` | — | — | — | — | — | — | — | **LOST** |
| 790 | L10219–L10227 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (or	(up-point-distance knight-group-x ranged-group-x >= 25)     (and(up-compare-goal gl-knight-group-state != SATTACKING)     (up-po...` | — | — | — | — | — | — | — | **LOST** |
| 791 | L10229–L10235 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 0)     (up-point-distance knight-group-x ranged-group-x < 7)` | — | — | — | — | — | — | — | **LOST** |
| 792 | L10237–L10248 | QEVAL @ L9821 | `(defrule     (goal gl-second-turn 1)     (up-compare-goal gl-knight-retreat != -1)` | — | — | — | — | — | — | — | **LOST** |
| 793 | L10251–L10267 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 794 | L10270–L10286 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 795 | L10288–L10297 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 796 | L10299–L10306 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)` | — | — | — | — | — | — | — | **LOST** |
| 797 | L10308–L10313 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-point | — | — | **LOST** |
| 798 | L10315–L10333 | QEVAL @ L9821 | `(defrule     (unit-type-count knight-line >= 1)     (up-group-size c: KnightGroup < 1)     (up-compare-goal SUPERIORITY < 15)     (up-group-size c: RangedGroup >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 799 | L10335–L10346 | QEVAL @ L9821 | `(defrule     (up-group-size c: KnightGroup > 0)     (or	(up-group-size c: RangedGroup < 1)     (up-compare-goal SUPERIORITY >= 20))` | — | — | — | — | — | — | — | **LOST** |
| 800 | L10349–L10360 | QEVAL @ L9821 | `(defrule     (taunt-detected me 77)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 801 | L10362–L10367 | QEVAL @ L9821 | `(defrule     (taunt-detected me 77)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 802 | L10369–L10374 | QEVAL @ L9821 | `(defrule     (taunt-detected me 78)` | — | — | — | — | — | — | — | **LOST** |
| 803 | L10376–L10380 | QEVAL @ L9821 | `(defrule     (true)` | — | — | — | — | — | 11 | — | **LOST** |
| 804 | L10382–L10387 | QEVAL @ L9821 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-point-distance ranged-group-x knight-group-x >= 8)` | goal | — | — | — | — | — | — | **LOST** |
| 805 | L10389–L10393 | QEVAL @ L9821 | `(defrule     (true)` | goal2 | — | — | — | — | — | — | **LOST** |
| 806 | L10395–L10399 | QEVAL @ L9821 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal2 | — | — | — | — | — | — | **LOST** |
| 807 | L10401–L10410 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 808 | L10412–L10420 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 809 | L10422–L10431 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 810 | L10433–L10438 | QEVAL @ L9821 | `(defrule     (false)     (goal gl-knight-retreat 2)` | goal2 | — | — | — | — | — | — | **LOST** |
| 811 | L10440–L10452 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | gl-knight-group-state, split | — | — | up-full-reset-search | up-target-point | — | — | **LOST** |
| 812 | L10454–L10460 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 1)     (up-compare-goal gl-knight-eval >= CostOfFighting)` | gl-knight-retreat | — | — | — | — | — | — | **LOST** |
| 813 | L10462–L10470 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 3)     (or	(up-compare-goal gl-knight-eval >= CostOfIgnoringTCFire)     (or	(not(up-projectile-detected projectile-town-center c:< 3000))   ...` | gl-knight-retreat | — | — | — | — | — | — | **LOST** |
| 814 | L10472–L10479 | QEVAL @ L9821 | `(defrule     (false)     (goal gl-knight-retreat 2)     (up-point-distance knight-group-x ranged-group-x < 10)` | gl-knight-retreat | — | — | — | — | — | — | **LOST** |
| 815 | L10483–L10494 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-enemy-strategy != KRUSH)     (up-compare-goal gl-ranged-style != SEPARATE)     (players-unit-type-count t...` | — | — | — | — | — | — | — | **LOST** |
| 816 | L10496–L10505 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-ranged-style != COMBINED)     (or	(up-compare-goal gl-enemy-strategy == KRUSH)     (or	(players-unit-type...` | — | — | — | — | — | — | — | **LOST** |
| 817 | L10507–L10513 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup < 1)     (up-compare-goal gl-ranged-style != -1)` | — | — | — | — | — | — | — | **LOST** |
| 818 | L10516–L10527 | QRAIDING @ L10481 | `(defrule     (goal gl-tenth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 819 | L10530–L10534 | QRAIDING @ L10481 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 820 | L10536–L10544 | QRAIDING @ L10481 | `(defrule     (game-time > 3)     (goal gl-second-turn 1)     (up-group-size c: RaidGroup < 1)     (unit-type-count archer-line >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 821 | L10546–L10562 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 822 | L10565–L10571 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 823 | L10573–L10583 | QRAIDING @ L10481 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 824 | L10585–L10594 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 825 | L10596–L10603 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)     (up-point-distance raid-group-x home-x >= 25)` | — | — | — | up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 826 | L10605–L10615 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | up-remove-objects | up-target-point | — | — | **LOST** |
| 827 | L10617–L10622 | QRAIDING @ L10481 | `(defrule     (taunt-detected me 86)` | — | — | — | — | — | — | — | **LOST** |
| 828 | L10624–L10642 | QRAIDING @ L10481 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 829 | L10644–L10658 | QRAIDING @ L10481 | `(defrule     (true)     (false)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 830 | L10662–L10672 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 831 | L10675–L10694 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | goal, goal4 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 832 | L10696–L10700 | QRAIDING @ L10481 | `(defrule     (up-compare-goal goal4 >= 1)` | — | — | — | — | — | 1 | — | **LOST** |
| 833 | L10702–L10707 | QRAIDING @ L10481 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | — | **LOST** |
| 834 | L10709–L10713 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 835 | L10717–L10723 | QRAIDING @ L10481 | `(defrule     (or	(up-group-size c: RaidGroup < 1)     (and(players-building-type-count every-enemy watch-tower < 1)     (players-building-type-count every-enemy town-center < 1)))` | — | — | — | — | — | 4 | — | **LOST** |
| 836 | L10725–L10734 | QRAIDING @ L10481 | `(defrule     (true)` | goal1, rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 837 | L10736–L10743 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 838 | L10745–L10750 | QRAIDING @ L10481 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 839 | L10752–L10759 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-object | — | — | — | **LOST** |
| 840 | L10762–L10766 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 13 | — | **LOST** |
| 841 | L10768–L10776 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 842 | L10778–L10782 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 843 | L10785–L10793 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 844 | L10795–L10806 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 845 | L10808–L10819 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 846 | L10821–L10829 | QRAIDING @ L10481 | `(defrule     (false)     (goal SPLIT 1)     (up-timer-status t-raid-target-reset != timer-running)` | — | t-raid-target-reset | — | up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 847 | L10831–L10836 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | up-get-search-state | up-get-search-state | — | — | **LOST** |
| 848 | L10838–L10849 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 849 | L10851–L10865 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 850 | L10867–L10881 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 851 | L10883–L10899 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 852 | L10901–L10907 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 853 | L10909–L10918 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | 1 | — | **LOST** |
| 854 | L10921–L10925 | QRAIDING @ L10481 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 855 | L10928–L10932 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 3 | — | **LOST** |
| 856 | L10934–L10938 | QRAIDING @ L10481 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 857 | L10940–L10947 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 858 | L10949–L10960 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 859 | L10963–L10967 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 4 | — | **LOST** |
| 860 | L10969–L10978 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | up-get-object-data | — | — | **LOST** |
| 861 | L10980–L10991 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search | — | — | — | **LOST** |
| 862 | L11001–L11009 | QRAIDING @ L10481 | `(defrule     (up-compare-goal gl-raid-can-fire != YES)     (up-compare-goal gl-highest-next-attack < arch-firing-threshold-1)     (up-compare-goal goal2 g:<= gl-raid-group-range)` | — | — | — | — | — | — | — | **LOST** |
| 863 | L11011–L11020 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 864 | L11023–L11027 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 4 | — | **LOST** |
| 865 | L11029–L11037 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-can-move YES)     (up-compare-goal goal4 >= 1)     (up-timer-status t-raid-retreat != timer-running)     (or	(goal gl-fifth-turn 1)     (up-compare-go...` | split | t-raid-retreat | — | — | — | — | — | **LOST** |
| 866 | L11039–L11049 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 867 | L11051–L11064 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 868 | L11066–L11071 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | — | **LOST** |
| 869 | L11073–L11083 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | up-target-point | — | — | **LOST** |
| 870 | L11086–L11090 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 1 | — | **LOST** |
| 871 | L11093–L11111 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-can-move YES)     (up-compare-goal goal4 < 1)` | — | — | — | — | — | — | — | **LOST** |
| 872 | L11114–L11118 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 9 | — | **LOST** |
| 873 | L11120–L11124 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 874 | L11127–L11135 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 875 | L11137–L11144 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-1)` | — | — | — | — | — | — | — | **LOST** |
| 876 | L11146–L11153 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-2)` | — | — | — | — | — | — | — | **LOST** |
| 877 | L11155–L11162 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 878 | L11164–L11168 | QRAIDING @ L10481 | `(defrule     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 879 | L11170–L11174 | QRAIDING @ L10481 | `(defrule     (up-point-distance raid-group-x point-x < 8)` | — | — | — | — | — | — | — | **LOST** |
| 880 | L11177–L11182 | QRAIDING @ L10481 | `(defrule     (true)     (false)` | — | — | — | — | — | — | — | **LOST** |
| 881 | L11184–L11202 | QRAIDING @ L10481 | `(defrule     (goal goal1 -1)` | — | — | — | — | — | — | — | **LOST** |
| 882 | L11205–L11210 | QRAIDING @ L10481 | `(defrule     (or	(game-time < 10)     (up-group-size c: RaidGroup < 1))` | — | — | — | — | — | 44 | — | **LOST** |
| 883 | L11212–L11217 | QRAIDING @ L10481 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | — | **LOST** |
| 884 | L11219–L11225 | QRAIDING @ L10481 | `(defrule     (timer-triggered t-raid-retreat)` | — | t-raid-retreat | — | — | — | — | — | **LOST** |
| 885 | L11229–L11237 | QRAIDING @ L10481 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 886 | L11240–L11246 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 887 | L11249–L11255 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 888 | L11257–L11264 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 889 | L11268–L11276 | QRAIDING @ L10481 | `(defrule     (true)` | goal, goal1, rt, sn-focus-player-number | — | — | up-set-target-point | — | — | — | **LOST** |
| 890 | L11279–L11292 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | goal, goal1 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 891 | L11295–L11300 | QRAIDING @ L10481 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 892 | L11303–L11308 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 893 | L11310–L11319 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 894 | L11321–L11328 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 895 | L11330–L11341 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 896 | L11343–L11354 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 897 | L11357–L11362 | QRAIDING @ L10481 | `(defrule     (false)` | — | — | — | — | — | — | — | **LOST** |
| 898 | L11364–L11373 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 899 | L11375–L11382 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 900 | L11384–L11395 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 901 | L11397–L11408 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 902 | L11411–L11420 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type -1)     (up-compare-goal SUPERIORITY >= 15)` | — | — | — | — | — | — | — | **LOST** |
| 903 | L11422–L11431 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type -1)     (up-compare-goal SUPERIORITY < 15)` | — | — | — | — | — | — | — | **LOST** |
| 904 | L11435–L11440 | QRAIDING @ L10481 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 905 | L11443–L11458 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-clean-search, up-find-status-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 906 | L11461–L11467 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 907 | L11469–L11476 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt >= 1)     (goal gl-raid-retreat-type -1)` | — | — | — | — | — | — | — | **LOST** |
| 908 | L11480–L11488 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 909 | L11490–L11495 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-retreat-type FROM-SIEGE)` | goal1, goal3 | — | — | — | — | — | — | **LOST** |
| 910 | L11497–L11501 | QRAIDING @ L10481 | `(defrule     (up-compare-goal gl-enemy-group-size > 0)` | goal5 | — | — | — | — | — | — | **LOST** |
| 911 | L11503–L11507 | QRAIDING @ L10481 | `(defrule     (up-point-distance raid-group-x raid-nearest-fort-x < 15)` | goal1 | — | — | — | — | — | — | **LOST** |
| 912 | L11509–L11517 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style COMBINED)     (goal gl-raid-retreat-type FROM-UNITS)` | goal | — | — | — | — | — | — | **LOST** |
| 913 | L11519–L11527 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style SEPARATE)     (goal gl-raid-retreat-type FROM-UNITS)` | goal | — | — | — | — | — | — | **LOST** |
| 914 | L11529–L11535 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style SEPARATE)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)` | goal1 | — | — | — | — | — | — | **LOST** |
| 915 | L11537–L11543 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style COMBINED)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)` | goal | — | — | — | — | — | — | **LOST** |
| 916 | L11545–L11552 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style -1)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)` | goal | — | — | — | — | — | — | **LOST** |
| 917 | L11554–L11558 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup < 1)` | goal | — | — | — | — | — | — | **LOST** |
| 918 | L11561–L11572 | QRAIDING @ L10481 | `(defrule     (or	(goal gl-raid-can-fire NO)     (up-compare-goal goal4 < 1))     (up-timer-status t-raid-retreat == timer-running)     (or	(goal gl-tenth-turn 1)     (up-compare...` | — | t-raid-retreat | — | up-full-reset-search | — | — | — | **LOST** |
| 919 | L11575–L11583 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type FROM-UNITS)     (up-compare-goal gl-enemy-group-size > 0)` | — | — | — | — | — | — | — | **LOST** |
| 920 | L11585–L11593 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal gl-enemy-group-size < 1)     (up-compare-goal gl-raid-retreat-type != FROM-UNITS))` | — | — | — | — | — | — | — | **LOST** |
| 921 | L11596–L11604 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 922 | L11607–L11612 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 923 | L11614–L11626 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 924 | L11629–L11645 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type HOME-RETREAT)     (or	(goal gl-tenth-turn 1)     (up-compare-goal gl-raid-group-state != RETREATING))` | — | — | — | — | — | — | — | **LOST** |
| 925 | L11647–L11664 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (or	(goal gl-raid-retreat-type FROM-UNITS)     (goal gl-raid-retreat-type FROM-SIEGE))     (or	(goal gl-tenth-turn 1)     (up-compare-goal gl-rai...` | — | — | — | — | — | — | — | **LOST** |
| 926 | L11666–L11682 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)     (or	(goal gl-tenth-turn 1)     (up-compare-goal gl-raid-group-state != RETREATING))` | — | — | — | — | — | — | — | **LOST** |
| 927 | L11685–L11697 | QRAIDING @ L10481 | `(defrule     (true)` | goal, lt, point-x, point-y | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 928 | L11699–L11709 | QRAIDING @ L10481 | `(defrule     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 929 | L11711–L11718 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal lt > 0)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | — | **LOST** |
| 930 | L11720–L11727 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal > 0)` | point-x, point-y | — | — | — | — | — | — | **LOST** |
| 931 | L11729–L11733 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 932 | L11736–L11741 | QRAIDING @ L10481 | `(defrule     (true)` | — | t-raid-target-reset | — | — | — | — | — | **LOST** |
| 933 | L11745–L11752 | QRAIDING @ L10481 | `(defrule     (game-time > 5)     (goal gl-raid-status -1)     (up-group-size c: RaidGroup >= 3)` | — | — | — | — | — | — | — | **LOST** |
| 934 | L11754–L11759 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 935 | L11761–L11767 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-ranged-style SEPARATE)` | — | — | — | up-set-target-point | — | — | — | **LOST** |
| 936 | L11769–L11777 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 937 | L11779–L11786 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 2)` | — | — | — | up-remove-objects | — | — | — | **LOST** |
| 938 | L11788–L11794 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 2)` | — | — | — | up-remove-objects | — | — | — | **LOST** |
| 939 | L11796–L11802 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 2)` | — | — | — | up-remove-objects | — | — | — | **LOST** |
| 940 | L11804–L11818 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 1)` | gl-ancient-raid-target-id, gl-old-raid-target-id | — | — | up-clean-search, up-set-target-object, up-set-target-point | up-get-object-data | — | — | **LOST** |
| 941 | L11820–L11828 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 942 | L11831–L11839 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-TARGET)` | — | — | — | — | — | — | — | **LOST** |
| 943 | L11841–L11849 | QRAIDING @ L10481 | `(defrule     (up-compare-goal gl-raid-status != -1)     (up-timer-status t-raid-waypoint-reevaluate != timer-running)` | gl-raid-status | t-raid-waypoint-reevaluate | — | — | — | — | — | **LOST** |
| 944 | L11852–L11858 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-1)     (up-point-distance raid-group-x raid-target-x < 25)` | — | — | — | — | — | — | — | **LOST** |
| 945 | L11860–L11873 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-1)     (up-point-distance raid-group-x raid-target-x >= 25)` | — | — | — | — | — | — | — | **LOST** |
| 946 | L11875–L11881 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-1)     (up-point-distance raid-group-x raid-waypoint1-x < 4)` | — | — | — | — | — | — | — | **LOST** |
| 947 | L11884–L11890 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-2)     (up-point-distance raid-group-x raid-target-x < 45)` | — | — | — | — | — | — | — | **LOST** |
| 948 | L11892–L11905 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-2)     (up-point-distance raid-group-x raid-target-x >= 45)` | — | — | — | — | — | — | — | **LOST** |
| 949 | L11907–L11913 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-2)     (up-point-distance raid-group-x raid-waypoint2-x < 4)` | — | — | — | — | — | — | — | **LOST** |
| 950 | L11915–L11921 | QRAIDING @ L10481 | `(defrule     (false)     (goal gl-twenty-turn 1)     (goal gl-raid-status MOVING-TO-WAYPOINT-2)` | — | — | — | — | — | — | — | **LOST** |
| 951 | L11924–L11932 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-TARGET)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 952 | L11934–L11942 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt >= 1)     (goal gl-raid-status MOVING-TO-TARGET)     (up-point-distance raid-group-x raid-target-x < 10)` | — | — | — | — | — | — | — | **LOST** |
| 953 | L11944–L11953 | QRAIDING @ L10481 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-raid-status MOVING-TO-TARGET)     (or	(timer-triggered t-raid-target-reset)     (up-point-distance raid-group-x raid-target-x < 4))` | — | t-raid-target-reset | — | — | — | — | — | **LOST** |
| 954 | L11955–L11960 | QRAIDING @ L10481 | `(defrule     (taunt-detected me 21)` | — | — | — | — | — | — | — | **LOST** |
| 955 | L11963–L11976 | QRAIDING @ L10481 | `(defrule     (false)     (up-group-size c: RaidGroup < 3)     (up-compare-goal gl-raid-status != -1)` | gl-raid-status | t-raid-target-reset | — | up-find-local, up-full-reset-search | up-target-point | — | — | **LOST** |
| 956 | L11978–L11985 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 957 | L11987–L11994 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 958 | L11996–L12001 | QRAIDING @ L10481 | `(defrule     (taunt-detected me 99)` | — | — | — | — | — | — | — | **LOST** |
| 959 | L12003–L12007 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 1 | — | **LOST** |
| 960 | L12009–L12020 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 961 | L12022–L12031 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 962 | L12033–L12038 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 963 | L12042–L12052 | QRANGED MICRO @ L12040 | `(defrule     (goal gl-town-safe NO)     (goal gl-defend-town NO)     (up-group-size c: RangedGroup > 0)     (up-compare-goal SUPERIORITY >= 5)` | — | — | — | — | — | — | — | **LOST** |
| 964 | L12054–L12062 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 965 | L12065–L12069 | QRANGED MICRO @ L12040 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 4 | — | **LOST** |
| 966 | L12072–L12080 | QRANGED MICRO @ L12040 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 967 | L12083–L12094 | QRANGED MICRO @ L12040 | `(defrule     (stance-toward focus-player enemy)` | goal, point-x, point-y, rt | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 968 | L12097–L12102 | QRANGED MICRO @ L12040 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 969 | L12104–L12115 | QRANGED MICRO @ L12040 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 970 | L12117–L12124 | QRANGED MICRO @ L12040 | `(defrule     (up-compare-goal rt > 0)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | — | **LOST** |
| 971 | L12126–L12132 | QRANGED MICRO @ L12040 | `(defrule     (up-compare-goal goal > 0)` | point-x, point-y | — | — | — | — | — | — | **LOST** |
| 972 | L12135–L12150 | QRANGED MICRO @ L12040 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 973 | L12152–L12165 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 974 | L12167–L12176 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 975 | L12178–L12188 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 976 | L12190–L12198 | QRANGED MICRO @ L12040 | `(defrule     (false)     (goal SPLIT 1)     (up-group-size c: RangedGroup > 10)     (up-point-distance target-x ranged-group-x < 20)` | — | — | — | — | — | — | — | **LOST** |
| 977 | L12200–L12204 | QRANGED MICRO @ L12040 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 978 | L12206–L12216 | QRANGED MICRO @ L12040 | `(defrule     (false)     (goal gl-fifty-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 979 | L12218–L12234 | QRANGED MICRO @ L12040 | `(defrule     (up-group-size c: RangedGroup > 0)     (unit-type-count skirmisher-line >= 25)     (research-completed ri-elite-skirmisher)     (players-unit-type-count every-enemy...` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 980 | L12237–L12245 | QINITIALIZING GROUP @ L12236 | `(defrule     (up-group-size c: RangedGroup < 1)     (or	(and(unit-type-count skirmisher-line >= 1)     (up-research-status c: ri-elite-skirmisher < research-complete))     (and(...` | split | — | — | — | research, research-completed, up-research | — | — | **LOST** |
| 981 | L12247–L12254 | QINITIALIZING GROUP @ L12236 | `(defrule     (up-group-size c: RangedGroup < 1)     (unit-type-count skirmisher-line >= 1)     (or	(players-unit-type-count any-enemy knight-line >= 3)     (players-unit-type-co...` | split | — | — | — | — | — | — | **LOST** |
| 982 | L12256–L12274 | QINITIALIZING GROUP @ L12236 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 983 | L12276–L12280 | QINITIALIZING GROUP @ L12236 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 1 | — | **LOST** |
| 984 | L12282–L12295 | QINITIALIZING GROUP @ L12236 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 985 | L12297–L12304 | QINITIALIZING GROUP @ L12236 | `(defrule     (false)     (goal SPLIT 1)     (or (up-compare-goal gl-enemy-skirms-nearby < 4)     (up-compare-goal gl-ranged-group-state == HOME-RETREAT))` | — | — | — | up-find-local | — | — | — | **LOST** |
| 986 | L12306–L12315 | QINITIALIZING GROUP @ L12236 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | — | — | — | **LOST** |
| 987 | L12318–L12338 | QREGROUPING @ L12317 | `(defrule     (false)` | — | — | — | — | — | — | — | **LOST** |
| 988 | L12340–L12357 | QREGROUPING @ L12317 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 989 | L12359–L12364 | QREGROUPING @ L12317 | `(defrule     (or	(game-time < 3)     (up-group-size c: RangedGroup < 1))` | — | — | — | — | — | 9 | — | **LOST** |
| 990 | L12366–L12376 | QREGROUPING @ L12317 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 991 | L12378–L12386 | QREGROUPING @ L12317 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 992 | L12388–L12393 | QREGROUPING @ L12317 | `(defrule     (false)     (goal SPLIT 1)` | — | — | — | up-find-local | — | — | — | **LOST** |
| 993 | L12395–L12402 | QREGROUPING @ L12317 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)     (up-point-distance ranged-group-x home-x >= 25)` | — | — | — | up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 994 | L12404–L12415 | QREGROUPING @ L12317 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-point | — | — | **LOST** |
| 995 | L12417–L12422 | QREGROUPING @ L12317 | `(defrule     (taunt-detected me 86)` | — | — | — | — | — | — | — | **LOST** |
| 996 | L12424–L12442 | QREGROUPING @ L12317 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 997 | L12444–L12458 | QREGROUPING @ L12317 | `(defrule     (true)     (false)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 998 | L12460–L12472 | QREGROUPING @ L12317 | `(defrule     (false)     (up-compare-goal lt >= 1)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-point | — | — | **LOST** |
| 999 | L12480–L12486 | QMOVING @ L12474 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (and(players-current-age target-player < castle-age)     (players-military-population target-player < 4)))` | — | — | — | — | — | 16 | — | **LOST** |
| 1000 | L12488–L12494 | QMOVING @ L12474 | `(defrule     (timer-triggered t-ranged-retreat)` | — | t-ranged-retreat | — | — | — | — | — | **LOST** |
| 1001 | L12496–L12504 | QMOVING @ L12474 | `(defrule     (up-compare-goal gl-mangos-nearby >= 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1002 | L12506–L12515 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1003 | L12517–L12526 | QMOVING @ L12474 | `(defrule     (up-compare-goal lt < 1)     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-mangos-nearby >= 1)     (up-point-distance ranged-group-x home-x >= 5)` | — | — | — | — | — | — | — | **LOST** |
| 1004 | L12528–L12538 | QMOVING @ L12474 | `(defrule     (game-time > 10)     (up-group-size c: RangedGroup > 0)     (up-point-distance ranged-group-x home-x >= 8)     (up-point-distance ranged-group-x enemy-group-x < 20)...` | split | — | — | — | — | — | — | **LOST** |
| 1005 | L12540–L12548 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (player-valid 5)` | — | — | — | — | — | — | — | **LOST** |
| 1006 | L12550–L12561 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (not(player-valid 5))     (or	(up-compare-goal SUPERIORITY < 5)     (or	(current-age-time < 30)     (up-research-status c: castle-age == research...` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1007 | L12563–L12572 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (not(player-valid 5))     (up-compare-goal SUPERIORITY >= 5)` | — | — | — | — | — | — | — | **LOST** |
| 1008 | L12574–L12579 | QMOVING @ L12474 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | — | **LOST** |
| 1009 | L12581–L12585 | QMOVING @ L12474 | `(defrule     (up-point-distance ranged-group-x home-x > 40)` | goal1 | — | — | — | — | — | — | **LOST** |
| 1010 | L12587–L12591 | QMOVING @ L12474 | `(defrule     (up-point-distance enemy-x ranged-group-x < 30)` | goal | — | — | — | — | — | — | **LOST** |
| 1011 | L12593–L12598 | QMOVING @ L12474 | `(defrule     (up-point-distance ranged-group-x home-x < 15)` | goal, goal1 | — | — | — | — | — | — | **LOST** |
| 1012 | L12600–L12604 | QMOVING @ L12474 | `(defrule     (up-compare-goal gl-enemy-group-size < 1)` | goal | — | — | — | — | — | — | **LOST** |
| 1013 | L12606–L12615 | QMOVING @ L12474 | `(defrule     (up-timer-status t-ranged-retreat == timer-running)     (or	(goal gl-fifth-turn 1)     (up-compare-goal gl-ranged-group-state != HOME-RETREAT))` | split | t-ranged-retreat | — | — | — | — | — | **LOST** |
| 1014 | L12617–L12622 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 1015 | L12624–L12637 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-ranged-retreat != 1)` | — | — | — | — | — | — | — | **LOST** |
| 1016 | L12639–L12652 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (goal gl-ranged-retreat 1)` | — | — | — | — | — | — | — | **LOST** |
| 1017 | L12655–L12659 | QMOVING @ L12474 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 13 | — | **LOST** |
| 1018 | L12661–L12674 | QMOVING @ L12474 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5, goal6 | — | — | — | — | — | — | **LOST** |
| 1019 | L12676–L12682 | QMOVING @ L12474 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-castle-x < CastleRetreat...` | goal5 | — | — | — | research, research-completed | — | — | **LOST** |
| 1020 | L12684–L12690 | QMOVING @ L12474 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-tc-x < TCRetreatDistance)` | goal2 | — | — | — | research, research-completed | — | — | **LOST** |
| 1021 | L12692–L12697 | QMOVING @ L12474 | `(defrule     (not(research-completed ri-leather-archer-armor))     (up-point-distance ranged-group-x nearest-tc-x < 9)` | goal2 | — | — | — | research, research-completed | — | — | **LOST** |
| 1022 | L12699–L12704 | QMOVING @ L12474 | `(defrule     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)     (up-compare-goal gl-army-damage-potential < CostOfIgnoringTowers)` | goal3 | — | — | — | — | — | — | **LOST** |
| 1023 | L12706–L12710 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1024 | L12712–L12723 | QMOVING @ L12474 | `(defrule     (false)     (goal gl-can-move YES)     (up-point-distance home-x ranged-group-x < 20)     (up-timer-status t-ranged-retreat != timer-running)     (up-compare-goal g...` | split | t-ranged-retreat | — | — | — | — | — | **LOST** |
| 1025 | L12725–L12734 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1026 | L12736–L12745 | QMOVING @ L12474 | `(defrule     (goal SPLIT 2)     (or (and(up-compare-goal gl-target-distance g:<= goal)` | — | — | — | — | — | — | — | **LOST** |
| 1027 | L12747–L12762 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1028 | L12764–L12775 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1029 | L12777–L12789 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1030 | L12791–L12795 | QMOVING @ L12474 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 1031 | L12799–L12807 | QCCR @ L12797 | `(defrule     (true)` | goal, goal3, goal4, goal5, goal6 | — | — | — | — | — | — | **LOST** |
| 1032 | L12809–L12817 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1033 | L12819–L12832 | QCCR @ L12797 | `(defrule     (up-compare-goal lt >= 1)` | goal | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data, up-get-search-state | — | — | **LOST** |
| 1034 | L12834–L12840 | QCCR @ L12797 | `(defrule     (taunt-detected me 109)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1035 | L12842–L12847 | QCCR @ L12797 | `(defrule     (taunt-detected me 110)` | — | — | — | — | — | — | — | **LOST** |
| 1036 | L12849–L12855 | QCCR @ L12797 | `(defrule     (or	(and(up-compare-goal goal >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 1037 | L12858–L12864 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 1038 | L12866–L12870 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-find-local | — | — | — | **LOST** |
| 1039 | L12872–L12877 | QCCR @ L12797 | `(defrule     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local | research, research-completed | — | — | **LOST** |
| 1040 | L12879–L12884 | QCCR @ L12797 | `(defrule     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local | research, research-completed | — | — | **LOST** |
| 1041 | L12886–L12891 | QCCR @ L12797 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (research-available ri-chain-barding))` | — | — | — | up-find-local | research | — | — | **LOST** |
| 1042 | L12893–L12897 | QCCR @ L12797 | `(defrule     (up-compare-goal SUPERIORITY < 20)` | — | — | — | up-find-local | — | — | — | **LOST** |
| 1043 | L12899–L12908 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | — | **LOST** |
| 1044 | L12910–L12916 | QCCR @ L12797 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1045 | L12918–L12922 | QCCR @ L12797 | `(defrule     (up-compare-goal gl-ninety-turn < 45)` | goal | — | — | — | — | — | — | **LOST** |
| 1046 | L12924–L12928 | QCCR @ L12797 | `(defrule     (up-compare-goal gl-ninety-turn < 75)` | goal1 | — | — | — | — | — | — | **LOST** |
| 1047 | L12930–L12934 | QCCR @ L12797 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal2 | — | — | — | — | — | — | **LOST** |
| 1048 | L12936–L12947 | QCCR @ L12797 | `(defrule     (up-compare-goal lt > 0)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-point | — | — | **LOST** |
| 1049 | L12949–L12963 | QCCR @ L12797 | `(defrule     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1050 | L12965–L12970 | QCCR @ L12797 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 1051 | L12974–L12983 | QTCR @ L12972 | `(defrule     (true)` | goal, goal1, goal3, goal4, goal5, goal6 | — | — | — | — | — | — | **LOST** |
| 1052 | L12985–L12993 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1053 | L12995–L13008 | QTCR @ L12972 | `(defrule     (up-compare-goal lt >= 1)` | goal | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data, up-get-search-state | — | — | **LOST** |
| 1054 | L13010–L13016 | QTCR @ L12972 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1055 | L13019–L13027 | QTCR @ L12972 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1056 | L13030–L13037 | QTCR @ L12972 | `(defrule     (false)     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 1057 | L13039–L13044 | QTCR @ L12972 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | — | **LOST** |
| 1058 | L13046–L13053 | QTCR @ L12972 | `(defrule     (taunt-detected me 57)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1059 | L13055–L13060 | QTCR @ L12972 | `(defrule     (taunt-detected me 58)` | — | — | — | — | — | — | — | **LOST** |
| 1060 | L13062–L13069 | QTCR @ L12972 | `(defrule     (or (up-compare-goal goal1 < 460)` | — | — | — | — | — | — | — | **LOST** |
| 1061 | L13072–L13078 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 1062 | L13080–L13084 | QTCR @ L12972 | `(defrule     (goal gl-strategy KRUSH)` | — | — | — | — | — | — | — | **LOST** |
| 1063 | L13086–L13092 | QTCR @ L12972 | `(defrule     (goal gl-strategy KRUSH)     (up-projectile-detected projectile-town-center c:< 3000)     (up-projectile-target projectile-town-center == cavalry-class)` | — | — | — | — | — | — | — | **LOST** |
| 1064 | L13094–L13098 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-find-local | — | — | — | **LOST** |
| 1065 | L13100–L13105 | QTCR @ L12972 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local | research, research-completed | — | — | **LOST** |
| 1066 | L13107–L13114 | QTCR @ L12972 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1067 | L13116–L13126 | QTCR @ L12972 | `(defrule     (goal gl-strategy KRUSH)     (up-projectile-detected projectile-town-center c:< 3000)     (up-projectile-target projectile-town-center == cavalry-class)     (or	(up...` | — | — | — | up-find-local | research, up-research | — | — | **LOST** |
| 1068 | L13128–L13137 | QTCR @ L12972 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1069 | L13139–L13143 | QTCR @ L12972 | `(defrule     (up-compare-goal SUPERIORITY < 20)` | — | — | — | up-find-local | — | — | — | **LOST** |
| 1070 | L13145–L13152 | QTCR @ L12972 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local, up-remove-objects, up-set-target-point | research, research-completed | — | — | **LOST** |
| 1071 | L13154–L13165 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1072 | L13167–L13173 | QTCR @ L12972 | `(defrule     (true)` | goal, goal1, goal2 | — | — | — | — | — | — | **LOST** |
| 1073 | L13175–L13179 | QTCR @ L12972 | `(defrule     (up-compare-goal gl-ninety-turn < 45)` | goal | — | — | — | — | — | — | **LOST** |
| 1074 | L13181–L13185 | QTCR @ L12972 | `(defrule     (up-compare-goal gl-ninety-turn < 75)` | goal1 | — | — | — | — | — | — | **LOST** |
| 1075 | L13187–L13193 | QTCR @ L12972 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal2 | — | — | — | — | — | — | **LOST** |
| 1076 | L13195–L13206 | QTCR @ L12972 | `(defrule     (up-compare-goal lt > 0)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-point | — | — | **LOST** |
| 1077 | L13208–L13222 | QTCR @ L12972 | `(defrule     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1078 | L13224–L13229 | QTCR @ L12972 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 1079 | L13232–L13236 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 12 | — | **LOST** |
| 1080 | L13238–L13245 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: RangedGroup >= 7)     (up-point-distance march-x enemy-x >= 40)` | — | — | — | — | — | — | — | **LOST** |
| 1081 | L13247–L13254 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal, goal1, goal2, goal3 | — | — | — | — | — | — | **LOST** |
| 1082 | L13256–L13263 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-castle-x != -1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ra...` | goal3 | — | — | — | research, research-completed | — | — | **LOST** |
| 1083 | L13265–L13272 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-tc-x != -1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged...` | goal | — | — | — | research, research-completed | — | — | **LOST** |
| 1084 | L13274–L13281 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-tc-x != -1)     (up-point-distance ranged-group-x nearest-tc-x < 9)     (or (up-compare-goal SUPERIORITY < 20)     (not(research-completed ...` | goal | — | — | — | research, research-completed | — | — | **LOST** |
| 1085 | L13283–L13288 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: KnightGroup > 0)     (up-point-distance ranged-group-x knight-group-x >= 12)` | goal1 | — | — | — | — | — | — | **LOST** |
| 1086 | L13290–L13296 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-tower-x != -1)     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)     (up-compare-goal gl-army-damage-potential ...` | goal2 | — | — | — | — | — | — | **LOST** |
| 1087 | L13298–L13305 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (timer-triggered t-failsafe)     (up-timer-status t-ranged-retreat != timer-running)` | — | t-failsafe, t-ranged-retreat | — | — | — | — | — | **LOST** |
| 1088 | L13307–L13314 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-timer-status t-ranged-retreat != timer-running)     (or	(goal gl-fifth-turn 1)     (up-compare-goal gl-ranged-group-state != MARCHING))     (up-compare-goal gl-...` | split | t-ranged-retreat | — | — | — | — | — | **LOST** |
| 1089 | L13316–L13325 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1090 | L13327–L13334 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | — | **LOST** |
| 1091 | L13336–L13349 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1092 | L13351–L13356 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (taunt-detected me 55)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1093 | L13358–L13365 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (taunt-detected me 56)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1094 | L13367–L13376 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (taunt-detected me 37)` | — | — | — | — | — | — | — | **LOST** |
| 1095 | L13379–L13391 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5, goal6 | — | — | — | — | — | — | **LOST** |
| 1096 | L13393–L13397 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-point-distance ranged-group-x enemy-group-x < 6)` | goal3 | — | — | — | — | — | — | **LOST** |
| 1097 | L13399–L13406 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-castle-x < CastleRetreat...` | goal3, goal6 | — | — | — | research, research-completed | — | — | **LOST** |
| 1098 | L13408–L13415 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-tc-x < TCRetreatDistance)` | goal, goal3 | — | — | — | research, research-completed | — | — | **LOST** |
| 1099 | L13417–L13423 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (not(research-completed ri-leather-archer-armor))     (up-point-distance ranged-group-x nearest-tc-x < 10)` | goal, goal3 | — | — | — | research, research-completed | — | — | **LOST** |
| 1100 | L13425–L13430 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: KnightGroup > 0)     (up-point-distance ranged-group-x knight-group-x >= 12)` | goal1 | — | — | — | — | — | — | **LOST** |
| 1101 | L13432–L13437 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)     (up-compare-goal gl-army-damage-potential < CostOfIgnoringTowers)` | goal2 | — | — | — | — | — | — | **LOST** |
| 1102 | L13439–L13443 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal gl-melee-in-range >= 3)` | goal4 | — | — | — | — | — | — | **LOST** |
| 1103 | L13445–L13449 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1104 | L13451–L13457 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1105 | L13459–L13466 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal gl-can-move YES)     (up-compare-goal gl-melee-in-range >= 1)     (up-point-distance point-x ranged-group-x >= 3)` | — | — | — | — | — | — | — | **LOST** |
| 1106 | L13468–L13482 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | up-full-reset-search | — | — | — | **LOST** |
| 1107 | L13484–L13490 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | — | **LOST** |
| 1108 | L13492–L13502 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1109 | L13505–L13510 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | gl-direction | — | — | — | — | — | — | **LOST** |
| 1110 | L13512–L13527 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5, goal6, goal7, goal8 | — | — | — | — | — | — | **LOST** |
| 1111 | L13529–L13533 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (research-completed ri-elite-skirmisher)` | goal6 | — | — | — | research, research-completed | — | — | **LOST** |
| 1112 | L13535–L13550 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal gl-can-move YES)     (up-compare-goal gl-melee-in-range < 1)     (up-compare-goal gl-enemy-group-size >= 1)     (up-compare-goal gl-target-distance g:<= goal8)` | — | — | — | — | — | — | — | **LOST** |
| 1113 | L13553–L13560 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal gl-thirty-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1114 | L13562–L13567 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1115 | L13569–L13575 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1116 | L13577–L13584 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1117 | L13586–L13592 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1118 | L13594–L13600 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1119 | L13602–L13606 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1120 | L13609–L13616 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal2, goal3, goal7, goal8 | — | — | — | — | — | — | **LOST** |
| 1121 | L13618–L13624 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-castle-x < CastleRetreat...` | goal8 | — | — | — | research, research-completed | — | — | **LOST** |
| 1122 | L13626–L13632 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-tc-x < TCRetreatDistance)` | goal2 | — | — | — | research, research-completed | — | — | **LOST** |
| 1123 | L13634–L13639 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (not(research-completed ri-leather-archer-armor))     (up-point-distance ranged-group-x nearest-tc-x < 9)` | goal2 | — | — | — | research, research-completed | — | — | **LOST** |
| 1124 | L13641–L13646 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal SUPERIORITY < 10)     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)` | goal3 | — | — | — | — | — | — | **LOST** |
| 1125 | L13648–L13652 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1126 | L13655–L13663 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1127 | L13665–L13671 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | — | **LOST** |
| 1128 | L13673–L13679 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (false)     (up-point-distance point-x ranged-group-x < 15)` | — | — | — | — | — | — | — | **LOST** |
| 1129 | L13681–L13691 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1130 | L13693–L13699 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal goal7 3)     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1131 | L13701–L13705 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 1132 | L13708–L13712 | QCOMBAT MODE @ L13707 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 7 | — | **LOST** |
| 1133 | L13714–L13719 | QCOMBAT MODE @ L13707 | `(defrule     (or	(game-time < 5)     (goal RETREATING 0))` | — | — | — | — | — | 6 | — | **LOST** |
| 1134 | L13721–L13726 | QCOMBAT MODE @ L13707 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1135 | L13728–L13733 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | — | **LOST** |
| 1136 | L13735–L13743 | QCOMBAT MODE @ L13707 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1137 | L13747–L13759 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1138 | L13763–L13775 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1139 | L13778–L13786 | QCOMBAT MODE @ L13707 | `(defrule     (false)     (goal gl-can-fire YES)     (up-group-size c: RangedGroup >= 23)     (up-compare-goal gl-ranged-group-state != FIRING)     (up-timer-status t-ranged-retr...` | split | t-ranged-retreat | — | — | — | — | — | **LOST** |
| 1140 | L13788–L13801 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | — | — | — | — | up-get-object-data | — | — | **LOST** |
| 1141 | L13811–L13822 | QFAILSAFE @ L13810 | `(defrule     (food-amount < 400)     (gold-amount >= 180)     (goal gl-fifth-turn 1)     (unit-type-count-total archer >= 2)     (up-compare-sn sn-gold-gatherer-percentage > 0) ...` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage | — | — | — | research-pending, unit-type-count-total, up-research | — | — | **LOST** |
| 1142 | L13826–L13834 | QDARK @ L13824 | `(defrule     (true)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1143 | L13837–L13849 | QDARK @ L13824 | `(defrule     (current-age-time >= 15)     (civilian-population >= 7)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-maximum-wood-drop-distance, sn-stone-gatherer-percentage, sn-wood-dropsite-distance, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1144 | L13851–L13859 | QDARK @ L13824 | `(defrule     (civilian-population >= 14)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1145 | L13862–L13866 | QKRUSH @ L13861 | `(defrule     (up-compare-goal gl-strategy != KRUSH)` | — | — | — | — | — | 8 | — | **LOST** |
| 1146 | L13870–L13879 | QKRUSH @ L13861 | `(defrule     (civilian-population >= 15)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1147 | L13882–L13892 | QKRUSH @ L13861 | `(defrule     (false)     (civilian-population >= 16)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1148 | L13895–L13906 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1149 | L13909–L13921 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)     (up-research-status c: feudal-age >= research-pending)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1150 | L13925–L13935 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (up-research-status c: castle-age >= research-pending)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1151 | L13939–L13949 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (current-age >= castle-age)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1152 | L13952–L13964 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (current-age >= castle-age)     (or	(current-age-time >= 220)     (building-type-count-total farm >= 19))` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1153 | L13967–L13978 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (current-age-time >= 480)     (current-age >= castle-age)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1154 | L13983–L13989 | QFLUSH @ L13980 | `(defrule     (civilian-population == 18)     (goal gl-strategy FLUSH)` | split | — | — | — | — | — | — | **LOST** |
| 1155 | L13991–L14005 | QFLUSH @ L13980 | `(defrule     (goal SPLIT 1)     (food-amount < 230)     (or	(up-compare-goal gl-killed-boar-count < 2)     (and(up-compare-goal gl-killed-deer-count < 1)     (up-compare-goal gl...` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1156 | L14007–L14017 | QFLUSH @ L13980 | `(defrule     (goal SPLIT 1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1157 | L14020–L14030 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (or	(food-amount > 490)     (up-compare-goal gl-age-loading == FA-loading))` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1158 | L14033–L14042 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (current-age == feudal-age)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1159 | L14045–L14054 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count-total blacksmith >= 1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | building-type-count-total | — | ShadowByzantine/04_construction.per#3 | **UNKNOWN** |
| 1160 | L14057–L14066 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (up-research-status c: ri-fletching >= research-pending)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1161 | L14069–L14081 | QFLUSH @ L13980 | `(defrule     (game-time > 10)     (goal gl-strategy FLUSH)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1162 | L14084–L14098 | QFLUSH @ L13980 | `(defrule     (game-time > 10)     (goal gl-strategy FLUSH)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)     (dropsite-min-distance stone < 5)     (...` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1163 | L14101–L14111 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count-total market >= 1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1164 | L14115–L14124 | QKNIGHTS @ L14113 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-age-loading >= CA-loading)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1165 | L14127–L14137 | QKNIGHTS @ L14113 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-age-loading >= CA-loading)     (up-compare-goal gl-build-progress >= EskirmsNumber)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1166 | L14140–L14149 | QKNIGHTS @ L14113 | `(defrule     (current-age == castle-age)     (goal gl-strategy FLUSH)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1167 | L14152–L14163 | QKNIGHTS @ L14113 | `(defrule     (current-age-time > 300)     (current-age == castle-age)     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress >= ChainBardingNumber)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1168 | L14166–L14176 | QKNIGHTS @ L14113 | `(defrule     (current-age-time > 600)     (current-age == castle-age)     (goal gl-strategy FLUSH)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1169 | L14180–L14189 | QSIEGE @ L14178 | `(defrule     (goal gl-strategy SIEGE)     (up-compare-goal gl-age-loading >= CA-loading)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1170 | L14192–L14201 | QSIEGE @ L14178 | `(defrule     (current-age == castle-age)     (goal gl-strategy SIEGE)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/03_economy.per#2 | **UNKNOWN** |
| 1171 | L14204–L14214 | QSIEGE @ L14178 | `(defrule     (current-age-time > 300)     (current-age == castle-age)     (goal gl-strategy SIEGE)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1172 | L14294–L14307 | QSCALEMAIL @ L14293 | `(defrule     (goal gl-strategy FLUSH)     (game-time >= 1080)` | — | — | — | — | — | — | — | **LOST** |
| 1173 | L14309–L14313 | QSCALEMAIL @ L14293 | `(defrule     (goal gl-progression-pause SCALEMAIL)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1174 | L14315–L14324 | QSCALEMAIL @ L14293 | `(defrule     (goal gl-progression-pause SCALEMAIL)     (can-research-with-escrow ri-scale-mail)` | gl-progression-pause | — | can-research-with-escrow, set-escrow-percentage | — | up-research | — | — | **LOST** |
| 1175 | L14327–L14340 | QCHAINMAIL @ L14326 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (research-completed ri-pikeman)     (up-research-status c: ri-chain-mail < research-pending)     (up...` | gl-progression-pause | — | — | — | research, research-completed, research-pending, up-research | — | — | **LOST** |
| 1176 | L14342–L14347 | QCHAINMAIL @ L14326 | `(defrule     (goal gl-progression-pause CHAINMAIL)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1177 | L14349–L14360 | QCHAINMAIL @ L14326 | `(defrule     (goal gl-progression-pause CHAINMAIL)     (can-research-with-escrow ri-chain-mail)` | gl-progression-pause | — | can-research-with-escrow, set-escrow-percentage | — | up-research | — | — | **LOST** |
| 1178 | L14364–L14372 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item IRONCASTING)     (can-research-with-escrow ri-iron-casting)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1179 | L14374–L14380 | QIRONCASTING @ L14362 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1180 | L14382–L14389 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != IRONCASTING)     (up-compare-goal gl-build-progress == KrushIronCastingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1181 | L14391–L14400 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == IRONCASTING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1182 | L14402–L14409 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item IRONCASTING)     (up-research-status c: ri-iron-casting >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1183 | L14412–L14420 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item IRONCASTING)     (can-research-with-escrow ri-iron-casting)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1184 | L14422–L14428 | QIRONCASTING @ L14362 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1185 | L14430–L14437 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != IRONCASTING)     (up-compare-goal gl-build-progress == IronCastingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1186 | L14439–L14448 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == IRONCASTING)` | — | — | release-escrow, set-escrow-percentage, up-modify-escrow | — | — | — | — | **LOST** |
| 1187 | L14450–L14457 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item IRONCASTING)     (up-research-status c: ri-iron-casting >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1188 | L14461–L14469 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item FORGING)     (can-research-with-escrow ri-forging)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1189 | L14471–L14477 | QFORGING @ L14459 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1190 | L14479–L14487 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != FORGING)     (up-compare-goal gl-build-progress == ForgingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1191 | L14489–L14499 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == FORGING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1192 | L14501–L14508 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item FORGING)     (up-research-status c: ri-forging >= research-pending)` | gl-build-progress | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1193 | L14511–L14519 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item FORGING)     (can-research-with-escrow ri-forging)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1194 | L14521–L14527 | QFORGING @ L14459 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1195 | L14529–L14536 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != FORGING)     (up-compare-goal gl-build-progress == KrushForgingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1196 | L14538–L14548 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == FORGING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1197 | L14550–L14557 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item FORGING)     (up-research-status c: ri-forging >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1198 | L14561–L14569 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item CHAINBARDING)     (can-research-with-escrow ri-chain-barding)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1199 | L14571–L14577 | QCHAINBARDING @ L14559 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1200 | L14579–L14586 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != CHAINBARDING)     (up-compare-goal gl-build-progress == KrushChainBardingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1201 | L14588–L14599 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (current-age-time >= 460)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == CHAINBARDING)` | — | — | set-escrow-percentage | — | — | — | — | **LOST** |
| 1202 | L14601–L14608 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item CHAINBARDING)     (up-research-status c: ri-chain-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1203 | L14611–L14619 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item CHAINBARDING)     (can-research-with-escrow ri-chain-barding)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1204 | L14621–L14627 | QCHAINBARDING @ L14559 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1205 | L14629–L14636 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != CHAINBARDING)     (up-compare-goal gl-build-progress == ChainBardingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1206 | L14638–L14647 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == CHAINBARDING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1207 | L14649–L14656 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item CHAINBARDING)     (up-research-status c: ri-chain-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1208 | L14660–L14670 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (current-age-time >= 180)     (current-age == castle-age)     (goal gl-progression-pause -1)     (goal gl-current-build-item SCALEBARDI...` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1209 | L14672–L14678 | QSCALEBARDING @ L14658 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1210 | L14680–L14687 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != SCALEBARDING)     (up-compare-goal gl-build-progress == KrushScaleBardingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1211 | L14689–L14702 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (current-age-time >= 180)     (current-age == castle-age)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-curr...` | — | — | set-escrow-percentage | — | — | — | — | **LOST** |
| 1212 | L14704–L14711 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item SCALEBARDING)     (up-research-status c: ri-scale-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1213 | L14714–L14722 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item SCALEBARDING)     (can-research-with-escrow ri-scale-barding)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1214 | L14724–L14730 | QSCALEBARDING @ L14658 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1215 | L14732–L14739 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != SCALEBARDING)     (up-compare-goal gl-build-progress == ScaleBardingNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1216 | L14741–L14751 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == SCALEBARDING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1217 | L14753–L14760 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item SCALEBARDING)     (up-research-status c: ri-scale-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1218 | L14763–L14772 | QXBOW @ L14762 | `(defrule     (current-age >= castle-age)     (goal gl-progression-pause -1)     (unit-type-count-total archer-line >= 4)     (up-compare-goal gl-build-progress >= BowsawNumber) ...` | gl-progression-pause | — | — | — | research-pending, unit-type-count-total, up-research | — | — | **LOST** |
| 1219 | L14774–L14782 | QXBOW @ L14762 | `(defrule     (goal gl-progression-pause XBOW)     (up-can-research gl-escrow-state c: ri-crossbow)` | gl-progression-pause | — | — | — | up-research | — | — | **LOST** |
| 1220 | L14785–L14798 | QPIKES @ L14784 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-enemy-civ NORMAL)     (current-age >= castle-age)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-bui...` | split | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1221 | L14800–L14808 | QPIKES @ L14784 | `(defrule     (goal SPLIT 1)` | gl-progression-pause | — | set-escrow-percentage | — | — | — | — | **LOST** |
| 1222 | L14810–L14821 | QPIKES @ L14784 | `(defrule     (goal gl-progression-pause PIKES)     (can-research-with-escrow ri-pikeman)` | gl-progression-pause | — | can-research-with-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1223 | L14825–L14833 | QAGE @ L14823 | `(defrule     (goal gl-strategy KRUSH)     (research-available feudal-age)     (up-compare-goal gl-need-vills != NO)     (unit-type-count-total villager >= KrushDarkAgeVills)` | — | — | — | — | research, unit-type-count-total | — | — | **LOST** |
| 1224 | L14835–L14842 | QAGE @ L14823 | `(defrule     (goal gl-strategy FLUSH)     (research-available feudal-age)     (up-compare-goal gl-need-vills != NO)     (unit-type-count-total villager >= FlushDarkAgeVills)` | gl-need-vills | — | — | — | research, unit-type-count-total | — | — | **LOST** |
| 1225 | L14844–L14852 | QAGE @ L14823 | `(defrule     (goal gl-strategy FLUSH)     (research-available feudal-age)     (up-compare-goal gl-need-vills == NO)     (unit-type-count-total villager < FlushDarkAgeVills)` | gl-need-vills | — | — | — | research, unit-type-count-total | — | — | **LOST** |
| 1226 | L14854–L14866 | QAGE @ L14823 | `(defrule     (can-research feudal-age)     (or	(and(goal gl-strategy FLUSH)     (unit-type-count-total villager >= FlushDarkAgeVills))     (and(goal gl-strategy KRUSH)     (unit...` | gl-age-loading | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1227 | L14870–L14879 | QCUP @ L14868 | `(defrule     (goal gl-strategy KRUSH)     (current-age == feudal-age)     (up-compare-goal gl-need-vills != NO)     (up-research-status c: castle-age < research-pending)     (un...` | — | — | — | — | research-pending, unit-type-count-total, up-research | — | — | **LOST** |
| 1228 | L14881–L14891 | QCUP @ L14868 | `(defrule     (food-amount >= 640)     (gold-amount >= 150)     (goal gl-strategy FLUSH)     (research-available castle-age)     (or (goal gl-current-build-item CUP)     (unit-ty...` | gl-need-vills | — | — | — | research | — | — | **LOST** |
| 1229 | L14893–L14905 | QCUP @ L14868 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item CUP)     (can-research-with-escrow castle-age)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1230 | L14908–L14914 | QCUP @ L14868 | `(defrule     (goal gl-current-build-item CUP)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1231 | L14917–L14923 | QCUP @ L14868 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress > CupNumber)     (up-research-status c: castle-age < research-pending)` | gl-build-progress | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1232 | L14925–L14932 | QCUP @ L14868 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-build-progress > KrushCupNumber)     (up-research-status c: castle-age < research-pending)` | gl-build-progress | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1233 | L14934–L14942 | QCUP @ L14868 | `(defrule     (goal gl-strategy KRUSH)     (current-age == feudal-age)     (up-compare-goal gl-current-build-item != CUP)     (up-compare-goal gl-build-progress == KrushCupNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1234 | L14944–L14956 | QCUP @ L14868 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-enemy-strategy-type FC)     (up-compare-goal gl-current-build-item != CUP)     (up-compare-goal gl-build-progress == CupNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1235 | L14958–L14971 | QCUP @ L14868 | `(defrule     (goal gl-strategy FLUSH)     (research-available castle-age)     (goal gl-enemy-strategy-type FLUSH)     (up-compare-goal gl-current-build-item != CUP)     (up-comp...` | — | — | — | — | research | — | — | **LOST** |
| 1236 | L14974–L14985 | QFLTCH @ L14973 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item FLTCH)     (can-research-with-escrow ri-fletching)` | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | research | — | — | **LOST** |
| 1237 | L14987–L14993 | QFLTCH @ L14973 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1238 | L14995–L15004 | QFLTCH @ L14973 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress == 9)     (up-compare-goal gl-current-build-item != FLTCH)` | — | — | — | — | — | — | — | **LOST** |
| 1239 | L15006–L15014 | QFLTCH @ L14973 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count blacksmith >= 1)     (up-compare-goal gl-current-build-item == FLTCH)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1240 | L15016–L15022 | QFLTCH @ L14973 | `(defrule     (goal gl-current-build-item FLTCH)     (up-research-status c: ri-fletching >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1241 | L15025–L15032 | QLAA @ L15024 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item LAA)     (can-research-with-escrow ri-leather-archer-armor)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1242 | L15034–L15040 | QLAA @ L15024 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1243 | L15042–L15051 | QLAA @ L15024 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LAA)     (up-compare-goal gl-build-progress == LeatherArcherArmorNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1244 | L15053–L15062 | QLAA @ L15024 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == LAA)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1245 | L15064–L15070 | QLAA @ L15024 | `(defrule     (goal gl-current-build-item LAA)     (up-research-status c: ri-leather-archer-armor >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1246 | L15073–L15082 | QPAA @ L15072 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item PAA)     (can-research-with-escrow ri-padded-archer-armor)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1247 | L15084–L15090 | QPAA @ L15072 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1248 | L15092–L15100 | QPAA @ L15072 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != PAA)     (up-compare-goal gl-build-progress == PaddedArcherArmorNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1249 | L15102–L15111 | QPAA @ L15072 | `(defrule     (goal gl-current-build-item PAA)     (up-research-status c: ri-fletching >= research-complete)` | — | — | release-escrow, set-escrow-percentage, up-modify-escrow | — | up-research | — | — | **LOST** |
| 1250 | L15113–L15119 | QPAA @ L15072 | `(defrule     (goal gl-current-build-item PAA)     (up-research-status c: ri-padded-archer-armor >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1251 | L15122–L15129 | QBODKIN @ L15121 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item BODKIN)     (can-research-with-escrow ri-bodkin-arrow)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1252 | L15131–L15137 | QBODKIN @ L15121 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1253 | L15139–L15146 | QBODKIN @ L15121 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != BODKIN)     (up-compare-goal gl-build-progress == BodkinNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1254 | L15148–L15156 | QBODKIN @ L15121 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == BODKIN)` | — | — | set-escrow-percentage | — | — | — | — | **LOST** |
| 1255 | L15158–L15165 | QBODKIN @ L15121 | `(defrule     (false)     (up-compare-goal gl-current-build-item == BODKIN)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1256 | L15167–L15173 | QBODKIN @ L15121 | `(defrule     (goal gl-current-build-item BODKIN)     (up-research-status c: ri-bodkin-arrow >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1257 | L15176–L15185 | QLOOM @ L15175 | `(defrule     (research-available ri-loom)     (unit-type-count villager >= 9)     (up-timer-status t-relure != timer-running)     (dropsite-min-distance live-boar < max-bh-dista...` | gl-need-vills | t-relure | — | — | research | — | — | **LOST** |
| 1258 | L15187–L15199 | QLOOM @ L15175 | `(defrule     (can-research ri-loom)     (or	(and(game-time > 35)     (housing-headroom < 1))     (or	(goal gl-need-vills LOOM)     (or	(current-age > dark-age)     (and(food-amo...` | gl-need-vills | — | — | — | up-pending-objects | — | — | **LOST** |
| 1259 | L15202–L15209 | QMONKS @ L15201 | `(defrule     (can-train monk)     (unit-type-count-total monk < 3)` | — | — | — | — | train, unit-type-count-total | — | — | **LOST** |
| 1260 | L15211–L15218 | QMONKS @ L15201 | `(defrule     (can-train monk)     (unit-type-count-total monk < 3)` | — | — | — | — | train, unit-type-count-total | — | — | **LOST** |
| 1261 | L15220–L15227 | QMONKS @ L15201 | `(defrule     (can-train monk)     (unit-type-count-total monk < 3)` | — | — | — | — | train, unit-type-count-total | — | — | **LOST** |
| 1262 | L15230–L15238 | QMANGOS @ L15229 | `(defrule     (goal gl-town-safe NO)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1263 | L15240–L15250 | QMANGOS @ L15229 | `(defrule     (false)     (goal gl-town-safe NO)     (up-compare-goal rt >= 10)     (up-compare-goal SUPERIORITY < 10)     (can-train-with-escrow mangonel-line)` | — | — | can-train-with-escrow | — | — | — | — | **LOST** |
| 1264 | L15252–L15260 | QMANGOS @ L15229 | `(defrule     (not(goal SIEGE RAMS))     (can-train mangonel-line)     (goal gl-strategy SIEGE)     (unit-type-count-total scorpion-line >= 5)` | — | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1265 | L15262–L15269 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE 3)     (can-train-with-escrow mangonel-line)` | — | — | can-train-with-escrow | — | up-train | — | ShadowByzantine/12_execution.per#2; ShadowByzantine/16_pass1_transaction.per#10 | **UNKNOWN** |
| 1266 | L15271–L15282 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE 3)     (unit-type-count-total mangonel-line >= 2)` | siege | — | release-escrow, set-escrow-percentage | — | unit-type-count-total | — | — | **LOST** |
| 1267 | L15284–L15292 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE 3)     (up-pending-objects c: mangonel-line < 1)     (up-pending-objects c: battering-ram-line < 1)` | — | — | up-modify-escrow | — | up-pending-objects | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1268 | L15294–L15301 | QMANGOS @ L15229 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1269 | L15303–L15318 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE -1)     (current-age >= castle-age)     (building-type-count siege-workshop > 0)     (up-pending-objects c: mangonel-line < 2)     (unit-typ...` | — | — | — | — | unit-type-count-total, up-pending-objects | — | — | **LOST** |
| 1270 | L15321–L15334 | QSCORPS @ L15320 | `(defrule     (not(goal SIEGE RAMS))     (can-train scorpion-line)     (goal gl-strategy SIEGE)     (or	(unit-type-count-total scorpion-line < 5)     (or	(and(unit-type-count-tot...` | — | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1271 | L15337–L15347 | QRAMS @ L15336 | `(defrule     (goal SIEGE RAMS)     (or	(and(players-building-type-count target-player castle < 1)     (up-compare-goal gl-army-damage-potential < CostOfPausingForRams))     (or	...` | split | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1272 | L15349–L15359 | QRAMS @ L15336 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1273 | L15361–L15368 | QRAMS @ L15336 | `(defrule     (goal SIEGE RAMS)     (up-pending-objects c: mangonel-line < 1)     (up-pending-objects c: battering-ram-line < 1)` | — | — | up-modify-escrow | — | up-pending-objects | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1274 | L15370–L15378 | QRAMS @ L15336 | `(defrule     (goal SIEGE RAMS)     (can-train-with-escrow battering-ram-line)` | — | — | can-train-with-escrow | — | — | — | — | **LOST** |
| 1275 | L15380–L15393 | QRAMS @ L15336 | `(defrule     (goal SIEGE -1)     (current-age >= castle-age)     (building-type-count siege-workshop > 0)     (up-pending-objects c: battering-ram < 2)     (or	(unit-type-count-...` | — | — | — | — | unit-type-count-total, up-pending-objects | — | — | **LOST** |
| 1276 | L15397–L15407 | QSCOUTS @ L15395 | `(defrule     (goal gl-strategy KRUSH)     (can-train scout-cavalry-line)     (unit-type-count scout-cavalry-line < 1)     (or (food-amount >= 100)     (up-pending-objects c: vil...` | — | — | — | — | up-pending-objects | — | — | **LOST** |
| 1277 | L15411–L15419 | QKNIGHTS @ L15409 | `(defrule     (can-train knight-line)     (goal gl-strategy KRUSH)     (or (food-amount >= 100)     (up-pending-objects c: villager >= 2))` | — | — | — | — | up-pending-objects | — | — | **LOST** |
| 1278 | L15422–L15431 | QKNIGHTS @ L15409 | `(defrule     (can-train knight-line)     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause != XBOW)     (up-compare-goal gl-current-build-item != BODKIN)     (u...` | — | — | — | — | — | — | — | **LOST** |
| 1279 | L15433–L15443 | QKNIGHTS @ L15409 | `(defrule     (unit-type-count knight-line < 4)     (goal gl-strategy FLUSH)     (can-train-with-escrow knight-line)     (up-compare-goal gl-progression-pause != XBOW)     (up-co...` | — | — | can-train-with-escrow | — | up-train | — | ShadowByzantine/12_execution.per#2; ShadowByzantine/16_pass1_transaction.per#10 | **UNKNOWN** |
| 1280 | L15446–L15455 | QARCHERS @ L15445 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1281 | L15457–L15470 | QARCHERS @ L15445 | `(defrule     (or	(gold-amount >= 100)     (research-completed ri-fletching))     (up-can-train gl-escrow-state c: archer-line)     (or (unit-type-count-total archer-line < 4)   ...` | — | — | — | — | research, research-completed, research-pending, unit-type-count-total, up-research, up-train | — | — | **LOST** |
| 1282 | L15474–L15478 | QSKIRMS @ L15472 | `(defrule     (current-age >= castle-age)` | gl-escrow-state | — | — | — | — | — | — | **LOST** |
| 1283 | L15480–L15490 | QSKIRMS @ L15472 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1284 | L15492–L15502 | QSKIRMS @ L15472 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1285 | L15504–L15518 | QSKIRMS @ L15472 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1286 | L15520–L15530 | QSKIRMS @ L15472 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < -5)     (or	(up-compare-goal gl-skirm-total < 35)     (up-research-status c: castle-age >= research-pending)))...` | split | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1287 | L15532–L15540 | QSKIRMS @ L15472 | `(defrule     (goal SPLIT 2)` | gl-skirm-total | — | — | — | — | — | — | **LOST** |
| 1288 | L15542–L15547 | QSKIRMS @ L15472 | `(defrule     (true)` | gl-escrow-state, split | — | — | — | — | — | — | **LOST** |
| 1289 | L15550–L15562 | QMILITIAMAN @ L15549 | `(defrule     (goal gl-enemy-civ MESO)     (can-train militiaman-line)     (or	(and(current-age < castle-age)     (research-completed ri-man-at-arms))     (and(current-age > feud...` | — | — | — | — | research, research-completed, train, unit-type-count-total | — | — | **LOST** |
| 1290 | L15566–L15579 | QSPEARS @ L15564 | `(defrule     (goal gl-strategy FLUSH)     (can-train spearman-line)     (current-age-time >= 180)     (current-age < castle-age)     (research-completed ri-fletching)     (unit-...` | — | — | — | — | research, research-completed, unit-type-count-total | — | — | **LOST** |
| 1291 | L15581–L15594 | QSPEARS @ L15564 | `(defrule     (game-time >= 1080)` | — | — | — | — | — | — | — | **LOST** |
| 1292 | L15596–L15609 | QSPEARS @ L15564 | `(defrule     (player-valid 5)` | — | — | — | — | — | — | — | **LOST** |
| 1293 | L15611–L15623 | QSPEARS @ L15564 | `(defrule     (not(player-valid 5))     (goal gl-strategy FLUSH)     (can-train spearman-line)     (current-age >= castle-age)     (unit-type-count-total spearman-line < 10)     ...` | — | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1294 | L15626–L15632 | QSPEARS @ L15564 | `(defrule     (goal gl-strategy KRUSH)` | — | — | — | — | — | — | — | **LOST** |
| 1295 | L15634–L15641 | QSPEARS @ L15564 | `(defrule     (not(player-valid 5))     (goal gl-enemy-civ MESO)     (players-unit-type-count target-player monk < 1)     (players-unit-type-count target-player knight < 1)` | — | — | — | — | — | 2 | — | **LOST** |
| 1296 | L15643–L15655 | QSPEARS @ L15564 | `(defrule     (unit-type-count-total spearman-line < 6)     (up-compare-goal gl-progression-pause != PIKES)     (up-can-train gl-escrow-state c: spearman-line)     (or	(goal ENEM...` | — | — | — | — | unit-type-count-total, up-train | — | ShadowByzantine/12_execution.per#2; ShadowByzantine/16_pass1_transaction.per#10 | **UNKNOWN** |
| 1297 | L15657–L15669 | QSPEARS @ L15564 | `(defrule     (can-train spearman-line)     (up-compare-goal gl-progression-pause != PIKES)     (or	(and(military-population >= 5)     (unit-type-count-total spearman-line < 1)) ...` | — | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1298 | L15671–L15682 | QSPEARS @ L15564 | `(defrule     (can-train spearman-line)     (unit-type-count-total spearman-line < 6)     (up-compare-goal gl-progression-pause != PIKES)     (or	(goal gl-enemy-civ NORMAL)     (...` | — | — | — | — | unit-type-count-total | — | — | **LOST** |
| 1299 | L15686–L15692 | QTOWERS @ L15684 | `(defrule     (or (goal gl-position POCKET)     (or (goal gl-enemy-strategy DRUSH)     (building-type-count-total watch-tower >= 10)))` | — | — | — | — | building-type-count-total | 6 | — | **LOST** |
| 1300 | L15694–L15698 | QTOWERS @ L15684 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1301 | L15700–L15704 | QTOWERS @ L15684 | `(defrule     (goal gl-town-safe NO)` | — | — | — | — | — | — | — | **LOST** |
| 1302 | L15706–L15718 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control -1)     (or (goal gl-position FLANK)     (nand	(current-age-time < 100)     (current-age == feudal-age)))` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | — | **LOST** |
| 1303 | L15720–L15729 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 0)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | — | **LOST** |
| 1304 | L15731–L15740 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 1)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | — | **LOST** |
| 1305 | L15742–L15751 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 2)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | — | **LOST** |
| 1306 | L15753–L15762 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 3)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | — | **LOST** |
| 1307 | L15766–L15770 | QSTABLE @ L15764 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1308 | L15772–L15776 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1309 | L15778–L15783 | QSTABLE @ L15764 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | — | **LOST** |
| 1310 | L15786–L15800 | QSTABLE @ L15764 | `(defrule     (food-amount >= 175)     (gold-amount >= 175)     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (up-pending-obj...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-objects, up-pending-placement | — | — | **LOST** |
| 1311 | L15802–L15808 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1312 | L15810–L15817 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != EXTRA-STABLES)     (up-compare-goal gl-build-progress == KrushExtraStablesNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1313 | L15819–L15828 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item == EXTRA-STABLES)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1314 | L15830–L15837 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (building-type-count-total stable >= 4)     (goal gl-current-build-item EXTRA-STABLES)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1315 | L15839–L15845 | QSTABLE @ L15764 | `(defrule     (up-compare-goal gl-build-progress == KrushFinishedNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1316 | L15848–L15862 | QSTABLE @ L15764 | `(defrule     (food-amount >= 175)     (gold-amount >= 175)     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (up-pending-obj...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-objects, up-pending-placement | — | — | **LOST** |
| 1317 | L15864–L15870 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1318 | L15872–L15879 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != EXTRA-STABLES)     (up-compare-goal gl-build-progress == ExtraStablesNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1319 | L15881–L15890 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == EXTRA-STABLES)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1320 | L15892–L15899 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count-total stable >= 4)     (goal gl-current-build-item EXTRA-STABLES)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1321 | L15901–L15907 | QSTABLE @ L15764 | `(defrule     (up-compare-goal gl-build-progress == FinishedNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1322 | L15910–L15914 | QSTABLE @ L15764 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1323 | L15916–L15920 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1324 | L15922–L15927 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1325 | L15929–L15934 | QSTABLE @ L15764 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | — | **LOST** |
| 1326 | L15937–L15948 | QSTABLE @ L15764 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy KRUSH)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE1)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1327 | L15950–L15957 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1328 | L15959–L15966 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != STABLE1)     (up-compare-goal gl-build-progress == KrushStableNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1329 | L15968–L15978 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1330 | L15980–L15987 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item STABLE1)     (building-type-count-total stable >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1331 | L15990–L16001 | QSTABLE @ L15764 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE1)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1332 | L16003–L16010 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1333 | L16012–L16020 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != STABLE1)     (up-compare-goal gl-build-progress == Stable1Number)` | — | — | — | — | — | — | — | **LOST** |
| 1334 | L16022–L16032 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1335 | L16034–L16040 | QSTABLE @ L15764 | `(defrule     (goal gl-current-build-item STABLE1)     (building-type-count-total stable >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1336 | L16043–L16047 | QSTABLE @ L15764 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1337 | L16049–L16055 | QSTABLE @ L15764 | `(defrule     (or	(goal gl-strategy KRUSH)     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES)))` | goal | — | — | — | — | — | — | **LOST** |
| 1338 | L16057–L16062 | QSTABLE @ L15764 | `(defrule     (not(player-valid 3))     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1339 | L16065–L16077 | QSTABLE @ L15764 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE2)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1340 | L16079–L16085 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1341 | L16087–L16094 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != STABLE2)     (up-compare-goal gl-build-progress == KrushStable2Number)` | — | — | — | — | — | — | — | **LOST** |
| 1342 | L16096–L16106 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE2)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1343 | L16108–L16115 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item STABLE2)     (building-type-count-total stable >= 2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1344 | L16118–L16128 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE2)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1345 | L16130–L16136 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1346 | L16138–L16145 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != STABLE2)     (up-compare-goal gl-build-progress == SecondStableNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1347 | L16147–L16157 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE2)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1348 | L16159–L16166 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item STABLE2)     (building-type-count-total stable >= 2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1349 | L16170–L16174 | QMONASTERY @ L16168 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1350 | L16176–L16180 | QMONASTERY @ L16168 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | — | **LOST** |
| 1351 | L16182–L16193 | QMONASTERY @ L16168 | `(defrule     (goal gl-progression-pause -1)     (can-build-with-escrow monastery)     (up-pending-objects c: monastery < 1)     (goal gl-current-build-item MONASTERY)     (not(u...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-objects, up-pending-placement | — | — | **LOST** |
| 1352 | L16195–L16201 | QMONASTERY @ L16168 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1353 | L16203–L16210 | QMONASTERY @ L16168 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != MONASTERY)     (up-compare-goal gl-build-progress == MonasteryNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1354 | L16212–L16221 | QMONASTERY @ L16168 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == MONASTERY)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1355 | L16223–L16229 | QMONASTERY @ L16168 | `(defrule     (goal gl-current-build-item MONASTERY)     (building-type-count-total monastery >= 1)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1356 | L16233–L16237 | QMARKET @ L16231 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1357 | L16239–L16243 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1358 | L16245–L16249 | QMARKET @ L16231 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | — | **LOST** |
| 1359 | L16252–L16263 | QMARKET @ L16231 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy FLUSH)     (can-build-with-escrow market)     (goal gl-current-build-item MARKET1)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1360 | L16265–L16272 | QMARKET @ L16231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1361 | L16274–L16281 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != MARKET1)     (up-compare-goal gl-build-progress == MarketNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1362 | L16283–L16293 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == MARKET1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1363 | L16295–L16302 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item MARKET1)     (building-type-count-total market >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1364 | L16305–L16309 | QMARKET @ L16231 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1365 | L16311–L16315 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1366 | L16317–L16321 | QMARKET @ L16231 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | — | **LOST** |
| 1367 | L16324–L16334 | QMARKET @ L16231 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy KRUSH)     (can-build-with-escrow market)     (goal gl-current-build-item MARKET1)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1368 | L16336–L16343 | QMARKET @ L16231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1369 | L16345–L16352 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != MARKET1)     (up-compare-goal gl-build-progress == KrushMarketNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1370 | L16354–L16364 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == MARKET1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1371 | L16366–L16373 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item MARKET1)     (building-type-count-total market >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1372 | L16376–L16383 | QMARKET @ L16231 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1373 | L16385–L16398 | QMARKET @ L16231 | `(defrule     (or	(wood-amount < 60)     (or	(food-amount < 60)     (gold-amount < 60)))     (building-type-count-total market < 1)     (up-compare-goal gl-progression-pause == -...` | split | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1374 | L16400–L16406 | QMARKET @ L16231 | `(defrule     (goal SPLIT 1)` | gl-progression-pause, split | — | — | — | — | — | — | **LOST** |
| 1375 | L16408–L16422 | QMARKET @ L16231 | `(defrule     (current-age-time > 60)     (goal gl-strategy FLUSH)     (current-age == feudal-age)     (goal gl-progression-pause -1)     (or	(wood-amount >= 450)     (and(food-a...` | gl-progression-pause | — | — | — | building-type-count-total, research, up-pending-placement | — | — | **LOST** |
| 1376 | L16424–L16438 | QMARKET @ L16231 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1377 | L16440–L16444 | QMARKET @ L16231 | `(defrule     (goal gl-progression-pause MARKET)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1378 | L16446–L16450 | QMARKET @ L16231 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1379 | L16452–L16456 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1380 | L16458–L16462 | QMARKET @ L16231 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | — | **LOST** |
| 1381 | L16464–L16476 | QMARKET @ L16231 | `(defrule     (can-build-with-escrow market)     (goal gl-progression-pause MARKET)     (building-type-count-total market < 1)` | gl-progression-pause, sn-placement-zone-size | t-misc | can-build-with-escrow | — | building-type-count-total, up-build | — | — | **LOST** |
| 1382 | L16479–L16484 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (or (up-compare-goal gl-tenth-turn != 1)     (current-age < feudal-age))` | — | — | — | — | — | 4 | — | **LOST** |
| 1383 | L16487–L16493 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (true)` | gl-archery-in-town, gl-cavalry-in-town, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1384 | L16496–L16505 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (stance-toward focus-player enemy)` | gl-archery-in-town | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1385 | L16507–L16517 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (stance-toward focus-player enemy)` | gl-cavalry-in-town | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1386 | L16520–L16525 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | — | **LOST** |
| 1387 | L16529–L16533 | QRESIGNING @ L16527 | `(defrule     (not(player-valid 3))` | — | — | — | — | — | 2 | — | **LOST** |
| 1388 | L16535–L16547 | QRESIGNING @ L16527 | `(defrule     (civilian-population < 5)     (up-compare-goal CIVSUP < -30)     (up-compare-goal SUPERIORITY < 10)     (up-allied-goal every-ally CIVSUP < -30)     (building-type-...` | — | 5 | — | — | building-type-count-total | — | — | **LOST** |
| 1389 | L16549–L16555 | QRESIGNING @ L16527 | `(defrule     (timer-triggered 5)` | — | 5 | — | — | — | — | — | **LOST** |
| 1390 | L16558–L16562 | QRESIGNING @ L16527 | `(defrule     (player-valid 3)` | — | — | — | — | — | 6 | — | **LOST** |
| 1391 | L16564–L16570 | QRESIGNING @ L16527 | `(defrule     (true)` | goal1 | — | — | — | up-get-fact | — | — | **LOST** |
| 1392 | L16572–L16580 | QRESIGNING @ L16527 | `(defrule     (up-compare-goal goal1 >= 20)` | — | — | — | — | — | — | — | **LOST** |
| 1393 | L16582–L16591 | QRESIGNING @ L16527 | `(defrule     (military-population < 10)` | — | — | — | — | — | — | — | **LOST** |
| 1394 | L16593–L16603 | QRESIGNING @ L16527 | `(defrule     (military-population < 5)` | — | — | — | — | — | — | — | **LOST** |
| 1395 | L16605–L16611 | QRESIGNING @ L16527 | `(defrule     (timer-triggered 5)` | — | 5 | — | — | — | — | — | **LOST** |
| 1396 | L16614–L16622 | QSUPERIORITY @ L16613 | `(defrule     (players-building-count target-player > 0)` | superiority | — | — | — | up-get-fact | — | — | **LOST** |
| 1397 | L16625–L16633 | QCIVSUP @ L16624 | `(defrule     (players-building-count target-player > 0)` | civsup | — | — | — | up-get-fact | — | — | **LOST** |
| 1398 | L16638–L16651 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1399 | L16653–L16667 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1400 | L16670–L16683 | QTSA @ L16636 | `(defrule     (goal gl-attacking NO)     (goal gl-strategy FLUSH)     (players-building-count target-player >= 1)     (or	(up-group-size c: RangedGroup >= 6)     (and(up-group-si...` | sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1401 | L16686–L16696 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1402 | L16698–L16708 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1403 | L16711–L16725 | QTSA @ L16636 | `(defrule     (false)     (goal gl-ninety-turn 1)     (up-group-size c: RangedGroup < 1)     (up-group-size c: KnightGroup < 1)` | — | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | up-target-point | — | — | **LOST** |
| 1404 | L16729–L16734 | QENEMY STRAT @ L16728 | `(defrule     (players-unit-type-count target-player scout-cavalry-line >= 2)` | enemy-stable | — | — | — | — | — | — | **LOST** |
| 1405 | L16737–L16752 | QENEMY STRAT @ L16728 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1406 | L16754–L16764 | QENEMY STRAT @ L16728 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1407 | L16767–L16774 | QENEMY STRAT @ L16728 | `(defrule     (up-compare-goal gl-target-age >= CA-loading)     (players-civilian-population target-player < 33)` | gl-enemy-strategy-type | — | — | — | — | — | — | **LOST** |
| 1408 | L16777–L16784 | QENEMY STRAT @ L16728 | `(defrule     (players-current-age target-player == dark-age)     (players-military-population target-player >= 2)` | — | — | — | — | — | — | — | **LOST** |
| 1409 | L16786–L16794 | QENEMY STRAT @ L16728 | `(defrule     (current-age > dark-age)     (current-age-time >= 210)     (goal gl-enemy-strategy DRUSH)` | — | — | — | — | — | — | — | **LOST** |
| 1410 | L16799–L16804 | QCHAT @ L16797 | `(defrule     (players-military-population any-human-ally >= 30)` | — | — | — | — | — | — | — | **LOST** |
| 1411 | L16807–L16812 | QCHAT @ L16797 | `(defrule     (players-building-type-count any-human-ally monastery >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 1412 | L16815–L16821 | QCHAT @ L16797 | `(defrule     (research-completed ri-cartography)` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 1413 | L16824–L16831 | QCHAT @ L16797 | `(defrule     (current-age < imperial-age)     (players-current-age any-enemy == imperial-age)` | — | — | — | — | — | — | — | **LOST** |
| 1414 | L16834–L16841 | QCHAT @ L16797 | `(defrule     (current-age == dark-age)     (players-military-population any-human-enemy >= 5)` | — | — | — | — | — | — | — | **LOST** |
| 1415 | L16844–L16849 | QCHAT @ L16797 | `(defrule     (game-time > 2500)` | — | — | — | — | — | — | — | **LOST** |
| 1416 | L16853–L16862 | QSTRATEGY @ L16851 | `(defrule     (true)` | gl-enemy-strategy, gl-enemy-strategy-type, gl-strategy, gl-strategy-type | — | — | — | — | — | — | **LOST** |
| 1417 | L16866–L16877 | QSTRATEGY @ L16851 | `(defrule     (player-valid 3)     (game-time >= 5)     (not(player-in-game any-ally))     (up-compare-goal gl-strategy != KRUSH)` | sn-home-exploration-time | — | — | — | — | — | — | **LOST** |
| 1418 | L16880–L16887 | QSTRATEGY @ L16851 | `(defrule     (game-time > 10)     (current-age == dark-age)     (up-compare-goal gl-strategy != KRUSH)` | — | — | — | — | — | — | — | **LOST** |
| 1419 | L16889–L16905 | QSTRATEGY @ L16851 | `(defrule     (game-time > 5)     (game-time < 60)     (current-age == dark-age)     (up-compare-goal gl-strategy != KRUSH)     (or	(taunt-detected me 131)     (or	(taunt-detecte...` | gl-strategy, gl-strategy-type, sn-home-exploration-time | — | — | — | — | — | — | **LOST** |
| 1420 | L16910–L16919 | QSTRATEGY @ L16851 | `(defrule     (game-time > 3)     (game-time < 30)` | gl-position, gl-strategy, gl-strategy-type, sn-home-exploration-time | — | — | — | — | — | — | **LOST** |
| 1421 | L16923–L16939 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 105)` | split | — | — | — | — | — | — | **LOST** |
| 1422 | L16941–L16961 | QECO NUMBERS @ L16922 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1423 | L16964–L16969 | QECO NUMBERS @ L16922 | `(defrule     (true)` | sn-mining-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 1424 | L16971–L16976 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 2)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/04_construction.per#3 | **UNKNOWN** |
| 1425 | L16978–L16983 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 3)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/04_construction.per#3 | **UNKNOWN** |
| 1426 | L16985–L16990 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 5)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/04_construction.per#3 | **UNKNOWN** |
| 1427 | L16992–L16997 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 8)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/04_construction.per#3 | **UNKNOWN** |
| 1428 | L17000–L17008 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-town-safe NO)` | — | — | — | — | — | — | — | **LOST** |
| 1429 | L17010–L17020 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 5)` | — | — | — | — | — | — | — | **LOST** |
| 1430 | L17026–L17035 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-dark-build -1)     (or (current-age >= feudal-age)     (and(game-time > 80)     (up-compare-goal gl-current-sheep-count >= 6)))` | gl-dark-build | — | — | — | — | — | — | **LOST** |
| 1431 | L17037–L17046 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 50)     (wood-amount >= 200)     (goal gl-dark-build MillFirst)     (building-type-count-total mill < 1)` | gl-dark-build | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1432 | L17048–L17054 | QECO NUMBERS @ L16922 | `(defrule     (true)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 1433 | L17056–L17066 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 37)     (goal gl-dark-build -1)     (not(up-find-remote c: sheep c: 1))     (up-compare-goal gl-current-sheep-count < 1)` | gl-dark-build | — | — | up-find-remote | — | — | — | **LOST** |
| 1434 | L17068–L17079 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-dark-build -1)     (not(up-find-remote c: sheep c: 1))     (or	(and(game-time > 80)     (unit-type-count sheep < 1))     (and(game-time > 120)     (up-comp...` | gl-dark-build | — | — | up-find-remote | — | — | — | **LOST** |
| 1435 | L17082–L17088 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 93)     (goal gl-second-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1436 | L17090–L17095 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 94)` | — | — | — | — | — | — | — | **LOST** |
| 1437 | L17098–L17102 | QECO NUMBERS @ L16922 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 1438 | L17104–L17116 | QECO NUMBERS @ L16922 | `(defrule     (true)` | gl-build-progress, sn-initial-exploration-required, sn-percent-exploration-required, sn-safe-town-size | — | — | — | — | — | — | **LOST** |
| 1439 | L17119–L17127 | QECO NUMBERS @ L16922 | `(defrule     (true)` | gl-vills-under-tc, goal | — | — | — | up-get-fact | — | — | **LOST** |
| 1440 | L17129–L17134 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 87)` | — | — | — | — | — | — | — | **LOST** |
| 1441 | L17138–L17143 | QECO NUMBERS @ L16922 | `(defrule     (current-age == castle-age)` | sn-preferred-mill-placement | — | — | — | — | — | — | **LOST** |
| 1442 | L17146–L17152 | QECO NUMBERS @ L16922 | `(defrule     (true)` | sn-cap-civilian-explorers, sn-percent-civilian-explorers | — | — | — | — | — | — | **LOST** |
| 1443 | L17154–L17159 | QECO NUMBERS @ L16922 | `(defrule     (unit-type-count villager > 6)` | gl-early-gar | — | — | — | — | — | — | **LOST** |
| 1444 | L17161–L17178 | QECO NUMBERS @ L16922 | `(defrule     (game-time < 50)` | goal | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1445 | L17180–L17189 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 7)     (game-time < 50)     (goal gl-early-gar -1)     (current-age == dark-age)     (or (game-time > 30)     (up-compare-goal goal > 0))` | split | — | — | — | — | — | — | **LOST** |
| 1446 | L17191–L17205 | QECO NUMBERS @ L16922 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1447 | L17207–L17222 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-early-gar 0)     (current-age == dark-age)     (timer-triggered t-relure)` | — | t-relure | — | — | — | — | — | **LOST** |
| 1448 | L17224–L17239 | QECO NUMBERS @ L16922 | `(defrule     (true)` | gl-age-loading, gl-getting-sheep, gl-need-vills, sn-cap-civilian-builders, sn-enable-training-queue, sn-livestock-to-town-center, sn-maximum-gaia-attack-response, sn-percent-civilian-builders, sn-percent-civilian-gatherers, sn-preferred-mill-placement, sn-zero-priority-distance | — | — | — | — | — | — | **LOST** |
| 1449 | L17241–L17247 | QECO NUMBERS @ L16922 | `(defrule     (unit-type-count villager >= 37)` | sn-enable-training-queue | — | — | — | — | — | — | **LOST** |
| 1450 | L17249–L17255 | QUEUE @ L17245 | `(defrule     (current-age >= feudal-age)     (goal gl-strategy FLUSH)` | sn-enable-training-queue | — | — | — | — | — | — | **LOST** |
| 1451 | L17257–L17262 | QUEUE @ L17245 | `(defrule     (building-type-count mill > 0)` | sn-preferred-mill-placement | — | — | — | — | — | — | **LOST** |
| 1452 | L17265–L17269 | QUEUE @ L17245 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1453 | L17272–L17280 | QUEUE @ L17245 | `(defrule     (or (taunt-detected me 14)     (taunt-detected any-enemy 14))` | — | — | — | — | — | — | — | **LOST** |
| 1454 | L17283–L17298 | QUEUE @ L17245 | `(defrule     (true)` | gl-boar-unit, sn-allow-adjacent-dropsites, sn-disable-builder-assistance, sn-dropsite-separation-distance, sn-enable-new-building-system, sn-forage-defend-priority, sn-gold-defend-priority, sn-intelligent-gathering, sn-livestock-defend-priority, sn-stone-defend-priority, sn-use-by-type-max-gathering | — | — | — | — | — | — | **LOST** |
| 1455 | L17300–L17305 | QUEUE @ L17245 | `(defrule     (cc-players-unit-type-count 0 javelina > 0)` | gl-boar-unit | — | — | — | — | — | — | **LOST** |
| 1456 | L17308–L17323 | QUEUE @ L17245 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1457 | L17325–L17331 | QUEUE @ L17245 | `(defrule     (game-time > 30)` | sn-food-dropsite-distance, sn-maximum-food-drop-distance | — | — | — | — | — | — | **LOST** |
| 1458 | L17333–L17339 | QUEUE @ L17245 | `(defrule     (building-type-count farm > 7)` | sn-food-dropsite-distance, sn-maximum-food-drop-distance | — | — | — | — | — | — | **LOST** |
| 1459 | L17342–L17348 | QUEUE @ L17245 | `(defrule     (game-time > 4000)` | sn-maximum-hunt-drop-distance | — | — | — | — | — | — | **LOST** |
| 1460 | L17350–L17364 | QUEUE @ L17245 | `(defrule     (true)` | sn-cap-civilian-builders, sn-gold-dropsite-distance, sn-maximum-gold-drop-distance, sn-maximum-stone-drop-distance, sn-maximum-wood-drop-distance, sn-minimum-boar-hunt-group-size, sn-required-forest-tiles, sn-retask-gather-amount, sn-stone-dropsite-distance, sn-wood-dropsite-distance | — | — | — | — | — | — | **LOST** |
| 1461 | L17366–L17372 | QUEUE @ L17245 | `(defrule     (game-time > 500)` | sn-maximum-wood-drop-distance, sn-wood-dropsite-distance | — | — | — | — | — | — | **LOST** |
| 1462 | L17374–L17381 | QUEUE @ L17245 | `(defrule     (current-age == feudal-age)     (strategic-number sn-stone-gatherer-percentage != 0)` | sn-dropsite-separation-distance, sn-maximum-stone-drop-distance | — | — | — | — | — | — | **LOST** |
| 1463 | L17383–L17391 | QUEUE @ L17245 | `(defrule     (current-age-time > 200)     (current-age == feudal-age)     (strategic-number sn-stone-gatherer-percentage == 0)     (strategic-number sn-maximum-stone-drop-distan...` | sn-maximum-stone-drop-distance | — | — | — | — | — | — | **LOST** |
| 1464 | L17394–L17399 | QBECO @ L17393 | `(defrule     (goal gl-strategy KRUSH)     (current-age < castle-age)` | — | — | — | — | — | 15 | — | **LOST** |
| 1465 | L17401–L17408 | QBECO @ L17393 | `(defrule     (or	(current-age-time < 120)     (and(up-compare-goal gl-town-safe != YES)     (and(up-compare-goal gl-threat-time < 10000)     (up-compare-goal gl-threat-target ==...` | — | — | — | — | — | 14 | — | **LOST** |
| 1466 | L17410–L17415 | QBECO @ L17393 | `(defrule     (or	(current-age < feudal-age)     (up-timer-status BECO-TIMER == timer-running))` | — | beco-timer | — | — | — | 13 | — | **LOST** |
| 1467 | L17417–L17421 | QBECO @ L17393 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 1468 | L17424–L17433 | QBECO @ L17393 | `(defrule     (false)     (goal gl-fifty-turn 1)     (or	(up-compare-goal NET-WOOD-AMOUNT > 200)     (or	(up-compare-goal NET-FOOD-AMOUNT > 200)     (or	(up-compare-goal NET-GOLD...` | — | — | — | — | — | — | — | **LOST** |
| 1469 | L17436–L17448 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal gl-strategy != KRUSH)     (up-compare-goal NET-WOOD-AMOUNT < 100)     (up-compare-goal NET-FOOD-AMOUNT >= 250)` | sn-food-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | — | **LOST** |
| 1470 | L17450–L17462 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal gl-strategy != KRUSH)     (up-compare-goal NET-WOOD-AMOUNT < 150)     (up-compare-goal NET-FOOD-AMOUNT >= 400)` | sn-food-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | — | **LOST** |
| 1471 | L17464–L17476 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal gl-strategy != KRUSH)     (up-compare-goal NET-WOOD-AMOUNT < 300)     (up-compare-goal NET-FOOD-AMOUNT >= 800)` | — | — | — | — | — | — | — | **LOST** |
| 1472 | L17479–L17493 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (gold-amount > 200)     (food-amount < 600)     (or	(research-available castle-age)     (goal gl-current-build-item CUP))     (up-compare-sn sn-g...` | — | — | — | — | research | — | — | **LOST** |
| 1473 | L17495–L17508 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal NET-FOOD-AMOUNT < 100)     (up-compare-goal NET-GOLD-AMOUNT >= 300)     (up-compare-sn sn-gold-gatherer-percentage >= 2)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1474 | L17510–L17522 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal NET-FOOD-AMOUNT < 100)     (up-compare-goal NET-WOOD-AMOUNT >= 300)     (up-compare-sn sn-wood-gatherer-percentage >= 4)` | sn-food-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | — | **LOST** |
| 1475 | L17525–L17539 | QBECO @ L17393 | `(defrule     (false)     (goal SPLIT 0)     (goal gl-current-build-item CUP)     (unit-type-count villager-gold < 1)     (up-compare-sn sn-gold-gatherer-percentage < 2)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | — | **LOST** |
| 1476 | L17541–L17551 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (or	(and(gold-amount < 100)     (food-amount >= 500))     (and(gold-amount < 160)     (food-amount >= 700)))     (research-available castle-age) ...` | split | — | — | — | research | — | — | **LOST** |
| 1477 | L17553–L17564 | QBECO @ L17393 | `(defrule     (goal SPLIT 2)` | — | — | — | — | — | — | — | **LOST** |
| 1478 | L17566–L17581 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (game-time < 2400)` | — | — | — | — | — | — | — | **LOST** |
| 1479 | L17583–L17597 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (game-time < 2400)` | — | — | — | — | — | — | — | **LOST** |
| 1480 | L17599–L17607 | QBECO @ L17393 | `(defrule     (true)` | goal, split | — | — | — | — | — | — | **LOST** |
| 1481 | L17609–L17614 | QBECO @ L17393 | `(defrule     (up-compare-goal goal > 100)` | sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1482 | L17616–L17621 | QBECO @ L17393 | `(defrule     (up-compare-goal goal < 100)` | sn-wood-gatherer-percentage | — | — | — | — | — | — | **LOST** |
| 1483 | L17623–L17633 | QBECO @ L17393 | `(defrule     (or	(taunt-detected me 13)     (taunt-detected any-enemy 13))` | — | — | — | — | — | — | — | **LOST** |
| 1484 | L17637–L17643 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-town-safe, gl-town-under-attack | — | — | — | — | — | — | **LOST** |
| 1485 | L17647–L17653 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-enemies-in-town, goal, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1486 | L17656–L17666 | QTOWN SAFETY @ L17636 | `(defrule     (stance-toward focus-player enemy)` | gl-enemies-in-town | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1487 | L17669–L17674 | QTOWN SAFETY @ L17636 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 1488 | L17678–L17682 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1489 | L17685–L17693 | QTOWN SAFETY @ L17636 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1490 | L17696–L17702 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt < 2)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 1491 | L17704–L17712 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt >= 2)     (goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe == YES)` | — | — | — | — | — | — | — | **LOST** |
| 1492 | L17714–L17722 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt < 1)     (goal gl-town-safe BeingDrushed)     (up-compare-goal gl-enemies-in-town < 2)     (up-timer-status t-town-safe != timer-running)` | — | t-town-safe | — | — | — | — | — | **LOST** |
| 1493 | L17725–L17732 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal gl-town-safe == YES)     (up-compare-goal gl-enemies-in-town >= 2)` | — | — | — | — | — | — | — | **LOST** |
| 1494 | L17734–L17739 | QTOWN SAFETY @ L17636 | `(defrule     (goal gl-town-safe NO)     (up-compare-goal gl-enemies-in-town >= 2)` | — | t-town-safe | — | — | — | — | — | **LOST** |
| 1495 | L17741–L17749 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal gl-town-safe != YES)     (up-compare-goal gl-enemies-in-town < 1)     (up-timer-status t-town-safe != timer-running)` | — | t-town-safe | — | — | — | — | — | **LOST** |
| 1496 | L17753–L17758 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1497 | L17761–L17769 | QTOWN SAFETY @ L17636 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | — | **LOST** |
| 1498 | L17772–L17778 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 1499 | L17780–L17790 | QTOWN SAFETY @ L17636 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1500 | L17792–L17802 | QTOWN SAFETY @ L17636 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1501 | L17805–L17818 | QTOWN SAFETY @ L17636 | `(defrule     (current-age >= dark-age)` | sn-home-exploration-time, sn-maximum-explore-group-size, sn-percentage-explore-exterminators | — | — | — | — | — | — | **LOST** |
| 1502 | L17820–L17825 | QTOWN SAFETY @ L17636 | `(defrule     (current-age >= feudal-age)` | sn-home-exploration-time | — | — | — | — | — | — | **LOST** |
| 1503 | L17827–L17831 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-enemy-civ | — | — | — | — | — | — | **LOST** |
| 1504 | L17833–L17841 | QTOWN SAFETY @ L17636 | `(defrule     (false)     (not (player-valid 3))     (or (players-civ target-player incan)     (or (players-civ target-player aztec)     (players-civ target-player mayan)))` | gl-enemy-civ | — | — | — | — | — | — | **LOST** |
| 1505 | L17843–L17849 | QTOWN SAFETY @ L17636 | `(defrule     (or (players-civ every-enemy incan)     (or (players-civ every-enemy aztec)     (players-civ every-enemy mayan)))` | gl-enemy-civ | — | — | — | — | — | — | **LOST** |
| 1506 | L17851–L17857 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-escrow-state, sn-enable-patrol-attack | — | — | — | — | — | — | **LOST** |
| 1507 | L17859–L17865 | QTOWN SAFETY @ L17636 | `(defrule     (goal gl-attacking YES)` | sn-number-attack-groups, sn-percent-attack-soldiers | — | — | — | — | — | — | **LOST** |
| 1508 | L17867–L17880 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-allow-civilian-offense, sn-disable-attack-groups, sn-enable-offensive-priority, sn-focus-player-number, sn-ignore-tower-elevation, sn-number-attack-groups, sn-number-civilian-militia, sn-percent-building-cancellation | — | — | — | — | — | — | **LOST** |
| 1509 | L17882–L17901 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-do-not-scale-for-difficulty-level, sn-enemy-sighted-response-distance, sn-number-forward-builders, sn-percent-attack-soldiers, sn-percent-enemy-sighted-response | — | — | — | — | — | — | **LOST** |
| 1510 | L17903–L17907 | QTOWN SAFETY @ L17636 | `(defrule     (up-group-size c: RangedGroup > 0)` | — | — | — | — | — | — | — | **LOST** |
| 1511 | L17909–L17913 | QTOWN SAFETY @ L17636 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | — | — | **LOST** |
| 1512 | L17915–L17929 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-relic-return-distance | — | — | — | — | — | — | **LOST** |
| 1513 | L17931–L17943 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-special-attack-influence1, sn-special-attack-type1, sn-target-evaluation-boat, sn-target-evaluation-continent, sn-target-evaluation-distance, sn-target-evaluation-in-progress, sn-target-evaluation-kills, sn-target-evaluation-siege-weapon | — | — | — | — | — | — | **LOST** |
| 1514 | L17948–L17956 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-fifth-turn 1)     (goal gl-position POCKET)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1515 | L17959–L17965 | QTARGET PLAYER @ L17945 | `(defrule     (or	(game-time < 5)     (or (game-time > 10)     (not(player-valid 5))))` | — | — | — | — | — | 4 | — | **LOST** |
| 1516 | L17968–L17974 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search | — | — | — | **LOST** |
| 1517 | L17977–L17982 | QTARGET PLAYER @ L17945 | `(defrule     (not(stance-toward focus-player enemy))     (up-allied-goal focus-player gl-position != POCKET)` | — | — | — | up-find-remote | — | — | — | **LOST** |
| 1518 | L17985–L17990 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | — | **LOST** |
| 1519 | L17992–L18006 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | sn-focus-player-number | — | — | up-clean-search, up-set-target-object, up-set-target-point | up-get-object-data | — | — | **LOST** |
| 1520 | L18010–L18017 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 122)` | sn-target-player-number | — | — | — | — | — | — | **LOST** |
| 1521 | L18020–L18028 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 123)` | sn-target-player-number | — | — | — | — | — | — | **LOST** |
| 1522 | L18031–L18040 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 124)` | sn-target-player-number | — | — | — | — | — | — | **LOST** |
| 1523 | L18043–L18053 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 125)` | sn-target-player-number | — | — | — | — | — | — | **LOST** |
| 1524 | L18056–L18066 | QTARGET PLAYER @ L17945 | `(defrule     (or	(taunt-detected me 22)     (or	(taunt-detected any-ally 22)     (taunt-detected any-enemy 22)))` | — | — | — | — | — | — | — | **LOST** |
| 1525 | L18071–L18080 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time < 1020)` | — | — | — | — | — | — | — | **LOST** |
| 1526 | L18088–L18100 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target -1)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(no...` | — | — | — | — | — | — | — | **LOST** |
| 1527 | L18102–L18108 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1528 | L18111–L18123 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 1)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(not...` | — | — | — | — | — | — | — | **LOST** |
| 1529 | L18125–L18132 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1530 | L18135–L18147 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 3)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(not...` | — | — | — | — | — | — | — | **LOST** |
| 1531 | L18149–L18157 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1532 | L18160–L18172 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 5)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(not...` | — | — | — | — | — | — | — | **LOST** |
| 1533 | L18174–L18183 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1534 | L18186–L18197 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time >= 1200)     (goal gl-strategy KRUSH)     (not(player-in-game any-ally))     (player-in-game target-player)     (up-compare-goal gl-...` | — | — | — | — | — | — | — | **LOST** |
| 1535 | L18201–L18211 | QTARGET PLAYER @ L17945 | `(defrule     (false)     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target -1)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | — | **LOST** |
| 1536 | L18213–L18219 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1537 | L18222–L18232 | QTARGET PLAYER @ L17945 | `(defrule     (false)     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 1)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | — | **LOST** |
| 1538 | L18234–L18241 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1539 | L18244–L18253 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 3)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | — | **LOST** |
| 1540 | L18255–L18263 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1541 | L18266–L18275 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 5)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | — | **LOST** |
| 1542 | L18277–L18286 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1543 | L18289–L18298 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (player-in-game target-player)     (up-compare-goal gl-find-new-target != -1)     (players-civilian-population tar...` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1544 | L18302–L18314 | QTARGET PLAYER @ L17945 | `(defrule     (false)     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target -1)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target...` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1545 | L18316–L18322 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1546 | L18325–L18333 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 1)     (players-current-age target-player < castle-age)` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1547 | L18335–L18346 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 1)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target-player))    ...` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1548 | L18348–L18355 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1549 | L18358–L18366 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 3)     (players-current-age target-player < castle-age)` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1550 | L18368–L18379 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 3)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target-player))    ...` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1551 | L18381–L18389 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1552 | L18392–L18403 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 5)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target-player))    ...` | gl-find-new-target | — | — | — | — | — | — | **LOST** |
| 1553 | L18405–L18414 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1554 | L18417–L18427 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time >= 1200)     (goal gl-strategy KRUSH)     (player-in-game target-player)     (up-compare-goal gl-find-new-target != -1)` | — | — | — | — | — | — | — | **LOST** |
| 1555 | L18432–L18436 | QTARGET PLAYER @ L17945 | `(defrule     (up-compare-goal gl-privileged-player == my-player-number)` | — | — | — | — | — | 19 | — | **LOST** |
| 1556 | L18439–L18447 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1557 | L18449–L18460 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1558 | L18462–L18470 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1559 | L18472–L18478 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1560 | L18481–L18489 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1561 | L18491–L18500 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 1)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | — | **LOST** |
| 1562 | L18502–L18513 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1563 | L18515–L18522 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1564 | L18524–L18531 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1565 | L18534–L18542 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1566 | L18544–L18553 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 3)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | — | **LOST** |
| 1567 | L18555–L18566 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1568 | L18568–L18575 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1569 | L18577–L18585 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1570 | L18588–L18596 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1571 | L18598–L18609 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1572 | L18611–L18618 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1573 | L18620–L18629 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1574 | L18632–L18641 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1575 | L18644–L18648 | QTARGET PLAYER @ L17945 | `(defrule     (up-compare-goal gl-privileged-player != my-player-number)` | — | — | — | — | — | 15 | — | **LOST** |
| 1576 | L18651–L18659 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1577 | L18661–L18672 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1578 | L18674–L18681 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1579 | L18683–L18689 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1580 | L18692–L18700 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1581 | L18702–L18711 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 1)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | — | **LOST** |
| 1582 | L18713–L18724 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1583 | L18726–L18733 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1584 | L18735–L18742 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1585 | L18745–L18753 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1586 | L18755–L18764 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 3)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | — | **LOST** |
| 1587 | L18766–L18777 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1588 | L18779–L18786 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1589 | L18788–L18796 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1590 | L18799–L18807 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1591 | L18809–L18820 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1592 | L18822–L18829 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | — | **LOST** |
| 1593 | L18831–L18840 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1594 | L18843–L18852 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | — | **LOST** |
| 1595 | L18855–L18868 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 1200)` | — | — | — | — | — | — | — | **LOST** |
| 1596 | L18870–L18880 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number, sn-target-player-number, split | t-target-switch | — | — | — | — | — | **LOST** |
| 1597 | L18882–L18887 | QTARGET PLAYER @ L17945 | `(defrule     (game-time < 30)     (up-compare-goal gl-last-target-player s:!= sn-target-player-number)` | gl-last-target-player | — | — | — | — | — | — | **LOST** |
| 1598 | L18889–L18897 | QTARGET PLAYER @ L17945 | `(defrule     (game-time >= 30)     (up-compare-goal gl-last-target-player s:!= sn-target-player-number)` | gl-last-target-player | — | — | — | — | — | — | **LOST** |
| 1599 | L18900–L18906 | QTARGET PLAYER @ L17945 | `(defrule     (player-number 1)     (not(player-valid 3))` | sn-target-player-number | — | — | — | — | — | — | **LOST** |
| 1600 | L18908–L18914 | QTARGET PLAYER @ L17945 | `(defrule     (player-number 2)     (not(player-valid 3))` | sn-target-player-number | — | — | — | — | — | — | **LOST** |
| 1601 | L18916–L18920 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1602 | L18923–L18931 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1603 | L18934–L18939 | QPRIORITY @ L18933 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1604 | L18941–L18952 | QPRIORITY @ L18933 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1605 | L18956–L18968 | QPRIORITY @ L18933 | `(defrule     (goal gl-strategy FLUSH)     (unit-type-count knight >= 3)     (up-compare-goal SUPERIORITY >= 30)` | — | — | — | — | — | — | — | **LOST** |
| 1606 | L18970–L18982 | QPRIORITY @ L18933 | `(defrule     (goal gl-strategy FLUSH)     (or	(unit-type-count knight < 3)     (up-compare-goal SUPERIORITY < 30))` | — | — | — | — | — | — | — | **LOST** |
| 1607 | L18985–L18998 | QPRIORITY @ L18933 | `(defrule     (game-time < 1800)` | — | — | — | — | — | — | — | **LOST** |
| 1608 | L19000–L19013 | QPRIORITY @ L18933 | `(defrule     (goal gl-strategy KRUSH)     (or	(game-time >= 1800)` | — | — | — | — | — | — | — | **LOST** |
| 1609 | L19015–L19021 | QPRIORITY @ L18933 | `(defrule     (players-building-count target-player > 10)` | goal | — | — | — | — | — | — | **LOST** |
| 1610 | L19023–L19030 | QPRIORITY @ L18933 | `(defrule     (goal gl-attacking YES)     (goal gl-strategy KRUSH)     (taunt-detected any-ally 102)` | — | — | — | — | — | — | — | **LOST** |
| 1611 | L19033–L19039 | QSCOUTING @ L19032 | `(defrule     (game-time >= 50)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | — | **LOST** |
| 1612 | L19041–L19049 | QSCOUTING @ L19032 | `(defrule     (game-time >= 1500)` | — | — | — | — | — | — | — | **LOST** |
| 1613 | L19051–L19058 | QSCOUTING @ L19032 | `(defrule     (false)     (players-building-count target-player >= 1)` | — | — | — | — | — | — | — | **LOST** |
| 1614 | L19060–L19069 | QSCOUTING @ L19032 | `(defrule     (game-time < 1100)     (timer-triggered t-scout-enemy)     (players-building-count any-enemy > 0)     (strategic-number sn-total-number-explorers > 0)` | — | t-scout-enemy | — | — | — | — | — | **LOST** |
| 1615 | L19071–L19081 | QSCOUTING @ L19032 | `(defrule     (false)     (game-time >= 1100)     (timer-triggered t-scout-enemy)     (players-building-count any-enemy > 0)     (strategic-number sn-total-number-explorers > 0)` | — | t-scout-enemy | — | — | — | — | — | **LOST** |
| 1616 | L19084–L19089 | QATTACK EFFICIENCY @ L19083 | `(defrule     (false)     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 20 | — | **LOST** |
| 1617 | L19091–L19100 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | gl-attack-efficiency, goal, goal1, goal2, goal3, goal4 | — | — | — | — | — | — | **LOST** |
| 1618 | L19103–L19110 | QATTACK EFFICIENCY @ L19083 | `(defrule     (false)` | gl-attack-efficiency | — | — | — | up-get-fact | — | — | **LOST** |
| 1619 | L19113–L19117 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1620 | L19119–L19123 | QATTACK EFFICIENCY @ L19083 | `(defrule     (players-unit-type-count target-player battering-ram-line >= 2)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1621 | L19125–L19134 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1622 | L19136–L19140 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1623 | L19142–L19146 | QATTACK EFFICIENCY @ L19083 | `(defrule     (players-unit-type-count target-player battering-ram-line >= 1)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1624 | L19148–L19157 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1625 | L19159–L19163 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1626 | L19165–L19169 | QATTACK EFFICIENCY @ L19083 | `(defrule     (players-unit-type-count target-player battering-ram-line >= 2)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1627 | L19171–L19180 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1628 | L19182–L19186 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1629 | L19188–L19192 | QATTACK EFFICIENCY @ L19083 | `(defrule     (unit-type-count battering-ram-line >= 2)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1630 | L19195–L19199 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1631 | L19202–L19211 | QATTACK EFFICIENCY @ L19083 | `(defrule     (stance-toward focus-player enemy)` | gl-attack-efficiency, goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 1632 | L19213–L19217 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1633 | L19219–L19223 | QATTACK EFFICIENCY @ L19083 | `(defrule     (unit-type-count battering-ram-line >= 1)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1634 | L19226–L19230 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1635 | L19233–L19242 | QATTACK EFFICIENCY @ L19083 | `(defrule     (stance-toward focus-player enemy)` | gl-attack-efficiency, goal3 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | — | **LOST** |
| 1636 | L19244–L19248 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1637 | L19250–L19254 | QATTACK EFFICIENCY @ L19083 | `(defrule     (unit-type-count battering-ram-line >= 2)` | goal8 | — | — | — | — | — | — | **LOST** |
| 1638 | L19257–L19261 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | — | **LOST** |
| 1639 | L19264–L19273 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1640 | L19276–L19290 | QATTACK EFFICIENCY @ L19083 | `(defrule     (taunt-detected me 91)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | — | **LOST** |
| 1641 | L19292–L19297 | QATTACK EFFICIENCY @ L19083 | `(defrule     (taunt-detected me 92)` | — | — | — | — | — | — | — | **LOST** |
| 1642 | L19300–L19315 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (true)` | gl-army-damage-potential | — | — | — | up-get-fact | — | — | **LOST** |
| 1643 | L19318–L19326 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1644 | L19328–L19337 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (true)` | gl-army-damage-potential, goal | — | — | — | — | — | — | **LOST** |
| 1645 | L19340–L19349 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (false)     (players-current-age target-player < castle-age)     (or	(and(goal gl-enemy-strategy-type FC)     (military-population > 6))     (and(military-populatio...` | gl-army-damage-potential | — | — | — | — | — | — | **LOST** |
| 1646 | L19352–L19361 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (current-age == castle-age)     (up-compare-goal UP-FIRST != -1)     (or (current-age-time >= 30)     (players-current-age target-player == castle-age))` | — | — | — | — | — | — | — | **LOST** |
| 1647 | L19363–L19372 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (up-compare-goal UP-FIRST != -1)     (or (players-current-age-time target-player >= 30)     (current-age == castle-age))     (players-current-age target-player == c...` | — | — | — | — | — | — | — | **LOST** |
| 1648 | L19374–L19381 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (up-compare-goal gl-target-age < CA-loading)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1649 | L19383–L19387 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (goal UP-FIRST 1)` | gl-army-damage-potential | — | — | — | — | — | — | **LOST** |
| 1650 | L19389–L19397 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (goal UP-FIRST -1)     (up-compare-goal gl-target-age == CA-loading)     (up-research-status c: castle-age < research-pending)` | up-first | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1651 | L19399–L19403 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (goal UP-FIRST 0)` | gl-army-damage-potential | — | — | — | — | — | — | **LOST** |
| 1652 | L19405–L19410 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (current-age-time >= 30)     (current-age >= castle-age)` | gl-army-damage-potential | — | — | — | — | — | — | **LOST** |
| 1653 | L19412–L19417 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (players-current-age-time target-player >= 30)     (players-current-age target-player >= castle-age)` | gl-army-damage-potential | — | — | — | — | — | — | **LOST** |
| 1654 | L19420–L19424 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (research-completed ri-elite-skirmisher)` | gl-army-damage-potential | — | — | — | research, research-completed | — | — | **LOST** |
| 1655 | L19426–L19430 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (research-completed ri-leather-archer-armor)` | gl-army-damage-potential | — | — | — | research, research-completed | — | — | **LOST** |
| 1656 | L19432–L19436 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (research-completed ri-chain-barding)` | gl-army-damage-potential | — | — | — | research, research-completed | — | — | **LOST** |
| 1657 | L19438–L19443 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (unit-type-count battering-ram-line >= 2)     (up-compare-goal gl-army-damage-potential >= CostOfPausingForRams)` | gl-army-damage-potential | — | — | — | — | — | — | **LOST** |
| 1658 | L19446–L19452 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (taunt-detected me 67)     (current-age >= feudal-age)` | — | — | — | — | — | — | — | **LOST** |
| 1659 | L19454–L19459 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (taunt-detected me 68)` | — | — | — | — | — | — | — | **LOST** |
| 1660 | L19464–L19477 | Q2BA @ L19462 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item 2BA)     (can-research-with-escrow ri-double-bit-axe)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1661 | L19479–L19485 | Q2BA @ L19462 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1662 | L19487–L19495 | Q2BA @ L19462 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != 2BA)     (up-compare-goal gl-build-progress == Krush2BANumber)` | — | — | — | — | — | — | — | **LOST** |
| 1663 | L19497–L19504 | Q2BA @ L19462 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item 2BA)     (up-research-status c: ri-double-bit-axe >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1664 | L19507–L19520 | Q2BA @ L19462 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item 2BA)     (can-research-with-escrow ri-double-bit-axe)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1665 | L19522–L19528 | Q2BA @ L19462 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1666 | L19530–L19538 | Q2BA @ L19462 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != 2BA)     (up-compare-goal gl-build-progress == DoubleBitAxeNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1667 | L19540–L19547 | Q2BA @ L19462 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item 2BA)     (up-research-status c: ri-double-bit-axe >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1668 | L19551–L19560 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item BOWSAW)     (can-research-with-escrow ri-bow-saw)     (unit-type-count-t...` | — | — | can-research-with-escrow | — | unit-type-count-total, up-research | — | — | **LOST** |
| 1669 | L19562–L19568 | QBOWSAW @ L19549 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1670 | L19570–L19577 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != BOWSAW)     (up-compare-goal gl-build-progress == KrushBowsawNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1671 | L19579–L19590 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (unit-type-count-total villager >= 42)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == B...` | — | — | set-escrow-percentage | — | unit-type-count-total | — | — | **LOST** |
| 1672 | L19592–L19599 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item BOWSAW)     (up-research-status c: ri-bow-saw >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1673 | L19602–L19610 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item BOWSAW)     (can-research-with-escrow ri-bow-saw)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1674 | L19612–L19618 | QBOWSAW @ L19549 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1675 | L19620–L19627 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != BOWSAW)     (up-compare-goal gl-build-progress == BowsawNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1676 | L19629–L19638 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == BOWSAW)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1677 | L19640–L19647 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item BOWSAW)     (up-research-status c: ri-bow-saw >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1678 | L19651–L19663 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDMINING)     (can-research-with-escrow ri-gold-mining)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1679 | L19665–L19671 | QGOLDMINING @ L19649 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1680 | L19673–L19682 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != GOLDMINING)     (up-compare-goal gl-build-progress == KrushGoldMiningNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1681 | L19684–L19691 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item GOLDMINING)     (up-research-status c: ri-gold-mining >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1682 | L19694–L19706 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDMINING)     (can-research-with-escrow ri-gold-mining)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1683 | L19708–L19714 | QGOLDMINING @ L19649 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1684 | L19716–L19725 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDMINING)     (up-compare-goal gl-build-progress == GoldMiningNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1685 | L19727–L19734 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item GOLDMINING)     (up-research-status c: ri-gold-mining >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1686 | L19737–L19744 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDSHAFT)     (can-research-with-escrow ri-gold-shaft-mining)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1687 | L19746–L19752 | QGOLDSHAFT @ L19736 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1688 | L19754–L19763 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDSHAFT)     (up-compare-goal gl-build-progress == GoldshaftNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1689 | L19765–L19773 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDSHAFT)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1690 | L19775–L19781 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-current-build-item GOLDSHAFT)     (up-research-status c: ri-gold-shaft-mining >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1691 | L19786–L19797 | QHCOL @ L19784 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item HCOL)     (can-research-with-escrow ri-horse-collar)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1692 | L19799–L19805 | QHCOL @ L19784 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1693 | L19807–L19816 | QHCOL @ L19784 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != HCOL)     (up-compare-goal gl-build-progress == KrushHorseCollarNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1694 | L19818–L19826 | QHCOL @ L19784 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item HCOL)     (up-research-status c: ri-horse-collar >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1695 | L19829–L19841 | QHCOL @ L19784 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item HCOL)     (can-research-with-escrow ri-horse-collar)` | — | — | can-research-with-escrow | — | — | — | — | **LOST** |
| 1696 | L19843–L19849 | QHCOL @ L19784 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1697 | L19851–L19860 | QHCOL @ L19784 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != HCOL)     (up-compare-goal gl-build-progress == HorseCollarNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1698 | L19862–L19869 | QHCOL @ L19784 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item HCOL)     (up-research-status c: ri-horse-collar >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1699 | L19872–L19879 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item HEAVYPLOW)     (can-research-with-escrow ri-heavy-plow)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1700 | L19881–L19887 | QHEAVY PLOW @ L19871 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1701 | L19889–L19898 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != HEAVYPLOW)     (up-compare-goal gl-build-progress == HeavyPlowNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1702 | L19900–L19908 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == HEAVYPLOW)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1703 | L19910–L19916 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-current-build-item HEAVYPLOW)     (up-research-status c: ri-heavy-plow >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1704 | L19919–L19924 | QVILLAGERS @ L19918 | `(defrule     (not(goal gl-need-vills YES))     (up-timer-status t-vill-training != timer-disabled)` | — | t-vill-training | — | — | — | — | — | **LOST** |
| 1705 | L19927–L19936 | QVILLAGERS @ L19918 | `(defrule     (or (and(food-amount > 550)     (gold-amount > 155))     (and(gold-amount > 90)     (food-amount > 750)))     (research-available castle-age)` | — | — | — | — | research | — | — | **LOST** |
| 1706 | L19938–L19945 | QVILLAGERS @ L19918 | `(defrule     (goal gl-current-build-item PAA)     (research-completed ri-fletching)     (players-unit-type-count target-player skirmisher < 5)` | — | — | — | — | research, research-completed | — | — | **LOST** |
| 1707 | L19947–L19953 | QVILLAGERS @ L19918 | `(defrule     (false)     (goal gl-current-build-item FLTCH)     (building-type-count blacksmith > 0)` | — | — | — | — | — | 1 | — | **LOST** |
| 1708 | L19955–L19966 | QVILLAGERS @ L19918 | `(defrule     (goal gl-strategy FLUSH)     (up-can-train gl-escrow-state c: villager)     (or	(goal gl-need-vills YES)     (and(unit-type-count-total villager < 25)     (and(food...` | — | t-vill-training | — | — | unit-type-count-total, up-pending-objects, up-train | — | ShadowByzantine/12_execution.per#2; ShadowByzantine/16_pass1_transaction.per#10 | **UNKNOWN** |
| 1709 | L19969–L19980 | QVILLAGERS @ L19918 | `(defrule     (goal gl-need-vills YES)     (up-pending-objects c: villager < 1)     (or (current-age >= castle-age)     (and(current-age >= feudal-age)     (goal gl-strategy FLUS...` | — | — | — | — | up-pending-objects, up-train | — | ShadowByzantine/12_execution.per#2; ShadowByzantine/16_pass1_transaction.per#10 | **UNKNOWN** |
| 1710 | L19983–L19994 | QVILLAGERS @ L19918 | `(defrule     (goal gl-strategy KRUSH)     (up-can-train gl-escrow-state c: villager)     (or	(goal gl-need-vills YES)     (and(unit-type-count-total villager < KrushDarkAgeVills...` | — | — | — | — | unit-type-count-total, up-pending-objects, up-train | — | ShadowByzantine/12_execution.per#2; ShadowByzantine/16_pass1_transaction.per#10 | **UNKNOWN** |
| 1711 | L19998–L20004 | QESCROW @ L19996 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1712 | L20006–L20012 | QESCROW @ L19996 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1713 | L20015–L20026 | QESCROW @ L19996 | `(defrule     (goal gl-current-build-item FINISHED)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1714 | L20029–L20042 | QESCROW @ L19996 | `(defrule     (taunt-detected me 21)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1715 | L20044–L20051 | QESCROW @ L19996 | `(defrule     (or	(escrow-amount food > 850)     (and(escrow-amount food > 700)     (up-compare-goal gl-current-build-item != CUP)))` | — | — | — | — | — | — | — | **LOST** |
| 1716 | L20053–L20061 | QESCROW @ L19996 | `(defrule     (or	(escrow-amount wood > 700)     (and(escrow-amount wood > 250)     (and(up-compare-goal gl-build-progress >= FletchingNumber)     (up-research-status c: castle-a...` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1717 | L20063–L20070 | QESCROW @ L19996 | `(defrule     (or	(escrow-amount gold > 700)     (and(escrow-amount gold > 200)     (up-research-status c: castle-age < research-pending)))` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1718 | L20072–L20077 | QESCROW @ L19996 | `(defrule     (escrow-amount stone > 400)` | — | — | — | — | — | — | — | **LOST** |
| 1719 | L20079–L20095 | QESCROW @ L19996 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1720 | L20100–L20108 | QTSB @ L20097 | `(defrule     (goal gl-trushed YES)` | gl-original-ts, sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1721 | L20110–L20117 | QTSB @ L20097 | `(defrule     (goal gl-trushed NO)` | sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1722 | L20120–L20126 | QTSB @ L20097 | `(defrule     (game-time > 1800)` | sn-camp-max-distance | — | — | — | — | — | — | **LOST** |
| 1723 | L20129–L20137 | QTSB @ L20097 | `(defrule     (or	(taunt-detected me 26)     (taunt-detected any-enemy 26))` | sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1724 | L20139–L20146 | QTSB @ L20097 | `(defrule     (taunt-detected me 30)` | sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1725 | L20150–L20157 | QTSB @ L20097 | `(defrule     (current-age == dark-age)` | gl-original-ts, sn-camp-max-distance, sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1726 | L20160–L20167 | QTSB @ L20097 | `(defrule     (current-age == feudal-age)` | gl-original-ts, sn-camp-max-distance, sn-maximum-town-size | — | — | — | — | — | — | **LOST** |
| 1727 | L20170–L20177 | QTSB @ L20097 | `(defrule     (current-age == castle-age)` | — | — | — | — | — | — | — | **LOST** |
| 1728 | L20179–L20186 | QTSB @ L20097 | `(defrule     (current-age-time >= 120)     (current-age == castle-age)` | — | — | — | — | — | — | — | **LOST** |
| 1729 | L20190–L20198 | QRANGES @ L20188 | `(defrule     (goal gl-current-build-item RANGES)     (building-type-count-total archery-range >= 2)` | gl-build-progress, gl-current-build-item | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1730 | L20200–L20204 | QRANGES @ L20188 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1731 | L20206–L20211 | QRANGES @ L20188 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | — | **LOST** |
| 1732 | L20213–L20227 | QRANGES @ L20188 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item RANGES)     (can-build-with-escrow archery-range)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1733 | L20229–L20235 | QRANGES @ L20188 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1734 | L20237–L20245 | QRANGES @ L20188 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != RANGES)     (up-compare-goal gl-build-progress == RangesNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1735 | L20248–L20259 | QRANGES @ L20188 | `(defrule     (goal gl-progression-pause -1)     (can-build-with-escrow archery-range)     (goal gl-current-build-item EXTRA-RANGES)` | sn-placement-zone-size | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | — | — | **LOST** |
| 1736 | L20261–L20267 | QRANGES @ L20188 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1737 | L20269–L20278 | QRANGES @ L20188 | `(defrule     (false)     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress == 33)     (up-compare-goal gl-current-build-item != EXTRA-RANGES)` | — | — | — | — | — | — | — | **LOST** |
| 1738 | L20280–L20287 | QRANGES @ L20188 | `(defrule     (false)     (goal gl-current-build-item EXTRA-RANGES)     (building-type-count-total archery-range >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1739 | L20292–L20302 | QESKIRMS @ L20291 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1740 | L20304–L20310 | QESKIRMS @ L20291 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1741 | L20312–L20319 | QESKIRMS @ L20291 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != ESKIRMS)     (up-compare-goal gl-build-progress == EskirmsNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1742 | L20321–L20329 | QESKIRMS @ L20291 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == ESKIRMS)` | — | — | set-escrow-percentage | — | — | — | — | **LOST** |
| 1743 | L20331–L20337 | QESKIRMS @ L20291 | `(defrule     (goal gl-current-build-item ESKIRMS)     (up-research-status c: ri-elite-skirmisher >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1744 | L20341–L20346 | QSW @ L20339 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1745 | L20348–L20352 | QSW @ L20339 | `(defrule     (up-compare-goal SUPERIORITY >= 10)` | goal | — | — | — | — | — | — | **LOST** |
| 1746 | L20354–L20358 | QSW @ L20339 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | — | **LOST** |
| 1747 | L20360–L20371 | QSW @ L20339 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-progression-pause -1)     (goal gl-current-build-item SW1)     (can-build-with-escrow siege-workshop)     (not(up-pending-placem...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-placement | — | — | **LOST** |
| 1748 | L20373–L20379 | QSW @ L20339 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1749 | L20381–L20388 | QSW @ L20339 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != SW1)     (up-compare-goal gl-build-progress == FirstSiegeWorkshopNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1750 | L20390–L20400 | QSW @ L20339 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == SW1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1751 | L20402–L20408 | QSW @ L20339 | `(defrule     (false)     (up-compare-goal gl-current-build-item == SW1)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1752 | L20410–L20416 | QSW @ L20339 | `(defrule     (goal gl-current-build-item SW1)     (building-type-count-total siege-workshop >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1753 | L20419–L20430 | QSW @ L20339 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item SW2)     (can-build-with-escrow siege-workshop)` | sn-placement-zone-size | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | — | — | **LOST** |
| 1754 | L20432–L20439 | QSW @ L20339 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1755 | L20441–L20450 | QSW @ L20339 | `(defrule     (false)     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress == 33)     (up-compare-goal gl-current-build-item != SW2)` | — | — | — | — | — | — | — | **LOST** |
| 1756 | L20452–L20458 | QSW @ L20339 | `(defrule     (goal gl-current-build-item SW2)     (building-type-count-total siege-workshop >= 2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1757 | L20461–L20474 | QSW @ L20339 | `(defrule     (gold-amount > 150)     (wood-amount > 250)     (current-age-time > 150)     (can-build siege-workshop)     (goal gl-strategy SIEGE)     (building-type-count-total ...` | sn-placement-zone-size | — | — | — | building-type-count-total, up-build | — | — | **LOST** |
| 1758 | L20478–L20490 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (research-completed ri-pikeman)     (building-type-count-total barracks < 2)     (players-civilian-population target-player >= 80...` | — | — | — | — | building-type-count-total, research, research-completed | — | — | **LOST** |
| 1759 | L20492–L20503 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (research-completed ri-pikeman)     (building-type-count-total barracks < 2)     (players-civilian-population any-enemy >= 80)   ...` | gl-progression-pause | — | — | — | building-type-count-total, research, research-completed | — | — | **LOST** |
| 1760 | L20505–L20509 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause RAX2)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/16_pass1_transaction.per#5 | **UNKNOWN** |
| 1761 | L20511–L20515 | QRAX @ L20476 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1762 | L20517–L20521 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1763 | L20523–L20527 | QRAX @ L20476 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | — | **LOST** |
| 1764 | L20529–L20538 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause RAX2)     (can-build-with-escrow barracks)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1765 | L20540–L20547 | QRAX @ L20476 | `(defrule     (timer-triggered t-rax)     (building-type-count-total barracks < 1)` | — | t-rax | — | — | building-type-count-total | — | — | **LOST** |
| 1766 | L20550–L20554 | QRAX @ L20476 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1767 | L20556–L20560 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | — | **LOST** |
| 1768 | L20562–L20567 | QRAX @ L20476 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | — | **LOST** |
| 1769 | L20570–L20582 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (goal gl-strategy FLUSH)     (can-build-with-escrow barracks)     (goal gl-current-build-item RAX)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1770 | L20584–L20590 | QRAX @ L20476 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1771 | L20592–L20600 | QRAX @ L20476 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != RAX)     (up-compare-goal gl-build-progress == BarracksNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1772 | L20602–L20609 | QRAX @ L20476 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item RAX)     (building-type-count-total barracks >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1773 | L20612–L20624 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (goal gl-strategy KRUSH)     (can-build-with-escrow barracks)     (goal gl-current-build-item RAX)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1774 | L20626–L20632 | QRAX @ L20476 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1775 | L20634–L20641 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != RAX)     (up-compare-goal gl-build-progress == KrushBarracksNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1776 | L20643–L20650 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item RAX)     (building-type-count-total barracks >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1777 | L20653–L20657 | QSMITH @ L20652 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1778 | L20659–L20663 | QSMITH @ L20652 | `(defrule     (goal gl-town-safe NO)` | goal | — | — | — | — | — | — | **LOST** |
| 1779 | L20666–L20683 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow blacksmith)     (goal gl-current-build-item SMITH)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1780 | L20685–L20691 | QSMITH @ L20652 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1781 | L20693–L20700 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != SMITH)     (up-compare-goal gl-build-progress == BlackmithNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1782 | L20702–L20713 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)` | — | — | — | — | — | — | — | **LOST** |
| 1783 | L20715–L20722 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item SMITH)     (building-type-count-total blacksmith >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1784 | L20725–L20737 | QSMITH @ L20652 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-strategy KRUSH)     (can-build-with-escrow blacksmith)     (goal gl-current-build-item SMITH)` | — | — | can-build-with-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1785 | L20739–L20745 | QSMITH @ L20652 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1786 | L20747–L20754 | QSMITH @ L20652 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != SMITH)     (up-compare-goal gl-build-progress == KrushSmithNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1787 | L20756–L20763 | QSMITH @ L20652 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item SMITH)     (building-type-count-total blacksmith >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1788 | L20767–L20772 | QCASTLES @ L20765 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1789 | L20774–L20780 | QCASTLES @ L20765 | `(defrule     (not(player-valid 3))     (up-compare-goal SUPERIORITY >= 20)` | goal | — | — | — | — | — | — | **LOST** |
| 1790 | L20782–L20788 | QCASTLES @ L20765 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | — | **LOST** |
| 1791 | L20790–L20798 | QCASTLES @ L20765 | `(defrule     (can-build castle)     (current-age >= castle-age)` | sn-placement-zone-size | — | — | — | up-build | — | — | **LOST** |
| 1792 | L20801–L20817 | QFARMS @ L20800 | `(defrule     (goal gl-ninety-turn 1)     (goal gl-strategy KRUSH)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-get-fact, up-research | — | — | **LOST** |
| 1793 | L20819–L20828 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1794 | L20831–L20848 | QFARMS @ L20800 | `(defrule     (idle-farm-count < 2)     (goal gl-strategy KRUSH)     (current-age == feudal-age)     (can-build-with-escrow farm)     (up-pending-objects c: farm < 3)     (buildi...` | — | — | can-build-with-escrow | — | building-type-count-total, up-pending-objects | — | — | **LOST** |
| 1795 | L20851–L20857 | QFARMS @ L20800 | `(defrule     (or	(goal gl-current-build-item MARKET1)     (or	(up-pending-placement c: blacksmith)     (up-compare-goal gl-strategy != FLUSH)))` | — | — | — | — | up-pending-placement | 1 | — | **LOST** |
| 1796 | L20859–L20871 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1797 | L20873–L20882 | QFARMS @ L20800 | `(defrule     (goal SPLIT 1)     (or	(building-type-count-total blacksmith >= 1)     (or	(and(up-compare-goal rt >= 2)     (building-type-count-total farm < 7))     (and(up-compa...` | split | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1798 | L20884–L20892 | QFARMS @ L20800 | `(defrule     (goal SPLIT 2)     (or	(nand	(current-age == castle-age)     (up-compare-goal gl-current-build-item == ESKIRMS))     (up-research-status c: ri-elite-skirmisher >= r...` | — | — | — | — | research-pending, up-build, up-research | — | — | **LOST** |
| 1799 | L20894–L20899 | QFARMS @ L20800 | `(defrule     (true)` | gl-escrow-state, split | — | — | — | — | — | — | **LOST** |
| 1800 | L20902–L20911 | QFARMS @ L20800 | `(defrule     (can-build farm)     (wood-amount >= 90)     (idle-farm-count < 2)     (up-compare-goal MILL != YES)     (up-pending-objects c: farm < 2)     (building-type-count-t...` | split | — | — | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/04_construction.per#5 | **UNKNOWN** |
| 1801 | L20913–L20923 | QFARMS @ L20800 | `(defrule     (goal SPLIT 1)     (or	(current-age >= castle-age)     (and(goal gl-strategy KRUSH)     (up-research-status c: ri-horse-collar >= research-complete)))     (or	(wood...` | — | — | — | — | up-research | — | — | **LOST** |
| 1802 | L20925–L20929 | QFARMS @ L20800 | `(defrule     (true)` | split | — | — | — | — | — | — | **LOST** |
| 1803 | L20932–L20943 | QFARMS @ L20800 | `(defrule     (goal gl-second-turn 1)     (goal gl-strategy FLUSH)     (up-can-build gl-escrow-state c: farm)     (up-compare-goal gl-build-progress < FletchingNumber)     (or	(w...` | — | — | — | — | building-type-count-total, up-build | — | — | **LOST** |
| 1804 | L20949–L20963 | QFARMS @ L20800 | `(defrule     (current-age == dark-age)     (can-build-with-escrow farm)     (goal gl-strategy KRUSH)     (up-pending-objects c: farm < 1)     (goal gl-current-build-item FARMS) ...` | — | — | can-build-with-escrow | — | building-type-count-total, up-pending-objects | — | — | **LOST** |
| 1805 | L20965–L20973 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item FARMS)     (building-type-count-total farm >= 4)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1806 | L20975–L20981 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1807 | L20983–L20990 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != FARMS)     (up-compare-goal gl-build-progress == KrushFarmsNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1808 | L20993–L21006 | QFARMS @ L20800 | `(defrule     (current-age == dark-age)     (can-build-with-escrow farm)     (or (wood-amount >= 90)     (housing-headroom >= 3))     (goal gl-strategy KRUSH)     (up-pending-obj...` | — | — | can-build-with-escrow | — | building-type-count-total, up-pending-objects | — | — | **LOST** |
| 1809 | L21008–L21016 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item FARMS2)     (building-type-count-total farm >= 7)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1810 | L21018–L21025 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != FARMS2)     (up-compare-goal gl-build-progress == KrushFarms2Number)` | — | — | — | — | — | — | — | **LOST** |
| 1811 | L21028–L21041 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1812 | L21043–L21050 | QFARMS @ L20800 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item FARMS)     (building-type-count-total farm >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1813 | L21052–L21058 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1814 | L21060–L21068 | QFARMS @ L20800 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != FARMS)     (up-compare-goal gl-build-progress == FarmsNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1815 | L21071–L21076 | QHOUSE @ L21070 | `(defrule     (true)` | — | — | — | — | — | — | — | **LOST** |
| 1816 | L21078–L21086 | QHOUSE @ L21070 | `(defrule     (false)     (game-time >= 50)     (goal gl-fifth-turn 1)     (housing-headroom < 2)` | — | — | — | — | — | — | — | **LOST** |
| 1817 | L21088–L21099 | QHOUSE @ L21070 | `(defrule     (game-time > 6)     (housing-headroom < 5)     (population-headroom != 0)     (can-build-with-escrow house)     (up-pending-objects c: house < 1)     (building-type...` | — | — | can-build-with-escrow | — | up-build, up-pending-objects | — | — | **LOST** |
| 1818 | L21101–L21111 | QHOUSE @ L21070 | `(defrule     (game-time > 6)     (housing-headroom < 2)     (population-headroom != 0)     (can-build-with-escrow house)     (up-pending-objects c: house < 1)` | — | — | can-build-with-escrow | — | up-build, up-pending-objects | — | — | **LOST** |
| 1819 | L21113–L21120 | QHOUSE @ L21070 | `(defrule     (can-build house)` | — | — | — | — | up-build | — | — | **LOST** |
| 1820 | L21122–L21134 | QHOUSE @ L21070 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1821 | L21136–L21140 | QHOUSE @ L21070 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1822 | L21142–L21147 | QHOUSE @ L21070 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | — | **LOST** |
| 1823 | L21149–L21162 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 4)     (population-headroom != 0)     (building-type-count house < 5)     (up-pending-objects c: house < 1)` | — | — | — | — | up-pending-objects | — | ShadowByzantine/04_construction.per#1; ShadowByzantine/04_construction.per#2 | **UNKNOWN** |
| 1824 | L21164–L21178 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 4)     (population-headroom != 0)     (building-type-count house >= 5)     (up-pending-objects c: house < 1)     (building...` | — | — | — | — | up-pending-objects | — | ShadowByzantine/04_construction.per#1; ShadowByzantine/04_construction.per#2 | **UNKNOWN** |
| 1825 | L21180–L21193 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 10)     (population-headroom != 0)     (up-pending-objects c: house < 1)     (or	(and(goal gl-strategy KRUSH)     (buildin...` | sn-placement-fail-delta, sn-placement-zone-size | — | — | — | building-type-count-total, up-build, up-pending-objects | — | — | **LOST** |
| 1826 | L21195–L21208 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 15)     (population-headroom != 0)     (up-pending-objects c: house < 2)     (or	(and(goal gl-strategy FLUSH)     (buildin...` | split | — | — | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/04_construction.per#5 | **UNKNOWN** |
| 1827 | L21210–L21218 | QHOUSE @ L21070 | `(defrule     (goal SPLIT 1)` | sn-placement-fail-delta, sn-placement-zone-size, split | — | — | — | up-build | — | — | **LOST** |
| 1828 | L21222–L21235 | QLC @ L21220 | `(defrule     (goal gl-fifth-turn 1)     (civilian-population >= 7)     (or	(housing-headroom >= 5)     (civilian-population >= 15))     (goal gl-current-build-item LC1)     (can...` | sn-allow-adjacent-dropsites | — | can-build-with-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1829 | L21238–L21244 | QLC @ L21220 | `(defrule     (goal gl-dark-build LumberFirst)     (up-compare-goal gl-build-progress > 1)     (building-type-count-total lumber-camp < 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1830 | L21246–L21252 | QLC @ L21220 | `(defrule     (goal gl-dark-build MillFirst)     (up-compare-goal gl-build-progress > 2)     (building-type-count-total lumber-camp < 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1831 | L21254–L21264 | QLC @ L21220 | `(defrule     (up-compare-goal gl-current-build-item != LC1)     (or	(and(goal gl-dark-build MillFirst)     (up-compare-goal gl-build-progress == 2))     (and(goal gl-dark-build ...` | — | — | — | — | — | — | — | **LOST** |
| 1832 | L21267–L21273 | QLC @ L21220 | `(defrule     (goal gl-current-build-item LC1)     (building-type-count-total lumber-camp >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1833 | L21276–L21286 | QLC @ L21220 | `(defrule     (can-build lumber-camp)     (current-age >= feudal-age)     (up-gaia-type-count c: wood > 20)     (building-type-count-total lumber-camp < 1)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1834 | L21290–L21297 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item LC2)     (building-type-count-total lumber-camp >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1835 | L21299–L21314 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item LC2)     (or	(game-time >= 480)     (or	(wood-amount >= 110)     (housing-headroom >= 5)))     (can-build-w...` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow, set-escrow-percentage | — | building-type-count-total | — | — | **LOST** |
| 1836 | L21316–L21322 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1837 | L21324–L21332 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LC2)     (up-compare-goal gl-build-progress == LC2Number)` | — | — | — | — | — | — | — | **LOST** |
| 1838 | L21335–L21342 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item LC2)     (building-type-count-total lumber-camp >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1839 | L21344–L21359 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item LC2)     (or	(game-time >= 480)     (or	(wood-amount >= 110)     (housing-headroom >= 5)))     (can-build-w...` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow | — | building-type-count-total | — | — | **LOST** |
| 1840 | L21361–L21367 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1841 | L21369–L21376 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != LC2)     (up-compare-goal gl-build-progress == KrushLC2Number)` | — | — | — | — | — | — | — | **LOST** |
| 1842 | L21380–L21392 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item LC3)     (can-build-with-escrow lumber-camp)` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1843 | L21394–L21400 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1844 | L21402–L21410 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LC3)     (up-compare-goal gl-build-progress == LC3Number)` | — | — | — | — | — | — | — | **LOST** |
| 1845 | L21412–L21419 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item LC3)     (building-type-count-total lumber-camp >= 3)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1846 | L21422–L21434 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item LC3)     (can-build-with-escrow lumber-camp)` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1847 | L21436–L21442 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1848 | L21444–L21452 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != LC3)     (up-compare-goal gl-build-progress == KrushLC3Number)` | — | — | — | — | — | — | — | **LOST** |
| 1849 | L21454–L21461 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item LC3)     (building-type-count-total lumber-camp >= 3)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1850 | L21464–L21468 | QLC @ L21220 | `(defrule     (true)` | — | — | — | — | — | 4 | — | **LOST** |
| 1851 | L21470–L21479 | QLC @ L21220 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item LC4)     (can-build-with-escrow lumber-camp)` | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | build | — | — | **LOST** |
| 1852 | L21481–L21487 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1853 | L21489–L21497 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LC4)     (up-compare-goal gl-build-progress == LC4Number)` | — | — | — | — | — | — | — | **LOST** |
| 1854 | L21499–L21505 | QLC @ L21220 | `(defrule     (goal gl-current-build-item LC4)     (building-type-count-total lumber-camp >= 4)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1855 | L21509–L21522 | QLC @ L21220 | `(defrule     (or	(game-time >= 1570)` | — | — | — | — | — | — | — | **LOST** |
| 1856 | L21527–L21536 | QTRADING @ L21524 | `(defrule     (food-amount < 50)     (can-buy-commodity food)     (or	(gold-amount >= 230)     (and(gold-amount >= 170)     (up-compare-goal gl-build-progress < 13)))` | — | — | — | — | — | — | — | **LOST** |
| 1857 | L21538–L21550 | QTRADING @ L21524 | `(defrule     (can-buy-commodity food)     (or	(and(food-amount < 800)     (gold-amount >= 300))     (or	(and(food-amount < 550)     (gold-amount >= 240))     (and(food-amount < ...` | — | — | — | — | — | — | — | **LOST** |
| 1858 | L21553–L21563 | QTRADING @ L21524 | `(defrule     (wood-amount < 50)     (or	(gold-amount >= 320)     (and(gold-amount >= 240)     (or	(up-compare-goal gl-current-build-item < LC3)     (up-compare-goal gl-current-b...` | — | — | — | — | — | — | — | **LOST** |
| 1859 | L21567–L21575 | QTRADING @ L21524 | `(defrule     (gold-amount < 100)     (food-amount >= 320)     (can-sell-commodity food)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1860 | L21577–L21587 | QTRADING @ L21524 | `(defrule     (can-sell-commodity food)     (or	(and(gold-amount < 160)     (food-amount >= 880))     (and(gold-amount < 200)     (food-amount >= 980)))     (goal gl-current-buil...` | — | — | — | — | — | — | — | **LOST** |
| 1861 | L21590–L21598 | QTRADING @ L21524 | `(defrule     (wood-amount >= 270)     (goal gl-strategy FLUSH)     (can-sell-commodity wood)     (up-compare-goal gl-build-progress >= ExtraStablesNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1862 | L21600–L21607 | QTRADING @ L21524 | `(defrule     (wood-amount >= 260)     (can-sell-commodity wood)     (goal gl-current-build-item EXTRA-STABLES)` | — | — | — | — | — | — | — | **LOST** |
| 1863 | L21609–L21621 | QTRADING @ L21524 | `(defrule     (can-sell-commodity wood)     (up-compare-goal gl-current-build-item != EXTRA-STABLES)     (or	(and(gold-amount < 60)     (wood-amount >= 260))     (and(food-amount...` | — | — | — | — | — | — | — | **LOST** |
| 1864 | L21623–L21632 | QTRADING @ L21524 | `(defrule     (wood-amount >= 150)     (or	(food-amount < 750)     (gold-amount < 160))     (can-sell-commodity wood)     (goal gl-current-build-item CUP)` | — | — | — | — | — | — | — | **LOST** |
| 1865 | L21635–L21647 | QTRADING @ L21524 | `(defrule     (false)     (can-sell-commodity stone)     (or	(and(gold-amount < 100)     (stone-amount >= 220))     (or	(and(wood-amount < 100)     (stone-amount >= 220))     (an...` | — | — | — | — | — | — | — | **LOST** |
| 1866 | L21651–L21665 | QMILL @ L21649 | `(defrule     (can-build-with-escrow mill)     (or (resource-found food)     (game-time >= SkipMillTime))     (goal gl-current-build-item MILL1)     (building-type-count-total mi...` | sn-allow-adjacent-dropsites | t-build-delay | can-build-with-escrow, set-escrow-percentage | — | building-type-count-total | — | — | **LOST** |
| 1867 | L21667–L21673 | QMILL @ L21649 | `(defrule     (goal gl-current-build-item MILL1)     (building-type-count-total mill >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1868 | L21675–L21682 | QMILL @ L21649 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1869 | L21684–L21691 | QMILL @ L21649 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1870 | L21693–L21703 | QMILL @ L21649 | `(defrule     (up-compare-goal gl-current-build-item != MILL1)     (or	(and(goal gl-dark-build MillFirst)     (up-compare-goal gl-build-progress == 1))     (and(goal gl-dark-buil...` | — | — | — | — | — | — | — | **LOST** |
| 1871 | L21706–L21716 | QMILL @ L21649 | `(defrule     (can-build mill)     (resource-found food)     (current-age >= feudal-age)     (building-type-count-total mill < 1)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1872 | L21718–L21722 | QMILL @ L21649 | `(defrule     (true)` | goal | — | — | — | — | — | — | **LOST** |
| 1873 | L21724–L21728 | QMILL @ L21649 | `(defrule     (building-type-count-total mill == 2)` | goal | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1874 | L21730–L21734 | QMILL @ L21649 | `(defrule     (building-type-count-total mill == 3)` | goal | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1875 | L21736–L21746 | QMILL @ L21649 | `(defrule     (goal MILL YES)     (can-build mill)     (building-type-count-total mill < 4)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1876 | L21748–L21760 | QMILL @ L21649 | `(defrule     (up-compare-goal MILL != YES)     (not(up-pending-placement c: mill))     (or	(and(building-type-count-total mill < 2)     (building-type-count-total farm > 20))   ...` | — | — | — | — | building-type-count-total, up-pending-placement | — | — | **LOST** |
| 1877 | L21766–L21779 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1878 | L21781–L21796 | QMC @ L21762 | `(defrule     (goal gl-progression-pause -1)     (goal gl-strategy KRUSH)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC1)     (building-type-coun...` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | building-type-count-total | — | — | **LOST** |
| 1879 | L21798–L21809 | QMC @ L21762 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (dropsite-min-distance gold > 3)     (can-build-with-escrow mining-camp) ...` | split | t-build-delay | can-build-with-escrow | up-set-target-object | — | — | — | **LOST** |
| 1880 | L21811–L21827 | QMC @ L21762 | `(defrule     (goal SPLIT 1)` | — | t-build-delay | — | — | — | — | — | **LOST** |
| 1881 | L21829–L21835 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1882 | L21837–L21844 | QMC @ L21762 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != GOLDMC1)     (up-compare-goal gl-build-progress == KrushGoldMCNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1883 | L21846–L21854 | QMC @ L21762 | `(defrule     (goal gl-strategy KRUSH)     (dropsite-min-distance gold < 5)     (goal gl-current-build-item GOLDMC1)` | — | — | — | — | — | — | — | **LOST** |
| 1884 | L21857–L21870 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1885 | L21872–L21887 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC1)     (building-type-coun...` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | building-type-count-total | — | — | **LOST** |
| 1886 | L21889–L21900 | QMC @ L21762 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (dropsite-min-distance gold > 3)     (can-build-with-escrow mining-camp) ...` | split | t-build-delay | can-build-with-escrow | up-set-target-object | — | — | — | **LOST** |
| 1887 | L21902–L21918 | QMC @ L21762 | `(defrule     (goal SPLIT 1)` | — | t-build-delay | — | — | — | — | — | **LOST** |
| 1888 | L21920–L21926 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1889 | L21928–L21936 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDMC1)     (up-compare-goal gl-build-progress == GoldMC1Number)` | — | — | — | — | — | — | — | **LOST** |
| 1890 | L21938–L21945 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (dropsite-min-distance gold < 5)     (goal gl-current-build-item GOLDMC1)` | — | — | — | — | — | — | — | **LOST** |
| 1891 | L21948–L21952 | QMC @ L21762 | `(defrule     (true)` | — | — | — | — | — | 5 | — | **LOST** |
| 1892 | L21954–L21967 | QMC @ L21762 | `(defrule     (false)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC2)` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-point | — | — | — | **LOST** |
| 1893 | L21969–L21987 | QMC @ L21762 | `(defrule     (false)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC2)     (up-set-target-object search-remote ...` | — | — | can-build-with-escrow | up-set-target-object | — | — | — | **LOST** |
| 1894 | L21989–L21995 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1895 | L21997–L22005 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDMC2)     (up-compare-goal gl-build-progress == GoldMC2Number)` | — | — | — | — | — | — | — | **LOST** |
| 1896 | L22007–L22013 | QMC @ L21762 | `(defrule     (goal gl-current-build-item GOLDMC2)     (building-type-count-total mining-camp >= 3)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1897 | L22016–L22030 | QMC @ L21762 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item STONEMC1)` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | — | **LOST** |
| 1898 | L22032–L22051 | QMC @ L21762 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item STONEMC1)` | — | — | can-build-with-escrow | — | — | — | — | **LOST** |
| 1899 | L22053–L22059 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1900 | L22061–L22069 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != STONEMC1)     (up-compare-goal gl-build-progress == StoneMC1Number)` | — | — | — | — | — | — | — | **LOST** |
| 1901 | L22071–L22077 | QMC @ L21762 | `(defrule     (dropsite-min-distance stone < 5)     (goal gl-current-build-item STONEMC1)` | — | — | — | — | — | — | — | **LOST** |
| 1902 | L22080–L22095 | QMC @ L21762 | `(defrule     (or	(game-time >= 1480)` | — | — | — | — | — | — | — | **LOST** |
| 1903 | L22098–L22107 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-progression-pause -1)     (can-build-with-escrow university)     (goal gl-current-build-item UNIVERSITY)` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build | — | — | **LOST** |
| 1904 | L22109–L22115 | QUNIVERSITY @ L22097 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1905 | L22117–L22125 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != UNIVERSITY)     (up-compare-goal gl-build-progress == UniversityNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1906 | L22127–L22136 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == UNIVERSITY)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1907 | L22138–L22144 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-current-build-item UNIVERSITY)     (building-type-count-total university >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/02_state.per#1; ShadowByzantine/02_state.per#2; ShadowByzantine/04_construction.per#6 | **UNKNOWN** |
| 1908 | L22147–L22154 | QBALLISTICS @ L22146 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item BALLISTICS)     (can-research-with-escrow ri-ballistics)` | — | — | can-research-with-escrow | — | up-research | — | — | **LOST** |
| 1909 | L22156–L22162 | QBALLISTICS @ L22146 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1910 | L22164–L22173 | QBALLISTICS @ L22146 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != BALLISTICS)     (up-compare-goal gl-build-progress == BallisticsNumber)` | — | — | — | — | — | — | — | **LOST** |
| 1911 | L22175–L22183 | QBALLISTICS @ L22146 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == BALLISTICS)` | — | — | release-escrow, set-escrow-percentage | — | — | — | — | **LOST** |
| 1912 | L22185–L22191 | QBALLISTICS @ L22146 | `(defrule     (goal gl-current-build-item BALLISTICS)     (up-research-status c: ri-ballistics >= research-pending)` | — | — | — | — | research-pending, up-research | — | — | **LOST** |
| 1913 | L22195–L22200 | QEND @ L22193 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1914 | L22203–L22210 | QEND @ L22193 | `(defrule     (game-time > 45)     (goal gl-position FLANK)` | — | — | — | — | — | — | — | **LOST** |
| 1915 | L22212–L22218 | QEND @ L22193 | `(defrule     (game-time > 46)     (goal gl-position FLANK)` | — | — | — | — | — | — | — | **LOST** |
| 1916 | L22221–L22226 | QMISC @ L22220 | `(defrule     (true)` | gl-identity | — | — | — | — | — | — | **LOST** |
| 1917 | L22228–L22237 | QMISC @ L22220 | `(defrule     (game-time > 20)     (game-time < 40)     (or	(death-match-game)     (or	(current-age > dark-age)     (not(civ-selected viking))))` | — | — | — | — | — | — | — | **LOST** |
| 1918 | L22239–L22249 | QMISC @ L22220 | `(defrule     (goal gl-strategy FLUSH)     (or	(taunt-detected me 250)     (or	(taunt-detected any-ally 250)     (taunt-detected any-enemy 250)))` | — | — | — | — | — | — | — | **LOST** |
| 1919 | L22251–L22261 | QMISC @ L22220 | `(defrule     (goal gl-strategy KRUSH)     (or	(taunt-detected me 250)     (or	(taunt-detected any-ally 250)     (taunt-detected any-enemy 250)))` | — | — | — | — | — | — | — | **LOST** |
| 1920 | L22265–L22273 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (game-time < 660)     (not(goal EARLY-MINING-NOTICE YES))     (players-building-type-count target-player mining-camp > 0)` | early-mining-notice | — | — | — | — | — | — | **LOST** |
| 1921 | L22275–L22284 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (goal gl-enemy-strategy -1)     (players-current-age-time target-player > 100)     (players-current-age target-player > dark-age)` | — | — | — | — | — | — | — | **LOST** |
| 1922 | L22287–L22296 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (goal gl-enemy-strategy -1)     (players-current-age target-player == dark-age)     (players-military-population target-player > 2)` | gl-enemy-strategy | — | — | — | — | — | — | **LOST** |
| 1923 | L22299–L22312 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (not(goal gl-enemy-strategy RANGED-FLUSH))     (players-current-age target-player == feudal-age)     (or	(and(players-current-age-time target-player < 1...` | gl-enemy-strategy, gl-enemy-strategy-type | — | — | — | — | — | — | **LOST** |
| 1924 | L22314–L22325 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (not(goal gl-enemy-strategy SCRUSH))     (players-current-age target-player == feudal-age)     (players-building-type-count target-player archery-range ...` | gl-enemy-strategy, gl-enemy-strategy-type | — | — | — | — | — | — | **LOST** |
| 1925 | L22327–L22336 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (goal gl-enemy-strategy-type FC)     (up-compare-goal gl-target-age < CA-loading)     (players-current-age-time target-player > 100)     (players-curren...` | gl-enemy-strategy-type | — | — | — | — | — | — | **LOST** |
| 1926 | L22339–L22350 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (not(goal gl-enemy-strategy KRUSH))     (players-current-age target-player == feudal-age)     (players-building-type-count target-player stable > 0)    ...` | gl-enemy-strategy, gl-enemy-strategy-type | — | — | — | — | — | — | **LOST** |
| 1927 | L22354–L22359 | QEAGOL @ L22352 | `(defrule     (true)` | — | — | — | — | up-get-fact | — | — | **LOST** |
| 1928 | L22362–L22367 | QEAGOL @ L22352 | `(defrule     (true)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1929 | L22369–L22374 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age FA-loading)` | — | — | — | — | — | — | — | **LOST** |
| 1930 | L22376–L22382 | QEAGOL @ L22352 | `(defrule     (up-compare-goal gl-target-age < FA)     (players-current-age target-player == feudal-age)` | — | — | — | — | — | — | — | **LOST** |
| 1931 | L22384–L22389 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age CA-loading)` | — | — | — | — | — | — | — | **LOST** |
| 1932 | L22391–L22396 | QEAGOL @ L22352 | `(defrule     (up-compare-goal gl-target-age < CA)     (players-current-age target-player >= castle-age)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1933 | L22398–L22403 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age IA-loading)` | — | — | — | — | — | — | — | **LOST** |
| 1934 | L22405–L22410 | QEAGOL @ L22352 | `(defrule     (up-compare-goal gl-target-age < IA)     (players-current-age target-player >= imperial-age)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1935 | L22413–L22422 | QEAGOL @ L22352 | `(defrule     (game-time > 10)     (player-valid target-player)     (players-building-count target-player > 0)` | — | — | — | — | — | — | — | **LOST** |
| 1936 | L22424–L22428 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age-checking YES)` | — | — | — | — | — | — | — | **LOST** |
| 1937 | L22430–L22435 | QEAGOL @ L22352 | `(defrule     (true)` | gl-target-score1 | — | — | — | — | — | — | **LOST** |
| 1938 | L22438–L22443 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age-checking YES)     (players-current-age target-player == dark-age)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1939 | L22446–L22453 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age-checking YES)     (up-compare-goal gl-target-score1 > 37)     (up-compare-goal gl-target-age < FA-loading)` | — | — | — | — | — | — | — | **LOST** |
| 1940 | L22455–L22464 | QEAGOL @ L22352 | `(defrule     (false)     (goal gl-target-age-checking YES)     (goal gl-target-age FA-loading)     (up-compare-goal gl-target-score1 < -37)     (up-timer-status t-enemy-age-canc...` | gl-target-age | t-enemy-age-cancel | — | — | — | — | — | **LOST** |
| 1941 | L22466–L22472 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age FA-loading)     (goal gl-target-age-checking YES)     (players-current-age target-player == feudal-age)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1942 | L22475–L22483 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age FA)     (false)     (up-compare-goal gl-target-score1 > 65)     (players-current-age-time target-player > 30)` | — | — | — | — | — | — | — | **LOST** |
| 1943 | L22485–L22494 | QEAGOL @ L22352 | `(defrule     (false)     (goal gl-target-age CA-loading)     (goal gl-target-age-checking YES)     (up-compare-goal gl-target-score1 < -65)     (up-timer-status t-enemy-age-canc...` | — | t-enemy-age-cancel | — | — | — | — | — | **LOST** |
| 1944 | L22496–L22502 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age CA-loading)     (goal gl-target-age-checking YES)     (players-current-age target-player == castle-age)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1945 | L22505–L22512 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age CA)     (up-compare-goal gl-target-score1 > 100)     (players-current-age-time target-player > 30)` | — | — | — | — | — | — | — | **LOST** |
| 1946 | L22514–L22523 | QEAGOL @ L22352 | `(defrule     (false)     (goal gl-target-age-checking YES)     (goal gl-target-age IA-loading)     (up-compare-goal gl-target-score1 < -100)     (up-timer-status t-enemy-age-can...` | gl-target-age | t-enemy-age-cancel | — | — | — | — | — | **LOST** |
| 1947 | L22525–L22531 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age IA-loading)     (goal gl-target-age-checking YES)     (players-current-age target-player == imperial-age)` | gl-target-age | — | — | — | — | — | — | **LOST** |
| 1948 | L22533–L22539 | QEAGOL @ L22352 | `(defrule` | — | — | — | — | — | — | — | **LOST** |
| 1949 | L22542–L22546 | QSPECIAL TIMERS @ L22541 | `(defrule     (timer-triggered 30SEC)` | gl-switch | 30sec | — | — | — | — | — | **LOST** |
| 1950 | L22548–L22552 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status 30SEC != timer-running)` | — | 30sec | — | — | — | — | — | **LOST** |
| 1951 | L22554–L22558 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status ONE-MINUTE != timer-running)` | — | one-minute | — | — | — | — | — | **LOST** |
| 1952 | L22560–L22564 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status THREE-MINUTE != timer-running)` | — | three-minute | — | — | — | — | — | **LOST** |
| 1953 | L22566–L22570 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status TWO-MINUTE != timer-running)` | — | two-minute | — | — | — | — | — | **LOST** |
| 1954 | L22572–L22576 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status five-seconds-timer != timer-running)` | — | five-seconds-timer | — | — | — | — | — | **LOST** |
| 1955 | L22578–L22590 | QSPECIAL TIMERS @ L22541 | `(defrule     (true)` | gl-fifth-turn, gl-second-turn, gl-seventh-turn, gl-tenth-turn, gl-turn-count | — | — | — | — | — | — | **LOST** |
| 1956 | L22592–L22603 | QSPECIAL TIMERS @ L22541 | `(defrule     (true)` | gl-fifty-turn, gl-ninety-turn, gl-thirty-turn, gl-twenty-turn | — | — | — | — | — | — | **LOST** |

### D. Current ShadowByzantine inventory

| File | Current rule | Mechanism | Candidate donor region(s) | Classification basis |
|---|---:|---|---|---|
| `ShadowByzantine/02_state.per` | 1 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | ADAPTED/CHANGED |
| `ShadowByzantine/02_state.per` | 2 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | ADAPTED/CHANGED |
| `ShadowByzantine/03_economy.per` | 1 | train | — | ADDED/UNKNOWN |
| `ShadowByzantine/03_economy.per` | 2 | disable-self | QDARK @ L13824, QFLUSH @ L13980 | ADAPTED/CHANGED |
| `ShadowByzantine/04_construction.per` | 1 | build | QHOUSE @ L21070 | ADAPTED/CHANGED |
| `ShadowByzantine/04_construction.per` | 2 | build | QHOUSE @ L21070 | ADAPTED/CHANGED |
| `ShadowByzantine/04_construction.per` | 3 | build, building-type-count-total, disable-self | QECO NUMBERS @ L16922, QFLUSH @ L13980 | ADAPTED/CHANGED |
| `ShadowByzantine/04_construction.per` | 4 | build, building-type-count-total, disable-self | — | ADDED/UNKNOWN |
| `ShadowByzantine/04_construction.per` | 5 | build, building-type-count-total | QFARMS @ L20800, QHOUSE @ L21070 | ADAPTED/CHANGED |
| `ShadowByzantine/04_construction.per` | 6 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | ADAPTED/CHANGED |
| `ShadowByzantine/04_construction.per` | 7 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | ADAPTED/CHANGED |
| `ShadowByzantine/05_composition_policy.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 3 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 4 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 5 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 6 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 7 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 8 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 9 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 10 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 11 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 12 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 13 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 14 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 15 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 16 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 17 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 18 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 19 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 20 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 21 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 22 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 23 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/05_production.per` | 24 | unit-type-count-total | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 1 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 5 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 6 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 7 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 8 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 9 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 10 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 11 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 12 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 13 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/06_military.per` | 14 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 3 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 4 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 5 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 6 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 7 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 8 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 9 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 10 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 11 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 12 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 13 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 14 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 15 | build | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 16 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 17 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 18 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_placement.per` | 19 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 5 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 6 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 7 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 8 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 9 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 10 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/07_strategic reserve.per` | 11 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 5 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 6 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 7 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 8 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 9 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 10 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 11 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 12 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 13 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 14 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 15 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 16 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 17 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 18 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 19 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 20 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 21 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 22 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 23 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 24 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 25 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 26 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 27 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 28 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 29 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 30 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 31 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 32 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 33 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 34 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 35 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 36 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 37 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 38 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 39 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 40 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 41 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 42 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 43 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 44 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 45 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 46 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 47 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 48 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 49 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 50 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 51 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 52 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 53 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 54 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 55 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 56 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 57 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 58 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 59 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 60 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 61 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 62 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 63 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 64 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 65 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 66 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 67 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 68 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/08_requirements.per` | 69 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 5 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 6 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/09_capital.per` | 7 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/10_escrow.per` | 1 | release-escrow | — | ADDED/UNKNOWN |
| `ShadowByzantine/10_escrow.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/10_escrow.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/11_authority.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/11_authority.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/11_authority.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/11_authority.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/11_authority.per` | 5 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/12_execution.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/12_execution.per` | 2 | train, up-train | QMANGOS @ L15229, QVILLAGERS @ L19918 | ADAPTED/CHANGED |
| `ShadowByzantine/12_execution.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/13_verification.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/13_verification.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/13_verification.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/13_verification.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/13_verification.per` | 5 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/14_recovery.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/14_recovery.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/14_recovery.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/14_recovery.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/15_reassessment.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/15_reassessment.per` | 2 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 1 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 2 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | ADAPTED/CHANGED |
| `ShadowByzantine/16_pass1_transaction.per` | 3 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 4 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 5 | up-modify-escrow | QCHAINMAIL @ L14326, QMANGOS @ L15229, QSCALEMAIL @ L14293 | ADAPTED/CHANGED |
| `ShadowByzantine/16_pass1_transaction.per` | 6 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 7 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 8 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 9 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 10 | train, up-train | QMANGOS @ L15229, QVILLAGERS @ L19918 | ADAPTED/CHANGED |
| `ShadowByzantine/16_pass1_transaction.per` | 11 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 12 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 13 | release-escrow | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 14 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 15 | — | — | ADDED/UNKNOWN |
| `ShadowByzantine/16_pass1_transaction.per` | 16 | — | — | ADDED/UNKNOWN |

### E. Generator invariants

1. Donor ordinals are assigned solely by source-order `defrule` extraction.
2. Donor offsets are the actual source line intervals in `ShadowSource.per`.
3. No conceptual subsystem name is used as a donor ordinal.
4. Exact rule text is required for PRESERVED/MOVED; mechanism overlap alone cannot promote to exact transplantation.
5. A candidate match is not runtime qualification and does not establish firing reachability.
6. Command issuance remains distinct from world-state completion.

<!-- END GENERATED RULE-LEVEL ATLAS -->
