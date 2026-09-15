# The Byzantine Shadow — System 09: Market & Resource Exchange Forensic Engineering v0.1

**Status:** Forensic engineering specification  
**System:** 09 — Market / Resource Exchange / Liquidity  
**Predecessors:** System 01 — Initialization / Configuration; System 02 — State Namespace / Authority; System 03 — Target Acquisition; System 04 — Scouting / Information Acquisition; System 05 — Food Logistics; System 06 — Villager Economy / Labor Allocation; System 07 — Construction / Infrastructure; System 08 — Research / Technology  
**Primary disposition:** PRESERVE + IMPROVE  
**Evidence standard:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN  
**Source donor:** Shadow donor corpus previously audited; exact rule-level attribution must be re-established against the frozen donor before implementation.

---

# 0. Purpose and forensic standard

System 09 isolates the Shadow donor's **market and resource-exchange boundary**: the machinery that converts an authorized liquidity requirement into a bounded market transaction, while preserving resource commitments, affordability, age/technology prerequisites, transaction ordering, and post-transaction reconciliation.

The economic audit establishes that Shadow contains food, wood, gold, and stone trading logic using age-sensitive need/excess/trading thresholds. The important architectural interpretation is that this machinery is **liquidity management**, not an independent strategic objective. fileciteturn43file0L2-L2

The central engineering conclusion is:

> **Market activity is a resource-conversion transaction whose legitimacy depends on an explicit liquidity requirement, opportunity cost, affordability state, transaction authority, and observed economic consequence.**

A market command is not itself proof that a useful exchange occurred. Likewise, a resource shortage is not automatically proof that selling or buying is strategically correct.

System 09 therefore preserves the donor's market/exchange machinery while imposing the same commitment, transaction, authority, verification, and reconciliation model established by Systems 01–08.

---

# 1. Executive finding

The market subsystem should be treated as a **liquidity actuator**, not as a strategic planner and not as a generic emergency resource faucet.

The canonical architecture is:

```text
RESOURCE / CAPABILITY REQUIREMENT
        ↓
LIQUIDITY DEFICIT OR SURPLUS
        ↓
EXCHANGE CANDIDATE
        ↓
STRATEGIC / ECONOMIC AUTHORIZATION
        ↓
LIQUIDITY COMMITMENT
        ↓
RESOURCE PROTECTION / RESERVATION CHECK
        ↓
MARKET FEASIBILITY
        ↓
TRANSACTION AUTHORIZATION
        ↓
MARKET COMMAND
        ↓
OBSERVED RESOURCE / MARKET STATE CHANGE
        ↓
TRANSACTION VERIFICATION
        ↓
RESOURCE RECONCILIATION
        ↓
COMMITMENT UPDATE
        ↓
REASSESSMENT
```

This explicitly rejects the false equivalences:

```text
RESOURCE SHORTAGE → SELL SOMETHING
```

and:

```text
MARKET COMMAND → RESOURCE ACQUIRED
```

and:

```text
AFFORDABLE TRADE → STRATEGICALLY CORRECT TRADE
```

The market must be subordinate to the economic and strategic control planes.

**Disposition:** preserve donor market thresholds and transaction interfaces where directly supported; formalize liquidity requirements and exchange commitments; make protected-resource ownership explicit; prevent market activity from consuming strategic reservations; qualify one narrow buy/sell vertical slice before broad transplantation.

---

# 2. System boundary

## 2.1 In scope

System 09 owns the forensic/design boundary for:

1. liquidity requirements;
2. market transaction candidates;
3. resource-to-resource exchange decisions after higher-level authorization;
4. buy/sell feasibility;
5. age and prerequisite gating for market access;
6. market resource protection;
7. exchange transaction preparation;
8. market command interfaces;
9. observed resource-state changes;
10. transaction verification;
11. transaction retry and failure handling;
12. residual reservation reconciliation;
13. liquidity hysteresis;
14. emergency liquidity policy interfaces;
15. interaction with Shadow escrow and commitments;
16. interaction with System 06 labor/resource allocation;
17. interaction with Systems 07 and 08 when infrastructure/research creates a liquidity requirement;
18. market starvation/deadlock telemetry;
19. exchange opportunity-cost accounting.

## 2.2 Explicitly out of scope

System 09 does not own:

- global strategic doctrine;
- target-player selection;
- scouting;
- military composition selection;
- final strategic priority;
- general villager allocation;
- construction execution;
- research execution;
- production execution;
- unrestricted resource conversion;
- strategic commitment arbitration.

System 09 may identify that an authorized transaction is economically infeasible and may report a liquidity deficit. It must not silently invent the strategic requirement that justifies the trade.

---

# 3. Evidence hierarchy

### DIRECT

A market command, market predicate, trade threshold, resource condition, age condition, state carrier, escrow operation, jump, ordering rule, or release operation is explicitly present in the donor.

### COMPOSED

Multiple direct mechanisms establish an exchange policy or transaction lifecycle when their interaction is structurally demonstrated.

