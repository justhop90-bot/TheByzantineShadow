# The Byzantine Shadow — Full Machine Blueprint v0.3

**Status:** DESIGN BLUEPRINT / DONOR-TRACEABLE / IMPLEMENTATION GATE

**Repository:** `justhop90-bot/TheByzantineShadow`

**Base ref:** `main`

**Current repository head audited:** `0273174c322c027a98c5ceea1cb12d9a08ee215c`

**Canonical donor:** `ShadowSource.per`

**Canonical donor SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

**Canonical donor SHA-256:** `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`

**Donor size:** 22,604 lines / 615,773 UTF-8 bytes / 1,956 `defrule` blocks.

---

## 0. Purpose and authority

This document is the consolidated implementation blueprint for reconstructing the Shadow machine and adapting it to Byzantines. It replaces the need for another proliferation of conceptual architecture documents.

It does **not** claim that every model below is already runtime-qualified. Each model is classified by evidence state. The blueprint is deliberately donor-first:

```text
ShadowSource.per
    ↓
exact rule/order/state/jump/escrow evidence
    ↓
Shadow machine model
    ↓
Byzantine adaptation
    ↓
controlled improvement
    ↓
static validation
    ↓
runtime qualification
```

The repository doctrine remains controlling. No model in this blueprint may be promoted from inference to donor fact merely because the model is useful.

### Evidence classes

- **DIRECT** — explicitly recoverable from canonical donor source or qualified runtime.
- **COMPOSED** — assembled from multiple direct donor observations.
- **INFERRED** — interpretation of directly observed mechanics.
- **BYZANTINE-GENERALIZATION** — donor mechanism adapted to Byzantine requirements.
- **IMPROVEMENT** — new behavior not attributed to Shadow.
- **UNKNOWN** — evidence insufficient for implementation claims.

---

# 1. Machine-level design

The target is not a collection of independent subsystems. It is an ordered `.per` control machine whose state is distributed across goals, strategic numbers, timers, engine state, search state, escrow state, and source-order control flow.

```text
                    ┌──────────────────────────────┐
                    │     Ordered Rule Machine     │
                    │  source order + fall-through │
                    │       + positional jumps    │
                    └──────────────┬───────────────┘
                                   │
          ┌────────────────────────┼────────────────────────┐
          │                        │                        │
     Persistent State          Escrow State            Engine State
 goals / SNs / timers      reserve / feasibility       world / pending
          │                        │                        │
          └────────────────────────┼────────────────────────┘
                                   │
                         Search / Placement
                                   │
                         Commands / Execution
                                   │
                         World-State Observation
                                   │
                         Re-entry / Reassessment
```

The machine therefore has **models**, not necessarily one-for-one source files. A model is a coherent control mechanism recoverable from the donor corpus.

---

# 2. Model inventory

