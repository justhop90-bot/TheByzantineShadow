# The Byzantine Shadow — System 02 State Namespace & Authority Forensics v0.1

**Status:** Forensic engineering specification  
**System:** 02 — State Namespace / State Authority  
**Scope:** Goals, strategic numbers, counters, coordinates, enumerations, mode carriers, progression state, ownership, lifetime, reset semantics, and authority boundaries.  
**Evidence class:** Primarily DIRECT/COMPOSED from the existing Shadow forensic corpus; architectural prescriptions are AEGIS-GENERALIZATION and must not be represented as runtime-proven engine facts.

---

## 0. Executive Finding

The next system to isolate after initialization/configuration is not another behavioral subsystem. It is the **state namespace itself**.

The forensic corpus establishes that the Shadow donor is a distributed control system whose state is carried through goals, strategic numbers, timers, thresholds, coordinates, counters, progression markers, escrow state, and rule-order side effects. The forensic baseline reports approximately **1,503 constants, 1,193 goal writes, and 440 strategic-number writes** across the donor. This makes state ownership the highest-leverage architectural problem immediately after configuration.

The central finding is:

> **Shadow's state representation is richer than its explicit state model.**

The donor contains numerous state carriers, but their semantic classes are not represented in a canonical registry. Consequently, a numeric goal/SN may simultaneously function as fact, mode, counter, coordinate, latch, scheduler cursor, progress marker, temporary value, or control signal depending on context.

For AEGIS, this is unacceptable at the authority boundary. The implementation must therefore preserve useful donor semantics while rebuilding the namespace as an explicit, typed, owner-controlled state system.

This is not permission to rename or rewrite everything. The correct task is to determine **what every critical state variable means, who owns it, who may write it, what lifetime it has, what invalidates it, and what evidence it represents**.

---

## 1. Forensic Basis

### 1.1 Direct donor scale

The existing forensic deep dive records:

- 1,503 constants;
- 1,193 goal writes;
- 440 strategic-number writes;
- 188 jump calls;
- 178 escrow-percentage writes;
- 107 escrow releases;
- 43 escrow-aware builds;
- 28 escrow-aware researches;
- 4 escrow-aware trains.

These counts are static source evidence. They establish namespace/control complexity, **not runtime frequency or causal importance**.

### 1.2 Existing architecture already identifies the problem

The Shadow forensic decomposition classifies the state namespace as a major subsystem: goals/SNs encode facts, modes, counters, coordinates, and state machines. Its disposition is **preserve semantics; rebuild registry**.

The integrated blueprint further identifies `gl-current-build-item`, `gl-build-progress`, `gl-progression-pause`, and `gl-escrow-state` as semantically important state carriers rather than miscellaneous variables.

The strategic-control blueprint identifies rule ordering, `up-jump-rule`, current work-item state, progression markers, pauses, resource policy, affordability constraints, transaction side effects, and completion feedback as contributors to effective priority.

These findings converge on one conclusion: **state semantics are part of the control architecture and must be audited independently of behavior.**

---

## 2. State Taxonomy

Every Shadow state carrier must be assigned a semantic class. A variable may not remain an unclassified integer merely because the engine exposes it as a goal or strategic number.

### 2.1 Required semantic classes

| Class | Meaning | Examples / candidates |
|---|---|---|
| FACT | Observed or engine-derived state believed to represent current world state. | resource count, age, population, building count |
| BELIEF | Model-derived interpretation of observations. | enemy strategy hypothesis, threat classification |
| MODE | Current operating mode or policy regime. | escrow mode, economic mode, tactical mode |
| ENUMERATION | Encoded finite state/identity. | commitment state, transaction state, verification state |
| COUNTER | Monotonic or bounded progress/failure/age count. | retry count, progress index |
| CURSOR | Pointer to current item/phase in a sequence. | `gl-build-progress` |
| IDENTITY | Identity of a work item, commitment, transaction, owner, or target. | `gl-current-build-item` |
| COORDINATE | Spatial state. | home/target positions, geometry values |
| TIMER / EPOCH | Temporal state used for expiry, dwell, cooldown, or age. | timestamps, strategic-number timers |
| THRESHOLD | Policy boundary used in a predicate. | escrow level, activation/release threshold |
| LATCH | State intentionally held until an explicit clearing event. | pause/suppression state |
| AUTHORITY | Ownership/generation/permission state. | owner ID, generation, valid bit |
| RESERVATION | Economic state tied to a commitment or transaction. | escrow amount, resource reservation |
| EVIDENCE | Diagnostic or verification result. | verification status, observed postcondition |
| TELEMETRY | Inspection/diagnostic exposure. | starvation indicators, debug state |

