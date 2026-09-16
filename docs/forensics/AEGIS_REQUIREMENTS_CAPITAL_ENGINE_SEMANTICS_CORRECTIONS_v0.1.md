# AEGIS Requirements / Capital Engine-Semantics Corrections v0.1

## Purpose

This artifact records engine-level corrections that must be applied to the AEGIS requirements/capital implementation before further coding. It is intentionally separate from the architecture document so these facts cannot be lost inside higher-level design prose.

## 1. Goals are state storage, not declared variables

A goal is an integer state slot addressed by GoalId. `(goal <GoalId> <Value>)` tests equality. Other comparisons use `up-compare-goal`.

The implementation consequence is important: AEGIS `defconst` declarations name goal IDs; they do not allocate new variables. Goal lifetime, initialization, ownership, and collisions must therefore be audited explicitly.

For UserPatch cost-data, the general goal-space description is not enough. The cost-data commands impose a narrower extended-goal constraint: the starting goal must be within 41–508 and four consecutive goals are consumed.

## 2. Cost-data order is fixed

UserPatch cost-data is stored in four consecutive goals in this order:

```text
food, wood, stone, gold
```

Therefore the AEGIS demand block must be:

```lisp
(defconst AEGIS-DEMAND-FOOD 486)
(defconst AEGIS-DEMAND-WOOD 487)
(defconst AEGIS-DEMAND-STONE 488)
(defconst AEGIS-DEMAND-GOLD 489)
```

The previous food/wood/gold/stone ordering is invalid for the UserPatch cost-data contract.

## 3. `up-setup-cost-data`

Canonical form:

```lisp
(up-setup-cost-data 1 AEGIS-DEMAND-FOOD)
```

The second argument identifies the first of the four consecutive cost-data goals. The block is therefore 486–489.

## 4. `up-add-research-cost`

The command does not have a two-argument form.

Canonical shape:

```lisp
(up-add-research-cost <typeOp> <TechId> <typeOp> <Value>)
```

Example:

```lisp
(up-add-research-cost c: feudal-age c: 1)
```

Therefore an implementation such as:

```lisp
(up-add-research-cost c: feudal-age)
```

is incomplete and must be rejected during static audit.

## 5. `up-add-object-cost`

The same principle applies to object costs:

```lisp
(up-add-object-cost c: spearman c: 1)
```

It adds the specified quantity to the active cost-data set. Negative counts can subtract cost data, according to the documented UserPatch semantics.

## 6. Cost-data lifecycle

Requirements must own a deterministic lifecycle:

```text
reset
  -> setup
  -> add research/object costs
  -> optionally combine cost sets
  -> derive cost delta / publish demand
  -> retire or replace stale demand
```

A transaction must never inherit cost data from the preceding transaction.

## 7. Capital arithmetic

The intended accounting is:

```text
GROSS = observed resource stock
COMMITTED = observed engine escrow
LIQUID = GROSS - COMMITTED
DISCRETIONARY = LIQUID - POLICY RESERVE
```

Both LIQUID and DISCRETIONARY must be floored at zero.

Under the relevant goal math semantics, the floor operation is:

```lisp
(up-modify-goal AEGIS-LIQUID-FOOD c:max 0)
```

not:

```lisp
(up-modify-goal AEGIS-LIQUID-FOOD c:min 0)
```

The same correction applies to all four liquid resources and all four discretionary resources.

## 8. No premature code rewrite

These are semantic corrections, not a license to redesign the modules. Preserve the existing ownership topology:

```text
07 reserve policy
08 transaction/cost construction
09 capital accounting/feasibility
10 engine escrow
11 authority
12 execution
13 verification
14 recovery
15 closure/reassessment
```

Only the demonstrated semantic defects should be changed initially.

## 9. Evidence status

- Goal equality semantics: DIRECT / CONFIRMED from AIRef.
- Extended cost-data range 41–508: DIRECT / CONFIRMED from UserPatch documentation.
- Cost-data order food/wood/stone/gold: DIRECT / CONFIRMED.
- `up-add-research-cost` four-operand structure: DIRECT / CONFIRMED.
- `c:max 0` as the required nonnegative floor: DIRECT / CONFIRMED from goal math semantics and prior module audit.
- AEGIS ownership/lifecycle model: COMPOSED + AEGIS-GENERALIZATION.
