# Shadow DC7 — Full Escrow Dependency Closure v0.1

## Status

Forensic transplant-boundary report. Static source evidence only unless explicitly marked otherwise. This artifact traces the dependency closure of the active Shadow escrow/reservation families around the recovered source-order machine. It deliberately distinguishes **local closure** (rules immediately required by the family) from **shared-state closure** (writers/readers elsewhere in the 1,956-rule machine that can alter the family's inputs or bypass its local path).

## Historical basis

- Donor: `Shadow DC7.per`
- Historical commit: `1d9f45b3b9ac03adc24103df2b21c84b92a45fb6`
- Preserved blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`
- Extracted SHA-256: `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`
- Source: 22,604 lines / 615,773 UTF-8 bytes / 1,956 `defrule` blocks
- Primary source-order matrix: `SHADOW_SOURCE_ORDER_MATRIX_v0.3.md`
- Primary control-flow trace: `SHADOW_LIVE_CONTROL_FLOW_AND_ESCROW_v0.2.md`
- Prior transplant decomposition: `SHADOW_ESCROW_TRANSPLANT_SLICES_v0.1.md`

## Evidence discipline

1. Source-order reachability is not runtime firing proof.
2. Command issuance is not completion.
3. `can-research-with-escrow` / `can-train-with-escrow` are gates, not completion predicates.
4. `release-escrow` is an issued engine operation; it is not itself proof that escrow reached zero.
5. `gl-escrow-state` is an engine accounting-mode selector, not a logical commitment owner.
6. A shared goal is a dependency even when the family does not write it locally.
7. A jump is a control-flow edge; it is not a semantic priority edge.
8. The author warned that unused experimental code may remain, so every family is classified by active structural evidence rather than by source presence alone.

---

## 1. Closure model

Every family is decomposed into the following nodes:

```text
TRIGGER WRITERS
      ↓
TRIGGER READERS
      ↓
PROGRESSION CURSOR / INTERRUPTION
      ↓
ESCROW WRITERS
      ↓
ESCROW-MODE READERS/WRITERS
      ↓
COMMAND RULE
      ↓
COMPLETION OBSERVER
      ↓
PROGRESSION MUTATION
      ↓
RELEASE / RESTORATION
      ↓
RE-ENTRY
      ↓
COMPETING WRITERS
      ↘
       JUMP / BYPASS EDGES
```

The actual transplant boundary is the **smallest connected subgraph that preserves all state transitions needed for the desired behavior**, not the visible escrow rule itself.

### Shared substrate nodes

All research families below converge on a common Shadow substrate:

- `gl-strategy`
- `gl-build-progress`
- `gl-current-build-item`
- `gl-progression-pause`
- `gl-escrow-state`
- engine escrow amounts / percentages
- `up-research-status`
- `research-completed`
- `can-research-with-escrow`
- `set-escrow-percentage`
- `up-modify-escrow`
- `release-escrow`

This shared substrate is the principal reason **copying individual escrow rules is unsafe**: the rule's meaning is supplied by state written outside the rule.

---

## 2. Active escrow-family inventory

The recovered active `up-modify-escrow` reservation/modification families are:

| Family | Core rules | Resource action | Command | Completion / reconciliation |
|---|---|---|---|---|
| F01 Scale Mail | 1172–1174 | food +100 max | `up-research ... ri-scale-mail` | research-status / progression context |
| F02 Chain Mail | 1175–1177 | food +200, gold +100 max | `up-research ... ri-chain-mail` | research-status / progression context |
| F03 Iron Casting — KRUSH | 1179–1182 | food/gold LOW, wood released | `up-research ... ri-iron-casting` | status → `gl-build-progress +1` |
| F04 Iron Casting — FLUSH | 1184–1187 | food +220, gold +120, wood released | `up-research ... ri-iron-casting` | status → `gl-build-progress +1` |
| F05 Forging — KRUSH | 1189–1197 | food LOW, wood/gold released | `up-research ... ri-forging` | status → `gl-build-progress +1` |
| F06 Forging — FLUSH | 1194–1197 / 1188–1191 | food MID, wood/gold released | `up-research ... ri-forging` | status → `gl-build-progress +1` |
| F07 Chain Barding — KRUSH | 1199–1202 | food/gold LOW, wood released | `up-research ... ri-chain-barding` | status → `gl-build-progress +1` |
| F08 Chain Barding — FLUSH | 1204–1207 | food/gold MID-HIGH, wood released | `up-research ... ri-chain-barding` | status → `gl-build-progress +1` |
| F09 Scale Barding — KRUSH | 1209–1212 | food LOW, gold/wood released | `up-research ... ri-scale-barding` | status → `gl-build-progress +1` |
| F10 Fletching | 1237–1240 | food +100, gold +50 max | legacy `research ri-fletching` path | status → `gl-build-progress +1` |
| F11 Leather Archer Armor | 1242–1245 | food/gold MID-HIGH, wood released | `up-research ... ri-leather-archer-armor` | status → `gl-build-progress +1` |
| F12 Padded Archer Armor | 1247–1250 | food +100 max, wood/gold released | legacy `research ri-padded-archer-armor` path | status → `gl-build-progress +1` |

### Important qualification

The matrix contains additional `set-escrow-percentage`, `release-escrow`, build, siege, and diagnostic rules outside this twelve-family reservation set. They are **competing escrow users or separate escrow families**, not silently folded into these twelve research reservations. They therefore remain in the competing-writer / shared-substrate closure rather than being erased from the model.

---

# 3. Family dependency closures

## F01 — Scale Mail

### Local closure

```text
1172 trigger
  ├─ gl-strategy = FLUSH
  ├─ game-time >= 1080
  ├─ current-age >= FEUDAL
  ├─ gl-progression-pause = -1
  ├─ blacksmith > 0
  ├─ enemy-pocket OR enemy-strategy KRUSH/POSSIBLE-KRUSH
  └─ ri-scale-mail < research-pending
        ↓
1172 writes gl-progression-pause = SCALEMAIL
        ↓
1173 writes physical food escrow +100 max
        ↓
1174 requires pause=SCALEMAIL + can-research-with-escrow
        ↓
up-research gl-escrow-state ri-scale-mail
        ↓
clear pause; zero food percentage; release food
        ↓
1175 is the next strategic reader and can trigger CHAINMAIL only after pause is -1
```

### Dependency classes

- **Trigger writers:** all writers of `gl-strategy`, `gl-progression-pause`, enemy-strategy state, and any initialization that establishes blacksmith/age state.
- **Trigger readers:** 1172.
- **Escrow writer:** 1173.
- **Escrow-mode dependency:** `gl-escrow-state` is consumed by the command; its writer set is global/shared.
- **Command:** 1174.
- **Completion observer:** no completion proof is contained in 1174; downstream research-status rules are required.
- **Progression mutation:** subsequent progression logic, not the command itself, determines the next state.
- **Release:** 1174.
- **Re-entry:** 1175 and the broader FLUSH progression sequence.
- **Competing writers:** every global `gl-progression-pause` writer; every food escrow percentage writer; every `release-escrow food` writer.
- **Jump bypass:** any incoming jump targeting past 1172–1174 can bypass the family; any jump into the broader progression neighborhood can re-enter without traversing the local predecessor. Exact runtime firing remains unproven.

**Boundary:** trigger semantics + pause state + rule 1173 + command rule 1174 + completion/re-entry observers. Do not transplant 1173/1174 alone.

---

## F02 — Chain Mail

```text
1175 trigger
  -> pause=CHAINMAIL
  -> 1176 food+200/gold+100
  -> 1177 escrow-aware research
  -> pause=-1
  -> zero food/gold percentages
  -> release food/gold
  -> downstream progression resumes
```

**Trigger readers:** 1175 consumes `gl-strategy`, `gl-progression-pause`, Pikeman completion, Scale Mail/Bodkin status, and enemy cavalry/stable telemetry.

**Escrow writer:** 1176.

**Escrow mode:** global `gl-escrow-state` consumed by 1177.

**Command:** 1177.

**Completion observer:** research status is upstream gating; 1177 itself does not prove completion. Subsequent progression state is required.

**Release:** 1177.

**Re-entry:** 1178 and the Iron Casting progression branch.

**Competing writers:** all writers of pause and food/gold escrow percentages; Iron Casting and other later families share the same physical escrow namespace.

**Jump bypass:** incoming control-flow edges can bypass 1175–1177; no local jump exists in the three-rule family.

**Boundary:** the complete 1175–1177 chain plus the shared progression and release substrate.

---

## F03/F04 — Iron Casting bifurcation

Iron Casting is not one family. It is a **shared capability target with two policy branches**.

### KRUSH closure

```text
1179 reconcile build-progress to KrushIronCastingNumber
1180 restore current-build-item=IRONCASTING
1181 configure food/gold LOW; release wood
1178 command: up-research(...iron-casting)
1182 observe research-pending threshold
    -> build-progress +1
```

### FLUSH closure

```text
1184 reconcile build-progress to IronCastingNumber
1185 restore current-build-item=IRONCASTING
1186 reserve food+220/gold+120; release wood
1183 command: up-research(...iron-casting)
1187 observe research-pending threshold
    -> build-progress +1
```

### Critical finding

The **command appears before its branch-local reconciliation rules in source order** for each path. Therefore source order alone does not define the whole semantic path. The progression cursor and current-item writers are the actual bridge.

**Trigger writers/readers:** `gl-strategy`, `gl-current-build-item`, `gl-build-progress`, `gl-progression-pause`, and the relevant milestone constants.

**Escrow writers:** 1181 / 1186.

**Command:** 1178 / 1183.

**Completion observers:** 1182 / 1187 use research status and mutate build progress.

**Release:** 1181 / 1186 release wood; the source does not show a symmetric release of the food/gold protection at those exact rules because the next progression state owns the continuing escrow policy.

**Re-entry:** subsequent progression families read the updated cursor.

**Competing writers:** all KRUSH/FLUSH writers of `gl-build-progress`, `gl-current-build-item`, and escrow percentages.

**Jump bypass:** the family is vulnerable to any jump that crosses the command/cursor neighborhood; this is precisely why cursor reconciliation must be included in the transplant boundary.

**Boundary:** policy branch + cursor reconciliation + escrow configuration + command + completion observer. This is a **state-machine slice**, not an escrow slice.

---

## F05/F06 — Forging bifurcation

### KRUSH

1194 restores `KrushForgingNumber`; 1195 restores `FORGING`; 1196 configures LOW food and releases wood/gold; 1193 issues escrow-aware research; 1197 observes pending state and advances progress.

### FLUSH

1189 restores `ForgingNumber`; 1190 restores `FORGING`; 1191 configures MID food and releases wood/gold; 1188 issues escrow-aware research; 1192/1197-style progression logic advances after research status.

**Shared dependencies:** `gl-strategy`, `gl-progression-pause`, `gl-current-build-item`, `gl-build-progress`, `gl-escrow-state`, `ri-forging` status.

**Competing writers:** all progression writers and all percentage/release writers for food/wood/gold.

**Boundary:** retain the branch-specific policy constants and trigger predicates as policy; transplant the cursor → escrow → command → observed-status → advance mechanism as substrate.

---

## F07/F08 — Chain Barding bifurcation

### KRUSH

1199 → 1200 → 1201 → 1198 command → 1202 completion.

Reservation policy: food/gold LOW, wood released, with a time guard `current-age-time >= 460`.

### FLUSH

1204 → 1205 → 1206 → 1203 command → 1207 completion.

Reservation policy: food/gold MID-HIGH, wood released.

**Completion observer:** 1202 / 1207 use `research-status >= research-pending` and advance `gl-build-progress`.

**Boundary:** same as Forging, but preserve the age/time guard as strategic policy rather than generic substrate.

---

## F09 — Scale Barding KRUSH

```text
1209 restore cursor if needed
1210 restore current item
1211 configure food LOW; release gold/wood
1208 issue escrow-aware research
1212 observe research status -> progress +1
```

**Trigger dependency:** KRUSH strategy, castle-age, current-age-time >= 180, pause=-1, current item.

**Competing writers:** all writers of pause/current-item/build-progress and food/gold/wood escrow state.

**Boundary:** cursor reconciliation + physical resource policy + command + completion observer. Castle-age/time threshold is policy, not substrate.

---

## F10 — Fletching

The Fletching path is materially different and must not be falsely normalized to the later escrow-aware research families.

```text
1237 cursor correction if status < pending
1238 current-item = FLTCH
1239 reserve food +100 / gold +50
1240 status >= pending -> build-progress +1
```

A separate command rule at 1236 uses legacy `research ri-fletching`, not the exact escrow-aware `up-research gl-escrow-state` form.

**Finding:** this family is a **mixed-generation path**. It is evidence for economic reservation, but not a clean template for the newer escrow-aware execution contract.

**Boundary:** preserve the reservation/completion pattern only; do not transplant the legacy command semantics without separate runtime qualification.

---

## F11 — Leather Archer Armor

```text
1242 cursor correction
1243 current-item = LAA
1244 food/gold MID-HIGH; wood released
1241 escrow-aware research
1245 status >= pending -> build-progress +1
```

**Trigger dependencies:** `gl-strategy=FLUSH`, pause=-1, current item, research status, build-progress milestone.

**Competing writers:** shared progression cursor and escrow namespace.

**Boundary:** generic cursor/escrow/research/completion substrate; FLUSH trigger and MID-HIGH percentage are policy.

---

## F12 — Padded Archer Armor

```text
1247 cursor correction
1248 current-item = PAA
1249 completion-conditioned rebalancing: food +100; release wood/gold
1250 status >= pending -> build-progress +1
1246 legacy research command
```

**Finding:** PAA is another mixed-generation boundary. The escrow operation at 1249 is conditional on Fletching being complete, while the command at 1246 is legacy `research`, not the exact `up-research gl-escrow-state` form.

**Boundary:** transplant the **resource rebalancing + cursor reconciliation** mechanism, but treat the command layer as an unqualified legacy interface.

---

# 4. Trigger-writer closure

The families do not own their triggers. The shared state writers are therefore part of the dependency closure.

## `gl-strategy`

Shadow contains strategy initialization and strategy switching, including FLUSH and KRUSH. Every research family whose entry guard includes `goal gl-strategy ...` depends on that strategy state.

**Transplant consequence:** Byzantine policy must become the writer of the strategic mode/requirement decision. Viking FLUSH/KRUSH policy must not be copied as if it were civilization-neutral.

## `gl-progression-pause`

This is the central interrupt latch. Family triggers require `-1`; exceptional requirements set it to a family-specific token; execution/release paths clear it.

**Transplant consequence:** preserve the interrupt mechanism but change its writer authority. AEGIS can request an interruption; the Shadow substrate should remain the initial physical/economic actuator.

## `gl-current-build-item`

Multiple reconciliation rules write this goal from `gl-build-progress`. Family commands read it. This is a hidden dependency if only the escrow rules are copied.

## `gl-build-progress`

Progress is corrected backward when observed research state says the item has not actually been reached, then incremented after the required status is observed. This is the re-entry/reconciliation mechanism.

**Transplant consequence:** this cursor logic is more reusable than the specific progression numbers.

---

# 5. Escrow-mode closure

`gl-escrow-state` is consumed by escrow-aware `up-research` and `up-train` commands. It is therefore a command parameter dependency, not a reservation ledger.

The correct dependency graph is:

```text
AEGIS / Shadow strategic decision
        ↓
logical requirement
        ↓
physical escrow configuration
        ↓
(gl-escrow-state = with-escrow)
        ↓
up-research / up-train
```

Do **not** invert this into:

```text
gl-escrow-state = owner of the requirement
```

That would corrupt the engine/accounting abstraction.

---

# 6. Completion-observer closure

The research families use several observable predicates:

- `up-research-status ... < research-pending`
- `up-research-status ... >= research-pending`
- `research-completed ...`

The important dependency is directional:

```text
command issuance
      ↓
engine state changes later
      ↓
research-status observer
      ↓
progression mutation
```

The command rule itself must never be treated as the completion observer.

---

# 7. Release closure

There are two distinct release patterns.

### Terminal release

A family clears its percentage and issues `release-escrow resource`. This is the explicit cleanup boundary.

### Continuing-policy reconfiguration

Some progression rules deliberately release one resource while maintaining or increasing protection on another. Examples include Iron Casting and later blacksmith/progression stages.

Therefore:

```text
release(resource)
!=
transaction finished
```

and:

```text
resource release
!=
whole progression release
```

This is why a transplant that mechanically releases all four resources after every requirement would destroy Shadow's economic pacing.

---

# 8. Competing-writer closure

The most important competing writers are not necessarily adjacent to the family.

### Shared progression writers

- `gl-progression-pause`
- `gl-current-build-item`
- `gl-build-progress`
- `gl-strategy`

### Shared physical escrow writers

- `up-modify-escrow`
- `set-escrow-percentage`
- `release-escrow`

These are also used by building, siege, market, blacksmith, and other strategic paths elsewhere in Shadow. Consequently, **the physical escrow namespace is globally shared**.

### Practical consequence

A Byzantine transplant must not create a second physical escrow authority beside this substrate. It would produce two independent writers for the same engine state and make release/ownership ambiguous.

---

# 9. Jump bypass closure

The static CFG establishes two forms of control flow:

1. normal successor: rule `n -> n+1`
2. explicit jump successor: `n -> n+1+Δ`

For escrow transplantation, the dangerous jump cases are:

- **pre-trigger bypass:** jump skips the requirement trigger;
- **reservation bypass:** jump skips physical protection;
- **command bypass:** jump skips execution;
- **completion bypass:** jump skips observation and advances control without evidence;
- **release bypass:** jump leaves protected resources stranded;
- **re-entry jump:** jump returns directly to a progression neighborhood after an interruption.

The family-local reservation blocks above contain no explicit jump edge in their immediate rule triplets. The real hazard is therefore **incoming/outgoing jumps from the surrounding 1,956-rule machine**.

### Boundary rule

Any transplanted slice that changes source order must preserve, replace, or deliberately terminate every jump edge entering the removed/replaced state interval. A visually identical sequence inserted elsewhere is not semantically equivalent if an existing `up-jump-rule` target changes meaning.

---

# 10. Actual transplant boundaries

## Boundary A — Generic economic substrate

**Transplant.**

- physical escrow primitives
- escrow percentage reconfiguration
- resource-specific release
- escrow-aware engine accounting mode
- completion-driven resource/progression reconciliation
- interruption latch semantics
- cursor reconciliation pattern
- re-entry after interruption

**Initial owner:** Shadow-derived economic substrate.

## Boundary B — Byzantine policy layer

**Redesign.**

- enemy/threat classification
- capability gap
- candidate response
- resource cost vector
- Byzantine relative efficiency
- requirement identity
- strategic priority/arbitration
- interruption request

**Owner:** Byzantine/AEGIS policy layer.

## Boundary C — Viking-specific payload

**Do not transplant.**

- FLUSH/KRUSH strategic meaning
- Viking build-order milestones
- Viking unit composition assumptions
- Viking-specific timing thresholds unless independently justified
- enemy assumptions tuned to Shadow's test envelope

## Boundary D — Execution interface

**Preserve initially.**

- existing `up-research` / `up-train` semantics
- existing proven executors
- engine accounting mode

Change only after runtime evidence demonstrates a concrete defect.

## Boundary E — Mixed-generation legacy paths

**Quarantine pending qualification.**

Fletching and Padded Archer Armor contain legacy `research` command paths alongside the newer escrow machinery. They are useful forensic evidence but are not clean transplantation templates.

---

# 11. Minimal safe transplant unit

The minimum safe transplant unit is:

```text
[trigger contract]
      +
[progression cursor contract]
      +
[escrow policy]
      +
[escrow accounting mode]
      +
[execution command]
      +
[completion observer]
      +
[progression mutation]
      +
[release/reconfiguration]
      +
[re-entry]
      +
[incoming/outgoing jump closure]
      +
[competing-writer audit]
```

Anything smaller is a **code fragment**, not a behavioral transplant.

---

# 12. Final forensic conclusion

The dependency closure proves a stronger proposition than the prior escrow audit:

> **Shadow's reusable invention is not dynamic escrow by itself. It is a coupled interruption/progression/economic-control machine in which escrow, command accounting, observed completion, cursor reconciliation, release, and re-entry are mutually dependent.**

The practical transplant boundary is therefore:

```text
BYZANTINE REQUIREMENT
       ↓
SHADOW-DERIVED INTERRUPTION CONTRACT
       ↓
SHADOW-DERIVED PROGRESSION/CURSOR CONTRACT
       ↓
SHADOW-DERIVED PHYSICAL ESCROW
       ↓
SHADOW EXECUTION INTERFACE
       ↓
OBSERVED COMPLETION
       ↓
SHADOW-DERIVED RELEASE / RECONFIGURATION
       ↓
SHADOW-DERIVED RE-ENTRY
       ↓
BYZANTINE REASSESSMENT
```

This is the boundary we should implement. The Viking strategy should be stripped away; the economic-control machinery should not.

## Qualification status

| Component | Qualification |
|---|---|
| Historical source identity | CONFIRMED |
| 1,956-rule source-order machine | CONFIRMED static |
| Twelve active reservation/modification families | CONFIRMED static set, excluding explicitly diagnostic/dead candidates |
| Shared progression dependency | CONFIRMED static |
| Shared physical escrow namespace | CONFIRMED static |
| `gl-escrow-state` as accounting mode | CONFIRMED static |
| Command ≠ completion | CONFIRMED semantic discipline |
| Completion-driven cursor mutation | CONFIRMED static in the listed families |
| Runtime firing frequency | NOT ESTABLISHED |
| Runtime success of each family | NOT ESTABLISHED |
| Byzantine runtime transplant | NOT YET QUALIFIED |

The next engineering step is therefore **not** to copy these twelve families. It is to build one Byzantine-neutral substrate slice from the cleanest family, qualify it statically, then qualify its runtime state transitions before multiplying the mechanism across requirements.