| ID | Model | Purpose | Shadow code reference | Evidence | ShadowByzantine disposition |
|---|---|---|---|---|---|
| M00 | Source Identity & Ordered Program | Establish canonical donor and preserve exact rule order | `ShadowSource.per`; 1,956-rule source-order matrix | DIRECT | PRESERVE |
| M01 | Initialization / Register Bootstrap | Establish goals, timers, state defaults and baseline control state | QID / QGENERAL / QPOSITION opening regions; exact rule ordinals to be mechanically linked from atlas | COMPOSED | PRESERVE + Byzantine constants only where required |
| M02 | Sequential Control / Jump Machine | Use rule order, fall-through, positive skips, negative loops, and self-disabling rules as executable control | Global donor `up-jump-rule` corpus; source-order matrix | DIRECT | PRESERVE TOPOLOGY |
| M03 | Persistent State / Register Machine | Carry progression, tactical, strategic, production and interruption state across rule evaluations | Shared goal/SN corpus; goals 1–317, 392, 478–479; SN/timer corpus | DIRECT/COMPOSED | PRESERVE semantics; retype only when proven |
| M04 | Temporal Control | Gate transitions, delays, retries, reevaluation and tactical cadence | Timer corpus, including timers 1–42 and 46; `t-build-delay`, `t-command-delay`, `t-failsafe`, `t-target-switch`, raid timers, etc. | DIRECT | PRESERVE |
| M05 | Escrow / Reservation Machine | Protect resources, establish transaction mode, gate feasibility, issue operations, release/restoration and re-enter progression | `gl-escrow-state`; `up-modify-escrow`; `set-escrow-percentage`; `can-*-with-escrow`; `release-escrow`; 366 relevant rules / 12 reservation-modification rules / 70 release rules | STRONG STATIC | PRESERVE TOPOLOGY |
| M06 | Progression Cursor Machine | Track current build/research/production item, pause, advance, reconcile and re-enter | `gl-current-build-item`, `gl-progression-pause`, `gl-build-progress`; QSTABLE/QMONASTERY/construction regions | DIRECT/COMPOSED | PRESERVE |
| M07 | Resource Arbitration | Decide when resources are available for competing operations and protect committed resources | QECONOMY / escrow families / construction selectors | COMPOSED | PRESERVE; Byzantine policy may extend |
| M08 | Search Machine | Reset, configure, search local/remote, inspect, clean/remove, select target, extract point | QBUILDINGS and raid/search regions; `up-find-local`, `up-find-remote`, `up-set-target-object`, `up-get-fact`, target-point paths | DIRECT | PRESERVE |
| M09 | Placement Machine | Convert selected target/reference/search result into managed placement command and retry/re-entry state | `place-normal`, `place-point`, `place-control`; placement data / zone / fail-delta | DIRECT/COMPOSED | PRESERVE |
| M10 | Construction Machine | Select construction milestone, establish escrow, search/placement, issue build, observe completion, reconcile progression | Rules 1794–1896 and QBUILDINGS/QMARKET/QSTABLE/QMONASTERY regions | DIRECT/COMPOSED | PRESERVE; Byzantine building policy replaces donor-specific choices |
| M11 | Research Machine | Reserve resources, test feasibility, issue research, observe completion, mutate progression and release | QRESEARCH / technology reservation families; `can-research-with-escrow`; completion via research state | COMPOSED | PRESERVE; Byzantine tech policy adapts |
| M12 | Production Machine | Sequence military/economic production under resource and strategic constraints | QUNITS; QPRO; `can-train-with-escrow`; production jumps | COMPOSED | PRESERVE topology; Byzantine unit mapping |
| M13 | Production Preemption / Priority | Allow emergency or composition-specific branches to bypass normal progression using source-order jumps | QSKIRMS/QSPEARS/QARCHERS/QMANGOS positional bypasses | DIRECT | PRESERVE |
| M14 | Military Group Initialization | Establish group type, size, ranges, firing/movement state and tactical registers | M01 tactical initialization region ~L1938–2064; exact rule mapping to be atlas-linked | DIRECT/COMPOSED | PRESERVE + Byzantine composition |
| M15 | Military Evaluation / Advantage | Evaluate ranged advantage, fight state, distance, composition and tactical readiness | QADVANTAGE; `gl-range-advantage`; `SUPERIORITY`; tactical evaluation region | DIRECT/COMPOSED | PRESERVE |
| M16 | Target Acquisition / Search | Find and score military targets, retain target IDs and waypoints, re-evaluate | M02/M03 military search and raid target regions; `gl-find-new-target`, `gl-raid-target-id`, waypoint state | DIRECT/COMPOSED | PRESERVE |
| M17 | March / Attack / Defense | Move groups through march states, attack/retreat/defend transitions and distance guards | M03 military region; `gl-march-type`, `gl-defend-town`, retreat state | DIRECT | PRESERVE |
| M18 | Civilian Protection / Local Defense | Detect attack centroid/local threat and move civilians/garrison/response | TC garrison, enemy-attack centroid and anti-scout regions; `gl-town-under-attack`, `enemy-attack-x/y` | DIRECT/COMPOSED | PRESERVE + Byzantine response policy |
| M19 | Raid Machine | Acquire economic targets, compute waypoints, move, attack, retreat and reset targets | Raid target corpus; `gl-raid-*`, waypoint goals, raid timers | DIRECT | PRESERVE |
| M20 | Siege Response | Recognize siege threat and produce/position siege response | QRAMS/QMANGOS and `gl-mangos-nearby` / ram progression | COMPOSED | PRESERVE; Byzantine unit substitutions |
| M21 | Scouting / Intelligence | Explore, acquire information, maintain scouting state and recover stuck scouts | QSCOUT and scout-control state; `NEWSCOUTING`, `gl-scout-stuck`, exploration coordinates | COMPOSED | PRESERVE topology; Byzantine policy may alter objectives |
| M22 | Agriculture / Food Transition | Manage farms/hunting/food infrastructure and transition constraints | QECONOMY/QBUILDINGS farm rules; rules 1795–1800; hunting/farm regions | DIRECT/COMPOSED | PRESERVE mechanism; Byzantine economy adapts |
| M23 | Recovery / Failsafe | Detect invalid/stalled paths, restore state/resources, bypass/re-enter and continue | `gl-failsafe`, `t-failsafe`, negative jumps, rollback/reconciliation rules | COMPOSED | PRESERVE distributed recovery |
| M24 | Reassessment / Re-entry | Re-read persistent state and re-enter applicable control regions after interruption, completion, failure or release | Distributed donor progression/re-entry patterns | COMPOSED | PRESERVE; do not centralize |
| M25 | Shared Strategic State | Coordinate military/economic/build/research state through shared goals and SNs | Shared goal namespace; `gl-feudal-strategy`, `gl-strategy`, `gl-current-group`, `gl-switch`, etc. | DIRECT/COMPOSED | PRESERVE ownership topology |
| M26 | Byzantine Policy Layer | State Byzantine-specific needs without replacing Shadow execution | No direct donor analogue; Byzantine extension | BYZANTINE-GENERALIZATION | ADD AFTER DONOR MACHINE |
| M27 | Verification / Qualification | Distinguish command, pending, feasibility and actual world-state completion | Donor world-state observers: building/unit/research counts and status predicates | COMPOSED | PRESERVE donor observer semantics; improve only with evidence |

