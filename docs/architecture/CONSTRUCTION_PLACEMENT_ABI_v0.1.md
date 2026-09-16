# Construction ↔ Placement ABI v0.1

## Status

**DESIGN DRAFT — donor-derived boundary, not yet runtime-qualified.**

This contract is derived from the canonical `ShadowSource.per` construction/placement mechanisms and the construction/placement state-machine reconstruction. It follows `docs/AI_SCRIPTER_OPERATING_DOCTRINE.md` and the repository Drift Protocol.

The contract intentionally isolates unresolved engine semantics rather than inventing them.

## 1. Boundary

```text
Construction
  owns WHAT is currently authorized and WHERE the progression machine is
  ↓
Placement
  owns HOW an authorized construction target is spatially resolved
  ↓
Execution
  owns HOW the engine build operation is issued
  ↓
Verification
  owns WHETHER world state actually changed
```

Construction therefore does not delegate strategic intent to Placement, and Placement does not manufacture construction intent.

## 2. Request Contract

A Construction→Placement request contains the minimum semantic fields needed to reproduce observed Shadow dispatch:

| Field | Meaning | Authority |
|---|---|---|
| object type | structure to construct | Construction |
| placement mode | `normal`, `point`, or `control` | Construction/Placement boundary |
| escrow context | resource-accounting state required by dispatch | Escrow |
| builder requirement | requested builder assignment | Construction/Execution boundary |
| target requirement | object/point/control target requirement | Placement |
| placement configuration | zone/failure/separation parameters | Placement/policy boundary |
| progression identity | current build item/milestone | Construction |

No request field constitutes completion.

## 3. Placement Modes

### NORMAL

Used when the donor invokes `up-build place-normal`.

Required state:

```text
construction authorized
object type known
normal placement configuration available
```

Target-object or target-point state is not presumed unless the source path explicitly establishes it.

### POINT

Used when the donor invokes `up-build place-point`.

Required state:

```text
construction authorized
valid target point established
placement configuration established
```

Representative donor pattern:

```text
search resource
→ select target object
→ obtain target point
→ set target point
→ configure placement
→ up-build place-point
```

### CONTROL

Used when the donor invokes `up-build place-control`.

Required state:

```text
construction authorized
control-placement data established
```

The exact engine semantics of control placement remain an ABI item to qualify.

## 4. Target State

Placement owns the lifecycle:

```text
NONE
 ↓
SEARCHING
 ↓
CANDIDATE-FOUND
 ↓
TARGET-VALID
 ↓
TARGET-HANDOFF
 ↓
PLACEMENT-READY
 ↓
DISPATCHED
```

Failure paths do not imply completion:

```text
SEARCHING → NO-TARGET → SEARCHING / WAIT
TARGET-VALID → INVALID → SEARCHING
PLACEMENT-READY → FAILURE → REASSESS
```

The exact engine representation of empty-search and placement failure remains UNKNOWN.

## 5. Search Contract

For point-placement paths, Placement may execute the donor search sequence:

```text
up-full-reset-search
→ up-set-target-point
→ up-filter-distance
→ up-find-remote/local
→ inspect candidate state
→ up-clean-search
→ up-remove-objects
→ up-set-target-object
→ up-get-point
→ up-set-target-point
```

Search state is persistent control state. It must not be reduced to a pure function that loses the donor's stateful re-entry behavior.

## 6. Placement Configuration

Observed Shadow paths directly mutate placement parameters immediately before build dispatch, including:

- `sn-placement-zone-size`
- `sn-placement-fail-delta`
- `sn-allow-adjacent-dropsites`
- `sn-dropsite-separation-distance`

Therefore the previous assumption that geometry/failure policy is necessarily external to Placement is not established by the donor. Ownership remains a design boundary requiring further triangulation.

Contract:

```text
Construction supplies policy inputs when required
Placement materializes the configuration needed by the selected mode
Execution consumes the resulting configuration
```

## 7. Handoff

Construction→Placement occurs only after Construction has established:

```text
current build item
AND
construction feasibility
AND
pending guard
AND
construction authorization
```

Placement must return one of the following architectural outcomes:

```text
PLACEMENT_READY
TARGET_UNAVAILABLE
PLACEMENT_RETRY
PLACEMENT_FAILED
DISPATCH_READY
```

These are control outcomes, not world-state completion signals.

## 8. Execution Boundary

Placement prepares the spatial state required by the donor command. Execution issues the command.

The following must remain distinguishable:

```text
placement ready
command issued
pending placement/object exists
world object exists
world object satisfies completion condition
```

No intermediate state advances `gl-build-progress`.

## 9. Builder Assignment

Where the donor invokes `up-assign-builders`, the request may carry a builder requirement. Builder assignment remains an execution-side operation.

The following equivalence is prohibited:

```text
builder assignment accepted == building completed
```

