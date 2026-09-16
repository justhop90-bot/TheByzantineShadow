# ShadowSource Military–Production Boundary Atlas v0.1

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per` on `main`  
**Canonical source SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Purpose:** forensic mapping of the interface between Shadow's military/tactical control machine and its production/composition machinery.

## 0. Executive finding

The Military–Production boundary in Shadow is **not a clean call boundary and not a single source interval**. It is a shared-state/control-flow interface. Military continuously publishes battlefield-derived requirements and posture into persistent goals and coordinates; production consumes those conditions to determine what can/should be produced, while production-side state feeds back into military evaluation through observed army size, composition, upgrades, group state, and capability.

The correct reconstruction unit is therefore the **boundary closure**, not a thin `military.per -> production.per` API.

The canonical machine has this form:

```text
MILITARY OBSERVATION
   |
   +--> enemy-group-size
   +--> units-in-range
   +--> cavalry/melee/military telemetry
   +--> enemy composition / target geometry
   +--> tactical posture
   |
   v
MILITARY EVALUATION / POSTURE
   |
   +--> gl-ranged-eval
   +--> gl-ranged-group-size
   +--> gl-enemy-group-size
   +--> gl-ranged-group-range
   +--> gl-march-type
   +--> gl-defend-town
   +--> threat / target coordinates
   |
   v
PRODUCTION / TECHNOLOGY DEMAND
   |
   +--> unit availability / composition
   +--> technology completion
   +--> army-capability changes
   |
   v
MILITARY RE-EVALUATION
```

This is a **feedback loop**, not a one-way dependency.

## 1. Canonical evidence basis

The source establishes a large tactical initialization and ranged-control neighborhood beginning around rules 14–27 and continuing through the ranged evaluation/search machinery. The source explicitly initializes and mutates persistent tactical goals such as `gl-current-group`, `gl-defend-town`, `gl-ranged-group-state`, `gl-can-move`, `gl-can-fire`, `gl-ranged-group-range`, `gl-raid-group-range`, `gl-march-type`, and `gl-close-ranged-group-range`. It also changes those values in response to completed technologies such as Fletching, Bodkin Arrow, and Elite Skirmisher. This demonstrates a direct Technology/Production → Military state edge. 

Representative canonical evidence:

- `research-completed ri-fletching` increases tracking/range variables and modifies `gl-ranged-group-range`, `gl-raid-group-range`, and close-range thresholds.
- `research-completed ri-bodkin-arrow` performs a similar capability update.
- `research-completed ri-elite-skirmisher` increases tracking range.
- Military evaluation consumes `gl-army-damage-potential`, `gl-ranged-group-size`, `gl-enemy-group-size`, armor/range advantage, nearby towers, and other battlefield-derived state.
- The military search machine repeatedly iterates `sn-focus-player-number` across valid enemy players using negative jump edges.

The source window around the ranged machinery shows these state mutations and evaluations directly. [Canonical `ShadowSource.per`](https://github.com/justhop90-bot/TheByzantineShadow/blob/main/ShadowSource.per)

## 2. Boundary regions

### B01 — Military capability publication

**Approximate source window:** rules 14–27 onward; exact outer boundary is distributed/provisional.  
**Status:** DIRECT for recovered rules; outer boundary PROVISIONAL.

Military initializes the persistent tactical state used by subsequent control. Important writes include:

- `gl-defend-town`
- `gl-current-group`
- `gl-max-ranged-group-size`
- `gl-range-advantage`
- `gl-ranged-group-state`
- `gl-can-move`
- `gl-can-fire`
- `gl-raid-can-fire`
- `gl-enemy-tower-range`
- `gl-my-tower-range`
- `gl-ranged-group-range`
- `gl-raid-group-range`
- `gl-march-type`
- `gl-close-ranged-group-range`

These are persistent machine variables, not transient procedure parameters.

### B02 — Production-sensitive military evaluation

**Approximate source window:** ranged evaluation/search region beginning immediately after QADVANTAGE and extending through enemy composition/range/size calculations; approximately L2058–4300 in the recovered atlas.  
**Status:** DIRECT for recovered windows; outer boundary PROVISIONAL.

Military evaluates battlefield conditions using:

- `gl-enemy-group-size`
- `gl-ranged-group-size`
- `gl-army-damage-potential`
- `gl-ranged-eval`
- `gl-range-advantage`
- `gl-armor-advantage`
- `gl-mangos-nearby`
- `gl-units-in-close-range`
- `gl-total-units-in-range`
- `gl-total-military-in-range`
- `gl-cavalry-attacking`
- tower counts/ranges
- enemy unit types and local geometry.

This region is where military converts observed composition into tactical valuation. It is therefore a primary **consumer of production state** and a producer of production-relevant pressure.

### B03 — Technology/composition feedback

The military region reads research completion as an observed capability transition. Fletching and Bodkin alter effective ranges; Elite Skirmisher alters tracking. The important point is semantic: **research completion is not merely an economic event; it mutates the military capability model.**

Therefore a reconstruction that isolates technology/production from military must expose completion observations back into the military state machine.

### B04 — Army-size/composition feedback

The military machine uses observed own-group size and enemy-group size in `gl-ranged-eval`. For example, the source directly adds `gl-ranged-group-size` and subtracts `gl-enemy-group-size` from evaluation. This makes produced-unit completion observable to military even when no explicit `production -> military` procedure exists.

The boundary is therefore partly **observation-based** rather than command-based.

### B05 — Military-to-production demand interface

The donor source's tactical state is capable of determining when additional military capability is required, but the exact outer production dispatcher is distributed elsewhere in the 22,604-line source. Consequently, this atlas does **not** invent a single `produce-unit` rule or claim a nonexistent API.

The defensible interface is:

```text
battlefield observation
 -> tactical classification/evaluation
 -> persistent military state
 -> production-relevant deficit/capability condition
 -> production arbitration
 -> engine training/build action
 -> observed unit/technology completion
 -> military capability update
