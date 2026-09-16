# Byzantine Construction ABI v0.1

**Status:** Symbolic contract; implementation values intentionally unassigned.

## 1. Purpose

Defines the interface for infrastructure construction from strategic demand through verified world-state completion. The contract preserves the verified Shadow relationship:

`demand -> current item -> progression gate -> feasibility -> capital/escrow -> placement -> builder allocation -> execution -> pending -> verification -> progression/recovery`

This document defines relationships and ownership only. It assigns no numeric namespace values.

## 2. Owned State

The construction controller owns the semantic state of:

- `BYZ-CURRENT-BUILD-ITEM`
- `BYZ-BUILD-PROGRESS`
- `BYZ-PROGRESSION-PAUSE`
- `BYZ-CONSTRUCTION-STATE`

Candidate construction demand is not equivalent to an active construction transaction.

## 3. Symbolic Construction States

```text
BYZ-CONSTRUCTION-IDLE
BYZ-CONSTRUCTION-REQUESTED
BYZ-CONSTRUCTION-QUALIFIED
BYZ-CONSTRUCTION-RESERVED
BYZ-CONSTRUCTION-AUTHORIZED
BYZ-CONSTRUCTION-PLACEMENT
BYZ-CONSTRUCTION-EXECUTING
BYZ-CONSTRUCTION-PENDING
BYZ-CONSTRUCTION-VERIFYING
BYZ-CONSTRUCTION-COMPLETE
BYZ-CONSTRUCTION-FAILED
BYZ-CONSTRUCTION-EXPIRED
BYZ-CONSTRUCTION-RECOVERY
```

Numeric state IDs: **UNASSIGNED**.

## 4. Construction Request ABI

Every active request conceptually contains:

```text
BUILDING
STRATEGIC-REASON
PRIORITY
REQUIREMENTS
RESOURCE-REQUIREMENTS
ESCROW-POLICY
PLACEMENT-POLICY
BUILDER-POLICY
EXPIRY-POLICY
VERIFICATION-POLICY
```

The request is data for arbitration/authorization, not an execution command.

## 5. State Transitions

Forward:

```text
IDLE -> REQUESTED
REQUESTED -> QUALIFIED
QUALIFIED -> RESERVED
RESERVED -> AUTHORIZED
AUTHORIZED -> PLACEMENT
PLACEMENT -> EXECUTING
EXECUTING -> PENDING
PENDING -> VERIFYING
VERIFYING -> COMPLETE
```

Exceptional:

```text
REQUESTED -> EXPIRED
QUALIFIED -> FAILED
RESERVED -> FAILED
AUTHORIZED -> FAILED
PLACEMENT -> FAILED
EXECUTING -> FAILED
PENDING -> FAILED
VERIFYING -> FAILED
FAILED -> RECOVERY
EXPIRED -> RECOVERY
RECOVERY -> REQUESTED
```

## 6. Feasibility Boundary

Construction feasibility is an authorization input, not a completion signal.

The implementation may expose symbolic predicates equivalent to:

```text
BYZ-CAN-BUILD
BYZ-CAN-BUILD-WITH-ESCROW
```

Neither predicate establishes that a building exists in the world.

## 7. Execution Boundary

Only the execution authority may issue construction commands:

```text
build
up-build
up-assign-builders
```

Strategic demand, requirements, escrow, placement, and verification modules SHALL NOT independently issue those commands.

## 8. Progression Invariant

`ENGINE-COMMAND-ISSUED != CONSTRUCTION-COMPLETE`.

`PENDING != CONSTRUCTION-COMPLETE`.

`CONSTRUCTION-COMPLETE` requires verification evidence from the world-state verifier.

Only verified completion may advance `BYZ-BUILD-PROGRESS`.

## 9. Reconciliation

If the observed world state contradicts the active progression cursor, the controller SHALL enter reconciliation/recovery rather than advancing blindly.

```text
EXPECTED-STATE != OBSERVED-STATE
    -> RECONCILIATION
    -> ROLLBACK / REQUEUE / CANCEL
```

## 10. Numeric Namespace Policy

The following remain deliberately unassigned:

- goal IDs
- state IDs
- construction milestone values
- resource thresholds
- priority values
- timers and expiry intervals
- escrow percentages/caps
- builder counts
- placement distances and geometry thresholds

No value is to be inferred from this ABI.
