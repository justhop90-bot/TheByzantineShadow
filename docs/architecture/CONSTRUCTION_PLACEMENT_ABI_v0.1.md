# Construction ↔ Placement ABI v0.1

## Status

**DESIGN-READY / ENGINE-SEMANTICS-TRIANGULATED / NOT RUNTIME-QUALIFIED.**

This artifact is the authoritative Construction↔Placement contract. It consolidates the prior contract and its interface questions rather than creating a new ABI document.

Evidence hierarchy: canonical `ShadowSource.per` → preserved provenance → AI Reference / engine patch semantics → project reconstruction. Architectural ownership below is **COMPOSED/INFERRED** unless explicitly marked DIRECT.

## 1. Boundary

```text
Strategy/Policy
    ↓ WHY
Construction
    ↓ WHAT / WHEN / progression / authorization
Placement
    ↓ WHERE / placement mode / target / placement configuration
Execution
    ↓ HOW the engine command is issued
World / Verification
    ↓ WHETHER the requested world state exists
Construction
    ↓ reconcile / advance / recover / re-enter
```

The boundary is architectural. Shadow itself is a rule machine, not a set of source-level modules.

## 2. Authoritative State

### Construction owns

- current build item (`gl-current-build-item` family);
- progression cursor (`gl-build-progress` family);
- progression pause/interruption state (`gl-progression-pause` family);
- construction-local arbitration (`SPLIT` and equivalent local state);
- milestone selection, rollback/reconciliation, and advancement;
- dispatch eligibility.

### Placement owns

- placement mode selection at the dispatch boundary;
- target-object / target-point handoff state;
- search state used to resolve targets;
- placement-data configuration required by the selected placement mode;
- placement retry/re-entry state.

### Execution owns

- `build` / `up-build` invocation;
- `up-assign-builders` invocation;
- engine-side construction dispatch.

### Verification owns

- observation of pending state;
- observation of actual world objects/counts/properties;
- classification of completion versus non-completion;
- completion evidence returned to Construction.

### Escrow owns

- resource reservation/accounting and release operations.

Placement and Construction must not silently absorb Escrow or Verification authority.

## 3. Engine-Semantics Resolution Matrix

| Former OPEN question | Resolution | Evidence | Status |
|---|---|---|---|
| `up-build` ABI | `up-build PlacementType EscrowState BuildingId` is an **action** that adds a building to the construction queue. Placement type selects the engine placement mechanism; escrow state selects resource accounting. It is not a synchronous completion return. | Shadow + AI Reference/UP notes | **RESOLVED** |
| `up-assign-builders` ABI | `(up-assign-builders type/class number)` assigns **at least the specified number of builders** to a building type/class; it is an action/configuration operation, not completion. | AI Reference/UP notes + Shadow invocation | **RESOLVED** |
| empty search | `up-find-local` / `up-find-remote` return **false when used as Facts if the search produces zero results**. Search lists and counts are separate engine state; `up-get-search-state` exposes local/remote result counts and additions. | AI Reference/UP notes | **RESOLVED** |
| target-object selection | `up-set-target-object` selects an object from the current search list; as a Fact it returns false if the requested index cannot be set. Target state is engine search/target state, not completion state. | AI Reference/UP notes | **RESOLVED** |
| target lifetime | The engine maintains search/target state until it is changed/reset by subsequent search/target operations. Shadow explicitly rebuilds this state through reset → search → clean/remove → target selection. No donor evidence supports treating the target as a one-shot return value. | Shadow + AI Reference | **RESOLVED-CONDITIONAL** |
| `place-control` | `up-set-placement-data(player, object-type-or -1, distance)` supplies placement reference data for subsequent `up-build place-control`; the reference is the latest specified object for the player, with `-1` meaning home TC, and relative distance may be positive/negative. Relative placement uses the target player's location or map center if the target reference is unavailable. | Shadow + AI Reference/UP notes | **RESOLVED** |
| placement zone/failure | `sn-placement-zone-size` controls the initial placement zone stored with a successful build call; controlled placement can expand on failed placement attempts. `sn-placement-fail-delta` modifies placement distance on failure for control placement. | AI Reference/UP notes | **RESOLVED** |
| point placement | `place-point` uses the point established by `up-set-target-point`; its stored zone size controls initial placement zone and it expands on failed attempts. It does not use `up-set-placement-data` or `sn-placement-fail-delta`. | AI Reference/UP notes | **RESOLVED** |
| pending placement | `up-pending-placement` reports while the managed placement system is trying to place a building; documentation explicitly warns that mills/camps use a different placement system. | AI Reference/UP notes | **RESOLVED-CONDITIONAL** |
| pending objects | `up-pending-objects` compares pending train/build count. It is an observation of work not yet completed, not completion evidence. | AI Reference/UP notes | **RESOLVED** |
| placement failure | The engine retries managed placement internally across passes, expanding the relevant placement zone according to its placement mode/configuration. AI-side rules must not equate a dispatch call with success. | AI Reference/UP notes | **RESOLVED** |
| builder lifecycle | `up-assign-builders` sets an assignment policy (“at least N builders” for a type/class); it does not expose a donor-specific completion acknowledgement. Actual building completion remains world-state observation. | AI Reference/UP notes + Shadow | **RESOLVED** |