### INFERRED

The economic purpose of a threshold or market branch is strongly suggested by surrounding state but is not explicitly declared.

### AEGIS-GENERALIZATION

A design requirement introduced to make exchange attributable, auditable, commitment-safe, reversible, and compatible with AEGIS.

### UNCERTAIN

The evidence is insufficient to establish exact semantic meaning, exchange coefficients, engine lifecycle, or strategic effect.

Mandatory rule:

> **Do not infer liquidity policy from a single market condition, and do not infer resource acquisition from command issuance.**

Donor thresholds are evidence of donor behavior; they are not automatically optimal AEGIS coefficients.

---

# 4. Liquidity is not resource abundance

System 09 must distinguish at least five economic concepts:

```text
GROSS RESOURCE
PROTECTED RESOURCE
COMMITTED RESOURCE
LIQUID RESOURCE
ACQUIRED RESOURCE
```

A civilization may possess a large gross stock of a resource while having little genuinely liquid resource because commitments and policy protection consume the available envelope.

Conceptually:

```text
LIQUID RESOURCE
= GROSS RESOURCE
  − POLICY PROTECTION
  − ACTIVE COMMITMENT RESERVATIONS
  − OTHER GOVERNED HOLDS
```

This is an AEGIS accounting model, not an assertion about hidden engine internals.

The market system must therefore never evaluate exchange solely against raw stockpiles.

Example:

```text
100 WOOD GROSS
40 WOOD COMMITTED TO FARM INFRASTRUCTURE
20 WOOD POLICY-PROTECTED
```

does not mean that 100 wood is available for discretionary exchange.

---

# 5. Liquidity requirement contract

Every strategically meaningful market operation should be represented conceptually as a liquidity requirement.

Minimum fields:

```text
REQUIREMENT_ID
ORIGINATING_OBJECTIVE
TARGET_CAPABILITY
RESOURCE_NEEDED
RESOURCE_TO_SELL
MINIMUM_REQUIRED_AMOUNT
DESIRED_AMOUNT
CURRENT_VERIFIED_STOCK
CURRENT_LIQUID_AMOUNT
PROTECTED_AMOUNT
COMMITTED_AMOUNT
TRUE_LIQUIDITY_DEFICIT
URGENCY
PRIORITY_CONTEXT
CREATION_EPOCH
EXPIRY_CONDITION
INVALIDATION_CONDITION
COMPLETION_CONDITION
OWNER
GENERATION
EVIDENCE_LEVEL
```

The relevant quantity is:

```text
TRUE LIQUIDITY DEFICIT
= REQUIRED LIQUID AMOUNT
  − VERIFIED LIQUID AMOUNT
```

If the deficit is zero, a market transaction is not justified merely because a favorable price or threshold exists.

This requirement is an AEGIS-GENERALIZATION pending complete donor extraction.

---

# 6. Market candidate versus strategic objective

The architecture must distinguish:

```text
STRATEGIC OBJECTIVE
        ≠
LIQUIDITY REQUIREMENT
        ≠
MARKET CANDIDATE
        ≠
MARKET TRANSACTION
        ≠
RESOURCE OUTCOME
```

For example:

```text
NEED MILITARY CAPABILITY
        ↓
NEED GOLD
        ↓
GOLD LIQUIDITY DEFICIT
        ↓
SELL WOOD
```

The final step is not necessarily correct. Alternative funding paths may exist:

- reallocate labor;
- defer another commitment;
- release unnecessary escrow;
- use existing stock;
- construct infrastructure;
- research a different technology;
- trade a different resource;
- delay the underlying requirement.

Therefore the market system evaluates an **authorized exchange candidate**, not the civilization's strategic objective itself.

---

# 7. Buy and sell are separate transaction classes

The implementation must not collapse buying and selling into one undifferentiated market operation.

## Buy

```text
TARGET RESOURCE DEFICIT
→ SOURCE RESOURCE SELECTION
→ SELLABLE SURPLUS / LIQUIDITY CHECK
→ BUY FEASIBILITY
→ TRANSACTION
→ OBSERVED TARGET RESOURCE INCREASE
→ VERIFICATION
```

## Sell

```text
SOURCE RESOURCE SURPLUS
→ TARGET RESOURCE REQUIREMENT
→ PROTECTED / COMMITTED RESOURCE CHECK
→ SELL FEASIBILITY
→ TRANSACTION
→ OBSERVED SOURCE RESOURCE DECREASE
→ TARGET RESOURCE CONSEQUENCE
→ VERIFICATION
```

A sell operation must never treat committed resources as discretionary surplus without explicit preemption or release authority.

A buy operation must never assume that the purchased resource automatically satisfies a strategic requirement; the downstream capability must still be verified by its owning system.

---

# 8. Opportunity cost is a first-class constraint

A market transaction changes the resource composition of the economy.

Therefore the cost of a trade is not limited to the explicit exchange quantity.

