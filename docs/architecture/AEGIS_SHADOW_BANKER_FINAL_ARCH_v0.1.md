# AEGIS + Shadow Banker Architecture — Final Pass v0.1

**Status:** Architecture baseline; implementation not yet authorized by this document.

**Purpose:** Preserve Shadow's proven economic machinery while adding an AEGIS cognitive/arbitration layer and Byzantine-specific capability economics. This document is deliberately conservative: AEGIS must improve Shadow where evidence supports improvement, not replace functioning Shadow mechanisms for architectural cleanliness.

## 1. Core architectural decision

Shadow remains the economic substrate. AEGIS does not replace Shadow's escrow, resource protection, economic posture, or existing execution machinery unless a concrete defect is demonstrated.

The intended relationship is:

```text
WORLD
  -> OBSERVATION
  -> CLASSIFICATION
  -> CAPABILITY GAP
  -> REQUIREMENT
  -> EXECUTABLE CANDIDATES
  -> ENGINE COST VECTOR
  -> CAPITAL DEMAND
  -> AEGIS ARBITRATION
  -> LOGICAL COMMITMENT
  -> SHADOW ECONOMIC SYSTEM
  -> PHYSICAL ESCROW
  -> AUTHORITY
  -> EXISTING EXECUTOR
  -> WORLD-STATE RESULT
  -> VERIFICATION
  -> CAPABILITY COVERAGE
  -> REASSESSMENT
```

AEGIS supplies cognition, requirement formation, capital arbitration, and verification. Shadow/AiBuilder/Naga remain execution authorities until direct evidence justifies changing that boundary.

## 2. What must be preserved from Shadow

Shadow's strength is not merely that it uses escrow. Its strength is the coupling of strategic state, resource state, military state, timers, and economic behavior. The preserved Shadow corpus contains a large persistent goal/timer/state model and explicitly identifies its strategy, military, economic, scouting, and escrow machinery as interacting systems.

Therefore AEGIS must not mechanically replace:

- Shadow strategy state;
- Shadow escrow behavior;
- Shadow resource protection;
- Shadow release conditions;
- existing economic pacing;
- existing military/scouting executors;
- proven AiBuilder/Naga execution paths.

Any replacement requires a concrete defect plus evidence that the proposed mechanism improves the resulting behavior.

## 3. The five legitimate improvement domains

### 3.1 Explicit capability interpretation

Shadow observes circumstances and turns strategic state into economic behavior. AEGIS should make the intermediate interpretation explicit:

```text
circumstance
  -> capability gap
  -> requirement
  -> economic requirement
```

This is the principal cognitive addition, not a replacement for Shadow's economy.

### 3.2 Cross-capability capital arbitration

When several requirements are simultaneously valid, AEGIS should arbitrate scarce discretionary capital rather than allowing each subsystem to independently consume the same economic capacity.

Priority is not synonymous with spending. A high-priority requirement must still be feasible, executable, and strategically justified.

### 3.3 Civilization-specific marginal economics

Byzantine bonuses change the relative capital efficiency of capability solutions. AEGIS should eventually account for this when evaluating candidate transactions. The target abstraction is not "make more Byzantine units" but:

```text
Byzantine civilization advantage
  -> altered transaction cost
  -> altered capability efficiency
  -> altered capital priority
```

### 3.4 Explicit logical commitment reconciliation

UserPatch exposes physical escrow as resource-level state. It does not provide independent escrow accounts for individual requirements.

Therefore AEGIS may maintain multiple **logical commitments**, but the engine maintains one aggregate physical escrow state per resource.

Required invariant:

```text
aggregate logical commitments ~= physical engine escrow
```

subject to deliberate rounding/granularity and explicitly documented residuals.

### 3.5 Verification-driven reallocation

A command being accepted or queued is not equivalent to a capability being achieved. AEGIS should only treat a commitment as fulfilled after the intended world-state result has been verified. Verified completion can then release/reconcile capital and trigger reassessment.

## 4. Three economic ledgers

### Policy ledger

What the civilization intends to protect:

- strategic reserve;
- optionality floor;
- transition protection;
- threat reserve.