A single physical goal/SN may implement one or more of these only if the implementation has an explicit representation of the distinction. **Semantic overloading without an ownership/lifetime contract is prohibited for new authoritative state.**

---

## 3. The Critical Distinction: Value vs. Meaning

The same numeric value can have radically different semantics depending on the state carrier and writer.

For example:

```text
SN = 3
```

could mean:

- third progression item;
- three retries;
- economic mode 3;
- player index 3;
- three seconds/minutes of a timer;
- a unit/building identifier;
- a coordinate component.

Therefore the canonical registry must not be merely a list of names and values. It must record the **semantic contract** around the value.

Minimum registry fields:

```text
symbol
physical_channel      ; goal / strategic-number / other
semantic_type
owner
writers
readers
initial_value
valid_range
enumeration_map
unit_or_scale
creation_condition
lifetime
reset_condition
expiry_condition
invalidation_condition
precedence
side_effects
evidence_level
status
```

Where a field cannot yet be established, record `UNKNOWN` rather than inventing semantics.

---

## 4. Authority Model

The fundamental redesign is an explicit **single-writer authority model for critical state**.

For each authoritative state variable:

```text
STATE = {VALUE, OWNER, GENERATION, VALID, EPOCH, EVIDENCE_LEVEL}
```

The exact .per encoding is Muse's implementation decision. The semantic contract is not.

### 4.1 Owner

Every authoritative state field must have a declared owner.

Examples:

- AEGIS owns strategic objective state.
- Production Authority owns production authorization state.
- Shadow owns commitment funding and transaction state.
- AIByzBuild owns concrete executor activity.
- Verification owns verification result generation.

No subsystem may silently write another subsystem's authoritative state merely because it can reach the underlying goal/SN.

### 4.2 Generation

A generation/token concept is required where stale state can survive across retries, work items, or strategic decisions.

Conceptually:

```text
C17 generation 4
T17-2 generation 9
```

A late result from generation 8 must not mutate the current generation 9 authority state.

If the target .per ABI cannot encode a full generation model directly, Muse must create the strongest equivalent guard available and document the residual uncertainty.

### 4.3 Validity

State must be distinguishable between:

```text
VALID
INVALID
NOT_INITIALIZED
EXPIRED
UNKNOWN
```

A numeric sentinel such as `-1` may be useful historically, but its semantics must be explicitly established before it is used as a universal invalid value.

---

## 5. Lifetime and Reset Semantics

State lifetime is as important as state value.

Every critical state carrier must be assigned one of these lifetimes:

- game lifetime;
- civilization lifetime;
- strategic-episode lifetime;
- commitment lifetime;
- transaction lifetime;
- work-item lifetime;
- rule-evaluation lifetime;
- tick/epoch lifetime;
- temporary/latch lifetime.

The registry must define both **creation** and **destruction/reset** conditions.

### 5.1 Mandatory question

For every critical state variable, Muse must be able to answer:

> What event makes the old value no longer authoritative?

If the answer is “the next rule overwrites it,” that is not a sufficient contract for new architecture.

### 5.2 Reset hazards

Particular attention is required for:

- repeated strategy transitions;
- work-item reuse;
- player/target changes;
- map-size or geometry specialization;
- age transitions;
- commitment cancellation;
- transaction retry;
- preemption and resumption;
- initialization re-entry;
- conditional compilation branches.

A stale cursor, coordinate, owner, or escrow mode can create behavior that appears strategically irrational while actually being a state-lifetime defect.

---

## 6. State Machines Must Not Be Collapsed

The donor's procedural structure makes it tempting to encode a large number of meanings into one “current status” variable. Do not do this.

At minimum, Shadow requires separate dimensions for:

### Commitment

```text
CANDIDATE
PREPARING
COMMITTED
FUNDED
EXECUTING
SUSPENDED
VERIFIED
RETIRING
RETIRED
CANCELLED
EXPIRED
INVALIDATED
PREEMPTED
FAILED
BLOCKED
DEADLOCKED
```

### Transaction

```text
REQUESTED
RESERVING
RESERVED
PREFLIGHT
AUTHORIZED
ISSUED
OBSERVING
CONFIRMED
PARTIAL
REJECTED
FAILED
UNVERIFIED
RELEASED
EXPIRED
```

### Verification

```text
NOT_STARTED
PENDING
PASS
PARTIAL
FAIL
UNKNOWN
```

### Work-item progression

```text
CREATED
REQUIREMENT_DECLARED
RESERVATION_REQUESTED
RESERVATION_FUNDED
EXECUTION_AUTHORIZED
COMMAND_ISSUED
POSTCONDITION_OBSERVED
CONFIRMED
PROGRESS_ADVANCED
```

These are semantically different machines. Combining them into one goal increases ambiguity and makes failure recovery unsafe.

---

## 7. Critical Existing State Carriers

### 7.1 `gl-escrow-state`

**Disposition:** KEEP / FORMALIZE.

Direct donor evidence shows that this state is passed into transactional primitives such as `up-build`, `up-research`, and `up-train`, with explicit `with-escrow` / `without-escrow` switching.

Engineering interpretation: this is a **transaction-mode carrier**, not a strategic objective.

Requirements:

- explicit owner;
- valid modes;
- transition conditions;
- lifetime bound to transaction context;
- no stale mode leaking into an unrelated transaction;
- no implication that `with-escrow` means “success.”

### 7.2 `gl-current-build-item`

**Disposition:** KEEP / REFACTOR.

Treat as work-item identity, not merely a build-order integer.

It should identify the current economic/progression object sufficiently to bind:

```text
work item → requirement → commitment → transaction → verification
```

### 7.3 `gl-build-progress`

**Disposition:** KEEP / REFACTOR.

Treat as a progression cursor. It may advance only after the current work item's completion predicate has been verified.

### 7.4 `gl-progression-pause`

**Disposition:** KEEP / REFACTOR.

Treat as pending/suspended progression state. It must not become an unbounded global latch with unclear release semantics.

Required contract:

```text
pause owner
pause reason
creation epoch
resume predicate
expiry / invalidation
higher-priority override
```

### 7.5 Coordinates

The donor contains repeated spatial constants/state such as `home-x`, `home-y`, and `gl-position` in a namespace with duplicate/conditional definitions.

Do not assume duplicate textual names imply duplicate runtime semantics. First classify:

- map specialization;
- conditional definition;
- true collision;
- shadowed definition;
- stale legacy definition.

Coordinate state must additionally record coordinate frame/reference semantics where relevant.

---

## 8. Duplicate Definitions and Namespace Collisions

The donor contains approximately 1,500 distinct constants and duplicate definitions. The existence of duplicate names is not itself proof of a bug; conditional compilation and map specialization can legitimately produce repeated definitions.

However, duplicate definitions become dangerous when:

1. multiple branches can coexist;
2. the active definition is unclear;
3. readers assume a different range/type;
4. a later definition silently changes meaning;
5. a legacy writer remains reachable;
6. the same semantic concept has multiple physical channels.

### 8.1 Required classification

Every duplicate critical symbol must be assigned:

```text
LEGITIMATE_CONDITIONAL
LEGITIMATE_SPECIALIZATION
SHADOWED
CONFLICTING
LEGACY
UNKNOWN
```

No duplicate critical symbol may be used as a new architectural dependency until classified.

---

## 9. Writer/Reader Graph

The state audit should construct a directed graph:

```text
WRITER → STATE → READER
```

with metadata:

```text
writer type
rule/file
condition
write operation
value domain
precedence
side effects
reader condition
reader interpretation
owner
```

The most important graph is not simply “what references what.” It is:

> **Who can mutate an authoritative state value, under what condition, and which competing writer wins?**

This is the state equivalent of the Production Authority Matrix already being developed in AEGIS.