Conceptually:

```text
TRADE COST
= EXPLICIT MARKET COST
+ OPPORTUNITY COST
+ COMMITMENT DISPLACEMENT RISK
+ LIQUIDITY BUFFER LOSS
```

The exact numerical formulation is an AEGIS-GENERALIZATION until qualified.

The forensic task must recover donor conditions that implicitly represent:

- resource excess;
- resource shortage;
- minimum reserves;
- age-sensitive needs;
- technology-sensitive needs;
- emergency conditions;
- trade thresholds;
- resource protection.

Do not turn any one threshold into a universal exchange equation without evidence.

---

# 9. Donor threshold extraction

The economic audit establishes that the donor uses age-sensitive need/excess/trading thresholds for food, wood, gold, and stone. fileciteturn43file0L2-L2

These values must be classified individually.

For every threshold, record:

```text
SYMBOL
RESOURCE
OPERATION
VALUE
UNIT / SCALE
AGE CONDITION
READERS
WRITERS
PRECEDENCE
RESET CONDITION
EXPIRY CONDITION
SIDE EFFECTS
EVIDENCE_LEVEL
STATUS
```

Classify each threshold as one of:

```text
RESOURCE FLOOR
RESOURCE CEILING
EXCHANGE TRIGGER
EXCHANGE MAINTAIN
EXCHANGE RELEASE
EMERGENCY THRESHOLD
PROGRESSION THRESHOLD
UNKNOWN
```

Do not assume that a variable called `need`, `excess`, `trade`, `save`, or similar has the same semantic type across the donor.

---

# 10. Market commitment

Once an exchange candidate wins higher-level arbitration, it becomes a liquidity commitment.

Conceptually:

```text
CANDIDATE
→ PREPARING
→ COMMITTED
→ FUNDED / LIQUIDITY AVAILABLE
→ EXECUTING
→ VERIFIED
```

A market commitment must identify:

- commitment ID;
- originating requirement;
- buy/sell direction;
- source resource;
- target resource;
- minimum transaction amount;
- maximum authorized amount;
- minimum reserve remaining;
- creation epoch;
- generation;
- priority;
- completion predicate;
- expiry;
- cancellation predicate;
- retry policy;
- preemption policy;
- owner.

No discretionary market reservation should exist without attributable ownership.

---

# 11. Interaction with Shadow escrow

Market activity is particularly dangerous when combined with escrow because a market sale can make protected resources disappear from the economy's gross stock before their commitments have been satisfied.

The architecture must preserve:

```text
POLICY ESCROW
        ≠
COMMITMENT ESCROW
        ≠
TRANSACTION ESCROW
        ≠
LIQUIDITY
```

A market transaction may only consume a resource after determining whether that resource is:

```text
UNPROTECTED
RELEASABLE
COMMITTED
POLICY-PROTECTED
TRANSACTION-LOCKED
```

If a resource is committed, the market cannot sell it unless the owning authority explicitly releases or preempts that commitment.

This is a direct extension of the ownership contract established by the Shadow economic architecture.

---

# 12. Market preflight

Before issuing a trade, the system should establish all relevant feasibility conditions.

Conceptually:

```text
REQUIREMENT VALID
        ↓
COMMITMENT VALID
        ↓
SOURCE RESOURCE LIQUID
        ↓
MINIMUM RESERVE PRESERVED
        ↓
MARKET ACCESSIBLE
        ↓
AGE / PREREQUISITES SATISFIED
        ↓
TARGET RESOURCE NEED STILL EXISTS
        ↓
TRANSACTION WITHIN AUTHORIZED LIMIT
        ↓
PREFLIGHT PASS
```

Any failed condition must be attributable.

Possible results:

```text
NO_REQUIREMENT
NO_SOURCE_LIQUIDITY
SOURCE_PROTECTED
MINIMUM_RESERVE_VIOLATION
MARKET_UNAVAILABLE
PREREQUISITE_MISSING
TARGET_NO_LONGER_NEEDED
AMOUNT_INVALID
PREEMPTED
EXPIRED
UNKNOWN
```

A failed preflight must not consume commitment funding.

---

# 13. Market transaction lifecycle

System 09 uses the same transaction machine established by the Shadow blueprint:

```text
REQUESTED
→ RESERVING
→ RESERVED
→ PREFLIGHT
→ AUTHORIZED
→ ISSUED
→ OBSERVING
→ CONFIRMED
```

Failure states:

```text
REJECTED
FAILED
PARTIAL
UNVERIFIED
EXPIRED
RELEASED
```

A transaction identity must be immutable after issuance.

For example:

```text
R9 = liquidity requirement
C9 = liquidity commitment
T9-1 = first market transaction
T9-2 = retry
```

Never overwrite `T9-1` with `T9-2`; transaction history is required for forensic reconciliation.

---

# 14. Command acceptance versus economic consequence

The critical market verification boundary is:

```text
MARKET COMMAND ACCEPTED
        ≠
RESOURCE STATE MUTATED
        ≠
TRANSACTION COMPLETED
        ≠
LIQUIDITY REQUIREMENT SATISFIED
        ≠
DOWNSTREAM CAPABILITY ACQUIRED
```

The verifier must observe an appropriate postcondition.

Possible evidence includes:

```text
SOURCE RESOURCE DECREASED
TARGET RESOURCE INCREASED
EXPECTED MARKET STATE CHANGED
AUTHORIZED AMOUNT ACCOUNTED FOR
TRANSACTION COMPLETED
```

A command acknowledgement is W0 evidence at most unless the runtime qualification demonstrates that it carries stronger semantics.

---

# 15. Economic delta accounting

Market verification must account for the complete transaction delta.

Conceptually:

```text
PRE_TRANSACTION_STATE
        ↓
ISSUE
        ↓
POST_TRANSACTION_OBSERVATION
        ↓
RESOURCE DELTA
        ↓
EXPECTED DELTA COMPARISON
```

Record:

```text
RESOURCE_BEFORE
RESOURCE_AFTER
EXPECTED_SOURCE_DELTA
EXPECTED_TARGET_DELTA
OBSERVED_SOURCE_DELTA
OBSERVED_TARGET_DELTA
UNACCOUNTED_DELTA
TRANSACTION_ID
OBSERVED_EPOCH
EVIDENCE_LEVEL
```

If the observed delta does not match the expected transaction, classify the result as `PARTIAL`, `FAIL`, or `UNKNOWN` rather than silently advancing the commitment.

The exact engine accounting semantics require runtime qualification.

---

# 16. Partial trade

A market transaction may produce less useful effect than requested.

Example:

```text
REQUEST: BUY 200 GOLD
OBSERVED: BUY 120 GOLD
```

The correct sequence is:

```text
T9-1 → PARTIAL
        ↓
RECONCILE ACTUAL RESOURCE DELTA
        ↓
REMAINING LIQUIDITY REQUIREMENT = 80 GOLD
        ↓
REASSESS
        ↓
RETRY / ALTERNATIVE FUNDING / CANCEL
```

Do not mark the original requirement satisfied merely because some resource was acquired.

---

# 17. Resource release after trade

Unused or newly unnecessary reservations must be reconciled after a verified transaction.

For example:

```text
RESERVED SOURCE RESOURCE
        ↓
AUTHORIZED SALE
        ↓
ACTUAL SALE
        ↓
UNUSED RESERVATION
        ↓
RELEASE OR RETAIN ACCORDING TO COMMITMENT
```

Release must be attributable.

A global “reset escrow after trade” operation is unsafe unless its ownership and scope are explicitly proven.

This is especially important because the donor already contains deliberate resource-release behavior in its broader progression machinery. fileciteturn43file0L2-L2

---

# 18. Market hysteresis

Market thresholds are inherently prone to oscillation.

A naive controller can produce:

```text
SELL WOOD
→ WOOD LOW
→ STOP SELLING
→ WOOD RECOVERS
→ SELL WOOD
→ WOOD LOW
→ ...
```

or:

```text
BUY GOLD
→ GOLD ABOVE NEED
→ STOP
→ GOLD FALLS BELOW NEED
→ BUY
→ ...
```

System 09 therefore requires distinct:

```text
ACTIVATION THRESHOLD
MAINTAIN THRESHOLD
RELEASE THRESHOLD
PREEMPTION THRESHOLD
MINIMUM DWELL
MINIMUM TRANSACTION SIZE
MAXIMUM TRANSACTION SIZE
MAXIMUM COMMITMENT AGE
```

These are AEGIS-GENERALIZATION fields until donor/runtime evidence establishes exact values.

---

# 19. Emergency liquidity

Emergency liquidity is legitimate but dangerous.

An emergency market policy may be justified by conditions such as:

```text
CRITICAL FOOD FAILURE
CRITICAL MILITARY PRODUCTION BLOCK
CRITICAL INFRASTRUCTURE DEFICIT
CRITICAL RESEARCH WINDOW
SURVIVAL THREAT
```

However, emergency market authority must be:

- explicit;
- bounded;
- attributable;
- reversible;
- time-limited;
- subject to verification;
- subordinate to hard strategic authority.

The donor contains evidence of emergency economic policy, including a town-safety-dependent building cancellation policy. That demonstrates survival-driven capital reallocation, but it does not by itself establish a general market emergency doctrine. fileciteturn43file0L2-L2

Therefore emergency market behavior must be treated as donor evidence plus explicit AEGIS generalization, not as a hidden strategic brain.

---

# 20. Interaction with System 06 — Villager Economy

System 06 owns labor allocation. System 09 owns market transactions.

The interface is:

```text
RESOURCE REQUIREMENT
        ↓
SYSTEM 06: PRODUCE / ALLOCATE RESOURCE
        ↓
OBSERVED RESOURCE FLOW
        ↓
LIQUIDITY REASSESSMENT
        ↓
SYSTEM 09: MARKET IF STILL JUSTIFIED
```