---

# 3. Detailed model specifications

## M00 — Source Identity & Ordered Program

**Purpose:** The donor itself is the first model. Every reconstructed mechanism must remain traceable to an ordered source interval.

**Shadow reference:** `ShadowSource.per`; 1,956 `defrule` blocks; source-order matrix v0.3; `SourceRef`; `SourceShaRef`.

**Required implementation invariant:** no donor rule may be moved, merged, split, or semantically rewritten without recording the topology change.

**Output:** exact donor rule index with ordinal, line range, byte range, hash, reads/writes, actions, jump successor and semantic annotations.

**Status:** DIRECT / STATIC COMPLETE at corpus level; machine-field closure still being finalized.

---

## M01 — Initialization / Register Bootstrap

**Purpose:** Establish the initial state that makes later sequential regions deterministic.

**Shadow references:** opening QID/QGENERAL/QPOSITION regions; goal/timer initialization; `home-x=478`, `home-y=479`, `gl-position=46`, and shared state initialization.

**Required reconstruction:** preserve initialization order and writer precedence. Byzantine constants must not silently replace donor state carriers.

**Open evidence requirement:** exact donor rule ordinals should be linked mechanically from the atlas rather than inferred from region names.

---

## M02 — Sequential Control / Jump Machine

**Purpose:** This is the control-plane mechanism of Shadow. Rules are executable in source order; jumps bypass concrete regions and negative jumps create loops.

**Shadow references:** global `up-jump-rule` corpus; known QUNITS→QBUILDINGS crossings:

- QMANGOS emergency bypass → SIEGE-1.
- QARCHERS resource bypass → first QSKIRMS.
- QSKIRMS fewer-if-ahead `+2` → SPLIT-1.
- QSKIRMS fewer-if-enemy-castled `+1` → SPLIT-1.
- QSPEARS KRUSH bypass `+4` → QTOWERS.
- QSPEARS MESO bypass `+2` → Spear3.

**Design rule:** preserve jump destination, not merely intent.

**Failure mode:** replacing jumps with centralized priority dispatch destroys donor topology.

---

## M03 — Persistent State / Register Machine

**Purpose:** Goals/SNs/timers provide persistent AI-side memory across rule passes.

**Shadow references:** goals 1–317, 392, 478–479; major state carriers including `gl-current-build-item`, `gl-progression-pause`, `gl-escrow-state`, `gl-attacking`, `gl-current-group`, `gl-find-new-target`, `gl-raid-target-id`, `gl-defend-town`, `gl-failsafe`, `gl-march-type`, `gl-target-type`.

**Design rule:** numeric equality is not semantic aliasing. State must be typed by use, writer, reader and control region.

---

## M04 — Temporal Control

**Purpose:** Timers regulate cadence, retries, delays, target switching, attack behavior, scouting, housing, and failsafes.

**Shadow references:** timer corpus including `t-game-eval`, `ONE-MINUTE`, `TSA`, `hunting-timer`, `t-firing`, `t-command-delay`, `t-failsafe`, `t-target-switch`, `t-raid-waypoint-reevaluate`, `t-raid-retreat`, `t-build-delay`, `t-direction-switch`, `five-seconds-timer`, timer 46 TC dodging.

**Design rule:** temporal state is part of topology. A rule that appears statically reachable may remain temporally suppressed.

---

## M05 — Escrow / Reservation Machine

**Purpose:** Protect resources while an operation progresses through feasibility, commitment, execution and release.

**Shadow references:** 366 escrow/progression/command signal rules; 12 explicit reservation/modification rules; 70 release rules; 29 escrow-aware train/research command rules; `gl-escrow-state`; `up-modify-escrow`; `set-escrow-percentage`; `can-build-with-escrow`; `can-train-with-escrow`; `can-research-with-escrow`; `release-escrow`.