```

Where the exact production writer/consumer is not yet recovered, it is marked PROVISIONAL rather than fabricated.

## 3. Shared persistent state

| State | Military role | Production/technology role | Boundary semantics |
|---|---|---|---|
| `gl-ranged-group-size` | Own combat mass | Indirect result of produced units | Completion-observed feedback |
| `gl-enemy-group-size` | Threat/composition input | Can create production pressure | Military publication |
| `gl-ranged-eval` | Tactical decision metric | Can indicate capability deficit | Evaluation output |
| `gl-army-damage-potential` | Combat capability | Depends on actual army composition | Capability feedback |
| `gl-range-advantage` | Tactical matchup | Influenced by ranged composition/tech | Capability feedback |
| `gl-armor-advantage` | Tactical matchup | Influenced by unit composition | Capability feedback |
| `gl-ranged-group-range` | Engagement envelope | Modified by completed tech | Tech completion edge |
| `gl-close-ranged-group-range` | Local threat envelope | Modified by completed tech | Tech completion edge |
| `gl-tracking-range` | Observation envelope | Modified by tech | Tech completion edge |
| `gl-current-group` | Selects tactical group | Production determines available groups indirectly | Shared selector |
| `gl-defend-town` | Posture/arbitration | Production is subordinate to posture indirectly | Cross-region control |
| `gl-march-type` | Movement posture | Depends on army state | Shared tactical state |
| `gl-can-move` / `gl-can-fire` | Execution gating | Can suppress/alter tactical employment | Control-state interface |
| `gl-raid-can-fire` | Raid execution state | Composition-dependent | Cross-region capability |
| enemy/own unit counts | Combat model | Production result/requirements | Observation substrate |
| research completion | Capability mutation | Production/tech result | Completion edge |
| target/group coordinates | Tactical target | May influence production posture | Context publication |

## 4. Jump closure at the boundary

The military region is a sequential/reactive machine. Jump edges are therefore part of the boundary semantics.

### J01 — QADVANTAGE bypass

When the ranged group is absent or the group is sufficiently far from the enemy group, the source sets `gl-ranged-eval` to `WinningFight` and performs `up-jump-rule 44`. This is a control-flow bypass, not merely an optimization. It prevents the subsequent detailed evaluation block from executing under that condition.

### J02 — Enemy-player search loops

Military searches repeatedly increment `sn-focus-player-number` and use negative jumps (`up-jump-rule -2` and related offsets) to iterate through valid enemy players. These loops must remain intact when reconstructing the region; flattening them into a generic query changes execution semantics.

### J03 — Group/mode bypasses

The military source uses positive jumps to bypass tactical blocks when group size, enemy building presence, or tactical preconditions make a block irrelevant. These bypasses define the effective priority of neighboring rule clusters.

### J04 — Cross-region continuation

At the end of a military neighborhood, source-order continuation can enter non-military machinery without an explicit call. Consequently, reconstruction must preserve either canonical ordering or an explicitly equivalent dispatch mechanism. A module boundary cannot be treated as a hard execution barrier.

## 5. Engine commands crossing the boundary

The following command families are boundary-relevant:

### Military → engine

- `up-target-objects`
- `up-target-point`
- `up-target-point ... action-*`
- `up-set-target-object`
- `up-set-target-by-id`
- `up-full-reset-search`
- `up-filter-distance`
- `up-filter-include`
- `up-find-remote`
- `up-find-local`
- `up-find-status-remote`
- `up-clean-search`
- `up-remove-objects`
- `up-get-search-state`
- `up-get-point`
- `up-copy-point`
- `up-lerp-tiles`
- `up-cross-tiles`
- `up-ungarrison`

These are not production commands, but they consume or mutate the same persistent state that production depends upon.

### Production/technology → engine

The exact complete production command closure remains to be exhaustively recovered from the full source. The boundary atlas therefore deliberately does not assert an exact donor production command list beyond commands directly recovered elsewhere in the Shadow machine.

The important interface rule is: **engine command issuance is not completion.** A military-visible production result must be established from an observation such as unit-type count or research completion, not from the issuance of a training/research command.

## 6. Completion observations

The Military–Production boundary has three classes of completion evidence:

### C01 — Unit completion

Observed own unit/group counts are the authoritative downstream evidence that production changed the military population. The source uses group size and unit-type observations as live state rather than treating an order as completion.

### C02 — Technology completion

`research-completed` predicates directly mutate military range/tracking state. These are explicit completion observers.

### C03 — Tactical capability completion

Derived values such as `gl-army-damage-potential`, range advantage, armor advantage, and group size are secondary observations. They represent capability after underlying units/technology exist.

No rule should promote a production command into a completed military capability without one of these downstream observations.

## 7. Recovery and re-entry

Shadow does not present a centralized transaction-style recovery manager at this boundary. Recovery is distributed through ordinary reactive rules:

1. tactical state is recalculated from current observations;
2. invalid/empty searches are bypassed or looped to the next player;
3. group size and enemy composition are re-read;
4. military evaluation is recomputed;
5. posture/target commands are reissued when conditions remain true;
6. production-side changes become visible through subsequent unit/technology observations.

This is **reactive recovery**, not a centralized `RECOVERY` state.

That distinction matters for ShadowByzantine: the analytical transaction FSM may be useful for testing, but it should not be mistaken for the donor's implementation model.

## 8. Cross-region handoffs

### H01 — Military → Production

```text
Enemy observation
→ enemy composition / threat aggregate
→ military evaluation
→ capability deficit / tactical requirement
→ production-side arbitration
```

Evidence strength: COMPOSED/INFERRED where the exact production writer is outside the recovered boundary window; DIRECT for the military observations themselves.

### H02 — Production → Military

```text
unit/research completion
→ observed capability
→ group size / range / damage potential
→ gl-ranged-eval / tactical posture
```

Evidence strength: DIRECT for technology completion and military-state mutation; DIRECT/COMPOSED for unit-count-to-group-capability propagation.

### H03 — Military → Defense

Military posture writes/reads `gl-defend-town`, retreat/garrison state, enemy attack coordinates, and related threat values. The defense region can therefore preempt ordinary production/military employment.

### H04 — Military → Construction/Economy

Threat state and tactical location affect protection/retreat behavior and can change the economic environment in which production operates. This is a control dependency rather than a clean data API.

### H05 — Technology → Military

Explicit completion observers for Fletching, Bodkin Arrow, and Elite Skirmisher update range/tracking values. This is one of the clearest hard boundary edges in the source.

## 9. Boundary contract for reconstruction

The faithful Shadow reconstruction should expose the following conceptual contract without pretending the donor had an API:

```text
MILITARY PUBLISHES:
  enemy composition
  own composition/group size
  tactical evaluation
  posture
  target geometry
  capability deficits