The reverse path is also valid:

```text
LIQUIDITY DEFICIT
        ↓
SYSTEM 09 REPORTS FUNDING GAP
        ↓
SYSTEM 06 MAY REALLOCATE LABOR
        ↓
RESOURCE FLOW INCREASES
        ↓
MARKET REQUIREMENT MAY DISAPPEAR
```

System 09 must not force labor redistribution simply because a market transaction is available.

Conversely, System 06 must not assume that all deficits should be solved through labor allocation if an authorized market transaction is the better funding path.

The final arbitration belongs above both systems.

---

# 21. Interaction with construction and research

Construction and research may generate temporary liquidity requirements.

Example:

```text
SYSTEM 07
FARM REQUIREMENT
        ↓
WOOD DEFICIT
        ↓
SYSTEM 09 LIQUIDITY CANDIDATE
        ↓
SELL AUTHORIZED SURPLUS RESOURCE
        ↓
WOOD ACQUIRED
        ↓
SYSTEM 07 REASSESSMENT
```

Similarly:

```text
SYSTEM 08
TECHNOLOGY COMMITMENT
        ↓
GOLD DEFICIT
        ↓
SYSTEM 09 LIQUIDITY CANDIDATE
        ↓
AUTHORIZED EXCHANGE
        ↓
GOLD ACQUIRED
        ↓
SYSTEM 08 REASSESSMENT
```

The downstream system remains responsible for determining whether its own requirement is actually satisfied.

Market completion does not equal construction or research completion.

---

# 22. Interaction with production

Production is a major consumer of liquidity.

The interface is:

```text
PRODUCTION AUTHORITY
        ↓
RESOURCE REQUIREMENT
        ↓
SHADOW COMMITMENT
        ↓
CURRENT LIQUIDITY DEFICIT
        ↓
MARKET CANDIDATE
        ↓
MARKET TRANSACTION
        ↓
VERIFIED RESOURCE ACQUISITION
        ↓
PRODUCTION REASSESSMENT
```

This prevents the common architectural error:

```text
UNIT WANTED → MARKET BUY → TRAIN UNIT
```

without an explicit commitment, funding limit, verification boundary, or strategic arbitration.

---

# 23. Market and commitment preemption

A market commitment may itself be preempted if the originating strategic requirement disappears or a higher-priority commitment changes the resource allocation policy.

Sequence:

```text
ACTIVE MARKET COMMITMENT
        ↓
REQUIREMENT INVALIDATED / HIGHER PRIORITY COMMITMENT
        ↓
STOP NEW MARKET FUNDING
        ↓
RECONCILE RESERVED SOURCE RESOURCE
        ↓
RELEASE UNNEEDED RESERVATION
        ↓
MARKET COMMITMENT SUSPENDED / CANCELLED
        ↓
REASSESS
```

A market transaction already issued cannot be assumed cancellable merely because its commitment was preempted.

Logical authority and engine transaction interruption are separate questions.

---

# 24. Market deadlock

Market deadlock occurs when exchange logic repeatedly attempts to solve a liquidity problem that the exchange itself cannot safely solve.

Examples:

```text
NEED GOLD
→ GOLD LOW
→ WOOD IS COMMITTED
→ STONE IS ALSO PROTECTED
→ NO SELLABLE SURPLUS
→ MARKET RETRIES
→ NOTHING CHANGES
```

or:

```text
BUY GOLD
→ NEED FOOD TO SUPPORT VILLAGERS
→ FOOD COMMITTED
→ MARKET SOURCE INSUFFICIENT
→ BUY RETRIES FOREVER
```

The system must expose:

```text
NO_LIQUID_SOURCE
SOURCE_PROTECTED
TARGET_NOT_NEEDED
MARKET_UNAVAILABLE
TRANSACTION_UNVERIFIED
REPEATED_FAILURE
RESERVATION_STARVATION
DEADLOCK
```

Repeated identical preflight failure without meaningful state change must not create an infinite transaction loop.

---

# 25. Market starvation

Track at least:

- age of unresolved liquidity requirement;
- age of active market commitment;
- number of failed transactions;
- number of partial transactions;
- source-resource starvation age;
- target-resource starvation age;
- protected-resource concentration;
- market retry count;
- time since last successful exchange;
- percentage of gross resources unavailable to discretionary exchange.

A long-lived liquidity requirement with no viable exchange candidate should be reported upward as an economic feasibility problem, not hidden as a perpetual market attempt.

---

# 26. Donor rule-order and jump arbitration

The Shadow blueprint establishes that `up-jump-rule` and rule order act as procedural arbitration for production/research branches. The same forensic question must be applied to market rules. fileciteturn45file0L2-L2

For every market branch, recover:

```text
PRECEDING RULES
FOLLOWING RULES
JUMP TARGET
JUMP CONDITION
STATE WRITES
STATE READS
RESOURCE SIDE EFFECTS
ESCROW SIDE EFFECTS
RESET / RELEASE
```

