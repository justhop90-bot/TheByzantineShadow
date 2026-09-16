# Shadow Construction Executor Boundary — 2026-09-16

## Scope

This pass cross-checks the canonical Shadow construction transaction model against the current AiByz repository before implementation.

## Direct Shadow evidence

The canonical `ShadowSource.per` construction interval demonstrates a staged transaction pipeline:

`build-item intent → feasibility/escrow gate → search initialization → candidate discovery/filtering → target selection → point extraction → placement-policy setup → build command → pending/world observation → progression or recovery`.

Observed primitives include:

- `gl-current-build-item` — active construction intent/state.
- `gl-build-progress` — progression register; rules advance it and reset it when construction was skipped.
- `can-build-with-escrow` / `up-can-build` — feasibility/commitment gates.
- `release-escrow` and `set-escrow-percentage` — explicit resource commitment/release boundary.
- `up-full-reset-search`, `up-find-remote`, `up-clean-search`, `up-remove-objects` — candidate search/filter pipeline.
- `up-set-target-object`, `up-get-point`, `up-set-target-point` — target/placement state transfer.
- `set-strategic-number` — placement-policy parameters.
- `up-build` / `build` — execution primitives.
- `up-pending-objects` / `up-pending-placement` — duplicate/commitment suppression and observable pending state.
- `up-assign-builders` — builder assignment control.
- timers and `SPLIT` — temporal/arbitration serialization.

The GOLDMC1 sequence in the source is especially explicit: search for a gold mine, select a target object, extract its point, configure placement parameters, release wood escrow, issue `up-build place-point`, then use observable dropsite distance/progression rules to advance or recover.

## AiByz repository cross-check

The current AiByz `main` branch describes production `.per` implementation as blocked pending ownership/ABI and command-lifecycle gates. Its integration candidate loads an `Aegis-execution-final` layer, but the candidate civilian files exposed in `implementation/` are primarily observation, demand, arbitration, task-command, verification, productivity, and recovery modules. The repository's ownership inventory explicitly marks all candidate numeric channels as experimental and uncleared for production.

Therefore the repository does **not** currently provide sufficient direct evidence to claim that the AEGIS candidate already owns the engine-level construction executor or that its `build`, `up-build`, placement modes, or builder assignment semantics are runtime-qualified.

## Authority boundary

### Shadow

Shadow is strong evidence for the **behavioral construction transaction model** and historical executor choreography.

### AEGIS

AEGIS should own:

`OBSERVE → CLASSIFY/BELIEVE → OBJECTIVE → REQUIREMENT → CANDIDATES → EVALUATE → COMMIT → AUTHORIZE`

and should emit an explicit construction intent/authorization envelope.

### Existing executor

The engine-facing executor should retain ownership of:

`EXECUTE → PENDING/ACCEPTED → WORLD REALIZATION → VERIFY`

until the actual target-runtime executor semantics are directly inspected and qualified.

## Remaining forensic gate

Before writing production construction code, inspect the actual runtime-loaded AiByz/stock construction implementation, not only the candidate architecture repository, and establish exact semantics for:

1. `build` versus `up-build`.
2. `place-normal`, `place-control`, and `place-point`.
3. `up-assign-builders`.
4. escrow reservation/release timing relative to command issuance.
5. pending-object and pending-placement lifecycle.
6. construction completion/failure observability.
7. all current writers of construction intent, escrow, placement, and builder-assignment state.
8. numeric ABI ownership for every new AEGIS construction state channel.

## Readiness decision

**Specification-ready: YES.**

**Production-code-ready: NO.**

The blocker is no longer Shadow archaeology. It is executor ownership and target-runtime lifecycle qualification. Writing construction implementation before that evidence exists would convert a historically demonstrated model into an unverified engine contract.

## Evidence classification

- Shadow construction choreography: **DIRECT**.
- AEGIS/Shadow architectural mapping: **COMPOSED**.
- Claim that AEGIS may own cognition/authorization while the existing executor owns realization: **AEGIS-GENERALIZATION**, pending runtime qualification.
- Exact runtime semantics of `build`/`up-build`/placement/builder assignment in current AiByz: **UNCERTAIN** until inspected.
