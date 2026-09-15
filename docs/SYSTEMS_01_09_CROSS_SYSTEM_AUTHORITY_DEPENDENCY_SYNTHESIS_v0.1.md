# Systems 01–09 Cross-System Authority & Dependency Synthesis v0.1

**Repository:** `justhop90-bot/TheByzantineShadow`  
**Scope:** Systems 01–09  
**Status:** ARCHITECTURAL SYNTHESIS / FORENSIC CONTROL GATE  
**Implementation status:** NOT YET QUALIFIED FOR RUNTIME  
**Primary purpose:** establish the cross-system authority, dependency, resource, and evidence boundaries that must govern any subsequent `.per` implementation.

---

## 1. Executive Determination

Systems 01–09 should not be implemented as nine independent rule collections. Their useful architecture is a single governed control pipeline with specialized subsystems at the execution and verification boundaries.

The canonical cross-system flow is:

```text
WORLD / OBSERVATION
        ↓
BELIEF / CLASSIFICATION
        ↓
STRATEGIC OR ECONOMIC REQUIREMENT
        ↓
COMMITMENT
        ↓
RESOURCE RESERVATION / FEASIBILITY
        ↓
SPECIALIZED TRANSACTION
        ↓
EXECUTOR
        ↓
OBSERVED WORLD-STATE CHANGE
        ↓
VERIFICATION
        ↓
CAPABILITY / ECONOMIC RESULT
        ↓
RECONCILIATION
        ↓
REASSESSMENT
```

The principal architectural conclusion is that **authority must flow downward while evidence flows upward**.

A subsystem may execute or verify the class of operation it owns, but it must not silently acquire strategic authority merely because it possesses a command path, a goal channel, a threshold, or a successful-looking executor predicate.

The most important cross-system invariant is therefore:

> **Requirement ownership, commitment ownership, transaction authority, execution authority, and verification authority are distinct concepts and must not be collapsed into one goal, rule, or command path.**

---

## 2. Evidence Discipline

This document synthesizes Systems 01–09. It is therefore intentionally divided between donor-supported findings and AEGIS architectural conclusions.

### Evidence classes

- **DIRECT** — explicitly present in the donor/source material.
- **COMPOSED** — derived by tracing multiple directly observed facts.
- **INFERRED** — plausible interpretation not yet directly established.
- **AEGIS-GENERALIZATION** — deliberate redesign or abstraction introduced by AEGIS.
- **UNCERTAIN** — semantics requiring additional source extraction or runtime qualification.

### Evidence ladder

```text
SOURCE PRESENCE
      ↓
STATIC REACHABILITY
      ↓
LOAD / DEFINITION SURVIVAL
      ↓
RULE REACHABILITY
      ↓
RUNTIME OBSERVATION
      ↓
WORLD-STATE MUTATION
      ↓
VERIFIED CAPABILITY / ECONOMIC RESULT
      ↓
STRATEGIC EFFECT
```

No layer may be promoted merely because a lower layer exists.

In particular:

```text
COMMAND ACCEPTED ≠ EXECUTION COMPLETE
EXECUTION COMPLETE ≠ CAPABILITY VERIFIED
CAPABILITY VERIFIED ≠ STRATEGIC SUCCESS
```

---

# 3. System Boundary Registry

| System | Primary responsibility | Does not own | Primary output |
|---|---|---|---|
| 01 | Initialization/configuration | Strategic decisions after initialization | Valid initial control environment |
| 02 | State namespace and authority | Domain strategy | Typed state / ownership / validity model |
| 03 | Target acquisition | Strategic objective selection | Valid target state |
| 04 | Scouting / information acquisition | Target strategic meaning | Observations / information satisfaction |
| 05 | Food logistics | Civilization-wide strategic objective | Food continuity / logistics state |
| 06 | Villager economy / labor allocation | Strategic objective selection | Labor allocation / observed productivity |
| 07 | Construction / infrastructure | Strategic building objective | Verified infrastructure |
| 08 | Research / technology | Strategic technology priority | Verified technology/capability |
| 09 | Market / resource exchange | Strategic trade selection | Verified resource exchange consequence |

**Architectural status:** AEGIS boundary model; individual donor mechanisms require rule-level and runtime qualification.

---

# 4. Requirement Graph

## 4.1 Canonical graph

```text
WORLD / BELIEF / STRATEGIC STATE
              ↓
       STRATEGIC OBJECTIVE
              ↓
       CAPABILITY REQUIREMENT
              ↓
     DOMAIN REQUIREMENT
       ↙    ↓     ↘
   FOOD  INFRA    TECH
     ↘    ↓       ↙
       RESOURCE / LIQUIDITY
              ↓
          COMMITMENT
              ↓
        TRANSACTION
              ↓
          EXECUTOR
              ↓
       OBSERVED RESULT
              ↓
        VERIFICATION
              ↓
      REQUIREMENT UPDATE
              ↓
         REASSESSMENT
```

