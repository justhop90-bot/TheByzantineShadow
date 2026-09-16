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