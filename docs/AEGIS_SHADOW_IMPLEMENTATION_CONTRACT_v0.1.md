# The Byzantine Shadow — AEGIS / Shadow Implementation Contract v0.1

**Repository:** `justhop90-bot/TheByzantineShadow`  
**Purpose:** Convert the Systems 01–09 forensic architecture and shared-state authority resolution into a concrete implementation contract for the `.per` implementation.  
**Status:** DESIGN AUTHORITY / IMPLEMENTATION GATE  
**Target:** AoE2DE; exact engine ABI remains qualification-gated.  
**Evidence taxonomy:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN.

---

## 0. Executive mandate

This document is the implementation boundary between AEGIS strategic control and the Shadow economic/execution substrate.

Muse is authorized to implement the architecture described here, but **not** to invent engine semantics where the forensic record is UNCERTAIN. Where the contract specifies an AEGIS state or interface that has no direct `.per` analogue, Muse must map it to qualified engine primitives and record the mapping rather than silently changing the semantics.

The governing architecture is:

```text
WORLD / OBSERVATION
        ↓
BELIEF / CLASSIFICATION
        ↓
STRATEGIC OBJECTIVE
        ↓
CAPABILITY REQUIREMENT
        ↓
CANDIDATE SOLUTIONS
        ↓
PRIORITY / ARBITRATION
        ↓
COMMITMENT
        ↓
RESOURCE CONTROL
        ↓
SPECIALIZED SYSTEM
        ↓
TRANSACTION
        ↓
EXECUTOR
        ↓
COMMAND
        ↓
OBSERVED STATE CHANGE
        ↓
VERIFICATION
        ↓
CAPABILITY / ECONOMIC RESULT
        ↓
RECONCILIATION
        ↓
REASSESSMENT
```

**Authority flows downward. Evidence flows upward.**

The Shadow substrate must execute authorized work. It must not become a second strategic brain.

---

# 1. Non-negotiable architectural boundaries

## 1.1 Strategic authority

AEGIS owns:

- strategic objectives;
- strategic priority;
- capability requirements;
- candidate solution selection;
- strategic commitment creation/cancellation/preemption;
- interpretation of verified capability;
- strategic reassessment.

Shadow Systems 01–09 may provide feasibility, execution, economic, information, and verification evidence. They do not originate strategic objectives merely because a local condition is convenient.

## 1.2 System authority

| System | Owns | Must not own |
|---|---|---|
| S01 | Initialization/configuration | Runtime strategy |
| S02 | State registry, ownership contract, authority metadata | Domain strategy |
| S03 | Target state | Strategic objective |
| S04 | Scouting mission and observation state | Target meaning/strategy |
| S05 | Food-source and food-continuity state | Strategic priority |
| S06 | Labor allocation and productivity state | Strategic composition/objective |
| S07 | Construction/infrastructure transaction | Building doctrine |
| S08 | Research/technology transaction | Strategic technology priority |
| S09 | Market/resource-exchange transaction | Strategic trade selection |

These are AEGIS ownership boundaries, not claims that the donor already implements them cleanly.

## 1.3 Executor boundary

An executor may:

1. receive an authorized operation;
2. check local feasibility;
3. issue the engine command;
4. report observations;
5. expose failure.

An executor may not certify strategic success on its own.

---

# 2. Evidence and implementation status model

Every implementation element receives one of these statuses:

- **DONOR-PRESERVE** — directly recoverable mechanism worth retaining.
- **DONOR-ADAPT** — useful historical mechanism whose interface or coefficients require redesign.
- **AEGIS-NEW** — architectural mechanism introduced by AEGIS.
- **QUALIFY** — static source exists but semantics/reachability/runtime behavior remain unresolved.
- **QUARANTINE** — legacy/duplicate/conflicting mechanism must not enter the active architecture.
- **REPLACE** — donor mechanism is too coupled/unsafe for direct use.

A `.per` symbol must never be promoted solely because it is present in the donor.

---

