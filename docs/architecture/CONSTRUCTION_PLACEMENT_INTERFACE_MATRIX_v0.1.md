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
| placement config | Placement | Execution | zone/fail/separation settings | DIRECT | No |
| builder request | Construction/Placement | Execution | builder requirement | DIRECT for invocation; ABI semantics OPEN | No |
| build command | Execution | Engine | `build` / `up-build` | DIRECT | No |
| pending state | Engine | Construction | pending object/placement | DIRECT | No |
| world completion | Verification | Construction | building/object world state | DIRECT | **Yes** |
| progression advance | Construction | Construction | progress + 1 / next item | DIRECT | N/A |
| recovery | Construction | Construction | cursor rollback/re-entry | DIRECT | N/A |

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

**COMPOSED:** This matrix turns the distributed donor control flow into an explicit module interface.

**INFERRED:** Producer/consumer ownership is an architectural organization of the recovered graph, not a claim that Shadow had these named modules.

## Verification

The matrix was checked against the recovered construction patterns including farm, lumber-camp, mill, and mining-camp paths and against the donor placement forms `place-normal`, `place-point`, and `place-control`.

## Uncertainty

The exact engine semantics of `up-build`, `up-assign-builders`, search-empty state, placement failure, and `place-control` remain open until reference/ABI triangulation is complete.
