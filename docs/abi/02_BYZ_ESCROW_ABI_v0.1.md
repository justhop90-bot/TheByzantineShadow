# Byzantine Escrow ABI v0.1

**Status:** Symbolic contract; implementation values intentionally unassigned.

## 1. Purpose

Defines protected-capital semantics for construction obligations. Escrow is treated as a temporal capital partition: capital may be protected for an obligation without becoming proof that the obligation was executed.

## 2. Owned State

The escrow controller owns:

- `BYZ-ESCROW-STATE`
- reservation status
- committed capital state
- release-request state
- reconciliation state

Construction progression and strategic objective selection remain outside escrow authority.

## 3. Symbolic Escrow States

```text
BYZ-ESCROW-IDLE
BYZ-ESCROW-REQUESTED
BYZ-ESCROW-RESERVING
BYZ-ESCROW-COMMITTED
BYZ-ESCROW-RELEASE-REQUESTED
BYZ-ESCROW-RELEASING
BYZ-ESCROW-RECONCILING
BYZ-ESCROW-RELEASED
BYZ-ESCROW-CANCELLED
BYZ-ESCROW-EXPIRED
BYZ-ESCROW-RECOVERY
```

Numeric state IDs: **UNASSIGNED**.

## 4. Resource Interface

```text
BYZ-RESOURCE-FOOD
BYZ-RESOURCE-WOOD
BYZ-RESOURCE-GOLD
BYZ-RESOURCE-STONE
```

No resource thresholds, reserves, percentages, or caps are assigned.

## 5. Escrow Modes

```text
BYZ-ESCROW-INCLUDED
BYZ-ESCROW-EXCLUDED
```

These are symbolic representations of escrow-aware versus ordinary affordability/execution policy. Engine-facing values remain unassigned.

## 6. Reservation Contract

A reservation identifies:

```text
TRANSACTION
RESOURCE
REQUIRED-CAPITAL
RESERVATION-PRIORITY
RESERVATION-LIFETIME
RELEASE-CONDITION
CANCELLATION-CONDITION
```

A reservation is valid only while its obligation remains valid.

## 7. Lifecycle

```text
IDLE
 -> REQUESTED
 -> RESERVING
 -> COMMITTED
```

Release:

```text
COMMITTED
 -> RELEASE-REQUESTED
 -> RELEASING
 -> RECONCILING
 -> RELEASED
```

Cancellation/expiry:

```text
COMMITTED
 -> CANCELLED / EXPIRED
 -> RECOVERY
 -> RELEASE-REQUESTED
```

## 8. Feasibility Boundary

The ABI distinguishes:

```text
BYZ-CAN-BUILD
BYZ-CAN-BUILD-WITH-ESCROW
```

Neither predicate proves that construction occurred.

## 9. Release Invariant

Issuing an engine release operation establishes only a release request/in-flight state. It does not prove that the escrow balance has actually returned to the expected state.

Therefore:

```text
RELEASE-COMMAND
 !=
RELEASE-COMPLETE
```

Observed/reconciled engine state is required before capital is declared released.

## 10. Protected-Capital Principle

Escrow protects an obligation, not a building category.

If the objective disappears, is superseded, expires, or becomes infeasible, its reservation becomes recoverable subject to reconciliation.

## 11. Priority and Preemption

The ABI permits multiple construction obligations to compete for protected capital. Arbitration may revoke or reduce a lower-authority reservation when policy permits, but escrow itself does not select the strategic winner.

## 12. Numeric Namespace Policy

All of the following remain **UNASSIGNED**:

- goal IDs
- state IDs
- resource thresholds
- reserve amounts
- escrow percentages
- escrow caps
- priorities
- reservation timers
- expiry timers

No numeric value is implied by this ABI.