# 3. Canonical state interfaces

The implementation must conceptually represent the following state classes even where several are packed into engine-supported channels.

## 3.1 Requirement

```text
REQUIREMENT_ID
ORIGINATING_OBJECTIVE
REQUIRED_CAPABILITY
CURRENT_VERIFIED_STATE
VERIFIED_COMMITTED_STATE
TRUE_DEFICIT
PRIORITY
URGENCY
CREATION_EPOCH
EXPIRY
INVALIDATION
OWNER
GENERATION
EVIDENCE_LEVEL
```

Requirement means **what must become true**, not what command should be issued.

## 3.2 Commitment

```text
COMMITMENT_ID
REQUIREMENT_ID
OPERATION_CLASS
RESOURCE_REQUIREMENT
MINIMUM_VIABLE_FUNDING
RESERVED_AMOUNT
PRIORITY
OWNER
GENERATION
STATE
CREATION_EPOCH
EXPIRY
CANCELLATION_PREDICATE
PREEMPTION_PREDICATE
COMPLETION_PREDICATE
```

Commitment means an attributable decision to pursue a requirement through a bounded solution.

## 3.3 Transaction

```text
TRANSACTION_ID
COMMITMENT_ID
OPERATION_CLASS
STATE
AUTHORIZED_AMOUNT
ISSUED_AMOUNT
OBSERVED_RESULT
CREATION_EPOCH
EXPIRY
GENERATION
```

Transaction state:

```text
REQUESTED → RESERVING → RESERVED → PREFLIGHT → AUTHORIZED
→ ISSUED → OBSERVING → CONFIRMED
```

Exceptional outcomes:

```text
REJECTED / FAILED / PARTIAL / UNVERIFIED / RELEASED / EXPIRED
```

## 3.4 Verification

```text
VERIFICATION_ID
TRANSACTION_ID
EXPECTED_POSTCONDITION
OBSERVED_POSTCONDITION
EVIDENCE_LEVEL
RESULT
OBSERVED_EPOCH
GENERATION
```

Verification result:

```text
NOT_STARTED / PENDING / PASS / PARTIAL / FAIL / UNKNOWN
```

## 3.5 Progression

The progression state must preserve:

```text
CURRENT_WORK_ITEM
PROGRESS_CURSOR
PAUSE / SUSPENSION
REQUIREMENT
COMMITMENT
TRANSACTION
VERIFICATION
```

`gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause` are historical candidates for these semantics. Their physical donor channels must not be assumed reusable until namespace qualification.

`gl-escrow-state` is the historical candidate for transaction-mode selection between escrow-aware and non-escrow-aware execution.

---

# 4. Required mutation interfaces

The implementation must treat the following as logical interfaces even if `.per` implements them through rules, goals, strategic numbers, timers, or command predicates.

## 4.1 Requirement interface

```text
DECLARE_REQUIREMENT
READ_REQUIREMENT
INVALIDATE_REQUIREMENT
SATISFY_REQUIREMENT
REASSESS_REQUIREMENT
```

Only the requirement owner may mutate requirement state.

## 4.2 Commitment interface

```text
CREATE_COMMITMENT
FUND_COMMITMENT
SUSPEND_COMMITMENT
RESUME_COMMITMENT
CANCEL_COMMITMENT
EXPIRE_COMMITMENT
INVALIDATE_COMMITMENT
PREEMPT_COMMITMENT
VERIFY_COMMITMENT
RETIRE_COMMITMENT
```

## 4.3 Reservation interface

```text
REQUEST_RESERVATION
RESERVE
VERIFY_RESERVATION
TRANSFER_TO_TRANSACTION
CONSUME
RETURN_REMAINDER
RELEASE
RECONCILE
```

`set-escrow-percentage` and `up-modify-escrow` are donor mechanisms with different apparent roles. They must not be collapsed into one opaque “escrow” operation without rule-level evidence.

## 4.4 Transaction interface