PRODUCTION/TECHNOLOGY PUBLISHES:
  observed unit counts
  observed technology completion
  capability-affecting upgrades

SHARED:
  persistent goals
  strategic numbers
  coordinates
  group identity
  timers
  source-order/jump control

ENGINE:
  searches
  target commands
  movement/attack/garrison commands
  production/research/build commands

VERIFICATION:
  world-state observations only
```

## 10. Reconstruction consequence

Do **not** implement this boundary as:

```text
Military module -> Production API -> unit trainer
```

That would erase the donor's defining behavior: persistent shared state, source-order dispatch, negative-jump iteration, reactive re-evaluation, and capability feedback.

The better reconstruction is:

```text
                  +----------------------+
                  |   PERSISTENT STATE   |
                  +----------+-----------+
                             |
            +----------------+----------------+
            |                                 |
      MILITARY REGION                  PRODUCTION REGION
            |                                 |
            | battlefield                    | units/tech
            v                                 v
      evaluation/posture  <------------ capability
            |                                 |
            +------------ feedback -----------+
                             |
                         ENGINE
```

The production region can therefore be transplanted as a coherent machine, but its military interface must preserve the shared-state and completion-observation closure documented here.

## 11. Evidence gaps deliberately retained

1. Exact outer source boundaries of the complete production dispatcher remain to be exhaustively segmented.
2. Exact writer matrix for every production target is not asserted here.
3. Exact production command/release closure is not inferred from military observations.
4. Source-order continuation across every military/production transition still requires complete jump-graph extraction.
5. Runtime firing and completion remain unqualified by this static atlas.

These are evidence gaps, not implementation assumptions.

## 12. Bottom line

The Military–Production boundary is best understood as a **bidirectional capability-control interface embedded in Shadow's persistent sequential machine**. Military publishes battlefield pressure and tactical capability requirements; production changes the physical army; technology completion changes combat envelopes; military observes those changes and recomputes evaluation.

The boundary's essential invariant is:

```text
OBSERVE → CLASSIFY → PERSIST STATE → PRODUCTION/TECH EFFECT
→ OBSERVE ACTUAL RESULT → UPDATE MILITARY CAPABILITY
→ RE-EVALUATE → RE-ENTER CONTROL FLOW
```

That invariant is a forensic reconstruction aid, not a claim that Shadow literally implemented those stages as named modules.
