# Byzantine Verification ABI v0.1

**Status:** Symbolic contract; implementation values intentionally unassigned.

## 1. Purpose

Defines the evidence boundary between an engine command and a verified change in game state. The verifier is the sole authority for declaring construction complete from observed world state.

## 2. Owned State

Verification owns:

- verification status
- evidence classification
- expected-versus-observed comparison
- completion confirmation
- contradiction/failure detection
- reconciliation request

It does not own strategic selection or construction execution.

## 3. Verification States

```text
BYZ-VERIFY-NOT-STARTED
BYZ-VERIFY-PENDING
BYZ-VERIFY-OBSERVING
BYZ-VERIFY-CONFIRMED
BYZ-VERIFY-FAILED
BYZ-VERIFY-CONTRADICTED
BYZ-VERIFY-RECONCILE
```

Numeric state IDs: **UNASSIGNED**.

## 4. Evidence Classes

```text
BYZ-EVIDENCE-COMMAND-ISSUED
BYZ-EVIDENCE-PENDING
BYZ-EVIDENCE-WORLD-OBJECT
BYZ-EVIDENCE-COUNT
BYZ-EVIDENCE-SPATIAL
BYZ-EVIDENCE-OTHER-DECLARED
```

Evidence class does not itself determine completion; its admissibility is defined by the construction target's verification policy.

## 5. Completion Invariant

```text
COMMAND-ISSUED != PENDING != COMPLETE
```

A command being accepted, a pending object being observed, or a placement request being issued is not sufficient evidence that the intended building exists in the required world state.

`BYZ-VERIFY-CONFIRMED` requires an admissible world-state observation satisfying the active verification predicate.

## 6. Pending Interface

The verifier may consume engine-visible pending concepts corresponding to:

```text
BYZ-PENDING-OBJECT
BYZ-PENDING-PLACEMENT
```

These are intermediate evidence states only.

## 7. Expected/Observed Reconciliation

The verifier compares:

```text
EXPECTED-CONSTRUCTION-STATE
EXPECTED-WORLD-STATE
```

against:

```text
OBSERVED-CONSTRUCTION-STATE
OBSERVED-WORLD-STATE
```

Contradiction produces:

```text
BYZ-VERIFY-CONTRADICTED
 -> BYZ-VERIFY-RECONCILE
```

## 8. Progression Boundary

Only `BYZ-VERIFY-CONFIRMED` may authorize advancement of `BYZ-BUILD-PROGRESS`.

The verifier does not choose the next building or strategic objective.

## 9. Failure Semantics

The verifier SHALL distinguish at minimum:

```text
NOT-YET-VERIFIED
PENDING
FAILED
CONFIRMED
CONTRADICTED
```

A missing observation must not automatically be converted into failure, and failure must not be converted into completion.

## 10. Provenance

Verification SHOULD retain the evidence class and observation responsible for its decision so that progression can be audited after execution.

## 11. Authority Boundary

Verification may confirm, reject, contradict, and request reconciliation. It SHALL NOT issue construction commands, release capital as a side effect, or invent a strategic objective.

## 12. Numeric Namespace Policy

No goal ID, state ID, threshold, timer, count, distance, percentage, or builder allocation is assigned.