```text
REQUEST_TRANSACTION
PREFLIGHT_TRANSACTION
AUTHORIZE_TRANSACTION
ISSUE_TRANSACTION
OBSERVE_TRANSACTION
VERIFY_TRANSACTION
RETRY_TRANSACTION
FAIL_TRANSACTION
EXPIRE_TRANSACTION
RELEASE_TRANSACTION
```

## 4.5 Verification interface

```text
DECLARE_EXPECTED_POSTCONDITION
OBSERVE
COMPARE
CLASSIFY_RESULT
PROMOTE_EVIDENCE
RECONCILE
```

---

# 5. System-specific implementation contracts

## S01 — Initialization / Configuration

### Inputs

Engine/environment state and compile-time configuration.

### Outputs

Validated initial constants, enumerations, state-channel availability, and environment contract.

### Allowed mutations

Initialization only, except explicitly documented configuration state.

### Forbidden

S01 must not continuously override domain-owned runtime state merely because a default exists.

### Gate

Every configuration constant must be classified as environment contract, engine/ABI vocabulary, policy coefficient, or compile-time feature selection. Static definition does not establish runtime activity.

---

## S02 — State Namespace / Authority

S02 is the registry/governance layer.

### Owns

- semantic classification;
- physical channel registry;
- owner metadata;
- generation metadata;
- validity/lifetime metadata;
- conflict classification;
- writer/reader registry.

### Does not own

Food policy, labor policy, construction strategy, research strategy, market strategy, military strategy, or production strategy.

### Required operation

For every shared state:

```text
LOOKUP → OWNER CHECK → GENERATION CHECK → VALIDITY CHECK → AUTHORIZE / REJECT
```

S02 may reject an invalid mutation without becoming the writer of the domain state.

---

## S03 — Target Acquisition

### Input

Verified/fresh observations from S04 and strategic target requirements from AEGIS.

### Owns

Target identity, target kind, target position, target validity, target freshness/generation.

### Does not own

Why the target matters strategically.

### Required output

A target record that downstream systems can consume without confusing target player, object, type, position, and objective.

### Verification

Observation provenance + target-state consistency.

Target loss must be classified independently from mission failure and strategic commitment failure.

---

## S04 — Scouting / Information Acquisition

### Input

Information requirements.

### Owns

Scout mission, mode, route/geometry, observation record, freshness, information-satisfaction state.

### Canonical pipeline

```text
INFORMATION REQUIREMENT
→ SCOUT AUTHORIZATION
→ MODE
→ ROUTE / GEOMETRY
→ MOVEMENT
→ OBSERVATION
→ OBSERVATION RECORD
→ INFORMATION SATISFACTION
```

### Critical distinction

`AREA_VISITED` is not necessarily `AREA_INFORMATIVE`, and neither necessarily means `INFORMATION_REQUIREMENT_SATISFIED`.

### Forbidden

Scouting cannot silently convert movement success into strategic knowledge.

---

## S05 — Food Logistics

### Input

Food demand/continuity requirements and available worker/resource state.

### Owns

Food source state, food continuity state, source transition policy, food-flow observations, food-specific requirements.

### Does not own

General worker allocation. It requests labor from S06.

### Canonical output

```text
FOOD REQUIREMENT
→ SOURCE REQUIREMENT
→ WORKER / INFRASTRUCTURE REQUIREMENT
→ OBSERVED FOOD FLOW
→ CONTINUITY VERIFICATION
```

Food stock, food flow, and food continuity must remain distinct.

---

## S06 — Villager Economy / Labor Allocation

### Input

Authorized economic requirements from AEGIS/Shadow systems.

### Owns

Worker allocation, worker transition state, productive allocation, resource-flow observation, economic feasibility state.

### Does not own

Strategic composition, strategic priorities, market strategy, construction strategy, research strategy.

### Canonical output

```text
RESOURCE REQUIREMENT
→ LABOR REQUIREMENT
→ WORKER ASSIGNMENT
→ OBSERVED PRODUCTIVITY
→ RESOURCE FLOW
→ ECONOMIC REASSESSMENT
```