**Canonical topology:**

```text
resource policy
 → escrow mutation
 → escrow-aware feasibility
 → operation command
 → world-state observation
 → progression reconciliation
 → release/restoration
 → re-entry
```

**Critical distinction:** escrow mutation is not commitment confirmation; feasibility is not completion; command is not completion; release command is not proof of zero escrow.

---

## M06 — Progression Cursor Machine

**Purpose:** Track the current milestone and determine when the machine may advance.

**Shadow references:** `gl-current-build-item`, `gl-progression-pause`, `gl-build-progress`; QSTABLE/QMONASTERY and construction rules 1794–1896.

**Canonical construction sequence:**

```text
current item
 → selector / feasibility
 → escrow
 → search
 → placement
 → command
 → world-state observation
 → progress mutation
 → release/re-entry
```

**Rule:** progression must not advance from a command alone.

---

## M07 — Resource Arbitration

**Purpose:** Resolve resource competition while preserving protected requirements.

**Shadow references:** QECONOMY, construction farm/camp selectors, technology escrow families, production escrow paths.

**Byzantine adaptation:** Byzantine resource weighting may change policy, but the underlying reservation/commitment mechanism remains Shadow-derived.

---

## M08 — Search Machine

**Purpose:** Produce valid target/reference state for construction, raid, tactical and placement operations.

**Shadow references:** `up-find-local`, `up-find-remote`, `up-set-target-object`, target cleanup/removal, point extraction, search loops.

**Canonical search topology:**

```text
reset
 → configure filters
 → find local/remote
 → inspect
 → clean/remove
 → target object
 → extract point
 → set target point
```

**Rule:** no target is a search result state, not a construction failure and not a completion state.

---

## M09 — Placement Machine

**Purpose:** Translate search/reference state into engine placement state and managed build commands.

**Shadow references:** `place-normal`, `place-point`, `place-control`; `up-set-placement-data`; `sn-placement-zone-size`; `sn-placement-fail-delta`; `up-set-target-point`.

**Modes:** normal, point, control.

**Control placement:** `up-set-placement-data(player, object-type-or -1, distance)` followed by `up-build place-control`; `-1` denotes home-TC-relative placement in the recovered engine semantics.

**Rule:** placement retry does not advance construction progression.

---

## M10 — Construction Machine

**Purpose:** Execute building progression without confusing dispatch, pending state, placement, or world-state completion.

**Shadow references:** rules 1794–1800; rules 1890–1896; QBUILDINGS; QMARKET; QSTABLE; QMONASTERY.

**Representative direct anchors:**

- 1794: progression/placement guard and jump.
- 1795: farm selection.
- 1796: progression split.
- 1797: `up-build place-normal` farm.
- 1798: escrow-state reset/progression reset.
- 1799: farm selection.
- 1800: farm build.
- 1890–1896: mining-camp search/placement/progression/escrow/re-entry sequence.

**Completion authority:** donor building counts / world-state facts, not `up-build`, pending state, builder assignment or search success.

---

## M11 — Research Machine

**Purpose:** Reserve resources for technology, issue research, observe research completion and reconcile progression.

**Shadow references:** technology reservation families and `can-research-with-escrow`; research completion mutations in military state.

**Known reservation families:** Scale Mail, Chain Mail, Iron Casting KRUSH/FLUSH, Forging KRUSH/FLUSH, Chain Barding KRUSH/FLUSH, Scale Barding, Fletching, Leather Archer Armor, Padded Archer Armor.

**Design rule:** technology-specific escrow families remain tied to progression state; they are not independent global transactions.

---

## M12 — Production Machine

**Purpose:** Produce military/economic units through ordered production regions with resource and strategic guards.

**Shadow references:** QUNITS/QPRO; QMONKS, QMANGOS, QSCORPS, QRAMS, QSCOUTS, QKNIGHTS, QARCHERS, QSKIRMS, QMILITIAMAN, QSPEARS; `can-train-with-escrow`.

**Required reconstruction:** preserve production-region order and bypass edges.

---

## M13 — Production Preemption / Priority

**Purpose:** Override normal production sequencing when conditions warrant emergency or strategic preemption.

**Shadow references:** known QSKIRMS/QSPEARS/QARCHERS/QMANGOS positional jumps.

**Design rule:** preemption is distributed through jumps and rule ordering. Do not centralize it unless donor topology proves such a mechanism.

---

## M14 — Military Group Initialization

**Purpose:** Establish tactical group state and initial combat parameters.

