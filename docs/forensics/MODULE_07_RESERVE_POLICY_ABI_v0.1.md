# Module 07 Reserve Policy ABI v0.1

## Finding

The repository contains a reserve-policy selector but did not contain a qualified numeric source for the four resource-specific reserve amounts.

The existing Module 07 selected four policy classes from age and military population, then attempted to write undefined constants such as `AEGIS-EARLY-FOOD-RESERVE`. That conflated **policy class metadata** with **policy data**. The numeric reserve values are not recoverable merely from the class names.

The module now selects policy class only and fails closed until an authoritative provider supplies the reserve vector.

## Existing policy-class topology

The current selector is preserved:

| Engine state | Policy class |
|---|---|
| Dark Age | EARLY |
| Feudal + military population < 6 | DEVELOPMENT |
| Feudal + military population >= 6 | MILITARY |
| Castle + military population < 12 | DEVELOPMENT |
| Castle + military population >= 12 | MILITARY |
| Imperial | LATE |

These predicates are existing module behavior, not newly invented numeric policy values. fileciteturn145file0

## ABI

The central constant registry now reserves:

| Symbol | ID | Semantic type |
|---|---:|---|
| `AEGIS-RESERVE-POLICY-SOURCE` | 574 | policy-source metadata slot |
| `AEGIS-RESERVE-POLICY-READY` | 575 | provider handshake/state |
| `AEGIS-RESERVE-INPUT-FOOD` | 576 | reserve data slot |
| `AEGIS-RESERVE-INPUT-WOOD` | 577 | reserve data slot |
| `AEGIS-RESERVE-INPUT-GOLD` | 578 | reserve data slot |
| `AEGIS-RESERVE-INPUT-STONE` | 579 | reserve data slot |
| `AEGIS-CAPITAL-RESERVE-STATE` | 580 | reserve-adjusted capital state |
| `AEGIS-DISCRETIONARY-SLACK-FOOD` | 581 | computed slack |
| `AEGIS-DISCRETIONARY-SLACK-WOOD` | 582 | computed slack |
| `AEGIS-DISCRETIONARY-SLACK-GOLD` | 583 | computed slack |
| `AEGIS-DISCRETIONARY-SLACK-STONE` | 584 | computed slack |
| `AEGIS-RESERVE-CAPITAL-FEASIBILITY` | 585 | reserve-adjusted result |

The existing 471–474 goals remain the AEGIS resource-specific reserve vector consumed by the broader architecture. The new 576–579 slots are the **provider input boundary**, allowing the source of the values to be identified separately from their applied state.

## Provider contract

A future authoritative provider must perform this sequence:

```text
policy class selected
       ↓
resolve authoritative policy data
       ↓
populate F/W/G/S provider slots
       ↓
validate vector completeness
       ↓
READY = BOUND
       ↓
Module 09 may perform reserve-adjusted feasibility
```

Selecting `EARLY`, `DEVELOPMENT`, `MILITARY`, or `LATE` does **not** imply any particular reserve amount.

## Capital semantics

Gross capital remains:

```text
GROSS_SLACK(resource)
    = CURRENT_RESOURCE(resource) - TRANSACTION_COST(resource)
```

Reserve-adjusted discretionary capacity must eventually be:

```text
DISCRETIONARY(resource)
    = CURRENT_RESOURCE(resource) - RESERVE(resource)
```

and authorization must require:

```text
CURRENT_RESOURCE
    - TRANSACTION_COST
    - RESERVE
    >= 0
```

for all four resources.

The existing Module 09 implementation currently qualifies only the gross boundary: engine-derived cost → gross capital feasibility. fileciteturn154file0

## What remains deliberately unresolved

1. **Numeric reserve values:** not assigned.
2. **Authoritative provider:** not assigned.
3. **Shadow donor analogue for the policy vector:** not yet established.
4. **Exact `.per` arithmetic implementation for subtracting the reserve vector:** not promoted until the relevant engine ABI is qualified.
5. **Whether reserve is a static policy vector, age-dependent table, dynamic function, or another Shadow mechanism:** unresolved.

No numeric value should be inserted into 576–579 until the provider is recovered from authenticated Shadow evidence or another explicitly qualified source.

## Safety invariant

Until `AEGIS-RESERVE-POLICY-READY == AEGIS-RESERVE-BOUND`, reserve-adjusted capital feasibility is **UNQUALIFIED** and must not authorize escrow commitment.

This is intentionally a fail-closed ABI boundary, not a missing implementation disguised as a default policy.