`DESIRED ≠ ASSIGNED ≠ PRODUCTIVE ≠ OBSERVED FLOW`.

---

## S07 — Construction / Infrastructure

### Input

Authorized infrastructure requirement and builder/resource availability.

### Owns

Construction transaction, building requirement state, site/build execution state, pending/building/completion/operational verification.

### Interfaces

```text
S06 → BUILDER AVAILABILITY
S09 → LIQUIDITY IF AUTHORIZED
S07 → BUILD EXECUTION
```

### Required separation

```text
COMMAND ISSUED
≠ PENDING OBJECT
≠ PLACED
≠ COMPLETED
≠ OPERATIONAL
```

### Escrow-aware execution

Historical `can-build-with-escrow` / `up-build` patterns may be preserved where qualified. They are execution interfaces, not strategic authorities.

---

## S08 — Research / Technology

### Input

Authorized capability/technology requirement.

### Owns

Technology candidate state, prerequisite evaluation, research transaction, research completion, technology-to-capability verification.

### Required separation

```text
TECHNOLOGY ID
≠ RESEARCH TRANSACTION
≠ VERIFIED CAPABILITY EFFECT
```

### Prerequisite rule

A missing prerequisite is a feasibility condition, not automatic strategic rejection.

### Escrow-aware execution

Historical `can-research-with-escrow` / `up-research` mechanisms may be preserved where qualified.

---

## S09 — Market / Resource Exchange

### Input

Authorized liquidity requirement.

### Owns

Market candidate, market transaction, exchange feasibility, transaction state, observed resource consequence, reconciliation.

### Does not own

The strategic reason for trading.

### Required separation

```text
RESOURCE REQUIREMENT
→ LIQUIDITY DEFICIT
→ EXCHANGE CANDIDATE
→ AUTHORIZATION
→ MARKET TRANSACTION
→ OBSERVED RESOURCE DELTA
→ VERIFICATION
```

The recovered donor constants `LOW-ESCROW`, `MID-ESCROW`, `MID-HIGH-ESCROW`, `HIGH-ESCROW` and market thresholds are donor evidence, not automatically AEGIS coefficients. Their use sites must remain qualification-gated.

---

# 6. Cross-system interface contracts

## 6.1 S04 ↔ S03

```text
S04 PRODUCES OBSERVATION
S03 CONSUMES OBSERVATION
S03 OWNS TARGET STATE
```

S03 may request refreshed information. S04 determines how information is acquired.

## 6.2 S05 ↔ S06

```text
S05 PRODUCES FOOD LABOR REQUIREMENT
S06 OWNS LABOR ASSIGNMENT
S05 VERIFIES FOOD CONTINUITY
S06 VERIFIES PRODUCTIVITY
```

Neither system may overwrite the other's semantic state.

## 6.3 S06 ↔ S07

```text
S07 DECLARES BUILDER REQUIREMENT
S06 ASSIGNS WORKER
S07 OWNS CONSTRUCTION TRANSACTION
```

Construction cannot silently rewrite general labor policy.

## 6.4 S07 ↔ S08

```text
S08 REQUIRES INFRASTRUCTURE PREREQUISITE
S07 OWNS INFRASTRUCTURE
S08 CONSUMES VERIFIED PREREQUISITE STATE
```

## 6.5 S08 ↔ S09

```text
S08 DECLARES AUTHORIZED LIQUIDITY REQUIREMENT
S09 EXECUTES MARKET TRANSACTION
S08 VERIFIES RESEARCH RESULT
```

S09 does not decide that research deserves funding.

## 6.6 S07 ↔ S09

Same pattern for construction funding. S09 verifies the exchange; S07 verifies the building.

## 6.7 AEGIS / Production Authority ↔ Shadow