## 4.2 Requirement ownership

The originating strategic authority creates the strategic objective. Domain systems translate that objective into domain requirements. They must not reverse the relationship and manufacture a strategic objective from a local shortage unless explicitly authorized as an emergency condition.

Examples:

```text
AEGIS objective
  → food continuity requirement
  → System 05 logistics requirement
  → System 06 labor requirement
  → System 07 farm requirement
```

```text
AEGIS capability objective
  → technology requirement
  → System 08 research transaction
```

```text
AEGIS capability objective
  → composition requirement
  → production authority
  → resource requirement
  → System 09 liquidity transaction if necessary
```

The requirement graph must prevent:

- food shortage → automatic strategic doctrine;
- resource shortage → automatic market sale;
- missing building → automatic strategic priority;
- idle villager → arbitrary economic objective;
- observed enemy target → automatic attack objective;
- eligible technology → automatic research commitment.

These are authority leaks unless explicitly represented as policy.

---

# 5. Authority Graph

## 5.1 Canonical authority path

```text
AEGIS / AUTHORIZED STRATEGIC PLANE
                ↓
          OBJECTIVE OWNER
                ↓
       REQUIREMENT AUTHORITY
                ↓
       COMMITMENT AUTHORITY
                ↓
       DOMAIN TRANSACTION AUTHORITY
                ↓
          EXECUTOR INTERFACE
                ↓
         ENGINE COMMAND
```

The reverse path carries evidence rather than authority:

```text
ENGINE STATE
    ↑
OBSERVATION
    ↑
VERIFICATION
    ↑
DOMAIN RESULT
    ↑
REQUIREMENT SATISFACTION
    ↑
REASSESSMENT
```

## 5.2 Authority dimensions

Every authoritative control object should be understood as:

```text
VALID
+ OWNER
+ GENERATION
+ STAGE
+ PAYLOAD
+ EVIDENCE_LEVEL
+ EPOCH
```

A numeric goal value alone is not an adequate authority record.

## 5.3 System authority matrix

| Authority | System 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Initialization | PRIMARY | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER |
| State ownership registry | — | PRIMARY | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER |
| Target state | — | GOVERNANCE | PRIMARY | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER |
| Information acquisition | — | GOVERNANCE | CONSUMER | PRIMARY | CONSUMER | CONSUMER | CONSUMER | CONSUMER | CONSUMER |
| Food logistics | — | GOVERNANCE | — | INFORMATION INPUT | PRIMARY | CONSUMER | CONSUMER | CONSUMER | CONSUMER |
| Labor allocation | — | GOVERNANCE | — | INFORMATION INPUT | CONSUMER | PRIMARY | BUILDER INPUT | RESEARCH INPUT | MARKET INPUT |
| Construction | — | GOVERNANCE | — | INFORMATION INPUT | CONSUMER | BUILDER INPUT | PRIMARY | PREREQUISITE PROVIDER | CONSUMER |
| Research | — | GOVERNANCE | — | INFORMATION INPUT | CONSUMER | LABOR INPUT | PREREQUISITE CONSUMER | PRIMARY | RESOURCE INPUT |
| Market exchange | — | GOVERNANCE | — | INFORMATION INPUT | RESOURCE INPUT | RESOURCE INPUT | RESOURCE INPUT | RESOURCE INPUT | PRIMARY |
| Strategic objective selection | — | — | NO | NO | NO | NO | NO | NO | NO |

The final row is intentional: **Systems 03–09 are domain mechanisms, not independent strategic brains.**

---

# 6. Resource Graph

## 6.1 Resource lifecycle

```text
GROSS RESOURCE
      ↓
POLICY-PROTECTED RESOURCE
      ↓
COMMITTED RESOURCE
      ↓
TRANSACTION-RESERVED RESOURCE
      ↓
EXECUTOR CONSUMPTION
      ↓
OBSERVED RESOURCE DELTA
      ↓
RECONCILIATION
      ↓
REMAINING / RELEASED / RECOMMITTED RESOURCE
```

Conceptual AEGIS accounting model:

```text
transaction_available =
    gross_resource
  − policy_protection
  − active_commitment_reservations
  − other_governed_holds
```

This is an **AEGIS accounting abstraction**, not an assertion that the AoE2 engine exposes this exact ledger.

## 6.2 Escrow separation

Three distinct mechanisms must remain separate:

### Policy escrow

Background economic protection such as donor escrow levels.

### Commitment escrow

Attributable reservation associated with a specific commitment.

### Transaction escrow

Short-lived reservation associated with one executable transaction.

The critical invariant is:

> A transaction may consume only resources authorized for that transaction. It may not silently consume another commitment's protected resources.