**Shadow references:** military initialization region ~L1938–2064; `gl-current-group=RangedGroup`; `sn-number-tasked-units=40`; `gl-max-ranged-group-size=40`; `gl-range-advantage=0`; `gl-ranged-group-state=FIRING`; `gl-can-move`; `gl-can-fire`; tower/ranged/raid range state.

**Qualification:** exact rule ordinals must be attached from the generated atlas rather than estimated from line regions.

---

## M15 — Military Evaluation / Advantage

**Purpose:** Determine tactical state, fight advantage, movement eligibility and firing behavior.

**Shadow references:** QADVANTAGE; `gl-range-advantage`, `SUPERIORITY`, `gl-total-military-in-range`, `gl-army-damage-potential`, distance thresholds and ranged group state.

**Known behavior:** insufficient group size or excessive point distance can set evaluation state and jump into tactical processing.

---

## M16 — Target Acquisition / Search

**Purpose:** Acquire, store, reevaluate and replace military targets.

**Shadow references:** `gl-find-new-target`, `gl-target-hp`, `gl-last-target-player`, `gl-target-type`, raid target state, waypoint state, search loops.

**Design rule:** target identity is persistent state and must be explicitly invalidated/reset; stale targets are part of recovery topology.

---

## M17 — March / Attack / Defense

**Purpose:** Control movement and tactical transitions among march, attack, defense and retreat states.

**Shadow references:** `gl-march-type`, `gl-attacking`, `gl-defend-town`, `gl-ranged-retreat`, `gl-knight-retreat`, `gl-raid-retreat-type`, `retreat-now-goal`, `attack-status-goal`, `restart-attack-goal` where applicable to the donor state model.

**Design rule:** preserve threshold/state transitions rather than rewriting them as a generic combat controller.

---

## M18 — Civilian Protection / Local Defense

**Purpose:** Detect local enemy pressure and protect civilians/TC economy.

**Shadow references:** `gl-town-under-attack`, `enemy-attack-x/y`, `gl-enemy-attack-size`, `gl-enemies-in-town`, TC garrison and villager-retreat regions.

**Byzantine adaptation:** policy can alter response composition, but detection and local-response control mechanisms should remain donor-derived.

---

## M19 — Raid Machine

**Purpose:** Find economic targets, select routes, move raid groups, attack, retreat and reset targets.

**Shadow references:** lumber camps, mining camps, mills; `gl-raid-target-id`; `raid-waypoint1-x/y`; `raid-group-x/y`; `t-raid-waypoint-reevaluate`; `t-raid-retreat`; `t-raid-target-reset`.

**Design rule:** preserve target invalidation and waypoint reevaluation loops.

---

## M20 — Siege Response

**Purpose:** Recognize and respond to siege threats using production and tactical state.

**Shadow references:** QRAMS/QMANGOS; `gl-mangos-nearby`; ram train/re-entry sequence; siege emergency branches.

**Canonical ram pattern:** stop → split → escrow changes/release → siege state → escrow-aware train → train → observed ram count → progression/re-entry.

---

## M21 — Scouting / Intelligence

**Purpose:** Explore, identify enemy state, maintain scout movement and recover stalled scouting.

**Shadow references:** QSCOUT; `NEWSCOUTING`; `gl-scout-stuck`; `saved-scout-x/y`; `explo-x/y`; `gl-scouting-switch`; exploration timers.

**Design rule:** preserve exploration/search geometry and recovery loops before changing scouting policy.

---

## M22 — Agriculture / Food Transition

**Purpose:** Sustain food production and transition from hunt/forage to farms while respecting construction/resource constraints.

**Shadow references:** farm rules 1795–1800, hunting/forage/deer/boar/farm regions.

**Design rule:** food-transition behavior must be reconstructed from actual donor selector/progression logic; do not treat farm construction as an isolated economic module.

---

## M23 — Recovery / Failsafe

**Purpose:** Restore the machine when a command, search, placement, target, resource or progression path does not produce the expected state.

**Shadow references:** `gl-failsafe`, `t-failsafe`, negative jumps, progression rollback/reconciliation, target resets, resource restoration and bypass rules.

**Design rule:** recovery remains distributed. A central recovery manager would be an architectural change requiring direct donor evidence.

---

## M24 — Reassessment / Re-entry

**Purpose:** Re-enter normal machine processing after interruption, completion, failed feasibility, stale search state or released escrow.

**Shadow references:** repeated current-item checks, progress mutation, negative jumps, release/re-entry sequences across QBUILDINGS/QUNITS/QRESEARCH.

**Design rule:** re-entry is not an RPC-style response. It is continued evaluation of persistent state through the ordered rule stream.