```text
AEGIS
→ CAPABILITY REQUIREMENT
→ PRODUCTION COMMITMENT
→ RESOURCE REQUIREMENT
→ SHADOW ECONOMIC SUBSTRATE
→ AIByzBuild / TRAIN EXECUTOR
→ OBSERVED QUEUE / UNIT STATE
→ PRODUCTION VERIFICATION
→ AEGIS REASSESSMENT
```

Production requested but not verified is not capability.

---

# 7. Resource and escrow contract

Three economic layers must remain distinct:

### Policy escrow

Background protection policy. Historical levels exist in donor evidence; exact semantics must be qualified.

### Commitment escrow

Attributable reservation protecting a specific commitment.

### Transaction escrow

Short-lived amount transferred into a specific transaction/executor path.

Conceptual lifecycle:

```text
POLICY PROTECTION

COMMITMENT:
CANDIDATE → RESERVED → FUNDED → CONSUMED / RELEASED

TRANSACTION:
REQUESTED → RESERVED → AUTHORIZED → ISSUED
→ OBSERVED → CONSUMED / RETURNED
```

A transaction must not silently convert its reservation into a permanent commitment. A commitment must not silently consume another commitment's resources.

---

# 8. Production integration contract

The production authority boundary is deliberately outside Shadow's nine economic systems.

Required chain:

```text
OBSERVED THREAT / OPPORTUNITY
        ↓
CAPABILITY REQUIREMENT
        ↓
COMPOSITION TARGET
        ↓
TRUE DEFICIT
        ↓
RESOURCE REQUIREMENT
        ↓
COMMITMENT
        ↓
FUNDING
        ↓
PRODUCTION AUTHORITY
        ↓
AIByzBuild / TRAIN EXECUTOR
        ↓
OBSERVED QUEUE / UNIT MUTATION
        ↓
VERIFICATION
        ↓
CAPABILITY UPDATE
```

Use:

```text
TRUE DEFICIT
= DEMAND
− CURRENT_VERIFIED_CAPABILITY
− VERIFIED_COMMITTED_CAPABILITY
```

Do not count merely requested or command-issued units as verified committed capability unless the commitment semantics explicitly establish that level of evidence.

---

# 9. Failure contract

Every specialized system must expose at least:

```text
NO_REQUIREMENT
NO_RESOURCES
NO_BUILDER / NO_WORKER
NO_VALID_SITE
PREREQUISITE_MISSING
PREFLIGHT_REJECTED
COMMAND_REJECTED
NO_POSTCONDITION
PARTIAL
INTERRUPTED
VERIFICATION_TIMEOUT
EXPIRED
INVALIDATED
PREEMPTED
FAILED
BLOCKED
DEADLOCKED
UNKNOWN
```

Failure is state. It must not disappear into a jump back to the same rule.

Repeated failure must increment or otherwise expose a diagnosable failure condition so the controller can replan, relax, cancel, or escalate.

---

# 10. Preemption contract

Preemption is only legal through an authority transition:

```text
ACTIVE
→ SUSPEND
→ FREEZE NEW FUNDING
→ RECONCILE RESERVATIONS
→ EXECUTE HIGHER PRIORITY WORK
→ VERIFY
→ RESUME / RETIRE / REPLAN
```

The higher-priority path must identify the reason for preemption.

Emergency preemption may violate normal hysteresis only when the emergency predicate is explicit and bounded.

A preemptor does not inherit ownership of the preempted commitment merely because it suspended it.

---

# 11. Hysteresis and anti-thrashing

Any continuously evaluated shared state that can trigger allocation, trade, research, construction, or production changes must avoid single-threshold oscillation.

At minimum, where the semantics require it, implement:

```text
ACTIVATION THRESHOLD
MAINTAIN THRESHOLD
RELEASE THRESHOLD
PREEMPTION THRESHOLD
MINIMUM DWELL
MINIMUM VIABLE COMMITMENT
MAXIMUM RESERVATION AGE
```

These are AEGIS design requirements unless donor evidence establishes equivalent semantics.

---

# 12. `.per` implementation constraints

