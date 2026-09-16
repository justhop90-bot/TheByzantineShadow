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

Generated directly from `ShadowSource.per` (1956 rules) and the current `ShadowByzantine/**/*.per` tree (2150 rules).
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
| 1 | L1–L5 | UNHEADED @ L1 | `(defrule     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1 | **PRESERVED** |
| 2 | L7–L13 | UNHEADED @ L7 | `(defrule     (taunt-detected my-player-number 7)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#2 | **PRESERVED** |
| 3 | L1451–L1456 | QPOSITION @ L1401 | `(defrule     (true)` | gl-scout-unit | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#3 | **PRESERVED** |
| 4 | L1791–L1800 | QEAGOL @ L1723 | `(defrule     (building-type-count town-center > 0)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#4 | **PRESERVED** |
| 5 | L1802–L1810 | QEAGOL @ L1723 | `(defrule     (unit-type-count scout-cavalry-line > 0)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#5 | **PRESERVED** |
| 6 | L1812–L1819 | QEAGOL @ L1723 | `(defrule     (true)` | gl-max-coordinate-value | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#6 | **PRESERVED** |
| 7 | L1821–L1832 | QEAGOL @ L1723 | `(defrule     (true)` | — | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#7 | **PRESERVED** |
| 8 | L1834–L1845 | QEAGOL @ L1723 | `(defrule     (true)` | net-food-amount, net-gold-amount, net-stone-amount, net-wood-amount | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#8 | **PRESERVED** |
| 9 | L1848–L1862 | QEAGOL @ L1723 | `(defrule     (taunt-detected me 100)     (goal gl-second-turn 1)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#9 | **PRESERVED** |
| 10 | L1864–L1870 | QEAGOL @ L1723 | `(defrule     (goal gl-fifth-turn 1)     (taunt-detected me 100)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#10 | **PRESERVED** |
| 11 | L1872–L1877 | QEAGOL @ L1723 | `(defrule     (taunt-detected me 101)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#11 | **PRESERVED** |
| 12 | L1925–L1929 | QSETUP @ L1924 | `(defrule     (taunt-detected me 27)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#12 | **PRESERVED** |
| 13 | L1931–L1936 | QSETUP @ L1924 | `(defrule     (taunt-detected me 28)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#13 | **PRESERVED** |
| 14 | L1938–L1946 | QSETUP @ L1924 | `(defrule     (false)     (up-group-size c: RaidGroup > 0)     (goal gl-current-group RaidGroup)` | gl-current-group | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#14 | **PRESERVED** |
| 15 | L1948–L1955 | QSETUP @ L1924 | `(defrule     (false)     (up-group-size c: RangedGroup > 0)     (goal gl-current-group RangedGroup)` | gl-current-group | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#15 | **PRESERVED** |
| 16 | L1957–L1978 | QSETUP @ L1924 | `(defrule     (true)` | gl-current-group, gl-defend-town, gl-max-ranged-group-size, gl-range-advantage, sn-number-tasked-units | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#16 | **PRESERVED** |
| 17 | L1981–L1985 | QSETUP @ L1924 | `(defrule     (true)` | gl-tracking-range | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#17 | **PRESERVED** |
| 18 | L1987–L1991 | QSETUP @ L1924 | `(defrule     (true)` | gl-tracking-range | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#18 | **PRESERVED** |
| 19 | L1993–L1998 | QSETUP @ L1924 | `(defrule     (or	(goal gl-town-safe YES)     (up-point-distance home-x ranged-group-x >= 35))` | gl-tracking-range | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#19 | **PRESERVED** |
| 20 | L2000–L2004 | QSETUP @ L1924 | `(defrule     (research-completed ri-fletching)` | gl-tracking-range | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#20 | **PRESERVED** |
| 21 | L2006–L2010 | QSETUP @ L1924 | `(defrule     (research-completed ri-bodkin-arrow)` | gl-tracking-range | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#21 | **PRESERVED** |
| 22 | L2012–L2016 | QSETUP @ L1924 | `(defrule     (research-completed ri-elite-skirmisher)` | gl-tracking-range | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#22 | **PRESERVED** |
| 23 | L2018–L2027 | QSETUP @ L1924 | `(defrule     (research-completed ri-fletching)` | gl-close-ranged-group-range, gl-enemy-tower-range, gl-my-tower-range, gl-raid-group-range, gl-ranged-group-range | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#23 | **PRESERVED** |
| 24 | L2029–L2038 | QSETUP @ L1924 | `(defrule     (research-completed ri-bodkin-arrow)` | gl-close-ranged-group-range, gl-enemy-tower-range, gl-my-tower-range, gl-raid-group-range, gl-ranged-group-range | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#24 | **PRESERVED** |
| 25 | L2040–L2046 | QSETUP @ L1924 | `(defrule     (research-completed ri-crossbow)` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#25 | **PRESERVED** |
| 26 | L2048–L2055 | QSETUP @ L1924 | `(defrule     (research-completed ri-elite-skirmisher)` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#26 | **PRESERVED** |
| 27 | L2058–L2064 | QADVANTAGE @ L2057 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (up-point-distance ranged-group-x enemy-group-x > 15))` | gl-ranged-eval | — | — | — | — | 44 | ShadowByzantine/ShadowByzantine.per#27 | **PRESERVED** |
| 28 | L2066–L2072 | QADVANTAGE @ L2057 | `(defrule     (true)` | gl-ranged-eval, goal, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#28 | **PRESERVED** |
| 29 | L2075–L2088 | QADVANTAGE @ L2057 | `(defrule     (false)` | gl-ranged-eval, rt, sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#29 | **PRESERVED** |
| 30 | L2091–L2096 | QADVANTAGE @ L2057 | `(defrule     (or	(up-research-status c: ri-fletching == research-pending)     (up-research-status c: ri-padded-archer-armor == research-pending))` | gl-ranged-eval | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#30 | **PRESERVED** |
| 31 | L2099–L2103 | QADVANTAGE @ L2057 | `(defrule     (goal UP-FIRST 1)` | gl-ranged-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#31 | **PRESERVED** |
| 32 | L2105–L2109 | QADVANTAGE @ L2057 | `(defrule     (goal UP-FIRST 0)` | gl-ranged-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#32 | **PRESERVED** |
| 33 | L2112–L2118 | QADVANTAGE @ L2057 | `(defrule     (true)` | gl-ranged-eval, goal9 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#33 | **PRESERVED** |
| 34 | L2121–L2132 | QADVANTAGE @ L2057 | `(defrule     (false)     (up-point-distance ranged-group-x enemy-group-x > 2)     (up-point-distance ranged-group-x enemy-group-x < 10)` | — | — | — | up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#34 | **PRESERVED** |
| 35 | L2134–L2141 | QADVANTAGE @ L2057 | `(defrule     (false)     (up-compare-goal goal8 >= 1)` | gl-ranged-eval, goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#35 | **PRESERVED** |
| 36 | L2144–L2149 | QADVANTAGE @ L2057 | `(defrule     (true)` | gl-ranged-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#36 | **PRESERVED** |
| 37 | L2152–L2161 | QADVANTAGE @ L2057 | `(defrule     (true)     (false)` | goal6, goal7 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#37 | **PRESERVED** |
| 38 | L2163–L2177 | QADVANTAGE @ L2057 | `(defrule     (false)     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)     (up-get-object-data object-data-pierce-armor goal6)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#38 | **PRESERVED** |
| 39 | L2179–L2184 | QADVANTAGE @ L2057 | `(defrule     (false)     (players-unit-type-count target-player skirmisher >= 6)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#39 | **PRESERVED** |
| 40 | L2186–L2195 | QADVANTAGE @ L2057 | `(defrule     (false)     (goal SPLIT 1)     (up-compare-goal gl-armor-advantage >= 1)` | gl-armor-advantage, gl-ranged-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#40 | **PRESERVED** |
| 41 | L2197–L2206 | QADVANTAGE @ L2057 | `(defrule     (false)     (goal SPLIT 1)     (up-compare-goal gl-armor-advantage < 1)` | gl-armor-advantage, gl-ranged-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#41 | **PRESERVED** |
| 42 | L2208–L2213 | QADVANTAGE @ L2057 | `(defrule     (true)     (false)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#42 | **PRESERVED** |
| 43 | L2217–L2223 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal6, goal7, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#43 | **PRESERVED** |
| 44 | L2226–L2234 | QADVANTAGE @ L2057 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#44 | **PRESERVED** |
| 45 | L2237–L2243 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 46 | L2245–L2257 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)` | gl-range-advantage, goal7, split | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#46 | **PRESERVED** |
| 47 | L2259–L2268 | QADVANTAGE @ L2057 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-range-advantage >= 1)` | gl-range-advantage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#47 | **PRESERVED** |
| 48 | L2270–L2279 | QADVANTAGE @ L2057 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-range-advantage < 1)` | gl-range-advantage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#48 | **PRESERVED** |
| 49 | L2281–L2285 | QADVANTAGE @ L2057 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 50 | L2288–L2297 | QADVANTAGE @ L2057 | `(defrule     (false)     (unit-type-count scout-cavalry-line > 0)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#50 | **PRESERVED** |
| 51 | L2299–L2305 | QADVANTAGE @ L2057 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 52 | L2308–L2326 | QADVANTAGE @ L2057 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 53 | L2330–L2336 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal, goal6 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#53 | **PRESERVED** |
| 54 | L2338–L2344 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal goal < 1)     (up-compare-goal gl-enemy-group-size < 5)` | gl-ranged-eval, goal6 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#54 | **PRESERVED** |
| 55 | L2347–L2353 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal, goal5 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#55 | **PRESERVED** |
| 56 | L2355–L2361 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal goal < 1)     (up-group-size c: RangedGroup < 5)` | gl-ranged-eval, goal5 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#56 | **PRESERVED** |
| 57 | L2366–L2375 | QADVANTAGE @ L2057 | `(defrule     (players-unit-type-count any-ally knight-line > 0)` | goal1, rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#57 | **PRESERVED** |
| 58 | L2378–L2385 | QADVANTAGE @ L2057 | `(defrule     (stance-toward focus-player ally)     (players-unit-type-count any-ally knight-line > 0)` | goal1 | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#58 | **PRESERVED** |
| 59 | L2388–L2394 | QADVANTAGE @ L2057 | `(defrule     (player-valid focus-player)     (players-unit-type-count any-ally knight-line > 0)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#59 | **PRESERVED** |
| 60 | L2396–L2402 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal goal1 > 0)     (players-unit-type-count any-ally knight-line > 0)` | gl-ranged-eval, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#60 | **PRESERVED** |
| 61 | L2405–L2410 | QADVANTAGE @ L2057 | `(defrule     (true)` | goal, lt | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#61 | **PRESERVED** |
| 62 | L2412–L2422 | QADVANTAGE @ L2057 | `(defrule     (unit-type-count knight-line > 0)` | goal | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#62 | **PRESERVED** |
| 63 | L2424–L2430 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal lt > 0)     (unit-type-count knight-line > 0)     (research-completed ri-chain-barding)` | goal | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#63 | **PRESERVED** |
| 64 | L2432–L2437 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal lt > 0)     (unit-type-count knight-line > 0)` | gl-ranged-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#64 | **PRESERVED** |
| 65 | L2440–L2448 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal gl-enemy-group-size > 0)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#65 | **PRESERVED** |
| 66 | L2450–L2455 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal lt > 0)` | gl-ranged-eval, lt | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#66 | **PRESERVED** |
| 67 | L2459–L2464 | QADVANTAGE @ L2057 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#67 | **PRESERVED** |
| 68 | L2467–L2473 | QADVANTAGE @ L2057 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#68 | **PRESERVED** |
| 69 | L2476–L2482 | QADVANTAGE @ L2057 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | up-get-search-state | up-get-search-state | -2 | ShadowByzantine/ShadowByzantine.per#69 | **PRESERVED** |
| 70 | L2484–L2488 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt < 1)` | rt | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#70 | **PRESERVED** |
| 71 | L2490–L2496 | QADVANTAGE @ L2057 | `(defrule     (up-compare-goal rt >= 1)` | gl-ranged-eval, rt | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#71 | **PRESERVED** |
| 72 | L2499–L2517 | QADVANTAGE @ L2057 | `(defrule     (taunt-detected me 59)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#72 | **PRESERVED** |
| 73 | L2519–L2524 | QADVANTAGE @ L2057 | `(defrule     (taunt-detected me 60)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#73 | **PRESERVED** |
| 74 | L2526–L2531 | QADVANTAGE @ L2057 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#74 | **PRESERVED** |
| 75 | L2536–L2540 | QNA @ L2534 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 12 | ShadowByzantine/ShadowByzantine.per#75; ShadowByzantine/ShadowByzantine.per#1079 | **PRESERVED** |
| 76 | L2542–L2551 | QNA @ L2534 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#76 | **PRESERVED** |
| 77 | L2553–L2563 | QNA @ L2534 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#77 | **PRESERVED** |
| 78 | L2565–L2572 | QNA @ L2534 | `(defrule     (false)     (goal gl-can-move NO)     (up-compare-goal gl-target-distance g:> gl-ranged-group-range)` | gl-can-move | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#78 | **PRESERVED** |
| 79 | L2574–L2581 | QNA @ L2534 | `(defrule     (false)     (goal gl-can-move YES)     (up-compare-goal gl-target-distance g:<= gl-ranged-group-range)` | gl-can-move | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#79 | **PRESERVED** |
| 80 | L2590–L2598 | QNA @ L2534 | `(defrule     (up-compare-goal gl-can-fire != YES)     (up-compare-goal gl-highest-next-attack <= firing-threshold-1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#80 | **PRESERVED** |
| 81 | L2600–L2609 | QNA @ L2534 | `(defrule     (timer-triggered t-failsafe)     (up-compare-goal gl-can-fire != YES)     (up-compare-goal gl-target-distance g:<= gl-ranged-group-range)` | — | t-failsafe | — | — | — | — | ShadowByzantine/ShadowByzantine.per#81 | **PRESERVED** |
| 82 | L2611–L2618 | QNA @ L2534 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 83 | L2621–L2629 | QNA @ L2534 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 84 | L2631–L2639 | QNA @ L2534 | `(defrule     (timer-triggered t-failsafe)     (up-compare-goal gl-can-move != YES)` | — | t-failsafe | — | — | — | — | ShadowByzantine/ShadowByzantine.per#84 | **PRESERVED** |
| 85 | L2641–L2649 | QNA @ L2534 | `(defrule     (taunt-detected me 63)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#85 | **PRESERVED** |
| 86 | L2651–L2656 | QNA @ L2534 | `(defrule     (taunt-detected me 64)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#86 | **PRESERVED** |
| 87 | L2658–L2664 | QNA @ L2534 | `(defrule     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#87; ShadowByzantine/ShadowByzantine.per#236; ShadowByzantine/ShadowByzantine.per#300 | **PRESERVED** |
| 88 | L2667–L2671 | QTARGET STUFF @ L2666 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 56 | ShadowByzantine/ShadowByzantine.per#88 | **PRESERVED** |
| 89 | L2673–L2686 | QTARGET STUFF @ L2666 | `(defrule     (true)` | gl-target-class, gl-target-distance, gl-target-hp, gl-target-type, goal, rt, target-id, target-x, target-y | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#89 | **PRESERVED** |
| 90 | L2690–L2703 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)` | goal, sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#90 | **PRESERVED** |
| 91 | L2707–L2711 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 92 | L2714–L2725 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)     (up-compare-goal gl-ranged-eval >= WinningFight)     (up-compare-goal gl-ranged-group-state != M...` | split | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#92 | **PRESERVED** |
| 93 | L2727–L2734 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#93 | **PRESERVED** |
| 94 | L2736–L2743 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#94 | **PRESERVED** |
| 95 | L2745–L2750 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#95; ShadowByzantine/ShadowByzantine.per#142; ShadowByzantine/ShadowByzantine.per#847 | **PRESERVED** |
| 96 | L2753–L2759 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -5 | ShadowByzantine/ShadowByzantine.per#96; ShadowByzantine/ShadowByzantine.per#102; ShadowByzantine/ShadowByzantine.per#108 | **PRESERVED** |
| 97 | L2763–L2767 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 98 | L2770–L2778 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#98 | **PRESERVED** |
| 99 | L2780–L2787 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#99; ShadowByzantine/ShadowByzantine.per#105 | **PRESERVED** |
| 100 | L2789–L2796 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#100; ShadowByzantine/ShadowByzantine.per#106; ShadowByzantine/ShadowByzantine.per#123 | **PRESERVED** |
| 101 | L2798–L2805 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#101; ShadowByzantine/ShadowByzantine.per#107; ShadowByzantine/ShadowByzantine.per#124 | **PRESERVED** |
| 102 | L2808–L2814 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -5 | ShadowByzantine/ShadowByzantine.per#96; ShadowByzantine/ShadowByzantine.per#102; ShadowByzantine/ShadowByzantine.per#108 | **PRESERVED** |
| 103 | L2818–L2822 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 104 | L2825–L2835 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | goal, split | — | — | up-find-remote, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#104 | **PRESERVED** |
| 105 | L2837–L2844 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#99; ShadowByzantine/ShadowByzantine.per#105 | **PRESERVED** |
| 106 | L2846–L2853 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#100; ShadowByzantine/ShadowByzantine.per#106; ShadowByzantine/ShadowByzantine.per#123 | **PRESERVED** |
| 107 | L2855–L2862 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#101; ShadowByzantine/ShadowByzantine.per#107; ShadowByzantine/ShadowByzantine.per#124 | **PRESERVED** |
| 108 | L2865–L2871 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -5 | ShadowByzantine/ShadowByzantine.per#96; ShadowByzantine/ShadowByzantine.per#102; ShadowByzantine/ShadowByzantine.per#108 | **PRESERVED** |
| 109 | L2875–L2879 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 110 | L2882–L2895 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#110 | **PRESERVED** |
| 111 | L2897–L2905 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (goal gl-ranged-group-state MINI-RETREAT)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#111 | **PRESERVED** |
| 112 | L2907–L2915 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-ranged-group-state != MINI-RETREAT)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#112 | **PRESERVED** |
| 113 | L2918–L2924 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -4 | ShadowByzantine/ShadowByzantine.per#113 | **PRESERVED** |
| 114 | L2928–L2932 | QTARGET STUFF @ L2666 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 115 | L2935–L2942 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#115 | **PRESERVED** |
| 116 | L2944–L2953 | QTARGET STUFF @ L2666 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#116 | **PRESERVED** |
| 117 | L2956–L2962 | QTARGET STUFF @ L2666 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | ShadowByzantine/ShadowByzantine.per#117 | **PRESERVED** |
| 118 | L2967–L2971 | QUICKIES @ L2964 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 119 | L2974–L2992 | QUICKIES @ L2964 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#119 | **PRESERVED** |
| 120 | L2994–L2998 | QUICKIES @ L2964 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#120; ShadowByzantine/ShadowByzantine.per#136; ShadowByzantine/ShadowByzantine.per#1777 | **PRESERVED** |
| 121 | L3000–L3004 | QUICKIES @ L2964 | `(defrule     (goal gl-switch 1)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#121; ShadowByzantine/ShadowByzantine.per#129; ShadowByzantine/ShadowByzantine.per#137 | **PRESERVED** |
| 122 | L3006–L3013 | QUICKIES @ L2964 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#122; ShadowByzantine/ShadowByzantine.per#130; ShadowByzantine/ShadowByzantine.per#138 | **PRESERVED** |
| 123 | L3015–L3022 | QUICKIES @ L2964 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#100; ShadowByzantine/ShadowByzantine.per#106; ShadowByzantine/ShadowByzantine.per#123 | **PRESERVED** |
| 124 | L3024–L3031 | QUICKIES @ L2964 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#101; ShadowByzantine/ShadowByzantine.per#107; ShadowByzantine/ShadowByzantine.per#124 | **PRESERVED** |
| 125 | L3034–L3040 | QUICKIES @ L2964 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -7 | ShadowByzantine/ShadowByzantine.per#125; ShadowByzantine/ShadowByzantine.per#133 | **PRESERVED** |
| 126 | L3045–L3049 | QUICKIES @ L3042 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 127 | L3052–L3062 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#127 | **PRESERVED** |
| 128 | L3064–L3068 | QUICKIES @ L3042 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#128 | **PRESERVED** |
| 129 | L3070–L3074 | QUICKIES @ L3042 | `(defrule     (goal gl-switch 1)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#121; ShadowByzantine/ShadowByzantine.per#129; ShadowByzantine/ShadowByzantine.per#137 | **PRESERVED** |
| 130 | L3076–L3083 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#122; ShadowByzantine/ShadowByzantine.per#130; ShadowByzantine/ShadowByzantine.per#138 | **PRESERVED** |
| 131 | L3085–L3092 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#100; ShadowByzantine/ShadowByzantine.per#106; ShadowByzantine/ShadowByzantine.per#123 | **PRESERVED** |
| 132 | L3094–L3101 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)` | split | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#101; ShadowByzantine/ShadowByzantine.per#107; ShadowByzantine/ShadowByzantine.per#124 | **PRESERVED** |
| 133 | L3104–L3110 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -7 | ShadowByzantine/ShadowByzantine.per#125; ShadowByzantine/ShadowByzantine.per#133 | **PRESERVED** |
| 134 | L3115–L3119 | QUICKIES @ L3042 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 135 | L3122–L3130 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (stance-toward focus-player enemy)` | split | — | — | up-find-remote, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#135 | **PRESERVED** |
| 136 | L3132–L3136 | QUICKIES @ L3042 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#120; ShadowByzantine/ShadowByzantine.per#136; ShadowByzantine/ShadowByzantine.per#1777 | **PRESERVED** |
| 137 | L3138–L3142 | QUICKIES @ L3042 | `(defrule     (goal gl-switch 1)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#121; ShadowByzantine/ShadowByzantine.per#129; ShadowByzantine/ShadowByzantine.per#137 | **PRESERVED** |
| 138 | L3144–L3151 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#122; ShadowByzantine/ShadowByzantine.per#130; ShadowByzantine/ShadowByzantine.per#138 | **PRESERVED** |
| 139 | L3153–L3160 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#100; ShadowByzantine/ShadowByzantine.per#106; ShadowByzantine/ShadowByzantine.per#123 | **PRESERVED** |
| 140 | L3162–L3169 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#140 | **PRESERVED** |
| 141 | L3171–L3178 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#141 | **PRESERVED** |
| 142 | L3180–L3185 | QUICKIES @ L3042 | `(defrule     (goal SPLIT 1)` | split | — | — | up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#95; ShadowByzantine/ShadowByzantine.per#142; ShadowByzantine/ShadowByzantine.per#847 | **PRESERVED** |
| 143 | L3188–L3194 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -9 | ShadowByzantine/ShadowByzantine.per#143 | **PRESERVED** |
| 144 | L3197–L3202 | QUICKIES @ L3042 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#144 | **PRESERVED** |
| 145 | L3205–L3216 | QUICKIES @ L3042 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#145 | **PRESERVED** |
| 146 | L3219–L3224 | QUICKIES @ L3042 | `(defrule     (taunt-detected me 61)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#146 | **PRESERVED** |
| 147 | L3226–L3237 | QUICKIES @ L3042 | `(defrule     (taunt-detected me 61)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#147 | **PRESERVED** |
| 148 | L3239–L3244 | QUICKIES @ L3042 | `(defrule     (taunt-detected me 62)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#148 | **PRESERVED** |
| 149 | L3247–L3257 | QMISC @ L3246 | `(defrule     (goal gl-thirty-turn 1)     (current-age >= feudal-age)` | split | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#149 | **PRESERVED** |
| 150 | L3259–L3270 | QMISC @ L3246 | `(defrule     (goal SPLIT 1)     (up-compare-goal lt > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#150 | **PRESERVED** |
| 151 | L3272–L3276 | QMISC @ L3246 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#151; ShadowByzantine/ShadowByzantine.per#931; ShadowByzantine/ShadowByzantine.per#977 | **PRESERVED** |
| 152 | L3280–L3286 | QMISC @ L3246 | `(defrule     (players-building-type-count every-enemy town-center < 1)` | nearest-tc-x, nearest-tc-y | — | — | — | — | 12 | ShadowByzantine/ShadowByzantine.per#152 | **PRESERVED** |
| 153 | L3288–L3292 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 5 | ShadowByzantine/ShadowByzantine.per#153 | **PRESERVED** |
| 154 | L3295–L3304 | QMISC @ L3246 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#154 | **PRESERVED** |
| 155 | L3307–L3313 | QMISC @ L3246 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 156 | L3316–L3322 | QMISC @ L3246 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 157 | L3324–L3329 | QMISC @ L3246 | `(defrule     (up-compare-goal rt >= 1)` | — | — | — | up-clean-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#157 | **PRESERVED** |
| 158 | L3331–L3339 | QMISC @ L3246 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#158 | **PRESERVED** |
| 159 | L3343–L3349 | QMISC @ L3246 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#159 | **PRESERVED** |
| 160 | L3352–L3356 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | ShadowByzantine/ShadowByzantine.per#160 | **PRESERVED** |
| 161 | L3359–L3365 | QMISC @ L3246 | `(defrule     (false)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#161 | **PRESERVED** |
| 162 | L3367–L3372 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | up-clean-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#162 | **PRESERVED** |
| 163 | L3374–L3379 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup >= 1)` | — | — | — | up-clean-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#163 | **PRESERVED** |
| 164 | L3381–L3386 | QMISC @ L3246 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#164 | **PRESERVED** |
| 165 | L3388–L3392 | QMISC @ L3246 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 34 | ShadowByzantine/ShadowByzantine.per#165 | **PRESERVED** |
| 166 | L3395–L3402 | QMISC @ L3246 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (players-building-type-count every-enemy castle < 1))` | nearest-castle-x, nearest-castle-y | — | — | — | — | 5 | ShadowByzantine/ShadowByzantine.per#166 | **PRESERVED** |
| 167 | L3405–L3411 | QMISC @ L3246 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#167; ShadowByzantine/ShadowByzantine.per#173 | **PRESERVED** |
| 168 | L3414–L3418 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | ShadowByzantine/ShadowByzantine.per#168 | **PRESERVED** |
| 169 | L3421–L3426 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 170 | L3428–L3433 | QMISC @ L3246 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#170; ShadowByzantine/ShadowByzantine.per#176 | **PRESERVED** |
| 171 | L3435–L3440 | QMISC @ L3246 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#171 | **PRESERVED** |
| 172 | L3443–L3450 | QMISC @ L3246 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (players-building-type-count every-enemy watch-tower < 1))` | nearest-tower-x, nearest-tower-y | — | — | — | — | 5 | ShadowByzantine/ShadowByzantine.per#172 | **PRESERVED** |
| 173 | L3453–L3459 | QMISC @ L3246 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#167; ShadowByzantine/ShadowByzantine.per#173 | **PRESERVED** |
| 174 | L3462–L3466 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | ShadowByzantine/ShadowByzantine.per#174 | **PRESERVED** |
| 175 | L3469–L3474 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 176 | L3476–L3481 | QMISC @ L3246 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#170; ShadowByzantine/ShadowByzantine.per#176 | **PRESERVED** |
| 177 | L3483–L3488 | QMISC @ L3246 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#177 | **PRESERVED** |
| 178 | L3492–L3498 | QMISC @ L3246 | `(defrule     (true)` | gl-mangos-nearby, goal, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#178 | **PRESERVED** |
| 179 | L3501–L3510 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-mangos-nearby | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#179 | **PRESERVED** |
| 180 | L3513–L3518 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 181 | L3522–L3527 | QMISC @ L3246 | `(defrule     (true)` | gl-units-in-close-range, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#181 | **PRESERVED** |
| 182 | L3530–L3544 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-units-in-close-range | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#182 | **PRESERVED** |
| 183 | L3547–L3552 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 184 | L3556–L3562 | QMISC @ L3246 | `(defrule     (true)` | gl-total-military-in-range, gl-total-units-in-range, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#184 | **PRESERVED** |
| 185 | L3565–L3580 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-total-military-in-range, gl-total-units-in-range | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#185 | **PRESERVED** |
| 186 | L3583–L3588 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 187 | L3590–L3603 | QMISC @ L3246 | `(defrule     (taunt-detected me 50)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#187 | **PRESERVED** |
| 188 | L3605–L3610 | QMISC @ L3246 | `(defrule     (taunt-detected me 51)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#188 | **PRESERVED** |
| 189 | L3612–L3616 | QMISC @ L3246 | `(defrule     (false)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#189 | **PRESERVED** |
| 190 | L3618–L3624 | QMISC @ L3246 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 191 | L3627–L3633 | QMISC @ L3246 | `(defrule     (true)` | gl-melee-in-range, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#191 | **PRESERVED** |
| 192 | L3636–L3649 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | gl-melee-in-range, split | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#192 | **PRESERVED** |
| 193 | L3651–L3661 | QMISC @ L3246 | `(defrule     (goal SPLIT 1)` | gl-melee-in-range | — | — | up-find-remote, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#193 | **PRESERVED** |
| 194 | L3664–L3671 | QMISC @ L3246 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#194 | **PRESERVED** |
| 195 | L3674–L3679 | QMISC @ L3246 | `(defrule     (true)` | gl-cavalry-attacking, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#195 | **PRESERVED** |
| 196 | L3682–L3696 | QMISC @ L3246 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#196 | **PRESERVED** |
| 197 | L3699–L3704 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 198 | L3707–L3712 | QMISC @ L3246 | `(defrule     (true)` | gl-enemy-group-size, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#198 | **PRESERVED** |
| 199 | L3715–L3728 | QMISC @ L3246 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 200 | L3731–L3736 | QMISC @ L3246 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 201 | L3739–L3749 | QMISC @ L3246 | `(defrule     (game-time > 5)     (or	(taunt-detected me 19)     (taunt-detected any-enemy 19))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#201 | **PRESERVED** |
| 202 | L3752–L3763 | QMPOINTS @ L3751 | `(defrule     (goal gl-tenth-turn 1)     (taunt-detected me 89)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#202 | **PRESERVED** |
| 203 | L3765–L3770 | QMPOINTS @ L3751 | `(defrule     (taunt-detected me 90)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#203 | **PRESERVED** |
| 204 | L3773–L3778 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingFour)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#204 | **PRESERVED** |
| 205 | L3780–L3785 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingThree)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#205 | **PRESERVED** |
| 206 | L3787–L3792 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingTwo)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#206 | **PRESERVED** |
| 207 | L3794–L3799 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (goal gl-march-type MarchingOne)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#207 | **PRESERVED** |
| 208 | L3802–L3811 | QMPOINTS @ L3751 | `(defrule     (game-time < 1500)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#208 | **PRESERVED** |
| 209 | L3813–L3822 | QMPOINTS @ L3751 | `(defrule     (goal gl-defend-town NO)     (up-group-size c: RangedGroup > 0)     (up-point-distance march-x home-x < 3)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#209 | **PRESERVED** |
| 210 | L3825–L3836 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-march-type == DefendingLC)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#210 | **PRESERVED** |
| 211 | L3838–L3849 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-set-target-object search-local c: 0)     (up-compare-goal gl-march-type == DefendingLC)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#211 | **PRESERVED** |
| 212 | L3851–L3862 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-march-type == DefendingMill)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#212 | **PRESERVED** |
| 213 | L3864–L3875 | QMPOINTS @ L3751 | `(defrule     (goal gl-attacking NO)     (up-group-size c: RangedGroup > 0)     (up-set-target-object search-local c: 0)     (up-compare-goal gl-march-type == DefendingMill)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#213 | **PRESERVED** |
| 214 | L3878–L3890 | QMPOINTS @ L3751 | `(defrule     (game-time > 2)     (goal gl-tenth-turn 1)     (players-building-type-count target-player town-center > 0)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#214 | **PRESERVED** |
| 215 | L3892–L3909 | QMPOINTS @ L3751 | `(defrule     (game-time > 5)     (goal gl-attacking YES)     (goal gl-thirty-turn 1)     (players-building-count target-player > 0)     (players-building-type-count target-playe...` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#215 | **PRESERVED** |
| 216 | L3911–L3927 | QMPOINTS @ L3751 | `(defrule     (game-time > 5)     (goal gl-attacking NO)     (goal gl-thirty-turn 1)     (players-building-count target-player > 0)     (players-building-type-count target-player...` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#216 | **PRESERVED** |
| 217 | L3930–L3941 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 218 | L3943–L3955 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 219 | L3957–L3969 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 220 | L3971–L3982 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 221 | L3984–L3992 | QMPOINTS @ L3751 | `(defrule     (or	(game-time < 5)     (or	(goal gl-defend-town YES)     (or	(goal gl-attacking NO)     (or	(players-building-type-count target-player town-center < 1)     (up-gro...` | — | — | — | — | — | 12 | ShadowByzantine/ShadowByzantine.per#221 | **PRESERVED** |
| 222 | L3995–L4006 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 223 | L4008–L4016 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#223 | **PRESERVED** |
| 224 | L4018–L4029 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 225 | L4031–L4039 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 226 | L4041–L4049 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#226 | **PRESERVED** |
| 227 | L4052–L4066 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 228 | L4068–L4079 | QMPOINTS @ L3751 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 229 | L4081–L4088 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type, split | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#229 | **PRESERVED** |
| 230 | L4091–L4097 | QMPOINTS @ L3751 | `(defrule     (goal gl-march-type MarchingTwo)     (or (taunt-detected me 85)     (up-point-distance ranged-group-x march-x < 5))` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#230 | **PRESERVED** |
| 231 | L4099–L4106 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type, split | — | — | — | — | 2 | ShadowByzantine/ShadowByzantine.per#231 | **PRESERVED** |
| 232 | L4109–L4115 | QMPOINTS @ L3751 | `(defrule     (goal gl-march-type MarchingThree)     (or (taunt-detected me 85)     (up-point-distance ranged-group-x march-x < 5))` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#232 | **PRESERVED** |
| 233 | L4117–L4123 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | gl-march-type, split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#233 | **PRESERVED** |
| 234 | L4125–L4130 | QMPOINTS @ L3751 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#234 | **PRESERVED** |
| 235 | L4134–L4148 | QMINIS @ L4132 | `(defrule     (true)     (goal gl-fifth-turn 1)     (up-group-size c: RangedGroup < 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#235 | **PRESERVED** |
| 236 | L4150–L4165 | QMINIS @ L4132 | `(defrule     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#87; ShadowByzantine/ShadowByzantine.per#236; ShadowByzantine/ShadowByzantine.per#300 | **PRESERVED** |
| 237 | L4171–L4178 | QMINIS @ L4132 | `(defrule     (or	(game-time < 10)     (or	(goal gl-getting-sheep YES)     (or	(unit-type-count scout-cavalry-line < 1)     (goal NEWSCOUTING FINISHED))))` | — | — | — | — | — | 6 | ShadowByzantine/ShadowByzantine.per#237 | **PRESERVED** |
| 238 | L4180–L4188 | QMINIS @ L4132 | `(defrule     (goal gl-seventh-turn 1)     (up-compare-goal NEWSCOUTING >= 45)     (unit-type-count scout-cavalry-line > 0)     (up-point-distance saved-scout-x scout-x < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#238 | **PRESERVED** |
| 239 | L4190–L4201 | QMINIS @ L4132 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-scout-stuck 0)     (up-compare-goal NEWSCOUTING < 45)     (up-point-distance saved-scout-x scout-x < 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#239 | **PRESERVED** |
| 240 | L4203–L4217 | QMINIS @ L4132 | `(defrule     (goal gl-scout-stuck 2)     (up-timer-status 28 == timer-running)` | — | 28 | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#240 | **PRESERVED** |
| 241 | L4219–L4227 | QMINIS @ L4132 | `(defrule     (goal gl-scout-stuck 2)     (or	(timer-triggered 28)     (up-point-distance scout-x saved-scout-x >= 3))` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#241 | **PRESERVED** |
| 242 | L4229–L4238 | QMINIS @ L4132 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-scout-stuck 0)     (up-point-distance saved-scout-x scout-x >= 4)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#242 | **PRESERVED** |
| 243 | L4240–L4247 | QMINIS @ L4132 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-scout-stuck -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#243 | **PRESERVED** |
| 244 | L4250–L4256 | QMINIS @ L4132 | `(defrule     (taunt-detected me 103)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#244 | **PRESERVED** |
| 245 | L4258–L4263 | QMINIS @ L4132 | `(defrule     (taunt-detected me 103)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#245 | **PRESERVED** |
| 246 | L4265–L4270 | QMINIS @ L4132 | `(defrule     (taunt-detected me 104)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#246 | **PRESERVED** |
| 247 | L4277–L4283 | QMINIS @ L4132 | `(defrule     (building-type-count lumber-camp == 1)` | — | — | — | up-find-local, up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#247 | **PRESERVED** |
| 248 | L4285–L4297 | QMINIS @ L4132 | `(defrule     (building-type-count lumber-camp == 1)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#248 | **PRESERVED** |
| 249 | L4299–L4316 | QMINIS @ L4132 | `(defrule     (building-type-count lumber-camp == 1)     (up-set-target-object search-local c: 0)` | sn-focus-player-number | — | — | up-clean-search, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#249 | **PRESERVED** |
| 250 | L4319–L4326 | QMINIS @ L4132 | `(defrule     (false)     (building-type-count lumber-camp == 2)` | — | — | — | up-find-local, up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#250 | **PRESERVED** |
| 251 | L4328–L4341 | QMINIS @ L4132 | `(defrule     (false)     (building-type-count lumber-camp == 2)     (up-set-target-object search-local c: 0)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-set-target-object, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#251 | **PRESERVED** |
| 252 | L4343–L4361 | QMINIS @ L4132 | `(defrule     (false)     (building-type-count lumber-camp == 2)     (up-set-target-object search-local c: 0)` | sn-focus-player-number | — | — | up-clean-search, up-full-reset-search, up-set-target-object | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#252 | **PRESERVED** |
| 253 | L4364–L4381 | QMINIS @ L4132 | `(defrule     (current-age == castle-age)     (goal gl-current-build-item ESKIRMS)     (building-type-count archery-range >= 1)     (research-available ri-elite-skirmisher)     (...` | — | — | — | up-full-reset-search | research, research-pending, up-pending-objects, up-research | — | ShadowByzantine/ShadowByzantine.per#253 | **PRESERVED** |
| 254 | L4384–L4391 | QHOUSES @ L4383 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 255 | L4393–L4398 | QHOUSES @ L4383 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#255 | **PRESERVED** |
| 256 | L4400–L4408 | QHOUSES @ L4383 | `(defrule     (goal goal -1)` | — | — | — | up-full-reset-search, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#256 | **PRESERVED** |
| 257 | L4410–L4420 | QHOUSES @ L4383 | `(defrule     (goal goal -1)     (up-compare-goal lt >= 1)     (up-set-target-object search-local c: 0)` | split | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#257 | **PRESERVED** |
| 258 | L4422–L4438 | QHOUSES @ L4383 | `(defrule     (goal goal -1)     (goal SPLIT 1)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#258 | **PRESERVED** |
| 259 | L4440–L4453 | QHOUSES @ L4383 | `(defrule     (goal goal 0)     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | goal | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#259 | **PRESERVED** |
| 260 | L4455–L4472 | QHOUSES @ L4383 | `(defrule     (goal goal 1)     (up-compare-goal rt >= 3)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object, up-set-target-point | up-target-point | — | ShadowByzantine/ShadowByzantine.per#260 | **PRESERVED** |
| 261 | L4476–L4483 | QLC @ L4474 | `(defrule     (true)` | split | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#261 | **PRESERVED** |
| 262 | L4485–L4496 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-trees-around, sn-focus-player-number | — | — | up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#262 | **PRESERVED** |
| 263 | L4498–L4503 | QLC @ L4474 | `(defrule     (true)` | sn-lumber-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#263 | **PRESERVED** |
| 264 | L4505–L4516 | QLC @ L4474 | `(defrule     (game-time >= 90)     (goal gl-dark-build LumberFirst)     (up-compare-goal gl-trees-around < 12)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#264 | **PRESERVED** |
| 265 | L4518–L4523 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 1)` | sn-lumber-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#265 | **PRESERVED** |
| 266 | L4525–L4531 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 3)` | sn-lumber-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#266 | **PRESERVED** |
| 267 | L4533–L4539 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 4)` | sn-lumber-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#267 | **PRESERVED** |
| 268 | L4541–L4547 | QLC @ L4474 | `(defrule     (building-type-count lumber-camp >= 5)` | sn-lumber-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#268 | **PRESERVED** |
| 269 | L4549–L4556 | QLC @ L4474 | `(defrule     (taunt-detected me 97)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#269 | **PRESERVED** |
| 270 | L4558–L4563 | QLC @ L4474 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 271 | L4565–L4578 | QLC @ L4474 | `(defrule     (goal gl-lclerp -1)` | split | — | — | up-full-reset-search, up-set-target-object, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#271 | **PRESERVED** |
| 272 | L4580–L4596 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-lclerp, sn-focus-player-number, split | — | — | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-object | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#272 | **PRESERVED** |
| 273 | L4598–L4604 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)     (up-compare-goal rt < 7)` | gl-lclerp | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#273 | **PRESERVED** |
| 274 | L4606–L4611 | QLC @ L4474 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#274 | **PRESERVED** |
| 275 | L4613–L4620 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (up-compare-goal goal >= 2)` | — | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#275 | **PRESERVED** |
| 276 | L4622–L4628 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (up-compare-goal goal < 2)` | gl-lclerp | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#276 | **PRESERVED** |
| 277 | L4630–L4635 | QLC @ L4474 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 278 | L4637–L4647 | QLC @ L4474 | `(defrule     (goal gl-lclerp -1)` | split | — | — | up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#278 | **PRESERVED** |
| 279 | L4649–L4663 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-lclerp, sn-focus-player-number, split | — | — | up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#279 | **PRESERVED** |
| 280 | L4665–L4671 | QLC @ L4474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 281 | L4673–L4680 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)     (building-type-count lumber-camp < 2)     (up-point-distance point-x home-x < 15)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#281 | **PRESERVED** |
| 282 | L4682–L4688 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)     (up-compare-goal rt < 7)` | — | — | — | — | — | 2 | ShadowByzantine/ShadowByzantine.per#282 | **PRESERVED** |
| 283 | L4690–L4694 | QLC @ L4474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 284 | L4696–L4703 | QLC @ L4474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 285 | L4705–L4717 | QLC @ L4474 | `(defrule     (goal gl-lclerp 0)` | sn-focus-player-number, split | — | — | up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#285 | **PRESERVED** |
| 286 | L4719–L4730 | QLC @ L4474 | `(defrule     (goal SPLIT 1)` | gl-lclerp, split | — | — | up-clean-search, up-remove-objects, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#286 | **PRESERVED** |
| 287 | L4732–L4740 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (up-can-build-line 0 point-x c: palisade-wall)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#287 | **PRESERVED** |
| 288 | L4742–L4747 | QLC @ L4474 | `(defrule     (goal gl-lclerp 1)     (not(up-can-build-line gl-escrow-state point-x c: house))` | gl-lclerp | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#288 | **PRESERVED** |
| 289 | L4749–L4756 | QLC @ L4474 | `(defrule     (goal gl-lclerp 2)     (not(up-can-build-line gl-escrow-state point-x c: house))` | — | — | — | — | — | -1 | ShadowByzantine/ShadowByzantine.per#289 | **PRESERVED** |
| 290 | L4758–L4764 | QLC @ L4474 | `(defrule     (goal gl-lclerp 2)     (up-can-build-line gl-escrow-state point-x c: house)` | gl-lclerp | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#290 | **PRESERVED** |
| 291 | L4766–L4780 | QLC @ L4474 | `(defrule     (goal gl-lclerp 3)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | up-target-point | — | ShadowByzantine/ShadowByzantine.per#291 | **PRESERVED** |
| 292 | L4782–L4789 | QLC @ L4474 | `(defrule     (goal gl-lclerp 3)` | — | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#292 | **PRESERVED** |
| 293 | L4791–L4797 | QLC @ L4474 | `(defrule     (goal gl-lclerp 4)     (up-pending-objects c: lumber-camp < 1)` | gl-lclerp | — | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#293 | **PRESERVED** |
| 294 | L4803–L4808 | QANTI-TRUSH @ L4799 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#294; ShadowByzantine/ShadowByzantine.per#617; ShadowByzantine/ShadowByzantine.per#623 | **PRESERVED** |
| 295 | L4811–L4820 | QANTI-TRUSH @ L4799 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#295 | **PRESERVED** |
| 296 | L4823–L4829 | QANTI-TRUSH @ L4799 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 297 | L4831–L4837 | QANTI-TRUSH @ L4799 | `(defrule     (goal gl-trushed YES)     (up-compare-goal rt < 1)` | gl-trushed | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#297 | **PRESERVED** |
| 298 | L4839–L4855 | QANTI-TRUSH @ L4799 | `(defrule     (game-time < 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#298 | **PRESERVED** |
| 299 | L4857–L4861 | QANTI-TRUSH @ L4799 | `(defrule     (goal gl-trushed YES)` | — | — | — | — | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#299 | **PRESERVED** |
| 300 | L4864–L4869 | QGARRISONING TC @ L4863 | `(defrule     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#87; ShadowByzantine/ShadowByzantine.per#236; ShadowByzantine/ShadowByzantine.per#300 | **PRESERVED** |
| 301 | L4871–L4877 | QGARRISONING TC @ L4863 | `(defrule     (true)` | goal, goal1, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#301 | **PRESERVED** |
| 302 | L4879–L4889 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (stance-toward focus-player enemy)` | goal | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#302 | **PRESERVED** |
| 303 | L4891–L4899 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (up-compare-goal goal > 0)     (up-set-target-object search-remote c: 0)` | gl-saved-focus-player, split | — | — | up-set-target-object | — | 1 | ShadowByzantine/ShadowByzantine.per#303 | **PRESERVED** |
| 304 | L4901–L4907 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | ShadowByzantine/ShadowByzantine.per#304 | **PRESERVED** |
| 305 | L4909–L4918 | QGARRISONING TC @ L4863 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#305 | **PRESERVED** |
| 306 | L4920–L4925 | QGARRISONING TC @ L4863 | `(defrule     (goal SPLIT 1)     (unit-type-count sheep > 0)` | — | — | — | up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#306 | **PRESERVED** |
| 307 | L4927–L4931 | QGARRISONING TC @ L4863 | `(defrule     (true)` | — | — | — | up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#307 | **PRESERVED** |
| 308 | L4933–L4942 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc -1)     (up-compare-goal lt >= 1)     (up-compare-goal goal >= 1)` | — | — | — | — | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#308 | **PRESERVED** |
| 309 | L4944–L4953 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc 1)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#309 | **PRESERVED** |
| 310 | L4955–L4962 | QGARRISONING TC @ L4863 | `(defrule     (goal gl-garrison-tc 1)     (up-compare-goal rt < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#310 | **PRESERVED** |
| 311 | L4964–L4968 | QGARRISONING TC @ L4863 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 312 | L4972–L4976 | QVILLS @ L4970 | `(defrule     (goal enemy-attack-x -1)` | — | — | — | — | — | 9 | ShadowByzantine/ShadowByzantine.per#312 | **PRESERVED** |
| 313 | L4978–L4984 | QVILLS @ L4970 | `(defrule     (true)` | gl-enemy-attack-size, sn-focus-player-number | — | — | up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#313 | **PRESERVED** |
| 314 | L4986–L4997 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)` | gl-enemy-attack-size | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#314 | **PRESERVED** |
| 315 | L4999–L5004 | QVILLS @ L4970 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 316 | L5006–L5011 | QVILLS @ L4970 | `(defrule     (true)` | goal, lt | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#316 | **PRESERVED** |
| 317 | L5013–L5018 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 318 | L5020–L5031 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 319 | L5033–L5041 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#319; ShadowByzantine/ShadowByzantine.per#321 | **PRESERVED** |
| 320 | L5043–L5053 | QVILLS @ L4970 | `(defrule     (true)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#320 | **PRESERVED** |
| 321 | L5055–L5064 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#319; ShadowByzantine/ShadowByzantine.per#321 | **PRESERVED** |
| 322 | L5068–L5072 | QVILLS @ L4970 | `(defrule     (players-military-population every-enemy >= 17)` | — | — | — | — | — | 6 | ShadowByzantine/ShadowByzantine.per#322 | **PRESERVED** |
| 323 | L5075–L5081 | QVILLS @ L4970 | `(defrule     (true)` | goal, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#323 | **PRESERVED** |
| 324 | L5084–L5093 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 325 | L5096–L5102 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 326 | L5104–L5114 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 327 | L5116–L5132 | QVILLS @ L4970 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt >= 1)     (up-point-distance point-x home-x < 25)` | — | — | — | up-clean-search, up-find-remote, up-remove-objects, up-set-target-point | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#327 | **PRESERVED** |
| 328 | L5134–L5146 | QVILLS @ L4970 | `(defrule     (goal gl-skirm-vills 3)     (or	(goal gl-ninety-turn 1)     (or	(up-compare-goal lt < 1)     (up-point-distance point-x home-x >= 30)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#328 | **PRESERVED** |
| 329 | L5149–L5154 | QVILLS @ L4970 | `(defrule     (false)     (goal gl-town-safe YES)` | — | — | — | — | — | 8 | ShadowByzantine/ShadowByzantine.per#329 | **PRESERVED** |
| 330 | L5158–L5169 | QVILLS @ L4970 | `(defrule     (true)` | enemy-attack-x, enemy-attack-y, goal, goal1, point-x, point-y, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#330 | **PRESERVED** |
| 331 | L5171–L5175 | QVILLS @ L4970 | `(defrule     (current-age == feudal-age)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#331 | **PRESERVED** |
| 332 | L5177–L5181 | QVILLS @ L4970 | `(defrule     (current-age >= castle-age)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#332 | **PRESERVED** |
| 333 | L5183–L5191 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#333 | **PRESERVED** |
| 334 | L5193–L5203 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)     (up-set-target-object search-remote c: 0)` | goal1, point-x, point-y | — | — | up-get-search-state, up-set-target-object | up-get-object-data, up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#334 | **PRESERVED** |
| 335 | L5205–L5212 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt > 0)     (stance-toward focus-player enemy)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | ShadowByzantine/ShadowByzantine.per#335 | **PRESERVED** |
| 336 | L5214–L5219 | QVILLS @ L4970 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -4 | ShadowByzantine/ShadowByzantine.per#336 | **PRESERVED** |
| 337 | L5221–L5227 | QVILLS @ L4970 | `(defrule     (up-compare-goal goal1 > 0)` | point-x, point-y | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#337 | **PRESERVED** |
| 338 | L5231–L5238 | QVILLS @ L4970 | `(defrule     (true)` | goal, goal1, goal2, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#338 | **PRESERVED** |
| 339 | L5241–L5250 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#339 | **PRESERVED** |
| 340 | L5253–L5259 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 341 | L5261–L5276 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | goal, goal1, split | — | — | up-find-local, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#341 | **PRESERVED** |
| 342 | L5278–L5287 | QVILLS @ L4970 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#342 | **PRESERVED** |
| 343 | L5289–L5299 | QVILLS @ L4970 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal1 > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#343 | **PRESERVED** |
| 344 | L5301–L5309 | QVILLS @ L4970 | `(defrule     (taunt-detected me 30)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#344 | **PRESERVED** |
| 345 | L5311–L5316 | QVILLS @ L4970 | `(defrule     (taunt-detected me 31)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#345 | **PRESERVED** |
| 346 | L5318–L5322 | QVILLS @ L4970 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 347 | L5325–L5330 | QVILLS @ L4970 | `(defrule     (players-current-age-time every-enemy >= 60)     (players-current-age every-enemy >= castle-age)` | — | — | — | — | — | 8 | ShadowByzantine/ShadowByzantine.per#347 | **PRESERVED** |
| 348 | L5333–L5337 | QVILLS @ L4970 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 349 | L5340–L5353 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 350 | L5356–L5362 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 351 | L5364–L5379 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 352 | L5381–L5392 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt == 1)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#352 | **PRESERVED** |
| 353 | L5394–L5405 | QVILLS @ L4970 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt >= 1)     (up-point-distance point-x home-x < 25)` | split | — | — | up-clean-search, up-find-remote, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#353 | **PRESERVED** |
| 354 | L5407–L5421 | QVILLS @ L4970 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-point | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#354 | **PRESERVED** |
| 355 | L5423–L5436 | QVILLS @ L4970 | `(defrule     (goal gl-aggressive-vills 3)     (or	(goal gl-ninety-turn 1)     (or	(up-point-distance point-x home-x >= 30)     (and(up-compare-goal lt < 1)     (up-timer-status ...` | — | t-infantry-attack | — | — | — | — | ShadowByzantine/ShadowByzantine.per#355 | **PRESERVED** |
| 356 | L5440–L5445 | QVILLS @ L4970 | `(defrule     (or	(goal gl-aggressive-vills 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#356 | **PRESERVED** |
| 357 | L5448–L5453 | QVILLS @ L4970 | `(defrule     (true)` | goal2, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#357 | **PRESERVED** |
| 358 | L5456–L5466 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 359 | L5469–L5475 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 360 | L5477–L5490 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 361 | L5492–L5501 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 1)     (goal gl-aggressive-vills -1)` | — | — | — | up-clean-search, up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#361 | **PRESERVED** |
| 362 | L5503–L5513 | QVILLS @ L4970 | `(defrule     (up-compare-goal goal1 < 1)     (goal gl-aggressive-vills 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#362 | **PRESERVED** |
| 363 | L5516–L5520 | QVILLS @ L4970 | `(defrule     (players-current-age every-enemy >= castle-age)` | — | — | — | — | — | 5 | ShadowByzantine/ShadowByzantine.per#363 | **PRESERVED** |
| 364 | L5523–L5529 | QVILLS @ L4970 | `(defrule     (true)` | goal1, goal2, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#364 | **PRESERVED** |
| 365 | L5532–L5541 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 366 | L5544–L5550 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 367 | L5552–L5565 | QVILLS @ L4970 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 368 | L5567–L5576 | QVILLS @ L4970 | `(defrule     (up-compare-goal lt >= 2)     (goal gl-aggressive-vills -1)` | — | — | — | up-clean-search, up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#368 | **PRESERVED** |
| 369 | L5578–L5588 | QVILLS @ L4970 | `(defrule     (up-compare-goal goal1 < 1)     (goal gl-aggressive-vills 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#369 | **PRESERVED** |
| 370 | L5590–L5597 | QVILLS @ L4970 | `(defrule     (taunt-detected me 95)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#370 | **PRESERVED** |
| 371 | L5599–L5604 | QVILLS @ L4970 | `(defrule     (taunt-detected me 96)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#371 | **PRESERVED** |
| 372 | L5607–L5618 | QVILLS @ L4970 | `(defrule     (false)     (game-time > 5)     (up-compare-goal gl-threat-time < 1000)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#372 | **PRESERVED** |
| 373 | L5620–L5632 | QVILLS @ L4970 | `(defrule     (false)     (game-time > 5)     (goal gl-tenth-turn 1)     (up-compare-goal gl-threat-time < 1000)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#373 | **PRESERVED** |
| 374 | L5636–L5642 | QVILLS @ L4970 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#374 | **PRESERVED** |
| 375 | L5645–L5655 | QVILLS @ L4970 | `(defrule     (stance-toward focus-player enemy)     (players-unit-type-count focus-player battering-ram-line > 0)` | — | — | — | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#375 | **PRESERVED** |
| 376 | L5658–L5664 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 377 | L5666–L5683 | QVILLS @ L4970 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)     (players-unit-type-count focus-player battering-ram-line > 0)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-search-state, up-target-objects | — | ShadowByzantine/ShadowByzantine.per#377 | **PRESERVED** |
| 378 | L5687–L5700 | QSHEEP @ L5685 | `(defrule     (game-time < 300)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#378 | **PRESERVED** |
| 379 | L5703–L5708 | QSHEEP @ L5685 | `(defrule     (or	(up-compare-goal gl-current-sheep-count < 3)     (goal gl-sheep-scouting FINISHED))` | — | — | — | — | — | 11 | ShadowByzantine/ShadowByzantine.per#379 | **PRESERVED** |
| 380 | L5710–L5721 | QSHEEP @ L5685 | `(defrule     (up-compare-goal gl-current-sheep-count >= 3)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#380 | **PRESERVED** |
| 381 | L5723–L5728 | QSHEEP @ L5685 | `(defrule     (up-set-target-by-id g: sheep1-id)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#381 | **PRESERVED** |
| 382 | L5730–L5736 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal gl-sheep-scouting >= 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#382 | **PRESERVED** |
| 383 | L5738–L5746 | QSHEEP @ L5685 | `(defrule     (goal gl-sheep-scouting 0)     (up-point-distance point2-x home-x < 50)     (up-point-distance point2-x home-x >= 18)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#383 | **PRESERVED** |
| 384 | L5748–L5756 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#384 | **PRESERVED** |
| 385 | L5758–L5766 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#385 | **PRESERVED** |
| 386 | L5768–L5777 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#386 | **PRESERVED** |
| 387 | L5779–L5789 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-sheep-scouting 1)     (up-point-distance point-x point2-x < 3)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#387 | **PRESERVED** |
| 388 | L5791–L5803 | QSHEEP @ L5685 | `(defrule     (goal gl-fifth-turn 1)     (up-set-target-by-id g: sheep1-id)     (up-compare-goal gl-sheep-scouting < 2)     (up-compare-goal gl-sheep-scouting >= 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#388 | **PRESERVED** |
| 389 | L5805–L5818 | QSHEEP @ L5685 | `(defrule     (game-time >= 60)     (up-set-target-by-id g: sheep1-id)     (or	(game-time >= 200)     (and(game-time >= 122)     (up-compare-goal gl-current-sheep-count == 4)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#389 | **PRESERVED** |
| 390 | L5820–L5826 | QSHEEP @ L5685 | `(defrule     (false)     (goal gl-sheep-scouting 2)     (up-set-target-by-id g: sheep1-id)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#390 | **PRESERVED** |
| 391 | L5829–L5837 | QNEWSCOUTING @ L5828 | `(defrule     (true)     (or	(game-time < 2)     (or	(current-age > dark-age)     (or	(up-compare-goal NEWSCOUTING >= 50)     (up-timer-status 28 == timer-running))))` | — | 28 | — | — | — | 33 | ShadowByzantine/ShadowByzantine.per#391 | **PRESERVED** |
| 392 | L5839–L5844 | QNEWSCOUTING @ L5828 | `(defrule     (true)` | cross | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#392 | **PRESERVED** |
| 393 | L5846–L5855 | QNEWSCOUTING @ L5828 | `(defrule     (true)` | goal1, goal2, goal3, goal4 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#393 | **PRESERVED** |
| 394 | L5857–L5862 | QNEWSCOUTING @ L5828 | `(defrule     (up-point-distance scout-x home-x >= 32)` | goal2, goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#394 | **PRESERVED** |
| 395 | L5865–L5870 | QNEWSCOUTING @ L5828 | `(defrule     (game-time < 60)     (unit-type-count sheep < 4)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#395 | **PRESERVED** |
| 396 | L5872–L5883 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 200)     (up-gaia-type-count c: deer-class < 1)     (or	(game-time > 410)     (and(goal gl-sighted-boar-count 2)     (or (and(game-time > 320)     (up...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#396 | **PRESERVED** |
| 397 | L5885–L5894 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 398 | L5896–L5903 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 200)     (goal gl-sighted-boar-count 2)     (up-compare-goal gl-current-sheep-count < 7)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#398 | **PRESERVED** |
| 399 | L5905–L5911 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 400 | L5914–L5923 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 401 | L5925–L5938 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-scouting-switch -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#401 | **PRESERVED** |
| 402 | L5940–L5946 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal SPLIT 1)     (up-point-contains explo-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#402 | **PRESERVED** |
| 403 | L5948–L5954 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal SPLIT 1)     (up-point-distance scout-x explo-x >= 50)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#403 | **PRESERVED** |
| 404 | L5956–L5962 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal SPLIT 1)     (up-point-explored explo-x != explored-no)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#404 | **PRESERVED** |
| 405 | L5964–L5972 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 406 | L5974–L5987 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-scouting-switch 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#406 | **PRESERVED** |
| 407 | L5989–L5994 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-scouting-switch 0)     (up-timer-status t-direction-switch != timer-running)` | gl-scouting-switch | t-direction-switch | — | — | — | — | ShadowByzantine/ShadowByzantine.per#407 | **PRESERVED** |
| 408 | L5996–L6006 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 409 | L6009–L6019 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#409 | **PRESERVED** |
| 410 | L6022–L6029 | QNEWSCOUTING @ L5828 | `(defrule     (true)     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#410 | **PRESERVED** |
| 411 | L6031–L6037 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal gl-inside-forest 1)` | gl-inside-forest | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#411 | **PRESERVED** |
| 412 | L6039–L6046 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal gl-inside-forest -1)     (up-point-distance scout-x home-x >= MaxDistance)` | gl-inside-forest | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#412 | **PRESERVED** |
| 413 | L6048–L6054 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (goal gl-inside-forest 2)` | gl-inside-forest | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#413 | **PRESERVED** |
| 414 | L6056–L6061 | QNEWSCOUTING @ L5828 | `(defrule     (game-time < 100)     (up-point-contains explo-x c: tree-class)` | — | t-misc | — | — | — | — | ShadowByzantine/ShadowByzantine.per#414 | **PRESERVED** |
| 415 | L6063–L6068 | QNEWSCOUTING @ L5828 | `(defrule     (up-point-distance scout-x home-x >= 33)     (up-point-contains explo-x c: tree-class)` | — | t-misc | — | — | — | — | ShadowByzantine/ShadowByzantine.per#415 | **PRESERVED** |
| 416 | L6070–L6076 | QNEWSCOUTING @ L5828 | `(defrule     (up-point-contains explo-x c: tree-class)     (up-timer-status t-misc == timer-running)` | — | t-misc | — | — | — | — | ShadowByzantine/ShadowByzantine.per#416 | **PRESERVED** |
| 417 | L6079–L6092 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 418 | L6094–L6103 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 419 | L6105–L6117 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 420 | L6119–L6126 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 0)     (up-compare-goal goal >= 6)` | — | — | — | up-full-reset-search | up-target-point | — | ShadowByzantine/ShadowByzantine.per#420 | **PRESERVED** |
| 421 | L6128–L6134 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 0)     (up-compare-goal goal < 6)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#421 | **PRESERVED** |
| 422 | L6136–L6143 | QNEWSCOUTING @ L5828 | `(defrule     (or	(up-compare-goal explo-x >= 116)     (or	(up-compare-goal explo-y >= 116)     (or	(up-compare-goal explo-x < 4)     (up-compare-goal explo-y < 4))))` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#422 | **PRESERVED** |
| 423 | L6145–L6158 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 424 | L6160–L6168 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | newscouting, split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#424 | **PRESERVED** |
| 425 | L6171–L6176 | QNEWSCOUTING @ L5828 | `(defrule     (goal gl-fifth-turn 1)     (taunt-detected me 33)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#425 | **PRESERVED** |
| 426 | L6178–L6183 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 34)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#426 | **PRESERVED** |
| 427 | L6185–L6193 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (game-time > 10)     (up-compare-goal NEWSCOUTING < 50)     (up-point-distance scout-x home-x >= MaxDistance)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#427 | **PRESERVED** |
| 428 | L6195–L6204 | QNEWSCOUTING @ L5828 | `(defrule     (false)     (game-time > 10)     (up-compare-goal NEWSCOUTING < 50)     (up-point-distance explo-x home-x >= MaxDistance)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#428 | **PRESERVED** |
| 429 | L6206–L6222 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#429 | **PRESERVED** |
| 430 | L6224–L6230 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-second-turn 1)     (up-point-explored explo-x != explored-no)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#430 | **PRESERVED** |
| 431 | L6232–L6238 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-second-turn 1)     (up-point-contains explo-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#431 | **PRESERVED** |
| 432 | L6240–L6245 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 81)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#432 | **PRESERVED** |
| 433 | L6247–L6252 | QNEWSCOUTING @ L5828 | `(defrule     (taunt-detected me 82)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#433 | **PRESERVED** |
| 434 | L6254–L6263 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 300)     (up-compare-goal NEWSCOUTING < FINISHED)     (up-compare-goal gl-current-sheep-count < 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#434 | **PRESERVED** |
| 435 | L6265–L6272 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 47)     (up-compare-goal gl-current-sheep-count >= 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#435 | **PRESERVED** |
| 436 | L6274–L6284 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 80)     (up-gaia-type-count c: forage-bush < 5)     (up-gaia-type-count c: forage-bush >= 1)     (up-compare-goal NEWSCOUTING < FINISHED)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#436 | **PRESERVED** |
| 437 | L6286–L6301 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 48)     (goal gl-fifth-turn 1)` | sn-focus-player-number | — | — | up-find-local, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | up-target-point | — | ShadowByzantine/ShadowByzantine.per#437 | **PRESERVED** |
| 438 | L6303–L6310 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 48)     (up-gaia-type-count c: forage-bush >= 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#438 | **PRESERVED** |
| 439 | L6312–L6321 | QNEWSCOUTING @ L5828 | `(defrule     (game-time >= 290)     (up-compare-goal NEWSCOUTING < FINISHED)     (up-compare-goal gl-sighted-boar-count < 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#439 | **PRESERVED** |
| 440 | L6323–L6330 | QNEWSCOUTING @ L5828 | `(defrule     (goal NEWSCOUTING 49)     (up-compare-goal gl-sighted-boar-count >= 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#440 | **PRESERVED** |
| 441 | L6332–L6339 | QNEWSCOUTING @ L5828 | `(defrule     (up-compare-goal NEWSCOUTING < FINISHED)     (up-compare-goal gl-current-sheep-count >= 7)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#441 | **PRESERVED** |
| 442 | L6341–L6347 | QNEWSCOUTING @ L5828 | `(defrule     (or	(game-time < 200)     (or	(military-population > 5)     (up-timer-status 28 == timer-running)))` | — | 28 | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#442 | **PRESERVED** |
| 443 | L6349–L6360 | QNEWSCOUTING @ L5828 | `(defrule     (up-compare-goal NEWSCOUTING < 50)     (up-gaia-type-count c: deer-class > 0)     (or	(game-time > 410)     (and(goal gl-sighted-boar-count 2)     (or (and(game-tim...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#443 | **PRESERVED** |
| 444 | L6362–L6371 | QNEWSCOUTING @ L5828 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 445 | L6373–L6387 | QNEWSCOUTING @ L5828 | `(defrule     (true)     (up-timer-status 28 != timer-running)     (up-compare-goal NEWSCOUTING != FINISHED)     (or	(up-compare-goal NEWSCOUTING == 50)     (game-time s:> sn-hom...` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#445 | **PRESERVED** |
| 446 | L6389–L6397 | QNEWSCOUTING @ L5828 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-compare-goal NEWSCOUTING != FINISHED)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#446 | **PRESERVED** |
| 447 | L6399–L6404 | QNEWSCOUTING @ L5828 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#447 | **PRESERVED** |
| 448 | L6407–L6411 | QCIRCLE SCOUTING @ L6406 | `(defrule     (players-building-type-count target-player town-center > 0)` | — | — | — | — | — | 15 | ShadowByzantine/ShadowByzantine.per#448 | **PRESERVED** |
| 449 | L6414–L6418 | QCIRCLE SCOUTING @ L6406 | `(defrule     (up-compare-goal gl-strategy != FLUSH)` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#449 | **PRESERVED** |
| 450 | L6420–L6436 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-tenth-turn 1)     (players-building-type-count target-player farm < 1)     (players-building-type-count target-player house < 1)     (or	(players-building-...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#450 | **PRESERVED** |
| 451 | L6438–L6451 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-find-remote, up-set-target-object | up-target-point | — | ShadowByzantine/ShadowByzantine.per#451 | **PRESERVED** |
| 452 | L6453–L6473 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-tenth-turn 1)     (players-building-type-count target-player farm < 1)     (players-building-type-count target-player house > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#452 | **PRESERVED** |
| 453 | L6475–L6494 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-tenth-turn 1)     (military-population < 20)     (players-building-type-count target-player farm > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#453 | **PRESERVED** |
| 454 | L6497–L6513 | QCIRCLE SCOUTING @ L6406 | `(defrule     (true)     (false)` | goal, sn-focus-player-number, split | — | — | up-find-remote, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#454 | **PRESERVED** |
| 455 | L6516–L6521 | QCIRCLE SCOUTING @ L6406 | `(defrule     (or	(not(player-in-game any-ally))     (up-compare-goal gl-circle-direcion != -1))` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#455 | **PRESERVED** |
| 456 | L6523–L6536 | QCIRCLE SCOUTING @ L6406 | `(defrule     (game-time > 5)` | goal, sn-focus-player-number, split | — | — | up-find-remote, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#456 | **PRESERVED** |
| 457 | L6538–L6551 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#457 | **PRESERVED** |
| 458 | L6553–L6561 | QCIRCLE SCOUTING @ L6406 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 459 | L6563–L6571 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal1 g:> goal)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#459; ShadowByzantine/ShadowByzantine.per#463 | **PRESERVED** |
| 460 | L6574–L6579 | QCIRCLE SCOUTING @ L6406 | `(defrule     (or	(player-in-game any-ally)     (up-compare-goal gl-circle-direcion != -1))` | — | — | — | — | — | 3 | ShadowByzantine/ShadowByzantine.per#460 | **PRESERVED** |
| 461 | L6581–L6599 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-dlure FINISHED)     (unit-type-count scout-cavalry > 0)     (up-timer-status 28 != timer-running)` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#461 | **PRESERVED** |
| 462 | L6601–L6608 | QCIRCLE SCOUTING @ L6406 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 463 | L6610–L6617 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal1 g:> goal)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#459; ShadowByzantine/ShadowByzantine.per#463 | **PRESERVED** |
| 464 | L6620–L6624 | QCIRCLE SCOUTING @ L6406 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#464; ShadowByzantine/ShadowByzantine.per#685; ShadowByzantine/ShadowByzantine.per#834 | **PRESERVED** |
| 465 | L6626–L6630 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-circle-direcion COUNTERCLOCKWISE)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#465 | **PRESERVED** |
| 466 | L6632–L6636 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-circle-direcion CLOCKWISE)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#466 | **PRESERVED** |
| 467 | L6638–L6651 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal gl-twenty-turn 1)     (goal gl-dlure FINISHED)     (goal gl-strategy KRUSH)     (unit-type-count scout-cavalry > 0)     (up-timer-status 28 != timer-running) ...` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#467 | **PRESERVED** |
| 468 | L6653–L6670 | QCIRCLE SCOUTING @ L6406 | `(defrule     (player-valid 3)     (game-time < 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#468 | **PRESERVED** |
| 469 | L6672–L6690 | QCIRCLE SCOUTING @ L6406 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 470 | L6692–L6699 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)     (up-point-distance scout-x center-x >= max-circle-scout-distance)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#470 | **PRESERVED** |
| 471 | L6701–L6713 | QCIRCLE SCOUTING @ L6406 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#471 | **PRESERVED** |
| 472 | L6716–L6723 | QFORAGE @ L6715 | `(defrule     (building-type-count mill >= 1)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#472 | **PRESERVED** |
| 473 | L6725–L6736 | QFORAGE @ L6715 | `(defrule     (goal gl-tenth-turn 1)     (up-compare-goal BH < 1)     (building-type-count mill >= 1)     (unit-type-count villager-forager < 1)     (or	(and(unit-type-count shee...` | split | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#473 | **PRESERVED** |
| 474 | L6738–L6751 | QFORAGE @ L6715 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#474 | **PRESERVED** |
| 475 | L6753–L6765 | QFORAGE @ L6715 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#475 | **PRESERVED** |
| 476 | L6768–L6773 | QCOUNTING SHEEP @ L6767 | `(defrule     (true)` | gl-current-sheep-count, gl-new-sheep-count, gl-sheep-count-last | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#476 | **PRESERVED** |
| 477 | L6775–L6777 | QCOUNTING SHEEP @ L6767 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#477 | **PRESERVED** |
| 478 | L6779–L6789 | QCOUNTING SHEEP @ L6767 | `(defrule     (up-compare-goal gl-sheep-count g:> gl-sheep-count-last)     (dropsite-min-distance livestock-class < 8)     (building-type-count town-center > 0)` | gl-current-sheep-count, gl-new-sheep-count, gl-sheep-count-last | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#478 | **PRESERVED** |
| 479 | L6791–L6793 | QCOUNTING SHEEP @ L6767 | `(defrule     (up-compare-goal gl-sheep-count g:< gl-sheep-count-last)` | gl-sheep-count-last | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#479 | **PRESERVED** |
| 480 | L6796–L6811 | QDLURING @ L6795 | `(defrule     (true)     (or	(up-compare-goal gl-dlure == -1)     (up-compare-goal gl-deer-distance >= 20))     (or	(up-group-size c: RangedGroup >= 1)     (game-time s:> sn-home...` | sn-maximum-hunt-drop-distance, sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#480 | **PRESERVED** |
| 481 | L6813–L6822 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 482 | L6824–L6837 | QDLURING @ L6795 | `(defrule     (true)` | goal4, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#482 | **PRESERVED** |
| 483 | L6839–L6857 | QDLURING @ L6795 | `(defrule     (goal gl-deer-walking 3)` | goal4, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#483 | **PRESERVED** |
| 484 | L6859–L6867 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 485 | L6869–L6879 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 486 | L6881–L6889 | QDLURING @ L6795 | `(defrule     (up-compare-goal gl-dlure >= 0)     (up-compare-goal gl-deer-walking == -1)     (up-point-distance point2-x saved-x < 7)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#486 | **PRESERVED** |
| 487 | L6891–L6899 | QDLURING @ L6795 | `(defrule     (goal gl-deer-walking 0)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#487 | **PRESERVED** |
| 488 | L6901–L6914 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 489 | L6916–L6930 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 490 | L6932–L6942 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 491 | L6944–L6952 | QDLURING @ L6795 | `(defrule     (up-compare-goal goal1 > 0)     (up-set-target-by-id g: deer-id)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#491 | **PRESERVED** |
| 492 | L6954–L6963 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)     (or	(goal gl-fifth-turn 1)     (goal gl-fifth-turn 2))     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#492 | **PRESERVED** |
| 493 | L6965–L6976 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 494 | L6979–L6984 | QDLURING @ L6795 | `(defrule     (true)` | goal2, goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#494 | **PRESERVED** |
| 495 | L6986–L7003 | QDLURING @ L6795 | `(defrule     (true)` | sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#495 | **PRESERVED** |
| 496 | L7005–L7015 | QDLURING @ L6795 | `(defrule     (true)` | — | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#496 | **PRESERVED** |
| 497 | L7017–L7031 | QDLURING @ L6795 | `(defrule     (goal gl-tenth-turn 1)     (unit-type-count villager-forager >= 3)     (dropsite-min-distance live-boar >= 10)     (up-timer-status t-misc != timer-running)     (or...` | — | t-misc | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#497 | **PRESERVED** |
| 498 | L7033–L7043 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-find-remote, up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#498 | **PRESERVED** |
| 499 | L7045–L7061 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | gl-killed-deer-count, split | t-misc | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#499 | **PRESERVED** |
| 500 | L7063–L7068 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 501 | L7070–L7082 | QDLURING @ L6795 | `(defrule     (dropsite-min-distance live-boar >= 10)     (up-timer-status t-misc != timer-running)     (or	(up-compare-goal goal2 >= 1)     (and(up-compare-goal goal3 >= 1)     ...` | split | t-misc | — | — | research-pending, unit-type-count-total, up-research | — | ShadowByzantine/ShadowByzantine.per#501 | **PRESERVED** |
| 502 | L7084–L7102 | QDLURING @ L6795 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 503 | L7104–L7108 | QDLURING @ L6795 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#503; ShadowByzantine/ShadowByzantine.per#520; ShadowByzantine/ShadowByzantine.per#1601 | **PRESERVED** |
| 504 | L7110–L7122 | QDLURING @ L6795 | `(defrule     (up-compare-goal goal1 < 2)     (up-compare-goal gl-dlure >= 0)     (up-compare-goal gl-dlure != FINISHED)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#504 | **PRESERVED** |
| 505 | L7130–L7140 | QDLURING @ L6795 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 506 | L7142–L7158 | QDLURING @ L6795 | `(defrule     (taunt-detected me 73)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#506 | **PRESERVED** |
| 507 | L7160–L7166 | QDLURING @ L6795 | `(defrule     (taunt-detected me 73)     (goal gl-tenth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#507 | **PRESERVED** |
| 508 | L7168–L7173 | QDLURING @ L6795 | `(defrule     (taunt-detected me 74)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#508 | **PRESERVED** |
| 509 | L7175–L7180 | QBH @ L7174 | `(defrule     (true)` | goal1, goal7 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#509 | **PRESERVED** |
| 510 | L7182–L7188 | QBH @ L7174 | `(defrule     (true)` | gl-killed-boar-count, gl-sighted-boar-count | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#510 | **PRESERVED** |
| 511 | L7190–L7201 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 512 | L7204–L7213 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#512 | **PRESERVED** |
| 513 | L7215–L7223 | QBH @ L7174 | `(defrule     (or	(goal gl-town-safe NO)     (or	(up-compare-goal BH >= 2)     (or	(up-compare-goal lt > 0)     (or	(unit-type-count-total villager < 10)     (up-compare-goal gl-...` | — | — | — | — | unit-type-count-total | 6 | ShadowByzantine/ShadowByzantine.per#513 | **PRESERVED** |
| 514 | L7225–L7230 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 515 | L7232–L7241 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 516 | L7243–L7253 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 517 | L7255–L7263 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 518 | L7265–L7271 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 519 | L7273–L7279 | QBH @ L7174 | `(defrule     (true)     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#519 | **PRESERVED** |
| 520 | L7281–L7285 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#503; ShadowByzantine/ShadowByzantine.per#520; ShadowByzantine/ShadowByzantine.per#1601 | **PRESERVED** |
| 521 | L7288–L7300 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#521 | **PRESERVED** |
| 522 | L7302–L7315 | QBH @ L7174 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-hitpoints > 25)     (up-get-object-data object-data-target-id ...` | — | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#522 | **PRESERVED** |
| 523 | L7317–L7321 | QBH @ L7174 | `(defrule     (true)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#523 | **PRESERVED** |
| 524 | L7323–L7327 | QBH @ L7174 | `(defrule     (research-completed ri-loom)` | goal1 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#524 | **PRESERVED** |
| 525 | L7329–L7341 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#525 | **PRESERVED** |
| 526 | L7343–L7352 | QBH @ L7174 | `(defrule     (up-compare-goal rt > 0)     (up-set-target-by-id g: current-boar-id)     (up-get-object-data object-data-target-id goal)     (up-set-target-by-id g: goal)` | — | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#526 | **PRESERVED** |
| 527 | L7354–L7362 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 528 | L7364–L7376 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#528 | **PRESERVED** |
| 529 | L7378–L7388 | QBH @ L7174 | `(defrule     (goal SPLIT 1)     (up-compare-goal lt > 0)     (or	(up-object-data object-data-hitpoints g:< goal1)     (and(up-point-distance point2-x point-x < 1)     (up-point-...` | — | — | — | — | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#529 | **PRESERVED** |
| 530 | L7390–L7394 | QBH @ L7174 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 531 | L7397–L7410 | QBH @ L7174 | `(defrule     (true)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#531 | **PRESERVED** |
| 532 | L7412–L7419 | QBH @ L7174 | `(defrule     (up-compare-goal rt == 1)     (goal gl-sighted-boar-count 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#532 | **PRESERVED** |
| 533 | L7421–L7430 | QBH @ L7174 | `(defrule     (goal gl-sighted-boar-count 1)     (or	(up-compare-goal rl == 2)     (and(up-compare-goal rl == 1)     (up-compare-goal gl-killed-boar-count > 0)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#533 | **PRESERVED** |
| 534 | L7432–L7438 | QBH @ L7174 | `(defrule     (goal gl-town-safe NO)     (up-compare-goal BH > -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#534 | **PRESERVED** |
| 535 | L7440–L7450 | QBH @ L7174 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 536 | L7452–L7466 | QBH @ L7174 | `(defrule     (goal BH 0)` | bh, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#536 | **PRESERVED** |
| 537 | L7468–L7474 | QBH @ L7174 | `(defrule     (goal old-boar-id -1)     (up-compare-goal current-boar-id != -1)` | old-boar-id | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#537 | **PRESERVED** |
| 538 | L7476–L7484 | QBH @ L7174 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal BH == 3)     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#538 | **PRESERVED** |
| 539 | L7486–L7495 | QBH @ L7174 | `(defrule     (up-set-target-by-id g: current-boar-id)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#539 | **PRESERVED** |
| 540 | L7497–L7505 | QBH @ L7174 | `(defrule     (goal lt 0)     (or	(goal BH 2)     (goal BH 3))     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#540 | **PRESERVED** |
| 541 | L7507–L7514 | QBH @ L7174 | `(defrule     (goal goal1 -1)     (up-compare-goal BH == 3)     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#541 | **PRESERVED** |
| 542 | L7516–L7530 | QBH @ L7174 | `(defrule     (unit-type-count villager >= 9)     (up-compare-goal current-boar-id != -1)     (or	(goal BH 10)     (and(goal BH 1)     (dropsite-min-distance live-boar < 33)))   ...` | split | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | up-research | — | ShadowByzantine/ShadowByzantine.per#542 | **PRESERVED** |
| 543 | L7532–L7538 | QBH @ L7174 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal7 >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#543; ShadowByzantine/ShadowByzantine.per#546 | **PRESERVED** |
| 544 | L7540–L7555 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-object | up-get-object-data, up-target-objects | — | ShadowByzantine/ShadowByzantine.per#544 | **PRESERVED** |
| 545 | L7557–L7572 | QBH @ L7174 | `(defrule     (research-completed ri-loom)     (or	(unit-type-count sheep < 1)     (unit-type-count villager >= 9))     (up-compare-goal current-boar-id != -1)     (or	(goal BH 1...` | split | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#545 | **PRESERVED** |
| 546 | L7574–L7580 | QBH @ L7174 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal7 >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#543; ShadowByzantine/ShadowByzantine.per#546 | **PRESERVED** |
| 547 | L7582–L7597 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-object | up-get-object-data, up-target-objects | — | ShadowByzantine/ShadowByzantine.per#547 | **PRESERVED** |
| 548 | L7599–L7608 | QBH @ L7174 | `(defrule     (goal BH 2)     (goal gl-killed-boar-count 0)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-action == actionid-attack)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#548 | **PRESERVED** |
| 549 | L7610–L7619 | QBH @ L7174 | `(defrule     (goal BH 2)     (goal gl-killed-boar-count 1)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-action == actionid-attack)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#549 | **PRESERVED** |
| 550 | L7621–L7636 | QBH @ L7174 | `(defrule     (goal gl-fifth-turn 1)     (dropsite-min-distance live-boar < 4)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#550 | **PRESERVED** |
| 551 | L7638–L7656 | QBH @ L7174 | `(defrule     (goal SPLIT 1)` | gl-killed-boar-count, sn-focus-player-number | — | — | up-find-remote, up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#551 | **PRESERVED** |
| 552 | L7658–L7663 | QBH @ L7174 | `(defrule     (goal BH 4)     (dropsite-min-distance live-boar > 10)` | bh | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#552 | **PRESERVED** |
| 553 | L7668–L7674 | QBH @ L7174 | `(defrule     (false)     (up-set-target-by-id g: lurer-id)     (dropsite-min-distance live-boar < 10)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#553 | **PRESERVED** |
| 554 | L7676–L7682 | QBH @ L7174 | `(defrule     (false)     (up-set-target-by-id g: current-boar-id)     (dropsite-min-distance live-boar < 10)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#554 | **PRESERVED** |
| 555 | L7685–L7692 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-carry < 10)     (up-compare-goal gl-killed-boar-count >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#555 | **PRESERVED** |
| 556 | L7694–L7702 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: current-boar-id)` | — | — | — | up-find-local, up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#556 | **PRESERVED** |
| 557 | L7704–L7715 | QRETARGETING @ L7684 | `(defrule     (false)     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-carry >= 50)     (up-ob...` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#557 | **PRESERVED** |
| 558 | L7717–L7725 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 1)     (up-set-target-by-id g: current-boar-id)     (up-object-data object-data-hitpoints < 2)     (up-compare-goal...` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#558 | **PRESERVED** |
| 559 | L7727–L7736 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (dropsite-min-distance live-boar < 10)     (up-set-target-by-id g: current-boar-id)     (up-compare-goal gl-...` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#559 | **PRESERVED** |
| 560 | L7738–L7742 | QRETARGETING @ L7684 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#560; ShadowByzantine/ShadowByzantine.per#570 | **PRESERVED** |
| 561 | L7744–L7748 | QRETARGETING @ L7684 | `(defrule     (research-completed ri-loom)` | goal | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#561; ShadowByzantine/ShadowByzantine.per#571 | **PRESERVED** |
| 562 | L7750–L7759 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#562 | **PRESERVED** |
| 563 | L7761–L7767 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)     (up-set-target-by-id g: current-boar-id)     (up-get-object-data object-data-target-id goal1)` | — | — | — | up-remove-objects | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#563 | **PRESERVED** |
| 564 | L7769–L7781 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#564 | **PRESERVED** |
| 565 | L7783–L7790 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: old-boar-id)     (up-object-data object-data-carry < 10)     (up-compare-goal gl-killed-boar-count >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#565 | **PRESERVED** |
| 566 | L7792–L7800 | QRETARGETING @ L7684 | `(defrule     (up-set-target-by-id g: old-boar-id)     (up-compare-goal gl-killed-boar-count >= 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#566 | **PRESERVED** |
| 567 | L7802–L7813 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (up-set-target-by-id g: old-boar-id)     (up-object-data object-data-carry >= 50)     (up-object-data object...` | — | t-kill-boar | — | — | — | — | ShadowByzantine/ShadowByzantine.per#567 | **PRESERVED** |
| 568 | L7815–L7824 | QRETARGETING @ L7684 | `(defrule     (goal gl-fifth-turn 1)     (up-compare-goal lt < 1)     (up-set-target-by-id g: old-boar-id)     (up-object-data object-data-hitpoints < 2)     (up-compare-goal gl-...` | split | t-kill-boar | — | — | — | — | ShadowByzantine/ShadowByzantine.per#568 | **PRESERVED** |
| 569 | L7826–L7836 | QRETARGETING @ L7684 | `(defrule     (false)     (goal gl-fifth-turn 1)     (up-compare-goal lt < 4)     (dropsite-min-distance live-boar < 10)     (up-set-target-by-id g: current-boar-id)     (up-comp...` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#569 | **PRESERVED** |
| 570 | L7838–L7842 | QRETARGETING @ L7684 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#560; ShadowByzantine/ShadowByzantine.per#570 | **PRESERVED** |
| 571 | L7844–L7848 | QRETARGETING @ L7684 | `(defrule     (research-completed ri-loom)` | goal | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#561; ShadowByzantine/ShadowByzantine.per#571 | **PRESERVED** |
| 572 | L7850–L7859 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#572 | **PRESERVED** |
| 573 | L7861–L7867 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)     (up-set-target-by-id g: old-boar-id)     (up-get-object-data object-data-target-id goal1)` | — | — | — | up-remove-objects | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#573 | **PRESERVED** |
| 574 | L7869–L7880 | QRETARGETING @ L7684 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-objects | — | ShadowByzantine/ShadowByzantine.per#574 | **PRESERVED** |
| 575 | L7883–L7888 | QRETARGETING @ L7684 | `(defrule     (false)     (goal BH 10)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#575 | **PRESERVED** |
| 576 | L7890–L7907 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-second-turn 1)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#576 | **PRESERVED** |
| 577 | L7909–L7922 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#577 | **PRESERVED** |
| 578 | L7924–L7931 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-fifth-turn 1)     (up-set-target-by-id g: current-boar-id)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#578 | **PRESERVED** |
| 579 | L7933–L7940 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 75)     (goal gl-fifth-turn 1)     (up-set-target-by-id g: old-boar-id)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#579 | **PRESERVED** |
| 580 | L7942–L7947 | QRETARGETING @ L7684 | `(defrule     (taunt-detected me 76)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#580 | **PRESERVED** |
| 581 | L7950–L7958 | QFORCEDROP @ L7949 | `(defrule     (wood-amount >= 70)     (goal gl-twenty-turn 1)     (building-type-count-total lumber-camp < 2)     (up-compare-goal gl-current-build-item == LC2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#581 | **PRESERVED** |
| 582 | L7960–L7966 | QFORCEDROP @ L7949 | `(defrule     (current-age == feudal-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#582 | **PRESERVED** |
| 583 | L7968–L7977 | QFORCEDROP @ L7949 | `(defrule     (wood-amount > 130)     (wood-amount < 175)     (goal gl-tenth-turn 1)     (current-age == feudal-age)     (goal gl-current-build-item RANGES)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#583 | **PRESERVED** |
| 584 | L7979–L7984 | QFORCEDROP @ L7949 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 585 | L7986–L7994 | QFORCEDROP @ L7949 | `(defrule     (or	(and(food-amount >= 50)     (unit-type-count villager < FlushDarkAgeVills))     (or	(and(food-amount >= 500)     (current-age == dark-age))     (up-research-sta...` | force-res-drop-goal | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#585 | **PRESERVED** |
| 586 | L7996–L8005 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal force-res-drop-goal -1)     (unit-type-count villager < 13)     (timer-triggered villager-timer)     (up-pending-objects c: villager == 1)` | — | villager-timer | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#586 | **PRESERVED** |
| 587 | L8007–L8023 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal force-res-drop-goal 0)     (timer-triggered villager-timer)     (up-pending-objects c: villager < 2)     (or	(unit-type-count villager ...` | goal | villager-timer | — | — | up-get-fact, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#587 | **PRESERVED** |
| 588 | L8025–L8035 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal force-res-drop-goal 0)     (current-age == dark-age)     (unit-type-count villager < 16)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#588 | **PRESERVED** |
| 589 | L8037–L8047 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 500)     (food-amount >= 410)     (goal gl-fifth-turn 1)     (current-age == dark-age)     (goal gl-strategy FLUSH)     (research-available feudal-age)` | — | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#589 | **PRESERVED** |
| 590 | L8049–L8060 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 500)     (food-amount < 410)     (food-amount >= 360)     (goal gl-tenth-turn 1)     (current-age == dark-age)     (goal gl-strategy FLUSH)     (rese...` | — | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#590 | **PRESERVED** |
| 591 | L8062–L8074 | QFORCEDROP @ L7949 | `(defrule     (food-amount >= 600)     (gold-amount >= 140)     (goal gl-twenty-turn 1)     (or	(gold-amount < 200)     (food-amount < 800))     (current-age == feudal-age)     (...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#591 | **PRESERVED** |
| 592 | L8076–L8085 | QFORCEDROP @ L7949 | `(defrule     (food-amount < 50)     (goal gl-twenty-turn 1)     (current-age < feudal-age)     (timer-triggered t-vill-training)     (up-pending-objects c: villager < 2)` | — | t-vill-training | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#592 | **PRESERVED** |
| 593 | L8089–L8094 | QCLAIMING SHEEP @ L8087 | `(defrule     (or	(game-time < 2)     (game-time > 30))` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#593 | **PRESERVED** |
| 594 | L8096–L8106 | QCLAIMING SHEEP @ L8087 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#594 | **PRESERVED** |
| 595 | L8108–L8115 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-compare-goal rt > 0)` | split | — | — | up-clean-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#595 | **PRESERVED** |
| 596 | L8117–L8127 | QCLAIMING SHEEP @ L8087 | `(defrule     (goal SPLIT 1)` | split | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#596 | **PRESERVED** |
| 597 | L8129–L8137 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-compare-goal lt > 0)` | — | — | — | up-clean-search, up-remove-objects | up-target-point | — | ShadowByzantine/ShadowByzantine.per#597 | **PRESERVED** |
| 598 | L8140–L8146 | QCLAIMING SHEEP @ L8087 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 599 | L8148–L8152 | QCLAIMING SHEEP @ L8087 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#599 | **PRESERVED** |
| 600 | L8154–L8160 | QCLAIMING SHEEP @ L8087 | `(defrule     (current-age == dark-age)     (or	(current-age-time > 180)     (unit-type-count sheep < 1))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#600 | **PRESERVED** |
| 601 | L8162–L8166 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#601 | **PRESERVED** |
| 602 | L8168–L8178 | QCLAIMING SHEEP @ L8087 | `(defrule     (true)` | sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#602 | **PRESERVED** |
| 603 | L8180–L8193 | QCLAIMING SHEEP @ L8087 | `(defrule     (up-compare-goal rt > 0)` | sn-focus-player-number, split | — | — | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#603 | **PRESERVED** |
| 604 | L8195–L8206 | QCLAIMING SHEEP @ L8087 | `(defrule     (goal SPLIT 1)` | gl-getting-sheep | 28 | — | — | up-target-point | — | ShadowByzantine/ShadowByzantine.per#604 | **PRESERVED** |
| 605 | L8208–L8213 | QCLAIMING SHEEP @ L8087 | `(defrule     (false)     (timer-triggered 28)` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#605 | **PRESERVED** |
| 606 | L8215–L8220 | QCLAIMING SHEEP @ L8087 | `(defrule     (false)     (up-timer-status 28 == timer-running)` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#606 | **PRESERVED** |
| 607 | L8224–L8238 | QFARMS @ L8222 | `(defrule     (idle-farm-count > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#607 | **PRESERVED** |
| 608 | L8240–L8258 | QFARMS @ L8222 | `(defrule     (goal SPLIT 1)` | — | — | — | up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#608 | **PRESERVED** |
| 609 | L8260–L8265 | QFARMS @ L8222 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#609 | **PRESERVED** |
| 610 | L8269–L8276 | QARCHERS @ L8267 | `(defrule     (false)     (or	(game-time < 10)     (or	(unit-type-count archer < 1)     (up-group-size c: RangedGroup < 1)))` | — | — | — | — | — | 2 | ShadowByzantine/ShadowByzantine.per#610 | **PRESERVED** |
| 611 | L8280–L8286 | QARCHERS @ L8267 | `(defrule     (true)` | gl-enemy-skirms-nearby, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#611 | **PRESERVED** |
| 612 | L8289–L8298 | QARCHERS @ L8267 | `(defrule     (stance-toward focus-player enemy)` | gl-enemy-skirms-nearby | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#612 | **PRESERVED** |
| 613 | L8301–L8306 | QARCHERS @ L8267 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 614 | L8308–L8317 | QARCHERS @ L8267 | `(defrule     (up-compare-goal rt >= 1)` | gl-enemy-skirms-nearby | — | — | up-clean-search, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#614 | **PRESERVED** |
| 615 | L8320–L8336 | QARCHERS @ L8267 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 616 | L8341–L8346 | QSKIRMS @ L8338 | `(defrule     (players-unit-type-count target-player archer-line >= 4)` | gl-enemy-archers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#616 | **PRESERVED** |
| 617 | L8349–L8354 | QSKIRMS @ L8338 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#294; ShadowByzantine/ShadowByzantine.per#617; ShadowByzantine/ShadowByzantine.per#623 | **PRESERVED** |
| 618 | L8357–L8365 | QSKIRMS @ L8338 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#618 | **PRESERVED** |
| 619 | L8368–L8374 | QSKIRMS @ L8338 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 620 | L8376–L8392 | QSKIRMS @ L8338 | `(defrule     (true)     (goal gl-tenth-turn 1)     (goal gl-enemy-archers YES)     (or	(goal gl-town-safe YES)     (up-compare-goal rt < 1))     (up-group-size c: RangedGroup > ...` | split | — | — | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#620 | **PRESERVED** |
| 621 | L8394–L8403 | QSKIRMS @ L8338 | `(defrule     (goal SPLIT 1)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state, up-target-point | — | ShadowByzantine/ShadowByzantine.per#621 | **PRESERVED** |
| 622 | L8406–L8410 | QDEFENSE @ L8405 | `(defrule     (current-age < feudal-age)` | — | — | — | — | — | 3 | ShadowByzantine/ShadowByzantine.per#622 | **PRESERVED** |
| 623 | L8413–L8418 | QDEFENSE @ L8405 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#294; ShadowByzantine/ShadowByzantine.per#617; ShadowByzantine/ShadowByzantine.per#623 | **PRESERVED** |
| 624 | L8421–L8429 | QDEFENSE @ L8405 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#624 | **PRESERVED** |
| 625 | L8432–L8438 | QDEFENSE @ L8405 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 626 | L8440–L8455 | QDEFENSE @ L8405 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 627 | L8457–L8464 | QDEFENSE @ L8405 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-cavalry-in-town < 3)     (up-compare-goal gl-archery-in-town >= 4)` | — | — | — | up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#627 | **PRESERVED** |
| 628 | L8466–L8483 | QDEFENSE @ L8405 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#628 | **PRESERVED** |
| 629 | L8486–L8499 | QMANGOS @ L8485 | `(defrule     (goal gl-ninety-turn 1)     (unit-type-count mangonel > 0)     (up-compare-goal SUPERIORITY < 20)     (up-group-size c: RangedGroup > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#629 | **PRESERVED** |
| 630 | L8504–L8515 | QSPEARS @ L8501 | `(defrule     (unit-type-count spearman-line >= 1)` | goal, lt, point-x, point-y | — | — | up-find-local, up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#630 | **PRESERVED** |
| 631 | L8517–L8527 | QSPEARS @ L8501 | `(defrule     (unit-type-count spearman-line >= 1)     (up-set-target-object search-local c: 0)` | goal, point-x, point-y | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#631 | **PRESERVED** |
| 632 | L8529–L8536 | QSPEARS @ L8501 | `(defrule     (up-compare-goal lt > 0)     (unit-type-count spearman-line >= 1)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | ShadowByzantine/ShadowByzantine.per#632 | **PRESERVED** |
| 633 | L8538–L8545 | QSPEARS @ L8501 | `(defrule     (up-compare-goal goal > 0)     (unit-type-count spearman-line >= 1)` | point-x, point-y | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#633 | **PRESERVED** |
| 634 | L8547–L8554 | QSPEARS @ L8501 | `(defrule     (goal gl-thirty-turn 1)     (up-group-size c: RangedGroup < 1)` | — | — | — | up-find-local, up-full-reset-search | up-target-point | — | ShadowByzantine/ShadowByzantine.per#634 | **PRESERVED** |
| 635 | L8556–L8560 | QSPEARS @ L8501 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#635 | **PRESERVED** |
| 636 | L8562–L8569 | QSPEARS @ L8501 | `(defrule     (game-time >= 1020)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#636 | **PRESERVED** |
| 637 | L8571–L8576 | QSPEARS @ L8501 | `(defrule     (up-group-size c: RangedGroup < 1)     (unit-type-count skirmisher-line < 1)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#637 | **PRESERVED** |
| 638 | L8580–L8588 | QSPEARS @ L8501 | `(defrule     (true)` | goal, goal1, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#638 | **PRESERVED** |
| 639 | L8591–L8607 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal, goal1 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#639 | **PRESERVED** |
| 640 | L8610–L8615 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 641 | L8617–L8633 | QSPEARS @ L8501 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 642 | L8636–L8641 | QSPEARS @ L8501 | `(defrule     (or (up-group-size c: RangedGroup < 1)     (unit-type-count spearman-line < 1))` | — | — | — | — | — | 34 | ShadowByzantine/ShadowByzantine.per#642 | **PRESERVED** |
| 643 | L8643–L8653 | QSPEARS @ L8501 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#643 | **PRESERVED** |
| 644 | L8655–L8660 | QSPEARS @ L8501 | `(defrule     (up-point-distance enemy-group-x ranged-group-x < 15)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#644 | **PRESERVED** |
| 645 | L8663–L8676 | QSPEARS @ L8501 | `(defrule     (true)` | goal1, sn-focus-player-number | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#645 | **PRESERVED** |
| 646 | L8680–L8689 | QSPEARS @ L8501 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 647 | L8693–L8708 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#647 | **PRESERVED** |
| 648 | L8710–L8718 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal3 | — | — | up-find-remote, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#648 | **PRESERVED** |
| 649 | L8721–L8726 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | ShadowByzantine/ShadowByzantine.per#649; ShadowByzantine/ShadowByzantine.per#833; ShadowByzantine/ShadowByzantine.per#1386 | **PRESERVED** |
| 650 | L8731–L8737 | QSPEARS @ L8501 | `(defrule     (true)` | goal6, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#650 | **PRESERVED** |
| 651 | L8740–L8750 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal6 | — | — | up-find-status-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#651 | **PRESERVED** |
| 652 | L8753–L8758 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 653 | L8763–L8769 | QSPEARS @ L8501 | `(defrule     (true)` | goal4, rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#653 | **PRESERVED** |
| 654 | L8772–L8784 | QSPEARS @ L8501 | `(defrule     (stance-toward focus-player enemy)` | goal4 | — | — | up-find-status-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#654 | **PRESERVED** |
| 655 | L8787–L8792 | QSPEARS @ L8501 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 656 | L8796–L8811 | QSPEARS @ L8501 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 657 | L8814–L8819 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-status-remote | — | — | ShadowByzantine/ShadowByzantine.per#657 | **PRESERVED** |
| 658 | L8822–L8828 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#658; ShadowByzantine/ShadowByzantine.per#664; ShadowByzantine/ShadowByzantine.per#669 | **PRESERVED** |
| 659 | L8830–L8839 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#659 | **PRESERVED** |
| 660 | L8841–L8856 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#660 | **PRESERVED** |
| 661 | L8858–L8862 | QSPEARS @ L8501 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 662 | L8866–L8880 | QSPEARS @ L8501 | `(defrule     (up-compare-goal goal6 < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#662 | **PRESERVED** |
| 663 | L8883–L8888 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote | — | — | ShadowByzantine/ShadowByzantine.per#663 | **PRESERVED** |
| 664 | L8891–L8897 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#658; ShadowByzantine/ShadowByzantine.per#664; ShadowByzantine/ShadowByzantine.per#669 | **PRESERVED** |
| 665 | L8899–L8909 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#665 | **PRESERVED** |
| 666 | L8911–L8923 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-remove-objects, up-set-target-point | up-target-objects, up-target-point | — | ShadowByzantine/ShadowByzantine.per#666 | **PRESERVED** |
| 667 | L8927–L8939 | QSPEARS @ L8501 | `(defrule     (goal gl-second-turn 1)     (or	(up-compare-goal goal1 >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#667 | **PRESERVED** |
| 668 | L8942–L8950 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#668 | **PRESERVED** |
| 669 | L8953–L8959 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#658; ShadowByzantine/ShadowByzantine.per#664; ShadowByzantine/ShadowByzantine.per#669 | **PRESERVED** |
| 670 | L8961–L8971 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#670 | **PRESERVED** |
| 671 | L8973–L8985 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-find-local, up-remove-objects, up-set-target-point | up-target-objects, up-target-point | — | ShadowByzantine/ShadowByzantine.per#671 | **PRESERVED** |
| 672 | L8988–L8999 | QSPEARS @ L8501 | `(defrule     (goal gl-second-turn 1)     (up-compare-goal goal1 < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#672 | **PRESERVED** |
| 673 | L9001–L9009 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 674 | L9011–L9018 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)     (up-point-distance ranged-group-x home-x >= 25)` | — | — | — | up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#674; ShadowByzantine/ShadowByzantine.per#993 | **PRESERVED** |
| 675 | L9020–L9028 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#675 | **PRESERVED** |
| 676 | L9030–L9035 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)     (up-point-distance spear-group-x nearest-tower-x < 9)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#676 | **PRESERVED** |
| 677 | L9037–L9045 | QSPEARS @ L8501 | `(defrule     (goal SPLIT 1)` | split | — | — | — | up-target-point | — | ShadowByzantine/ShadowByzantine.per#677 | **PRESERVED** |
| 678 | L9048–L9059 | QSPEARS @ L8501 | `(defrule     (taunt-detected me 53)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#678 | **PRESERVED** |
| 679 | L9061–L9066 | QSPEARS @ L8501 | `(defrule     (taunt-detected me 54)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#679 | **PRESERVED** |
| 680 | L9070–L9076 | QSCOUT @ L9068 | `(defrule     (game-time > 300)     (goal gl-ninety-turn 1)     (unit-type-count scout-cavalry-line > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#680 | **PRESERVED** |
| 681 | L9079–L9084 | QSCOUT @ L9068 | `(defrule     (up-set-target-by-id g: scout-id)     (unit-type-count scout-cavalry-line >= 1)` | — | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#681 | **PRESERVED** |
| 682 | L9086–L9101 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 683 | L9103–L9115 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 684 | L9117–L9127 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#684 | **PRESERVED** |
| 685 | L9129–L9133 | QSCOUT @ L9068 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#464; ShadowByzantine/ShadowByzantine.per#685; ShadowByzantine/ShadowByzantine.per#834 | **PRESERVED** |
| 686 | L9135–L9142 | QSCOUT @ L9068 | `(defrule     (game-time < 860)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#686 | **PRESERVED** |
| 687 | L9144–L9151 | QSCOUT @ L9068 | `(defrule     (or	(goal SOD 0)     (or	(goal gl-strategy KRUSH)     (or	(goal gl-position POCKET)     (unit-type-count scout-cavalry < 1))))` | — | — | — | — | — | 36 | ShadowByzantine/ShadowByzantine.per#687 | **PRESERVED** |
| 688 | L9153–L9163 | QSCOUT @ L9068 | `(defrule     (or	(goal gl-scout-added FINISHED)     (players-building-type-count target-player town-center < 1))     (or	(up-timer-status 28 == timer-running)     (or	(goal gl-s...` | — | 28 | — | — | — | 35 | ShadowByzantine/ShadowByzantine.per#688 | **PRESERVED** |
| 689 | L9165–L9174 | QSCOUT @ L9068 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#689 | **PRESERVED** |
| 690 | L9176–L9187 | QSCOUT @ L9068 | `(defrule     (goal gl-fifth-turn 1)     (strategic-number sn-total-number-explorers > 0)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#690 | **PRESERVED** |
| 691 | L9189–L9207 | QSCOUT @ L9068 | `(defrule     (goal gl-fifth-turn 1)     (current-age-time < 400)     (goal gl-strategy FLUSH)     (current-age < castle-age)     (goal NEWSCOUTING FINISHED)     (up-group-size c...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#691 | **PRESERVED** |
| 692 | L9209–L9213 | QSCOUT @ L9068 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 31 | ShadowByzantine/ShadowByzantine.per#692 | **PRESERVED** |
| 693 | L9216–L9221 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 694 | L9224–L9234 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | goal3 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#694 | **PRESERVED** |
| 695 | L9237–L9243 | QSCOUT @ L9068 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 696 | L9246–L9253 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 697 | L9256–L9264 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | goal5 | — | — | up-find-remote, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#697 | **PRESERVED** |
| 698 | L9267–L9272 | QSCOUT @ L9068 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 699 | L9275–L9281 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 700 | L9284–L9294 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#700 | **PRESERVED** |
| 701 | L9296–L9302 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 702 | L9304–L9315 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)` | goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#702 | **PRESERVED** |
| 703 | L9318–L9324 | QSCOUT @ L9068 | `(defrule     (player-valid focus-player)` | sn-focus-player-number, split | — | — | — | — | -4 | ShadowByzantine/ShadowByzantine.per#703 | **PRESERVED** |
| 704 | L9326–L9330 | QSCOUT @ L9068 | `(defrule     (up-set-target-by-id g: scout-id)` | — | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#704 | **PRESERVED** |
| 705 | L9333–L9340 | QSCOUT @ L9068 | `(defrule     (true)` | — | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#705 | **PRESERVED** |
| 706 | L9343–L9357 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 707 | L9360–L9366 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)     (stance-toward focus-player enemy)` | — | — | — | up-find-remote | — | — | ShadowByzantine/ShadowByzantine.per#707 | **PRESERVED** |
| 708 | L9369–L9375 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#658; ShadowByzantine/ShadowByzantine.per#664; ShadowByzantine/ShadowByzantine.per#669 | **PRESERVED** |
| 709 | L9377–L9386 | QSCOUT @ L9068 | `(defrule     (goal SPLIT 1)` | — | — | — | up-clean-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#709 | **PRESERVED** |
| 710 | L9388–L9392 | QSCOUT @ L9068 | `(defrule     (up-point-distance nearest-tower-x scout-x < 7)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#710 | **PRESERVED** |
| 711 | L9394–L9398 | QSCOUT @ L9068 | `(defrule     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#711 | **PRESERVED** |
| 712 | L9400–L9410 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 713 | L9412–L9418 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 714 | L9421–L9429 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 715 | L9432–L9439 | QSCOUT @ L9068 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#715 | **PRESERVED** |
| 716 | L9442–L9447 | QSCOUT @ L9068 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 717 | L9449–L9459 | QSCOUT @ L9068 | `(defrule     (true)` | goal4, sn-focus-player-number | — | — | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#717 | **PRESERVED** |
| 718 | L9461–L9474 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 719 | L9477–L9483 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 720 | L9485–L9494 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 721 | L9496–L9503 | QSCOUT @ L9068 | `(defrule     (or	(up-compare-goal goal2 >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#721 | **PRESERVED** |
| 722 | L9505–L9512 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 723 | L9515–L9530 | QSCOUT @ L9068 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 724 | L9532–L9541 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 9)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#724 | **PRESERVED** |
| 725 | L9543–L9548 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 10)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#725 | **PRESERVED** |
| 726 | L9551–L9563 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 69)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#726 | **PRESERVED** |
| 727 | L9565–L9573 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 70)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#727 | **PRESERVED** |
| 728 | L9575–L9583 | QSCOUT @ L9068 | `(defrule     (taunt-detected me 71)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#728 | **PRESERVED** |
| 729 | L9586–L9597 | QSCOUT @ L9068 | `(defrule     (or	(timer-triggered 28)     (taunt-detected me 11))     (up-compare-goal gl-scout-added != FINISHED)` | — | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#729 | **PRESERVED** |
| 730 | L9599–L9608 | QSCOUT @ L9068 | `(defrule     (or	(timer-triggered 28)     (taunt-detected me 11))     (up-compare-goal gl-scout-added == FINISHED)` | gl-getting-sheep | 28 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#730 | **PRESERVED** |
| 731 | L9611–L9619 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 732 | L9621–L9627 | QSOD @ L9610 | `(defrule     (or	(not(up-set-target-by-id g: scout-id))     (and(goal SOD -1)     (unit-type-count scout-cavalry-line < 1)))` | — | — | — | — | — | 14 | ShadowByzantine/ShadowByzantine.per#732 | **PRESERVED** |
| 733 | L9629–L9639 | QSOD @ L9610 | `(defrule     (true)` | goal, goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#733 | **PRESERVED** |
| 734 | L9642–L9647 | QSOD @ L9610 | `(defrule     (up-set-target-by-id g: scout-id)` | goal1 | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#734 | **PRESERVED** |
| 735 | L9649–L9654 | QSOD @ L9610 | `(defrule     (military-population < 6)     (current-age >= feudal-age)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#735 | **PRESERVED** |
| 736 | L9656–L9660 | QSOD @ L9610 | `(defrule     (players-building-type-count every-enemy town-center < 1)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#736 | **PRESERVED** |
| 737 | L9662–L9667 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 738 | L9669–L9674 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 739 | L9681–L9690 | QSOD @ L9610 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 740 | L9692–L9701 | QSOD @ L9610 | `(defrule     (goal SOD -1)     (up-compare-goal rt > 0)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#740 | **PRESERVED** |
| 741 | L9703–L9709 | QSOD @ L9610 | `(defrule     (goal SOD -1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | ShadowByzantine/ShadowByzantine.per#741 | **PRESERVED** |
| 742 | L9712–L9718 | QSOD @ L9610 | `(defrule     (true)` | goal, goal1, goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#742 | **PRESERVED** |
| 743 | L9720–L9726 | QSOD @ L9610 | `(defrule     (goal gl-strategy KRUSH)` | goal, goal1, goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#743 | **PRESERVED** |
| 744 | L9728–L9733 | QSOD @ L9610 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-circle-direcion CLOCKWISE)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#744 | **PRESERVED** |
| 745 | L9735–L9753 | QSOD @ L9610 | `(defrule     (goal SPLIT 1)` | — | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#745 | **PRESERVED** |
| 746 | L9755–L9763 | QSOD @ L9610 | `(defrule     (goal SOD 0)     (or	(up-timer-status 28 != timer-running)     (unit-type-count scout-cavalry-line < 1))` | — | 28 | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#746 | **PRESERVED** |
| 747 | L9767–L9776 | QKNIGHT GROUP @ L9765 | `(defrule     (goal gl-attacking -1)     (goal gl-tenth-turn 1)     (goal gl-town-safe YES)     (goal gl-strategy KRUSH)     (unit-type-count knight-line > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#747 | **PRESERVED** |
| 748 | L9779–L9792 | QKNIGHT GROUP @ L9765 | `(defrule     (true)` | goal, lt, point-x, point-y, sn-focus-player-number | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#748 | **PRESERVED** |
| 749 | L9794–L9803 | QKNIGHT GROUP @ L9765 | `(defrule     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#749; ShadowByzantine/ShadowByzantine.per#928 | **PRESERVED** |
| 750 | L9805–L9811 | QKNIGHT GROUP @ L9765 | `(defrule     (up-compare-goal lt > 0)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | ShadowByzantine/ShadowByzantine.per#750 | **PRESERVED** |
| 751 | L9813–L9819 | QKNIGHT GROUP @ L9765 | `(defrule     (up-compare-goal goal > 0)` | point-x, point-y | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#751 | **PRESERVED** |
| 752 | L9822–L9834 | QEVAL @ L9821 | `(defrule     (true)` | goal1 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#752 | **PRESERVED** |
| 753 | L9836–L9845 | QEVAL @ L9821 | `(defrule     (true)` | goal | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#753 | **PRESERVED** |
| 754 | L9847–L9858 | QEVAL @ L9821 | `(defrule     (true)` | goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#754 | **PRESERVED** |
| 755 | L9860–L9864 | QEVAL @ L9821 | `(defrule     (up-group-size c: KnightGroup < 1)` | — | — | — | — | — | 10 | ShadowByzantine/ShadowByzantine.per#755 | **PRESERVED** |
| 756 | L9867–L9873 | QEVAL @ L9821 | `(defrule     (true)` | gl-knight-eval | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#756 | **PRESERVED** |
| 757 | L9875–L9879 | QEVAL @ L9821 | `(defrule     (research-completed ri-scale-barding)` | gl-knight-eval | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#757 | **PRESERVED** |
| 758 | L9882–L9886 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 759 | L9888–L9892 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 760 | L9894–L9898 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 761 | L9901–L9911 | QEVAL @ L9821 | `(defrule     (true)` | goal3 | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#761 | **PRESERVED** |
| 762 | L9913–L9918 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 763 | L9921–L9926 | QEVAL @ L9821 | `(defrule     (research-completed ri-chain-barding)` | gl-knight-eval | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#763 | **PRESERVED** |
| 764 | L9928–L9932 | QEVAL @ L9821 | `(defrule     (research-completed ri-forging)` | gl-knight-eval | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#764 | **PRESERVED** |
| 765 | L9934–L9938 | QEVAL @ L9821 | `(defrule     (research-completed ri-iron-casting)` | gl-knight-eval | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#765 | **PRESERVED** |
| 766 | L9941–L9945 | QEVAL @ L9821 | `(defrule     (up-group-size c: KnightGroup < 1)` | — | — | — | — | — | 30 | ShadowByzantine/ShadowByzantine.per#766 | **PRESERVED** |
| 767 | L9947–L9954 | QEVAL @ L9821 | `(defrule     (true)` | goal, goal1, goal2, goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#767; ShadowByzantine/ShadowByzantine.per#1081 | **PRESERVED** |
| 768 | L9956–L9968 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 769 | L9970–L9979 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 770 | L9981–L9994 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 771 | L9996–L10006 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 772 | L10010–L10017 | QEVAL @ L9821 | `(defrule     (up-compare-goal goal3 >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#772 | **PRESERVED** |
| 773 | L10019–L10035 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 774 | L10038–L10046 | QEVAL @ L9821 | `(defrule     (up-compare-goal goal3 < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#774 | **PRESERVED** |
| 775 | L10048–L10057 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 776 | L10060–L10071 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 777 | L10073–L10088 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 778 | L10090–L10103 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 779 | L10106–L10111 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 780 | L10114–L10122 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (nand	(up-compare-goal SUPERIORITY >= 20)     (research-completed ri-chain-barding))     (up-point-distance knight-group-x nearest-c...` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#780 | **PRESERVED** |
| 781 | L10124–L10131 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 4)     (up-point-distance knight-group-x point-x < 3)     (up-point-distance knight-group-x nearest-castle-x >= 18)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#781 | **PRESERVED** |
| 782 | L10134–L10140 | QEVAL @ L9821 | `(defrule     (up-compare-goal goal2 < 4)     (up-group-size c: KnightGroup >= 2)     (up-compare-goal gl-knight-group-state == SATTACKING)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#782 | **PRESERVED** |
| 783 | L10142–L10153 | QEVAL @ L9821 | `(defrule     (false)     (goal gl-knight-retreat -1)     (up-compare-goal goal2 >= 1)     (up-group-size c: KnightGroup < 5)     (or	(up-compare-goal goal2 >= 3)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#783 | **PRESERVED** |
| 784 | L10155–L10161 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 3)     (up-compare-goal goal2 < 1)` | gl-knight-retreat | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#784 | **PRESERVED** |
| 785 | L10164–L10174 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (up-group-size c: KnightGroup < 8)     (not(research-completed ri-chain-barding))     (or	(up-compare-goal goal >= 4)     (and(up-co...` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#785 | **PRESERVED** |
| 786 | L10176–L10186 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (up-group-size c: KnightGroup < 7)     (research-completed ri-chain-barding)     (or	(up-compare-goal goal >= 6)     (and(up-compare...` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#786 | **PRESERVED** |
| 787 | L10188–L10194 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 2)     (up-compare-goal goal < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#787 | **PRESERVED** |
| 788 | L10197–L10207 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (up-group-size c: KnightGroup < 7)     (nand	(up-compare-goal SUPERIORITY >= 8)     (research-completed ri-chain-barding))     (up-p...` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#788 | **PRESERVED** |
| 789 | L10209–L10216 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 1)     (up-point-distance knight-group-x point-x < 3)     (up-point-distance knight-group-x nearest-tc-x >= 12)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#789 | **PRESERVED** |
| 790 | L10219–L10227 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat -1)     (or	(up-point-distance knight-group-x ranged-group-x >= 25)     (and(up-compare-goal gl-knight-group-state != SATTACKING)     (up-po...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#790 | **PRESERVED** |
| 791 | L10229–L10235 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 0)     (up-point-distance knight-group-x ranged-group-x < 7)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#791 | **PRESERVED** |
| 792 | L10237–L10248 | QEVAL @ L9821 | `(defrule     (goal gl-second-turn 1)     (up-compare-goal gl-knight-retreat != -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#792 | **PRESERVED** |
| 793 | L10251–L10267 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 794 | L10270–L10286 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 795 | L10288–L10297 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 796 | L10299–L10306 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#796 | **PRESERVED** |
| 797 | L10308–L10313 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-point | — | ShadowByzantine/ShadowByzantine.per#797 | **PRESERVED** |
| 798 | L10315–L10333 | QEVAL @ L9821 | `(defrule     (unit-type-count knight-line >= 1)     (up-group-size c: KnightGroup < 1)     (up-compare-goal SUPERIORITY < 15)     (up-group-size c: RangedGroup >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#798 | **PRESERVED** |
| 799 | L10335–L10346 | QEVAL @ L9821 | `(defrule     (up-group-size c: KnightGroup > 0)     (or	(up-group-size c: RangedGroup < 1)     (up-compare-goal SUPERIORITY >= 20))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#799 | **PRESERVED** |
| 800 | L10349–L10360 | QEVAL @ L9821 | `(defrule     (taunt-detected me 77)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#800 | **PRESERVED** |
| 801 | L10362–L10367 | QEVAL @ L9821 | `(defrule     (taunt-detected me 77)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#801 | **PRESERVED** |
| 802 | L10369–L10374 | QEVAL @ L9821 | `(defrule     (taunt-detected me 78)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#802 | **PRESERVED** |
| 803 | L10376–L10380 | QEVAL @ L9821 | `(defrule     (true)` | — | — | — | — | — | 11 | ShadowByzantine/ShadowByzantine.per#803 | **PRESERVED** |
| 804 | L10382–L10387 | QEVAL @ L9821 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-point-distance ranged-group-x knight-group-x >= 8)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#804 | **PRESERVED** |
| 805 | L10389–L10393 | QEVAL @ L9821 | `(defrule     (true)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#805 | **PRESERVED** |
| 806 | L10395–L10399 | QEVAL @ L9821 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#806 | **PRESERVED** |
| 807 | L10401–L10410 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 808 | L10412–L10420 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 809 | L10422–L10431 | QEVAL @ L9821 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 810 | L10433–L10438 | QEVAL @ L9821 | `(defrule     (false)     (goal gl-knight-retreat 2)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#810 | **PRESERVED** |
| 811 | L10440–L10452 | QEVAL @ L9821 | `(defrule     (goal SPLIT 1)` | gl-knight-group-state, split | — | — | up-full-reset-search | up-target-point | — | ShadowByzantine/ShadowByzantine.per#811 | **PRESERVED** |
| 812 | L10454–L10460 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 1)     (up-compare-goal gl-knight-eval >= CostOfFighting)` | gl-knight-retreat | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#812 | **PRESERVED** |
| 813 | L10462–L10470 | QEVAL @ L9821 | `(defrule     (goal gl-knight-retreat 3)     (or	(up-compare-goal gl-knight-eval >= CostOfIgnoringTCFire)     (or	(not(up-projectile-detected projectile-town-center c:< 3000))   ...` | gl-knight-retreat | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#813 | **PRESERVED** |
| 814 | L10472–L10479 | QEVAL @ L9821 | `(defrule     (false)     (goal gl-knight-retreat 2)     (up-point-distance knight-group-x ranged-group-x < 10)` | gl-knight-retreat | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#814 | **PRESERVED** |
| 815 | L10483–L10494 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-enemy-strategy != KRUSH)     (up-compare-goal gl-ranged-style != SEPARATE)     (players-unit-type-count t...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#815 | **PRESERVED** |
| 816 | L10496–L10505 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-ranged-style != COMBINED)     (or	(up-compare-goal gl-enemy-strategy == KRUSH)     (or	(players-unit-type...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#816 | **PRESERVED** |
| 817 | L10507–L10513 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup < 1)     (up-compare-goal gl-ranged-style != -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#817 | **PRESERVED** |
| 818 | L10516–L10527 | QRAIDING @ L10481 | `(defrule     (goal gl-tenth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#818 | **PRESERVED** |
| 819 | L10530–L10534 | QRAIDING @ L10481 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 820 | L10536–L10544 | QRAIDING @ L10481 | `(defrule     (game-time > 3)     (goal gl-second-turn 1)     (up-group-size c: RaidGroup < 1)     (unit-type-count archer-line >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#820 | **PRESERVED** |
| 821 | L10546–L10562 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 822 | L10565–L10571 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 823 | L10573–L10583 | QRAIDING @ L10481 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#823; ShadowByzantine/ShadowByzantine.per#828; ShadowByzantine/ShadowByzantine.per#990 | **PRESERVED** |
| 824 | L10585–L10594 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 825 | L10596–L10603 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)     (up-point-distance raid-group-x home-x >= 25)` | — | — | — | up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#825 | **PRESERVED** |
| 826 | L10605–L10615 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | up-remove-objects | up-target-point | — | ShadowByzantine/ShadowByzantine.per#826 | **PRESERVED** |
| 827 | L10617–L10622 | QRAIDING @ L10481 | `(defrule     (taunt-detected me 86)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#827; ShadowByzantine/ShadowByzantine.per#995 | **PRESERVED** |
| 828 | L10624–L10642 | QRAIDING @ L10481 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#823; ShadowByzantine/ShadowByzantine.per#828; ShadowByzantine/ShadowByzantine.per#990 | **PRESERVED** |
| 829 | L10644–L10658 | QRAIDING @ L10481 | `(defrule     (true)     (false)` | — | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#829 | **PRESERVED** |
| 830 | L10662–L10672 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#830 | **PRESERVED** |
| 831 | L10675–L10694 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | goal, goal4 | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#831 | **PRESERVED** |
| 832 | L10696–L10700 | QRAIDING @ L10481 | `(defrule     (up-compare-goal goal4 >= 1)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#832 | **PRESERVED** |
| 833 | L10702–L10707 | QRAIDING @ L10481 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | ShadowByzantine/ShadowByzantine.per#649; ShadowByzantine/ShadowByzantine.per#833; ShadowByzantine/ShadowByzantine.per#1386 | **PRESERVED** |
| 834 | L10709–L10713 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#464; ShadowByzantine/ShadowByzantine.per#685; ShadowByzantine/ShadowByzantine.per#834 | **PRESERVED** |
| 835 | L10717–L10723 | QRAIDING @ L10481 | `(defrule     (or	(up-group-size c: RaidGroup < 1)     (and(players-building-type-count every-enemy watch-tower < 1)     (players-building-type-count every-enemy town-center < 1)))` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#835 | **PRESERVED** |
| 836 | L10725–L10734 | QRAIDING @ L10481 | `(defrule     (true)` | goal1, rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#836 | **PRESERVED** |
| 837 | L10736–L10743 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 838 | L10745–L10750 | QRAIDING @ L10481 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 839 | L10752–L10759 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | up-clean-search, up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#839 | **PRESERVED** |
| 840 | L10762–L10766 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 13 | ShadowByzantine/ShadowByzantine.per#840 | **PRESERVED** |
| 841 | L10768–L10776 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#841; ShadowByzantine/ShadowByzantine.per#1456; ShadowByzantine/ShadowByzantine.per#1744 | **PRESERVED** |
| 842 | L10778–L10782 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 843 | L10785–L10793 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 844 | L10795–L10806 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 845 | L10808–L10819 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 846 | L10821–L10829 | QRAIDING @ L10481 | `(defrule     (false)     (goal SPLIT 1)     (up-timer-status t-raid-target-reset != timer-running)` | — | t-raid-target-reset | — | up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#846 | **PRESERVED** |
| 847 | L10831–L10836 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#95; ShadowByzantine/ShadowByzantine.per#142; ShadowByzantine/ShadowByzantine.per#847 | **PRESERVED** |
| 848 | L10838–L10849 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 849 | L10851–L10865 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 850 | L10867–L10881 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 851 | L10883–L10899 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 852 | L10901–L10907 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 853 | L10909–L10918 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | 1 | ShadowByzantine/ShadowByzantine.per#853 | **PRESERVED** |
| 854 | L10921–L10925 | QRAIDING @ L10481 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#854 | **PRESERVED** |
| 855 | L10928–L10932 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 3 | ShadowByzantine/ShadowByzantine.per#855 | **PRESERVED** |
| 856 | L10934–L10938 | QRAIDING @ L10481 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 857 | L10940–L10947 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 858 | L10949–L10960 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 859 | L10963–L10967 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#859; ShadowByzantine/ShadowByzantine.per#864 | **PRESERVED** |
| 860 | L10969–L10978 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#860 | **PRESERVED** |
| 861 | L10980–L10991 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | up-clean-search, up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#861 | **PRESERVED** |
| 862 | L11001–L11009 | QRAIDING @ L10481 | `(defrule     (up-compare-goal gl-raid-can-fire != YES)     (up-compare-goal gl-highest-next-attack < arch-firing-threshold-1)     (up-compare-goal goal2 g:<= gl-raid-group-range)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#862 | **PRESERVED** |
| 863 | L11011–L11020 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 864 | L11023–L11027 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#859; ShadowByzantine/ShadowByzantine.per#864 | **PRESERVED** |
| 865 | L11029–L11037 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-can-move YES)     (up-compare-goal goal4 >= 1)     (up-timer-status t-raid-retreat != timer-running)     (or	(goal gl-fifth-turn 1)     (up-compare-go...` | split | t-raid-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#865 | **PRESERVED** |
| 866 | L11039–L11049 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 867 | L11051–L11064 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 868 | L11066–L11071 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#868 | **PRESERVED** |
| 869 | L11073–L11083 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | up-target-point | — | ShadowByzantine/ShadowByzantine.per#869 | **PRESERVED** |
| 870 | L11086–L11090 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#870; ShadowByzantine/ShadowByzantine.per#959 | **PRESERVED** |
| 871 | L11093–L11111 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-can-move YES)     (up-compare-goal goal4 < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#871 | **PRESERVED** |
| 872 | L11114–L11118 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 9 | ShadowByzantine/ShadowByzantine.per#872 | **PRESERVED** |
| 873 | L11120–L11124 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#464; ShadowByzantine/ShadowByzantine.per#685; ShadowByzantine/ShadowByzantine.per#834 | **PRESERVED** |
| 874 | L11127–L11135 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 875 | L11137–L11144 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#875 | **PRESERVED** |
| 876 | L11146–L11153 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#876 | **PRESERVED** |
| 877 | L11155–L11162 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 878 | L11164–L11168 | QRAIDING @ L10481 | `(defrule     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#878 | **PRESERVED** |
| 879 | L11170–L11174 | QRAIDING @ L10481 | `(defrule     (up-point-distance raid-group-x point-x < 8)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#879 | **PRESERVED** |
| 880 | L11177–L11182 | QRAIDING @ L10481 | `(defrule     (true)     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#880 | **PRESERVED** |
| 881 | L11184–L11202 | QRAIDING @ L10481 | `(defrule     (goal goal1 -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#881 | **PRESERVED** |
| 882 | L11205–L11210 | QRAIDING @ L10481 | `(defrule     (or	(game-time < 10)     (up-group-size c: RaidGroup < 1))` | — | — | — | — | — | 44 | ShadowByzantine/ShadowByzantine.per#882 | **PRESERVED** |
| 883 | L11212–L11217 | QRAIDING @ L10481 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#883 | **PRESERVED** |
| 884 | L11219–L11225 | QRAIDING @ L10481 | `(defrule     (timer-triggered t-raid-retreat)` | — | t-raid-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#884 | **PRESERVED** |
| 885 | L11229–L11237 | QRAIDING @ L10481 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#885 | **PRESERVED** |
| 886 | L11240–L11246 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#886 | **PRESERVED** |
| 887 | L11249–L11255 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 888 | L11257–L11264 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 889 | L11268–L11276 | QRAIDING @ L10481 | `(defrule     (true)` | goal, goal1, rt, sn-focus-player-number | — | — | up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#889 | **PRESERVED** |
| 890 | L11279–L11292 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | goal, goal1 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#890 | **PRESERVED** |
| 891 | L11295–L11300 | QRAIDING @ L10481 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 892 | L11303–L11308 | QRAIDING @ L10481 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 893 | L11310–L11319 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 894 | L11321–L11328 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 895 | L11330–L11341 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 896 | L11343–L11354 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 897 | L11357–L11362 | QRAIDING @ L10481 | `(defrule     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#87; ShadowByzantine/ShadowByzantine.per#236; ShadowByzantine/ShadowByzantine.per#300 | **PRESERVED** |
| 898 | L11364–L11373 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 899 | L11375–L11382 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 900 | L11384–L11395 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 901 | L11397–L11408 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 902 | L11411–L11420 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type -1)     (up-compare-goal SUPERIORITY >= 15)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#902 | **PRESERVED** |
| 903 | L11422–L11431 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type -1)     (up-compare-goal SUPERIORITY < 15)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#903 | **PRESERVED** |
| 904 | L11435–L11440 | QRAIDING @ L10481 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#294; ShadowByzantine/ShadowByzantine.per#617; ShadowByzantine/ShadowByzantine.per#623 | **PRESERVED** |
| 905 | L11443–L11458 | QRAIDING @ L10481 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-clean-search, up-find-status-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#905 | **PRESERVED** |
| 906 | L11461–L11467 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 907 | L11469–L11476 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt >= 1)     (goal gl-raid-retreat-type -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#907 | **PRESERVED** |
| 908 | L11480–L11488 | QRAIDING @ L10481 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#908 | **PRESERVED** |
| 909 | L11490–L11495 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-retreat-type FROM-SIEGE)` | goal1, goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#909 | **PRESERVED** |
| 910 | L11497–L11501 | QRAIDING @ L10481 | `(defrule     (up-compare-goal gl-enemy-group-size > 0)` | goal5 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#910 | **PRESERVED** |
| 911 | L11503–L11507 | QRAIDING @ L10481 | `(defrule     (up-point-distance raid-group-x raid-nearest-fort-x < 15)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#911 | **PRESERVED** |
| 912 | L11509–L11517 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style COMBINED)     (goal gl-raid-retreat-type FROM-UNITS)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#912 | **PRESERVED** |
| 913 | L11519–L11527 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style SEPARATE)     (goal gl-raid-retreat-type FROM-UNITS)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#913 | **PRESERVED** |
| 914 | L11529–L11535 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style SEPARATE)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#914 | **PRESERVED** |
| 915 | L11537–L11543 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style COMBINED)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#915 | **PRESERVED** |
| 916 | L11545–L11552 | QRAIDING @ L10481 | `(defrule     (goal gl-ranged-style -1)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#916 | **PRESERVED** |
| 917 | L11554–L11558 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RangedGroup < 1)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#917 | **PRESERVED** |
| 918 | L11561–L11572 | QRAIDING @ L10481 | `(defrule     (or	(goal gl-raid-can-fire NO)     (up-compare-goal goal4 < 1))     (up-timer-status t-raid-retreat == timer-running)     (or	(goal gl-tenth-turn 1)     (up-compare...` | — | t-raid-retreat | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#918 | **PRESERVED** |
| 919 | L11575–L11583 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type FROM-UNITS)     (up-compare-goal gl-enemy-group-size > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#919 | **PRESERVED** |
| 920 | L11585–L11593 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal gl-enemy-group-size < 1)     (up-compare-goal gl-raid-retreat-type != FROM-UNITS))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#920 | **PRESERVED** |
| 921 | L11596–L11604 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#921 | **PRESERVED** |
| 922 | L11607–L11612 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#922 | **PRESERVED** |
| 923 | L11614–L11626 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 924 | L11629–L11645 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type HOME-RETREAT)     (or	(goal gl-tenth-turn 1)     (up-compare-goal gl-raid-group-state != RETREATING))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#924 | **PRESERVED** |
| 925 | L11647–L11664 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (or	(goal gl-raid-retreat-type FROM-UNITS)     (goal gl-raid-retreat-type FROM-SIEGE))     (or	(goal gl-tenth-turn 1)     (up-compare-goal gl-rai...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#925 | **PRESERVED** |
| 926 | L11666–L11682 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-raid-retreat-type FROM-FORTIFICATIONS)     (or	(goal gl-tenth-turn 1)     (up-compare-goal gl-raid-group-state != RETREATING))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#926 | **PRESERVED** |
| 927 | L11685–L11697 | QRAIDING @ L10481 | `(defrule     (true)` | goal, lt, point-x, point-y | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#927 | **PRESERVED** |
| 928 | L11699–L11709 | QRAIDING @ L10481 | `(defrule     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#749; ShadowByzantine/ShadowByzantine.per#928 | **PRESERVED** |
| 929 | L11711–L11718 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal lt > 0)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | ShadowByzantine/ShadowByzantine.per#929 | **PRESERVED** |
| 930 | L11720–L11727 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal goal > 0)` | point-x, point-y | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#930 | **PRESERVED** |
| 931 | L11729–L11733 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#151; ShadowByzantine/ShadowByzantine.per#931; ShadowByzantine/ShadowByzantine.per#977 | **PRESERVED** |
| 932 | L11736–L11741 | QRAIDING @ L10481 | `(defrule     (true)` | — | t-raid-target-reset | — | — | — | — | ShadowByzantine/ShadowByzantine.per#932 | **PRESERVED** |
| 933 | L11745–L11752 | QRAIDING @ L10481 | `(defrule     (game-time > 5)     (goal gl-raid-status -1)     (up-group-size c: RaidGroup >= 3)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#933 | **PRESERVED** |
| 934 | L11754–L11759 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 935 | L11761–L11767 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (goal gl-ranged-style SEPARATE)` | — | — | — | up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#935 | **PRESERVED** |
| 936 | L11769–L11777 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#936 | **PRESERVED** |
| 937 | L11779–L11786 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 2)` | — | — | — | up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#937 | **PRESERVED** |
| 938 | L11788–L11794 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 2)` | — | — | — | up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#938 | **PRESERVED** |
| 939 | L11796–L11802 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 2)` | — | — | — | up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#939 | **PRESERVED** |
| 940 | L11804–L11818 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)     (up-compare-goal rt >= 1)` | gl-ancient-raid-target-id, gl-old-raid-target-id | — | — | up-clean-search, up-set-target-object, up-set-target-point | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#940 | **PRESERVED** |
| 941 | L11820–L11828 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 942 | L11831–L11839 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-TARGET)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#942 | **PRESERVED** |
| 943 | L11841–L11849 | QRAIDING @ L10481 | `(defrule     (up-compare-goal gl-raid-status != -1)     (up-timer-status t-raid-waypoint-reevaluate != timer-running)` | gl-raid-status | t-raid-waypoint-reevaluate | — | — | — | — | ShadowByzantine/ShadowByzantine.per#943 | **PRESERVED** |
| 944 | L11852–L11858 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-1)     (up-point-distance raid-group-x raid-target-x < 25)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#944 | **PRESERVED** |
| 945 | L11860–L11873 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-1)     (up-point-distance raid-group-x raid-target-x >= 25)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#945 | **PRESERVED** |
| 946 | L11875–L11881 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-1)     (up-point-distance raid-group-x raid-waypoint1-x < 4)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#946 | **PRESERVED** |
| 947 | L11884–L11890 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-2)     (up-point-distance raid-group-x raid-target-x < 45)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#947 | **PRESERVED** |
| 948 | L11892–L11905 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status CHOOSING-WAYPOINT-2)     (up-point-distance raid-group-x raid-target-x >= 45)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#948 | **PRESERVED** |
| 949 | L11907–L11913 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-WAYPOINT-2)     (up-point-distance raid-group-x raid-waypoint2-x < 4)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#949 | **PRESERVED** |
| 950 | L11915–L11921 | QRAIDING @ L10481 | `(defrule     (false)     (goal gl-twenty-turn 1)     (goal gl-raid-status MOVING-TO-WAYPOINT-2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#950 | **PRESERVED** |
| 951 | L11924–L11932 | QRAIDING @ L10481 | `(defrule     (goal gl-raid-status MOVING-TO-TARGET)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#951 | **PRESERVED** |
| 952 | L11934–L11942 | QRAIDING @ L10481 | `(defrule     (up-compare-goal rt >= 1)     (goal gl-raid-status MOVING-TO-TARGET)     (up-point-distance raid-group-x raid-target-x < 10)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#952 | **PRESERVED** |
| 953 | L11944–L11953 | QRAIDING @ L10481 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-raid-status MOVING-TO-TARGET)     (or	(timer-triggered t-raid-target-reset)     (up-point-distance raid-group-x raid-target-x < 4))` | — | t-raid-target-reset | — | — | — | — | ShadowByzantine/ShadowByzantine.per#953 | **PRESERVED** |
| 954 | L11955–L11960 | QRAIDING @ L10481 | `(defrule     (taunt-detected me 21)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#954 | **PRESERVED** |
| 955 | L11963–L11976 | QRAIDING @ L10481 | `(defrule     (false)     (up-group-size c: RaidGroup < 3)     (up-compare-goal gl-raid-status != -1)` | gl-raid-status | t-raid-target-reset | — | up-find-local, up-full-reset-search | up-target-point | — | ShadowByzantine/ShadowByzantine.per#955 | **PRESERVED** |
| 956 | L11978–L11985 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 957 | L11987–L11994 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 958 | L11996–L12001 | QRAIDING @ L10481 | `(defrule     (taunt-detected me 99)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#958 | **PRESERVED** |
| 959 | L12003–L12007 | QRAIDING @ L10481 | `(defrule     (up-group-size c: RaidGroup < 1)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#870; ShadowByzantine/ShadowByzantine.per#959 | **PRESERVED** |
| 960 | L12009–L12020 | QRAIDING @ L10481 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 961 | L12022–L12031 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 962 | L12033–L12038 | QRAIDING @ L10481 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#962 | **PRESERVED** |
| 963 | L12042–L12052 | QRANGED MICRO @ L12040 | `(defrule     (goal gl-town-safe NO)     (goal gl-defend-town NO)     (up-group-size c: RangedGroup > 0)     (up-compare-goal SUPERIORITY >= 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#963 | **PRESERVED** |
| 964 | L12054–L12062 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 965 | L12065–L12069 | QRANGED MICRO @ L12040 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#965 | **PRESERVED** |
| 966 | L12072–L12080 | QRANGED MICRO @ L12040 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#966 | **PRESERVED** |
| 967 | L12083–L12094 | QRANGED MICRO @ L12040 | `(defrule     (stance-toward focus-player enemy)` | goal, point-x, point-y, rt | — | — | up-find-remote, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#967 | **PRESERVED** |
| 968 | L12097–L12102 | QRANGED MICRO @ L12040 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 969 | L12104–L12115 | QRANGED MICRO @ L12040 | `(defrule     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#969 | **PRESERVED** |
| 970 | L12117–L12124 | QRANGED MICRO @ L12040 | `(defrule     (up-compare-goal rt > 0)` | — | — | — | up-get-search-state, up-remove-objects | up-get-search-state | -2 | ShadowByzantine/ShadowByzantine.per#970 | **PRESERVED** |
| 971 | L12126–L12132 | QRANGED MICRO @ L12040 | `(defrule     (up-compare-goal goal > 0)` | point-x, point-y | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#971 | **PRESERVED** |
| 972 | L12135–L12150 | QRANGED MICRO @ L12040 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 973 | L12152–L12165 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 974 | L12167–L12176 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 975 | L12178–L12188 | QRANGED MICRO @ L12040 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 976 | L12190–L12198 | QRANGED MICRO @ L12040 | `(defrule     (false)     (goal SPLIT 1)     (up-group-size c: RangedGroup > 10)     (up-point-distance target-x ranged-group-x < 20)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#976 | **PRESERVED** |
| 977 | L12200–L12204 | QRANGED MICRO @ L12040 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#151; ShadowByzantine/ShadowByzantine.per#931; ShadowByzantine/ShadowByzantine.per#977 | **PRESERVED** |
| 978 | L12206–L12216 | QRANGED MICRO @ L12040 | `(defrule     (false)     (goal gl-fifty-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#978 | **PRESERVED** |
| 979 | L12218–L12234 | QRANGED MICRO @ L12040 | `(defrule     (up-group-size c: RangedGroup > 0)     (unit-type-count skirmisher-line >= 25)     (research-completed ri-elite-skirmisher)     (players-unit-type-count every-enemy...` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#979 | **PRESERVED** |
| 980 | L12237–L12245 | QINITIALIZING GROUP @ L12236 | `(defrule     (up-group-size c: RangedGroup < 1)     (or	(and(unit-type-count skirmisher-line >= 1)     (up-research-status c: ri-elite-skirmisher < research-complete))     (and(...` | split | — | — | — | research, research-completed, up-research | — | ShadowByzantine/ShadowByzantine.per#980 | **PRESERVED** |
| 981 | L12247–L12254 | QINITIALIZING GROUP @ L12236 | `(defrule     (up-group-size c: RangedGroup < 1)     (unit-type-count skirmisher-line >= 1)     (or	(players-unit-type-count any-enemy knight-line >= 3)     (players-unit-type-co...` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#981 | **PRESERVED** |
| 982 | L12256–L12274 | QINITIALIZING GROUP @ L12236 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 983 | L12276–L12280 | QINITIALIZING GROUP @ L12236 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#983 | **PRESERVED** |
| 984 | L12282–L12295 | QINITIALIZING GROUP @ L12236 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 985 | L12297–L12304 | QINITIALIZING GROUP @ L12236 | `(defrule     (false)     (goal SPLIT 1)     (or (up-compare-goal gl-enemy-skirms-nearby < 4)     (up-compare-goal gl-ranged-group-state == HOME-RETREAT))` | — | — | — | up-find-local | — | — | ShadowByzantine/ShadowByzantine.per#985 | **PRESERVED** |
| 986 | L12306–L12315 | QINITIALIZING GROUP @ L12236 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | — | — | ShadowByzantine/ShadowByzantine.per#986 | **PRESERVED** |
| 987 | L12318–L12338 | QREGROUPING @ L12317 | `(defrule     (false)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#87; ShadowByzantine/ShadowByzantine.per#236; ShadowByzantine/ShadowByzantine.per#300 | **PRESERVED** |
| 988 | L12340–L12357 | QREGROUPING @ L12317 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 989 | L12359–L12364 | QREGROUPING @ L12317 | `(defrule     (or	(game-time < 3)     (up-group-size c: RangedGroup < 1))` | — | — | — | — | — | 9 | ShadowByzantine/ShadowByzantine.per#989 | **PRESERVED** |
| 990 | L12366–L12376 | QREGROUPING @ L12317 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#823; ShadowByzantine/ShadowByzantine.per#828; ShadowByzantine/ShadowByzantine.per#990 | **PRESERVED** |
| 991 | L12378–L12386 | QREGROUPING @ L12317 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 992 | L12388–L12393 | QREGROUPING @ L12317 | `(defrule     (false)     (goal SPLIT 1)` | — | — | — | up-find-local | — | — | ShadowByzantine/ShadowByzantine.per#992 | **PRESERVED** |
| 993 | L12395–L12402 | QREGROUPING @ L12317 | `(defrule     (goal SPLIT 1)     (goal gl-town-safe NO)     (up-point-distance ranged-group-x home-x >= 25)` | — | — | — | up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#674; ShadowByzantine/ShadowByzantine.per#993 | **PRESERVED** |
| 994 | L12404–L12415 | QREGROUPING @ L12317 | `(defrule     (goal SPLIT 1)` | — | — | — | up-remove-objects | up-target-point | — | ShadowByzantine/ShadowByzantine.per#994 | **PRESERVED** |
| 995 | L12417–L12422 | QREGROUPING @ L12317 | `(defrule     (taunt-detected me 86)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#827; ShadowByzantine/ShadowByzantine.per#995 | **PRESERVED** |
| 996 | L12424–L12442 | QREGROUPING @ L12317 | `(defrule     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#823; ShadowByzantine/ShadowByzantine.per#828; ShadowByzantine/ShadowByzantine.per#990 | **PRESERVED** |
| 997 | L12444–L12458 | QREGROUPING @ L12317 | `(defrule     (true)     (false)` | — | — | — | up-find-local, up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#997 | **PRESERVED** |
| 998 | L12460–L12472 | QREGROUPING @ L12317 | `(defrule     (false)     (up-compare-goal lt >= 1)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-point | — | ShadowByzantine/ShadowByzantine.per#998 | **PRESERVED** |
| 999 | L12480–L12486 | QMOVING @ L12474 | `(defrule     (or	(up-group-size c: RangedGroup < 1)     (and(players-current-age target-player < castle-age)     (players-military-population target-player < 4)))` | — | — | — | — | — | 16 | ShadowByzantine/ShadowByzantine.per#999 | **PRESERVED** |
| 1000 | L12488–L12494 | QMOVING @ L12474 | `(defrule     (timer-triggered t-ranged-retreat)` | — | t-ranged-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1000 | **PRESERVED** |
| 1001 | L12496–L12504 | QMOVING @ L12474 | `(defrule     (up-compare-goal gl-mangos-nearby >= 1)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1001 | **PRESERVED** |
| 1002 | L12506–L12515 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1003 | L12517–L12526 | QMOVING @ L12474 | `(defrule     (up-compare-goal lt < 1)     (up-group-size c: RangedGroup > 0)     (up-compare-goal gl-mangos-nearby >= 1)     (up-point-distance ranged-group-x home-x >= 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1003 | **PRESERVED** |
| 1004 | L12528–L12538 | QMOVING @ L12474 | `(defrule     (game-time > 10)     (up-group-size c: RangedGroup > 0)     (up-point-distance ranged-group-x home-x >= 8)     (up-point-distance ranged-group-x enemy-group-x < 20)...` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1004 | **PRESERVED** |
| 1005 | L12540–L12548 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (player-valid 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1005 | **PRESERVED** |
| 1006 | L12550–L12561 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (not(player-valid 5))     (or	(up-compare-goal SUPERIORITY < 5)     (or	(current-age-time < 30)     (up-research-status c: castle-age == research...` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1006 | **PRESERVED** |
| 1007 | L12563–L12572 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (not(player-valid 5))     (up-compare-goal SUPERIORITY >= 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1007 | **PRESERVED** |
| 1008 | L12574–L12579 | QMOVING @ L12474 | `(defrule     (true)` | goal, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1008 | **PRESERVED** |
| 1009 | L12581–L12585 | QMOVING @ L12474 | `(defrule     (up-point-distance ranged-group-x home-x > 40)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1009 | **PRESERVED** |
| 1010 | L12587–L12591 | QMOVING @ L12474 | `(defrule     (up-point-distance enemy-x ranged-group-x < 30)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1010 | **PRESERVED** |
| 1011 | L12593–L12598 | QMOVING @ L12474 | `(defrule     (up-point-distance ranged-group-x home-x < 15)` | goal, goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1011 | **PRESERVED** |
| 1012 | L12600–L12604 | QMOVING @ L12474 | `(defrule     (up-compare-goal gl-enemy-group-size < 1)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1012 | **PRESERVED** |
| 1013 | L12606–L12615 | QMOVING @ L12474 | `(defrule     (up-timer-status t-ranged-retreat == timer-running)     (or	(goal gl-fifth-turn 1)     (up-compare-goal gl-ranged-group-state != HOME-RETREAT))` | split | t-ranged-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1013 | **PRESERVED** |
| 1014 | L12617–L12622 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1014 | **PRESERVED** |
| 1015 | L12624–L12637 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (up-compare-goal gl-ranged-retreat != 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1015 | **PRESERVED** |
| 1016 | L12639–L12652 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)     (goal gl-ranged-retreat 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1016 | **PRESERVED** |
| 1017 | L12655–L12659 | QMOVING @ L12474 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 13 | ShadowByzantine/ShadowByzantine.per#1017 | **PRESERVED** |
| 1018 | L12661–L12674 | QMOVING @ L12474 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5, goal6 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1018 | **PRESERVED** |
| 1019 | L12676–L12682 | QMOVING @ L12474 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-castle-x < CastleRetreat...` | goal5 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1019 | **PRESERVED** |
| 1020 | L12684–L12690 | QMOVING @ L12474 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-tc-x < TCRetreatDistance)` | goal2 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1020 | **PRESERVED** |
| 1021 | L12692–L12697 | QMOVING @ L12474 | `(defrule     (not(research-completed ri-leather-archer-armor))     (up-point-distance ranged-group-x nearest-tc-x < 9)` | goal2 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1021 | **PRESERVED** |
| 1022 | L12699–L12704 | QMOVING @ L12474 | `(defrule     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)     (up-compare-goal gl-army-damage-potential < CostOfIgnoringTowers)` | goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1022 | **PRESERVED** |
| 1023 | L12706–L12710 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1024 | L12712–L12723 | QMOVING @ L12474 | `(defrule     (false)     (goal gl-can-move YES)     (up-point-distance home-x ranged-group-x < 20)     (up-timer-status t-ranged-retreat != timer-running)     (up-compare-goal g...` | split | t-ranged-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1024 | **PRESERVED** |
| 1025 | L12725–L12734 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1026 | L12736–L12745 | QMOVING @ L12474 | `(defrule     (goal SPLIT 2)     (or (and(up-compare-goal gl-target-distance g:<= goal)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1026 | **PRESERVED** |
| 1027 | L12747–L12762 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1028 | L12764–L12775 | QMOVING @ L12474 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1029 | L12777–L12789 | QMOVING @ L12474 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1029; ShadowByzantine/ShadowByzantine.per#1129 | **PRESERVED** |
| 1030 | L12791–L12795 | QMOVING @ L12474 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 1031 | L12799–L12807 | QCCR @ L12797 | `(defrule     (true)` | goal, goal3, goal4, goal5, goal6 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1031 | **PRESERVED** |
| 1032 | L12809–L12817 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1032 | **PRESERVED** |
| 1033 | L12819–L12832 | QCCR @ L12797 | `(defrule     (up-compare-goal lt >= 1)` | goal | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data, up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1033 | **PRESERVED** |
| 1034 | L12834–L12840 | QCCR @ L12797 | `(defrule     (taunt-detected me 109)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1034 | **PRESERVED** |
| 1035 | L12842–L12847 | QCCR @ L12797 | `(defrule     (taunt-detected me 110)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1035 | **PRESERVED** |
| 1036 | L12849–L12855 | QCCR @ L12797 | `(defrule     (or	(and(up-compare-goal goal >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1036 | **PRESERVED** |
| 1037 | L12858–L12864 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#1037 | **PRESERVED** |
| 1038 | L12866–L12870 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-find-local | — | — | ShadowByzantine/ShadowByzantine.per#1038; ShadowByzantine/ShadowByzantine.per#1064 | **PRESERVED** |
| 1039 | L12872–L12877 | QCCR @ L12797 | `(defrule     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1039 | **PRESERVED** |
| 1040 | L12879–L12884 | QCCR @ L12797 | `(defrule     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1040 | **PRESERVED** |
| 1041 | L12886–L12891 | QCCR @ L12797 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (research-available ri-chain-barding))` | — | — | — | up-find-local | research | — | ShadowByzantine/ShadowByzantine.per#1041 | **PRESERVED** |
| 1042 | L12893–L12897 | QCCR @ L12797 | `(defrule     (up-compare-goal SUPERIORITY < 20)` | — | — | — | up-find-local | — | — | ShadowByzantine/ShadowByzantine.per#1042; ShadowByzantine/ShadowByzantine.per#1069 | **PRESERVED** |
| 1043 | L12899–L12908 | QCCR @ L12797 | `(defrule     (true)` | — | — | — | up-clean-search, up-get-search-state, up-remove-objects | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1043 | **PRESERVED** |
| 1044 | L12910–L12916 | QCCR @ L12797 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1044 | **PRESERVED** |
| 1045 | L12918–L12922 | QCCR @ L12797 | `(defrule     (up-compare-goal gl-ninety-turn < 45)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1045; ShadowByzantine/ShadowByzantine.per#1073 | **PRESERVED** |
| 1046 | L12924–L12928 | QCCR @ L12797 | `(defrule     (up-compare-goal gl-ninety-turn < 75)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1046 | **PRESERVED** |
| 1047 | L12930–L12934 | QCCR @ L12797 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1047 | **PRESERVED** |
| 1048 | L12936–L12947 | QCCR @ L12797 | `(defrule     (up-compare-goal lt > 0)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-point | — | ShadowByzantine/ShadowByzantine.per#1048 | **PRESERVED** |
| 1049 | L12949–L12963 | QCCR @ L12797 | `(defrule     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1049; ShadowByzantine/ShadowByzantine.per#1077 | **PRESERVED** |
| 1050 | L12965–L12970 | QCCR @ L12797 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1050 | **PRESERVED** |
| 1051 | L12974–L12983 | QTCR @ L12972 | `(defrule     (true)` | goal, goal1, goal3, goal4, goal5, goal6 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1051 | **PRESERVED** |
| 1052 | L12985–L12993 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1052 | **PRESERVED** |
| 1053 | L12995–L13008 | QTCR @ L12972 | `(defrule     (up-compare-goal lt >= 1)` | goal | — | — | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | up-get-object-data, up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1053 | **PRESERVED** |
| 1054 | L13010–L13016 | QTCR @ L12972 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1054 | **PRESERVED** |
| 1055 | L13019–L13027 | QTCR @ L12972 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1055 | **PRESERVED** |
| 1056 | L13030–L13037 | QTCR @ L12972 | `(defrule     (false)     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#1056 | **PRESERVED** |
| 1057 | L13039–L13044 | QTCR @ L12972 | `(defrule     (up-compare-goal rt >= 1)     (up-set-target-object search-remote c: 0)` | — | — | — | up-set-target-object | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#1057 | **PRESERVED** |
| 1058 | L13046–L13053 | QTCR @ L12972 | `(defrule     (taunt-detected me 57)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1058 | **PRESERVED** |
| 1059 | L13055–L13060 | QTCR @ L12972 | `(defrule     (taunt-detected me 58)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1059 | **PRESERVED** |
| 1060 | L13062–L13069 | QTCR @ L12972 | `(defrule     (or (up-compare-goal goal1 < 460)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1060 | **PRESERVED** |
| 1061 | L13072–L13078 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#1061 | **PRESERVED** |
| 1062 | L13080–L13084 | QTCR @ L12972 | `(defrule     (goal gl-strategy KRUSH)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1062 | **PRESERVED** |
| 1063 | L13086–L13092 | QTCR @ L12972 | `(defrule     (goal gl-strategy KRUSH)     (up-projectile-detected projectile-town-center c:< 3000)     (up-projectile-target projectile-town-center == cavalry-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1063 | **PRESERVED** |
| 1064 | L13094–L13098 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-find-local | — | — | ShadowByzantine/ShadowByzantine.per#1038; ShadowByzantine/ShadowByzantine.per#1064 | **PRESERVED** |
| 1065 | L13100–L13105 | QTCR @ L12972 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1065 | **PRESERVED** |
| 1066 | L13107–L13114 | QTCR @ L12972 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1067 | L13116–L13126 | QTCR @ L12972 | `(defrule     (goal gl-strategy KRUSH)     (up-projectile-detected projectile-town-center c:< 3000)     (up-projectile-target projectile-town-center == cavalry-class)     (or	(up...` | — | — | — | up-find-local | research, up-research | — | ShadowByzantine/ShadowByzantine.per#1067 | **PRESERVED** |
| 1068 | L13128–L13137 | QTCR @ L12972 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1069 | L13139–L13143 | QTCR @ L12972 | `(defrule     (up-compare-goal SUPERIORITY < 20)` | — | — | — | up-find-local | — | — | ShadowByzantine/ShadowByzantine.per#1042; ShadowByzantine/ShadowByzantine.per#1069 | **PRESERVED** |
| 1070 | L13145–L13152 | QTCR @ L12972 | `(defrule     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))` | — | — | — | up-find-local, up-remove-objects, up-set-target-point | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1070 | **PRESERVED** |
| 1071 | L13154–L13165 | QTCR @ L12972 | `(defrule     (true)` | — | — | — | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1071 | **PRESERVED** |
| 1072 | L13167–L13173 | QTCR @ L12972 | `(defrule     (true)` | goal, goal1, goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1072 | **PRESERVED** |
| 1073 | L13175–L13179 | QTCR @ L12972 | `(defrule     (up-compare-goal gl-ninety-turn < 45)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1045; ShadowByzantine/ShadowByzantine.per#1073 | **PRESERVED** |
| 1074 | L13181–L13185 | QTCR @ L12972 | `(defrule     (up-compare-goal gl-ninety-turn < 75)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1074 | **PRESERVED** |
| 1075 | L13187–L13193 | QTCR @ L12972 | `(defrule     (up-group-size c: RangedGroup > 0)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1075 | **PRESERVED** |
| 1076 | L13195–L13206 | QTCR @ L12972 | `(defrule     (up-compare-goal lt > 0)     (up-set-target-object search-local c: 0)` | — | — | — | up-set-target-object | up-target-point | — | ShadowByzantine/ShadowByzantine.per#1076 | **PRESERVED** |
| 1077 | L13208–L13222 | QTCR @ L12972 | `(defrule     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1049; ShadowByzantine/ShadowByzantine.per#1077 | **PRESERVED** |
| 1078 | L13224–L13229 | QTCR @ L12972 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1078 | **PRESERVED** |
| 1079 | L13232–L13236 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 12 | ShadowByzantine/ShadowByzantine.per#75; ShadowByzantine/ShadowByzantine.per#1079 | **PRESERVED** |
| 1080 | L13238–L13245 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: RangedGroup >= 7)     (up-point-distance march-x enemy-x >= 40)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1080 | **PRESERVED** |
| 1081 | L13247–L13254 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal, goal1, goal2, goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#767; ShadowByzantine/ShadowByzantine.per#1081 | **PRESERVED** |
| 1082 | L13256–L13263 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-castle-x != -1)     (or	(up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ra...` | goal3 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1082 | **PRESERVED** |
| 1083 | L13265–L13272 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-tc-x != -1)     (or	(up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged...` | goal | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1083 | **PRESERVED** |
| 1084 | L13274–L13281 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-tc-x != -1)     (up-point-distance ranged-group-x nearest-tc-x < 9)     (or (up-compare-goal SUPERIORITY < 20)     (not(research-completed ...` | goal | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1084 | **PRESERVED** |
| 1085 | L13283–L13288 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: KnightGroup > 0)     (up-point-distance ranged-group-x knight-group-x >= 12)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1085; ShadowByzantine/ShadowByzantine.per#1100 | **PRESERVED** |
| 1086 | L13290–L13296 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal nearest-tower-x != -1)     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)     (up-compare-goal gl-army-damage-potential ...` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1086 | **PRESERVED** |
| 1087 | L13298–L13305 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (timer-triggered t-failsafe)     (up-timer-status t-ranged-retreat != timer-running)` | — | t-failsafe, t-ranged-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1087 | **PRESERVED** |
| 1088 | L13307–L13314 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-timer-status t-ranged-retreat != timer-running)     (or	(goal gl-fifth-turn 1)     (up-compare-goal gl-ranged-group-state != MARCHING))     (up-compare-goal gl-...` | split | t-ranged-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1088 | **PRESERVED** |
| 1089 | L13316–L13325 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1089 | **PRESERVED** |
| 1090 | L13327–L13334 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: tree-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1090 | **PRESERVED** |
| 1091 | L13336–L13349 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1092 | L13351–L13356 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (taunt-detected me 55)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1092 | **PRESERVED** |
| 1093 | L13358–L13365 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (taunt-detected me 56)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1093 | **PRESERVED** |
| 1094 | L13367–L13376 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (taunt-detected me 37)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1094 | **PRESERVED** |
| 1095 | L13379–L13391 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5, goal6 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1095 | **PRESERVED** |
| 1096 | L13393–L13397 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-point-distance ranged-group-x enemy-group-x < 6)` | goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1096 | **PRESERVED** |
| 1097 | L13399–L13406 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-castle-x < CastleRetreat...` | goal3, goal6 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1097 | **PRESERVED** |
| 1098 | L13408–L13415 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-tc-x < TCRetreatDistance)` | goal, goal3 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1098 | **PRESERVED** |
| 1099 | L13417–L13423 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (not(research-completed ri-leather-archer-armor))     (up-point-distance ranged-group-x nearest-tc-x < 10)` | goal, goal3 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1099 | **PRESERVED** |
| 1100 | L13425–L13430 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-group-size c: KnightGroup > 0)     (up-point-distance ranged-group-x knight-group-x >= 12)` | goal1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1085; ShadowByzantine/ShadowByzantine.per#1100 | **PRESERVED** |
| 1101 | L13432–L13437 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)     (up-compare-goal gl-army-damage-potential < CostOfIgnoringTowers)` | goal2 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1101 | **PRESERVED** |
| 1102 | L13439–L13443 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal gl-melee-in-range >= 3)` | goal4 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1102 | **PRESERVED** |
| 1103 | L13445–L13449 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1104 | L13451–L13457 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1105 | L13459–L13466 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal gl-can-move YES)     (up-compare-goal gl-melee-in-range >= 1)     (up-point-distance point-x ranged-group-x >= 3)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1105 | **PRESERVED** |
| 1106 | L13468–L13482 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#1106 | **PRESERVED** |
| 1107 | L13484–L13490 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1107; ShadowByzantine/ShadowByzantine.per#1127 | **PRESERVED** |
| 1108 | L13492–L13502 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1108 | **PRESERVED** |
| 1109 | L13505–L13510 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | gl-direction | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1109 | **PRESERVED** |
| 1110 | L13512–L13527 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal, goal1, goal2, goal3, goal4, goal5, goal6, goal7, goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1110 | **PRESERVED** |
| 1111 | L13529–L13533 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (research-completed ri-elite-skirmisher)` | goal6 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1111 | **PRESERVED** |
| 1112 | L13535–L13550 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal gl-can-move YES)     (up-compare-goal gl-melee-in-range < 1)     (up-compare-goal gl-enemy-group-size >= 1)     (up-compare-goal gl-target-distance g:<= goal8)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1112 | **PRESERVED** |
| 1113 | L13553–L13560 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal gl-thirty-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1113 | **PRESERVED** |
| 1114 | L13562–L13567 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1114 | **PRESERVED** |
| 1115 | L13569–L13575 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1116 | L13577–L13584 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1117 | L13586–L13592 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1118 | L13594–L13600 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1119 | L13602–L13606 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1119 | **PRESERVED** |
| 1120 | L13609–L13616 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | goal2, goal3, goal7, goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1120 | **PRESERVED** |
| 1121 | L13618–L13624 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 30)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-castle-x < CastleRetreat...` | goal8 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1121 | **PRESERVED** |
| 1122 | L13626–L13632 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (or (up-compare-goal SUPERIORITY < 20)     (not(research-completed ri-leather-archer-armor)))     (up-point-distance ranged-group-x nearest-tc-x < TCRetreatDistance)` | goal2 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1122 | **PRESERVED** |
| 1123 | L13634–L13639 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (not(research-completed ri-leather-archer-armor))     (up-point-distance ranged-group-x nearest-tc-x < 9)` | goal2 | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1123 | **PRESERVED** |
| 1124 | L13641–L13646 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (up-compare-goal SUPERIORITY < 10)     (up-point-distance ranged-group-x nearest-tower-x < TowerRetreatDistance)` | goal3 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1124 | **PRESERVED** |
| 1125 | L13648–L13652 | QMARCH TO ENEMY BASE @ L13231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1126 | L13655–L13663 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1127 | L13665–L13671 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (up-point-contains point-x c: building-class)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1107; ShadowByzantine/ShadowByzantine.per#1127 | **PRESERVED** |
| 1128 | L13673–L13679 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)     (false)     (up-point-distance point-x ranged-group-x < 15)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1128 | **PRESERVED** |
| 1129 | L13681–L13691 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1029; ShadowByzantine/ShadowByzantine.per#1129 | **PRESERVED** |
| 1130 | L13693–L13699 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (goal goal7 3)     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1130 | **PRESERVED** |
| 1131 | L13701–L13705 | QMARCH TO ENEMY BASE @ L13231 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 1132 | L13708–L13712 | QCOMBAT MODE @ L13707 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 7 | ShadowByzantine/ShadowByzantine.per#1132 | **PRESERVED** |
| 1133 | L13714–L13719 | QCOMBAT MODE @ L13707 | `(defrule     (or	(game-time < 5)     (goal RETREATING 0))` | — | — | — | — | — | 6 | ShadowByzantine/ShadowByzantine.per#1133 | **PRESERVED** |
| 1134 | L13721–L13726 | QCOMBAT MODE @ L13707 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1134 | **PRESERVED** |
| 1135 | L13728–L13733 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1135 | **PRESERVED** |
| 1136 | L13735–L13743 | QCOMBAT MODE @ L13707 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1137 | L13747–L13759 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1138 | L13763–L13775 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1139 | L13778–L13786 | QCOMBAT MODE @ L13707 | `(defrule     (false)     (goal gl-can-fire YES)     (up-group-size c: RangedGroup >= 23)     (up-compare-goal gl-ranged-group-state != FIRING)     (up-timer-status t-ranged-retr...` | split | t-ranged-retreat | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1139 | **PRESERVED** |
| 1140 | L13788–L13801 | QCOMBAT MODE @ L13707 | `(defrule     (goal SPLIT 1)` | — | — | — | — | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#1140 | **PRESERVED** |
| 1141 | L13811–L13822 | QFAILSAFE @ L13810 | `(defrule     (food-amount < 400)     (gold-amount >= 180)     (goal gl-fifth-turn 1)     (unit-type-count-total archer >= 2)     (up-compare-sn sn-gold-gatherer-percentage > 0) ...` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage | — | — | — | research-pending, unit-type-count-total, up-research | — | ShadowByzantine/ShadowByzantine.per#1141 | **PRESERVED** |
| 1142 | L13826–L13834 | QDARK @ L13824 | `(defrule     (true)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1142 | **PRESERVED** |
| 1143 | L13837–L13849 | QDARK @ L13824 | `(defrule     (current-age-time >= 15)     (civilian-population >= 7)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-maximum-wood-drop-distance, sn-stone-gatherer-percentage, sn-wood-dropsite-distance, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1143 | **PRESERVED** |
| 1144 | L13851–L13859 | QDARK @ L13824 | `(defrule     (civilian-population >= 14)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1144 | **PRESERVED** |
| 1145 | L13862–L13866 | QKRUSH @ L13861 | `(defrule     (up-compare-goal gl-strategy != KRUSH)` | — | — | — | — | — | 8 | ShadowByzantine/ShadowByzantine.per#1145 | **PRESERVED** |
| 1146 | L13870–L13879 | QKRUSH @ L13861 | `(defrule     (civilian-population >= 15)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1146 | **PRESERVED** |
| 1147 | L13882–L13892 | QKRUSH @ L13861 | `(defrule     (false)     (civilian-population >= 16)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1147 | **PRESERVED** |
| 1148 | L13895–L13906 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1148 | **PRESERVED** |
| 1149 | L13909–L13921 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)     (up-research-status c: feudal-age >= research-pending)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1149 | **PRESERVED** |
| 1150 | L13925–L13935 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (up-research-status c: castle-age >= research-pending)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1150 | **PRESERVED** |
| 1151 | L13939–L13949 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (current-age >= castle-age)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1151 | **PRESERVED** |
| 1152 | L13952–L13964 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (current-age >= castle-age)     (or	(current-age-time >= 220)     (building-type-count-total farm >= 19))` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1152 | **PRESERVED** |
| 1153 | L13967–L13978 | QKRUSH @ L13861 | `(defrule     (game-time > 10)     (current-age-time >= 480)     (current-age >= castle-age)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1153 | **PRESERVED** |
| 1154 | L13983–L13989 | QFLUSH @ L13980 | `(defrule     (civilian-population == 18)     (goal gl-strategy FLUSH)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1154 | **PRESERVED** |
| 1155 | L13991–L14005 | QFLUSH @ L13980 | `(defrule     (goal SPLIT 1)     (food-amount < 230)     (or	(up-compare-goal gl-killed-boar-count < 2)     (and(up-compare-goal gl-killed-deer-count < 1)     (up-compare-goal gl...` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1155 | **PRESERVED** |
| 1156 | L14007–L14017 | QFLUSH @ L13980 | `(defrule     (goal SPLIT 1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1156 | **PRESERVED** |
| 1157 | L14020–L14030 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (or	(food-amount > 490)     (up-compare-goal gl-age-loading == FA-loading))` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1157 | **PRESERVED** |
| 1158 | L14033–L14042 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (current-age == feudal-age)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1158 | **PRESERVED** |
| 1159 | L14045–L14054 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count-total blacksmith >= 1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1159 | **PRESERVED** |
| 1160 | L14057–L14066 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (up-research-status c: ri-fletching >= research-pending)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1160 | **PRESERVED** |
| 1161 | L14069–L14081 | QFLUSH @ L13980 | `(defrule     (game-time > 10)     (goal gl-strategy FLUSH)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1161 | **PRESERVED** |
| 1162 | L14084–L14098 | QFLUSH @ L13980 | `(defrule     (game-time > 10)     (goal gl-strategy FLUSH)     (dropsite-min-distance gold < 5)     (dropsite-min-distance gold > -1)     (dropsite-min-distance stone < 5)     (...` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1162 | **PRESERVED** |
| 1163 | L14101–L14111 | QFLUSH @ L13980 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count-total market >= 1)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1163 | **PRESERVED** |
| 1164 | L14115–L14124 | QKNIGHTS @ L14113 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-age-loading >= CA-loading)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1164 | **PRESERVED** |
| 1165 | L14127–L14137 | QKNIGHTS @ L14113 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-age-loading >= CA-loading)     (up-compare-goal gl-build-progress >= EskirmsNumber)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1165 | **PRESERVED** |
| 1166 | L14140–L14149 | QKNIGHTS @ L14113 | `(defrule     (current-age == castle-age)     (goal gl-strategy FLUSH)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1166 | **PRESERVED** |
| 1167 | L14152–L14163 | QKNIGHTS @ L14113 | `(defrule     (current-age-time > 300)     (current-age == castle-age)     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress >= ChainBardingNumber)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1167 | **PRESERVED** |
| 1168 | L14166–L14176 | QKNIGHTS @ L14113 | `(defrule     (current-age-time > 600)     (current-age == castle-age)     (goal gl-strategy FLUSH)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1168 | **PRESERVED** |
| 1169 | L14180–L14189 | QSIEGE @ L14178 | `(defrule     (goal gl-strategy SIEGE)     (up-compare-goal gl-age-loading >= CA-loading)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1169 | **PRESERVED** |
| 1170 | L14192–L14201 | QSIEGE @ L14178 | `(defrule     (current-age == castle-age)     (goal gl-strategy SIEGE)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1170 | **PRESERVED** |
| 1171 | L14204–L14214 | QSIEGE @ L14178 | `(defrule     (current-age-time > 300)     (current-age == castle-age)     (goal gl-strategy SIEGE)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-stone-gatherer-percentage, sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1171 | **PRESERVED** |
| 1172 | L14294–L14307 | QSCALEMAIL @ L14293 | `(defrule     (goal gl-strategy FLUSH)     (game-time >= 1080)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1172 | **PRESERVED** |
| 1173 | L14309–L14313 | QSCALEMAIL @ L14293 | `(defrule     (goal gl-progression-pause SCALEMAIL)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1173 | **PRESERVED** |
| 1174 | L14315–L14324 | QSCALEMAIL @ L14293 | `(defrule     (goal gl-progression-pause SCALEMAIL)     (can-research-with-escrow ri-scale-mail)` | gl-progression-pause | — | can-research-with-escrow, set-escrow-percentage | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1174 | **PRESERVED** |
| 1175 | L14327–L14340 | QCHAINMAIL @ L14326 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (research-completed ri-pikeman)     (up-research-status c: ri-chain-mail < research-pending)     (up...` | gl-progression-pause | — | — | — | research, research-completed, research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1175 | **PRESERVED** |
| 1176 | L14342–L14347 | QCHAINMAIL @ L14326 | `(defrule     (goal gl-progression-pause CHAINMAIL)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1176 | **PRESERVED** |
| 1177 | L14349–L14360 | QCHAINMAIL @ L14326 | `(defrule     (goal gl-progression-pause CHAINMAIL)     (can-research-with-escrow ri-chain-mail)` | gl-progression-pause | — | can-research-with-escrow, set-escrow-percentage | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1177 | **PRESERVED** |
| 1178 | L14364–L14372 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item IRONCASTING)     (can-research-with-escrow ri-iron-casting)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1178 | **PRESERVED** |
| 1179 | L14374–L14380 | QIRONCASTING @ L14362 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1180 | L14382–L14389 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != IRONCASTING)     (up-compare-goal gl-build-progress == KrushIronCastingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1180 | **PRESERVED** |
| 1181 | L14391–L14400 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == IRONCASTING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1181 | **PRESERVED** |
| 1182 | L14402–L14409 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item IRONCASTING)     (up-research-status c: ri-iron-casting >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1182 | **PRESERVED** |
| 1183 | L14412–L14420 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item IRONCASTING)     (can-research-with-escrow ri-iron-casting)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1183 | **PRESERVED** |
| 1184 | L14422–L14428 | QIRONCASTING @ L14362 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1185 | L14430–L14437 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != IRONCASTING)     (up-compare-goal gl-build-progress == IronCastingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1185 | **PRESERVED** |
| 1186 | L14439–L14448 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == IRONCASTING)` | — | — | release-escrow, set-escrow-percentage, up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1186 | **PRESERVED** |
| 1187 | L14450–L14457 | QIRONCASTING @ L14362 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item IRONCASTING)     (up-research-status c: ri-iron-casting >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1187 | **PRESERVED** |
| 1188 | L14461–L14469 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item FORGING)     (can-research-with-escrow ri-forging)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1188 | **PRESERVED** |
| 1189 | L14471–L14477 | QFORGING @ L14459 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1190 | L14479–L14487 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != FORGING)     (up-compare-goal gl-build-progress == ForgingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1190 | **PRESERVED** |
| 1191 | L14489–L14499 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == FORGING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1191 | **PRESERVED** |
| 1192 | L14501–L14508 | QFORGING @ L14459 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item FORGING)     (up-research-status c: ri-forging >= research-pending)` | gl-build-progress | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1192 | **PRESERVED** |
| 1193 | L14511–L14519 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item FORGING)     (can-research-with-escrow ri-forging)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1193 | **PRESERVED** |
| 1194 | L14521–L14527 | QFORGING @ L14459 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1195 | L14529–L14536 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != FORGING)     (up-compare-goal gl-build-progress == KrushForgingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1195 | **PRESERVED** |
| 1196 | L14538–L14548 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == FORGING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1196 | **PRESERVED** |
| 1197 | L14550–L14557 | QFORGING @ L14459 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item FORGING)     (up-research-status c: ri-forging >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1197 | **PRESERVED** |
| 1198 | L14561–L14569 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item CHAINBARDING)     (can-research-with-escrow ri-chain-barding)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1198 | **PRESERVED** |
| 1199 | L14571–L14577 | QCHAINBARDING @ L14559 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1200 | L14579–L14586 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != CHAINBARDING)     (up-compare-goal gl-build-progress == KrushChainBardingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1200 | **PRESERVED** |
| 1201 | L14588–L14599 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (current-age-time >= 460)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == CHAINBARDING)` | — | — | set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1201 | **PRESERVED** |
| 1202 | L14601–L14608 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item CHAINBARDING)     (up-research-status c: ri-chain-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1202 | **PRESERVED** |
| 1203 | L14611–L14619 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item CHAINBARDING)     (can-research-with-escrow ri-chain-barding)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1203 | **PRESERVED** |
| 1204 | L14621–L14627 | QCHAINBARDING @ L14559 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1205 | L14629–L14636 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != CHAINBARDING)     (up-compare-goal gl-build-progress == ChainBardingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1205 | **PRESERVED** |
| 1206 | L14638–L14647 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == CHAINBARDING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1206 | **PRESERVED** |
| 1207 | L14649–L14656 | QCHAINBARDING @ L14559 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item CHAINBARDING)     (up-research-status c: ri-chain-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1207 | **PRESERVED** |
| 1208 | L14660–L14670 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (current-age-time >= 180)     (current-age == castle-age)     (goal gl-progression-pause -1)     (goal gl-current-build-item SCALEBARDI...` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1208 | **PRESERVED** |
| 1209 | L14672–L14678 | QSCALEBARDING @ L14658 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1210 | L14680–L14687 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != SCALEBARDING)     (up-compare-goal gl-build-progress == KrushScaleBardingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1210 | **PRESERVED** |
| 1211 | L14689–L14702 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (current-age-time >= 180)     (current-age == castle-age)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-curr...` | — | — | set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1211 | **PRESERVED** |
| 1212 | L14704–L14711 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item SCALEBARDING)     (up-research-status c: ri-scale-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1212 | **PRESERVED** |
| 1213 | L14714–L14722 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item SCALEBARDING)     (can-research-with-escrow ri-scale-barding)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1213 | **PRESERVED** |
| 1214 | L14724–L14730 | QSCALEBARDING @ L14658 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1215 | L14732–L14739 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != SCALEBARDING)     (up-compare-goal gl-build-progress == ScaleBardingNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1215 | **PRESERVED** |
| 1216 | L14741–L14751 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == SCALEBARDING)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1216 | **PRESERVED** |
| 1217 | L14753–L14760 | QSCALEBARDING @ L14658 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item SCALEBARDING)     (up-research-status c: ri-scale-barding >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1217 | **PRESERVED** |
| 1218 | L14763–L14772 | QXBOW @ L14762 | `(defrule     (current-age >= castle-age)     (goal gl-progression-pause -1)     (unit-type-count-total archer-line >= 4)     (up-compare-goal gl-build-progress >= BowsawNumber) ...` | gl-progression-pause | — | — | — | research-pending, unit-type-count-total, up-research | — | ShadowByzantine/ShadowByzantine.per#1218 | **PRESERVED** |
| 1219 | L14774–L14782 | QXBOW @ L14762 | `(defrule     (goal gl-progression-pause XBOW)     (up-can-research gl-escrow-state c: ri-crossbow)` | gl-progression-pause | — | — | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1219 | **PRESERVED** |
| 1220 | L14785–L14798 | QPIKES @ L14784 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-enemy-civ NORMAL)     (current-age >= castle-age)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-bui...` | split | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1220 | **PRESERVED** |
| 1221 | L14800–L14808 | QPIKES @ L14784 | `(defrule     (goal SPLIT 1)` | gl-progression-pause | — | set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1221 | **PRESERVED** |
| 1222 | L14810–L14821 | QPIKES @ L14784 | `(defrule     (goal gl-progression-pause PIKES)     (can-research-with-escrow ri-pikeman)` | gl-progression-pause | — | can-research-with-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1222 | **PRESERVED** |
| 1223 | L14825–L14833 | QAGE @ L14823 | `(defrule     (goal gl-strategy KRUSH)     (research-available feudal-age)     (up-compare-goal gl-need-vills != NO)     (unit-type-count-total villager >= KrushDarkAgeVills)` | — | — | — | — | research, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1223 | **PRESERVED** |
| 1224 | L14835–L14842 | QAGE @ L14823 | `(defrule     (goal gl-strategy FLUSH)     (research-available feudal-age)     (up-compare-goal gl-need-vills != NO)     (unit-type-count-total villager >= FlushDarkAgeVills)` | gl-need-vills | — | — | — | research, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1224 | **PRESERVED** |
| 1225 | L14844–L14852 | QAGE @ L14823 | `(defrule     (goal gl-strategy FLUSH)     (research-available feudal-age)     (up-compare-goal gl-need-vills == NO)     (unit-type-count-total villager < FlushDarkAgeVills)` | gl-need-vills | — | — | — | research, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1225 | **PRESERVED** |
| 1226 | L14854–L14866 | QAGE @ L14823 | `(defrule     (can-research feudal-age)     (or	(and(goal gl-strategy FLUSH)     (unit-type-count-total villager >= FlushDarkAgeVills))     (and(goal gl-strategy KRUSH)     (unit...` | gl-age-loading | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1226 | **PRESERVED** |
| 1227 | L14870–L14879 | QCUP @ L14868 | `(defrule     (goal gl-strategy KRUSH)     (current-age == feudal-age)     (up-compare-goal gl-need-vills != NO)     (up-research-status c: castle-age < research-pending)     (un...` | — | — | — | — | research-pending, unit-type-count-total, up-research | — | ShadowByzantine/ShadowByzantine.per#1227 | **PRESERVED** |
| 1228 | L14881–L14891 | QCUP @ L14868 | `(defrule     (food-amount >= 640)     (gold-amount >= 150)     (goal gl-strategy FLUSH)     (research-available castle-age)     (or (goal gl-current-build-item CUP)     (unit-ty...` | gl-need-vills | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#1228 | **PRESERVED** |
| 1229 | L14893–L14905 | QCUP @ L14868 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item CUP)     (can-research-with-escrow castle-age)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1229 | **PRESERVED** |
| 1230 | L14908–L14914 | QCUP @ L14868 | `(defrule     (goal gl-current-build-item CUP)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1230 | **PRESERVED** |
| 1231 | L14917–L14923 | QCUP @ L14868 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress > CupNumber)     (up-research-status c: castle-age < research-pending)` | gl-build-progress | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1231 | **PRESERVED** |
| 1232 | L14925–L14932 | QCUP @ L14868 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-build-progress > KrushCupNumber)     (up-research-status c: castle-age < research-pending)` | gl-build-progress | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1232 | **PRESERVED** |
| 1233 | L14934–L14942 | QCUP @ L14868 | `(defrule     (goal gl-strategy KRUSH)     (current-age == feudal-age)     (up-compare-goal gl-current-build-item != CUP)     (up-compare-goal gl-build-progress == KrushCupNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1233 | **PRESERVED** |
| 1234 | L14944–L14956 | QCUP @ L14868 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-enemy-strategy-type FC)     (up-compare-goal gl-current-build-item != CUP)     (up-compare-goal gl-build-progress == CupNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1234 | **PRESERVED** |
| 1235 | L14958–L14971 | QCUP @ L14868 | `(defrule     (goal gl-strategy FLUSH)     (research-available castle-age)     (goal gl-enemy-strategy-type FLUSH)     (up-compare-goal gl-current-build-item != CUP)     (up-comp...` | — | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#1235 | **PRESERVED** |
| 1236 | L14974–L14985 | QFLTCH @ L14973 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item FLTCH)     (can-research-with-escrow ri-fletching)` | — | — | can-research-with-escrow, release-escrow, set-escrow-percentage | — | research | — | ShadowByzantine/ShadowByzantine.per#1236 | **PRESERVED** |
| 1237 | L14987–L14993 | QFLTCH @ L14973 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1238 | L14995–L15004 | QFLTCH @ L14973 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress == 9)     (up-compare-goal gl-current-build-item != FLTCH)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1238 | **PRESERVED** |
| 1239 | L15006–L15014 | QFLTCH @ L14973 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count blacksmith >= 1)     (up-compare-goal gl-current-build-item == FLTCH)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1239 | **PRESERVED** |
| 1240 | L15016–L15022 | QFLTCH @ L14973 | `(defrule     (goal gl-current-build-item FLTCH)     (up-research-status c: ri-fletching >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1240 | **PRESERVED** |
| 1241 | L15025–L15032 | QLAA @ L15024 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item LAA)     (can-research-with-escrow ri-leather-archer-armor)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1241 | **PRESERVED** |
| 1242 | L15034–L15040 | QLAA @ L15024 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1243 | L15042–L15051 | QLAA @ L15024 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LAA)     (up-compare-goal gl-build-progress == LeatherArcherArmorNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1243 | **PRESERVED** |
| 1244 | L15053–L15062 | QLAA @ L15024 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == LAA)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1244 | **PRESERVED** |
| 1245 | L15064–L15070 | QLAA @ L15024 | `(defrule     (goal gl-current-build-item LAA)     (up-research-status c: ri-leather-archer-armor >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1245 | **PRESERVED** |
| 1246 | L15073–L15082 | QPAA @ L15072 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item PAA)     (can-research-with-escrow ri-padded-archer-armor)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1246 | **PRESERVED** |
| 1247 | L15084–L15090 | QPAA @ L15072 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1248 | L15092–L15100 | QPAA @ L15072 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != PAA)     (up-compare-goal gl-build-progress == PaddedArcherArmorNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1248 | **PRESERVED** |
| 1249 | L15102–L15111 | QPAA @ L15072 | `(defrule     (goal gl-current-build-item PAA)     (up-research-status c: ri-fletching >= research-complete)` | — | — | release-escrow, set-escrow-percentage, up-modify-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1249 | **PRESERVED** |
| 1250 | L15113–L15119 | QPAA @ L15072 | `(defrule     (goal gl-current-build-item PAA)     (up-research-status c: ri-padded-archer-armor >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1250 | **PRESERVED** |
| 1251 | L15122–L15129 | QBODKIN @ L15121 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item BODKIN)     (can-research-with-escrow ri-bodkin-arrow)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1251 | **PRESERVED** |
| 1252 | L15131–L15137 | QBODKIN @ L15121 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1253 | L15139–L15146 | QBODKIN @ L15121 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != BODKIN)     (up-compare-goal gl-build-progress == BodkinNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1253 | **PRESERVED** |
| 1254 | L15148–L15156 | QBODKIN @ L15121 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == BODKIN)` | — | — | set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1254 | **PRESERVED** |
| 1255 | L15158–L15165 | QBODKIN @ L15121 | `(defrule     (false)     (up-compare-goal gl-current-build-item == BODKIN)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1255 | **PRESERVED** |
| 1256 | L15167–L15173 | QBODKIN @ L15121 | `(defrule     (goal gl-current-build-item BODKIN)     (up-research-status c: ri-bodkin-arrow >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1256 | **PRESERVED** |
| 1257 | L15176–L15185 | QLOOM @ L15175 | `(defrule     (research-available ri-loom)     (unit-type-count villager >= 9)     (up-timer-status t-relure != timer-running)     (dropsite-min-distance live-boar < max-bh-dista...` | gl-need-vills | t-relure | — | — | research | — | ShadowByzantine/ShadowByzantine.per#1257 | **PRESERVED** |
| 1258 | L15187–L15199 | QLOOM @ L15175 | `(defrule     (can-research ri-loom)     (or	(and(game-time > 35)     (housing-headroom < 1))     (or	(goal gl-need-vills LOOM)     (or	(current-age > dark-age)     (and(food-amo...` | gl-need-vills | — | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1258 | **PRESERVED** |
| 1259 | L15202–L15209 | QMONKS @ L15201 | `(defrule     (can-train monk)     (unit-type-count-total monk < 3)` | — | — | — | — | train, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1259 | **PRESERVED** |
| 1260 | L15211–L15218 | QMONKS @ L15201 | `(defrule     (can-train monk)     (unit-type-count-total monk < 3)` | — | — | — | — | train, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1260 | **PRESERVED** |
| 1261 | L15220–L15227 | QMONKS @ L15201 | `(defrule     (can-train monk)     (unit-type-count-total monk < 3)` | — | — | — | — | train, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1261 | **PRESERVED** |
| 1262 | L15230–L15238 | QMANGOS @ L15229 | `(defrule     (goal gl-town-safe NO)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1262 | **PRESERVED** |
| 1263 | L15240–L15250 | QMANGOS @ L15229 | `(defrule     (false)     (goal gl-town-safe NO)     (up-compare-goal rt >= 10)     (up-compare-goal SUPERIORITY < 10)     (can-train-with-escrow mangonel-line)` | — | — | can-train-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1263 | **PRESERVED** |
| 1264 | L15252–L15260 | QMANGOS @ L15229 | `(defrule     (not(goal SIEGE RAMS))     (can-train mangonel-line)     (goal gl-strategy SIEGE)     (unit-type-count-total scorpion-line >= 5)` | — | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1264 | **PRESERVED** |
| 1265 | L15262–L15269 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE 3)     (can-train-with-escrow mangonel-line)` | — | — | can-train-with-escrow | — | up-train | — | ShadowByzantine/ShadowByzantine.per#1265 | **PRESERVED** |
| 1266 | L15271–L15282 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE 3)     (unit-type-count-total mangonel-line >= 2)` | siege | — | release-escrow, set-escrow-percentage | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1266 | **PRESERVED** |
| 1267 | L15284–L15292 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE 3)     (up-pending-objects c: mangonel-line < 1)     (up-pending-objects c: battering-ram-line < 1)` | — | — | up-modify-escrow | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1267 | **PRESERVED** |
| 1268 | L15294–L15301 | QMANGOS @ L15229 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1269 | L15303–L15318 | QMANGOS @ L15229 | `(defrule     (false)     (goal SIEGE -1)     (current-age >= castle-age)     (building-type-count siege-workshop > 0)     (up-pending-objects c: mangonel-line < 2)     (unit-typ...` | — | — | — | — | unit-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1269 | **PRESERVED** |
| 1270 | L15321–L15334 | QSCORPS @ L15320 | `(defrule     (not(goal SIEGE RAMS))     (can-train scorpion-line)     (goal gl-strategy SIEGE)     (or	(unit-type-count-total scorpion-line < 5)     (or	(and(unit-type-count-tot...` | — | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1270 | **PRESERVED** |
| 1271 | L15337–L15347 | QRAMS @ L15336 | `(defrule     (goal SIEGE RAMS)     (or	(and(players-building-type-count target-player castle < 1)     (up-compare-goal gl-army-damage-potential < CostOfPausingForRams))     (or	...` | split | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1271 | **PRESERVED** |
| 1272 | L15349–L15359 | QRAMS @ L15336 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1273 | L15361–L15368 | QRAMS @ L15336 | `(defrule     (goal SIEGE RAMS)     (up-pending-objects c: mangonel-line < 1)     (up-pending-objects c: battering-ram-line < 1)` | — | — | up-modify-escrow | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1273 | **PRESERVED** |
| 1274 | L15370–L15378 | QRAMS @ L15336 | `(defrule     (goal SIEGE RAMS)     (can-train-with-escrow battering-ram-line)` | — | — | can-train-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1274 | **PRESERVED** |
| 1275 | L15380–L15393 | QRAMS @ L15336 | `(defrule     (goal SIEGE -1)     (current-age >= castle-age)     (building-type-count siege-workshop > 0)     (up-pending-objects c: battering-ram < 2)     (or	(unit-type-count-...` | — | — | — | — | unit-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1275 | **PRESERVED** |
| 1276 | L15397–L15407 | QSCOUTS @ L15395 | `(defrule     (goal gl-strategy KRUSH)     (can-train scout-cavalry-line)     (unit-type-count scout-cavalry-line < 1)     (or (food-amount >= 100)     (up-pending-objects c: vil...` | — | — | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1276 | **PRESERVED** |
| 1277 | L15411–L15419 | QKNIGHTS @ L15409 | `(defrule     (can-train knight-line)     (goal gl-strategy KRUSH)     (or (food-amount >= 100)     (up-pending-objects c: villager >= 2))` | — | — | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1277 | **PRESERVED** |
| 1278 | L15422–L15431 | QKNIGHTS @ L15409 | `(defrule     (can-train knight-line)     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause != XBOW)     (up-compare-goal gl-current-build-item != BODKIN)     (u...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1278 | **PRESERVED** |
| 1279 | L15433–L15443 | QKNIGHTS @ L15409 | `(defrule     (unit-type-count knight-line < 4)     (goal gl-strategy FLUSH)     (can-train-with-escrow knight-line)     (up-compare-goal gl-progression-pause != XBOW)     (up-co...` | — | — | can-train-with-escrow | — | up-train | — | ShadowByzantine/ShadowByzantine.per#1279 | **PRESERVED** |
| 1280 | L15446–L15455 | QARCHERS @ L15445 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1281 | L15457–L15470 | QARCHERS @ L15445 | `(defrule     (or	(gold-amount >= 100)     (research-completed ri-fletching))     (up-can-train gl-escrow-state c: archer-line)     (or (unit-type-count-total archer-line < 4)   ...` | — | — | — | — | research, research-completed, research-pending, unit-type-count-total, up-research, up-train | — | ShadowByzantine/ShadowByzantine.per#1281 | **PRESERVED** |
| 1282 | L15474–L15478 | QSKIRMS @ L15472 | `(defrule     (current-age >= castle-age)` | gl-escrow-state | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1282 | **PRESERVED** |
| 1283 | L15480–L15490 | QSKIRMS @ L15472 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1284 | L15492–L15502 | QSKIRMS @ L15472 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1285 | L15504–L15518 | QSKIRMS @ L15472 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1286 | L15520–L15530 | QSKIRMS @ L15472 | `(defrule     (goal SPLIT 1)     (or	(up-compare-goal SUPERIORITY < -5)     (or	(up-compare-goal gl-skirm-total < 35)     (up-research-status c: castle-age >= research-pending)))...` | split | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1286 | **PRESERVED** |
| 1287 | L15532–L15540 | QSKIRMS @ L15472 | `(defrule     (goal SPLIT 2)` | gl-skirm-total | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1287 | **PRESERVED** |
| 1288 | L15542–L15547 | QSKIRMS @ L15472 | `(defrule     (true)` | gl-escrow-state, split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1288; ShadowByzantine/ShadowByzantine.per#1799 | **PRESERVED** |
| 1289 | L15550–L15562 | QMILITIAMAN @ L15549 | `(defrule     (goal gl-enemy-civ MESO)     (can-train militiaman-line)     (or	(and(current-age < castle-age)     (research-completed ri-man-at-arms))     (and(current-age > feud...` | — | — | — | — | research, research-completed, train, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1289 | **PRESERVED** |
| 1290 | L15566–L15579 | QSPEARS @ L15564 | `(defrule     (goal gl-strategy FLUSH)     (can-train spearman-line)     (current-age-time >= 180)     (current-age < castle-age)     (research-completed ri-fletching)     (unit-...` | — | — | — | — | research, research-completed, unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1290 | **PRESERVED** |
| 1291 | L15581–L15594 | QSPEARS @ L15564 | `(defrule     (game-time >= 1080)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1291 | **PRESERVED** |
| 1292 | L15596–L15609 | QSPEARS @ L15564 | `(defrule     (player-valid 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1292 | **PRESERVED** |
| 1293 | L15611–L15623 | QSPEARS @ L15564 | `(defrule     (not(player-valid 5))     (goal gl-strategy FLUSH)     (can-train spearman-line)     (current-age >= castle-age)     (unit-type-count-total spearman-line < 10)     ...` | — | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1293 | **PRESERVED** |
| 1294 | L15626–L15632 | QSPEARS @ L15564 | `(defrule     (goal gl-strategy KRUSH)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1294 | **PRESERVED** |
| 1295 | L15634–L15641 | QSPEARS @ L15564 | `(defrule     (not(player-valid 5))     (goal gl-enemy-civ MESO)     (players-unit-type-count target-player monk < 1)     (players-unit-type-count target-player knight < 1)` | — | — | — | — | — | 2 | ShadowByzantine/ShadowByzantine.per#1295 | **PRESERVED** |
| 1296 | L15643–L15655 | QSPEARS @ L15564 | `(defrule     (unit-type-count-total spearman-line < 6)     (up-compare-goal gl-progression-pause != PIKES)     (up-can-train gl-escrow-state c: spearman-line)     (or	(goal ENEM...` | — | — | — | — | unit-type-count-total, up-train | — | ShadowByzantine/ShadowByzantine.per#1296 | **PRESERVED** |
| 1297 | L15657–L15669 | QSPEARS @ L15564 | `(defrule     (can-train spearman-line)     (up-compare-goal gl-progression-pause != PIKES)     (or	(and(military-population >= 5)     (unit-type-count-total spearman-line < 1)) ...` | — | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1297 | **PRESERVED** |
| 1298 | L15671–L15682 | QSPEARS @ L15564 | `(defrule     (can-train spearman-line)     (unit-type-count-total spearman-line < 6)     (up-compare-goal gl-progression-pause != PIKES)     (or	(goal gl-enemy-civ NORMAL)     (...` | — | — | — | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1298 | **PRESERVED** |
| 1299 | L15686–L15692 | QTOWERS @ L15684 | `(defrule     (or (goal gl-position POCKET)     (or (goal gl-enemy-strategy DRUSH)     (building-type-count-total watch-tower >= 10)))` | — | — | — | — | building-type-count-total | 6 | ShadowByzantine/ShadowByzantine.per#1299 | **PRESERVED** |
| 1300 | L15694–L15698 | QTOWERS @ L15684 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1300 | **PRESERVED** |
| 1301 | L15700–L15704 | QTOWERS @ L15684 | `(defrule     (goal gl-town-safe NO)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1301 | **PRESERVED** |
| 1302 | L15706–L15718 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control -1)     (or (goal gl-position FLANK)     (nand	(current-age-time < 100)     (current-age == feudal-age)))` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1302 | **PRESERVED** |
| 1303 | L15720–L15729 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 0)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1303 | **PRESERVED** |
| 1304 | L15731–L15740 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 1)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1304 | **PRESERVED** |
| 1305 | L15742–L15751 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 2)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1305 | **PRESERVED** |
| 1306 | L15753–L15762 | QTOWERS @ L15684 | `(defrule     (can-build watch-tower)     (goal gl-tower-control 3)` | gl-tower-control, sn-placement-zone-size | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1306 | **PRESERVED** |
| 1307 | L15766–L15770 | QSTABLE @ L15764 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1307; ShadowByzantine/ShadowByzantine.per#1322; ShadowByzantine/ShadowByzantine.per#1336 | **PRESERVED** |
| 1308 | L15772–L15776 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1308; ShadowByzantine/ShadowByzantine.per#1323; ShadowByzantine/ShadowByzantine.per#1365 | **PRESERVED** |
| 1309 | L15778–L15783 | QSTABLE @ L15764 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1309 | **PRESERVED** |
| 1310 | L15786–L15800 | QSTABLE @ L15764 | `(defrule     (food-amount >= 175)     (gold-amount >= 175)     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (up-pending-obj...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-objects, up-pending-placement | — | ShadowByzantine/ShadowByzantine.per#1310 | **PRESERVED** |
| 1311 | L15802–L15808 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1312 | L15810–L15817 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != EXTRA-STABLES)     (up-compare-goal gl-build-progress == KrushExtraStablesNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1312 | **PRESERVED** |
| 1313 | L15819–L15828 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item == EXTRA-STABLES)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1313 | **PRESERVED** |
| 1314 | L15830–L15837 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (building-type-count-total stable >= 4)     (goal gl-current-build-item EXTRA-STABLES)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1314 | **PRESERVED** |
| 1315 | L15839–L15845 | QSTABLE @ L15764 | `(defrule     (up-compare-goal gl-build-progress == KrushFinishedNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1315 | **PRESERVED** |
| 1316 | L15848–L15862 | QSTABLE @ L15764 | `(defrule     (food-amount >= 175)     (gold-amount >= 175)     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (up-pending-obj...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-objects, up-pending-placement | — | ShadowByzantine/ShadowByzantine.per#1316 | **PRESERVED** |
| 1317 | L15864–L15870 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1318 | L15872–L15879 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != EXTRA-STABLES)     (up-compare-goal gl-build-progress == ExtraStablesNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1318 | **PRESERVED** |
| 1319 | L15881–L15890 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == EXTRA-STABLES)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1319 | **PRESERVED** |
| 1320 | L15892–L15899 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (building-type-count-total stable >= 4)     (goal gl-current-build-item EXTRA-STABLES)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1320 | **PRESERVED** |
| 1321 | L15901–L15907 | QSTABLE @ L15764 | `(defrule     (up-compare-goal gl-build-progress == FinishedNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1321 | **PRESERVED** |
| 1322 | L15910–L15914 | QSTABLE @ L15764 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1307; ShadowByzantine/ShadowByzantine.per#1322; ShadowByzantine/ShadowByzantine.per#1336 | **PRESERVED** |
| 1323 | L15916–L15920 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1308; ShadowByzantine/ShadowByzantine.per#1323; ShadowByzantine/ShadowByzantine.per#1365 | **PRESERVED** |
| 1324 | L15922–L15927 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1325 | L15929–L15934 | QSTABLE @ L15764 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1325; ShadowByzantine/ShadowByzantine.per#1731; ShadowByzantine/ShadowByzantine.per#1768 | **PRESERVED** |
| 1326 | L15937–L15948 | QSTABLE @ L15764 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy KRUSH)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE1)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1326 | **PRESERVED** |
| 1327 | L15950–L15957 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1328 | L15959–L15966 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != STABLE1)     (up-compare-goal gl-build-progress == KrushStableNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1328 | **PRESERVED** |
| 1329 | L15968–L15978 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1329 | **PRESERVED** |
| 1330 | L15980–L15987 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item STABLE1)     (building-type-count-total stable >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1330 | **PRESERVED** |
| 1331 | L15990–L16001 | QSTABLE @ L15764 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE1)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1331 | **PRESERVED** |
| 1332 | L16003–L16010 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1333 | L16012–L16020 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != STABLE1)     (up-compare-goal gl-build-progress == Stable1Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1333 | **PRESERVED** |
| 1334 | L16022–L16032 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1334 | **PRESERVED** |
| 1335 | L16034–L16040 | QSTABLE @ L15764 | `(defrule     (goal gl-current-build-item STABLE1)     (building-type-count-total stable >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1335 | **PRESERVED** |
| 1336 | L16043–L16047 | QSTABLE @ L15764 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1307; ShadowByzantine/ShadowByzantine.per#1322; ShadowByzantine/ShadowByzantine.per#1336 | **PRESERVED** |
| 1337 | L16049–L16055 | QSTABLE @ L15764 | `(defrule     (or	(goal gl-strategy KRUSH)     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES)))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1337 | **PRESERVED** |
| 1338 | L16057–L16062 | QSTABLE @ L15764 | `(defrule     (not(player-valid 3))     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1338 | **PRESERVED** |
| 1339 | L16065–L16077 | QSTABLE @ L15764 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE2)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1339 | **PRESERVED** |
| 1340 | L16079–L16085 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1341 | L16087–L16094 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != STABLE2)     (up-compare-goal gl-build-progress == KrushStable2Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1341 | **PRESERVED** |
| 1342 | L16096–L16106 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE2)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1342 | **PRESERVED** |
| 1343 | L16108–L16115 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item STABLE2)     (building-type-count-total stable >= 2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1343 | **PRESERVED** |
| 1344 | L16118–L16128 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow stable)     (goal gl-current-build-item STABLE2)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1344 | **PRESERVED** |
| 1345 | L16130–L16136 | QSTABLE @ L15764 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1346 | L16138–L16145 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != STABLE2)     (up-compare-goal gl-build-progress == SecondStableNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1346 | **PRESERVED** |
| 1347 | L16147–L16157 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == STABLE2)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1347 | **PRESERVED** |
| 1348 | L16159–L16166 | QSTABLE @ L15764 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item STABLE2)     (building-type-count-total stable >= 2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1348 | **PRESERVED** |
| 1349 | L16170–L16174 | QMONASTERY @ L16168 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1349 | **PRESERVED** |
| 1350 | L16176–L16180 | QMONASTERY @ L16168 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1350 | **PRESERVED** |
| 1351 | L16182–L16193 | QMONASTERY @ L16168 | `(defrule     (goal gl-progression-pause -1)     (can-build-with-escrow monastery)     (up-pending-objects c: monastery < 1)     (goal gl-current-build-item MONASTERY)     (not(u...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-objects, up-pending-placement | — | ShadowByzantine/ShadowByzantine.per#1351 | **PRESERVED** |
| 1352 | L16195–L16201 | QMONASTERY @ L16168 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1353 | L16203–L16210 | QMONASTERY @ L16168 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != MONASTERY)     (up-compare-goal gl-build-progress == MonasteryNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1353 | **PRESERVED** |
| 1354 | L16212–L16221 | QMONASTERY @ L16168 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == MONASTERY)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1354 | **PRESERVED** |
| 1355 | L16223–L16229 | QMONASTERY @ L16168 | `(defrule     (goal gl-current-build-item MONASTERY)     (building-type-count-total monastery >= 1)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1355 | **PRESERVED** |
| 1356 | L16233–L16237 | QMARKET @ L16231 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1356 | **PRESERVED** |
| 1357 | L16239–L16243 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1357 | **PRESERVED** |
| 1358 | L16245–L16249 | QMARKET @ L16231 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1358; ShadowByzantine/ShadowByzantine.per#1366 | **PRESERVED** |
| 1359 | L16252–L16263 | QMARKET @ L16231 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy FLUSH)     (can-build-with-escrow market)     (goal gl-current-build-item MARKET1)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1359 | **PRESERVED** |
| 1360 | L16265–L16272 | QMARKET @ L16231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1361 | L16274–L16281 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != MARKET1)     (up-compare-goal gl-build-progress == MarketNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1361 | **PRESERVED** |
| 1362 | L16283–L16293 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == MARKET1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1362 | **PRESERVED** |
| 1363 | L16295–L16302 | QMARKET @ L16231 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item MARKET1)     (building-type-count-total market >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1363 | **PRESERVED** |
| 1364 | L16305–L16309 | QMARKET @ L16231 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1307; ShadowByzantine/ShadowByzantine.per#1322; ShadowByzantine/ShadowByzantine.per#1336 | **PRESERVED** |
| 1365 | L16311–L16315 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1308; ShadowByzantine/ShadowByzantine.per#1323; ShadowByzantine/ShadowByzantine.per#1365 | **PRESERVED** |
| 1366 | L16317–L16321 | QMARKET @ L16231 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1358; ShadowByzantine/ShadowByzantine.per#1366 | **PRESERVED** |
| 1367 | L16324–L16334 | QMARKET @ L16231 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy KRUSH)     (can-build-with-escrow market)     (goal gl-current-build-item MARKET1)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1367 | **PRESERVED** |
| 1368 | L16336–L16343 | QMARKET @ L16231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1369 | L16345–L16352 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != MARKET1)     (up-compare-goal gl-build-progress == KrushMarketNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1369 | **PRESERVED** |
| 1370 | L16354–L16364 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == MARKET1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1370 | **PRESERVED** |
| 1371 | L16366–L16373 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item MARKET1)     (building-type-count-total market >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1371 | **PRESERVED** |
| 1372 | L16376–L16383 | QMARKET @ L16231 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 1373 | L16385–L16398 | QMARKET @ L16231 | `(defrule     (or	(wood-amount < 60)     (or	(food-amount < 60)     (gold-amount < 60)))     (building-type-count-total market < 1)     (up-compare-goal gl-progression-pause == -...` | split | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1373 | **PRESERVED** |
| 1374 | L16400–L16406 | QMARKET @ L16231 | `(defrule     (goal SPLIT 1)` | gl-progression-pause, split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1374 | **PRESERVED** |
| 1375 | L16408–L16422 | QMARKET @ L16231 | `(defrule     (current-age-time > 60)     (goal gl-strategy FLUSH)     (current-age == feudal-age)     (goal gl-progression-pause -1)     (or	(wood-amount >= 450)     (and(food-a...` | gl-progression-pause | — | — | — | building-type-count-total, research, up-pending-placement | — | ShadowByzantine/ShadowByzantine.per#1375 | **PRESERVED** |
| 1376 | L16424–L16438 | QMARKET @ L16231 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1377 | L16440–L16444 | QMARKET @ L16231 | `(defrule     (goal gl-progression-pause MARKET)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1377 | **PRESERVED** |
| 1378 | L16446–L16450 | QMARKET @ L16231 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1378 | **PRESERVED** |
| 1379 | L16452–L16456 | QMARKET @ L16231 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1308; ShadowByzantine/ShadowByzantine.per#1323; ShadowByzantine/ShadowByzantine.per#1365 | **PRESERVED** |
| 1380 | L16458–L16462 | QMARKET @ L16231 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1380; ShadowByzantine/ShadowByzantine.per#1746; ShadowByzantine/ShadowByzantine.per#1763 | **PRESERVED** |
| 1381 | L16464–L16476 | QMARKET @ L16231 | `(defrule     (can-build-with-escrow market)     (goal gl-progression-pause MARKET)     (building-type-count-total market < 1)` | gl-progression-pause, sn-placement-zone-size | t-misc | can-build-with-escrow | — | building-type-count-total, up-build | — | ShadowByzantine/ShadowByzantine.per#1381 | **PRESERVED** |
| 1382 | L16479–L16484 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (or (up-compare-goal gl-tenth-turn != 1)     (current-age < feudal-age))` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#1382 | **PRESERVED** |
| 1383 | L16487–L16493 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (true)` | gl-archery-in-town, gl-cavalry-in-town, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1383 | **PRESERVED** |
| 1384 | L16496–L16505 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (stance-toward focus-player enemy)` | gl-archery-in-town | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1384 | **PRESERVED** |
| 1385 | L16507–L16517 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (stance-toward focus-player enemy)` | gl-cavalry-in-town | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1385 | **PRESERVED** |
| 1386 | L16520–L16525 | QANALYZING ENEMY ATTACK @ L16478 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -3 | ShadowByzantine/ShadowByzantine.per#649; ShadowByzantine/ShadowByzantine.per#833; ShadowByzantine/ShadowByzantine.per#1386 | **PRESERVED** |
| 1387 | L16529–L16533 | QRESIGNING @ L16527 | `(defrule     (not(player-valid 3))` | — | — | — | — | — | 2 | ShadowByzantine/ShadowByzantine.per#1387 | **PRESERVED** |
| 1388 | L16535–L16547 | QRESIGNING @ L16527 | `(defrule     (civilian-population < 5)     (up-compare-goal CIVSUP < -30)     (up-compare-goal SUPERIORITY < 10)     (up-allied-goal every-ally CIVSUP < -30)     (building-type-...` | — | 5 | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1388 | **PRESERVED** |
| 1389 | L16549–L16555 | QRESIGNING @ L16527 | `(defrule     (timer-triggered 5)` | — | 5 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1389; ShadowByzantine/ShadowByzantine.per#1395 | **PRESERVED** |
| 1390 | L16558–L16562 | QRESIGNING @ L16527 | `(defrule     (player-valid 3)` | — | — | — | — | — | 6 | ShadowByzantine/ShadowByzantine.per#1390 | **PRESERVED** |
| 1391 | L16564–L16570 | QRESIGNING @ L16527 | `(defrule     (true)` | goal1 | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1391 | **PRESERVED** |
| 1392 | L16572–L16580 | QRESIGNING @ L16527 | `(defrule     (up-compare-goal goal1 >= 20)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1392 | **PRESERVED** |
| 1393 | L16582–L16591 | QRESIGNING @ L16527 | `(defrule     (military-population < 10)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1393 | **PRESERVED** |
| 1394 | L16593–L16603 | QRESIGNING @ L16527 | `(defrule     (military-population < 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1394 | **PRESERVED** |
| 1395 | L16605–L16611 | QRESIGNING @ L16527 | `(defrule     (timer-triggered 5)` | — | 5 | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1389; ShadowByzantine/ShadowByzantine.per#1395 | **PRESERVED** |
| 1396 | L16614–L16622 | QSUPERIORITY @ L16613 | `(defrule     (players-building-count target-player > 0)` | superiority | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1396 | **PRESERVED** |
| 1397 | L16625–L16633 | QCIVSUP @ L16624 | `(defrule     (players-building-count target-player > 0)` | civsup | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1397 | **PRESERVED** |
| 1398 | L16638–L16651 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1399 | L16653–L16667 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1400 | L16670–L16683 | QTSA @ L16636 | `(defrule     (goal gl-attacking NO)     (goal gl-strategy FLUSH)     (players-building-count target-player >= 1)     (or	(up-group-size c: RangedGroup >= 6)     (and(up-group-si...` | sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1400 | **PRESERVED** |
| 1401 | L16686–L16696 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1402 | L16698–L16708 | QTSA @ L16636 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1403 | L16711–L16725 | QTSA @ L16636 | `(defrule     (false)     (goal gl-ninety-turn 1)     (up-group-size c: RangedGroup < 1)     (up-group-size c: KnightGroup < 1)` | — | — | — | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | up-target-point | — | ShadowByzantine/ShadowByzantine.per#1403 | **PRESERVED** |
| 1404 | L16729–L16734 | QENEMY STRAT @ L16728 | `(defrule     (players-unit-type-count target-player scout-cavalry-line >= 2)` | enemy-stable | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1404 | **PRESERVED** |
| 1405 | L16737–L16752 | QENEMY STRAT @ L16728 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1406 | L16754–L16764 | QENEMY STRAT @ L16728 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1407 | L16767–L16774 | QENEMY STRAT @ L16728 | `(defrule     (up-compare-goal gl-target-age >= CA-loading)     (players-civilian-population target-player < 33)` | gl-enemy-strategy-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1407 | **PRESERVED** |
| 1408 | L16777–L16784 | QENEMY STRAT @ L16728 | `(defrule     (players-current-age target-player == dark-age)     (players-military-population target-player >= 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1408 | **PRESERVED** |
| 1409 | L16786–L16794 | QENEMY STRAT @ L16728 | `(defrule     (current-age > dark-age)     (current-age-time >= 210)     (goal gl-enemy-strategy DRUSH)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1409 | **PRESERVED** |
| 1410 | L16799–L16804 | QCHAT @ L16797 | `(defrule     (players-military-population any-human-ally >= 30)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1410 | **PRESERVED** |
| 1411 | L16807–L16812 | QCHAT @ L16797 | `(defrule     (players-building-type-count any-human-ally monastery >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1411 | **PRESERVED** |
| 1412 | L16815–L16821 | QCHAT @ L16797 | `(defrule     (research-completed ri-cartography)` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1412 | **PRESERVED** |
| 1413 | L16824–L16831 | QCHAT @ L16797 | `(defrule     (current-age < imperial-age)     (players-current-age any-enemy == imperial-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1413 | **PRESERVED** |
| 1414 | L16834–L16841 | QCHAT @ L16797 | `(defrule     (current-age == dark-age)     (players-military-population any-human-enemy >= 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1414 | **PRESERVED** |
| 1415 | L16844–L16849 | QCHAT @ L16797 | `(defrule     (game-time > 2500)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1415 | **PRESERVED** |
| 1416 | L16853–L16862 | QSTRATEGY @ L16851 | `(defrule     (true)` | gl-enemy-strategy, gl-enemy-strategy-type, gl-strategy, gl-strategy-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1416 | **PRESERVED** |
| 1417 | L16866–L16877 | QSTRATEGY @ L16851 | `(defrule     (player-valid 3)     (game-time >= 5)     (not(player-in-game any-ally))     (up-compare-goal gl-strategy != KRUSH)` | sn-home-exploration-time | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1417 | **PRESERVED** |
| 1418 | L16880–L16887 | QSTRATEGY @ L16851 | `(defrule     (game-time > 10)     (current-age == dark-age)     (up-compare-goal gl-strategy != KRUSH)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1418 | **PRESERVED** |
| 1419 | L16889–L16905 | QSTRATEGY @ L16851 | `(defrule     (game-time > 5)     (game-time < 60)     (current-age == dark-age)     (up-compare-goal gl-strategy != KRUSH)     (or	(taunt-detected me 131)     (or	(taunt-detecte...` | gl-strategy, gl-strategy-type, sn-home-exploration-time | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1419 | **PRESERVED** |
| 1420 | L16910–L16919 | QSTRATEGY @ L16851 | `(defrule     (game-time > 3)     (game-time < 30)` | gl-position, gl-strategy, gl-strategy-type, sn-home-exploration-time | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1420 | **PRESERVED** |
| 1421 | L16923–L16939 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 105)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1421 | **PRESERVED** |
| 1422 | L16941–L16961 | QECO NUMBERS @ L16922 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1423 | L16964–L16969 | QECO NUMBERS @ L16922 | `(defrule     (true)` | sn-mining-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1423 | **PRESERVED** |
| 1424 | L16971–L16976 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 2)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1424 | **PRESERVED** |
| 1425 | L16978–L16983 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 3)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1425 | **PRESERVED** |
| 1426 | L16985–L16990 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 5)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1426 | **PRESERVED** |
| 1427 | L16992–L16997 | QECO NUMBERS @ L16922 | `(defrule     (building-type-count-total mining-camp >= 8)` | sn-mining-camp-max-distance | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1427 | **PRESERVED** |
| 1428 | L17000–L17008 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-town-safe NO)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1428 | **PRESERVED** |
| 1429 | L17010–L17020 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 5)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1429 | **PRESERVED** |
| 1430 | L17026–L17035 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-dark-build -1)     (or (current-age >= feudal-age)     (and(game-time > 80)     (up-compare-goal gl-current-sheep-count >= 6)))` | gl-dark-build | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1430 | **PRESERVED** |
| 1431 | L17037–L17046 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 50)     (wood-amount >= 200)     (goal gl-dark-build MillFirst)     (building-type-count-total mill < 1)` | gl-dark-build | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1431 | **PRESERVED** |
| 1432 | L17048–L17054 | QECO NUMBERS @ L16922 | `(defrule     (true)` | — | — | — | up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#1432 | **PRESERVED** |
| 1433 | L17056–L17066 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 37)     (goal gl-dark-build -1)     (not(up-find-remote c: sheep c: 1))     (up-compare-goal gl-current-sheep-count < 1)` | gl-dark-build | — | — | up-find-remote | — | — | ShadowByzantine/ShadowByzantine.per#1433 | **PRESERVED** |
| 1434 | L17068–L17079 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-dark-build -1)     (not(up-find-remote c: sheep c: 1))     (or	(and(game-time > 80)     (unit-type-count sheep < 1))     (and(game-time > 120)     (up-comp...` | gl-dark-build | — | — | up-find-remote | — | — | ShadowByzantine/ShadowByzantine.per#1434 | **PRESERVED** |
| 1435 | L17082–L17088 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 93)     (goal gl-second-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1435 | **PRESERVED** |
| 1436 | L17090–L17095 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 94)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1436 | **PRESERVED** |
| 1437 | L17098–L17102 | QECO NUMBERS @ L16922 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 1438 | L17104–L17116 | QECO NUMBERS @ L16922 | `(defrule     (true)` | gl-build-progress, sn-initial-exploration-required, sn-percent-exploration-required, sn-safe-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1438 | **PRESERVED** |
| 1439 | L17119–L17127 | QECO NUMBERS @ L16922 | `(defrule     (true)` | gl-vills-under-tc, goal | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1439 | **PRESERVED** |
| 1440 | L17129–L17134 | QECO NUMBERS @ L16922 | `(defrule     (taunt-detected me 87)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1440 | **PRESERVED** |
| 1441 | L17138–L17143 | QECO NUMBERS @ L16922 | `(defrule     (current-age == castle-age)` | sn-preferred-mill-placement | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1441 | **PRESERVED** |
| 1442 | L17146–L17152 | QECO NUMBERS @ L16922 | `(defrule     (true)` | sn-cap-civilian-explorers, sn-percent-civilian-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1442 | **PRESERVED** |
| 1443 | L17154–L17159 | QECO NUMBERS @ L16922 | `(defrule     (unit-type-count villager > 6)` | gl-early-gar | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1443 | **PRESERVED** |
| 1444 | L17161–L17178 | QECO NUMBERS @ L16922 | `(defrule     (game-time < 50)` | goal | — | — | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1444 | **PRESERVED** |
| 1445 | L17180–L17189 | QECO NUMBERS @ L16922 | `(defrule     (game-time > 7)     (game-time < 50)     (goal gl-early-gar -1)     (current-age == dark-age)     (or (game-time > 30)     (up-compare-goal goal > 0))` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1445 | **PRESERVED** |
| 1446 | L17191–L17205 | QECO NUMBERS @ L16922 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#405; ShadowByzantine/ShadowByzantine.per#408; ShadowByzantine/ShadowByzantine.per#493 | **PRESERVED** |
| 1447 | L17207–L17222 | QECO NUMBERS @ L16922 | `(defrule     (goal gl-early-gar 0)     (current-age == dark-age)     (timer-triggered t-relure)` | — | t-relure | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1447 | **PRESERVED** |
| 1448 | L17224–L17239 | QECO NUMBERS @ L16922 | `(defrule     (true)` | gl-age-loading, gl-getting-sheep, gl-need-vills, sn-cap-civilian-builders, sn-enable-training-queue, sn-livestock-to-town-center, sn-maximum-gaia-attack-response, sn-percent-civilian-builders, sn-percent-civilian-gatherers, sn-preferred-mill-placement, sn-zero-priority-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1448 | **PRESERVED** |
| 1449 | L17241–L17247 | QECO NUMBERS @ L16922 | `(defrule     (unit-type-count villager >= 37)` | sn-enable-training-queue | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1449 | **PRESERVED** |
| 1450 | L17249–L17255 | QUEUE @ L17245 | `(defrule     (current-age >= feudal-age)     (goal gl-strategy FLUSH)` | sn-enable-training-queue | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1450 | **PRESERVED** |
| 1451 | L17257–L17262 | QUEUE @ L17245 | `(defrule     (building-type-count mill > 0)` | sn-preferred-mill-placement | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1451 | **PRESERVED** |
| 1452 | L17265–L17269 | QUEUE @ L17245 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1452 | **PRESERVED** |
| 1453 | L17272–L17280 | QUEUE @ L17245 | `(defrule     (or (taunt-detected me 14)     (taunt-detected any-enemy 14))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1453 | **PRESERVED** |
| 1454 | L17283–L17298 | QUEUE @ L17245 | `(defrule     (true)` | gl-boar-unit, sn-allow-adjacent-dropsites, sn-disable-builder-assistance, sn-dropsite-separation-distance, sn-enable-new-building-system, sn-forage-defend-priority, sn-gold-defend-priority, sn-intelligent-gathering, sn-livestock-defend-priority, sn-stone-defend-priority, sn-use-by-type-max-gathering | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1454 | **PRESERVED** |
| 1455 | L17300–L17305 | QUEUE @ L17245 | `(defrule     (cc-players-unit-type-count 0 javelina > 0)` | gl-boar-unit | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1455 | **PRESERVED** |
| 1456 | L17308–L17323 | QUEUE @ L17245 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#841; ShadowByzantine/ShadowByzantine.per#1456; ShadowByzantine/ShadowByzantine.per#1744 | **PRESERVED** |
| 1457 | L17325–L17331 | QUEUE @ L17245 | `(defrule     (game-time > 30)` | sn-food-dropsite-distance, sn-maximum-food-drop-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1457 | **PRESERVED** |
| 1458 | L17333–L17339 | QUEUE @ L17245 | `(defrule     (building-type-count farm > 7)` | sn-food-dropsite-distance, sn-maximum-food-drop-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1458 | **PRESERVED** |
| 1459 | L17342–L17348 | QUEUE @ L17245 | `(defrule     (game-time > 4000)` | sn-maximum-hunt-drop-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1459 | **PRESERVED** |
| 1460 | L17350–L17364 | QUEUE @ L17245 | `(defrule     (true)` | sn-cap-civilian-builders, sn-gold-dropsite-distance, sn-maximum-gold-drop-distance, sn-maximum-stone-drop-distance, sn-maximum-wood-drop-distance, sn-minimum-boar-hunt-group-size, sn-required-forest-tiles, sn-retask-gather-amount, sn-stone-dropsite-distance, sn-wood-dropsite-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1460 | **PRESERVED** |
| 1461 | L17366–L17372 | QUEUE @ L17245 | `(defrule     (game-time > 500)` | sn-maximum-wood-drop-distance, sn-wood-dropsite-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1461 | **PRESERVED** |
| 1462 | L17374–L17381 | QUEUE @ L17245 | `(defrule     (current-age == feudal-age)     (strategic-number sn-stone-gatherer-percentage != 0)` | sn-dropsite-separation-distance, sn-maximum-stone-drop-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1462 | **PRESERVED** |
| 1463 | L17383–L17391 | QUEUE @ L17245 | `(defrule     (current-age-time > 200)     (current-age == feudal-age)     (strategic-number sn-stone-gatherer-percentage == 0)     (strategic-number sn-maximum-stone-drop-distan...` | sn-maximum-stone-drop-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1463 | **PRESERVED** |
| 1464 | L17394–L17399 | QBECO @ L17393 | `(defrule     (goal gl-strategy KRUSH)     (current-age < castle-age)` | — | — | — | — | — | 15 | ShadowByzantine/ShadowByzantine.per#1464 | **PRESERVED** |
| 1465 | L17401–L17408 | QBECO @ L17393 | `(defrule     (or	(current-age-time < 120)     (and(up-compare-goal gl-town-safe != YES)     (and(up-compare-goal gl-threat-time < 10000)     (up-compare-goal gl-threat-target ==...` | — | — | — | — | — | 14 | ShadowByzantine/ShadowByzantine.per#1465 | **PRESERVED** |
| 1466 | L17410–L17415 | QBECO @ L17393 | `(defrule     (or	(current-age < feudal-age)     (up-timer-status BECO-TIMER == timer-running))` | — | beco-timer | — | — | — | 13 | ShadowByzantine/ShadowByzantine.per#1466 | **PRESERVED** |
| 1467 | L17417–L17421 | QBECO @ L17393 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 1468 | L17424–L17433 | QBECO @ L17393 | `(defrule     (false)     (goal gl-fifty-turn 1)     (or	(up-compare-goal NET-WOOD-AMOUNT > 200)     (or	(up-compare-goal NET-FOOD-AMOUNT > 200)     (or	(up-compare-goal NET-GOLD...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1468 | **PRESERVED** |
| 1469 | L17436–L17448 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal gl-strategy != KRUSH)     (up-compare-goal NET-WOOD-AMOUNT < 100)     (up-compare-goal NET-FOOD-AMOUNT >= 250)` | sn-food-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1469 | **PRESERVED** |
| 1470 | L17450–L17462 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal gl-strategy != KRUSH)     (up-compare-goal NET-WOOD-AMOUNT < 150)     (up-compare-goal NET-FOOD-AMOUNT >= 400)` | sn-food-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1470 | **PRESERVED** |
| 1471 | L17464–L17476 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal gl-strategy != KRUSH)     (up-compare-goal NET-WOOD-AMOUNT < 300)     (up-compare-goal NET-FOOD-AMOUNT >= 800)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1471 | **PRESERVED** |
| 1472 | L17479–L17493 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (gold-amount > 200)     (food-amount < 600)     (or	(research-available castle-age)     (goal gl-current-build-item CUP))     (up-compare-sn sn-g...` | — | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#1472 | **PRESERVED** |
| 1473 | L17495–L17508 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal NET-FOOD-AMOUNT < 100)     (up-compare-goal NET-GOLD-AMOUNT >= 300)     (up-compare-sn sn-gold-gatherer-percentage >= 2)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1473 | **PRESERVED** |
| 1474 | L17510–L17522 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (up-compare-goal NET-FOOD-AMOUNT < 100)     (up-compare-goal NET-WOOD-AMOUNT >= 300)     (up-compare-sn sn-wood-gatherer-percentage >= 4)` | sn-food-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1474 | **PRESERVED** |
| 1475 | L17525–L17539 | QBECO @ L17393 | `(defrule     (false)     (goal SPLIT 0)     (goal gl-current-build-item CUP)     (unit-type-count villager-gold < 1)     (up-compare-sn sn-gold-gatherer-percentage < 2)` | sn-food-gatherer-percentage, sn-gold-gatherer-percentage, sn-wood-gatherer-percentage, split | beco-timer | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1475 | **PRESERVED** |
| 1476 | L17541–L17551 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (or	(and(gold-amount < 100)     (food-amount >= 500))     (and(gold-amount < 160)     (food-amount >= 700)))     (research-available castle-age) ...` | split | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#1476 | **PRESERVED** |
| 1477 | L17553–L17564 | QBECO @ L17393 | `(defrule     (goal SPLIT 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1477 | **PRESERVED** |
| 1478 | L17566–L17581 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (game-time < 2400)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1478; ShadowByzantine/ShadowByzantine.per#1479 | **PRESERVED** |
| 1479 | L17583–L17597 | QBECO @ L17393 | `(defrule     (goal SPLIT 0)     (game-time < 2400)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1478; ShadowByzantine/ShadowByzantine.per#1479 | **PRESERVED** |
| 1480 | L17599–L17607 | QBECO @ L17393 | `(defrule     (true)` | goal, split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1480 | **PRESERVED** |
| 1481 | L17609–L17614 | QBECO @ L17393 | `(defrule     (up-compare-goal goal > 100)` | sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1481 | **PRESERVED** |
| 1482 | L17616–L17621 | QBECO @ L17393 | `(defrule     (up-compare-goal goal < 100)` | sn-wood-gatherer-percentage | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1482 | **PRESERVED** |
| 1483 | L17623–L17633 | QBECO @ L17393 | `(defrule     (or	(taunt-detected me 13)     (taunt-detected any-enemy 13))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1483 | **PRESERVED** |
| 1484 | L17637–L17643 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-town-safe, gl-town-under-attack | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1484 | **PRESERVED** |
| 1485 | L17647–L17653 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-enemies-in-town, goal, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1485 | **PRESERVED** |
| 1486 | L17656–L17666 | QTOWN SAFETY @ L17636 | `(defrule     (stance-toward focus-player enemy)` | gl-enemies-in-town | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1486 | **PRESERVED** |
| 1487 | L17669–L17674 | QTOWN SAFETY @ L17636 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 1488 | L17678–L17682 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#91; ShadowByzantine/ShadowByzantine.per#97; ShadowByzantine/ShadowByzantine.per#103 | **PRESERVED** |
| 1489 | L17685–L17693 | QTOWN SAFETY @ L17636 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1489 | **PRESERVED** |
| 1490 | L17696–L17702 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt < 2)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#1490 | **PRESERVED** |
| 1491 | L17704–L17712 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt >= 2)     (goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe == YES)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1491 | **PRESERVED** |
| 1492 | L17714–L17722 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt < 1)     (goal gl-town-safe BeingDrushed)     (up-compare-goal gl-enemies-in-town < 2)     (up-timer-status t-town-safe != timer-running)` | — | t-town-safe | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1492 | **PRESERVED** |
| 1493 | L17725–L17732 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal gl-town-safe == YES)     (up-compare-goal gl-enemies-in-town >= 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1493 | **PRESERVED** |
| 1494 | L17734–L17739 | QTOWN SAFETY @ L17636 | `(defrule     (goal gl-town-safe NO)     (up-compare-goal gl-enemies-in-town >= 2)` | — | t-town-safe | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1494 | **PRESERVED** |
| 1495 | L17741–L17749 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal gl-town-safe != YES)     (up-compare-goal gl-enemies-in-town < 1)     (up-timer-status t-town-safe != timer-running)` | — | t-town-safe | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1495 | **PRESERVED** |
| 1496 | L17753–L17758 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#294; ShadowByzantine/ShadowByzantine.per#617; ShadowByzantine/ShadowByzantine.per#623 | **PRESERVED** |
| 1497 | L17761–L17769 | QTOWN SAFETY @ L17636 | `(defrule     (stance-toward focus-player enemy)` | — | — | — | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1497 | **PRESERVED** |
| 1498 | L17772–L17778 | QTOWN SAFETY @ L17636 | `(defrule     (up-compare-goal rt < 1)     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#45; ShadowByzantine/ShadowByzantine.per#156; ShadowByzantine/ShadowByzantine.per#296 | **PRESERVED** |
| 1499 | L17780–L17790 | QTOWN SAFETY @ L17636 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1500 | L17792–L17802 | QTOWN SAFETY @ L17636 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1501 | L17805–L17818 | QTOWN SAFETY @ L17636 | `(defrule     (current-age >= dark-age)` | sn-home-exploration-time, sn-maximum-explore-group-size, sn-percentage-explore-exterminators | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1501 | **PRESERVED** |
| 1502 | L17820–L17825 | QTOWN SAFETY @ L17636 | `(defrule     (current-age >= feudal-age)` | sn-home-exploration-time | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1502 | **PRESERVED** |
| 1503 | L17827–L17831 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-enemy-civ | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1503 | **PRESERVED** |
| 1504 | L17833–L17841 | QTOWN SAFETY @ L17636 | `(defrule     (false)     (not (player-valid 3))     (or (players-civ target-player incan)     (or (players-civ target-player aztec)     (players-civ target-player mayan)))` | gl-enemy-civ | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1504 | **PRESERVED** |
| 1505 | L17843–L17849 | QTOWN SAFETY @ L17636 | `(defrule     (or (players-civ every-enemy incan)     (or (players-civ every-enemy aztec)     (players-civ every-enemy mayan)))` | gl-enemy-civ | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1505 | **PRESERVED** |
| 1506 | L17851–L17857 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | gl-escrow-state, sn-enable-patrol-attack | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1506 | **PRESERVED** |
| 1507 | L17859–L17865 | QTOWN SAFETY @ L17636 | `(defrule     (goal gl-attacking YES)` | sn-number-attack-groups, sn-percent-attack-soldiers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1507 | **PRESERVED** |
| 1508 | L17867–L17880 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-allow-civilian-offense, sn-disable-attack-groups, sn-enable-offensive-priority, sn-focus-player-number, sn-ignore-tower-elevation, sn-number-attack-groups, sn-number-civilian-militia, sn-percent-building-cancellation | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1508 | **PRESERVED** |
| 1509 | L17882–L17901 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-do-not-scale-for-difficulty-level, sn-enemy-sighted-response-distance, sn-number-forward-builders, sn-percent-attack-soldiers, sn-percent-enemy-sighted-response | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1509 | **PRESERVED** |
| 1510 | L17903–L17907 | QTOWN SAFETY @ L17636 | `(defrule     (up-group-size c: RangedGroup > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1510 | **PRESERVED** |
| 1511 | L17909–L17913 | QTOWN SAFETY @ L17636 | `(defrule     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1511 | **PRESERVED** |
| 1512 | L17915–L17929 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-relic-return-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1512 | **PRESERVED** |
| 1513 | L17931–L17943 | QTOWN SAFETY @ L17636 | `(defrule     (true)` | sn-special-attack-influence1, sn-special-attack-type1, sn-target-evaluation-boat, sn-target-evaluation-continent, sn-target-evaluation-distance, sn-target-evaluation-in-progress, sn-target-evaluation-kills, sn-target-evaluation-siege-weapon | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1513 | **PRESERVED** |
| 1514 | L17948–L17956 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-fifth-turn 1)     (goal gl-position POCKET)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1514 | **PRESERVED** |
| 1515 | L17959–L17965 | QTARGET PLAYER @ L17945 | `(defrule     (or	(game-time < 5)     (or (game-time > 10)     (not(player-valid 5))))` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#1515 | **PRESERVED** |
| 1516 | L17968–L17974 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | rt, sn-focus-player-number | — | — | up-full-reset-search | — | — | ShadowByzantine/ShadowByzantine.per#1516 | **PRESERVED** |
| 1517 | L17977–L17982 | QTARGET PLAYER @ L17945 | `(defrule     (not(stance-toward focus-player enemy))     (up-allied-goal focus-player gl-position != POCKET)` | — | — | — | up-find-remote | — | — | ShadowByzantine/ShadowByzantine.per#1517 | **PRESERVED** |
| 1518 | L17985–L17990 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid focus-player)` | sn-focus-player-number | — | — | — | — | -2 | ShadowByzantine/ShadowByzantine.per#169; ShadowByzantine/ShadowByzantine.per#175; ShadowByzantine/ShadowByzantine.per#180 | **PRESERVED** |
| 1519 | L17992–L18006 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | sn-focus-player-number | — | — | up-clean-search, up-set-target-object, up-set-target-point | up-get-object-data | — | ShadowByzantine/ShadowByzantine.per#1519 | **PRESERVED** |
| 1520 | L18010–L18017 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 122)` | sn-target-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1520 | **PRESERVED** |
| 1521 | L18020–L18028 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 123)` | sn-target-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1521 | **PRESERVED** |
| 1522 | L18031–L18040 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 124)` | sn-target-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1522 | **PRESERVED** |
| 1523 | L18043–L18053 | QTARGET PLAYER @ L17945 | `(defrule     (taunt-detected me 125)` | sn-target-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1523 | **PRESERVED** |
| 1524 | L18056–L18066 | QTARGET PLAYER @ L17945 | `(defrule     (or	(taunt-detected me 22)     (or	(taunt-detected any-ally 22)     (taunt-detected any-enemy 22)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1524 | **PRESERVED** |
| 1525 | L18071–L18080 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time < 1020)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1525 | **PRESERVED** |
| 1526 | L18088–L18100 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target -1)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(no...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1526 | **PRESERVED** |
| 1527 | L18102–L18108 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1528 | L18111–L18123 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 1)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(not...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1528 | **PRESERVED** |
| 1529 | L18125–L18132 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1530 | L18135–L18147 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 3)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(not...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1530 | **PRESERVED** |
| 1531 | L18149–L18157 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1532 | L18160–L18172 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 5)     (not(player-in-game any-ally))     (game-time >= KrushTimeToRetarget)     (or	(not...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1532 | **PRESERVED** |
| 1533 | L18174–L18183 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1534 | L18186–L18197 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time >= 1200)     (goal gl-strategy KRUSH)     (not(player-in-game any-ally))     (player-in-game target-player)     (up-compare-goal gl-...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1534 | **PRESERVED** |
| 1535 | L18201–L18211 | QTARGET PLAYER @ L17945 | `(defrule     (false)     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target -1)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1535 | **PRESERVED** |
| 1536 | L18213–L18219 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1537 | L18222–L18232 | QTARGET PLAYER @ L17945 | `(defrule     (false)     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 1)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1537 | **PRESERVED** |
| 1538 | L18234–L18241 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1539 | L18244–L18253 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 3)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1539 | **PRESERVED** |
| 1540 | L18255–L18263 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1541 | L18266–L18275 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 5)     (players-civilian-population any-enemy >= 80)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1541 | **PRESERVED** |
| 1542 | L18277–L18286 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1543 | L18289–L18298 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (player-in-game target-player)     (up-compare-goal gl-find-new-target != -1)     (players-civilian-population tar...` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1543 | **PRESERVED** |
| 1544 | L18302–L18314 | QTARGET PLAYER @ L17945 | `(defrule     (false)     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target -1)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target...` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1544 | **PRESERVED** |
| 1545 | L18316–L18322 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1546 | L18325–L18333 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 1)     (players-current-age target-player < castle-age)` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1546 | **PRESERVED** |
| 1547 | L18335–L18346 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 1)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target-player))    ...` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1547 | **PRESERVED** |
| 1548 | L18348–L18355 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1549 | L18358–L18366 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 3)     (players-current-age target-player < castle-age)` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1549 | **PRESERVED** |
| 1550 | L18368–L18379 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 3)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target-player))    ...` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1550 | **PRESERVED** |
| 1551 | L18381–L18389 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1552 | L18392–L18403 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (goal gl-strategy KRUSH)     (goal gl-find-new-target 5)     (game-time >= KrushTimeToRetarget)     (or	(not(player-in-game target-player))    ...` | gl-find-new-target | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1552 | **PRESERVED** |
| 1553 | L18405–L18414 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1554 | L18417–L18427 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time >= 1200)     (goal gl-strategy KRUSH)     (player-in-game target-player)     (up-compare-goal gl-find-new-target != -1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1554 | **PRESERVED** |
| 1555 | L18432–L18436 | QTARGET PLAYER @ L17945 | `(defrule     (up-compare-goal gl-privileged-player == my-player-number)` | — | — | — | — | — | 19 | ShadowByzantine/ShadowByzantine.per#1555 | **PRESERVED** |
| 1556 | L18439–L18447 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1557 | L18449–L18460 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1558 | L18462–L18470 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1558; ShadowByzantine/ShadowByzantine.per#1578 | **PRESERVED** |
| 1559 | L18472–L18478 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1560 | L18481–L18489 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1561 | L18491–L18500 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 1)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1561; ShadowByzantine/ShadowByzantine.per#1581 | **PRESERVED** |
| 1562 | L18502–L18513 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1563 | L18515–L18522 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1563; ShadowByzantine/ShadowByzantine.per#1583 | **PRESERVED** |
| 1564 | L18524–L18531 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1565 | L18534–L18542 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1566 | L18544–L18553 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 3)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1566; ShadowByzantine/ShadowByzantine.per#1586 | **PRESERVED** |
| 1567 | L18555–L18566 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1568 | L18568–L18575 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1568; ShadowByzantine/ShadowByzantine.per#1588 | **PRESERVED** |
| 1569 | L18577–L18585 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1570 | L18588–L18596 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1571 | L18598–L18609 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1572 | L18611–L18618 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1572; ShadowByzantine/ShadowByzantine.per#1592 | **PRESERVED** |
| 1573 | L18620–L18629 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1574 | L18632–L18641 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1575 | L18644–L18648 | QTARGET PLAYER @ L17945 | `(defrule     (up-compare-goal gl-privileged-player != my-player-number)` | — | — | — | — | — | 15 | ShadowByzantine/ShadowByzantine.per#1575 | **PRESERVED** |
| 1576 | L18651–L18659 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1577 | L18661–L18672 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1578 | L18674–L18681 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1558; ShadowByzantine/ShadowByzantine.per#1578 | **PRESERVED** |
| 1579 | L18683–L18689 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1580 | L18692–L18700 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1581 | L18702–L18711 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 1)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1561; ShadowByzantine/ShadowByzantine.per#1581 | **PRESERVED** |
| 1582 | L18713–L18724 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1583 | L18726–L18733 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1563; ShadowByzantine/ShadowByzantine.per#1583 | **PRESERVED** |
| 1584 | L18735–L18742 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1585 | L18745–L18753 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1586 | L18755–L18764 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 5)     (goal gl-find-new-target 3)     (players-current-age target-player < castle-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1566; ShadowByzantine/ShadowByzantine.per#1586 | **PRESERVED** |
| 1587 | L18766–L18777 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1588 | L18779–L18786 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1568; ShadowByzantine/ShadowByzantine.per#1588 | **PRESERVED** |
| 1589 | L18788–L18796 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1590 | L18799–L18807 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1591 | L18809–L18820 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1592 | L18822–L18829 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1572; ShadowByzantine/ShadowByzantine.per#1592 | **PRESERVED** |
| 1593 | L18831–L18840 | QTARGET PLAYER @ L17945 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1594 | L18843–L18852 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 900)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1556; ShadowByzantine/ShadowByzantine.per#1557; ShadowByzantine/ShadowByzantine.per#1560 | **PRESERVED** |
| 1595 | L18855–L18868 | QTARGET PLAYER @ L17945 | `(defrule     (player-valid 3)     (game-time > 1200)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1595 | **PRESERVED** |
| 1596 | L18870–L18880 | QTARGET PLAYER @ L17945 | `(defrule     (goal SPLIT 1)` | sn-focus-player-number, sn-target-player-number, split | t-target-switch | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1596 | **PRESERVED** |
| 1597 | L18882–L18887 | QTARGET PLAYER @ L17945 | `(defrule     (game-time < 30)     (up-compare-goal gl-last-target-player s:!= sn-target-player-number)` | gl-last-target-player | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1597 | **PRESERVED** |
| 1598 | L18889–L18897 | QTARGET PLAYER @ L17945 | `(defrule     (game-time >= 30)     (up-compare-goal gl-last-target-player s:!= sn-target-player-number)` | gl-last-target-player | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1598 | **PRESERVED** |
| 1599 | L18900–L18906 | QTARGET PLAYER @ L17945 | `(defrule     (player-number 1)     (not(player-valid 3))` | sn-target-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1599 | **PRESERVED** |
| 1600 | L18908–L18914 | QTARGET PLAYER @ L17945 | `(defrule     (player-number 2)     (not(player-valid 3))` | sn-target-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1600 | **PRESERVED** |
| 1601 | L18916–L18920 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#503; ShadowByzantine/ShadowByzantine.per#520; ShadowByzantine/ShadowByzantine.per#1601 | **PRESERVED** |
| 1602 | L18923–L18931 | QTARGET PLAYER @ L17945 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1602 | **PRESERVED** |
| 1603 | L18934–L18939 | QPRIORITY @ L18933 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1604 | L18941–L18952 | QPRIORITY @ L18933 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1604 | **PRESERVED** |
| 1605 | L18956–L18968 | QPRIORITY @ L18933 | `(defrule     (goal gl-strategy FLUSH)     (unit-type-count knight >= 3)     (up-compare-goal SUPERIORITY >= 30)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1605 | **PRESERVED** |
| 1606 | L18970–L18982 | QPRIORITY @ L18933 | `(defrule     (goal gl-strategy FLUSH)     (or	(unit-type-count knight < 3)     (up-compare-goal SUPERIORITY < 30))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1606 | **PRESERVED** |
| 1607 | L18985–L18998 | QPRIORITY @ L18933 | `(defrule     (game-time < 1800)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1607 | **PRESERVED** |
| 1608 | L19000–L19013 | QPRIORITY @ L18933 | `(defrule     (goal gl-strategy KRUSH)     (or	(game-time >= 1800)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1608 | **PRESERVED** |
| 1609 | L19015–L19021 | QPRIORITY @ L18933 | `(defrule     (players-building-count target-player > 10)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1609 | **PRESERVED** |
| 1610 | L19023–L19030 | QPRIORITY @ L18933 | `(defrule     (goal gl-attacking YES)     (goal gl-strategy KRUSH)     (taunt-detected any-ally 102)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1610 | **PRESERVED** |
| 1611 | L19033–L19039 | QSCOUTING @ L19032 | `(defrule     (game-time >= 50)` | sn-number-explore-groups, sn-total-number-explorers | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1611 | **PRESERVED** |
| 1612 | L19041–L19049 | QSCOUTING @ L19032 | `(defrule     (game-time >= 1500)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1612 | **PRESERVED** |
| 1613 | L19051–L19058 | QSCOUTING @ L19032 | `(defrule     (false)     (players-building-count target-player >= 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1613 | **PRESERVED** |
| 1614 | L19060–L19069 | QSCOUTING @ L19032 | `(defrule     (game-time < 1100)     (timer-triggered t-scout-enemy)     (players-building-count any-enemy > 0)     (strategic-number sn-total-number-explorers > 0)` | — | t-scout-enemy | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1614 | **PRESERVED** |
| 1615 | L19071–L19081 | QSCOUTING @ L19032 | `(defrule     (false)     (game-time >= 1100)     (timer-triggered t-scout-enemy)     (players-building-count any-enemy > 0)     (strategic-number sn-total-number-explorers > 0)` | — | t-scout-enemy | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1615 | **PRESERVED** |
| 1616 | L19084–L19089 | QATTACK EFFICIENCY @ L19083 | `(defrule     (false)     (up-group-size c: RangedGroup < 1)` | — | — | — | — | — | 20 | ShadowByzantine/ShadowByzantine.per#1616 | **PRESERVED** |
| 1617 | L19091–L19100 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | gl-attack-efficiency, goal, goal1, goal2, goal3, goal4 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1617 | **PRESERVED** |
| 1618 | L19103–L19110 | QATTACK EFFICIENCY @ L19083 | `(defrule     (false)` | gl-attack-efficiency | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1618 | **PRESERVED** |
| 1619 | L19113–L19117 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1619; ShadowByzantine/ShadowByzantine.per#1628 | **PRESERVED** |
| 1620 | L19119–L19123 | QATTACK EFFICIENCY @ L19083 | `(defrule     (players-unit-type-count target-player battering-ram-line >= 2)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1620 | **PRESERVED** |
| 1621 | L19125–L19134 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1622 | L19136–L19140 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1622; ShadowByzantine/ShadowByzantine.per#1632 | **PRESERVED** |
| 1623 | L19142–L19146 | QATTACK EFFICIENCY @ L19083 | `(defrule     (players-unit-type-count target-player battering-ram-line >= 1)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1623 | **PRESERVED** |
| 1624 | L19148–L19157 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1625 | L19159–L19163 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1625; ShadowByzantine/ShadowByzantine.per#1636 | **PRESERVED** |
| 1626 | L19165–L19169 | QATTACK EFFICIENCY @ L19083 | `(defrule     (players-unit-type-count target-player battering-ram-line >= 2)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1626 | **PRESERVED** |
| 1627 | L19171–L19180 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1628 | L19182–L19186 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1619; ShadowByzantine/ShadowByzantine.per#1628 | **PRESERVED** |
| 1629 | L19188–L19192 | QATTACK EFFICIENCY @ L19083 | `(defrule     (unit-type-count battering-ram-line >= 2)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1629 | **PRESERVED** |
| 1630 | L19195–L19199 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#503; ShadowByzantine/ShadowByzantine.per#520; ShadowByzantine/ShadowByzantine.per#1601 | **PRESERVED** |
| 1631 | L19202–L19211 | QATTACK EFFICIENCY @ L19083 | `(defrule     (stance-toward focus-player enemy)` | gl-attack-efficiency, goal2 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1631 | **PRESERVED** |
| 1632 | L19213–L19217 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1622; ShadowByzantine/ShadowByzantine.per#1632 | **PRESERVED** |
| 1633 | L19219–L19223 | QATTACK EFFICIENCY @ L19083 | `(defrule     (unit-type-count battering-ram-line >= 1)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1633 | **PRESERVED** |
| 1634 | L19226–L19230 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#503; ShadowByzantine/ShadowByzantine.per#520; ShadowByzantine/ShadowByzantine.per#1601 | **PRESERVED** |
| 1635 | L19233–L19242 | QATTACK EFFICIENCY @ L19083 | `(defrule     (stance-toward focus-player enemy)` | gl-attack-efficiency, goal3 | — | — | up-find-remote, up-full-reset-search, up-get-search-state | up-get-search-state | — | ShadowByzantine/ShadowByzantine.per#1635 | **PRESERVED** |
| 1636 | L19244–L19248 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1625; ShadowByzantine/ShadowByzantine.per#1636 | **PRESERVED** |
| 1637 | L19250–L19254 | QATTACK EFFICIENCY @ L19083 | `(defrule     (unit-type-count battering-ram-line >= 2)` | goal8 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1637 | **PRESERVED** |
| 1638 | L19257–L19261 | QATTACK EFFICIENCY @ L19083 | `(defrule     (true)` | sn-focus-player-number | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#503; ShadowByzantine/ShadowByzantine.per#520; ShadowByzantine/ShadowByzantine.per#1601 | **PRESERVED** |
| 1639 | L19264–L19273 | QATTACK EFFICIENCY @ L19083 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1640 | L19276–L19290 | QATTACK EFFICIENCY @ L19083 | `(defrule     (taunt-detected me 91)     (goal gl-fifth-turn 1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1640 | **PRESERVED** |
| 1641 | L19292–L19297 | QATTACK EFFICIENCY @ L19083 | `(defrule     (taunt-detected me 92)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1641 | **PRESERVED** |
| 1642 | L19300–L19315 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (true)` | gl-army-damage-potential | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1642 | **PRESERVED** |
| 1643 | L19318–L19326 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1643 | **PRESERVED** |
| 1644 | L19328–L19337 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (true)` | gl-army-damage-potential, goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1644 | **PRESERVED** |
| 1645 | L19340–L19349 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (false)     (players-current-age target-player < castle-age)     (or	(and(goal gl-enemy-strategy-type FC)     (military-population > 6))     (and(military-populatio...` | gl-army-damage-potential | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1645 | **PRESERVED** |
| 1646 | L19352–L19361 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (current-age == castle-age)     (up-compare-goal UP-FIRST != -1)     (or (current-age-time >= 30)     (players-current-age target-player == castle-age))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1646 | **PRESERVED** |
| 1647 | L19363–L19372 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (up-compare-goal UP-FIRST != -1)     (or (players-current-age-time target-player >= 30)     (current-age == castle-age))     (players-current-age target-player == c...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1647 | **PRESERVED** |
| 1648 | L19374–L19381 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (up-compare-goal gl-target-age < CA-loading)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1648 | **PRESERVED** |
| 1649 | L19383–L19387 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (goal UP-FIRST 1)` | gl-army-damage-potential | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1649 | **PRESERVED** |
| 1650 | L19389–L19397 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (goal UP-FIRST -1)     (up-compare-goal gl-target-age == CA-loading)     (up-research-status c: castle-age < research-pending)` | up-first | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1650 | **PRESERVED** |
| 1651 | L19399–L19403 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (goal UP-FIRST 0)` | gl-army-damage-potential | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1651 | **PRESERVED** |
| 1652 | L19405–L19410 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (current-age-time >= 30)     (current-age >= castle-age)` | gl-army-damage-potential | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1652 | **PRESERVED** |
| 1653 | L19412–L19417 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (players-current-age-time target-player >= 30)     (players-current-age target-player >= castle-age)` | gl-army-damage-potential | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1653 | **PRESERVED** |
| 1654 | L19420–L19424 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (research-completed ri-elite-skirmisher)` | gl-army-damage-potential | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1654 | **PRESERVED** |
| 1655 | L19426–L19430 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (research-completed ri-leather-archer-armor)` | gl-army-damage-potential | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1655 | **PRESERVED** |
| 1656 | L19432–L19436 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (research-completed ri-chain-barding)` | gl-army-damage-potential | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1656 | **PRESERVED** |
| 1657 | L19438–L19443 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (unit-type-count battering-ram-line >= 2)     (up-compare-goal gl-army-damage-potential >= CostOfPausingForRams)` | gl-army-damage-potential | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1657 | **PRESERVED** |
| 1658 | L19446–L19452 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (taunt-detected me 67)     (current-age >= feudal-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1658 | **PRESERVED** |
| 1659 | L19454–L19459 | QDAMAGE POTENTIAL @ L19299 | `(defrule     (taunt-detected me 68)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1659 | **PRESERVED** |
| 1660 | L19464–L19477 | Q2BA @ L19462 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item 2BA)     (can-research-with-escrow ri-double-bit-axe)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1660 | **PRESERVED** |
| 1661 | L19479–L19485 | Q2BA @ L19462 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1662 | L19487–L19495 | Q2BA @ L19462 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != 2BA)     (up-compare-goal gl-build-progress == Krush2BANumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1662 | **PRESERVED** |
| 1663 | L19497–L19504 | Q2BA @ L19462 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item 2BA)     (up-research-status c: ri-double-bit-axe >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1663 | **PRESERVED** |
| 1664 | L19507–L19520 | Q2BA @ L19462 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item 2BA)     (can-research-with-escrow ri-double-bit-axe)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1664 | **PRESERVED** |
| 1665 | L19522–L19528 | Q2BA @ L19462 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1666 | L19530–L19538 | Q2BA @ L19462 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != 2BA)     (up-compare-goal gl-build-progress == DoubleBitAxeNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1666 | **PRESERVED** |
| 1667 | L19540–L19547 | Q2BA @ L19462 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item 2BA)     (up-research-status c: ri-double-bit-axe >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1667 | **PRESERVED** |
| 1668 | L19551–L19560 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item BOWSAW)     (can-research-with-escrow ri-bow-saw)     (unit-type-count-t...` | — | — | can-research-with-escrow | — | unit-type-count-total, up-research | — | ShadowByzantine/ShadowByzantine.per#1668 | **PRESERVED** |
| 1669 | L19562–L19568 | QBOWSAW @ L19549 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1670 | L19570–L19577 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != BOWSAW)     (up-compare-goal gl-build-progress == KrushBowsawNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1670 | **PRESERVED** |
| 1671 | L19579–L19590 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (unit-type-count-total villager >= 42)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == B...` | — | — | set-escrow-percentage | — | unit-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1671 | **PRESERVED** |
| 1672 | L19592–L19599 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item BOWSAW)     (up-research-status c: ri-bow-saw >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1672 | **PRESERVED** |
| 1673 | L19602–L19610 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item BOWSAW)     (can-research-with-escrow ri-bow-saw)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1673 | **PRESERVED** |
| 1674 | L19612–L19618 | QBOWSAW @ L19549 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1675 | L19620–L19627 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != BOWSAW)     (up-compare-goal gl-build-progress == BowsawNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1675 | **PRESERVED** |
| 1676 | L19629–L19638 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == BOWSAW)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1676 | **PRESERVED** |
| 1677 | L19640–L19647 | QBOWSAW @ L19549 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item BOWSAW)     (up-research-status c: ri-bow-saw >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1677 | **PRESERVED** |
| 1678 | L19651–L19663 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDMINING)     (can-research-with-escrow ri-gold-mining)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1678 | **PRESERVED** |
| 1679 | L19665–L19671 | QGOLDMINING @ L19649 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1680 | L19673–L19682 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != GOLDMINING)     (up-compare-goal gl-build-progress == KrushGoldMiningNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1680 | **PRESERVED** |
| 1681 | L19684–L19691 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item GOLDMINING)     (up-research-status c: ri-gold-mining >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1681 | **PRESERVED** |
| 1682 | L19694–L19706 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDMINING)     (can-research-with-escrow ri-gold-mining)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1682 | **PRESERVED** |
| 1683 | L19708–L19714 | QGOLDMINING @ L19649 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1684 | L19716–L19725 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDMINING)     (up-compare-goal gl-build-progress == GoldMiningNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1684 | **PRESERVED** |
| 1685 | L19727–L19734 | QGOLDMINING @ L19649 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item GOLDMINING)     (up-research-status c: ri-gold-mining >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1685 | **PRESERVED** |
| 1686 | L19737–L19744 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDSHAFT)     (can-research-with-escrow ri-gold-shaft-mining)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1686 | **PRESERVED** |
| 1687 | L19746–L19752 | QGOLDSHAFT @ L19736 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1688 | L19754–L19763 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDSHAFT)     (up-compare-goal gl-build-progress == GoldshaftNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1688 | **PRESERVED** |
| 1689 | L19765–L19773 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item GOLDSHAFT)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1689 | **PRESERVED** |
| 1690 | L19775–L19781 | QGOLDSHAFT @ L19736 | `(defrule     (goal gl-current-build-item GOLDSHAFT)     (up-research-status c: ri-gold-shaft-mining >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1690 | **PRESERVED** |
| 1691 | L19786–L19797 | QHCOL @ L19784 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item HCOL)     (can-research-with-escrow ri-horse-collar)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1691 | **PRESERVED** |
| 1692 | L19799–L19805 | QHCOL @ L19784 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1693 | L19807–L19816 | QHCOL @ L19784 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != HCOL)     (up-compare-goal gl-build-progress == KrushHorseCollarNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1693 | **PRESERVED** |
| 1694 | L19818–L19826 | QHCOL @ L19784 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item HCOL)     (up-research-status c: ri-horse-collar >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1694 | **PRESERVED** |
| 1695 | L19829–L19841 | QHCOL @ L19784 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item HCOL)     (can-research-with-escrow ri-horse-collar)` | — | — | can-research-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1695 | **PRESERVED** |
| 1696 | L19843–L19849 | QHCOL @ L19784 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1697 | L19851–L19860 | QHCOL @ L19784 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != HCOL)     (up-compare-goal gl-build-progress == HorseCollarNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1697 | **PRESERVED** |
| 1698 | L19862–L19869 | QHCOL @ L19784 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item HCOL)     (up-research-status c: ri-horse-collar >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1698 | **PRESERVED** |
| 1699 | L19872–L19879 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item HEAVYPLOW)     (can-research-with-escrow ri-heavy-plow)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1699 | **PRESERVED** |
| 1700 | L19881–L19887 | QHEAVY PLOW @ L19871 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1701 | L19889–L19898 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != HEAVYPLOW)     (up-compare-goal gl-build-progress == HeavyPlowNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1701 | **PRESERVED** |
| 1702 | L19900–L19908 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == HEAVYPLOW)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1702 | **PRESERVED** |
| 1703 | L19910–L19916 | QHEAVY PLOW @ L19871 | `(defrule     (goal gl-current-build-item HEAVYPLOW)     (up-research-status c: ri-heavy-plow >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1703 | **PRESERVED** |
| 1704 | L19919–L19924 | QVILLAGERS @ L19918 | `(defrule     (not(goal gl-need-vills YES))     (up-timer-status t-vill-training != timer-disabled)` | — | t-vill-training | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1704 | **PRESERVED** |
| 1705 | L19927–L19936 | QVILLAGERS @ L19918 | `(defrule     (or (and(food-amount > 550)     (gold-amount > 155))     (and(gold-amount > 90)     (food-amount > 750)))     (research-available castle-age)` | — | — | — | — | research | — | ShadowByzantine/ShadowByzantine.per#1705 | **PRESERVED** |
| 1706 | L19938–L19945 | QVILLAGERS @ L19918 | `(defrule     (goal gl-current-build-item PAA)     (research-completed ri-fletching)     (players-unit-type-count target-player skirmisher < 5)` | — | — | — | — | research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1706 | **PRESERVED** |
| 1707 | L19947–L19953 | QVILLAGERS @ L19918 | `(defrule     (false)     (goal gl-current-build-item FLTCH)     (building-type-count blacksmith > 0)` | — | — | — | — | — | 1 | ShadowByzantine/ShadowByzantine.per#1707 | **PRESERVED** |
| 1708 | L19955–L19966 | QVILLAGERS @ L19918 | `(defrule     (goal gl-strategy FLUSH)     (up-can-train gl-escrow-state c: villager)     (or	(goal gl-need-vills YES)     (and(unit-type-count-total villager < 25)     (and(food...` | — | t-vill-training | — | — | unit-type-count-total, up-pending-objects, up-train | — | ShadowByzantine/ShadowByzantine.per#1708 | **PRESERVED** |
| 1709 | L19969–L19980 | QVILLAGERS @ L19918 | `(defrule     (goal gl-need-vills YES)     (up-pending-objects c: villager < 1)     (or (current-age >= castle-age)     (and(current-age >= feudal-age)     (goal gl-strategy FLUS...` | — | — | — | — | up-pending-objects, up-train | — | ShadowByzantine/ShadowByzantine.per#1709 | **PRESERVED** |
| 1710 | L19983–L19994 | QVILLAGERS @ L19918 | `(defrule     (goal gl-strategy KRUSH)     (up-can-train gl-escrow-state c: villager)     (or	(goal gl-need-vills YES)     (and(unit-type-count-total villager < KrushDarkAgeVills...` | — | — | — | — | unit-type-count-total, up-pending-objects, up-train | — | ShadowByzantine/ShadowByzantine.per#1710 | **PRESERVED** |
| 1711 | L19998–L20004 | QESCROW @ L19996 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1712 | L20006–L20012 | QESCROW @ L19996 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1713 | L20015–L20026 | QESCROW @ L19996 | `(defrule     (goal gl-current-build-item FINISHED)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1713 | **PRESERVED** |
| 1714 | L20029–L20042 | QESCROW @ L19996 | `(defrule     (taunt-detected me 21)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1714 | **PRESERVED** |
| 1715 | L20044–L20051 | QESCROW @ L19996 | `(defrule     (or	(escrow-amount food > 850)     (and(escrow-amount food > 700)     (up-compare-goal gl-current-build-item != CUP)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1715 | **PRESERVED** |
| 1716 | L20053–L20061 | QESCROW @ L19996 | `(defrule     (or	(escrow-amount wood > 700)     (and(escrow-amount wood > 250)     (and(up-compare-goal gl-build-progress >= FletchingNumber)     (up-research-status c: castle-a...` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1716 | **PRESERVED** |
| 1717 | L20063–L20070 | QESCROW @ L19996 | `(defrule     (or	(escrow-amount gold > 700)     (and(escrow-amount gold > 200)     (up-research-status c: castle-age < research-pending)))` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1717 | **PRESERVED** |
| 1718 | L20072–L20077 | QESCROW @ L19996 | `(defrule     (escrow-amount stone > 400)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1718 | **PRESERVED** |
| 1719 | L20079–L20095 | QESCROW @ L19996 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1720 | L20100–L20108 | QTSB @ L20097 | `(defrule     (goal gl-trushed YES)` | gl-original-ts, sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1720 | **PRESERVED** |
| 1721 | L20110–L20117 | QTSB @ L20097 | `(defrule     (goal gl-trushed NO)` | sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1721 | **PRESERVED** |
| 1722 | L20120–L20126 | QTSB @ L20097 | `(defrule     (game-time > 1800)` | sn-camp-max-distance | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1722 | **PRESERVED** |
| 1723 | L20129–L20137 | QTSB @ L20097 | `(defrule     (or	(taunt-detected me 26)     (taunt-detected any-enemy 26))` | sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1723 | **PRESERVED** |
| 1724 | L20139–L20146 | QTSB @ L20097 | `(defrule     (taunt-detected me 30)` | sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1724 | **PRESERVED** |
| 1725 | L20150–L20157 | QTSB @ L20097 | `(defrule     (current-age == dark-age)` | gl-original-ts, sn-camp-max-distance, sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1725 | **PRESERVED** |
| 1726 | L20160–L20167 | QTSB @ L20097 | `(defrule     (current-age == feudal-age)` | gl-original-ts, sn-camp-max-distance, sn-maximum-town-size | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1726 | **PRESERVED** |
| 1727 | L20170–L20177 | QTSB @ L20097 | `(defrule     (current-age == castle-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1727 | **PRESERVED** |
| 1728 | L20179–L20186 | QTSB @ L20097 | `(defrule     (current-age-time >= 120)     (current-age == castle-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1728 | **PRESERVED** |
| 1729 | L20190–L20198 | QRANGES @ L20188 | `(defrule     (goal gl-current-build-item RANGES)     (building-type-count-total archery-range >= 2)` | gl-build-progress, gl-current-build-item | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1729 | **PRESERVED** |
| 1730 | L20200–L20204 | QRANGES @ L20188 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1730 | **PRESERVED** |
| 1731 | L20206–L20211 | QRANGES @ L20188 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1325; ShadowByzantine/ShadowByzantine.per#1731; ShadowByzantine/ShadowByzantine.per#1768 | **PRESERVED** |
| 1732 | L20213–L20227 | QRANGES @ L20188 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item RANGES)     (can-build-with-escrow archery-range)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1732 | **PRESERVED** |
| 1733 | L20229–L20235 | QRANGES @ L20188 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1734 | L20237–L20245 | QRANGES @ L20188 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != RANGES)     (up-compare-goal gl-build-progress == RangesNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1734 | **PRESERVED** |
| 1735 | L20248–L20259 | QRANGES @ L20188 | `(defrule     (goal gl-progression-pause -1)     (can-build-with-escrow archery-range)     (goal gl-current-build-item EXTRA-RANGES)` | sn-placement-zone-size | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1735 | **PRESERVED** |
| 1736 | L20261–L20267 | QRANGES @ L20188 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1737 | L20269–L20278 | QRANGES @ L20188 | `(defrule     (false)     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress == 33)     (up-compare-goal gl-current-build-item != EXTRA-RANGES)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1737 | **PRESERVED** |
| 1738 | L20280–L20287 | QRANGES @ L20188 | `(defrule     (false)     (goal gl-current-build-item EXTRA-RANGES)     (building-type-count-total archery-range >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1738 | **PRESERVED** |
| 1739 | L20292–L20302 | QESKIRMS @ L20291 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1740 | L20304–L20310 | QESKIRMS @ L20291 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1741 | L20312–L20319 | QESKIRMS @ L20291 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != ESKIRMS)     (up-compare-goal gl-build-progress == EskirmsNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1741 | **PRESERVED** |
| 1742 | L20321–L20329 | QESKIRMS @ L20291 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == ESKIRMS)` | — | — | set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1742 | **PRESERVED** |
| 1743 | L20331–L20337 | QESKIRMS @ L20291 | `(defrule     (goal gl-current-build-item ESKIRMS)     (up-research-status c: ri-elite-skirmisher >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1743 | **PRESERVED** |
| 1744 | L20341–L20346 | QSW @ L20339 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#841; ShadowByzantine/ShadowByzantine.per#1456; ShadowByzantine/ShadowByzantine.per#1744 | **PRESERVED** |
| 1745 | L20348–L20352 | QSW @ L20339 | `(defrule     (up-compare-goal SUPERIORITY >= 10)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1745 | **PRESERVED** |
| 1746 | L20354–L20358 | QSW @ L20339 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1380; ShadowByzantine/ShadowByzantine.per#1746; ShadowByzantine/ShadowByzantine.per#1763 | **PRESERVED** |
| 1747 | L20360–L20371 | QSW @ L20339 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-progression-pause -1)     (goal gl-current-build-item SW1)     (can-build-with-escrow siege-workshop)     (not(up-pending-placem...` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build, up-pending-placement | — | ShadowByzantine/ShadowByzantine.per#1747 | **PRESERVED** |
| 1748 | L20373–L20379 | QSW @ L20339 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1749 | L20381–L20388 | QSW @ L20339 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != SW1)     (up-compare-goal gl-build-progress == FirstSiegeWorkshopNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1749 | **PRESERVED** |
| 1750 | L20390–L20400 | QSW @ L20339 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-progression-pause == -1)     (up-compare-goal gl-current-build-item == SW1)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1750 | **PRESERVED** |
| 1751 | L20402–L20408 | QSW @ L20339 | `(defrule     (false)     (up-compare-goal gl-current-build-item == SW1)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1751 | **PRESERVED** |
| 1752 | L20410–L20416 | QSW @ L20339 | `(defrule     (goal gl-current-build-item SW1)     (building-type-count-total siege-workshop >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1752 | **PRESERVED** |
| 1753 | L20419–L20430 | QSW @ L20339 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item SW2)     (can-build-with-escrow siege-workshop)` | sn-placement-zone-size | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1753 | **PRESERVED** |
| 1754 | L20432–L20439 | QSW @ L20339 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1755 | L20441–L20450 | QSW @ L20339 | `(defrule     (false)     (goal gl-strategy FLUSH)     (up-compare-goal gl-build-progress == 33)     (up-compare-goal gl-current-build-item != SW2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1755 | **PRESERVED** |
| 1756 | L20452–L20458 | QSW @ L20339 | `(defrule     (goal gl-current-build-item SW2)     (building-type-count-total siege-workshop >= 2)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1756 | **PRESERVED** |
| 1757 | L20461–L20474 | QSW @ L20339 | `(defrule     (gold-amount > 150)     (wood-amount > 250)     (current-age-time > 150)     (can-build siege-workshop)     (goal gl-strategy SIEGE)     (building-type-count-total ...` | sn-placement-zone-size | — | — | — | building-type-count-total, up-build | — | ShadowByzantine/ShadowByzantine.per#1757 | **PRESERVED** |
| 1758 | L20478–L20490 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (research-completed ri-pikeman)     (building-type-count-total barracks < 2)     (players-civilian-population target-player >= 80...` | — | — | — | — | building-type-count-total, research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1758 | **PRESERVED** |
| 1759 | L20492–L20503 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (research-completed ri-pikeman)     (building-type-count-total barracks < 2)     (players-civilian-population any-enemy >= 80)   ...` | gl-progression-pause | — | — | — | building-type-count-total, research, research-completed | — | ShadowByzantine/ShadowByzantine.per#1759 | **PRESERVED** |
| 1760 | L20505–L20509 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause RAX2)` | — | — | up-modify-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1760 | **PRESERVED** |
| 1761 | L20511–L20515 | QRAX @ L20476 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1307; ShadowByzantine/ShadowByzantine.per#1322; ShadowByzantine/ShadowByzantine.per#1336 | **PRESERVED** |
| 1762 | L20517–L20521 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1308; ShadowByzantine/ShadowByzantine.per#1323; ShadowByzantine/ShadowByzantine.per#1365 | **PRESERVED** |
| 1763 | L20523–L20527 | QRAX @ L20476 | `(defrule     (up-compare-goal gl-town-safe != YES)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1380; ShadowByzantine/ShadowByzantine.per#1746; ShadowByzantine/ShadowByzantine.per#1763 | **PRESERVED** |
| 1764 | L20529–L20538 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause RAX2)     (can-build-with-escrow barracks)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1764 | **PRESERVED** |
| 1765 | L20540–L20547 | QRAX @ L20476 | `(defrule     (timer-triggered t-rax)     (building-type-count-total barracks < 1)` | — | t-rax | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1765 | **PRESERVED** |
| 1766 | L20550–L20554 | QRAX @ L20476 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1307; ShadowByzantine/ShadowByzantine.per#1322; ShadowByzantine/ShadowByzantine.per#1336 | **PRESERVED** |
| 1767 | L20556–L20560 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1308; ShadowByzantine/ShadowByzantine.per#1323; ShadowByzantine/ShadowByzantine.per#1365 | **PRESERVED** |
| 1768 | L20562–L20567 | QRAX @ L20476 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1325; ShadowByzantine/ShadowByzantine.per#1731; ShadowByzantine/ShadowByzantine.per#1768 | **PRESERVED** |
| 1769 | L20570–L20582 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (goal gl-strategy FLUSH)     (can-build-with-escrow barracks)     (goal gl-current-build-item RAX)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1769 | **PRESERVED** |
| 1770 | L20584–L20590 | QRAX @ L20476 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1771 | L20592–L20600 | QRAX @ L20476 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != RAX)     (up-compare-goal gl-build-progress == BarracksNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1771 | **PRESERVED** |
| 1772 | L20602–L20609 | QRAX @ L20476 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item RAX)     (building-type-count-total barracks >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1772 | **PRESERVED** |
| 1773 | L20612–L20624 | QRAX @ L20476 | `(defrule     (goal gl-progression-pause -1)     (goal gl-strategy KRUSH)     (can-build-with-escrow barracks)     (goal gl-current-build-item RAX)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1773 | **PRESERVED** |
| 1774 | L20626–L20632 | QRAX @ L20476 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1775 | L20634–L20641 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != RAX)     (up-compare-goal gl-build-progress == KrushBarracksNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1775 | **PRESERVED** |
| 1776 | L20643–L20650 | QRAX @ L20476 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item RAX)     (building-type-count-total barracks >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1776 | **PRESERVED** |
| 1777 | L20653–L20657 | QSMITH @ L20652 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#120; ShadowByzantine/ShadowByzantine.per#136; ShadowByzantine/ShadowByzantine.per#1777 | **PRESERVED** |
| 1778 | L20659–L20663 | QSMITH @ L20652 | `(defrule     (goal gl-town-safe NO)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1778 | **PRESERVED** |
| 1779 | L20666–L20683 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow blacksmith)     (goal gl-current-build-item SMITH)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1779 | **PRESERVED** |
| 1780 | L20685–L20691 | QSMITH @ L20652 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1781 | L20693–L20700 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != SMITH)     (up-compare-goal gl-build-progress == BlackmithNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1781 | **PRESERVED** |
| 1782 | L20702–L20713 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1782 | **PRESERVED** |
| 1783 | L20715–L20722 | QSMITH @ L20652 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item SMITH)     (building-type-count-total blacksmith >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1783 | **PRESERVED** |
| 1784 | L20725–L20737 | QSMITH @ L20652 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-strategy KRUSH)     (can-build-with-escrow blacksmith)     (goal gl-current-build-item SMITH)` | — | — | can-build-with-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1784 | **PRESERVED** |
| 1785 | L20739–L20745 | QSMITH @ L20652 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1786 | L20747–L20754 | QSMITH @ L20652 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != SMITH)     (up-compare-goal gl-build-progress == KrushSmithNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1786 | **PRESERVED** |
| 1787 | L20756–L20763 | QSMITH @ L20652 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item SMITH)     (building-type-count-total blacksmith >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1787 | **PRESERVED** |
| 1788 | L20767–L20772 | QCASTLES @ L20765 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1788 | **PRESERVED** |
| 1789 | L20774–L20780 | QCASTLES @ L20765 | `(defrule     (not(player-valid 3))     (up-compare-goal SUPERIORITY >= 20)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1789 | **PRESERVED** |
| 1790 | L20782–L20788 | QCASTLES @ L20765 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1790 | **PRESERVED** |
| 1791 | L20790–L20798 | QCASTLES @ L20765 | `(defrule     (can-build castle)     (current-age >= castle-age)` | sn-placement-zone-size | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1791 | **PRESERVED** |
| 1792 | L20801–L20817 | QFARMS @ L20800 | `(defrule     (goal gl-ninety-turn 1)     (goal gl-strategy KRUSH)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-get-fact, up-research | — | ShadowByzantine/ShadowByzantine.per#1792 | **PRESERVED** |
| 1793 | L20819–L20828 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1794 | L20831–L20848 | QFARMS @ L20800 | `(defrule     (idle-farm-count < 2)     (goal gl-strategy KRUSH)     (current-age == feudal-age)     (can-build-with-escrow farm)     (up-pending-objects c: farm < 3)     (buildi...` | — | — | can-build-with-escrow | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1794 | **PRESERVED** |
| 1795 | L20851–L20857 | QFARMS @ L20800 | `(defrule     (or	(goal gl-current-build-item MARKET1)     (or	(up-pending-placement c: blacksmith)     (up-compare-goal gl-strategy != FLUSH)))` | — | — | — | — | up-pending-placement | 1 | ShadowByzantine/ShadowByzantine.per#1795 | **PRESERVED** |
| 1796 | L20859–L20871 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1797 | L20873–L20882 | QFARMS @ L20800 | `(defrule     (goal SPLIT 1)     (or	(building-type-count-total blacksmith >= 1)     (or	(and(up-compare-goal rt >= 2)     (building-type-count-total farm < 7))     (and(up-compa...` | split | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1797 | **PRESERVED** |
| 1798 | L20884–L20892 | QFARMS @ L20800 | `(defrule     (goal SPLIT 2)     (or	(nand	(current-age == castle-age)     (up-compare-goal gl-current-build-item == ESKIRMS))     (up-research-status c: ri-elite-skirmisher >= r...` | — | — | — | — | research-pending, up-build, up-research | — | ShadowByzantine/ShadowByzantine.per#1798 | **PRESERVED** |
| 1799 | L20894–L20899 | QFARMS @ L20800 | `(defrule     (true)` | gl-escrow-state, split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1288; ShadowByzantine/ShadowByzantine.per#1799 | **PRESERVED** |
| 1800 | L20902–L20911 | QFARMS @ L20800 | `(defrule     (can-build farm)     (wood-amount >= 90)     (idle-farm-count < 2)     (up-compare-goal MILL != YES)     (up-pending-objects c: farm < 2)     (building-type-count-t...` | split | — | — | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1800 | **PRESERVED** |
| 1801 | L20913–L20923 | QFARMS @ L20800 | `(defrule     (goal SPLIT 1)     (or	(current-age >= castle-age)     (and(goal gl-strategy KRUSH)     (up-research-status c: ri-horse-collar >= research-complete)))     (or	(wood...` | — | — | — | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1801 | **PRESERVED** |
| 1802 | L20925–L20929 | QFARMS @ L20800 | `(defrule     (true)` | split | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#49; ShadowByzantine/ShadowByzantine.per#311; ShadowByzantine/ShadowByzantine.per#346 | **PRESERVED** |
| 1803 | L20932–L20943 | QFARMS @ L20800 | `(defrule     (goal gl-second-turn 1)     (goal gl-strategy FLUSH)     (up-can-build gl-escrow-state c: farm)     (up-compare-goal gl-build-progress < FletchingNumber)     (or	(w...` | — | — | — | — | building-type-count-total, up-build | — | ShadowByzantine/ShadowByzantine.per#1803 | **PRESERVED** |
| 1804 | L20949–L20963 | QFARMS @ L20800 | `(defrule     (current-age == dark-age)     (can-build-with-escrow farm)     (goal gl-strategy KRUSH)     (up-pending-objects c: farm < 1)     (goal gl-current-build-item FARMS) ...` | — | — | can-build-with-escrow | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1804 | **PRESERVED** |
| 1805 | L20965–L20973 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item FARMS)     (building-type-count-total farm >= 4)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1805 | **PRESERVED** |
| 1806 | L20975–L20981 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1807 | L20983–L20990 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != FARMS)     (up-compare-goal gl-build-progress == KrushFarmsNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1807 | **PRESERVED** |
| 1808 | L20993–L21006 | QFARMS @ L20800 | `(defrule     (current-age == dark-age)     (can-build-with-escrow farm)     (or (wood-amount >= 90)     (housing-headroom >= 3))     (goal gl-strategy KRUSH)     (up-pending-obj...` | — | — | can-build-with-escrow | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1808 | **PRESERVED** |
| 1809 | L21008–L21016 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item FARMS2)     (building-type-count-total farm >= 7)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1809 | **PRESERVED** |
| 1810 | L21018–L21025 | QFARMS @ L20800 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != FARMS2)     (up-compare-goal gl-build-progress == KrushFarms2Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1810 | **PRESERVED** |
| 1811 | L21028–L21041 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1812 | L21043–L21050 | QFARMS @ L20800 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item FARMS)     (building-type-count-total farm >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1812 | **PRESERVED** |
| 1813 | L21052–L21058 | QFARMS @ L20800 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1814 | L21060–L21068 | QFARMS @ L20800 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != FARMS)     (up-compare-goal gl-build-progress == FarmsNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1814 | **PRESERVED** |
| 1815 | L21071–L21076 | QHOUSE @ L21070 | `(defrule     (true)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#190; ShadowByzantine/ShadowByzantine.per#254; ShadowByzantine/ShadowByzantine.per#270 | **PRESERVED** |
| 1816 | L21078–L21086 | QHOUSE @ L21070 | `(defrule     (false)     (game-time >= 50)     (goal gl-fifth-turn 1)     (housing-headroom < 2)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1816 | **PRESERVED** |
| 1817 | L21088–L21099 | QHOUSE @ L21070 | `(defrule     (game-time > 6)     (housing-headroom < 5)     (population-headroom != 0)     (can-build-with-escrow house)     (up-pending-objects c: house < 1)     (building-type...` | — | — | can-build-with-escrow | — | up-build, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1817 | **PRESERVED** |
| 1818 | L21101–L21111 | QHOUSE @ L21070 | `(defrule     (game-time > 6)     (housing-headroom < 2)     (population-headroom != 0)     (can-build-with-escrow house)     (up-pending-objects c: house < 1)` | — | — | can-build-with-escrow | — | up-build, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1818 | **PRESERVED** |
| 1819 | L21113–L21120 | QHOUSE @ L21070 | `(defrule     (can-build house)` | — | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1819 | **PRESERVED** |
| 1820 | L21122–L21134 | QHOUSE @ L21070 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1821 | L21136–L21140 | QHOUSE @ L21070 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1821 | **PRESERVED** |
| 1822 | L21142–L21147 | QHOUSE @ L21070 | `(defrule     (or	(goal gl-enemy-strategy DRUSH)     (up-compare-goal gl-town-safe != YES))` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1325; ShadowByzantine/ShadowByzantine.per#1731; ShadowByzantine/ShadowByzantine.per#1768 | **PRESERVED** |
| 1823 | L21149–L21162 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 4)     (population-headroom != 0)     (building-type-count house < 5)     (up-pending-objects c: house < 1)` | — | — | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1823 | **PRESERVED** |
| 1824 | L21164–L21178 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 4)     (population-headroom != 0)     (building-type-count house >= 5)     (up-pending-objects c: house < 1)     (building...` | — | — | — | — | up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1824 | **PRESERVED** |
| 1825 | L21180–L21193 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 10)     (population-headroom != 0)     (up-pending-objects c: house < 1)     (or	(and(goal gl-strategy KRUSH)     (buildin...` | sn-placement-fail-delta, sn-placement-zone-size | — | — | — | building-type-count-total, up-build, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1825 | **PRESERVED** |
| 1826 | L21195–L21208 | QHOUSE @ L21070 | `(defrule     (can-build house)     (housing-headroom < 15)     (population-headroom != 0)     (up-pending-objects c: house < 2)     (or	(and(goal gl-strategy FLUSH)     (buildin...` | split | — | — | — | building-type-count-total, up-pending-objects | — | ShadowByzantine/ShadowByzantine.per#1826 | **PRESERVED** |
| 1827 | L21210–L21218 | QHOUSE @ L21070 | `(defrule     (goal SPLIT 1)` | sn-placement-fail-delta, sn-placement-zone-size, split | — | — | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1827 | **PRESERVED** |
| 1828 | L21222–L21235 | QLC @ L21220 | `(defrule     (goal gl-fifth-turn 1)     (civilian-population >= 7)     (or	(housing-headroom >= 5)     (civilian-population >= 15))     (goal gl-current-build-item LC1)     (can...` | sn-allow-adjacent-dropsites | — | can-build-with-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1828 | **PRESERVED** |
| 1829 | L21238–L21244 | QLC @ L21220 | `(defrule     (goal gl-dark-build LumberFirst)     (up-compare-goal gl-build-progress > 1)     (building-type-count-total lumber-camp < 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1829 | **PRESERVED** |
| 1830 | L21246–L21252 | QLC @ L21220 | `(defrule     (goal gl-dark-build MillFirst)     (up-compare-goal gl-build-progress > 2)     (building-type-count-total lumber-camp < 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1830 | **PRESERVED** |
| 1831 | L21254–L21264 | QLC @ L21220 | `(defrule     (up-compare-goal gl-current-build-item != LC1)     (or	(and(goal gl-dark-build MillFirst)     (up-compare-goal gl-build-progress == 2))     (and(goal gl-dark-build ...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1831 | **PRESERVED** |
| 1832 | L21267–L21273 | QLC @ L21220 | `(defrule     (goal gl-current-build-item LC1)     (building-type-count-total lumber-camp >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1832 | **PRESERVED** |
| 1833 | L21276–L21286 | QLC @ L21220 | `(defrule     (can-build lumber-camp)     (current-age >= feudal-age)     (up-gaia-type-count c: wood > 20)     (building-type-count-total lumber-camp < 1)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1833 | **PRESERVED** |
| 1834 | L21290–L21297 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item LC2)     (building-type-count-total lumber-camp >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1834 | **PRESERVED** |
| 1835 | L21299–L21314 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item LC2)     (or	(game-time >= 480)     (or	(wood-amount >= 110)     (housing-headroom >= 5)))     (can-build-w...` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow, set-escrow-percentage | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1835 | **PRESERVED** |
| 1836 | L21316–L21322 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1837 | L21324–L21332 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LC2)     (up-compare-goal gl-build-progress == LC2Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1837 | **PRESERVED** |
| 1838 | L21335–L21342 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item LC2)     (building-type-count-total lumber-camp >= 2)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1838 | **PRESERVED** |
| 1839 | L21344–L21359 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item LC2)     (or	(game-time >= 480)     (or	(wood-amount >= 110)     (housing-headroom >= 5)))     (can-build-w...` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1839 | **PRESERVED** |
| 1840 | L21361–L21367 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1841 | L21369–L21376 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != LC2)     (up-compare-goal gl-build-progress == KrushLC2Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1841 | **PRESERVED** |
| 1842 | L21380–L21392 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item LC3)     (can-build-with-escrow lumber-camp)` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1842 | **PRESERVED** |
| 1843 | L21394–L21400 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1844 | L21402–L21410 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LC3)     (up-compare-goal gl-build-progress == LC3Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1844 | **PRESERVED** |
| 1845 | L21412–L21419 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-current-build-item LC3)     (building-type-count-total lumber-camp >= 3)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1845 | **PRESERVED** |
| 1846 | L21422–L21434 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (goal gl-current-build-item LC3)     (can-build-with-escrow lumber-camp)` | sn-allow-adjacent-dropsites, sn-dropsite-separation-distance | — | can-build-with-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1846 | **PRESERVED** |
| 1847 | L21436–L21442 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1848 | L21444–L21452 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != LC3)     (up-compare-goal gl-build-progress == KrushLC3Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1848 | **PRESERVED** |
| 1849 | L21454–L21461 | QLC @ L21220 | `(defrule     (goal gl-strategy KRUSH)     (goal gl-current-build-item LC3)     (building-type-count-total lumber-camp >= 3)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1849 | **PRESERVED** |
| 1850 | L21464–L21468 | QLC @ L21220 | `(defrule     (true)` | — | — | — | — | — | 4 | ShadowByzantine/ShadowByzantine.per#1850 | **PRESERVED** |
| 1851 | L21470–L21479 | QLC @ L21220 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item LC4)     (can-build-with-escrow lumber-camp)` | — | — | can-build-with-escrow, release-escrow, set-escrow-percentage | — | build | — | ShadowByzantine/ShadowByzantine.per#1851 | **PRESERVED** |
| 1852 | L21481–L21487 | QLC @ L21220 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1853 | L21489–L21497 | QLC @ L21220 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != LC4)     (up-compare-goal gl-build-progress == LC4Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1853 | **PRESERVED** |
| 1854 | L21499–L21505 | QLC @ L21220 | `(defrule     (goal gl-current-build-item LC4)     (building-type-count-total lumber-camp >= 4)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1854 | **PRESERVED** |
| 1855 | L21509–L21522 | QLC @ L21220 | `(defrule     (or	(game-time >= 1570)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1855 | **PRESERVED** |
| 1856 | L21527–L21536 | QTRADING @ L21524 | `(defrule     (food-amount < 50)     (can-buy-commodity food)     (or	(gold-amount >= 230)     (and(gold-amount >= 170)     (up-compare-goal gl-build-progress < 13)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1856 | **PRESERVED** |
| 1857 | L21538–L21550 | QTRADING @ L21524 | `(defrule     (can-buy-commodity food)     (or	(and(food-amount < 800)     (gold-amount >= 300))     (or	(and(food-amount < 550)     (gold-amount >= 240))     (and(food-amount < ...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1857 | **PRESERVED** |
| 1858 | L21553–L21563 | QTRADING @ L21524 | `(defrule     (wood-amount < 50)     (or	(gold-amount >= 320)     (and(gold-amount >= 240)     (or	(up-compare-goal gl-current-build-item < LC3)     (up-compare-goal gl-current-b...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1858 | **PRESERVED** |
| 1859 | L21567–L21575 | QTRADING @ L21524 | `(defrule     (gold-amount < 100)     (food-amount >= 320)     (can-sell-commodity food)     (up-research-status c: castle-age >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1859 | **PRESERVED** |
| 1860 | L21577–L21587 | QTRADING @ L21524 | `(defrule     (can-sell-commodity food)     (or	(and(gold-amount < 160)     (food-amount >= 880))     (and(gold-amount < 200)     (food-amount >= 980)))     (goal gl-current-buil...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1860 | **PRESERVED** |
| 1861 | L21590–L21598 | QTRADING @ L21524 | `(defrule     (wood-amount >= 270)     (goal gl-strategy FLUSH)     (can-sell-commodity wood)     (up-compare-goal gl-build-progress >= ExtraStablesNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1861 | **PRESERVED** |
| 1862 | L21600–L21607 | QTRADING @ L21524 | `(defrule     (wood-amount >= 260)     (can-sell-commodity wood)     (goal gl-current-build-item EXTRA-STABLES)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1862 | **PRESERVED** |
| 1863 | L21609–L21621 | QTRADING @ L21524 | `(defrule     (can-sell-commodity wood)     (up-compare-goal gl-current-build-item != EXTRA-STABLES)     (or	(and(gold-amount < 60)     (wood-amount >= 260))     (and(food-amount...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1863 | **PRESERVED** |
| 1864 | L21623–L21632 | QTRADING @ L21524 | `(defrule     (wood-amount >= 150)     (or	(food-amount < 750)     (gold-amount < 160))     (can-sell-commodity wood)     (goal gl-current-build-item CUP)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1864 | **PRESERVED** |
| 1865 | L21635–L21647 | QTRADING @ L21524 | `(defrule     (false)     (can-sell-commodity stone)     (or	(and(gold-amount < 100)     (stone-amount >= 220))     (or	(and(wood-amount < 100)     (stone-amount >= 220))     (an...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1865 | **PRESERVED** |
| 1866 | L21651–L21665 | QMILL @ L21649 | `(defrule     (can-build-with-escrow mill)     (or (resource-found food)     (game-time >= SkipMillTime))     (goal gl-current-build-item MILL1)     (building-type-count-total mi...` | sn-allow-adjacent-dropsites | t-build-delay | can-build-with-escrow, set-escrow-percentage | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1866 | **PRESERVED** |
| 1867 | L21667–L21673 | QMILL @ L21649 | `(defrule     (goal gl-current-build-item MILL1)     (building-type-count-total mill >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1867 | **PRESERVED** |
| 1868 | L21675–L21682 | QMILL @ L21649 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1869 | L21684–L21691 | QMILL @ L21649 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1870 | L21693–L21703 | QMILL @ L21649 | `(defrule     (up-compare-goal gl-current-build-item != MILL1)     (or	(and(goal gl-dark-build MillFirst)     (up-compare-goal gl-build-progress == 1))     (and(goal gl-dark-buil...` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1870 | **PRESERVED** |
| 1871 | L21706–L21716 | QMILL @ L21649 | `(defrule     (can-build mill)     (resource-found food)     (current-age >= feudal-age)     (building-type-count-total mill < 1)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1871 | **PRESERVED** |
| 1872 | L21718–L21722 | QMILL @ L21649 | `(defrule     (true)` | goal | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1872 | **PRESERVED** |
| 1873 | L21724–L21728 | QMILL @ L21649 | `(defrule     (building-type-count-total mill == 2)` | goal | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1873 | **PRESERVED** |
| 1874 | L21730–L21734 | QMILL @ L21649 | `(defrule     (building-type-count-total mill == 3)` | goal | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1874 | **PRESERVED** |
| 1875 | L21736–L21746 | QMILL @ L21649 | `(defrule     (goal MILL YES)     (can-build mill)     (building-type-count-total mill < 4)` | — | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1875 | **PRESERVED** |
| 1876 | L21748–L21760 | QMILL @ L21649 | `(defrule     (up-compare-goal MILL != YES)     (not(up-pending-placement c: mill))     (or	(and(building-type-count-total mill < 2)     (building-type-count-total farm > 20))   ...` | — | — | — | — | building-type-count-total, up-pending-placement | — | ShadowByzantine/ShadowByzantine.per#1876 | **PRESERVED** |
| 1877 | L21766–L21779 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1878 | L21781–L21796 | QMC @ L21762 | `(defrule     (goal gl-progression-pause -1)     (goal gl-strategy KRUSH)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC1)     (building-type-coun...` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1878 | **PRESERVED** |
| 1879 | L21798–L21809 | QMC @ L21762 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy KRUSH)     (goal gl-progression-pause -1)     (dropsite-min-distance gold > 3)     (can-build-with-escrow mining-camp) ...` | split | t-build-delay | can-build-with-escrow | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#1879 | **PRESERVED** |
| 1880 | L21811–L21827 | QMC @ L21762 | `(defrule     (goal SPLIT 1)` | — | t-build-delay | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1880; ShadowByzantine/ShadowByzantine.per#1887 | **PRESERVED** |
| 1881 | L21829–L21835 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1882 | L21837–L21844 | QMC @ L21762 | `(defrule     (goal gl-strategy KRUSH)     (up-compare-goal gl-current-build-item != GOLDMC1)     (up-compare-goal gl-build-progress == KrushGoldMCNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1882 | **PRESERVED** |
| 1883 | L21846–L21854 | QMC @ L21762 | `(defrule     (goal gl-strategy KRUSH)     (dropsite-min-distance gold < 5)     (goal gl-current-build-item GOLDMC1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1883 | **PRESERVED** |
| 1884 | L21857–L21870 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1885 | L21872–L21887 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC1)     (building-type-coun...` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1885 | **PRESERVED** |
| 1886 | L21889–L21900 | QMC @ L21762 | `(defrule     (goal gl-tenth-turn 1)     (goal gl-strategy FLUSH)     (goal gl-progression-pause -1)     (dropsite-min-distance gold > 3)     (can-build-with-escrow mining-camp) ...` | split | t-build-delay | can-build-with-escrow | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#1886 | **PRESERVED** |
| 1887 | L21902–L21918 | QMC @ L21762 | `(defrule     (goal SPLIT 1)` | — | t-build-delay | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1880; ShadowByzantine/ShadowByzantine.per#1887 | **PRESERVED** |
| 1888 | L21920–L21926 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1889 | L21928–L21936 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDMC1)     (up-compare-goal gl-build-progress == GoldMC1Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1889 | **PRESERVED** |
| 1890 | L21938–L21945 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (dropsite-min-distance gold < 5)     (goal gl-current-build-item GOLDMC1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1890 | **PRESERVED** |
| 1891 | L21948–L21952 | QMC @ L21762 | `(defrule     (true)` | — | — | — | — | — | 5 | ShadowByzantine/ShadowByzantine.per#1891 | **PRESERVED** |
| 1892 | L21954–L21967 | QMC @ L21762 | `(defrule     (false)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC2)` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#1892 | **PRESERVED** |
| 1893 | L21969–L21987 | QMC @ L21762 | `(defrule     (false)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item GOLDMC2)     (up-set-target-object search-remote ...` | — | — | can-build-with-escrow | up-set-target-object | — | — | ShadowByzantine/ShadowByzantine.per#1893 | **PRESERVED** |
| 1894 | L21989–L21995 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1895 | L21997–L22005 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != GOLDMC2)     (up-compare-goal gl-build-progress == GoldMC2Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1895 | **PRESERVED** |
| 1896 | L22007–L22013 | QMC @ L21762 | `(defrule     (goal gl-current-build-item GOLDMC2)     (building-type-count-total mining-camp >= 3)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1896 | **PRESERVED** |
| 1897 | L22016–L22030 | QMC @ L21762 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item STONEMC1)` | sn-focus-player-number | — | can-build-with-escrow | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | — | — | ShadowByzantine/ShadowByzantine.per#1897 | **PRESERVED** |
| 1898 | L22032–L22051 | QMC @ L21762 | `(defrule     (goal gl-fifth-turn 1)     (goal gl-progression-pause -1)     (can-build-with-escrow mining-camp)     (goal gl-current-build-item STONEMC1)` | — | — | can-build-with-escrow | — | — | — | ShadowByzantine/ShadowByzantine.per#1898 | **PRESERVED** |
| 1899 | L22053–L22059 | QMC @ L21762 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1900 | L22061–L22069 | QMC @ L21762 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != STONEMC1)     (up-compare-goal gl-build-progress == StoneMC1Number)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1900 | **PRESERVED** |
| 1901 | L22071–L22077 | QMC @ L21762 | `(defrule     (dropsite-min-distance stone < 5)     (goal gl-current-build-item STONEMC1)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1901 | **PRESERVED** |
| 1902 | L22080–L22095 | QMC @ L21762 | `(defrule     (or	(game-time >= 1480)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1902 | **PRESERVED** |
| 1903 | L22098–L22107 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-progression-pause -1)     (can-build-with-escrow university)     (goal gl-current-build-item UNIVERSITY)` | sn-placement-zone-size | — | can-build-with-escrow | — | up-build | — | ShadowByzantine/ShadowByzantine.per#1903 | **PRESERVED** |
| 1904 | L22109–L22115 | QUNIVERSITY @ L22097 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1905 | L22117–L22125 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != UNIVERSITY)     (up-compare-goal gl-build-progress == UniversityNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1905 | **PRESERVED** |
| 1906 | L22127–L22136 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == UNIVERSITY)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1906 | **PRESERVED** |
| 1907 | L22138–L22144 | QUNIVERSITY @ L22097 | `(defrule     (goal gl-current-build-item UNIVERSITY)     (building-type-count-total university >= 1)` | gl-build-progress | — | — | — | building-type-count-total | — | ShadowByzantine/ShadowByzantine.per#1907 | **PRESERVED** |
| 1908 | L22147–L22154 | QBALLISTICS @ L22146 | `(defrule     (goal gl-progression-pause -1)     (goal gl-current-build-item BALLISTICS)     (can-research-with-escrow ri-ballistics)` | — | — | can-research-with-escrow | — | up-research | — | ShadowByzantine/ShadowByzantine.per#1908 | **PRESERVED** |
| 1909 | L22156–L22162 | QBALLISTICS @ L22146 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1910 | L22164–L22173 | QBALLISTICS @ L22146 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item != BALLISTICS)     (up-compare-goal gl-build-progress == BallisticsNumber)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1910 | **PRESERVED** |
| 1911 | L22175–L22183 | QBALLISTICS @ L22146 | `(defrule     (goal gl-strategy FLUSH)     (up-compare-goal gl-current-build-item == BALLISTICS)` | — | — | release-escrow, set-escrow-percentage | — | — | — | ShadowByzantine/ShadowByzantine.per#1911 | **PRESERVED** |
| 1912 | L22185–L22191 | QBALLISTICS @ L22146 | `(defrule     (goal gl-current-build-item BALLISTICS)     (up-research-status c: ri-ballistics >= research-pending)` | — | — | — | — | research-pending, up-research | — | ShadowByzantine/ShadowByzantine.per#1912 | **PRESERVED** |
| 1913 | L22195–L22200 | QEND @ L22193 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1914 | L22203–L22210 | QEND @ L22193 | `(defrule     (game-time > 45)     (goal gl-position FLANK)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1914 | **PRESERVED** |
| 1915 | L22212–L22218 | QEND @ L22193 | `(defrule     (game-time > 46)     (goal gl-position FLANK)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1915 | **PRESERVED** |
| 1916 | L22221–L22226 | QMISC @ L22220 | `(defrule     (true)` | gl-identity | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1916 | **PRESERVED** |
| 1917 | L22228–L22237 | QMISC @ L22220 | `(defrule     (game-time > 20)     (game-time < 40)     (or	(death-match-game)     (or	(current-age > dark-age)     (not(civ-selected viking))))` | — | — | — | — | — | — | — | **LOST** |
| 1918 | L22239–L22249 | QMISC @ L22220 | `(defrule     (goal gl-strategy FLUSH)     (or	(taunt-detected me 250)     (or	(taunt-detected any-ally 250)     (taunt-detected any-enemy 250)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1918 | **PRESERVED** |
| 1919 | L22251–L22261 | QMISC @ L22220 | `(defrule     (goal gl-strategy KRUSH)     (or	(taunt-detected me 250)     (or	(taunt-detected any-ally 250)     (taunt-detected any-enemy 250)))` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1919 | **PRESERVED** |
| 1920 | L22265–L22273 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (game-time < 660)     (not(goal EARLY-MINING-NOTICE YES))     (players-building-type-count target-player mining-camp > 0)` | early-mining-notice | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1920 | **PRESERVED** |
| 1921 | L22275–L22284 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (goal gl-enemy-strategy -1)     (players-current-age-time target-player > 100)     (players-current-age target-player > dark-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1921 | **PRESERVED** |
| 1922 | L22287–L22296 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (goal gl-enemy-strategy -1)     (players-current-age target-player == dark-age)     (players-military-population target-player > 2)` | gl-enemy-strategy | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1922 | **PRESERVED** |
| 1923 | L22299–L22312 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (not(goal gl-enemy-strategy RANGED-FLUSH))     (players-current-age target-player == feudal-age)     (or	(and(players-current-age-time target-player < 1...` | gl-enemy-strategy, gl-enemy-strategy-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1923 | **PRESERVED** |
| 1924 | L22314–L22325 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (not(goal gl-enemy-strategy SCRUSH))     (players-current-age target-player == feudal-age)     (players-building-type-count target-player archery-range ...` | gl-enemy-strategy, gl-enemy-strategy-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1924 | **PRESERVED** |
| 1925 | L22327–L22336 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (goal gl-enemy-strategy-type FC)     (up-compare-goal gl-target-age < CA-loading)     (players-current-age-time target-player > 100)     (players-curren...` | gl-enemy-strategy-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1925 | **PRESERVED** |
| 1926 | L22339–L22350 | QENEMY STRATEGY @ L22263 | `(defrule     (false)     (not(goal gl-enemy-strategy KRUSH))     (players-current-age target-player == feudal-age)     (players-building-type-count target-player stable > 0)    ...` | gl-enemy-strategy, gl-enemy-strategy-type | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1926 | **PRESERVED** |
| 1927 | L22354–L22359 | QEAGOL @ L22352 | `(defrule     (true)` | — | — | — | — | up-get-fact | — | ShadowByzantine/ShadowByzantine.per#1927 | **PRESERVED** |
| 1928 | L22362–L22367 | QEAGOL @ L22352 | `(defrule     (true)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1928 | **PRESERVED** |
| 1929 | L22369–L22374 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age FA-loading)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1929 | **PRESERVED** |
| 1930 | L22376–L22382 | QEAGOL @ L22352 | `(defrule     (up-compare-goal gl-target-age < FA)     (players-current-age target-player == feudal-age)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1930 | **PRESERVED** |
| 1931 | L22384–L22389 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age CA-loading)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1931 | **PRESERVED** |
| 1932 | L22391–L22396 | QEAGOL @ L22352 | `(defrule     (up-compare-goal gl-target-age < CA)     (players-current-age target-player >= castle-age)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1932 | **PRESERVED** |
| 1933 | L22398–L22403 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age IA-loading)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1933 | **PRESERVED** |
| 1934 | L22405–L22410 | QEAGOL @ L22352 | `(defrule     (up-compare-goal gl-target-age < IA)     (players-current-age target-player >= imperial-age)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1934 | **PRESERVED** |
| 1935 | L22413–L22422 | QEAGOL @ L22352 | `(defrule     (game-time > 10)     (player-valid target-player)     (players-building-count target-player > 0)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1935 | **PRESERVED** |
| 1936 | L22424–L22428 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age-checking YES)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1936 | **PRESERVED** |
| 1937 | L22430–L22435 | QEAGOL @ L22352 | `(defrule     (true)` | gl-target-score1 | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1937 | **PRESERVED** |
| 1938 | L22438–L22443 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age-checking YES)     (players-current-age target-player == dark-age)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1938 | **PRESERVED** |
| 1939 | L22446–L22453 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age-checking YES)     (up-compare-goal gl-target-score1 > 37)     (up-compare-goal gl-target-age < FA-loading)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1939 | **PRESERVED** |
| 1940 | L22455–L22464 | QEAGOL @ L22352 | `(defrule     (false)     (goal gl-target-age-checking YES)     (goal gl-target-age FA-loading)     (up-compare-goal gl-target-score1 < -37)     (up-timer-status t-enemy-age-canc...` | gl-target-age | t-enemy-age-cancel | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1940 | **PRESERVED** |
| 1941 | L22466–L22472 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age FA-loading)     (goal gl-target-age-checking YES)     (players-current-age target-player == feudal-age)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1941 | **PRESERVED** |
| 1942 | L22475–L22483 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age FA)     (false)     (up-compare-goal gl-target-score1 > 65)     (players-current-age-time target-player > 30)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1942 | **PRESERVED** |
| 1943 | L22485–L22494 | QEAGOL @ L22352 | `(defrule     (false)     (goal gl-target-age CA-loading)     (goal gl-target-age-checking YES)     (up-compare-goal gl-target-score1 < -65)     (up-timer-status t-enemy-age-canc...` | — | t-enemy-age-cancel | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1943 | **PRESERVED** |
| 1944 | L22496–L22502 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age CA-loading)     (goal gl-target-age-checking YES)     (players-current-age target-player == castle-age)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1944 | **PRESERVED** |
| 1945 | L22505–L22512 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age CA)     (up-compare-goal gl-target-score1 > 100)     (players-current-age-time target-player > 30)` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1945 | **PRESERVED** |
| 1946 | L22514–L22523 | QEAGOL @ L22352 | `(defrule     (false)     (goal gl-target-age-checking YES)     (goal gl-target-age IA-loading)     (up-compare-goal gl-target-score1 < -100)     (up-timer-status t-enemy-age-can...` | gl-target-age | t-enemy-age-cancel | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1946 | **PRESERVED** |
| 1947 | L22525–L22531 | QEAGOL @ L22352 | `(defrule     (goal gl-target-age IA-loading)     (goal gl-target-age-checking YES)     (players-current-age target-player == imperial-age)` | gl-target-age | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1947 | **PRESERVED** |
| 1948 | L22533–L22539 | QEAGOL @ L22352 | `(defrule` | — | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#51; ShadowByzantine/ShadowByzantine.per#52; ShadowByzantine/ShadowByzantine.per#82 | **PRESERVED** |
| 1949 | L22542–L22546 | QSPECIAL TIMERS @ L22541 | `(defrule     (timer-triggered 30SEC)` | gl-switch | 30sec | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1949 | **PRESERVED** |
| 1950 | L22548–L22552 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status 30SEC != timer-running)` | — | 30sec | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1950 | **PRESERVED** |
| 1951 | L22554–L22558 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status ONE-MINUTE != timer-running)` | — | one-minute | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1951 | **PRESERVED** |
| 1952 | L22560–L22564 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status THREE-MINUTE != timer-running)` | — | three-minute | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1952 | **PRESERVED** |
| 1953 | L22566–L22570 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status TWO-MINUTE != timer-running)` | — | two-minute | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1953 | **PRESERVED** |
| 1954 | L22572–L22576 | QSPECIAL TIMERS @ L22541 | `(defrule     (up-timer-status five-seconds-timer != timer-running)` | — | five-seconds-timer | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1954 | **PRESERVED** |
| 1955 | L22578–L22590 | QSPECIAL TIMERS @ L22541 | `(defrule     (true)` | gl-fifth-turn, gl-second-turn, gl-seventh-turn, gl-tenth-turn, gl-turn-count | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1955 | **PRESERVED** |
| 1956 | L22592–L22603 | QSPECIAL TIMERS @ L22541 | `(defrule     (true)` | gl-fifty-turn, gl-ninety-turn, gl-thirty-turn, gl-twenty-turn | — | — | — | — | — | ShadowByzantine/ShadowByzantine.per#1956 | **PRESERVED** |

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
| `ShadowByzantine/ShadowByzantine.per` | 1 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 2 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 3 | disable-self | QPOSITION @ L1401 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 4 | build, disable-self, up-find-local, up-full-reset-search, up-set-target-object | QADVANTAGE @ L2057, QEAGOL @ L1723 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 5 | up-find-local, up-full-reset-search, up-set-target-object | QADVANTAGE @ L2057, QEAGOL @ L1723 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 6 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 7 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 8 | — | QEAGOL @ L1723 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 9 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 10 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 11 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 12 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 13 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 14 | up-jump-rule | QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 15 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 16 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 17 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 18 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 19 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 20 | research, research-completed | QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 21 | research, research-completed | QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 22 | research, research-completed | QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 23 | disable-self, research, research-completed | QCHAT @ L16797, QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 24 | disable-self, research, research-completed | QCHAT @ L16797, QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 25 | research, research-completed | QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 26 | research, research-completed | QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 27 | up-jump-rule | QADVANTAGE @ L2057 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 28 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 29 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QADVANTAGE @ L2057, QSPEARS @ L8501, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 30 | research, research-pending, up-research | QADVANTAGE @ L2057, QDLURING @ L6795, QFORCEDROP @ L7949 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 31 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 32 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 33 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 34 | up-full-reset-search, up-get-search-state, up-remove-objects | QADVANTAGE @ L2057, QBH @ L7174, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 35 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 36 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 37 | up-find-remote, up-full-reset-search, up-get-search-state | QADVANTAGE @ L2057, QRAIDING @ L10481, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 38 | up-find-local, up-full-reset-search, up-set-target-object | QADVANTAGE @ L2057, QEAGOL @ L1723 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 39 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 40 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 41 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 42 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 43 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 44 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 45 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 46 | up-find-local, up-full-reset-search, up-set-target-object | QADVANTAGE @ L2057, QEAGOL @ L1723 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 47 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 48 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 49 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 50 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 51 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 52 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 53 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 54 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 55 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 56 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 57 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 58 | up-find-remote, up-get-search-state | QADVANTAGE @ L2057, QEVAL @ L9821, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 59 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 60 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 61 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 62 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QECO NUMBERS @ L16922, QHOUSES @ L4383 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 63 | research, research-completed | QADVANTAGE @ L2057, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 64 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 65 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 66 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 67 | up-full-reset-search | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 68 | up-find-remote, up-set-target-point | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 69 | up-get-search-state, up-jump-rule | QADVANTAGE @ L2057, QLC @ L4474, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 70 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 71 | up-full-reset-search | QADVANTAGE @ L2057, QTARGET PLAYER @ L17945, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 72 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 73 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 74 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 75 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 76 | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | QNA @ L2534, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 77 | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | QNA @ L2534, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 78 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 79 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 80 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 81 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 82 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 83 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 84 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 85 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 86 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 87 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 88 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 89 | up-full-reset-search | QADVANTAGE @ L2057, QTARGET PLAYER @ L17945, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 90 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QADVANTAGE @ L2057, QSPEARS @ L8501, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 91 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 92 | build, up-find-remote, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 93 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 94 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 95 | up-get-search-state | QRAIDING @ L10481, QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 96 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 97 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 98 | up-find-remote, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 99 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 100 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 101 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 102 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 103 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 104 | up-find-remote, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 105 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 106 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 107 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 108 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 109 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 110 | up-find-remote, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 111 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 112 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 113 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 114 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 115 | up-find-remote, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 116 | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 117 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 118 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 119 | up-find-remote, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 120 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 121 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 122 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 123 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 124 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 125 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 126 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 127 | up-find-remote, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L2964, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 128 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 129 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 130 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 131 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 132 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666, QUICKIES @ L2964 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 133 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 134 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 135 | up-find-remote, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 136 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 137 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 138 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 139 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 140 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 141 | research, research-completed, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 142 | up-get-search-state | QRAIDING @ L10481, QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 143 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 144 | up-clean-search, up-set-target-point | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 145 | up-set-target-object | QHOUSES @ L4383, QTCR @ L12972, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 146 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 147 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 148 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 149 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | QBH @ L7174, QCLAIMING SHEEP @ L8087, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 150 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 151 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 152 | build, up-jump-rule | QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 153 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 154 | up-full-reset-search, up-set-target-point | QMISC @ L3246, QRAIDING @ L10481, QRANGED MICRO @ L12040 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 155 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 156 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 157 | up-clean-search, up-set-target-point | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 158 | up-set-target-object | QMISC @ L3246, QTCR @ L12972, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 159 | up-full-reset-search | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 160 | up-find-status-remote | QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 161 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 162 | up-clean-search, up-set-target-point | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 163 | up-clean-search, up-set-target-point | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 164 | up-set-target-object | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 165 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 166 | build, up-jump-rule | QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 167 | up-full-reset-search | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 168 | up-find-status-remote | QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 169 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 170 | up-clean-search, up-set-target-point | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 171 | up-set-target-object | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 172 | build, up-jump-rule | QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 173 | up-full-reset-search | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 174 | up-find-status-remote | QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 175 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 176 | up-clean-search, up-set-target-point | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 177 | up-set-target-object | QMISC @ L3246, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 178 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 179 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QMISC @ L3246, QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 180 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 181 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 182 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 183 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 184 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 185 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 186 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 187 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 188 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 189 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 190 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 191 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 192 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 193 | up-find-remote, up-get-search-state, up-remove-objects | QMISC @ L3246, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 194 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 195 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 196 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 197 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 198 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 199 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 200 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 201 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 202 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 203 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 204 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 205 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 206 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 207 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 208 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 209 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 210 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 211 | up-set-target-object | QMPOINTS @ L3751, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 212 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 213 | up-set-target-object | QMPOINTS @ L3751, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 214 | build | QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 215 | build, up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | QMINIS @ L4132, QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 216 | build, up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object | QMINIS @ L4132, QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 217 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 218 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 219 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 220 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 221 | build, up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 222 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 223 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 224 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 225 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 226 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 227 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 228 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 229 | up-jump-rule | QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 230 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 231 | up-jump-rule | QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 232 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 233 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 234 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 235 | build, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QCLAIMING SHEEP @ L8087, QMINIS @ L4132, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 236 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 237 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 238 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 239 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 240 | up-full-reset-search | QMINIS @ L4132, QSCOUT @ L9068, QSOD @ L9610 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 241 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 242 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 243 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 244 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 245 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 246 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 247 | build, disable-self, up-find-local, up-full-reset-search | QMINIS @ L4132 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 248 | build, up-set-target-object | QMINIS @ L4132 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 249 | build, up-clean-search, up-full-reset-search, up-set-target-object | QMINIS @ L4132, QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 250 | build, disable-self, up-find-local, up-full-reset-search | QMINIS @ L4132 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 251 | build, disable-self, up-clean-search, up-find-local, up-full-reset-search, up-set-target-object, up-set-target-point | QMINIS @ L4132 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 252 | build, disable-self, up-clean-search, up-full-reset-search, up-set-target-object, up-target-objects | QFORAGE @ L6715, QMINIS @ L4132 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 253 | build, research, research-pending, up-full-reset-search, up-research | QCUP @ L14868, QFLTCH @ L14973, QMINIS @ L4132 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 254 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 255 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 256 | up-full-reset-search, up-get-search-state | QADVANTAGE @ L2057, QHOUSES @ L4383, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 257 | up-set-target-object | QHOUSES @ L4383, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 258 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QHOUSES @ L4383, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 259 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | QADVANTAGE @ L2057, QECO NUMBERS @ L16922, QHOUSES @ L4383 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 260 | up-set-target-object, up-set-target-point, up-target-point | QCCR @ L12797, QHOUSES @ L4383, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 261 | up-full-reset-search, up-set-target-point | QHOUSES @ L4383, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 262 | up-get-search-state | QLC @ L4474, QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 263 | disable-self | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 264 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 265 | build, disable-self | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 266 | build | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 267 | build | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 268 | build | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 269 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 270 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 271 | up-full-reset-search, up-set-target-object, up-set-target-point | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 272 | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-object | QLC @ L4474, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 273 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 274 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 275 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 276 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 277 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 278 | up-full-reset-search, up-set-target-object | QHOUSES @ L4383, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 279 | up-full-reset-search, up-get-search-state, up-set-target-point | QCLAIMING SHEEP @ L8087, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 280 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 281 | build, up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 282 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 283 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 284 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 285 | up-full-reset-search, up-get-search-state, up-set-target-point | QCLAIMING SHEEP @ L8087, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 286 | up-clean-search, up-remove-objects, up-set-target-object | QCLAIMING SHEEP @ L8087, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 287 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 288 | build | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 289 | build, up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 290 | build | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 291 | build, up-find-local, up-full-reset-search, up-set-target-object, up-target-point | QLC @ L4474, QNEWSCOUTING @ L5828, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 292 | build, up-build | QLC @ L4474, QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 293 | — | QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 294 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 295 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 296 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 297 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 298 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 299 | up-target-objects | QANTI-TRUSH @ L4799, QBH @ L7174, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 300 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 301 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 302 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QGARRISONING TC @ L4863, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 303 | up-jump-rule, up-set-target-object | QGARRISONING TC @ L4863, QHOUSES @ L4383, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 304 | up-jump-rule | QADVANTAGE @ L2057, QGARRISONING TC @ L4863, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 305 | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects | QGARRISONING TC @ L4863, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 306 | up-remove-objects | QGARRISONING TC @ L4863, QINITIALIZING GROUP @ L12236, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 307 | up-get-search-state | QLC @ L4474, QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 308 | up-target-objects | QANTI-TRUSH @ L4799, QBH @ L7174, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 309 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QCLAIMING SHEEP @ L8087, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 310 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 311 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 312 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 313 | up-set-target-point | QFARMS @ L8222, QRAIDING @ L10481, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 314 | up-find-remote, up-full-reset-search, up-get-search-state | QADVANTAGE @ L2057, QRAIDING @ L10481, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 315 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 316 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 317 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 318 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 319 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 320 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QMINIS @ L4132, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 321 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 322 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 323 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 324 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 325 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 326 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 327 | up-clean-search, up-find-remote, up-remove-objects, up-set-target-point, up-target-objects | QFORAGE @ L6715, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 328 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 329 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 330 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 331 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 332 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 333 | up-find-remote, up-full-reset-search, up-set-target-point | QEVAL @ L9821, QSCOUT @ L9068, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 334 | up-get-search-state, up-set-target-object | QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 335 | up-get-search-state, up-jump-rule, up-remove-objects | QRANGED MICRO @ L12040, QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 336 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 337 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 338 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 339 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 340 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 341 | up-find-local, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | QCLAIMING SHEEP @ L8087, QHOUSES @ L4383, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 342 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QCLAIMING SHEEP @ L8087, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 343 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 344 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 345 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 346 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 347 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 348 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 349 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 350 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 351 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 352 | up-set-target-object | QHOUSES @ L4383, QUICKIES @ L3042, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 353 | up-clean-search, up-find-remote, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QUICKIES @ L2964, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 354 | up-clean-search, up-remove-objects, up-set-target-point, up-target-objects | QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 355 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 356 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 357 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 358 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 359 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 360 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 361 | up-clean-search, up-remove-objects, up-target-objects | QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 362 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 363 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 364 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 365 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 366 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 367 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 368 | up-clean-search, up-remove-objects, up-target-objects | QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 369 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 370 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 371 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 372 | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | QRETARGETING @ L7684, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 373 | up-set-target-object, up-target-objects | QBH @ L7174, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 374 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 375 | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects, up-set-target-point | QDLURING @ L6795, QTARGET STUFF @ L2666, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 376 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 377 | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point, up-target-objects | QHOUSES @ L4383, QRAIDING @ L10481, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 378 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 379 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 380 | up-clean-search, up-find-local, up-full-reset-search, up-set-target-object | QADVANTAGE @ L2057, QEAGOL @ L1723, QSHEEP @ L5685 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 381 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 382 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 383 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 384 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 385 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 386 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 387 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 388 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 389 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 390 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 391 | up-jump-rule | QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 392 | disable-self | QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 393 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 394 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 395 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 396 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 397 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 398 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 399 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 400 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 401 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 402 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 403 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 404 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 405 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 406 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 407 | — | QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 408 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 409 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 410 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 411 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 412 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 413 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 414 | enable-timer | QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 415 | enable-timer | QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 416 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 417 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 418 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 419 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 420 | up-full-reset-search, up-target-point | QEVAL @ L9821, QNEWSCOUTING @ L5828, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 421 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 422 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 423 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 424 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 425 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 426 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 427 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 428 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 429 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 430 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 431 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 432 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 433 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 434 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 435 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 436 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 437 | up-find-local, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point, up-target-point | QCIRCLE SCOUTING @ L6406, QLC @ L4474, QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 438 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 439 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 440 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 441 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 442 | up-jump-rule | QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 443 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 444 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 445 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 446 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 447 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 448 | build, up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 449 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 450 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 451 | up-clean-search, up-find-local, up-find-remote, up-set-target-object, up-target-point | QCIRCLE SCOUTING @ L6406, QLC @ L4474, QNEWSCOUTING @ L5828 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 452 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 453 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 454 | disable-self, up-find-remote, up-full-reset-search, up-set-target-object | QCIRCLE SCOUTING @ L6406, QCLAIMING SHEEP @ L8087 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 455 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 456 | disable-self, up-find-remote, up-full-reset-search, up-set-target-object | QCIRCLE SCOUTING @ L6406, QCLAIMING SHEEP @ L8087 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 457 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 458 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 459 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 460 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 461 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 462 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 463 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 464 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 465 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 466 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 467 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 468 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 469 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 470 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 471 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 472 | build, up-find-local, up-full-reset-search, up-set-target-object | QEAGOL @ L1723, QFORAGE @ L6715, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 473 | build, up-full-reset-search | QFORAGE @ L6715, QLC @ L4474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 474 | build, up-clean-search, up-find-local, up-get-search-state, up-remove-objects, up-set-target-point | QCLAIMING SHEEP @ L8087, QFORAGE @ L6715, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 475 | up-clean-search, up-find-remote, up-remove-objects, up-target-objects | QBH @ L7174, QDLURING @ L6795, QFORAGE @ L6715 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 476 | disable-self | QCOUNTING SHEEP @ L6767 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 477 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 478 | build | QCOUNTING SHEEP @ L6767 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 479 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 480 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 481 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 482 | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QDLURING @ L6795, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 483 | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | QBH @ L7174, QDLURING @ L6795 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 484 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 485 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 486 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 487 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QDLURING @ L6795 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 488 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 489 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 490 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 491 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 492 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 493 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 494 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 495 | up-full-reset-search, up-set-target-point | QDLURING @ L6795, QMISC @ L3246, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 496 | up-full-reset-search | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 497 | research, research-pending, up-research | QADVANTAGE @ L2057, QDLURING @ L6795 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 498 | up-clean-search, up-find-local, up-find-remote, up-remove-objects, up-target-objects | QDLURING @ L6795, QFORAGE @ L6715 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 499 | build, enable-timer, up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-remove-objects, up-target-objects | QDLURING @ L6795, QFORAGE @ L6715 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 500 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 501 | research, research-pending, unit-type-count-total, up-research | QDLURING @ L6795, QSKIRMS @ L15472 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 502 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 503 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 504 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 505 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 506 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 507 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 508 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 509 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 510 | disable-self | QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 511 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 512 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QBH @ L7174, QCLAIMING SHEEP @ L8087, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 513 | unit-type-count-total, up-jump-rule | QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 514 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 515 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 516 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 517 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 518 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 519 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 520 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 521 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 522 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 523 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 524 | research, research-completed | QBH @ L7174, QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 525 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 526 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 527 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 528 | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | QBH @ L7174, QRETARGETING @ L7684, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 529 | up-target-objects | QANTI-TRUSH @ L4799, QBH @ L7174, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 530 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 531 | up-clean-search, up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-object, up-set-target-point | QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 532 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 533 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 534 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 535 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 536 | up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-object, up-set-target-point | QBH @ L7174, QSPEARS @ L8501, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 537 | disable-self | QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 538 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 539 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | QBH @ L7174, QMISC @ L3246, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 540 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 541 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 542 | build, research, up-find-local, up-full-reset-search, up-remove-objects, up-research, up-set-target-point | QBH @ L7174, QPIKES @ L14784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 543 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 544 | up-clean-search, up-remove-objects, up-set-target-object, up-target-objects | QBH @ L7174, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 545 | build, research, research-completed, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | QBH @ L7174, QTARGET STUFF @ L2666, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 546 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 547 | up-clean-search, up-remove-objects, up-set-target-object, up-target-objects | QBH @ L7174, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 548 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 549 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 550 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 551 | up-find-remote, up-remove-objects, up-target-objects | QBH @ L7174, QDLURING @ L6795, QFORAGE @ L6715 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 552 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 553 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 554 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 555 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 556 | up-find-local, up-full-reset-search | QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 557 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 558 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 559 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 560 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 561 | research, research-completed | QADVANTAGE @ L2057, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 562 | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | QRETARGETING @ L7684, QSKIRMS @ L8338 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 563 | up-remove-objects | QGARRISONING TC @ L4863, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 564 | build, up-remove-objects, up-target-objects | QRETARGETING @ L7684, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 565 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 566 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | QBH @ L7174, QMISC @ L3246, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 567 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 568 | — | QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 569 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 570 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 571 | research, research-completed | QADVANTAGE @ L2057, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 572 | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | QRETARGETING @ L7684, QSKIRMS @ L8338 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 573 | up-remove-objects | QGARRISONING TC @ L4863, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 574 | build, up-remove-objects, up-target-objects | QRETARGETING @ L7684, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 575 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 576 | up-clean-search, up-find-remote, up-full-reset-search, up-set-target-object, up-set-target-point | QBH @ L7174, QMPOINTS @ L3751, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 577 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 578 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 579 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 580 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 581 | build, building-type-count-total | QFORCEDROP @ L7949, QMONASTERY @ L16168, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 582 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 583 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 584 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 585 | research, research-pending, up-research | QADVANTAGE @ L2057, QDLURING @ L6795, QFORCEDROP @ L7949 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 586 | — | QFORCEDROP @ L7949 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 587 | — | QFORCEDROP @ L7949 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 588 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 589 | research | QFORCEDROP @ L7949, QLOOM @ L15175 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 590 | research | QFORCEDROP @ L7949, QLOOM @ L15175 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 591 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 592 | train | QFORCEDROP @ L7949, QKNIGHTS @ L15409, QSCOUTS @ L15395 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 593 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 594 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QCLAIMING SHEEP @ L8087, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 595 | up-clean-search, up-set-target-object | QARCHERS @ L8267, QCLAIMING SHEEP @ L8087, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 596 | build, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QCLAIMING SHEEP @ L8087, QMISC @ L3246, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 597 | up-clean-search, up-remove-objects, up-target-point | QCLAIMING SHEEP @ L8087, QEVAL @ L9821, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 598 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 599 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 600 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 601 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 602 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QCLAIMING SHEEP @ L8087, QGARRISONING TC @ L4863 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 603 | up-clean-search, up-find-local, up-find-remote, up-full-reset-search, up-set-target-object | QCIRCLE SCOUTING @ L6406, QCLAIMING SHEEP @ L8087, QMPOINTS @ L3751 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 604 | enable-timer, up-target-point | QCLAIMING SHEEP @ L8087, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 605 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 606 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 607 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 608 | up-set-target-point | QFARMS @ L8222, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 609 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 610 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 611 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 612 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QARCHERS @ L8267, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 613 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 614 | up-clean-search, up-set-target-object | QARCHERS @ L8267, QRAIDING @ L10481, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 615 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 616 | disable-self | QSKIRMS @ L8338 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 617 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 618 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 619 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 620 | up-clean-search, up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point | QBH @ L7174, QSKIRMS @ L8338 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 621 | up-get-search-state, up-remove-objects, up-target-point | QEVAL @ L9821, QRAIDING @ L10481, QSKIRMS @ L8338 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 622 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 623 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 624 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 625 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 626 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 627 | up-remove-objects | QDEFENSE @ L8405, QGARRISONING TC @ L4863, QINITIALIZING GROUP @ L12236 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 628 | up-remove-objects, up-set-target-point | QDEFENSE @ L8405, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 629 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 630 | up-find-local, up-full-reset-search, up-set-target-point | QRAIDING @ L10481, QREGROUPING @ L12317, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 631 | up-set-target-object | QHOUSES @ L4383, QSPEARS @ L8501, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 632 | up-get-search-state, up-jump-rule, up-remove-objects | QKNIGHT GROUP @ L9765, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 633 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 634 | up-find-local, up-full-reset-search, up-target-point | QLC @ L4474, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 635 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 636 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 637 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 638 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 639 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 640 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 641 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 642 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 643 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 644 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 645 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QEVAL @ L9821, QSPEARS @ L8501, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 646 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 647 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QEVAL @ L9821, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 648 | up-find-remote, up-get-search-state, up-set-target-point | QEVAL @ L9821, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 649 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 650 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 651 | up-find-status-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 652 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 653 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 654 | up-find-status-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QDLURING @ L6795, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 655 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 656 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 657 | up-find-status-remote | QMISC @ L3246, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 658 | up-jump-rule | QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 659 | up-clean-search, up-remove-objects, up-set-target-point | QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 660 | up-set-target-object | QHOUSES @ L4383, QSPEARS @ L8501, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 661 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 662 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 663 | up-find-remote | QSCOUT @ L9068, QSPEARS @ L8501, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 664 | up-jump-rule | QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 665 | up-set-target-point | QFARMS @ L8222, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 666 | up-find-local, up-remove-objects, up-set-target-point, up-target-objects, up-target-point | QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 667 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 668 | up-find-remote, up-set-target-point | QSPEARS @ L8501, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 669 | up-jump-rule | QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 670 | up-clean-search, up-find-remote, up-remove-objects, up-set-target-object, up-set-target-point | QBH @ L7174, QSPEARS @ L8501, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 671 | up-find-local, up-remove-objects, up-set-target-point, up-target-objects, up-target-point | QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 672 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 673 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 674 | up-remove-objects, up-set-target-point | QRAIDING @ L10481, QREGROUPING @ L12317, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 675 | up-clean-search, up-remove-objects, up-set-target-point | QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 676 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 677 | up-target-point | QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 678 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 679 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 680 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 681 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 682 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 683 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 684 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 685 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 686 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 687 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 688 | build, up-jump-rule | QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 689 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 690 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 691 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 692 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 693 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 694 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QEVAL @ L9821, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 695 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 696 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 697 | up-find-remote, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 698 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 699 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 700 | up-find-remote, up-full-reset-search, up-set-target-point | QSCOUT @ L9068, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 701 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 702 | up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects | QEVAL @ L9821, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 703 | up-jump-rule | QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 704 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 705 | up-full-reset-search | QADVANTAGE @ L2057, QMINIS @ L4132, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 706 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 707 | up-find-remote | QSCOUT @ L9068, QSPEARS @ L8501, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 708 | up-jump-rule | QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 709 | up-clean-search, up-set-target-object | QARCHERS @ L8267, QCLAIMING SHEEP @ L8087, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 710 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 711 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 712 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 713 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 714 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 715 | build, up-find-remote, up-remove-objects | QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 716 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 717 | up-clean-search, up-find-remote, up-get-search-state, up-remove-objects | QDLURING @ L6795, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 718 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 719 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 720 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 721 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 722 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 723 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 724 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 725 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 726 | up-find-local, up-full-reset-search, up-set-target-object | QADVANTAGE @ L2057, QEAGOL @ L1723 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 727 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 728 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 729 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 730 | disable-timer | QCLAIMING SHEEP @ L8087, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 731 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 732 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 733 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 734 | — | QSOD @ L9610 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 735 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 736 | build | QSOD @ L9610 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 737 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 738 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 739 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 740 | up-set-target-object | QMISC @ L3246, QSOD @ L9610, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 741 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246, QSOD @ L9610 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 742 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 743 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 744 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 745 | up-full-reset-search | QADVANTAGE @ L2057, QMARCH TO ENEMY BASE @ L13231, QSOD @ L9610 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 746 | up-full-reset-search | QADVANTAGE @ L2057, QMINIS @ L4132, QSOD @ L9610 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 747 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 748 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | QKNIGHT GROUP @ L9765, QMISC @ L3246, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 749 | up-set-target-object | QHOUSES @ L4383, QSPEARS @ L8501, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 750 | up-get-search-state, up-jump-rule, up-remove-objects | QKNIGHT GROUP @ L9765, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 751 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 752 | build, up-find-remote, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QEVAL @ L9821, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 753 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QGARRISONING TC @ L4863, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 754 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 755 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 756 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 757 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 758 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 759 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 760 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 761 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QSCOUT @ L9068, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 762 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 763 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 764 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 765 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 766 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 767 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 768 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 769 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 770 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 771 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 772 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 773 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 774 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 775 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 776 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 777 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 778 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 779 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 780 | research, research-completed | QEVAL @ L9821, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 781 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 782 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 783 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 784 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 785 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 786 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 787 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 788 | research, research-completed | QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 789 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 790 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 791 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 792 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 793 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 794 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 795 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 796 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 797 | up-remove-objects, up-target-point | QEVAL @ L9821, QRAIDING @ L10481, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 798 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 799 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 800 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 801 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 802 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 803 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 804 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 805 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 806 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 807 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 808 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 809 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 810 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 811 | up-full-reset-search, up-target-point | QEVAL @ L9821, QNEWSCOUTING @ L5828, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 812 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 813 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 814 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 815 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 816 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 817 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 818 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 819 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 820 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 821 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 822 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 823 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 824 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 825 | up-remove-objects, up-set-target-point | QRAIDING @ L10481, QREGROUPING @ L12317, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 826 | up-remove-objects, up-target-point | QEVAL @ L9821, QRAIDING @ L10481, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 827 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 828 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 829 | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-point | QRAIDING @ L10481, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 830 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 831 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QGARRISONING TC @ L4863, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 832 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 833 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 834 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 835 | build, up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 836 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 837 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 838 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 839 | up-clean-search, up-set-target-object | QARCHERS @ L8267, QCLAIMING SHEEP @ L8087, QSCOUT @ L9068 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 840 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 841 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 842 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 843 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 844 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 845 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 846 | up-remove-objects, up-set-target-point | QDEFENSE @ L8405, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 847 | up-get-search-state | QRAIDING @ L10481, QTARGET STUFF @ L2666, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 848 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 849 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 850 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 851 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 852 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 853 | up-jump-rule, up-set-target-object | QRAIDING @ L10481, QTCR @ L12972, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 854 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 855 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 856 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 857 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 858 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 859 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 860 | up-clean-search, up-full-reset-search, up-remove-objects, up-set-target-object | QNA @ L2534, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 861 | up-clean-search, up-full-reset-search | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 862 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 863 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 864 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 865 | — | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 866 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 867 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 868 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 869 | up-target-point | QEVAL @ L9821, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 870 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 871 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 872 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 873 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 874 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 875 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 876 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 877 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 878 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 879 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 880 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 881 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 882 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 883 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 884 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 885 | up-full-reset-search, up-set-target-point | QMISC @ L3246, QRAIDING @ L10481, QRANGED MICRO @ L12040 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 886 | up-find-remote, up-get-search-state | QADVANTAGE @ L2057, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 887 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 888 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 889 | up-set-target-point | QFARMS @ L8222, QRAIDING @ L10481, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 890 | up-find-remote, up-full-reset-search, up-get-search-state | QEVAL @ L9821, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 891 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 892 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 893 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 894 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 895 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 896 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 897 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 898 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 899 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 900 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 901 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 902 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 903 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 904 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 905 | up-clean-search, up-find-status-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 906 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 907 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 908 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 909 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 910 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 911 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 912 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 913 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 914 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 915 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 916 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 917 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 918 | up-full-reset-search | QADVANTAGE @ L2057, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 919 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 920 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 921 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 922 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 923 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 924 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 925 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 926 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 927 | up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects | QKNIGHT GROUP @ L9765, QMISC @ L3246, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 928 | up-set-target-object | QHOUSES @ L4383, QSPEARS @ L8501, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 929 | up-get-search-state, up-jump-rule, up-remove-objects | QKNIGHT GROUP @ L9765, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 930 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 931 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 932 | disable-self, enable-timer | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 933 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 934 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 935 | up-set-target-point | QFARMS @ L8222, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 936 | up-find-remote, up-get-search-state | QCLAIMING SHEEP @ L8087, QGARRISONING TC @ L4863, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 937 | up-remove-objects | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 938 | up-remove-objects | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 939 | up-remove-objects | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 940 | up-clean-search, up-set-target-object, up-set-target-point | QARCHERS @ L8267, QRAIDING @ L10481, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 941 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 942 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 943 | enable-timer | QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 944 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 945 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 946 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 947 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 948 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 949 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 950 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 951 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246, QRAIDING @ L10481 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 952 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 953 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 954 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 955 | disable-timer, up-find-local, up-full-reset-search, up-target-point | QLC @ L4474, QRAIDING @ L10481, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 956 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 957 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 958 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 959 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 960 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 961 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 962 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 963 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 964 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 965 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 966 | up-full-reset-search, up-set-target-point | QMISC @ L3246, QRAIDING @ L10481, QRANGED MICRO @ L12040 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 967 | up-find-remote, up-get-search-state | QADVANTAGE @ L2057, QRAIDING @ L10481, QRANGED MICRO @ L12040 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 968 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 969 | up-set-target-object | QHOUSES @ L4383, QSPEARS @ L8501, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 970 | up-get-search-state, up-jump-rule, up-remove-objects | QRANGED MICRO @ L12040, QSPEARS @ L8501, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 971 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 972 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 973 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 974 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 975 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 976 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 977 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 978 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 979 | research, research-completed | QDAMAGE POTENTIAL @ L19299, QRANGED MICRO @ L12040 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 980 | research, research-completed, up-research | QBH @ L7174, QCHAINMAIL @ L14326, QINITIALIZING GROUP @ L12236 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 981 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 982 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 983 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 984 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 985 | up-find-local | QCCR @ L12797, QINITIALIZING GROUP @ L12236, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 986 | up-remove-objects | QGARRISONING TC @ L4863, QINITIALIZING GROUP @ L12236, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 987 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 988 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 989 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 990 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 991 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 992 | up-find-local | QCCR @ L12797, QINITIALIZING GROUP @ L12236, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 993 | up-remove-objects, up-set-target-point | QRAIDING @ L10481, QREGROUPING @ L12317, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 994 | up-remove-objects, up-target-point | QEVAL @ L9821, QRAIDING @ L10481, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 995 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 996 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 997 | up-find-local, up-full-reset-search, up-set-target-point | QREGROUPING @ L12317, QSPEARS @ L8501 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 998 | up-set-target-object, up-target-point | QCCR @ L12797, QREGROUPING @ L12317, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 999 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1000 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1001 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1002 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1003 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1004 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1005 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1006 | research, research-pending, up-research | QADVANTAGE @ L2057, QMOVING @ L12474, QSKIRMS @ L15472 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1007 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1008 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1009 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1010 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1011 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1012 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1013 | — | QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1014 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1015 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1016 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1017 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1018 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1019 | research, research-completed | QEVAL @ L9821, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1020 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1021 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1022 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1023 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1024 | — | QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1025 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1026 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1027 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1028 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1029 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1030 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1031 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1032 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1033 | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | QCCR @ L12797, QHOUSES @ L4383, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1034 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1035 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1036 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1037 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1038 | up-find-local | QCCR @ L12797, QINITIALIZING GROUP @ L12236, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1039 | research, research-completed, up-find-local | QCCR @ L12797, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1040 | research, research-completed, up-find-local | QCCR @ L12797, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1041 | research, up-find-local | QCCR @ L12797 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1042 | up-find-local | QCCR @ L12797, QINITIALIZING GROUP @ L12236, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1043 | up-clean-search, up-get-search-state, up-remove-objects | QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1044 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1045 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1046 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1047 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1048 | up-set-target-object, up-target-point | QCCR @ L12797, QREGROUPING @ L12317, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1049 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1050 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1051 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1052 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1053 | up-clean-search, up-find-local, up-full-reset-search, up-get-search-state, up-remove-objects, up-set-target-object, up-set-target-point | QCCR @ L12797, QHOUSES @ L4383, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1054 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1055 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1056 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1057 | up-set-target-object | QHOUSES @ L4383, QTCR @ L12972, QUICKIES @ L3042 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1058 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1059 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1060 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1061 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1062 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1063 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1064 | up-find-local | QCCR @ L12797, QINITIALIZING GROUP @ L12236, QREGROUPING @ L12317 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1065 | research, research-completed, up-find-local | QCCR @ L12797, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1066 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1067 | research, up-find-local, up-research | QCCR @ L12797, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1068 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1069 | up-find-local | QCCR @ L12797, QINITIALIZING GROUP @ L12236, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1070 | research, research-completed, up-find-local, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1071 | up-clean-search, up-get-search-state, up-remove-objects, up-set-target-point | QTARGET STUFF @ L2666, QTCR @ L12972, QVILLS @ L4970 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1072 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1073 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1074 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1075 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1076 | up-set-target-object, up-target-point | QCCR @ L12797, QREGROUPING @ L12317, QTCR @ L12972 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1077 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1078 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1079 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1080 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1081 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1082 | research, research-completed | QMARCH TO ENEMY BASE @ L13231 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1083 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1084 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1085 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1086 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1087 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1088 | — | QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1089 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1090 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1091 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1092 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1093 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1094 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1095 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1096 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1097 | research, research-completed | QMARCH TO ENEMY BASE @ L13231 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1098 | research, research-completed | QMARCH TO ENEMY BASE @ L13231 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1099 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QRETARGETING @ L7684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1100 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1101 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1102 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1103 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1104 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1105 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1106 | up-full-reset-search | QMARCH TO ENEMY BASE @ L13231, QSOD @ L9610, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1107 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1108 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1109 | disable-self | QMARCH TO ENEMY BASE @ L13231 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1110 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1111 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1112 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1113 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1114 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1115 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1116 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1117 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1118 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1119 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1120 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1121 | research, research-completed | QEVAL @ L9821, QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1122 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1123 | research, research-completed | QMARCH TO ENEMY BASE @ L13231, QMOVING @ L12474 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1124 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1125 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1126 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1127 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1128 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1129 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1130 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1131 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1132 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1133 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1134 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1135 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1136 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1137 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1138 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1139 | — | QCOMBAT MODE @ L13707 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1140 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1141 | research, research-pending, unit-type-count-total, up-research | QCUP @ L14868, QDLURING @ L6795, QFAILSAFE @ L13810 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1142 | disable-self | QDARK @ L13824, QFLUSH @ L13980 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1143 | disable-self | QDARK @ L13824 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1144 | disable-self | QDARK @ L13824, QFLUSH @ L13980 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1145 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1146 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1147 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1148 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1149 | research, research-pending, up-research | QFLUSH @ L13980, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1150 | research, research-pending, up-research | QFLUSH @ L13980, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1151 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1152 | build, building-type-count-total | QFLUSH @ L13980, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1153 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1154 | disable-self | QFLUSH @ L13980 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1155 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1156 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1157 | disable-self | QFLUSH @ L13980, QSIEGE @ L14178 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1158 | disable-self | QFLUSH @ L13980, QKNIGHTS @ L14113, QSIEGE @ L14178 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1159 | build, building-type-count-total, disable-self | QFLUSH @ L13980, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1160 | disable-self, research, research-pending, up-research | QFLUSH @ L13980, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1161 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1162 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1163 | build, building-type-count-total | QFLUSH @ L13980, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1164 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1165 | build, disable-self | QFLUSH @ L13980, QKNIGHTS @ L14113 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1166 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1167 | build, disable-self | QFLUSH @ L13980, QKNIGHTS @ L14113 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1168 | disable-self | QFLUSH @ L13980, QKNIGHTS @ L14113, QSIEGE @ L14178 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1169 | disable-self | QFLUSH @ L13980, QSIEGE @ L14178 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1170 | disable-self | QFLUSH @ L13980, QKNIGHTS @ L14113, QSIEGE @ L14178 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1171 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1172 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1173 | up-modify-escrow | QCHAINMAIL @ L14326, QMARKET @ L16231, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1174 | can-research-with-escrow, research, set-escrow-percentage, up-research | QCHAINMAIL @ L14326, QPIKES @ L14784, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1175 | build, research, research-completed, research-pending, up-research | QCHAINMAIL @ L14326, QRAX @ L20476, QXBOW @ L14762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1176 | up-modify-escrow | QCHAINMAIL @ L14326, QMARKET @ L16231, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1177 | can-research-with-escrow, research, set-escrow-percentage, up-research | QCHAINMAIL @ L14326, QPIKES @ L14784, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1178 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1179 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1180 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1181 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1182 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1183 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1184 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1185 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1186 | build, release-escrow, set-escrow-percentage, up-modify-escrow | QIRONCASTING @ L14362, QPAA @ L15072 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1187 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1188 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1189 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1190 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1191 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1192 | build, research, research-pending, up-research | QCUP @ L14868, QFORGING @ L14459 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1193 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1194 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1195 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1196 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1197 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1198 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1199 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1200 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1201 | build, set-escrow-percentage | QBODKIN @ L15121, QCHAINBARDING @ L14559, QSCALEBARDING @ L14658 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1202 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1203 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1204 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1205 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1206 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1207 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1208 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1209 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1210 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1211 | build, set-escrow-percentage | QBODKIN @ L15121, QCHAINBARDING @ L14559, QSCALEBARDING @ L14658 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1212 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1213 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1214 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1215 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1216 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1217 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1218 | build, research, research-pending, unit-type-count-total, up-research | QDLURING @ L6795, QFAILSAFE @ L13810, QXBOW @ L14762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1219 | research, up-research | QCHAINMAIL @ L14326, QSCALEMAIL @ L14293, QXBOW @ L14762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1220 | build, research, research-pending, up-research | QCUP @ L14868, QPIKES @ L14784, QSKIRMS @ L15472 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1221 | set-escrow-percentage | QCHAINBARDING @ L14559, QPIKES @ L14784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1222 | can-research-with-escrow, research, set-escrow-percentage | QCHAINMAIL @ L14326, QPIKES @ L14784, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1223 | research, unit-type-count-total | QAGE @ L14823 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1224 | research, unit-type-count-total | QAGE @ L14823 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1225 | research, unit-type-count-total | QAGE @ L14823 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1226 | research, unit-type-count-total | QAGE @ L14823 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1227 | research, research-pending, unit-type-count-total, up-research | QCUP @ L14868, QDLURING @ L6795, QFAILSAFE @ L13810 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1228 | build, research | QAGE @ L14823, QCUP @ L14868, QLOOM @ L15175 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1229 | build, can-research-with-escrow, research | QCUP @ L14868, QGOLDMINING @ L19649, QPAA @ L15072 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1230 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1231 | build, research, research-pending, up-research | QCUP @ L14868, QFORGING @ L14459 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1232 | build, research, research-pending, up-research | QCUP @ L14868, QFORGING @ L14459 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1233 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1234 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1235 | build, research | QBECO @ L17393, QCUP @ L14868 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1236 | build, can-research-with-escrow, release-escrow, research, set-escrow-percentage | QFLTCH @ L14973, QGOLDSHAFT @ L19736, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1237 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1238 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1239 | build, up-modify-escrow | QBODKIN @ L15121, QFLTCH @ L14973, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1240 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1241 | build, can-research-with-escrow, research, up-research | QBODKIN @ L15121, QGOLDSHAFT @ L19736, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1242 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1243 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1244 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1245 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1246 | build, can-research-with-escrow, research | QCUP @ L14868, QGOLDMINING @ L19649, QPAA @ L15072 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1247 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1248 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1249 | build, release-escrow, research, set-escrow-percentage, up-modify-escrow, up-research | QCUP @ L14868, QIRONCASTING @ L14362, QPAA @ L15072 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1250 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1251 | build, can-research-with-escrow, research, up-research | QBODKIN @ L15121, QGOLDSHAFT @ L19736, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1252 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1253 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1254 | build, set-escrow-percentage | QBODKIN @ L15121, QCHAINBARDING @ L14559, QSCALEBARDING @ L14658 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1255 | build, up-modify-escrow | QBODKIN @ L15121, QFLTCH @ L14973, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1256 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1257 | research | QAGE @ L14823, QLOOM @ L15175 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1258 | research | QLOOM @ L15175 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1259 | disable-self, train, unit-type-count-total | QMONKS @ L15201 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1260 | disable-self, train, unit-type-count-total | QMONKS @ L15201 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1261 | disable-self, train, unit-type-count-total | QMONKS @ L15201 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1262 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMANGOS @ L15229, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1263 | can-train-with-escrow, train | QMANGOS @ L15229, QRAMS @ L15336 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1264 | train, unit-type-count-total | QMANGOS @ L15229, QSCORPS @ L15320, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1265 | can-train-with-escrow, train, up-train | QKNIGHTS @ L15409, QMANGOS @ L15229, QRAMS @ L15336 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1266 | release-escrow, set-escrow-percentage, unit-type-count-total | QBOWSAW @ L19549, QESCROW @ L19996, QMANGOS @ L15229 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1267 | up-modify-escrow | QMANGOS @ L15229, QRAMS @ L15336, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1268 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1269 | build, unit-type-count-total | QMANGOS @ L15229, QRAMS @ L15336 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1270 | train, unit-type-count-total | QMANGOS @ L15229, QSCORPS @ L15320, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1271 | build, unit-type-count-total | QRAMS @ L15336 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1272 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1273 | up-modify-escrow | QMANGOS @ L15229, QRAMS @ L15336, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1274 | can-train-with-escrow, train | QMANGOS @ L15229, QRAMS @ L15336 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1275 | build, unit-type-count-total | QMANGOS @ L15229, QRAMS @ L15336 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1276 | train | QFORCEDROP @ L7949, QKNIGHTS @ L15409, QSCOUTS @ L15395 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1277 | train | QFORCEDROP @ L7949, QKNIGHTS @ L15409, QSCOUTS @ L15395 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1278 | build, train | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1279 | build, can-train-with-escrow, train, up-train | QKNIGHTS @ L15409, QMANGOS @ L15229 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1280 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1281 | research, research-completed, research-pending, train, unit-type-count-total, up-research, up-train | QARCHERS @ L15445, QCHAINMAIL @ L14326, QXBOW @ L14762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1282 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1283 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1284 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1285 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1286 | research, research-pending, up-research | QDLURING @ L6795, QPIKES @ L14784, QSKIRMS @ L15472 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1287 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1288 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1289 | research, research-completed, train, unit-type-count-total | QMILITIAMAN @ L15549, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1290 | research, research-completed, train, unit-type-count-total | QAGE @ L14823, QMILITIAMAN @ L15549, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1291 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1292 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1293 | build, train, unit-type-count-total | QMANGOS @ L15229, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1294 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1295 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1296 | build, train, unit-type-count-total, up-train | QSPEARS @ L15564, QVILLAGERS @ L19918 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1297 | train, unit-type-count-total | QMANGOS @ L15229, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1298 | train, unit-type-count-total | QMANGOS @ L15229, QSPEARS @ L15564 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1299 | build, building-type-count-total, up-jump-rule | QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1300 | build, up-assign-builders | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1301 | build, up-assign-builders | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1302 | build, up-build | QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1303 | build, up-build | QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1304 | build, up-build | QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1305 | build, up-build | QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1306 | build, up-build | QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1307 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1308 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1309 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1310 | build, can-build-with-escrow, up-build | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1311 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1312 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1313 | build, release-escrow, set-escrow-percentage | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1314 | build, building-type-count-total | QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1315 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1316 | build, can-build-with-escrow, up-build | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1317 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1318 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1319 | build, release-escrow, set-escrow-percentage | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1320 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1321 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1322 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1323 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1324 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1325 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1326 | build, can-build-with-escrow | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1327 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1328 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1329 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1330 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1331 | build, can-build-with-escrow | QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1332 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1333 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1334 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1335 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1336 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1337 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1338 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1339 | build, can-build-with-escrow | QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1340 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1341 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1342 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1343 | build, building-type-count-total | QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1344 | build, can-build-with-escrow | QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1345 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1346 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1347 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1348 | build, building-type-count-total | QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1349 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1350 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1351 | build, can-build-with-escrow, up-build | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1352 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1353 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1354 | build, release-escrow, set-escrow-percentage | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1355 | build, building-type-count-total | QFORCEDROP @ L7949, QMONASTERY @ L16168, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1356 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1357 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1358 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1359 | build, can-build-with-escrow | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1360 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1361 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1362 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1363 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1364 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1365 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1366 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1367 | build, can-build-with-escrow | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1368 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1369 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1370 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1371 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1372 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1373 | build, building-type-count-total | QFARMS @ L20800, QMARKET @ L16231 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1374 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1375 | build, building-type-count-total, research | QMARKET @ L16231, QRAX @ L20476 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1376 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1377 | up-modify-escrow | QCHAINMAIL @ L14326, QMARKET @ L16231, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1378 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1379 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1380 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1381 | build, building-type-count-total, can-build-with-escrow, disable-timer, up-assign-builders, up-build | QMARKET @ L16231, QMONASTERY @ L16168, QUNIVERSITY @ L22097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1382 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1383 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1384 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QANALYZING ENEMY ATTACK @ L16478, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1385 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QANALYZING ENEMY ATTACK @ L16478, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1386 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1387 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1388 | build, building-type-count-total, disable-self, enable-timer | QRESIGNING @ L16527 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1389 | disable-self | QRESIGNING @ L16527 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1390 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1391 | — | QRESIGNING @ L16527 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1392 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1393 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1394 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1395 | disable-self | QRESIGNING @ L16527 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1396 | build | QCIVSUP @ L16624, QSUPERIORITY @ L16613 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1397 | build | QCIVSUP @ L16624, QSUPERIORITY @ L16613 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1398 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1399 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1400 | build | QTSA @ L16636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1401 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1402 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1403 | up-find-local, up-full-reset-search, up-remove-objects, up-set-target-point, up-target-point | QNEWSCOUTING @ L5828, QSPEARS @ L8501, QTSA @ L16636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1404 | disable-self | QENEMY STRAT @ L16728 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1405 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1406 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1407 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1408 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1409 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1410 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1411 | build, disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1412 | disable-self, research, research-completed | QCHAT @ L16797, QSETUP @ L1924 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1413 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1414 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1415 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1416 | disable-self | QSTRATEGY @ L16851 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1417 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1418 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1419 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1420 | disable-self | QSTRATEGY @ L16851 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1421 | build | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1422 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1423 | disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1424 | build, building-type-count-total, disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1425 | build, building-type-count-total, disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1426 | build, building-type-count-total, disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1427 | build, building-type-count-total, disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1428 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1429 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1430 | build | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1431 | build, building-type-count-total | QECO NUMBERS @ L16922, QLC @ L21220 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1432 | up-full-reset-search, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1433 | build, up-find-remote | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1434 | build, up-find-remote | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1435 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1436 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1437 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1438 | build | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1439 | — | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1440 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1441 | disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1442 | disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1443 | disable-self | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1444 | up-find-local, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QECO NUMBERS @ L16922, QHOUSES @ L4383 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1445 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1446 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1447 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1448 | build, disable-self, train | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1449 | train | QECO NUMBERS @ L16922 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1450 | disable-self, train | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1451 | build, disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1452 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1453 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1454 | build, disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1455 | disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1456 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1457 | disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1458 | build, disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1459 | disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1460 | build, disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1461 | disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1462 | disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1463 | disable-self | QUEUE @ L17245 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1464 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1465 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1466 | up-jump-rule | QBECO @ L17393 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1467 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1468 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1469 | enable-timer | QBECO @ L17393 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1470 | enable-timer | QBECO @ L17393 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1471 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1472 | build, research | QBECO @ L17393, QCUP @ L14868 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1473 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1474 | enable-timer | QBECO @ L17393 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1475 | build, enable-timer | QBECO @ L17393 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1476 | build, research | QBECO @ L17393, QBH @ L7174 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1477 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1478 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1479 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1480 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1481 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1482 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1483 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1484 | disable-self | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1485 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1486 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1487 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1488 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1489 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QEVAL @ L9821, QMISC @ L3246, QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1490 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1491 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1492 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1493 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1494 | enable-timer | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1495 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1496 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1497 | up-find-remote, up-full-reset-search, up-get-search-state, up-set-target-point | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1498 | up-jump-rule | QADVANTAGE @ L2057, QTARGET STUFF @ L2666 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1499 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1500 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1501 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1502 | disable-self | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1503 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1504 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1505 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1506 | disable-self | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1507 | disable-self | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1508 | build, disable-self | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1509 | build | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1510 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1511 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1512 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1513 | disable-self | QTOWN SAFETY @ L17636 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1514 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1515 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1516 | up-full-reset-search | QADVANTAGE @ L2057, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1517 | up-find-remote | QSCOUT @ L9068, QSPEARS @ L8501, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1518 | up-jump-rule | QADVANTAGE @ L2057, QMISC @ L3246 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1519 | up-clean-search, up-set-target-object, up-set-target-point | QRAIDING @ L10481, QSPEARS @ L8501, QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1520 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1521 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1522 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1523 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1524 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1525 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1526 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1527 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1528 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1529 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1530 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1531 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1532 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1533 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1534 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1535 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1536 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1537 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1538 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1539 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1540 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1541 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1542 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1543 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1544 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1545 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1546 | disable-self | QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1547 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1548 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1549 | disable-self | QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1550 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1551 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1552 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1553 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1554 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1555 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1556 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1557 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1558 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1559 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1560 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1561 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1562 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1563 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1564 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1565 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1566 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1567 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1568 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1569 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1570 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1571 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1572 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1573 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1574 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1575 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1576 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1577 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1578 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1579 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1580 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1581 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1582 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1583 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1584 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1585 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1586 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1587 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1588 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1589 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1590 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1591 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1592 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1593 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1594 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1595 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1596 | enable-timer | QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1597 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1598 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1599 | disable-self | QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1600 | disable-self | QTARGET PLAYER @ L17945 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1601 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1602 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1603 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1604 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1605 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1606 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1607 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1608 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1609 | build | QCASTLES @ L20765, QDAMAGE POTENTIAL @ L19299, QPRIORITY @ L18933 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1610 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1611 | disable-self | QSCOUTING @ L19032 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1612 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1613 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1614 | build | QSCOUTING @ L19032 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1615 | build, enable-timer | QSCOUTING @ L19032 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1616 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1617 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1618 | — | QATTACK EFFICIENCY @ L19083 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1619 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1620 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1621 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1622 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1623 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1624 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1625 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1626 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1627 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1628 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1629 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1630 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1631 | up-find-remote, up-full-reset-search, up-get-search-state | QATTACK EFFICIENCY @ L19083, QEVAL @ L9821 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1632 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1633 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1634 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1635 | up-find-remote, up-full-reset-search, up-get-search-state | QADVANTAGE @ L2057, QATTACK EFFICIENCY @ L19083 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1636 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1637 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1638 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1639 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1640 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1641 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1642 | — | QDAMAGE POTENTIAL @ L19299 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1643 | build | QCASTLES @ L20765, QDAMAGE POTENTIAL @ L19299, QPRIORITY @ L18933 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1644 | build | QDAMAGE POTENTIAL @ L19299, QPRIORITY @ L18933 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1645 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1646 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1647 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1648 | research, research-pending, up-research | QADVANTAGE @ L2057, QDAMAGE POTENTIAL @ L19299, QDLURING @ L6795 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1649 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1650 | disable-self, research, research-pending, up-research | QDAMAGE POTENTIAL @ L19299, QFLUSH @ L13980 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1651 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1652 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1653 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1654 | research, research-completed | QDAMAGE POTENTIAL @ L19299 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1655 | research, research-completed | QDAMAGE POTENTIAL @ L19299 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1656 | research, research-completed | QDAMAGE POTENTIAL @ L19299 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1657 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1658 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1659 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1660 | build, can-research-with-escrow, research | Q2BA @ L19462, QHCOL @ L19784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1661 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1662 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1663 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1664 | build, can-research-with-escrow, research | Q2BA @ L19462, QHCOL @ L19784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1665 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1666 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1667 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1668 | build, can-research-with-escrow, research, unit-type-count-total, up-research | QBOWSAW @ L19549, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1669 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1670 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1671 | build, set-escrow-percentage, unit-type-count-total | QBOWSAW @ L19549, QCHAINBARDING @ L14559, QSCALEBARDING @ L14658 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1672 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1673 | build, can-research-with-escrow, research, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1674 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1675 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1676 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1677 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1678 | build, can-research-with-escrow, research | QGOLDMINING @ L19649, QHCOL @ L19784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1679 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1680 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1681 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1682 | build, can-research-with-escrow, research | QGOLDMINING @ L19649, QHCOL @ L19784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1683 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1684 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1685 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1686 | build, can-research-with-escrow, research, up-research | QBODKIN @ L15121, QGOLDSHAFT @ L19736, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1687 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1688 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1689 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QGOLDSHAFT @ L19736, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1690 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1691 | build, can-research-with-escrow, research | Q2BA @ L19462, QHCOL @ L19784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1692 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1693 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1694 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1695 | build, can-research-with-escrow, research | QGOLDMINING @ L19649, QHCOL @ L19784 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1696 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1697 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1698 | build, research, research-pending, up-research | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1699 | build, can-research-with-escrow, research, up-research | QBODKIN @ L15121, QGOLDSHAFT @ L19736, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1700 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1701 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1702 | build, release-escrow, set-escrow-percentage | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1703 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1704 | disable-timer, train | QVILLAGERS @ L19918 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1705 | research | QFORCEDROP @ L7949, QLOOM @ L15175 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1706 | build, research, research-completed | QSETUP @ L1924, QVILLAGERS @ L19918 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1707 | build, up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1708 | enable-timer, train, unit-type-count-total, up-train | QVILLAGERS @ L19918 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1709 | train, up-train | QVILLAGERS @ L19918 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1710 | train, unit-type-count-total, up-train | QVILLAGERS @ L19918 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1711 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1712 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1713 | build, release-escrow, set-escrow-percentage | QESCROW @ L19996, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1714 | release-escrow, set-escrow-percentage | QESCROW @ L19996, QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1715 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1716 | build, research, research-pending, up-research | QCUP @ L14868, QESCROW @ L19996 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1717 | research, research-pending, up-research | QADVANTAGE @ L2057, QDLURING @ L6795, QFORCEDROP @ L7949 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1718 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1719 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1720 | disable-self | QTSB @ L20097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1721 | disable-self | QTSB @ L20097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1722 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1723 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1724 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1725 | disable-self | QTSB @ L20097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1726 | disable-self | QTSB @ L20097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1727 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1728 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1729 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1730 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1731 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1732 | build, can-build-with-escrow | QRANGES @ L20188, QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1733 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1734 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1735 | build, can-build-with-escrow, release-escrow, set-escrow-percentage, up-build | QMONASTERY @ L16168, QRANGES @ L20188, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1736 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1737 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1738 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1739 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1740 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1741 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1742 | build, set-escrow-percentage | QBODKIN @ L15121, QCHAINBARDING @ L14559, QSCALEBARDING @ L14658 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1743 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1744 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1745 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1746 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1747 | build, can-build-with-escrow, up-build | QMONASTERY @ L16168, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1748 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1749 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1750 | build, release-escrow, set-escrow-percentage | QFORGING @ L14459, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1751 | build, up-modify-escrow | QBODKIN @ L15121, QFLTCH @ L14973, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1752 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1753 | build, can-build-with-escrow, release-escrow, set-escrow-percentage, up-build | QMONASTERY @ L16168, QRANGES @ L20188, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1754 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1755 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1756 | build, building-type-count-total | QFORCEDROP @ L7949, QMONASTERY @ L16168, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1757 | build, building-type-count-total, up-build | QFARMS @ L20800, QHOUSE @ L21070, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1758 | build, building-type-count-total, research, research-completed | QMARKET @ L16231, QRAX @ L20476 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1759 | build, building-type-count-total, research, research-completed | QMARKET @ L16231, QRAX @ L20476 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1760 | up-modify-escrow | QCHAINMAIL @ L14326, QMARKET @ L16231, QSCALEMAIL @ L14293 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1761 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1762 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1763 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1764 | build, can-build-with-escrow | QRANGES @ L20188, QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1765 | build, building-type-count-total, up-assign-builders | QRAX @ L20476 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1766 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1767 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1768 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1769 | build, can-build-with-escrow | QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1770 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1771 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1772 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1773 | build, can-build-with-escrow | QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1774 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1775 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1776 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1777 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1778 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1779 | build, can-build-with-escrow | QRAX @ L20476, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1780 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1781 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1782 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1783 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1784 | build, can-build-with-escrow, set-escrow-percentage | QLC @ L21220, QSMITH @ L20652 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1785 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1786 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1787 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1788 | build, up-assign-builders | QCASTLES @ L20765 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1789 | build, up-assign-builders | QCASTLES @ L20765 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1790 | build, up-assign-builders | QCASTLES @ L20765 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1791 | build, up-build | QCASTLES @ L20765, QMONASTERY @ L16168, QUNIVERSITY @ L22097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1792 | research, research-pending, up-research | QADVANTAGE @ L2057, QDLURING @ L6795, QFARMS @ L20800 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1793 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1794 | build, building-type-count-total, can-build-with-escrow | QFARMS @ L20800 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1795 | build, up-jump-rule | QFARMS @ L20800 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1796 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1797 | build, building-type-count-total | QFARMS @ L20800, QMARKET @ L16231 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1798 | build, research, research-pending, up-build, up-research | QCUP @ L14868, QFARMS @ L20800, QFLTCH @ L14973 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1799 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1800 | build, building-type-count-total | QFARMS @ L20800, QHOUSE @ L21070 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1801 | build, research, up-research | QFARMS @ L20800, QIRONCASTING @ L14362 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1802 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1803 | build, building-type-count-total, up-build | QFARMS @ L20800, QHOUSE @ L21070, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1804 | build, building-type-count-total, can-build-with-escrow | QFARMS @ L20800 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1805 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1806 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1807 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1808 | build, building-type-count-total, can-build-with-escrow | QFARMS @ L20800 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1809 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1810 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1811 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1812 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1813 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1814 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1815 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1816 | build, up-assign-builders | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1817 | build, can-build-with-escrow, up-build | QHOUSE @ L21070, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1818 | build, can-build-with-escrow, up-build | QHOUSE @ L21070, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1819 | build, disable-self, up-assign-builders, up-build | QHOUSE @ L21070, QLC @ L4474, QTOWERS @ L15684 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1820 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1821 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1822 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1823 | build | QHOUSE @ L21070 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1824 | build | QHOUSE @ L21070 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1825 | build, building-type-count-total, up-build | QFARMS @ L20800, QHOUSE @ L21070, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1826 | build, building-type-count-total | QFARMS @ L20800, QHOUSE @ L21070 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1827 | build, up-build | QCASTLES @ L20765, QHOUSE @ L21070 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1828 | build, can-build-with-escrow, set-escrow-percentage | QLC @ L21220, QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1829 | build, building-type-count-total | QLC @ L21220, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1830 | build, building-type-count-total | QLC @ L21220, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1831 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1832 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1833 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1834 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1835 | build, building-type-count-total, can-build-with-escrow, set-escrow-percentage | QLC @ L21220, QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1836 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1837 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1838 | build, building-type-count-total | QMARKET @ L16231, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1839 | build, building-type-count-total, can-build-with-escrow | QFARMS @ L20800, QLC @ L21220 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1840 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1841 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1842 | build, can-build-with-escrow, set-escrow-percentage | QLC @ L21220 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1843 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1844 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1845 | build, building-type-count-total | QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1846 | build, can-build-with-escrow, set-escrow-percentage | QLC @ L21220 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1847 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1848 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1849 | build, building-type-count-total | QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1850 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1851 | build, can-build-with-escrow, release-escrow, set-escrow-percentage | QLC @ L21220, QRANGES @ L20188, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1852 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1853 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1854 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1855 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1856 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1857 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1858 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1859 | research, research-pending, up-research | QADVANTAGE @ L2057, QDLURING @ L6795, QFORCEDROP @ L7949 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1860 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1861 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1862 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1863 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1864 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1865 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1866 | build, building-type-count-total, can-build-with-escrow, enable-timer, set-escrow-percentage | QLC @ L21220, QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1867 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1868 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1869 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1870 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1871 | build, building-type-count-total | QFLUSH @ L13980, QFORCEDROP @ L7949, QKRUSH @ L13861 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1872 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1873 | build, building-type-count-total | QFORCEDROP @ L7949, QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1874 | build, building-type-count-total | QFORCEDROP @ L7949, QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1875 | build, building-type-count-total | QFORCEDROP @ L7949, QKRUSH @ L13861, QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1876 | build, building-type-count-total | QMILL @ L21649 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1877 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1878 | build, building-type-count-total, can-build-with-escrow, up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1879 | build, can-build-with-escrow, up-set-target-object | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1880 | build, enable-timer | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1881 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1882 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1883 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1884 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1885 | build, building-type-count-total, can-build-with-escrow, up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1886 | build, can-build-with-escrow, up-set-target-object | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1887 | build, enable-timer | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1888 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1889 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1890 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1891 | up-jump-rule | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1892 | build, can-build-with-escrow, up-clean-search, up-find-remote, up-full-reset-search, up-set-target-point | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1893 | build, can-build-with-escrow, up-set-target-object | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1894 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1895 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1896 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1897 | build, can-build-with-escrow, up-clean-search, up-find-remote, up-full-reset-search, up-remove-objects, up-set-target-point | QMC @ L21762 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1898 | build, can-build-with-escrow | QMC @ L21762, QRANGES @ L20188, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1899 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1900 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1901 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1902 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1903 | build, can-build-with-escrow, up-build | QMONASTERY @ L16168, QSTABLE @ L15764, QUNIVERSITY @ L22097 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1904 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1905 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1906 | build, release-escrow, set-escrow-percentage | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1907 | build, building-type-count-total | QRANGES @ L20188, QSTABLE @ L15764, QSW @ L20339 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1908 | build, can-research-with-escrow, research, up-research | QBODKIN @ L15121, QGOLDSHAFT @ L19736, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1909 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1910 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1911 | build, release-escrow, set-escrow-percentage | QMONASTERY @ L16168, QSTABLE @ L15764 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1912 | build, research, research-pending, up-research | QCUP @ L14868, QFLTCH @ L14973, QLAA @ L15024 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1913 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1914 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1915 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1916 | disable-self | QMISC @ L22220 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1917 | disable-self | — | ADDED/UNKNOWN |
| `ShadowByzantine/ShadowByzantine.per` | 1918 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1919 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1920 | build | QENEMY STRATEGY @ L22263 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1921 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1922 | disable-self | QENEMY STRATEGY @ L22263 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1923 | build, disable-self | QENEMY STRATEGY @ L22263 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1924 | build | QENEMY STRATEGY @ L22263 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1925 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1926 | build | QENEMY STRATEGY @ L22263 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1927 | disable-self | QEAGOL @ L22352 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1928 | disable-self | QEAGOL @ L22352 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1929 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1930 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1931 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1932 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1933 | disable-self | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1934 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1935 | build | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1936 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1937 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1938 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1939 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1940 | — | QEAGOL @ L22352 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1941 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1942 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1943 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1944 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1945 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1946 | — | QEAGOL @ L22352 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1947 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1948 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1949 | — | QSPECIAL TIMERS @ L22541 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1950 | enable-timer | QSPECIAL TIMERS @ L22541 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1951 | enable-timer | QSPECIAL TIMERS @ L22541 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1952 | enable-timer | QSPECIAL TIMERS @ L22541 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1953 | enable-timer | QSPECIAL TIMERS @ L22541 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1954 | enable-timer | QSPECIAL TIMERS @ L22541 | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1955 | — | — | PRESERVED/MOVED |
| `ShadowByzantine/ShadowByzantine.per` | 1956 | — | — | PRESERVED/MOVED |

### E. Generator invariants

1. Donor ordinals are assigned solely by source-order `defrule` extraction.
2. Donor offsets are the actual source line intervals in `ShadowSource.per`.
3. No conceptual subsystem name is used as a donor ordinal.
4. Exact rule text is required for PRESERVED/MOVED; mechanism overlap alone cannot promote to exact transplantation.
5. A candidate match is not runtime qualification and does not establish firing reachability.
6. Command issuance remains distinct from world-state completion.

<!-- END GENERATED RULE-LEVEL ATLAS -->
