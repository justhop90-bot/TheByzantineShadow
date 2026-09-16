# Module 09 — Capital: Shadow Mirror + AI Encyclopedia Audit v0.1

## Scope

This audit treats `09_capital.per` as an AEGIS design artifact and compares it simultaneously against:

1. the verified Shadow escrow/economic patterns retained in the project corpus;
2. the AoE2/UserPatch scripting reference and patch notes;
3. the intended AEGIS responsibility boundary.

This is an architectural mirror, not a claim that Shadow contains a file with the same module boundary. Shadow's relevant mechanisms are distributed across its economic/strategy/escrow logic.

## Evidence classes

- **DIRECT** — engine/reference behavior directly documented or directly present in Shadow evidence.
- **COMPOSED** — deterministic calculation from direct facts.
- **AEGIS-GENERALIZATION** — new AEGIS architecture/policy derived from those facts.
- **UNCERTAIN** — requires runtime qualification before promotion.

---

## Executive finding

`09_capital.per` has the correct *responsibility boundary* but contains one **definite arithmetic defect** in its current implementation:

```lisp
(up-modify-goal ... c:min 0)
```

is the wrong operation for flooring a value at zero under the documented UserPatch semantics. The UserPatch history explicitly notes that the min/max math operators were corrected/inverted and that `min` stores the lesser value while `max` stores the greater value. Therefore a floor-at-zero operation requires `c:max 0`, not `c:min 0`. citeturn1search0

This defect occurs in all eight liquid/discretionary calculations.

The Shadow mirror otherwise supports the central observation model: Shadow directly caches resource amounts and escrow amounts into goals, and uses escrow as a strategic commitment mechanism. The AEGIS separation of **gross → committed → liquid → reserve → discretionary** is an AEGIS composition of those primitives, not a direct Shadow implementation.

---

# 1. Header / responsibility boundary

### Current implementation

The module declares:

- gross = current resources;
- committed = current engine escrow;
- liquid = gross − committed;
- reserve = policy output from Module 07;
- discretionary = liquid − reserve;
- transaction demand = Module 08 output;
- feasibility = discretionary >= demand.

### Audit

**STATUS: CONFIRMED architectural separation.**

This is the correct boundary for Module 09.

It does not own:

- objective selection;
- reserve policy;
- cost construction;
- escrow mutation;
- release;
- authority;
- execution;
- verification.

That separation is consistent with the AEGIS control model.

**Evidence:** AEGIS-GENERALIZATION.

### Shadow mirror

Shadow does not expose this exact nine-module decomposition. Instead, the relevant behavior is distributed. Shadow directly reads resource and escrow state, modifies escrow allocations, changes escrow percentages according to strategy, and releases escrow when commitments are no longer required.

The important mirrored primitive is therefore:

```text
ENGINE RESOURCE STOCK
        +
ENGINE ESCROW STOCK
        ↓
STRATEGIC ECONOMIC STATE
```

not a literal Shadow `09_capital.per` file.

---

# 2. Gross resource observation

Current block:

```lisp
(up-get-fact food-amount 0 AEGIS-GROSS-FOOD)
(up-get-fact wood-amount 0 AEGIS-GROSS-WOOD)
(up-get-fact gold-amount 0 AEGIS-GROSS-GOLD)
(up-get-fact stone-amount 0 AEGIS-GROSS-STONE)
```

### Audit

**STATUS: CORRECT.**

`food-amount`, `wood-amount`, `gold-amount`, and `stone-amount` are documented AI facts. `up-get-fact` is explicitly documented as an action that reads a fact into a goal. citeturn2search0turn0search3

This is also directly mirrored by Shadow's resource cache pattern.

**Evidence:** DIRECT.

### Important semantic point

`AEGIS-GROSS-*` is not an independent accounting ledger. It is a cached observation of the engine's resource facts.

That distinction should remain explicit.

---

# 3. Engine escrow observation

Current block:

```lisp
(up-get-fact escrow-amount food AEGIS-COMMITTED-FOOD)
(up-get-fact escrow-amount wood AEGIS-COMMITTED-WOOD)
(up-get-fact escrow-amount gold AEGIS-COMMITTED-GOLD)
(up-get-fact escrow-amount stone AEGIS-COMMITTED-STONE)
```

### Audit

**STATUS: CORRECT.**

`escrow-amount` is a documented fact for the computer player's escrow stockpile. `up-get-fact` can store it in a goal. citeturn2search1turn2search0

### Shadow mirror

This is one of the strongest direct Shadow parallels. Shadow explicitly caches escrow amounts into resource-specific goals alongside food/wood/gold/stone totals.