Muse must implement within the actual AoE2DE AI language ABI.

## 12.1 No imaginary primitives

Do not invent structs, object references, arbitrary dictionaries, callbacks, or event queues that `.per` cannot represent.

When a logical record must be encoded into primitive channels, document the packing scheme and its collision/lifetime constraints.

## 12.2 Numeric namespace

Every goal and strategic number used by AEGIS/Shadow must be registered before use.

The donor's numeric identity is not preserved merely for convenience.

## 12.3 Constants

Separate:

- immutable identifiers;
- policy thresholds;
- state sentinels;
- enum values;
- channel IDs;
- timer durations.

A numeric constant must have one documented semantic role per architecture generation.

## 12.4 Rule order

Source order may implement precedence, but the semantic precedence must be documented first.

## 12.5 `up-jump-rule`

Every jump that suppresses another branch must document:

```text
SOURCE RULE
TARGET RULE
REASON
AUTHORITY LEVEL
STATE AFFECTED
STATE PRESERVED
STATE RESET
PREEMPTION / SUPPRESSION CLASS
```

## 12.6 Timers

Every timer must document:

```text
START EVENT
CLOCK BASIS
DURATION
PURPOSE
READERS
EXPIRY EVENT
RESET EVENT
OWNER
```

A timer without a defined lifecycle is not sufficient evidence of temporal control.

---

# 13. Migration policy for donor code

The donor is not transplanted wholesale.

### PRESERVE

Where directly supported and architecturally bounded:

- escrow-aware feasibility predicates;
- escrow-aware execution interfaces;
- resource-saving mechanisms;
- progression/transaction sequencing;
- food-source knowledge;
- labor heuristics;
- construction mechanisms;
- research transaction mechanisms;
- market transaction mechanisms;
- useful scouting geometry and recovery;
- useful target acquisition machinery.

### FORMALIZE

- implicit commitment state;
- progression state;
- owner/generation semantics;
- verification boundaries;
- reservation attribution;
- preemption;
- failure states;
- transaction identity.

### ADAPT

- donor thresholds;
- escrow coefficients;
- age-specific policies;
- market exchange policy;
- map-dependent geometry;
- worker ratios and timing coefficients.

### REPLACE

- hidden strategic priority controller;
- ambiguous shared semantic state;
- duplicate strategic writers;
- unbounded bypass paths;
- donor-specific numeric namespace as an architectural dependency.

### QUARANTINE

- duplicate definitions with conflicting meanings;
- unreachable legacy experiments;
- mechanisms whose authority cannot be established;
- any path that silently creates strategic objectives below AEGIS.

`sn-resource-control` remains excluded from the Shadow donor architecture unless separately proven from source. The existing forensic correction must remain intact.

---

# 14. Qualification sequence

Implementation proceeds through these gates, in order.

## Gate I — Namespace freeze

Deliver:

- complete active symbol registry;
- physical channel map;
- owner map;
- writer/reader graph;
- duplicate/conditional definition ledger;
- generation/lifetime classification.

No broad implementation before this gate.

## Gate II — Authority freeze

Demonstrate:

- one owner per semantic state;
- no unauthorized writers;
- no strategic leakage;
- explicit precedence;
- explicit preemption;
- explicit reset/expiry.

## Gate III — ABI freeze

For each primitive used by the implementation, classify:

```text
STATIC EXISTENCE
LOAD SURVIVAL
RULE REACHABILITY
COMMAND ACCEPTANCE
WORLD-STATE MUTATION
VERIFIED POSTCONDITION
```

Unknown engine semantics remain UNKNOWN.

## Gate IV — Economic transaction slice

Qualify one narrow path end-to-end:

```text
REQUIREMENT
→ COMMITMENT
→ RESERVATION
→ PREFLIGHT
→ TRANSACTION
→ COMMAND
→ OBSERVATION
→ VERIFICATION
→ RECONCILIATION
```

Preferred first slice: civilian/farm construction or another minimal economic transaction already supported by the executor substrate.