---

## M25 — Shared Strategic State

**Purpose:** Permit otherwise separate control regions to communicate through common persistent state.

**Shadow references:** `gl-strategy`, `gl-feudal-strategy`, `gl-switch`, `gl-current-group`, `gl-current-build-item`, shared tactical and production goals.

**Design rule:** every shared state carrier requires a writer/reader ledger. A proposed single-owner abstraction is an AEGIS generalization unless donor topology proves it.

---

## M26 — Byzantine Policy Layer

**Purpose:** Encode Byzantine requirements: unit composition, infrastructure priorities, economic preferences, technology choices and emergency responses.

**Donor reference:** no direct Shadow analogue for Byzantine-specific policy.

**Evidence:** BYZANTINE-GENERALIZATION.

**Boundary:** policy chooses objectives/requirements; Shadow-derived machine mechanisms perform feasibility, reservation, sequencing, execution and verification.

**Constraint:** policy must not silently become a replacement transaction orchestrator.

---

## M27 — Verification / Qualification

**Purpose:** Close the distinction between intent, command, pending state and actual world state.

**Shadow references:** `building-type-count-total`, `unit-type-count`, research completion predicates/status, observed production/building state.

**Canonical state model:**

```text
intent
 → feasibility
 → reservation
 → command
 → pending / intermediate state
 → world-state observation
 → progression mutation
```

**Rule:** only the appropriate world-state observer may advance completion.

---

# 4. Construction / placement integrated model

Construction and placement are separate mechanisms but form one distributed donor control path.

```text
Construction objective
    ↓
current-build-item
    ↓
feasibility / escrow
    ↓
search
    ↓
target / point
    ↓
placement mode
    ↓
up-build
    ↓
pending / retry state
    ↓
world-state completion
    ↓
progression mutation
    ↓
release / re-entry
```

### Direct donor anchors

Rules **1794–1800** and **1890–1896** are mandatory anchor ranges for reconstruction. They must be linked to exact byte offsets by the machine-generated atlas.

### ABI invariants

- `up-build` is dispatch/action, not synchronous completion.
- `up-assign-builders` is assignment, not completion.
- search failure is not construction failure.
- placement failure is not construction failure.
- pending state is not world completion.
- progression does not advance merely because a command was issued.

---

# 5. Escrow integrated model

The escrow machine must be reconstructed as a graph, not as a utility function.

```text
                ┌───────────────┐
                │ policy / need │
                └───────┬───────┘
                        ↓
              resource feasibility
                        ↓
                escrow mutation
                        ↓
              escrow observation
                        ↓
              escrow-aware `can-*`
                        ↓
                   command
                        ↓
              world-state observer
                        ↓
                progression state
                        ↓
                release/restoration
                        ↓
                   re-entry
```

### Donor references

- `gl-escrow-state`
- `up-modify-escrow`
- `set-escrow-percentage`
- `can-build-with-escrow`
- `can-train-with-escrow`
- `can-research-with-escrow`
- `release-escrow`
- `gl-current-build-item`
- `gl-progression-pause`
- `gl-build-progress`

### Critical implementation rule

Do not replace the donor's distributed escrow/progression topology with a centralized transaction service. Any AEGIS transaction representation remains an improvement/generalization until a donor-equivalence mapping proves otherwise.

---

# 6. Production and preemption model

Production is not merely “choose unit X.” The donor contains ordered unit regions with branch bypasses that materially change which rules execute.

```text
strategic condition
   ↓
unit objective
   ↓
resource / composition test
   ↓
normal production region
   │
   ├── preemption jump ──→ emergency / alternate region
   │
   └── fall-through ─────→ next normal rule
```

### Required donor-preservation edges

At minimum the reconstruction must preserve the known QUNITS→QBUILDINGS jump topology listed under M02. The exact rule ordinals and source offsets are to be populated from the atlas rather than estimated.

### Byzantine adaptation

Byzantine policy may choose Spearman, Skirmisher, Archer, Knight, Camel, Siege or other civilization-valid objectives, but the mechanism that arbitrates, reserves, executes and verifies those objectives should remain structurally Shadow-derived.

---

# 7. Military model

The military machine is a set of interacting state regions rather than a single combat controller.

```text
initialize group
   ↓
evaluate capability / advantage
   ↓
acquire target
   ↓
choose march / attack / defend
   ↓
move / fire
   ↓
observe local tactical state
   ↓
retreat / retarget / reinforce / re-enter
```

### Core donor state carriers

