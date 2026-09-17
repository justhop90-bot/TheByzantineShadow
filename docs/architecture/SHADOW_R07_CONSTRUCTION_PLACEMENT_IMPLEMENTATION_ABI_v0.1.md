# SHADOW R07 CONSTRUCTION / PLACEMENT IMPLEMENTATION ABI v0.1

## Status

**AUTHENTICATED STATIC MAPPING — IMPLEMENTATION GATE OPEN — RUNTIME QUALIFICATION PENDING**

This document binds the authenticated R07 Construction/Progression evidence to the current `04_construction` and placement implementation boundary. It does not claim that the donor was physically modularized this way. Shadow is an ordered control machine; these are implementation boundaries derived from its observed state/data/control behavior.

## Authoritative evidence

- Canonical donor: `ShadowSource.per`
- R07: rules `1794–1896`
- R07 edge matrix: `docs/forensics/SHADOW_R07_EDGE_MATRIX_v0.1.csv`
- R07 state-transition matrix: `docs/forensics/SHADOW_R07_STATE_TRANSITION_MATRIX_v0.1.csv`
- R07 rule ledger: `docs/forensics/SHADOW_R07_CONSTRUCTION_PROGRESSION_RULE_LEDGER_v0.1.csv`
- Construction ABI: `docs/architecture/CONSTRUCTION_PLACEMENT_ABI_v0.1.md`

The authenticated R07 state-transition matrix has blob SHA `3e2534f3136218a6e887d2dc7a6b110ca2fd20a7`.

## 1. R07 topology

R07 contains 103 rules and 107 keyed edge records. Every rule has its source-order successor; the region has one incoming source-order edge `1793→1794` and one outgoing source-order edge `1896→1897`. Explicit internal jumps are:

- `1795 --(+1)--> 1796`
- `1850 --(+4)--> 1854`
- `1891 --(+5)--> 1896`

No explicit jump enters R07 from outside and no explicit jump exits R07.

Source order and positional jump semantics are therefore implementation constraints, not documentation conveniences.

## 2. Ownership boundary

### `04_construction` owns

- construction objective selection;
- `gl-current-build-item` progression cursor;
- `gl-build-progress` milestone cursor;
- `gl-progression-pause` construction/progression gating;
- R07-local `SPLIT` arbitration;
- construction feasibility gates;
- objective-local escrow transitions required by the construction path;
- builder assignment decisions;
- construction command issuance;
- consumption of pending/world-state observations;
- completion-gated progression advancement;
- progression reconciliation and re-entry.

### Placement implementation owns

- placement mode realization (`NORMAL`, `POINT`, `CONTROL`);
- search reset and search execution;
- target-object and target-point handling;
- placement-data configuration;
- placement-local strategic numbers;
- spatial placement retry/failure state.

Placement does **not** own strategic construction objectives, `gl-build-progress`, `gl-current-build-item`, global progression, or strategic escrow ownership.

## 3. State ABI

| State | Reads | Writes | Authority |
|---|---|---|---|
| `gl-current-build-item` | Construction | Construction | Construction |
| `gl-build-progress` | Construction | Construction | Construction |
| `gl-progression-pause` | Construction | Construction | Construction |
| `SPLIT` | R07 local control | R07 local control | Construction control |
| `gl-escrow-state` | Construction | Donor-authorized construction paths | Engine accounting-mode boundary |
| escrow percentages | Construction | Donor-authorized objective path | Objective-local resource protection |
| `sn-focus-player-number` | Placement/search | Placement/search | Placement |
| `sn-placement-zone-size` | Placement | Placement | Placement |
| `sn-placement-fail-delta` | Placement | Placement | Placement |
| `sn-allow-adjacent-dropsites` | Placement | Placement | Placement |
| `sn-dropsite-separation-distance` | Placement | Placement | Placement |
| search/target state | Placement | Placement | Placement |
| pending objects | Construction | none | Engine/world observation |
| pending placement | Construction/placement | none | Engine/world observation |
| building counts | Construction | none | World completion evidence |

No module may advance progression merely because it issued a command or observed a pending object.

## 4. Command ABI

Construction may dispatch the donor-observed construction commands at their corresponding control points:

- `build`
- `up-build place-normal`
- `up-build place-point`
- `up-build place-control`
- `up-assign-builders`

Placement may perform the spatial preparation operations:

- `up-full-reset-search`
- `up-find-local`
- `up-find-remote`
- `up-set-target-object`
- `up-get-point`
- `up-set-target-point`
- `up-set-placement-data`

The placement implementation must not silently turn command issuance into completion.

## 5. Pending-state ABI

The following states are distinct:

```text
CAN_BUILD
PENDING_OBJECT
PENDING_PLACEMENT
TARGET_RESOLVED
COMMAND_ISSUED
WORLD_OBJECT_OBSERVED
COMPLETED
```

In particular:

```text
can-build != pending
pending != completed
placement-ready != completed
command-issued != completed
```

`up-pending-objects` and `up-pending-placement` are guards/observations used to suppress or coordinate repeated execution. They are not completion evidence.

## 6. Completion ABI

R07 progression advances only from world-state or explicit reconciliation evidence.

Representative direct completion observers include:

- `building-type-count-total farm >= 4`
- `building-type-count-total farm >= 7`
- `building-type-count-total farm >= 2`
- `building-type-count-total lumber-camp >= 1`
- `building-type-count-total lumber-camp >= 2`
- `building-type-count-total lumber-camp >= 3`
- `building-type-count-total lumber-camp >= 4`
- `building-type-count-total mill >= 1`
- `building-type-count-total mining-camp >= 1`
- `building-type-count-total mining-camp >= 3`