Classify procedural priority as:

```text
EXPLICIT AUTHORITY
IMPLICIT PRECEDENCE
EMERGENCY OVERRIDE
LEGACY ORDERING
UNKNOWN
```

Source order must never be silently promoted to strategic priority.

---

# 27. Market state registry

Every market-related state carrier must be entered into the System 02 registry.

Minimum fields:

```text
SYMBOL
SEMANTIC TYPE
PHYSICAL CHANNEL
OWNER
WRITERS
READERS
INITIAL VALUE
VALID RANGE
UNIT / SCALE
CREATION CONDITION
LIFETIME
RESET CONDITION
EXPIRY CONDITION
INVALIDATION CONDITION
PRECEDENCE
SIDE EFFECTS
EVIDENCE LEVEL
STATUS
```

Likely donor categories include:

```text
RESOURCE NEED
RESOURCE EXCESS
TRADE THRESHOLD
MARKET MODE
BUY/SELL MODE
MARKET COOLDOWN
TRADE AMOUNT
RESOURCE PROTECTION
EMERGENCY ECONOMIC MODE
PROGRESSION LINK
```

Exact symbols and channels must be extracted rather than invented.

---

# 28. Duplicate and conflicting market definitions

The donor contains a large legacy namespace with duplicate definitions. System 09 must not transplant market constants or goals without classification.

Duplicate classes:

```text
LEGITIMATE_CONDITIONAL
LEGITIMATE_SPECIALIZATION
SHADOWED
CONFLICTING
LEGACY
UNKNOWN
```

For each duplicate market definition, establish:

1. which definition is active;
2. under what condition;
3. whether definitions coexist;
4. whether later source order overrides earlier state;
5. whether the values represent different semantic types;
6. whether a duplicate is a generation artifact;
7. whether both definitions can write the same runtime channel.

No conflicting definition may enter the canonical ABI unresolved.

---

# 29. Market bypass governance

Any resource conversion path that bypasses the canonical market commitment machinery must be classified.

Allowed classifications are:

```text
MANDATORY_CORE
EMERGENCY_BYPASS
LOW_COST_UNRESERVED
LEGACY_QUARANTINED
DUPLICATE_EXECUTOR
UNAUTHORIZED
```

Only the first three can survive.

An emergency bypass must still declare:

```text
OWNER
RESOURCE LIMIT
TIME LIMIT
ACTIVATION CONDITION
VERIFICATION
RELEASE / TERMINATION
```

This prevents ordinary market rules from silently bypassing commitment ownership.

---

# 30. Verification model

Verification must be transaction-specific.

## Sell

Minimum candidate evidence:

```text
SOURCE RESOURCE DECREASED
```

Sufficient transaction evidence may additionally require:

```text
EXPECTED TARGET VALUE / MARKET STATE
AUTHORIZED AMOUNT ACCOUNTED FOR
```

## Buy

Minimum candidate evidence:

```text
TARGET RESOURCE INCREASED
```

Sufficient transaction evidence may additionally require:

```text
SOURCE COST ACCOUNTED FOR
AUTHORIZED AMOUNT ACCOUNTED FOR
```

The exact sufficient postcondition must be established per engine behavior.

No market commitment becomes `VERIFIED` solely because the command was accepted.

---

# 31. Evidence levels for market state

Use the project-wide evidence ladder:

```text
W0 = COMMAND / CONTROL ACCEPTANCE
W1 = PENDING / TRANSACTION-ACCEPTED STATE
W2 = OBSERVED WORLD / RESOURCE STATE
W3 = VERIFIED CAPABILITY CONSEQUENCE
W4 = STRATEGIC EFFECT
```

For market activity:

```text
MARKET COMMAND ACCEPTED → W0
RESOURCE DELTA OBSERVED → W2
DOWNSTREAM FEASIBILITY IMPROVED → W3
STRATEGIC REQUIREMENT SATISFIED → W4
```

Do not promote W0 directly to W3 or W4.

---

# 32. First qualification slice

The first runtime qualification should be deliberately narrow.

Recommended slice:

```text
AUTHORIZED GOLD REQUIREMENT
        ↓
KNOWN WOOD SURPLUS
        ↓
SELL-WOOD TRANSACTION
        ↓
MARKET COMMAND
        ↓
OBSERVE WOOD DELTA
        ↓
OBSERVE GOLD DELTA / ECONOMIC CONSEQUENCE
        ↓
VERIFY
        ↓
RECONCILE COMMITMENT
        ↓
REASSESS GOLD REQUIREMENT
```

The qualification must answer:

1. What command is issued?
2. What engine state changes immediately?
3. Is there an observable pending/transaction state?
4. When does the resource delta occur?
5. What exact resource delta occurs?
6. Can the transaction be partially fulfilled?
7. What happens on failure?
8. Can the operation be repeated safely?
9. What state proves completion?
10. What state proves failure?
11. What happens to protected/escrowed resources?
12. Can a higher-priority commitment preempt the market operation?