`gl-current-group`, `gl-max-ranged-group-size`, `gl-range-advantage`, `gl-ranged-group-state`, `gl-can-move`, `gl-can-fire`, `gl-attack-efficiency`, `gl-defend-town`, `gl-ranged-retreat`, `gl-knight-eval`, `gl-knight-retreat`, `gl-enemy-attack-size`, `gl-enemies-in-town`, `gl-cavalry-in-town`, `gl-enemy-archers`, `gl-enemy-skirms-nearby`, `gl-total-military-in-range`, `gl-army-damage-potential`.

### Research→military coupling

The donor mutates military state when technologies complete, e.g. fletching/bodkin/elite skirmisher effects. This coupling must be preserved because it demonstrates that research completion is an input into the military state machine rather than an isolated technology subsystem.

---

# 8. Scouting / intelligence model

Scouting is persistent state plus search/geometry plus recovery.

```text
scout assignment
 → exploration state
 → search / movement geometry
 → information acquisition
 → target/state write
 → reassessment
 → stuck/recovery path
```

Donor references include QSCOUT, `NEWSCOUTING`, `gl-scout-stuck`, saved scout coordinates, exploration coordinates and scouting timers.

The Byzantine version should alter what information is strategically important only after the donor scouting mechanism is faithfully recovered.

---

# 9. Recovery model

Recovery is explicitly **distributed**.

A failed operation may cause:

- retained progression cursor;
- cleared or changed target state;
- escrow release/restoration;
- jump to an alternate branch;
- timer suppression/reset;
- re-evaluation;
- re-entry into the relevant source region.

The reconstruction must therefore search for recovery edges around every important command rather than implementing one universal recovery routine.

---

# 10. Byzantine adaptation model

Byzantine-specific policy is downstream of donor reconstruction.

### Policy responsibilities

- determine desired composition;
- identify infrastructure requirements;
- identify technology requirements;
- recognize Byzantine-specific tactical opportunities;
- define emergency priorities;
- supply objectives to Shadow-derived production/construction/research mechanisms.

### Mechanism responsibilities

- source-order arbitration;
- persistent state;
- escrow;
- feasibility;
- search;
- placement;
- command issuance;
- world-state verification;
- progression;
- preemption;
- recovery;
- re-entry.

### Hard boundary

A Byzantine policy rule must not become a hidden replacement for the Shadow machine merely because it is easier to code.

---

# 11. Improvements model

Improvements are permitted only after a donor mechanism is established.

Every improvement must record:

```text
DONOR BASELINE
    ↓
OBSERVED LIMITATION
    ↓
HYPOTHESIS
    ↓
MODIFIED MECHANISM
    ↓
EXPECTED EFFECT
    ↓
STATIC CHECK
    ↓
RUNTIME CHECK
    ↓
REPLAY RESULT
    ↓
REGRESSION RESULT
```

Examples of legitimate improvement candidates include:

- stronger Byzantine composition arbitration;
- improved economic transition policy;
- better threat classification;
- improved target scoring;
- explicit verification where donor behavior is ambiguous;
- Byzantine-specific emergency branches.

These must remain labeled as improvements rather than being attributed to Shadow.

---

# 12. Runtime topology target

The current runtime entrypoint and nested `ShadowByzantine/ShadowByzantine.per` orchestrator are **not accepted as donor architecture**.

Current runtime path:

```text
ShadowByzantine.per
    ↓
ShadowByzantine/ShadowByzantine.per
    ↓
01_constants
01b_byz_constants
02_state
03_economy
04_construction
16_pass1_transaction
```

The nested orchestrator is an architecture-review item because no direct Shadow analogue has yet been demonstrated.

### Target architecture

The eventual runtime should be expressed as ordered `.per` regions whose source order and jump topology correspond to the reconstructed machine. A packaging/load boundary is acceptable only insofar as it does not introduce an additional strategic control layer.

The exact final file partition is subordinate to the donor control topology.

---

# 13. Pass-1 transaction kernel disposition

`16_pass1_transaction.per` is retained as a controlled experimental vertical slice.

Its lifecycle is:

```text
objective
 → capital feasibility
 → escrow mutation
 → escrow observation
 → authority
 → baseline
 → can-train / train
 → world verification
 → release request
 → release
 → release observation
 → idle
```

This is useful as an engineering qualification harness, but it must not be retroactively represented as a literal Shadow subsystem.

**Evidence class:** DONOR-MECHANISM-DERIVED + BYZANTINE-GENERALIZATION + ENGINEERING EXPERIMENT.

---

# 14. Required machine-index fields

The canonical machine index must eventually expose for every one of the 1,956 donor rules:

