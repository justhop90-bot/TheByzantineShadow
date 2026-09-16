# Byzantine Placement ABI v0.1

**Status:** Symbolic contract; implementation values intentionally unassigned.

## 1. Purpose

Separates construction authorization from target resolution and placement. Shadow demonstrates materially different normal and point-placement paths; this ABI preserves that distinction and adds an explicit control-placement interface without assigning engine-specific numeric values.

## 2. Owned State

Placement owns the semantic state of:

- target selection
- target point
- placement mode
- placement constraints
- placement validity
- placement failure/retry status

Placement does not own strategic construction demand or completion verification.

## 3. Placement Modes

```text
BYZ-PLACE-NORMAL
BYZ-PLACE-POINT
BYZ-PLACE-CONTROL
```

Numeric mappings: **UNASSIGNED**.

## 4. Target States

```text
BYZ-TARGET-NONE
BYZ-TARGET-SEARCHING
BYZ-TARGET-OBJECT
BYZ-TARGET-POINT
BYZ-TARGET-CONTROL
BYZ-TARGET-VALID
BYZ-TARGET-INVALID
```

Numeric state IDs: **UNASSIGNED**.

## 5. Normal Placement Contract

```text
AUTHORIZED
 -> PLACE-NORMAL
 -> PLACEMENT-VALID
 -> EXECUTION-READY
```

Normal placement does not require the point-search pipeline unless its policy explicitly does so.

## 6. Point Placement Contract

Point construction SHALL follow the conceptual sequence:

```text
TARGET-SEARCH
 -> CANDIDATE-SELECTION
 -> POINT-EXTRACTION
 -> TARGET-POINT-SET
 -> PLACEMENT-VALIDATION
 -> EXECUTION-READY
```

The interface may map to engine primitives such as target search, point extraction, target-point assignment, and point construction, but this ABI does not hard-code their numeric parameters.

## 7. Controlled Placement Contract

Controlled placement SHALL support a separate policy path:

```text
CONTROL-DATA
 -> CONSTRAINT-CONFIGURATION
 -> TARGET-VALIDATION
 -> EXECUTION-READY
```

Symbolic policy fields:

```text
BYZ-PLACEMENT-DATA
BYZ-PLACEMENT-ZONE
BYZ-PLACEMENT-FAIL-POLICY
BYZ-PLACEMENT-SEPARATION-POLICY
BYZ-PLACEMENT-ADJACENCY-POLICY
```

## 8. Validation Boundary

Before execution, placement SHALL establish, to the extent observable:

```text
TARGET-EXISTS
TARGET-IS-VALID
PLACEMENT-CONSTRAINTS-SATISFIED
CONSTRUCTION-AUTHORITY-STILL-VALID
```

A failed target SHALL become `BYZ-TARGET-INVALID` / placement failure rather than being treated as a successful build.

## 9. Builder Interface

Placement may calculate or request a builder policy:

```text
BYZ-BUILDER-POLICY
```

Actual builder counts remain **UNASSIGNED** and belong to execution policy.

## 10. Recovery Interface

Placement failure may request one of:

```text
RETRY-SAME-TARGET
RESELECT-TARGET
RECALCULATE-PLACEMENT
DEFER
CANCEL
```

The retry count, timeout, distance, zone size, fail delta, and separation values remain **UNASSIGNED**.

## 11. Authority Boundary

Placement prepares an executable target. It does not:

- select strategic objectives;
- grant construction authority;
- release escrow by itself;
- declare construction complete;
- advance construction progression.

## 12. Numeric Namespace Policy

No goal ID, state ID, placement distance, zone size, failure delta, separation distance, builder count, timer, or other threshold is assigned.
