# Shadow R07 Rules 1794–1814 — Implementation Ledger v0.1

## Status

**STATIC TRANSPLANT COMMITTED — STATIC QUALIFICATION WORKFLOW ADDED — RUNTIME QUALIFICATION PENDING**

Canonical donor: `ShadowSource.per`

Authenticated Git blob SHA: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

Implementation target: `ShadowByzantine/04_construction.per`

## Source-boundary correction

The requested interval `1794–1814` is **not entirely farm progression** in the canonical donor.

- `1794–1805`: farm progression / progression cursor lifecycle.
- `1806–1814`: immediately following `QHOUSE` construction rules.

The implementation preserves the authenticated interval and its exact order rather than silently relabeling the QHOUSE rules as farm logic.

## Rule-order mapping

| Donor | Implementation | Reads | Writes | Escrow | Pending guard | Command | Completion evidence | Jump |
|---:|---|---|---|---|---|---|---|---|
| 1794 | exact ordered rule | `gl-second-turn`, `gl-strategy`, `gl-escrow-state`, `gl-build-progress`, wood, archery-range | none | escrow-aware feasibility | none | `up-build place-normal ... farm` | none | fall-through → 1795 |
| 1795 | exact ordered rule | dark age, KRUSH, `gl-current-build-item=FARMS`, farm `<4`, wood/housing | none | `release-escrow wood` | farm `<1` | `build farm` | none | →1796 |
| 1796 | exact ordered rule | KRUSH, current item FARMS, farm `>=4` | `gl-build-progress +=1`, disable-self | none | none | none | farm `>=4` | →1797 |
| 1797 | exact ordered rule | KRUSH, farm `<4`, progress `> KrushFarmsNumber` | `gl-build-progress = KrushFarmsNumber` | none | none | none | reconciliation predicate | →1798 |
| 1798 | exact ordered rule | KRUSH, current item != FARMS, progress == `KrushFarmsNumber` | `gl-current-build-item = FARMS` | none | none | none | none | →1799 |
| 1799 | exact ordered rule | dark age, KRUSH, current item FARMS2, farm `<7`, wood/housing | none | `release-escrow wood` | farm `<1` | `build farm` | none | →1800 |
| 1800 | exact ordered rule | KRUSH, current item FARMS2, farm `>=7` | `gl-build-progress +=1`, disable-self | none | none | none | farm `>=7` | →1801 |
| 1801 | exact ordered rule | KRUSH, current item != FARMS2, progress == `KrushFarms2Number` | `gl-current-build-item = FARMS2` | none | none | none | none | →1802 |
| 1802 | exact ordered rule | dark age, FLUSH, current item FARMS, farm `<2` or wood `>=310` | wood escrow percentage `0` | set percentage `0`; release wood | farm `<1` | `build farm` | none | →1803 |
| 1803 | exact ordered rule | FLUSH, current item FARMS, farm `>=2` | `gl-build-progress +=1` | none | none | none | farm `>=2` | →1804 |
| 1804 | exact ordered rule | FLUSH, farm `<2`, progress `> FarmsNumber` | `gl-build-progress = FarmsNumber` | none | none | none | reconciliation predicate | →1805 |
| 1805 | exact ordered rule | FLUSH, current item != FARMS, progress == `FarmsNumber` | wood escrow percentage `LOW-ESCROW`; current item FARMS | set wood percentage `LOW-ESCROW` | none | none | none | →1806 |
| 1806 | exact ordered rule | `true` | none | none | none | `up-assign-builders house 1` | none | →1807 |
| 1807 | exact ordered rule | disabled branch, game-time, fifth-turn, housing | none | none | none | warning chat; `up-assign-builders house 3` | none | →1808 |
| 1808 | exact ordered rule | game-time, housing, population, archery range, escrow-aware house feasibility | placement data | escrow-aware feasibility | house `<1` | `place-control`; placement data | none | →1809 |
| 1809 | exact ordered rule | game-time, housing, population, escrow-aware house feasibility | placement data | escrow-aware feasibility | house `<1` | `place-control`; placement data | none | →1810 |
| 1810 | exact ordered rule | `can-build house` | placement data; disable-self | none | none | `place-control`; assign 2 builders | none | →1811 |
| 1811 | exact ordered rule | house feasibility, civilian population, house count, sheep | placement data; disable-self | none | none | `place-control`; assign 1 builder | house count is only a predicate | →1812 |
| 1812 | exact ordered rule | `true` | generic `goal = 12` | none | none | none | none | →1813 |
| 1813 | exact ordered rule | enemy strategy / town safety | generic `goal = -5` | none | none | none | none | →1814 |
| 1814 | exact ordered rule | house feasibility, housing headroom, population headroom, house count, pending house | placement data; placement strategic numbers | none | house `<1` | `place-control`; assign 1 builder | none | →1815 |

## Completion semantics

The farm completion observers in this slice are exactly:

- rule `1796`: `building-type-count-total farm >= 4`
- rule `1800`: `building-type-count-total farm >= 7`
- rule `1803`: `building-type-count-total farm >= 2`

The reconciliation observers are:

- rule `1797`: farm `<4` while progress exceeds `KrushFarmsNumber`
- rule `1804`: farm `<2` while progress exceeds `FarmsNumber`

These are world-state predicates and progression reconciliation. They are not equivalent to command issuance or pending-object presence.

## Escrow semantics

The slice contains the following explicit escrow operations:

1. `1795`: `release-escrow wood`
2. `1799`: `release-escrow wood`
3. `1802`: `set-escrow-percentage wood 0` followed by `release-escrow wood`
4. `1805`: `set-escrow-percentage wood LOW-ESCROW`

Rule `1794` uses `gl-escrow-state` through the donor's `up-can-build` / `up-build` interface but performs no explicit escrow release.

The implementation does not reinterpret `gl-escrow-state` as a transaction-owner flag.

## Jump semantics

There are **zero explicit `up-jump-rule` operations** in rules `1794–1814`.

Therefore the exact local source-order edges are:

```text
1794→1795→1796→1797→1798→1799→1800→1801→1802→1803→1804→1805
→1806→1807→1808→1809→1810→1811→1812→1813→1814→1815
```

The implementation preserves that sequence.

## Static qualification

`tools/forensics/qualify_r07_1794_1814_implementation.py` performs:

1. canonical Git blob SHA verification;
2. donor rule-count verification (`1956`);
3. balanced `defrule` extraction;
4. exact ordered extraction of donor rules `1794–1814`;
5. ordered extraction of the 21 implementation rules;
6. normalized executable-body comparison;
7. `up-jump-rule` equivalence comparison;
8. source-order qualification.

The workflow `.github/workflows/qualify-r07-1794-1814.yml` runs that qualification on relevant pushes and manual dispatch.

## Runtime gate

Static equivalence does **not** establish AoE2DE runtime equivalence.

Runtime qualification must separately observe:

```text
feasibility
→ escrow mutation/release
→ command issuance
→ pending object
→ actual world object
→ building count
→ progression write
→ re-entry
```

The implementation therefore remains **runtime-unqualified** until an AoE2DE execution/replay demonstrates the corresponding world-state transitions.