## 6.3 Cross-system resource dependencies

```text
System 05 Food
      ↓
food continuity requirement
      ↓
System 06 Labor
      ↓
worker productivity
      ↓
resource flow
```

```text
System 07 Construction
      ↑
wood / stone reservation
      ↑
System 06 labor allocation
      ↑
System 09 liquidity if exchange is authorized
```

```text
System 08 Research
      ↑
resource reservation
      ↑
System 09 liquidity if exchange is authorized
```

```text
Production authority
      ↓
resource requirement
      ↓
System 09 liquidity support
      ↓
verified resource acquisition
      ↓
production feasibility reassessment
```

No system may treat gross stock as automatically liquid stock.

---

# 7. Dependency Graph

## 7.1 Primary dependency graph

```text
                         ┌───────────────┐
                         │  AEGIS /      │
                         │  STRATEGIC    │
                         │  AUTHORITY    │
                         └───────┬───────┘
                                 │
                    objective / requirement
                                 │
             ┌───────────────────┼───────────────────┐
             ↓                   ↓                   ↓
        INFORMATION          ECONOMIC            CAPABILITY
             │                   │                   │
             ↓                   ↓                   ↓
        System 04            System 05          Systems 07/08
             │                   │                   │
             ↓                   ↓                   ↓
        System 03            System 06         prerequisites
             │                   │                   │
             └──────────────┬────┴───────┬───────────┘
                            ↓            ↓
                       System 09     Production Authority
                            │            │
                            └──────┬─────┘
                                   ↓
                              EXECUTION
                                   ↓
                              OBSERVATION
                                   ↓
                              VERIFICATION
                                   ↓
                              REASSESSMENT
```

## 7.2 Dependency classes

### Hard dependency

The downstream action cannot legally or mechanically proceed without the upstream condition.

Example: research requiring a prerequisite building.

### Feasibility dependency

The downstream action may be logically desired but is not executable until the dependency is satisfied.

Example: construction requiring resources and a valid site.

### Information dependency

The downstream system needs current observation but does not own the observation mechanism.

Example: target acquisition consuming scouting observations.

### Economic dependency

A downstream operation requires resources or labor whose allocation belongs to another system.

### Verification dependency

A system may not advance its state until an observation supplied by an appropriate verifier establishes the postcondition.

### Strategic dependency

A domain operation exists because a higher-level objective authorized it.

This dependency must not be inverted.

---

# 8. Cross-System Transaction Contract

All nine systems should converge on a common transaction vocabulary even where their physical executor differs.

```text
REQUESTED
   ↓
RESERVING
   ↓
RESERVED
   ↓
PREFLIGHT
   ↓
AUTHORIZED
   ↓
ISSUED
   ↓
OBSERVING
   ↓
CONFIRMED
```

Failure / exceptional states:

```text
REJECTED
FAILED
PARTIAL
UNVERIFIED
EXPIRED
RELEASED
CANCELLED
PREEMPTED
BLOCKED
DEADLOCKED
```

The domain systems differ in what constitutes the postcondition:

| Domain | Command evidence | Sufficient verification candidate |
|---|---|---|
| Scouting | movement / scout command | informative observation acquired and recorded |
| Targeting | target assignment | valid target state observed and fresh |
| Food | assignment / movement / farm action | observed productive food flow / continuity state |
| Labor | worker assignment | observed productive allocation / resource flow |
| Construction | `up-build` / build action | pending object → placed → completed/operational as required |
| Research | `up-research` | research state / technology completion / capability effect |
| Market | buy/sell command | observed source/target resource deltas and transaction reconciliation |
| Production | train command | queue/unit mutation and required postcondition |

Exact engine semantics remain qualification-dependent.

---

# 9. Evidence Graph

## 9.1 Canonical evidence graph

```text
CONTROL INTENT
     ↓
COMMAND REQUEST
     ↓
COMMAND ACCEPTED [W0]
     ↓
PENDING / IN-PROGRESS [W1]
     ↓
ENGINE WORLD-STATE MUTATION [W2]
     ↓
VERIFIED CAPABILITY / ECONOMIC RESULT [W3]
     ↓
STRATEGIC EFFECT [W4]
```

The W-level labels are AEGIS evidence discipline. They must not be confused with native engine state names.

## 9.2 Promotion rules

### W0 → W1
Requires evidence that an action entered a pending or accepted state rather than merely that a rule fired.

### W1 → W2
Requires observable engine state mutation.

### W2 → W3
Requires a sufficient domain-specific postcondition.

### W3 → W4
Requires evidence that the verified capability or economic result actually affected the strategic objective.

A command trace cannot promote itself.

---

# 10. Cross-System State Flow

The minimum shared-state lifecycle is:

