# Module 08 → Module 09 Requirement/Capital Boundary v0.1

## Closed-slice contract

The Spearman vertical slice no longer supplies `60 food + 40 wood` as a policy constant.

Module 08 extension `08_requirements_transaction.per` owns the transaction cost vector. It initializes the UP cost-data block at goals 475–478 and adds exactly one `spearman-line` through `up-add-object-cost`.

Therefore the current engine-defined Spearman cost becomes:

```text
AEGIS-TRANSACTION-FOOD  = 475
AEGIS-TRANSACTION-WOOD  = 476
AEGIS-TRANSACTION-GOLD  = 477
AEGIS-TRANSACTION-STONE = 478
```

The values in those goals are data, not hard-coded prices.

## Module 09 consumption

Module 09 copies that four-goal cost set into the scratch cost-data block 41–44 with `up-add-cost-data`, then invokes `up-get-cost-delta 41`.

The engine consequently computes:

```text
current food - required food
current wood - required wood
current stone - required stone
current gold - required gold
```

Module 09 copies those deltas into its capital slack goals and declares feasibility only when all four are non-negative.

## Boundary ownership

```text
OBJECTIVE / REQUIREMENT
        │
        ▼
MODULE 08
engine object cost
        │
        │ 475–478
        ▼
MODULE 09
cost delta + capital feasibility
        │
        │ AEGIS-CAPITAL-FEASIBILITY
        ▼
MODULE 10
physical escrow mutation
```

No module in this chain hard-codes the Spearman resource price.

## Evidence basis

The UP command contract explicitly defines `up-add-object-cost` as adding a specified number of objects of a specified type to the current cost-data set, and `up-add-cost-data` as combining cost-data sets. `up-get-cost-delta` returns current resources minus current cost data. citeturn0search0turn3search0

The project reference also records that cost data is a four-goal food/wood/stone/gold vector and that `up-get-cost-delta` is independent of escrow. fileciteturn123file0

## Explicit remaining boundary

Strategic-reserve subtraction is not silently fabricated. The existing reserve module contains policy-state references whose numeric policy constants are not presently qualified in the repository. This slice therefore closes the **gross engine-cost → capital-feasibility** boundary first. Reserve-adjusted feasibility remains a separate qualification item.