```text
ordinal
source_line_start
source_line_end
source_byte_start
source_byte_end
raw_rule_sha256
region
predicates
reads_goals
writes_goals
reads_strategic_numbers
writes_strategic_numbers
reads_timers
writes_timers
actions
engine_commands
jump_delta
jump_destination
fallthrough_destination
disable_self
escrow_feasibility
escrow_mutation
escrow_release
search_operations
placement_operations
completion_observers
semantic_tags
```

The existing `forensics_shadow_rule_atlas.py` and `SHADOW_SOURCE_ORDER_MATRIX_v0.3` should be reconciled to provide this data. Do not create another independent atlas format.

---

# 15. Donor → ShadowByzantine implementation matrix

Every implementation region must eventually receive one of these dispositions:

- **PRESERVED** — topology/mechanism materially retained.
- **ADAPTED** — donor mechanism retained with Byzantine-specific inputs.
- **MOVED** — source region relocated; original and new topology both recorded.
- **CHANGED** — mechanism altered; reason and evidence required.
- **ADDED** — no donor analogue; must be labeled Byzantine-generalization or improvement.
- **LOST** — donor mechanism not yet reconstructed.
- **UNKNOWN** — insufficient evidence.

No `ADDED`, `CHANGED`, or `MOVED` classification may be silently presented as Shadow reconstruction.

---

# 16. Implementation sequence

## Gate A — Source closure

- verify canonical SHA chain;
- reconcile 1,956 rule ordinals;
- reconcile exact byte offsets;
- reconcile source-order matrix and rule atlas.

## Gate B — Machine closure

- complete state reader/writer graph;
- complete jump graph;
- complete escrow graph;
- complete search/placement graph;
- complete progression graph;
- identify completion observers;
- identify distributed recovery/re-entry edges.

## Gate C — Donor reconstruction

Reconstruct coherent regions in donor order, beginning with state/control/escrow/progression and then construction/research/production/military/scouting.

## Gate D — Topology diff

Audit current ShadowByzantine against donor and classify every meaningful mechanism as preserved/adapted/moved/changed/added/lost/unknown.

## Gate E — Architecture veto

Reassess the nested orchestrator against direct donor analogue, state-writer, jump, escrow, search, progression and engine-semantics tests.

## Gate F — Byzantine adaptation

Introduce Byzantine policy only after the donor mechanisms it feeds are reconstructed.

## Gate G — Improvement

Modify only with explicit baseline/limitation/hypothesis/qualification records.

## Gate H — Runtime qualification

```text
STATIC
   ↓
RUNTIME-CANDIDATE
   ↓
RUNTIME-QUALIFIED
   ↘
    RUNTIME-QUALIFIED-CONDITIONAL
```

---

# 17. Current gaps that block a claim of “fully reconstructed”

1. Exact machine-index field closure for all 1,956 rules.
2. Complete state reader/writer graph, especially strategic-number and timer readers.
3. Complete jump destination graph linked to exact rule ordinals.
4. Complete donor search/placement graph.
5. Complete donor completion-observer inventory.
6. Full donor→ShadowByzantine topology diff.
7. Runtime qualification of donor-derived behavior.
8. Architecture decision on the nested runtime orchestrator.
9. Reconciliation of stale historical documents whose former `UNRECOVERED` claims have been superseded by later source extraction.

These are finite forensic/engineering gates, not invitations to create more conceptual paperwork.

---

# 18. Definition of done

The ShadowByzantine machine is considered fully designed when:

1. every donor rule is machine-indexed;
2. every relevant state carrier has known readers/writers or an explicit UNKNOWN classification;
3. every jump has a verified destination;
4. every escrow operation belongs to a documented dependency chain;
5. construction/research/production operations have verified completion observers;
6. search and placement state are represented without conflating failure modes;
7. recovery and re-entry edges are identified;
8. ShadowByzantine has a complete donor topology diff;
9. every Byzantine addition is separately attributed;
10. the runtime load graph contains no unexplained control layer;
11. runtime qualification distinguishes command, pending, and world-state completion;
12. improvements are measurable against a reconstructed donor baseline.

---

# 19. Immediate implementation directive

**Do not create another architecture document.**

The next work should update the existing forensic machinery and this blueprint as the machine-index closes.

The highest-value engineering operation is:

```text
existing rule atlas generator
        +
existing source-order matrix
        +
existing escrow/control-flow evidence
        ↓
ONE reconciled donor machine index
        ↓
ONE donor → ShadowByzantine topology diff
        ↓
implementation
```

The repository is now sufficiently documented to move from conceptual architecture into exact machine reconstruction. The blueprint therefore treats the donor source, forensic extraction, and runtime qualification as one evidence chain rather than independent documentation projects.