Policy reserve is not automatically engine escrow.

### Commitment ledger

What AEGIS has logically promised to active requirements:

- requirement identity;
- capability rationale;
- resource demand;
- resource committed;
- funding state;
- priority/state;
- validity/fulfillment state.

These are AEGIS interpretations represented through goals and constants, not native engine objects.

### Engine ledger

What UserPatch is physically protecting:

- escrow food;
- escrow wood;
- escrow stone;
- escrow gold.

The engine does not know which logical requirement owns any particular escrowed resource.

## 5. Escrow is a protection mechanism, not an ownership or authority mechanism

The architecture must preserve these distinctions:

```text
policy reserve
  != logical commitment
  != physical escrow
  != authorization
  != execution
  != verification
```

`escrow-included` is an affordability/execution accounting mode. It is not AEGIS authority by itself.

Authority must remain explicit in AEGIS state, followed by an engine-legal execution path.

## 6. Cost-data is the transaction boundary

Where possible, AEGIS must derive transaction demand using UserPatch cost-data rather than duplicating hard-coded resource costs.

The intended chain is:

```text
REQUIREMENT
  -> CANDIDATE TRANSACTION
  -> ENGINE COST DATA
  -> CAPITAL DEMAND
```

UserPatch cost-data uses four consecutive extended goals in this order:

```text
food, wood, stone, gold
```

The cost-data starting goal must be within the documented extended-goal range 41–508.

For `up-add-research-cost`, the complete syntax is a type/operator + technology id + type/operator + count. A two-argument form is incomplete and must not be used.

Canonical example:

```lisp
(up-add-research-cost c: feudal-age c: 1)
```

The exact technology identifier must still be separately qualified against the current AIRef/AI Encyclopedia corpus before implementation.

## 7. Goal namespace correction

Goals are integer state storage, not declared variables. The AI Encyclopedia documents a large goal space in DE and a much smaller extended-goal space under older engines/UserPatch. The critical constraint for UserPatch cost-data is narrower: cost-data consumes four consecutive extended goals, and the documented valid starting range is 41–508.

Therefore the AEGIS registry must distinguish:

1. general logical goal availability;
2. extended-goal availability;
3. four-goal contiguous cost-data blocks;
4. other commands that consume extended goal pairs/quads.

A goal number being unused does **not** by itself make it safe for cost-data.

## 8. Current AEGIS demand registry

The cost-data order must be:

```lisp
(defconst AEGIS-DEMAND-FOOD 486)
(defconst AEGIS-DEMAND-WOOD 487)
(defconst AEGIS-DEMAND-STONE 488)
(defconst AEGIS-DEMAND-GOLD 489)
```

The previous food/wood/gold/stone ordering was incorrect for UserPatch cost-data and must not be implemented.

Because 486–489 are consecutive and within the documented 41–508 range, the block is structurally eligible for cost-data use. This does not yet prove every AEGIS module uses the block safely; cross-module ownership and lifetime must still be audited.

## 9. Requirements module correction

The current conceptual requirement-to-cost layer is directionally correct but its research-cost invocation must be corrected before implementation.

Incorrect/incomplete form:

```lisp
(up-add-research-cost c: feudal-age)
```

Correct shape:

```lisp
(up-add-research-cost c: feudal-age c: 1)
```

The requirement module must also establish a clear cost-data lifecycle:

```text
IDLE
  -> reset cost data
  -> select requirement/candidate
  -> setup cost data
  -> add object/research costs
  -> derive demand/delta
  -> publish demand
```

It must not leave stale cost data from the previous transaction available to capital arbitration.

## 10. Capital module correction

The current capital architecture is correct in ownership, but the arithmetic floor operation identified in the prior audit must be treated as a definite implementation defect.

The liquid/discretionary calculations currently use `c:min 0`. Under the intended floor-at-zero semantics, the operation must be `c:max 0`:

```lisp
(up-modify-goal AEGIS-LIQUID-FOOD c:max 0)
```

and equivalently for all four liquid resources and all four discretionary resources.

The conceptual model remains:

```text
GROSS
  - COMMITTED
  = LIQUID

LIQUID
  - RESERVE
  = DISCRETIONARY
```

with explicit nonnegative flooring.

This is a code defect to correct during implementation, not a reason to redesign the accounting model.

## 11. Byzantine capability economics

The first Byzantine-specific extension should be capability economics, not a new Byzantine build-order tree.

Candidate model:

```text
THREAT / STRATEGIC CONDITION
        -> CAPABILITY GAP
        -> CANDIDATE RESPONSES
        -> ENGINE COST
        -> BYZANTINE RELATIVE EFFICIENCY
        -> CAPITAL PRIORITY
```

Examples of capability classes include:

- anti-cavalry;
- anti-archer;
- anti-infantry;
- defensive survival;
- gold preservation;
- Imperial transition;
- siege response;
- map control;
- decisive late-game power spike.

The objective is not to hard-code one answer. It is to let Byzantine-specific economics alter the relative attractiveness of valid responses.

## 12. Opportunity cost

AEGIS should eventually evaluate not only:

```text
Can this transaction be funded?
```

but also:

```text
What strategic capability is delayed or endangered if this capital is committed here?
```

This should initially be implemented with discrete, auditable priority bands rather than pretending `.per` supports continuous numerical optimization.

## 13. Execution boundary

AEGIS should not become a second executor.

The banker authorizes/allocates a capability requirement. Existing production, construction, military, economy, AiBuilder, or Naga execution paths should perform the concrete transaction until direct evidence demonstrates that an executor is defective or incapable.

Therefore:

```text
AEGIS = cognition + arbitration + authority + verification
existing executors = concrete action
Shadow = economic substrate where proven
```

## 14. Execution capacity is independent of capital capacity

Funding multiple requirements does not imply that the engine can execute all of them in the same rule pass or queue context. UserPatch command semantics and queue behavior must be respected.

Therefore the architecture distinguishes:

```text
CAPITAL FEASIBILITY
  != EXECUTION ADMISSION
```

A funded transaction can remain authorized/pending without being issued until the relevant executor can legally accept it.

## 15. Final architecture

```text
WORLD
  -> OBSERVATION
  -> CLASSIFICATION
  -> CAPABILITY GAP
  -> REQUIREMENT
  -> EXECUTABLE CANDIDATES
  -> ENGINE COST VECTOR
  -> CAPITAL DEMAND
  -> AEGIS ARBITRATION
  -> LOGICAL COMMITMENT
  -> SHADOW ECONOMIC POSTURE
  -> PHYSICAL ESCROW
  -> AUTHORITY
  -> EXISTING EXECUTOR
  -> WORLD-STATE RESULT
  -> VERIFICATION
  -> CAPABILITY COVERAGE
  -> REASSESSMENT
```

### Fundamental rule

> **Shadow remains the economic engine. AEGIS becomes the cognitive and arbitration layer that tells that engine what capability the civilization needs, how urgently it matters, what it costs, what alternatives exist, and what opportunity cost is being accepted.**

## 16. Implementation gate

No implementation should begin from this document alone.

Before touching `.per`:

1. Cross-reference the exact Shadow behavior.
2. Cross-reference AIRef/AI Encyclopedia command semantics.
3. Cross-reference current AEGIS namespace and load order.
4. Verify goal-block ownership and lifetime.
5. Verify cost-data block safety.
6. Verify executor compatibility.
7. Classify each proposed behavior as DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, or UNCERTAIN.
8. Only then write code.
9. Re-audit the implementation against Shadow and AIRef before runtime qualification.

**Evidence status:**
- Shadow substrate preservation: DIRECT / CONFIRMED from retained corpus.
- UserPatch cost-data four-goal order: DIRECT / CONFIRMED.
- `up-add-research-cost` requires technology id plus operation/count: DIRECT / CONFIRMED.
- AEGIS capability arbitration layer: AEGIS-GENERALIZATION.
- Byzantine capability economics: AEGIS-GENERALIZATION grounded in documented civilization economics; implementation details remain to be qualified.
- Capital `c:min 0` defect: DIRECT code audit finding.