## 4. Placement Modes

### NORMAL

`up-build place-normal ...` invokes ordinary building placement. No target point or placement-data reference is implied by the command itself.

### POINT

`up-build place-point ...` uses the target point previously established with `up-set-target-point`. Shadow's mining-camp paths demonstrate the stateful sequence:

```text
search resource
→ select target object
→ obtain point
→ set target point
→ set placement parameters where required
→ dispatch place-point
```

### CONTROL

`up-build place-control ...` uses placement data established by `up-set-placement-data`.

Shadow provides direct examples for towers and extra stables:

```text
up-set-placement-data ...
set sn-placement-zone-size
up-build place-control ...
```

The target/reference data therefore belongs to the placement dispatch state, not to a generic search-result abstraction.

## 5. Placement Configuration Ownership

Shadow directly writes placement configuration immediately before dispatch, including:

- `sn-placement-zone-size`;
- `sn-placement-fail-delta`;
- `sn-allow-adjacent-dropsites`;
- `sn-dropsite-separation-distance`.

Therefore the earlier assumption that all geometry/failure policy is merely external input is **rejected**.

The safer contract is:

```text
Construction selects the construction milestone.
Placement materializes the placement state/configuration required by that donor path.
Execution consumes that prepared state.
```

Some placement strategic numbers may remain shared policy inputs, but their mutation at the dispatch boundary is Placement-side behavior and must not be hidden from the ABI.

## 6. Search Contract

The direct-targeting/search engine is stateful:

```text
up-full-reset-search
→ configure filters
→ up-find-local / up-find-remote
→ inspect result/search state
→ up-clean-search / up-remove-objects
→ up-set-target-object
→ up-get-point position-object
→ up-set-target-point
```

Reference semantics establish that filters configure state for later `find-*` calls; `find-*` can be used as Facts/Actions; zero-result searches return false when used as Facts; and `up-get-search-state` exposes search-result counts. citeturn2search0turn0search1

Therefore:

```text
NO TARGET
≠
PLACEMENT FAILURE
≠
CONSTRUCTION FAILURE
≠
COMPLETION
```

Search failure is a Placement state that causes re-entry/reassessment. It must not advance the Construction cursor.

## 7. Construction → Placement Entry Contract

Construction may enter Placement only after the donor path has established the applicable construction authorization, including its feasibility/pending/escrow conditions.

The conceptual request is:

```text
(object type,
 placement mode,
 progression identity,
 target requirement,
 placement configuration,
 escrow context,
 builder requirement)
```

This is an architectural representation of distributed Shadow state, not a new runtime API that must literally exist in `.per`.

## 8. Placement → Execution Contract

Execution receives:

```text
placement mode
object type
target point/object/reference as applicable
placement configuration
escrow state
builder assignment requirement as applicable
```

The engine then performs the action.

A crucial engine constraint is preserved: historical UP notes state that only one successful `build`/`up-build` command is allowed per AI rule pass; subsequent build commands silently fail. This makes one-dispatch-per-pass a qualification invariant rather than an optional optimization. citeturn3search0

## 9. Completion Contract

No Construction or Placement rule may advance progression merely because:

```text
can-build-with-escrow == true
up-build was invoked
up-assign-builders was invoked
up-pending-objects > 0
up-pending-placement == true
search found a target
release-escrow executed
```

Completion requires the donor's world-state observer, such as the relevant `building-type-count-total` threshold or other explicit completed-world predicate.

Shadow's stable/tower/construction patterns demonstrate the distinction directly: dispatch rules and later count-based progression rules are separate control events. fileciteturn547file0

## 10. Failure and Re-entry

### A. Feasibility failure

Retain the current construction item/cursor. Do not advance.

### B. Existing pending work

Suppress duplicate dispatch where the donor uses a pending guard. `up-pending-placement` is a managed-placement observation and must not be generalized to mills/camps because the engine explicitly uses a different placement system for them. citeturn2search0

### C. Search empty

`find-*` zero-result state is a search failure. Re-enter search/reassessment. Do not manufacture a target.

### D. Placement cannot currently succeed

The engine's managed placement mechanism may retry across internal passes. AI-side progression remains unchanged until world-state completion is observed.

### E. Command silently fails / second dispatch in same pass

Do not infer success. Re-enter on a later script pass subject to the donor's guards. The one-successful-build-per-rule-pass engine constraint is explicit in the reference history. citeturn3search0