No broad market transplantation should occur before these questions are answered for the selected path.

---

# 33. Static forensic extraction plan

Before implementation, perform a complete donor extraction of all market-related constructs.

Search and classify at minimum:

```text
buy
sell
market
trade
exchange
need
excess
surplus
shortage
resource thresholds
resource percentages
resource floors
resource ceilings
age gates
market prerequisites
market commands
market affordability
escrow interactions
release operations
up-jump-rule
jumps
progression writes
```

For every matched rule, capture:

```text
FILE
LINE / RULE ID
SYMBOLS READ
SYMBOLS WRITTEN
COMMANDS
RESOURCE SIDE EFFECTS
ESCROW SIDE EFFECTS
PREREQUISITES
ORDER / PRECEDENCE
JUMP TARGET
RESET
COMPLETION CONDITION
FAILURE CONDITION
EVIDENCE LEVEL
DISPOSITION
```

The output should form the System 09 source-to-authority graph.

---

# 34. Runtime qualification plan

Qualification must proceed from control evidence toward world evidence.

### S9-0 — Static extraction

Inventory every market rule and dependency.

### S9-1 — Namespace qualification

Resolve market state symbols, constants, goals, counters, and modes.

### S9-2 — Authority qualification

Identify every writer capable of initiating or cancelling market activity.

### S9-3 — ABI qualification

Determine command argument semantics, resource identifiers, amount semantics, and transaction state channels.

### S9-4 — Lifecycle qualification

Observe:

```text
REQUEST
→ COMMAND
→ STATE MUTATION
→ RESOURCE DELTA
→ VERIFICATION
```

### S9-5 — Failure qualification

Test rejected, insufficient, protected-resource, and unavailable-market conditions where practical.

### S9-6 — Partial-result qualification

Determine whether partial exchange is possible and how it is represented.

### S9-7 — Reconciliation qualification

Verify reservation release and actual resource accounting.

### S9-8 — Vertical slice qualification

Only after S9-0 through S9-7 are understood should the narrow production implementation be considered.

---

# 35. Donor disposition

| Donor mechanism | Disposition | Reason |
|---|---|---|
| Market buy/sell predicates | PRESERVE + FORMALIZE | Reusable feasibility layer |
| Resource need/excess thresholds | EXTRACT + CLASSIFY | Donor policy, not universal truth |
| Age-sensitive market rules | PRESERVE AS POLICY CANDIDATES | Requires contextual qualification |
| Trade amounts | EXTRACT + TUNE | Coefficients require evidence |
| Resource protection | KEEP + ATTRIBUTE | Prevent commitment violation |
| Market commands | KEEP AS EXECUTION INTERFACE | Never strategic authority |
| Escrow interaction | KEEP + CONSTRAIN | Preserve ownership semantics |
| Rule-order priority | EXTRACT + EXPLICITATE | Avoid hidden strategic arbitration |
| `up-jump-rule` market arbitration | EXTRACT + EXPLICITATE | Procedural priority must become declared |
| Emergency trade behavior | ADAPT | Bounded and reversible |
| Duplicate market constants | QUARANTINE | Namespace ambiguity |
| Wholesale donor market namespace | REPLACE | Canonical ABI required |
| Strategic trade selection | REPLACE / AEGIS-OWNED | Market must not become strategic brain |

---

# 36. Anti-patterns

The following are prohibited:

### 36.1 Sell-anything-to-fix-anything

A resource deficit cannot authorize arbitrary sale of another resource.

### 36.2 Treating gross stock as liquid stock

Committed or protected resources are not discretionary liquidity.

### 36.3 Command equals completion

A market command is not an economic postcondition.

### 36.4 Threshold equals strategy

A donor trade threshold is not a strategic objective.

### 36.5 Infinite retry

Repeated failure without state change must produce a bounded failure/deadlock state.

### 36.6 Hidden reservation destruction

Market operations may not silently consume another commitment's resources.

### 36.7 Global escrow reset

A trade must not globally release unrelated reservations merely because its own transaction completed.

### 36.8 Strategic feedback bypass

Market success does not directly rewrite strategic goals.

### 36.9 Price-only optimization

The cheapest exchange is not necessarily the correct exchange when protected commitments and opportunity costs exist.

### 36.10 Donor coefficient worship

Historical constants are evidence of implementation, not proof of optimal Byzantine policy in the target architecture.

---

# 37. Hard invariants

### MK-01 — Strategic ownership

System 09 never creates a strategic objective solely from a resource deficit.

### MK-02 — Attribution

Every governed market commitment has one identifiable owner.

### MK-03 — Protected resources

Committed resources cannot be sold without explicit release or preemption authority.

### MK-04 — Transaction identity

Every issued market operation has a unique transaction identity.

### MK-05 — Verification

Command acceptance cannot by itself complete a market commitment.