```text
OBSERVATION
   ↓
CLASSIFICATION
   ↓
BELIEF / STATE WRITE
   ↓
AUTHORITY EFFECT
   ↓
REQUIREMENT
   ↓
COMMITMENT
   ↓
RESOURCE RESERVATION
   ↓
TRANSACTION
   ↓
COMMAND
   ↓
OBSERVATION
   ↓
VERIFICATION
   ↓
RESULT
   ↓
RECONCILIATION
   ↓
REASSESSMENT
```

This prevents the common failure mode in which a command directly mutates a strategic goal or progression cursor.

The prohibited shortcut is:

```text
COMMAND → PROGRESS++
```

The required path is:

```text
COMMAND
  → OBSERVATION
  → VERIFICATION
  → WORK ITEM CONFIRMED
  → PROGRESS++
```

---

# 11. System-by-System Cross-Boundary Contracts

## 11.1 System 01 → Systems 02–09

System 01 establishes initial configuration and valid startup conditions. It must not become a permanent strategic controller merely because initialization variables remain globally visible.

**Required improvement:** distinguish initialization state from durable authority state and explicitly define lifetime.

## 11.2 System 02 → Systems 03–09

System 02 supplies the namespace and authority framework.

Critical carriers include:

- `gl-escrow-state`
- `gl-current-build-item`
- `gl-build-progress`
- `gl-progression-pause`
- target identity/state
- coordinates
- timers/epochs
- reservation/commitment identity

**Required improvement:** every shared carrier receives an owner, writer set, reader set, lifetime, validity rule, generation, precedence, and evidence level.

## 11.3 System 03 ↔ System 04

System 04 acquires information. System 03 converts suitable observations into target state.

```text
SCOUT → OBSERVE → RECORD → CLASSIFY → TARGET STATE
```

System 03 must not manufacture scouting facts; System 04 must not turn observations into strategic attack doctrine.

## 11.4 Systems 05 ↔ 06

System 05 determines food logistics requirements and source continuity. System 06 allocates labor.

```text
FOOD REQUIREMENT
      ↓
LABOR REQUIREMENT
      ↓
WORKER ASSIGNMENT
      ↓
OBSERVED PRODUCTIVITY
      ↓
FOOD FLOW
```

A desired worker ratio is not evidence of productive food flow.

## 11.5 Systems 06 ↔ 07

System 07 declares builder requirements; System 06 owns general labor allocation.

Construction must not silently steal labor from higher-priority commitments without an explicit arbitration/preemption path.

## 11.6 Systems 07 ↔ 08

Construction supplies infrastructure prerequisites for research. Research may create future capability requirements for infrastructure.

This is a dependency relationship, not reciprocal strategic authority.

## 11.7 Systems 07/08 ↔ 09

Market may support resource feasibility for construction or research.

The downstream system remains responsible for verifying its own requirement.

```text
MARKET VERIFIED RESOURCE ACQUISITION
          ≠
CONSTRUCTION VERIFIED
          ≠
RESEARCH VERIFIED
```

## 11.8 Production ↔ Systems 05–09

Production authority creates the capability requirement. The economic systems support feasibility and execution but do not redefine the capability objective.

This boundary is essential to the future Byzantine production slice.

---

# 12. Conflict Ledger

The following conflicts are architectural risks identified from the combined Systems 01–09 model. Where a conflict is not yet demonstrated by complete rule-level source extraction, it is marked as a risk rather than a confirmed defect.