### F. Progression overshoot

Use Shadow's explicit “come back if skipped” reconciliation rules: if world state is below the milestone but the cursor has advanced beyond it, reset `gl-build-progress` to the milestone and restore `gl-current-build-item` on the next progression pass.

## 11. Re-entry Rules

Re-entry is a normal property of the machine, not an exceptional transaction rollback. Re-entry occurs after:

- resource/escrow feasibility changes;
- pending state clears or changes;
- target/search state becomes available;
- placement retries advance or fail;
- timer guards expire;
- progression pause changes;
- world-state completion appears;
- cursor reconciliation detects a skipped milestone;
- a donor-specific failsafe reactivates the construction path.

The module contract therefore remains **persistent-state/reassessment**, not request/response/return.

## 12. Ownership Invariants

1. Placement never creates strategic construction intent.
2. Construction never declares completion from command issuance.
3. Escrow never declares completion.
4. Builder assignment never declares completion.
5. Search success never declares completion.
6. Pending state never declares completion.
7. Placement failure never advances progression.
8. One successful `build`/`up-build` per AI rule pass is respected.
9. `place-control` consumes placement data established for that operation.
10. `place-point` consumes a target point established for that operation.
11. Donor-specific failsafes and re-entry paths remain explicit.
12. Jumps remain control-flow edges, not abstract priority labels.

## 13. ABI Surface

### Construction → Placement

```text
request:
  object_type
  placement_mode
  progression_identity
  target_requirement
  placement_configuration
  escrow_context
  builder_requirement
```

### Placement → Execution

```text
prepared:
  placement_mode
  object_type
  target/reference state
  placement_configuration
  escrow_state
  builder_requirement
```

### Execution → Verification

```text
command-issued
pending-observation
world-state-observation
```

These are distinct events, not interchangeable return values.

### Verification → Construction

```text
WORLD_STATE_CONFIRMED
WORLD_STATE_NOT_CONFIRMED
```

Only `WORLD_STATE_CONFIRMED` may satisfy a completion transition.

## 14. Design Readiness

### RESOLVED

- `up-build` is an action/queue operation, not completion.
- `up-assign-builders` is an assignment policy/action, not completion.
- zero-result `find-*` behavior is defined.
- target-object selection semantics are defined.
- `place-control` reference semantics are defined.
- point-placement semantics are defined.
- placement zone/failure behavior is defined by engine semantics.
- pending-object/pending-placement meanings are separated.
- managed placement failure/retry is separated from AI progression.
- one successful build command per AI rule pass is a hard execution constraint.

### REMAINING / RUNTIME-QUALIFICATION ONLY

- exact DE-version behavior of the historical Shadow source under current AoE2DE 101.103.48987.0;
- whether every historical UP placement behavior is preserved identically by the current DE engine;
- exact runtime observation timing between `up-build`, pending state, foundation creation, and final building count;
- runtime behavior of Shadow's specific strategic-number combinations;
- runtime qualification of target/search lifetime across failed placement attempts.

These are no longer ABI-definition gaps. They are **runtime qualification questions**.

## 15. Evidence

**DIRECT:** Shadow contains `up-build place-normal`, `place-point`, and `place-control`; uses search state before point placement; writes placement configuration; uses pending guards; and advances progression from world-state observations. The tower and extra-stable paths are explicit examples. fileciteturn547file0

**REFERENCE-TRIANGULATED:** AI Reference/UP documentation establishes `up-build`, `up-assign-builders`, search facts/actions, target selection, placement data, point placement, pending-object semantics, placement retry behavior, and the one-build-per-rule-pass constraint. citeturn2search0turn3search0turn0search1

**COMPOSED:** The module boundary and ABI request/response vocabulary organize distributed Shadow state into implementation contracts.

**INFERRED:** Exact module ownership is an architectural mapping, not a literal donor module structure.

## 16. Verification

- All former ABI questions were rechecked against canonical Shadow patterns and engine/reference semantics.
- `up-build` remains a dispatch action, never completion.
- `up-assign-builders` remains assignment, never completion.
- search-empty is now resolved at the engine level.
- `place-control` is now resolved sufficiently for implementation design.
- point-placement configuration semantics are resolved.
- pending-placement is explicitly not generalized to camps/mills.
- placement failure is treated as an engine retry/re-entry condition rather than a transaction failure return.
- the one-successful-build-per-rule-pass constraint is now an explicit execution invariant.
- no new document was created; this authoritative ABI was consolidated in place.

## 17. Uncertainty

The ABI is **design-ready but not runtime-qualified**. The remaining uncertainty concerns current-DE qualification and timing/observability, not missing conceptual engine definitions. Runtime tests must distinguish command issuance, pending/foundation state, and completed world state and must test the exact donor placement configurations used by Shadow.
