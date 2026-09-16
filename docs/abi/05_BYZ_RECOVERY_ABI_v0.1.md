# Byzantine Recovery ABI v0.1

**Status:** Symbolic contract; implementation values intentionally unassigned.

## 1. Purpose

Defines recovery when construction intent, escrow state, placement state, progression, or observed world state diverge. Recovery is a control-plane function, not an alternative execution path.

## 2. Owned State

Recovery owns:

- recovery status
- recovery cause
- rollback/requeue decision
- cancellation/expiry handling
- recovery handoff to escrow
- re-entry conditions

It does not invent strategic objectives or directly execute construction.

## 3. Recovery Causes

```text
BYZ-RECOVERY-CONSTRUCTION-FAILED
BYZ-RECOVERY-PLACEMENT-FAILED
BYZ-RECOVERY-PENDING-STALE
BYZ-RECOVERY-VERIFICATION-CONTRADICTION
BYZ-RECOVERY-OBJECTIVE-CANCELLED
BYZ-RECOVERY-OBJECTIVE-EXPIRED
BYZ-RECOVERY-ESCROW-STALLED
BYZ-RECOVERY-CAPITAL-CONFLICT
BYZ-RECOVERY-STRATEGIC-SUPERSEDED
```

## 4. Recovery States

```text
BYZ-RECOVERY-NONE
BYZ-RECOVERY-DETECTED
BYZ-RECOVERY-DIAGNOSING
BYZ-RECOVERY-ROLLBACK
BYZ-RECOVERY-ESCROW-RELEASE
BYZ-RECOVERY-REQUEUE
BYZ-RECOVERY-RETRY
BYZ-RECOVERY-CANCELLED
BYZ-RECOVERY-COMPLETE
```

Numeric state IDs: **UNASSIGNED**.

## 5. Diagnostic Boundary

A recovery event SHALL first identify which state diverged:

```text
STRATEGIC
CONSTRUCTION
CAPITAL/ESCROW
PLACEMENT
EXECUTION
PENDING
WORLD-STATE/VERIFICATION
```

Recovery action must be derived from the diagnosed divergence rather than from a generic retry.

## 6. Recovery Actions

The symbolic action set is:

```text
BYZ-RECOVER-ROLLBACK
BYZ-RECOVER-REQUEUE
BYZ-RECOVER-RETRY
BYZ-RECOVER-RESELECT
BYZ-RECOVER-DEFER
BYZ-RECOVER-CANCEL
BYZ-RECOVER-RELEASE-CAPITAL
BYZ-RECOVER-RECONCILE
```

No retry count, timer, priority, or threshold is assigned.

## 7. Progression Recovery

If the progression cursor claims a milestone unsupported by world-state evidence:

```text
EXPECTED-PROGRESSION != VERIFIED-PROGRESSION
    -> RECOVERY
    -> ROLLBACK / RECONCILE
    -> REQUEUE
```

Rollback target values remain **UNASSIGNED**.

## 8. Escrow Recovery

A failed, cancelled, superseded, or expired construction obligation may request:

```text
ESCROW-COMMITTED
 -> RELEASE-REQUESTED
 -> RELEASING
 -> RECONCILING
 -> RELEASED
```

Recovery SHALL NOT assume that issuing a release command proves capital has already returned.

## 9. Placement Recovery

Placement failure may result in:

```text
RETRY-SAME-TARGET
RESELECT-TARGET
RECALCULATE-PLACEMENT
DEFER
CANCEL
```

No geometric threshold, retry limit, or timeout is assigned.

## 10. Stale Transaction Recovery

An obligation whose strategic validity has expired or been superseded SHALL be capable of losing its construction authority and releasing protected capital.

```text
ACTIVE
 -> STALE
 -> CANCEL / RECOVER
 -> ESCROW RELEASE
 -> CAPITAL AVAILABLE
```

The definition of staleness is unassigned.

## 11. Idempotence Invariant

Repeated recovery evaluation SHALL NOT:

- double-release escrow;
- double-advance progression;
- duplicate construction;
- duplicate builder allocation;
- create multiple active transactions for one recovered obligation.

Recovery therefore acts on observed state and explicit transaction identity, not assumptions about previous command success.

## 12. Re-entry Contract

A recovered transaction may return to `BYZ-CONSTRUCTION-REQUESTED` only after relevant construction, escrow, placement, and verification state has been reconciled.

```text
RECOVERY
 -> RECONCILE
 -> REQUESTED
```

is valid only when the prerequisite state is coherent.

## 13. Authority Boundary

Recovery may rollback progression, cancel stale obligations, request escrow release, invalidate placement, requeue construction, and request retry. It SHALL NOT independently create a new strategic objective.

## 14. Numeric Namespace Policy

No goal ID, state ID, rollback milestone, retry count, timer, escrow percentage, resource threshold, placement distance, builder count, or priority is assigned.