| ID | Conflict / risk | Systems | Severity | Evidence | Required resolution |
|---|---|---|---|---|---|
| X01 | Shared goal channels can acquire multiple semantic roles | 02 + all | CRITICAL | DIRECT / COMPOSED | Establish typed state registry and ownership |
| X02 | Donor duplicate `defconst` definitions can shadow or specialize state | 02 | HIGH | DIRECT | Classify every duplicate; quarantine ambiguous definitions |
| X03 | `gl-escrow-state` could be treated as policy, commitment, or transaction state | 02 + 05–09 | CRITICAL | COMPOSED | Formalize transaction-mode semantics and owner |
| X04 | Global escrow policy can be confused with attributable commitment reservation | 05/06/07/08/09 | CRITICAL | AEGIS-GENERALIZATION grounded in donor escrow mechanisms | Maintain separate ledgers/semantics |
| X05 | `gl-current-build-item` can become a strategic objective carrier | 02/07/08 | HIGH | COMPOSED | Restrict to work-item identity |
| X06 | `gl-build-progress` can be advanced by command issuance | 02/07/08 | CRITICAL | AEGIS control invariant | Require verified postcondition |
| X07 | Scouting observations can be promoted directly into attack authority | 03/04 | HIGH | Architectural risk | Require classification and strategic authorization |
| X08 | Target loss can be mistaken for strategic mission failure | 03 | HIGH | AEGIS-GENERALIZATION | Separate target lifecycle from commitment lifecycle |
| X09 | Scouting movement can be mistaken for information acquisition success | 04 | HIGH | AEGIS-GENERALIZATION | Verify informative observation, not movement alone |
| X10 | Desired labor allocation can be mistaken for productive economy | 05/06 | HIGH | DIRECT architecture | Observe productivity/resource flow |
| X11 | Farm construction can be treated as complete on command acceptance | 05/07 | CRITICAL | AEGIS evidence rule | Verify pending object/building/operational state |
| X12 | Builder allocation can bypass System 06 | 06/07 | HIGH | Architectural risk | Explicit builder requirement interface |
| X13 | Research eligibility can become automatic research authority | 08 | HIGH | Architectural risk | Separate candidate, authorization, commitment, execution |
| X14 | Research completion can be inferred from command acceptance | 08 | CRITICAL | AEGIS evidence rule | Observe research/technology state |
| X15 | Resource shortage can become automatic market authority | 09 | CRITICAL | AEGIS-GENERALIZATION | Require explicit liquidity requirement and authorization |
| X16 | `CA-*` thresholds can be interpreted without rule-level tracing | 09 | HIGH | DIRECT constants + incomplete rule evidence | Recover all writers/readers/branches before transplant |
| X17 | `LOW/MID/MID-HIGH/HIGH-ESCROW` may be assigned semantics from numeric values alone | 09 | HIGH | DIRECT constants; semantics UNCERTAIN | Recover units, selectors, writers, readers |
| X18 | `EXCESS-WOOD` can be incorrectly equated with sellable wood | 09 | HIGH | AEGIS forensic finding | Separate surplus, protected, committed, and liquid states |
| X19 | Market result can be inferred from market command | 09 | CRITICAL | AEGIS evidence rule | Verify resource deltas / economic consequence |
| X20 | Partial transaction can leave stale commitment state | 09 | HIGH | AEGIS-GENERALIZATION | Explicit PARTIAL → RECONCILE → REMAINING DEFICIT path |
| X21 | Residual escrow can be globally released | 05–09 | CRITICAL | Architectural risk | Release only attributable reservation remainder |
| X22 | `up-jump-rule` can encode hidden strategic authority | 02 + 05–09 | CRITICAL | DIRECT mechanism / AEGIS interpretation | Extract precedence graph; make authority explicit |
| X23 | Source order can substitute for formal precedence | all | HIGH | COMPOSED | Build explicit precedence/priority registry |
| X24 | Emergency bypass can become permanent alternate executor | all | CRITICAL | AEGIS-GENERALIZATION | Bound emergency paths by scope, duration, owner, verification |
| X25 | Multiple executors can issue the same transaction class | 06–09 | HIGH | Architectural risk | Establish one authoritative executor per transaction class |
| X26 | Cross-system dependency cycles can create deadlock | 05–09 | HIGH | COMPOSED | Add dependency graph + starvation/deadlock telemetry |
| X27 | A system can read stale observations as current authority | 03/04 | HIGH | AEGIS-GENERALIZATION | Freshness, epoch, expiry, generation |
| X28 | Building count can be treated as operational capability | 07/08 | HIGH | AEGIS-GENERALIZATION | Verify operational postcondition where required |
| X29 | Gross resources can be counted simultaneously by multiple commitments | 06–09 | CRITICAL | AEGIS accounting requirement | Central attributable reservation accounting |
| X30 | Verified resource acquisition may be mistaken for downstream capability acquisition | 07/08/09 | CRITICAL | AEGIS evidence model | Downstream system performs independent verification |
| X31 | Donor unused/legacy code can be mistaken for active architecture | all | HIGH | DIRECT source disclaimer | Require reachability evidence before promotion |
| X32 | Historical donor thresholds can become canonical AEGIS constants | 05/09 | HIGH | DIRECT constants | Treat coefficients as policy candidates until qualified |

---

# 13. Double-Spend and Double-Authority Audit

The cross-system architecture must explicitly reject these patterns.

## 13.1 Double-spend

```text
Commitment A reserves 300 wood
Commitment B sees gross wood = 300
Commitment B reserves 300 wood
```

Invalid.

The second commitment must see the first reservation.

## 13.2 Double executor

```text
System 07 issues build
legacy build rule also issues build
```

Invalid unless one path is explicitly classified as a bounded fallback under the same authority contract.

## 13.3 Double progression

```text
executor → progress++
verifier → progress++
```

Invalid.

Only the authoritative progression owner may advance the cursor after verification.

## 13.4 Double strategic authority

```text
threshold → strategic objective
AEGIS objective → strategic objective
```

The threshold path must not silently outrank the strategic authority.

---

# 14. Precedence and Preemption Graph

