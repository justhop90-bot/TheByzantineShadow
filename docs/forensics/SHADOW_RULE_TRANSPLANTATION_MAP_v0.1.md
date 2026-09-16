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