### MK-06 — Accounting

Observed resource deltas must be reconciled against the authorized transaction.

### MK-07 — Partial results

Partial exchanges cannot be promoted to full requirement satisfaction.

### MK-08 — Retry separation

Retries create new transaction identities and preserve historical outcomes.

### MK-09 — Expiry

Market commitments must have bounded lifetime or an explicit indefinite-policy classification.

### MK-10 — Hysteresis

Threshold-driven exchange must not oscillate around a single boundary.

### MK-11 — Emergency boundedness

Emergency market authority is explicit, bounded, reversible, and attributable.

### MK-12 — Dependency ownership

System 09 does not acquire ownership of downstream construction, production, research, or labor requirements merely because it funds them.

### MK-13 — No hidden priority

Source order and `up-jump-rule` are evidence of procedural precedence, not automatically strategic authority.

### MK-14 — Resource semantics

A numeric resource channel is not assumed to be liquid, committed, protected, or available without classification.

### MK-15 — Evidence promotion

W0 control evidence cannot be silently promoted to W2/W3/W4.

### MK-16 — Deadlock visibility

A market loop that cannot change its feasibility state must eventually surface a bounded failure/deadlock condition.

### MK-17 — Reconciliation

Unused reservation and actual resource consumption must be reconciled independently.

### MK-18 — No arbitrary exchange

A market operation must identify both the source and target economic purpose before authorization.

---

# 38. Definition of done

System 09 is not complete until the forensic and implementation evidence can answer, for every market path:

1. What requirement causes the trade candidate?
2. Who owns that requirement?
3. Who authorizes the exchange?
4. Which resource is purchased?
5. Which resource is sold?
6. What quantity is authorized?
7. What minimum reserve must remain?
8. Which resources are protected by commitments?
9. Which thresholds trigger, maintain, and release the trade?
10. What prerequisites exist?
11. Which donor rule establishes each prerequisite?
12. What exact command is issued?
13. What arguments does it consume?
14. What state changes immediately?
15. What world-state change proves the transaction occurred?
16. Can the transaction be partial?
17. How is partial completion represented?
18. How is failure represented?
19. How is retry represented?
20. What releases unused reservation?
21. What happens if the originating requirement disappears?
22. What happens under higher-priority preemption?
23. Can a protected resource ever be sold?
24. If so, who can authorize that exception?
25. How is opportunity cost represented?
26. What prevents oscillation?
27. What prevents infinite retry?
28. Which duplicate definitions exist?
29. Which bypass paths exist?
30. Which conclusions are DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, or UNCERTAIN?
31. Which conclusions are runtime-qualified?
32. Which remain donor-only?
33. What is the exact first production vertical slice?
34. What observation closes that slice?
35. What evidence demonstrates that the market transaction improved the intended economic state?

If these questions cannot be answered, System 09 remains forensic rather than implementation-ready.

---

# 39. Final engineering directive

Do not implement the Shadow market as a collection of `buy` and `sell` rules.

Build it as a **governed liquidity transaction boundary**.

The intended control loop is:

```text
AEGIS / AUTHORIZED REQUIREMENT
        ↓
LIQUIDITY DEFICIT
        ↓
CANDIDATE EXCHANGE
        ↓
COMMITMENT
        ↓
RESOURCE OWNERSHIP CHECK
        ↓
PREFLIGHT
        ↓
MARKET TRANSACTION
        ↓
OBSERVED RESOURCE DELTA
        ↓
VERIFICATION
        ↓
RECONCILIATION
        ↓
REQUIREMENT UPDATE
        ↓
REASSESSMENT
```

The market subsystem's purpose is not to make the civilization clever by itself. Its purpose is to make **authorized resource conversion disciplined, attributable, bounded, observable, and reversible**.

The strategic plane decides why liquidity is required. System 06 determines whether labor allocation can improve the underlying resource state. System 09 determines whether an authorized exchange is feasible and executes that exchange. The owning downstream system verifies whether the acquired resource actually advances its requirement.

That boundary is the difference between a market script and an economic control system.

---

# 40. Next forensic target

System 10 should not begin implementation immediately. First use the completed Systems 01–09 specifications to perform a **cross-system authority and dependency synthesis**.

The next forensic pass should construct one graph covering:

```text
REQUIREMENT
→ COMMITMENT
→ RESOURCE RESERVATION
→ LABOR / INFRASTRUCTURE / RESEARCH / MARKET TRANSACTION
→ EXECUTOR
→ OBSERVATION
→ VERIFICATION
→ CAPABILITY / ECONOMIC RESULT
→ REASSESSMENT
```

The purpose is to identify duplicated authority, orphaned state, conflicting writers, bypass executors, circular dependencies, and places where two systems can independently spend the same resource.

Do not treat Systems 01–09 as nine independent subsystems. The forensic objective now becomes proving that their **interfaces compose into one coherent control architecture** without creating a second strategic brain, an ungoverned economic loop, or an execution race.