The systems need an explicit precedence hierarchy rather than relying on textual rule order.

```text
HARD SAFETY / INVALID STATE
          ↓
EMERGENCY AUTHORITY
          ↓
EXPIRED / INVALID COMMITMENTS
          ↓
HIGH-PRIORITY AUTHORIZED REQUIREMENTS
          ↓
NORMAL COMMITTED WORK
          ↓
LOW-COST UNRESERVED WORK
          ↓
LEGACY / UNAUTHORIZED PATHS
```

`up-jump-rule` may implement a mechanism for suppression/preemption, but the mechanism itself does not establish what the strategic priority ought to be.

Preemption should conceptually follow:

```text
ACTIVE
  ↓
SUSPEND
  ↓
FREEZE NEW FUNDING
  ↓
RELEASE ATTRIBUTABLE EXCESS
  ↓
AUTHORIZE HIGHER-PRIORITY COMMITMENT
  ↓
EXECUTE
  ↓
VERIFY
  ↓
RECONSIDER SUSPENDED COMMITMENT
```

Whether the engine can physically interrupt an already-issued operation remains an engine-specific qualification question.

---

# 15. Hysteresis and Stability

Without hysteresis, the cross-system architecture can oscillate:

```text
NEED → COMMIT → RELEASE → NEED → COMMIT → RELEASE
```

Every commitment-sensitive system should therefore expose, conceptually:

- activation threshold;
- maintain threshold;
- release threshold;
- preemption threshold;
- minimum dwell time/epoch;
- minimum viable reservation;
- maximum reservation age;
- starvation age.

These are AEGIS design requirements unless directly supported by donor rule tracing.

---

# 16. Deadlock and Starvation Model

The synthesis must make failure visible rather than silently retrying.

Required telemetry dimensions:

- resource starvation age;
- production starvation age;
- villager starvation age;
- infrastructure starvation age;
- research starvation age;
- strategic commitment starvation age;
- escrow concentration;
- oldest active reservation;
- percentage of gross resources unavailable;
- number of blocked prerequisites;
- number of competing authorities;
- unverified command age;
- repeated transaction failure count.

Potential cycle:

```text
Farm requires wood
   ↓
Wood requires villagers
   ↓
Villagers require food
   ↓
Food requires farm
```

The existence of such a graph does not itself prove deadlock; deadlock requires inability of the current authority/resource allocation state to make progress. The graph is therefore diagnostic infrastructure, not a strategy rule.

---

# 17. Donor-to-AEGIS Transformation Rule

Every mechanism crossing from forensic corpus into implementation should pass this four-stage transformation:

```text
DONOR FACT
    ↓
RULE-LEVEL RECONSTRUCTION
    ↓
AEGIS INTERPRETATION / CRITIQUE
    ↓
IMPLEMENTATION CONTRACT
```

For example:

```text
DONOR FACT:
CA-WOOD-TRADING-THRESHOLD = 300

RULE-LEVEL QUESTION:
Who reads it? Under what predicates? What command follows? What state changes?

AEGIS INTERPRETATION:
Potential wood-trading decision boundary; exact semantic role unresolved.

IMPLEMENTATION REQUIREMENT:
Do not transplant 300 as a canonical threshold until its complete rule path,
unit, scope, ownership, precedence, and resource consequence are recovered.
```

Likewise:

```text
DONOR FACT:
gl-escrow-state exists and participates in escrow-aware operations.

AEGIS INTERPRETATION:
Useful transaction-mode carrier.

IMPLEMENTATION REQUIREMENT:
Formalize owner, generation, lifetime, legal values, transaction linkage,
preflight semantics, reset/release conditions, and verification interaction.
```

---

# 18. Cross-System Authority Rules

The implementation must satisfy the following rules.

### AUTH-01 — One strategic owner

Every strategic objective has one authoritative owner.

### AUTH-02 — Domain systems cannot promote local facts into strategic objectives without explicit policy authority.

### AUTH-03 — One authoritative owner per critical state carrier.

### AUTH-04 — Writers must be enumerated; readers do not imply ownership.

### AUTH-05 — Executor authority does not imply strategic authority.

### AUTH-06 — Verification authority is distinct from command authority.

### AUTH-07 — Progression authority is distinct from executor authority.

### AUTH-08 — Preemption authority must be explicit.

### AUTH-09 — Emergency bypass must be attributable, bounded, and reversible.

### AUTH-10 — Duplicate legacy executors must not silently coexist with the canonical executor.

---

# 19. Cross-System Resource Rules

### RES-01
Gross resource is not automatically liquid resource.

### RES-02
Policy protection is not attributable commitment escrow.

### RES-03
Commitment escrow is not transaction escrow.

### RES-04
Every reservation has an owner and purpose.

### RES-05
Every reservation has a release condition.