## Gate V — Cross-system slice

Qualify one integrated path such as:

```text
FOOD CONTINUITY DEFICIT
→ FARM REQUIREMENT
→ WOOD COMMITMENT
→ BUILDER REQUIREMENT
→ S06 ASSIGNMENT
→ S07 BUILD TRANSACTION
→ FARM OBSERVATION
→ VERIFICATION
→ ESCROW RECONCILIATION
→ FOOD REASSESSMENT
```

## Gate VI — Strategic handoff

Only after the economic slice is verified may AEGIS strategic requirements begin driving it.

## Gate VII — Production slice

Then qualify:

```text
CAPABILITY DEFICIT
→ PRODUCTION REQUIREMENT
→ RESOURCE COMMITMENT
→ AIByzBuild
→ TRAIN
→ QUEUE / UNIT OBSERVATION
→ VERIFICATION
→ CAPABILITY UPDATE
```

## Gate VIII — Adversarial qualification

Attempt to force:

- duplicate writers;
- stale generation writes;
- reservation double-spend;
- unauthorized release;
- progression race;
- duplicate executor issue;
- false verification;
- infinite retry;
- starvation;
- deadlock;
- emergency abuse.

Any critical failure blocks promotion.

---

# 15. Required implementation artifacts

Before declaring the contract implemented, Muse must produce:

1. **STATE_REGISTRY** — every shared symbol and semantic type.
2. **AUTHORITY_REGISTRY** — owner, writers, readers, mutation path.
3. **GENERATION_MAP** — generation-bearing states and invalidation events.
4. **PRECEDENCE_GRAPH** — semantic precedence and source-order implementation.
5. **JUMP_GRAPH** — every suppression/preemption path.
6. **RESOURCE_LEDGER** — policy, commitment, transaction, consumption, release.
7. **TRANSACTION_REGISTRY** — transaction classes and lifecycle states.
8. **VERIFICATION_MATRIX** — action → expected postcondition → evidence source.
9. **BYPASS_LEDGER** — every path that bypasses normal commitment/transaction machinery.
10. **FAILURE_LEDGER** — failure classification and recovery path.
11. **QUALIFICATION_LOG** — static and runtime evidence for each promoted primitive.
12. **VERTICAL_SLICE_REPORT** — complete trace of one end-to-end operation.

No artifact may substitute `UNRECOVERED` with `NONE` without complete source inspection.

---

# 16. Definition of done

The implementation is ready for broader strategic integration only when:

- every shared state has one owner;
- every writer is known;
- every mutation is authorized;
- stale generations cannot mutate current state;
- resource reservations are attributable;
- transaction state is distinct from commitment state;
- command issuance is distinct from observation;
- observation is distinct from verification;
- verification is distinct from capability;
- capability is distinct from strategic success;
- progression advances only after its required postcondition;
- preemption preserves or explicitly retires displaced commitments;
- failures remain visible;
- bypasses are classified;
- legacy paths are quarantined or explicitly delegated;
- at least one cross-system vertical slice is runtime-qualified;
- the implementation remains pure `.per`;
- no unqualified engine assumption is represented as fact.

---

# 17. Final directive to Muse

Do not begin by writing hundreds of `.per` rules.

Begin by making the architecture **mechanically difficult to violate**.

The correct implementation strategy is:

```text
REGISTER
→ OWN
→ GENERATE
→ ARBITRATE
→ RESERVE
→ EXECUTE
→ OBSERVE
→ VERIFY
→ RECONCILE
→ REASSESS
→ EXPAND
```

Extract the donor where it contains valuable knowledge. Improve it where its control semantics are implicit or unsafe. Replace it where strategic authority is hidden. Quarantine it where ownership cannot be established. Qualify every engine-dependent claim.

The objective is not a sophisticated collection of `.per` rules.

The objective is a **coherent, inspectable, recoverable control system whose strategic decisions are explicit and whose economic/execution substrate can be trusted to carry them out.**