Progression reconciliation is a separate mechanism. For example, if the world count is below an expected milestone while `gl-build-progress` has advanced beyond the recoverable milestone, the donor can reset the progression cursor to the known milestone. This is not equivalent to declaring construction complete.

## 7. Farm vertical slice: rules 1794–1814

This is the first implementation slice because it exercises nearly the complete Construction ABI.

### Dispatch

Rules `1794`, `1798`, and `1803` issue `up-build place-normal ... farm` paths.

### Local arbitration

Rules `1796–1802` manipulate `SPLIT`. `SPLIT` is local control state and must not become a strategic priority variable.

### Pending suppression

Rules including `1804` and `1811` use `up-pending-objects` before issuing farm construction.

### Execution

Farm construction uses `build farm` or `up-build place-normal ... farm`, with donor-observed escrow/resource mutations around execution.

### Completion

Rule `1805` advances `gl-build-progress` only after the farm-count milestone is observed. Rule `1809` does the analogous operation for the later farm milestone.

### Reconciliation

Rules `1806` and `1813` reconcile `gl-build-progress` backward when actual farm counts fall below the expected milestone.

### Cursor restoration

Rules `1807`, `1810`, and `1814` set the next `gl-current-build-item` phase.

## 8. Builder/control placement slice: rules 1815–1827

This slice binds builder assignment and `CONTROL` placement.

The sequence is:

```text
construction objective
→ feasibility
→ pending guard
→ placement-data configuration
→ place-control dispatch
→ builder assignment
→ later world-state observation
```

`up-set-placement-data` and `up-build place-control` belong to the Placement implementation boundary, while the decision to enter that path remains Construction authority.

Builder assignment is execution policy, not completion evidence.

## 9. Lumber-camp progression slice: 1828–1850

The lumber-camp region repeats the construction/progression lifecycle with different milestones and placement configuration.

Required behavior includes:

```text
current-build-item
→ feasibility
→ escrow/resource protection
→ placement or build dispatch
→ pending suppression
→ world count
→ gl-build-progress advancement
→ next objective
```

The explicit jump at rule `1850` must resolve to `1854` and must remain semantically equivalent after implementation.

## 10. Mining-camp search/POINT slice: 1877–1896

This is the second major implementation gate because it exercises embedded search and point placement.

Representative sequence:

```text
mining-camp objective
→ can-build-with-escrow
→ placement configuration
→ search reset
→ remote gold-mine search
→ target-point preparation
→ target object/point extraction
→ place-point
→ pending/retry state
→ mining-camp world count
→ progression milestone
```

The placement implementation owns the spatial middle of this chain. Construction retains ownership of the objective and progression endpoints.

Rule `1891` contains `up-jump-rule 5`, resolving to `1896`. Rule `1896` observes the `mining-camp >= 3` milestone and advances progression before the `1896→1897` R07 exit.

## 11. Source-order preservation

The implementation must not copy isolated rules into a new file and assume semantic equivalence.

Safe approaches are:

1. preserve the donor order for the reconstructed control slice;
2. construct an equivalent positional machine only after mechanically resolving all jump/fall-through edges; or
3. use an authenticated source transformation that proves jump equivalence.

Any implementation change that alters an edge requires regeneration of the affected CFG evidence.

## 12. Evidence classification

### DIRECT_DONOR_TEXT

Literal donor predicates, writes, commands, pending guards, placement operations, escrow operations, and explicit jump operations.

### MECHANICALLY_DERIVED

Resolved jump targets, fall-through successors, and transition effects directly computed from authenticated source text.

### MECHANICALLY_CLASSIFIED

R07 membership and cross-boundary classification.

### COMPOSED

Construction/Placement interface assignments formed from multiple direct donor observations.

### INFERRED

Physical file boundaries or generalized interfaces not literally present as donor modules.

### RUNTIME-UNPROVEN

Any claim that the reconstructed implementation produces the same engine/world-state behavior in AoE2DE runtime.

## 13. Implementation gates

### Gate A — Farm progression

Implement and statically qualify `1794–1814`.

Required checks:

- parser qualification;
- symbol declaration audit;
- duplicate writer audit;
- command inventory;
- pending-guard audit;
- completion-observer audit;
- CFG edge comparison;
- escrow mutation comparison.

### Gate B — Controlled placement

Implement `1815–1827` after Gate A passes.

Required checks:

- `up-set-placement-data` ordering;
- `place-control` dispatch;
- builder assignment ordering;
- pending-placement handling;
- world-state completion separation.

### Gate C — Search/POINT placement

Implement `1877–1896` after Gate B passes.

Required checks:

- search reset;
- remote resource search;
- target/point extraction;
- point dispatch;
- placement failure/re-entry;
- progression milestone;
- `1891→1896` jump equivalence.

## 14. Runtime qualification requirement

Static qualification is not runtime proof.

For each gate, runtime qualification must distinguish:

```text
command issued
pending object
foundation/world object
completed building count
progression mutation
re-entry
```

A successful parser or observed command does not promote the implementation to runtime-equivalent.

## 15. Final implementation invariant

```text
Construction owns lifecycle.
Placement owns spatial realization.
Execution issues commands.
Pending state suppresses/coordinates execution.
World state proves completion.
Progression advances only from evidence.
Escrow protects the selected objective.
Source order remains executable semantics.
```

This ABI is the implementation gate for the first R07 vertical slice. No broader construction abstraction should be introduced until the authenticated slice is statically and then runtime qualified.