### RES-06
Residual reservation must be reconciled after completion or partial completion.

### RES-07
A failed transaction does not justify global escrow reset.

### RES-08
A downstream system must not assume another system's resource acquisition is complete until verified evidence exists.

### RES-09
Resource accounting must expose competing commitments sufficiently to prevent double-spending.

### RES-10
Historical coefficients remain policy candidates until rule-level and, where necessary, runtime qualification.

---

# 20. Cross-System Verification Rules

### VER-01
Command acceptance is W0, not completion.

### VER-02
Pending state is not world-state completion.

### VER-03
Every transaction class defines its sufficient postcondition.

### VER-04
The postcondition must be observed, not inferred from intent.

### VER-05
Partial results require reconciliation.

### VER-06
Unverified actions do not advance strategic progress.

### VER-07
Verification failures are first-class states.

### VER-08
A downstream capability must be independently verified by the system responsible for that capability.

### VER-09
Observation freshness and generation must be part of validity where stale information could alter authority.

### VER-10
Strategic effect is a separate evidence promotion step after capability verification.

---

# 21. Required Static Extraction Before `.per` Implementation

The cross-system synthesis is not an implementation substitute. Before Muse implements the `.per` layer, the following static extraction must be completed for all shared and cross-boundary symbols:

1. definition;
2. every writer;
3. every reader;
4. every conditional definition;
5. every comparison operator;
6. every predecessor predicate;
7. every successor effect;
8. source-order position;
9. `up-jump-rule` interactions;
10. suppression/preemption interactions;
11. command issued;
12. goal/SN/timer mutation;
13. resource implication;
14. reset/clear;
15. expiry;
16. downstream reader;
17. cross-system owner;
18. evidence class;
19. donor disposition;
20. AEGIS improvement opportunity.

The highest-priority unresolved cross-system extraction targets are:

- `gl-escrow-state`;
- `gl-current-build-item`;
- `gl-build-progress`;
- `gl-progression-pause`;
- all escrow predicates and commands;
- all `up-jump-rule` paths touching shared work;
- market threshold symbols;
- construction fallback paths;
- research progression paths;
- food/farm transitions;
- labor assignment transitions;
- target/scouting observation handoffs.

---

# 22. Implementation Gate

No broad `.per` implementation should be accepted merely because the modules compile/load.

The required gate is:

```text
SYSTEM 01–09 SYNTHESIS
        ↓
SHARED STATE REGISTRY
        ↓
WRITER / READER GRAPH
        ↓
AUTHORITY GRAPH
        ↓
PRECEDENCE / JUMP GRAPH
        ↓
RESOURCE RESERVATION GRAPH
        ↓
DEPENDENCY / DEADLOCK GRAPH
        ↓
VERIFICATION CONTRACTS
        ↓
AEGIS IMPROVEMENT REVIEW
        ↓
.PER IMPLEMENTATION
        ↓
STATIC QUALIFICATION
        ↓
MINIMAL RUNTIME QUALIFICATION
        ↓
VERTICAL-SLICE ACCEPTANCE
```

The implementation must be rejected if any of the following remain opaque for a critical state carrier:

- owner unknown;
- competing writer unknown;
- lifetime unknown;
- reset/expiry unknown;
- precedence unknown;
- transaction linkage unknown;
- verification path absent;
- resource consequence unaccounted;
- strategic authority ambiguous.

---

# 23. First Integrated Vertical Slice

The first cross-system qualification should not attempt to exercise all nine systems simultaneously.

Recommended slice:

```text
FOOD CONTINUITY REQUIREMENT
        ↓
SYSTEM 05 FOOD REQUIREMENT
        ↓
SYSTEM 06 WOOD LABOR ALLOCATION
        ↓
OBSERVED WOOD FLOW
        ↓
SYSTEM 07 FARM REQUIREMENT
        ↓
COMMITMENT / ESCROW
        ↓
BUILDER ALLOCATION
        ↓
ESCROW-AWARE BUILD PREFLIGHT
        ↓
BUILD COMMAND
        ↓
PENDING FARM
        ↓
FARM COMPLETION / OPERATIONAL VERIFICATION
        ↓
RESERVATION RECONCILIATION
        ↓
SYSTEM 05 FOOD REASSESSMENT
```

This slice tests the most important shared boundaries without requiring the entire military/strategic stack to be operational.

The success criterion is not that a farm command fires. It is that the full causal chain becomes observable and reconcilable.

---

# 24. Second Integrated Slice

After the first slice:

```text
AUTHORIZED TECHNOLOGY REQUIREMENT
        ↓
SYSTEM 08 RESEARCH COMMITMENT
        ↓
RESOURCE RESERVATION
        ↓
SYSTEM 06 / SYSTEM 09 FEASIBILITY SUPPORT
        ↓
RESEARCH PREFLIGHT
        ↓
RESEARCH COMMAND
        ↓
RESEARCH STATE OBSERVATION
        ↓
TECHNOLOGY VERIFICATION
        ↓
CAPABILITY UPDATE
        ↓
RESERVATION RECONCILIATION
```