**Evidence:** DIRECT Shadow + DIRECT engine/reference.

### Architectural consequence

Calling this state **COMMITTED** is an AEGIS semantic interpretation of the engine's escrow mechanism. The engine itself supplies `escrow-amount`; AEGIS supplies the accounting interpretation.

**Evidence:** AEGIS-GENERALIZATION built from DIRECT engine state.

---

# 4. Liquid capital

Intended formula:

```text
LIQUID = GROSS - COMMITTED
```

Current implementation pattern:

```lisp
(up-modify-goal AEGIS-LIQUID-FOOD c:= AEGIS-GROSS-FOOD)
(up-modify-goal AEGIS-LIQUID-FOOD c:- AEGIS-COMMITTED-FOOD)
(up-modify-goal AEGIS-LIQUID-FOOD c:min 0)
```

and equivalent blocks for wood, gold, and stone.

### First two operations

**STATUS: CORRECT.**

`c:=` copies the constant's numeric value into the destination goal, and `c:-` subtracts the constant value. Goal arithmetic is directly documented. citeturn0search1turn0search6

### Third operation — DEFECT

**STATUS: DISPROVEN / MUST CHANGE.**

The code intends:

```text
max(GROSS - COMMITTED, 0)
```

but uses:

```lisp
c:min 0
```

The UserPatch documentation records the historical min/max correction and states that the corrected semantics make `min` retain the lesser value and `max` the greater value. Thus:

```lisp
c:min 0
```

forces a positive liquid value down to zero rather than flooring a negative value at zero. citeturn1search0

The intended operation is:

```lisp
(up-modify-goal AEGIS-LIQUID-FOOD c:max 0)
```

and equivalently for wood, gold, and stone.

**This is a concrete implementation defect, not an architectural disagreement.**

---

# 5. Discretionary capital

Intended formula:

```text
DISCRETIONARY = max(LIQUID - RESERVE, 0)
```

Current pattern:

```lisp
(up-modify-goal AEGIS-DISCRETIONARY-FOOD c:= AEGIS-LIQUID-FOOD)
(up-modify-goal AEGIS-DISCRETIONARY-FOOD c:- AEGIS-RESERVE-FOOD)
(up-modify-goal AEGIS-DISCRETIONARY-FOOD c:min 0)
```

### Audit

First two operations: **CORRECT.**

Final operation: **same definite min/max defect as liquid capital.**

It must use:

```lisp
c:max 0
```

not `c:min 0`. citeturn1search0

### Shadow mirror

Shadow clearly demonstrates strategic protection of resources through escrow allocation/percentage policy and selective release. However, the exact AEGIS concept of a separate non-escrow `RESERVE` layer is not a direct Shadow fact.

Therefore:

```text
LIQUID → RESERVE → DISCRETIONARY
```

is **AEGIS-GENERALIZATION**, not DIRECT Shadow behavior.

That distinction should remain in the evidence ledger.

---

# 6. Demand-active state

Current rules mark demand active for:

- RESERVING
- READY
- EXECUTING

and inactive for:

- IDLE
- COMPLETE
- FAILED

### Audit

**STATUS: ARCHITECTURALLY SOUND, BUT AEGIS-GENERALIZATION.**

There is no engine fact saying that these transaction states define capital-demand activity. These are AEGIS lifecycle states.

The design is internally coherent because capital feasibility should not remain actionable after a transaction has reached a terminal state.

### Potential temporal issue

A COMPLETE or FAILED transaction can still have escrow in the process of being released. Therefore `DEMAND-ACTIVE = INACTIVE` does **not** mean that committed capital has already returned to liquid capital.

That is correct if Module 10 owns escrow release and Module 15 owns lifecycle closure.

It would be incorrect to use `DEMAND-ACTIVE` as evidence that escrow has been released.

**Evidence:** AEGIS-GENERALIZATION.

---

# 7. Capital feasibility

Intended rule:

```text
DISCRETIONARY FOOD >= DEMAND FOOD
AND
DISCRETIONARY WOOD >= DEMAND WOOD
AND
DISCRETIONARY STONE >= DEMAND STONE
AND
DISCRETIONARY GOLD >= DEMAND GOLD
```

### Audit

The current implementation uses goal comparisons through `goal ... g:>= ...` and `g:<`.

**STATUS: CORRECT syntax model.**

The AI scripting references distinguish constant operands (`c:`) from goal operands (`g:`), and `up-compare-goal` is the documented goal-comparison mechanism. citeturn0search1turn0search3

### Semantic audit

**STATUS: CORRECT AEGIS composition.**

A transaction is feasible only when every resource dimension satisfies its corresponding cost demand.