Exact assignment semantics, reassignment behavior, and failure signaling remain UNKNOWN.

## 10. Completion Contract

Placement cannot declare construction completion.

Completion returns to Construction through Verification:

```text
build dispatch
→ world observation
→ required building/object state confirmed
→ Construction completion transition
→ progress mutation
→ next current-build-item selection
```

For count-based milestones, the authoritative observation is a world-state count such as `building-type-count-total` reaching the required threshold.

## 11. Failure and Re-entry

### Feasibility failure

Construction retains the current item. Placement is not entered or is exited without advancing progression.

### Pending guard

If the required object is already pending, duplicate dispatch is suppressed unless a donor-specific failsafe explicitly permits a retry path.

### Search failure

Placement retains/re-enters the target-search state. Construction retains the current objective.

### Placement failure

No progression advancement occurs. Placement configuration/search may be regenerated and the request re-entered.

### Command without completion

The command remains only an execution event. Construction waits for authoritative world-state evidence and reassesses.

### Progression overshoot

If the cursor has advanced beyond an uncompleted construction milestone, Construction performs donor-style cursor reconciliation and re-enters current-item selection.

## 12. Re-entry Rules

Re-entry is legal after:

- resource feasibility changes;
- pending state clears;
- a target becomes available;
- search configuration changes;
- placement configuration changes;
- timer guards expire;
- a higher-priority control path releases the progression pause;
- world-state completion is observed;
- progression reconciliation resets the cursor.

No one-shot request/response lifecycle is assumed.

## 13. Ownership Invariants

1. Placement cannot create strategic intent.
2. Construction cannot claim completion from command issuance.
3. Escrow cannot claim construction completion.
4. Builder assignment cannot claim construction completion.
5. Search success cannot claim construction completion.
6. Pending state cannot be treated as world-state completion.
7. Placement failure cannot silently advance progression.
8. Construction progression cannot outrun verified world state where the donor provides reconciliation.
9. Jumps remain control-flow edges rather than abstract priority labels.
10. Donor-specific failsafes remain explicit rather than being collapsed into generic retry behavior.

## 14. ABI Surface

### Construction → Placement

```text
request(object_type,
        placement_mode,
        progression_identity,
        target_requirement,
        builder_requirement,
        placement_policy_inputs,
        escrow_context)
```

### Placement → Construction

```text
PLACEMENT_READY
TARGET_UNAVAILABLE
PLACEMENT_RETRY
PLACEMENT_FAILED
DISPATCH_READY
```

### Placement → Execution

```text
placement_mode
object_type
target_state
target_object
target_point
placement_configuration
builder_requirement
```

### Verification → Construction

```text
WORLD_STATE_CONFIRMED
WORLD_STATE_NOT_CONFIRMED
```

## 15. Prohibited Collapses

The implementation must not collapse:

```text
can-build-with-escrow → completed
release-escrow → completed
build → completed
up-build → completed
pending-object → completed
pending-placement → completed
builder-assigned → completed
search-found → completed
```

Each is a distinct state/evidence class.

## 16. Design Readiness

The boundary is sufficiently specified for module-level design, but not for final runtime implementation of unresolved engine operations.

### READY

- Construction owns progression semantics.
- Placement owns target/mode/search semantics.
- Verification owns world-state completion evidence.
- Escrow remains separate.
- Execution remains separate.
- Failure preserves re-entry.
- Completion is observational.

### OPEN

- exact `up-build` ABI;
- exact `up-assign-builders` ABI;
- empty-search representation;
- placement-failure representation;
- target-state lifetime after failed dispatch;
- exact `place-control` semantics;
- final ownership of placement strategic-number mutation.

## Evidence

**DIRECT:** Shadow contains explicit `up-build place-normal`, `up-build place-point`, and `up-build place-control` paths; point-placement paths establish target objects/points and mutate placement parameters before dispatch; construction progression is mutated from observed building state.

**COMPOSED:** The Construction↔Placement request/response boundary combines these donor mechanisms into an explicit architectural interface.

**INFERRED:** The named module ownership boundaries are architectural abstractions derived from the donor state graph rather than literal Shadow module boundaries.

**UNKNOWN:** Several engine-level return/failure semantics remain unresolved.

## Verification

- Contract preserves the donor distinction between feasibility, dispatch, pending state, and completion.
- Contract preserves multiple placement modes.
- Contract preserves stateful search and re-entry.
- Contract does not convert jumps into priority semantics.
- Contract does not promote command acceptance into world-state completion.
- Contract explicitly isolates unresolved ABI behavior.

## Uncertainty

This artifact is a design contract, not runtime qualification. Any implementation that depends on an OPEN ABI item must mark the dependency and must not silently replace it with an assumed engine behavior. Additional canonical source extraction and AI Reference/AI Encyclopedia triangulation should resolve engine semantics before runtime qualification.