This tests whether research can use the common commitment/transaction substrate without acquiring ownership of strategic objective selection.

---

# 25. Third Integrated Slice

Only after the first two slices are stable:

```text
AUTHORIZED LIQUIDITY REQUIREMENT
        ↓
SYSTEM 09 MARKET CANDIDATE
        ↓
LIQUIDITY / RESERVATION CHECK
        ↓
MARKET TRANSACTION
        ↓
RESOURCE DELTA OBSERVATION
        ↓
TRANSACTION VERIFICATION
        ↓
RECONCILIATION
        ↓
DOWNSTREAM REQUIREMENT REASSESSMENT
```

This is the correct place to qualify the donor market thresholds and escrow semantics rather than assuming their meanings from declarations.

---

# 26. What This Synthesis Changes

The purpose of this document is not merely to document dependencies. It changes the engineering decision surface.

The project should no longer ask:

> “Which donor rule should be copied next?”

It should ask:

> “Which authoritative requirement is being satisfied, which commitment funds it, which executor performs it, what world-state postcondition proves it, and how is the resulting state reconciled across every dependent subsystem?”

This also changes how donor quality is evaluated.

A donor mechanism may be preserved because it solves a useful execution problem while simultaneously being improved because its authority boundary is implicit, its state is overloaded, its coefficients are opaque, or its verification semantics are weak.

The target is therefore **not Shadow reproduction**.

The target is:

```text
DONOR EXECUTION KNOWLEDGE
          +
AEGIS EXPLICIT AUTHORITY
          +
AEGIS RESOURCE ACCOUNTING
          +
AEGIS VERIFICATION
          +
AEGIS FAILURE / RECOVERY
          +
AEGIS CROSS-SYSTEM ARBITRATION
          ↓
A BETTER `.PER` CONTROL SYSTEM
```

---

# 27. Definition of Done

Systems 01–09 cross-system synthesis is complete only when the project can answer, from repository evidence and qualification evidence rather than assumption:

1. Who owns every strategic objective?
2. Who creates each requirement?
3. Who owns each commitment?
4. Who reserves each resource?
5. Who may release it?
6. Who may preempt it?
7. Who owns each transaction class?
8. Which executor issues each command?
9. Which fallback executors exist?
10. Which state carriers connect the systems?
11. Who writes each carrier?
12. Who reads each carrier?
13. What is each carrier's lifetime?
14. What invalidates it?
15. What expires it?
16. What is its precedence?
17. What evidence level does each transition provide?
18. What observation proves completion?
19. What observation proves capability?
20. What happens on partial completion?
21. What happens on failure?
22. What happens on preemption?
23. What happens on cancellation?
24. How is residual escrow reconciled?
25. How is double-spending prevented?
26. How is starvation detected?
27. How is deadlock detected?
28. Where can `up-jump-rule` suppress another path?
29. Where can source order create accidental precedence?
30. Where does any domain system accidentally acquire strategic authority?
31. Which donor facts remain unresolved?
32. Which AEGIS improvements are deliberate redesign?
33. Which semantics require runtime qualification?
34. Which `.per` implementation paths are uniquely authoritative?
35. Which verification paths close the loop back to reassessment?

If any critical answer is “unknown,” the architecture is not ready for unrestricted implementation.

---

# 28. Final Engineering Directive

Muse should treat Systems 01–09 as **one control architecture with nine domain boundaries**, not nine libraries.

The implementation priority is:

```text
1. AUTHORITATIVE STATE REGISTRY
2. REQUIREMENT / COMMITMENT CONTRACT
3. RESOURCE RESERVATION CONTRACT
4. TRANSACTION CONTRACT
5. VERIFICATION CONTRACT
6. CROSS-SYSTEM DEPENDENCY GRAPH
7. PRECEDENCE / PREEMPTION GRAPH
8. DOMAIN EXECUTORS
9. RUNTIME QUALIFICATION
```

Do not optimize the domain executors before the authority and accounting substrate is coherent.

Do not promote donor constants into canonical policy without recovering their rule paths.

Do not treat source presence as active architecture.

Do not treat command acceptance as completion.

Do not allow a domain subsystem to become a second strategic brain.

And do not merely transplant mechanisms that are demonstrably improvable.

The correct engineering objective is:

> **Extract what the donor actually does, explicitly model why it works, identify where its authority and verification boundaries are weak, improve those boundaries, implement the improved contract in `.per`, and qualify the resulting world-state transitions.**

That is the control-plane gate for the transition from forensic reconstruction to implementation.