### 9.1 Required graph classifications

- single writer;
- multiple writers / same authority;
- multiple writers / competing authority;
- conditional mutually exclusive writers;
- legacy writer;
- emergency bypass writer;
- unauthorized writer;
- dead writer;
- reader-only state;
- write-only state;
- apparent telemetry state that actually affects control.

---

## 10. Precedence Is Part of State Semantics

A state variable with multiple writers does not have a meaningful contract until precedence is known.

Precedence may arise from:

- rule order;
- `up-jump-rule`;
- explicit priority number;
- temporal guard;
- conditional exclusivity;
- later overwrite;
- state-machine gating.

Muse must therefore record precedence explicitly instead of treating source order as an incidental implementation detail.

Required representation:

```text
STATE S
  writer A: priority P1
  writer B: priority P2
  writer C: emergency override
  conflict rule: C > B > A
  tie behavior: explicit
```

If precedence cannot be established statically, mark it `UNCERTAIN` and do not promote it into a critical strategic authority claim.

---

## 11. Evidence Semantics of State

A state variable should carry an evidence classification where its value is derived from observations.

Example:

```text
enemy-cavalry-count = 6
```

could represent:

- DIRECT: six enemy cavalry observed now;
- COMPOSED: six from several observation events;
- BELIEF: estimated six;
- STALE: six observed earlier but not revalidated;
- UNKNOWN: six was written by an unqualified path.

The numerical value alone is insufficient.

AEGIS therefore needs the distinction:

```text
VALUE
SOURCE
EPOCH
CONFIDENCE / EVIDENCE_LEVEL
VALIDITY
```

This is particularly important when Shadow state feeds strategic arbitration.

---

## 12. Interaction with Escrow and Commitment

State namespace discipline is directly coupled to the economic kernel.

For each reservation, Shadow must prevent these states from being confused:

```text
policy protection
commitment reservation
transaction reservation
actual consumption
released remainder
```

A state carrier representing “reserved” must identify **what is reserved, for whom, and at which lifecycle level**.

Conceptually:

```text
RESOURCE
  ├─ POLICY_ESCROW
  ├─ COMMITMENT_ESCROW[C17]
  └─ TRANSACTION_ESCROW[T17-2]
```

The state registry must make those ownership distinctions explicit even if the .per representation is compressed.

---

## 13. Interaction with Progression

Progression is especially vulnerable to stale state.

The minimum safe dependency chain is:

```text
CURRENT_WORK_ITEM
      ↓
REQUIREMENT
      ↓
COMMITMENT
      ↓
TRANSACTION
      ↓
COMMAND
      ↓
OBSERVATION
      ↓
VERIFICATION
      ↓
PROGRESS_CURSOR
```

The following shortcut is prohibited:

```text
COMMAND
  ↓
PROGRESS_CURSOR++
```

A jump to the next item is itself an authority effect. It must therefore be conditioned on the verified state of the current item.

---

## 14. Interaction with Strategic Control

Shadow must expose economic state upward without allowing economic state to become an implicit strategic planner.

Correct:

```text
AEGIS:
  commitment = anti-cavalry capability
  priority = high
  minimum viable = 4 camels

Shadow:
  required resources = X
  commitment funding = Y
  transaction feasible = true
  transaction = T42
  verified production = 2/4
```

Incorrect:

```text
resources low
  → Shadow decides cavalry is the threat
  → Shadow chooses camels
  → Shadow silently creates strategic objective
```

Economic feasibility is an input to strategy, not a substitute for strategy.

---

## 15. Telemetry Must Not Become Authority by Accident

The donor contains extensive telemetry/inspection state. Muse must explicitly classify telemetry.

A diagnostic variable is not authoritative merely because another rule reads it.

Every telemetry field must be marked:

```text
OBSERVATIONAL_ONLY
CONTROL_INPUT
AUTHORITY_STATE
UNKNOWN
```

If a supposedly diagnostic field controls a branch, it is not merely telemetry and must enter the authority graph.

This is a high-value audit target because hidden telemetry-to-control coupling can explain behavior that is otherwise invisible in strategic documentation.

---

## 16. Required Static Analysis for System 02

Before broad implementation, produce a machine-readable or tabular state registry from the donor.