This is stronger and more correct than checking only total resource value because AoE2 transaction costs are resource-specific.

**Evidence:** COMPOSED from DIRECT engine cost/resource facts.

### Inactive case

The explicit rule setting feasibility to insufficient when demand is inactive is good defensive state hygiene.

It prevents a stale previous feasibility result from remaining authoritative after the transaction has ended.

---

# 8. Shadow mirror — what 09 is actually borrowing

| AEGIS 09 concept | Shadow evidence | Classification |
|---|---|---|
| Gross resource cache | Shadow caches food/wood/gold/stone facts | DIRECT |
| Escrow cache | Shadow caches escrow amounts | DIRECT |
| Escrow as committed capital | Shadow treats escrow as strategically allocated capital | COMPOSED |
| Liquid = gross − escrow | AEGIS accounting composition | AEGIS-GENERALIZATION |
| Strategic reserve | Shadow has strategic escrow allocation/release behavior, but not this exact reserve ledger | AEGIS-GENERALIZATION |
| Discretionary capital | AEGIS accounting abstraction | AEGIS-GENERALIZATION |
| Transaction demand | Shadow uses concrete costs/escrow thresholds; AEGIS makes cost demand explicit | COMPOSED / AEGIS-GENERALIZATION |
| Four-dimensional feasibility | Deterministic from resource-specific cost data | COMPOSED |
| Capital-feasibility state | AEGIS transaction-state abstraction | AEGIS-GENERALIZATION |

The correct interpretation is therefore **Shadow-inspired economic substrate, not Shadow transcription**.

---

# 9. AI Encyclopedia / UserPatch contract audit

### Verified commands used by 09

- `up-get-fact` — valid action for reading facts into goals. citeturn0search3turn2search0
- `food-amount`, `wood-amount`, `gold-amount`, `stone-amount` — documented resource facts. citeturn2search0turn2search1
- `escrow-amount` — documented escrow fact. citeturn2search1
- `up-modify-goal` — documented goal arithmetic operation. citeturn0search3turn0search4
- `c:=`, `c:-`, `g:<`, `g:>=` — valid operand/operator model. citeturn0search1
- `c:min` / `c:max` — valid math operators, but their corrected semantics make the current use of `c:min 0` wrong for flooring. citeturn1search0

### No unsupported engine command was found in 09.

The defect is semantic arithmetic, not an invented API.

---

# 10. Performance / rule-firing audit

All observation and arithmetic rules use `(true)` and therefore remain eligible to fire repeatedly.

That is **not inherently invalid**. Shadow uses persistent economic observation patterns of this general type.

However, this creates a runtime consideration:

```text
OBSERVE every pass
→ RECALCULATE every pass
→ WRITE every pass
```

This is acceptable for the POC if the number of rules remains small, but it should not automatically be generalized to a large production architecture. Repeated goal writes can have performance implications in AI scripting; this is documented by broader AI scripting experience and should be runtime-qualified before optimization policy is finalized.

**Status: UNCERTAIN / runtime-performance qualification pending.**

---

# 11. Final disposition

## Definite correction

Eight occurrences require correction:

```text
AEGIS-LIQUID-FOOD   c:min 0 → c:max 0
AEGIS-LIQUID-WOOD   c:min 0 → c:max 0
AEGIS-LIQUID-GOLD   c:min 0 → c:max 0
AEGIS-LIQUID-STONE  c:min 0 → c:max 0

AEGIS-DISCRETIONARY-FOOD   c:min 0 → c:max 0
AEGIS-DISCRETIONARY-WOOD   c:min 0 → c:max 0
AEGIS-DISCRETIONARY-GOLD   c:min 0 → c:max 0
AEGIS-DISCRETIONARY-STONE  c:min 0 → c:max 0
```

## No architectural correction required

The following ownership decisions should remain:

```text
07 → strategic reserve policy
08 → engine transaction cost construction
09 → capital accounting + feasibility
10 → engine escrow commitment/release
11 → authority
12 → execution
13 → verification
14 → failure recovery
15 → lifecycle closure/reassessment
```

## Promotion status

`09_capital.per` should **not** be considered runtime-qualified yet.

It is currently:

- architecture: **PROBABLE / internally coherent**
- engine primitives: **DIRECT / documented**
- Shadow correspondence: **DIRECT for resource/escrow observation; AEGIS-GENERALIZATION for the accounting layers**
- arithmetic implementation: **FAILED pending the eight `c:min` corrections**
- runtime behavior: **UNCERTAIN until executed and inspected in the target AoE2DE build**

The single discovered implementation defect is sufficiently concrete that it should be fixed before any runtime qualification of Module 09.
