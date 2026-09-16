# Construction / Placement Interface Matrix v0.1

## Status

DESIGN SUPPORT ARTIFACT — derived from the Shadow construction/placement reconstruction. Governed by `docs/AI_SCRIPTER_OPERATING_DOCTRINE.md`.

## Interface Matrix

| Boundary | Producer | Consumer | Data / signal | Evidence status | Completion? |
|---|---|---|---|---|---|
| progression | Construction | Construction | current item / progress cursor | DIRECT | No |
| feasibility | World/engine | Construction | `can-build*` | DIRECT | No |
| pending guard | Engine | Construction | pending object / placement | DIRECT | No |
| escrow | Escrow | Construction | reservation/availability state | DIRECT/COMPOSED | No |
| placement request | Construction | Placement | object, mode, target requirement | COMPOSED | No |
| search | Placement | Placement | candidates/search state | DIRECT | No |
| target | Placement | Placement/Execution | target object/point/control | DIRECT | No |
| placement config | Placement | Execution | zone/fail/separation settings | DIRECT + REFERENCE-TRIANGULATED | No |
| builder request | Construction/Placement | Execution | builder requirement | DIRECT for invocation; ABI lifecycle OPEN | No |
| build command | Execution | Engine | `build` / `up-build` | DIRECT + REFERENCE-TRIANGULATED | No |
| pending state | Engine | Construction | pending object/placement | DIRECT + REFERENCE-TRIANGULATED | No |
| world completion | Verification | Construction | building/object world state | DIRECT | **Yes** |
| progression advance | Construction | Construction | progress + 1 / next item | DIRECT | N/A |
| recovery | Construction | Construction | cursor rollback/re-entry | DIRECT | N/A |

## Engine-reference updates

The interface classification has been tightened by external engine/reference evidence:

- `up-build` is documented as an UP action that adds a building to the construction queue with dynamic values. It therefore remains a dispatch operation rather than a completion event. citeturn0search4
- `up-assign-builders` is documented as an UP action assigning a specific number of builders to a building type or class. Assignment remains execution state, not completion. citeturn0search4turn0search2
- `up-pending-objects` is a pending-count comparison; DE patch history confirms its queue-related behavior. Pending remains observational state distinct from completed world state. citeturn0search2turn0search7
- `sn-placement-zone-size` and `sn-placement-fail-delta` are documented placement controls associated with forward/control placement, strengthening their treatment as part of the dispatch configuration rather than arbitrary module metadata. citeturn0search5

These references narrow the engine semantics but do not close Shadow-specific failure/re-entry behavior.

## Required Separation

```text
FEASIBILITY
≠ RESERVATION
≠ TARGET VALIDITY
≠ PLACEMENT READY
≠ COMMAND ISSUED
≠ PENDING
≠ COMPLETION
```

Any implementation that collapses these states violates the forensic reconstruction.

## Evidence

**DIRECT:** Donor source contains distinct feasibility predicates, pending guards, placement modes, search operations, build commands, world-state completion tests, and progression mutations.

**REFERENCE-TRIANGULATED:** AI Reference and engine patch material independently support the action/observation character of `up-build`, `up-assign-builders`, `up-pending-objects`, and placement configuration controls.

**COMPOSED:** This matrix turns the distributed donor control flow into an explicit module interface.

**INFERRED:** Producer/consumer ownership is an architectural organization of the recovered graph, not a claim that Shadow had these named modules.

## Verification

The matrix was checked against the recovered construction patterns including farm, lumber-camp, mill, and mining-camp paths and against the donor placement forms `place-normal`, `place-point`, and `place-control`.

The matrix now also distinguishes donor evidence from independently triangulated engine semantics. No reference finding is being used to manufacture a Shadow-specific behavior that the donor does not show.

## Uncertainty

The exact engine semantics of Shadow-specific `up-build` return/failure behavior, `up-assign-builders` lifecycle/reassignment, search-empty state, placement failure, target lifetime, and `place-control` behavior remain open until sufficient reference evidence and runtime qualification exist.

No new artifact is warranted for these questions at this stage; they belong in this matrix and the authoritative Construction↔Placement ABI until their scope becomes genuinely distinct.