At minimum extract:

1. every `defconst` relevant to runtime state;
2. every goal/SN write;
3. every goal/SN read;
4. every state-like enumeration;
5. every sentinel value;
6. every timer/epoch pattern;
7. every coordinate carrier;
8. every progression carrier;
9. every escrow-state carrier;
10. every jump/order write that changes effective state;
11. every duplicate symbol;
12. every writer competing for the same state;
13. every cross-file state dependency;
14. every conditional definition;
15. every state reset/clear operation;
16. every state value consumed as a predicate;
17. every state value used to authorize an executor command.

For each item, preserve source location and evidence level.

---

## 17. Required Runtime Qualification Targets

Do not attempt to qualify the entire namespace at once. Select a critical slice.

### First slice

```text
gl-current-build-item
gl-build-progress
gl-progression-pause
gl-escrow-state
```

Then qualify:

```text
commitment identity
transaction identity
verification state
reservation state
owner/generation guard
```

The qualification question is not merely “does the value change?” It is:

> Does the state transition occur for the correct reason, under the correct authority, with the correct lifetime, and does a competing or stale writer fail to corrupt it?

---

## 18. Engineering Prescription to Muse

### 18.1 Do not start by rewriting all goals/SNs

First create the semantic registry. Then identify the minimum authoritative state required for the first vertical slice.

### 18.2 Do not assume one physical channel equals one semantic variable

A goal/SN is a storage primitive. The semantic type must be established independently.

### 18.3 Do not create a giant universal state integer

Separate commitment, transaction, verification, progression, ownership, and validity semantics.

### 18.4 Do not let source order remain the only authority mechanism

Where multiple writers exist, expose precedence explicitly and preserve procedural order only where qualification shows it is necessary.

### 18.5 Do not remove legacy state prematurely

Quarantine it. Prove unreachable or superseded status first.

### 18.6 Improve the donor where improvement reduces ambiguity without destroying behavior

Priority improvements include:

- typed/semantic registry;
- explicit ownership;
- generation/stale-result protection;
- explicit lifetime/reset rules;
- bounded retry state;
- explicit verification state;
- explicit commitment/transaction separation;
- normalized telemetry;
- controlled legacy bypasses.

---

## 19. System 02 Exit Criteria

System 02 is complete only when the implementation team can answer, for every critical Shadow state carrier:

1. What does it mean?
2. What physical channel stores it?
3. What values are legal?
4. Who owns it?
5. Who writes it?
6. Who reads it?
7. What is the precedence among writers?
8. When is it created?
9. How long is it valid?
10. What invalidates it?
11. What resets it?
12. What evidence does its value represent?
13. Can stale state survive into a new strategic episode?
14. Can a retry write the wrong generation?
15. Can a legacy writer override it?
16. Can telemetry mutate or authorize it?
17. Can it falsely advance progression?
18. Can it falsely release or retain escrow?
19. Can it silently become strategic authority?
20. What remains UNCERTAIN?

If any critical field cannot answer these questions, its semantics remain unqualified.

---

## 20. Final Finding

The deepest lesson from System 02 is that **state is not passive storage in Shadow**. State is the mechanism through which authority persists across rule evaluations.

A goal or strategic number is therefore not “just a variable.” When it controls progression, escrow, priority, executor authorization, or verification, it is part of the control plane.

The engineering objective is consequently not to make Shadow's state namespace prettier. It is to make it **auditable, attributable, temporally valid, non-ambiguous, and safe under competing writers** while preserving the donor's proven economic behavior.

The desired result is:

```text
OBSERVATION
  → STATE WRITE
  → CLASSIFICATION
  → AUTHORITY EFFECT
  → ECONOMIC / EXECUTION CONSEQUENCE
  → POSTCONDITION
  → VERIFICATION
  → STATE RECONCILIATION
  → REASSESSMENT
```

The state layer must be capable of representing that entire causal chain without collapsing its distinct stages into a single numeric flag.

**System 02 disposition: PRESERVE useful donor state semantics; REBUILD the authoritative registry; FORMALIZE ownership, lifetime, generation, precedence, and evidence; QUALIFY the critical state slice before broad implementation.**
