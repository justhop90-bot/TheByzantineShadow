# Construction / Placement Interface Matrix v0.1

## Status

**DESIGN-READY / ENGINE-SEMANTICS-TRIANGULATED / NOT RUNTIME-QUALIFIED.**

This remains the authoritative compact interface matrix for the Construction↔Placement boundary. It has been updated in place; no new document was created.

## Interface Matrix

| Boundary | Producer | Consumer | Data / signal | Evidence | Completion? |
|---|---|---|---|---|---|
| progression | Construction | Construction | current item / progress cursor | DIRECT | No |
| feasibility | Engine | Construction | `can-build*` | DIRECT | No |
| pending guard | Engine | Construction | `up-pending-objects`, `up-pending-placement` where applicable | DIRECT + REF | No |
| escrow | Escrow | Construction/Execution | reservation/accounting state | DIRECT/COMPOSED | No |
| placement request | Construction | Placement | object, mode, target requirement, configuration | COMPOSED | No |
| search | Placement | Placement | filters, local/remote results, search state | DIRECT + REF | No |
| empty search | Engine | Placement | `find-*` false as Fact when zero results | REF | No |
| target selection | Placement | Placement/Execution | target object / point / placement reference | DIRECT + REF | No |
| placement config | Placement | Execution | zone size, fail delta, adjacent-dropsite/separation controls where donor path uses them | DIRECT + REF | No |
| builder assignment | Execution | Engine | `up-assign-builders` type/class + minimum builder count | DIRECT + REF | No |
| build command | Execution | Engine | `build` / `up-build` | DIRECT + REF | No |
| managed placement retry | Engine | Placement/Construction | placement continues across engine passes | REF | No |
| pending state | Engine | Construction | pending object / pending placement | DIRECT + REF | No |
| world completion | Verification | Construction | completed building/object world state | DIRECT | **Yes** |
| progression advance | Construction | Construction | progress mutation / next current item | DIRECT | N/A |
| recovery/re-entry | Construction | Construction/Placement | cursor reconciliation / search / retry | DIRECT + REF | N/A |

## Resolved Engine Semantics

### `up-build`

`up-build` is an UP **action** that adds a building to the construction queue using a PlacementType and EscrowState. It is not a synchronous completion return. The engine therefore requires later observation of pending/world state. citeturn0search1turn3search0

### `up-assign-builders`

`up-assign-builders` assigns **at least a specified number of builders** to a building type or class. It is assignment policy, not completion. citeturn2search0

### Search-empty

`up-find-local` and `up-find-remote` can act as Facts; zero results return false. `up-get-search-state` exposes local/remote result information. Filters only configure state for later searches. Therefore empty search is now a resolved engine state, not an UNKNOWN ABI return. citeturn2search0

### Target selection

`up-set-target-object` selects an indexed result from the current search set and returns false as a Fact when the requested index cannot be selected. `up-get-point` can extract a position from the selected object. citeturn2search0turn0search1

### `place-control`

`up-set-placement-data` establishes the reference used by subsequent `up-build place-control`. The reference consists of player + object type (or `-1` for home TC) + relative placement distance. Relative placement is based on the target player's location or, when unavailable, the map center. Shadow directly uses this pattern for towers and controlled stable placement. citeturn2search0

### `place-point`

`up-build place-point` uses the point established by `up-set-target-point`. Its placement zone is stored with the build call and can expand when placement fails; point placement does not rely on `up-set-placement-data` or `sn-placement-fail-delta`. citeturn2search0

### Placement retry

Managed placement is not a Boolean success return. The engine retries placement across internal passes and expands the relevant placement zone according to the placement mode/configuration. `sn-placement-fail-delta` applies to control placement distance; zone-size behavior applies to the documented managed placement systems. citeturn2search0

### Pending state

`up-pending-objects` compares pending train/build count. `up-pending-placement` reports managed placement activity, but the engine documentation explicitly warns that mills and camps use a different placement system. Pending therefore remains a guard/observation class, not completion. citeturn2search0

### One-dispatch-per-rule-pass constraint

Historical engine documentation states that only one `build`/`up-build` command is allowed to succeed per AI rule pass; subsequent build commands silently fail. This is now an explicit execution invariant for qualification. citeturn3search0

## Shadow Cross-Check

Shadow directly demonstrates the control pattern for towers and extra stables:

```text
can-build
→ placement reference/configuration
→ up-build place-control
→ local progression/control-state mutation
```

Completion is handled separately through world-state observations such as building counts. The source therefore supports the separation between dispatch and completion. fileciteturn547file0

Point-placement construction similarly establishes a resource target, extracts its point, sets the target point, configures placement where required, and then dispatches `place-point`. This is a stateful target-resolution path, not a pure placement function.

## Required Separation

```text
FEASIBILITY
≠ RESERVATION
≠ SEARCH SUCCESS
≠ TARGET VALIDITY
≠ PLACEMENT READY
≠ COMMAND ISSUED
≠ PENDING
≠ WORLD COMPLETION
```

Any implementation collapsing these states violates the forensic reconstruction.

## Runtime-Qualification Boundary

The previous OPEN ABI questions are no longer conceptual gaps. They are now classified as runtime qualification questions:

- exact timing of command → pending/foundation → completed-world observation under current AoE2DE;
- persistence of target/search state across failed placement attempts in the current engine;
- current-DE behavior of Shadow's exact combinations of placement strategic numbers;
- current-DE equivalence of historical UP placement behavior.

These require runtime evidence, not another architecture document.

## Evidence

**DIRECT:** Shadow contains distinct feasibility predicates, pending guards, `place-normal`, `place-point`, `place-control`, search pipelines, build commands, placement configuration mutations, and world-state completion/progression rules. fileciteturn547file0

**REFERENCE-TRIANGULATED:** AI Reference/UP material resolves `up-build`, `up-assign-builders`, search-empty behavior, target selection, point/control placement, pending state, managed placement retry, and the one-build-per-rule-pass constraint. citeturn2search0turn3search0turn0search1

**COMPOSED:** Producer/consumer ownership is an architectural organization of the distributed donor graph.

**INFERRED:** Named module boundaries are not claims that Shadow had literal modules with those names.

## Verification

- Former OPEN ABI questions were cross-checked against canonical Shadow patterns and engine semantics.
- `up-build` is classified as dispatch, never completion.
- builder assignment is classified as assignment, never completion.
- empty search has an engine-defined false/count representation.
- target-object selection has an engine-defined failure condition.
- `place-control` reference semantics are defined.
- `place-point` semantics are defined.
- placement retry is distinguished from AI progression.
- pending placement is not generalized to mills/camps.
- one successful build command per AI rule pass is explicit.
- no new artifact was created; this authoritative matrix was updated in place.

## Uncertainty

No remaining **conceptual ABI** gap is currently identified. Remaining uncertainty is runtime-specific and must be resolved by qualification on the project's target AoE2DE build. The next useful engineering action is therefore implementation/test preparation, not additional paperwork.
