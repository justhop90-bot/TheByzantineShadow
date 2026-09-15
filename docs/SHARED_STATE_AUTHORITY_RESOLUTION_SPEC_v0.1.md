# The Byzantine Shadow — Shared-State Authority Resolution Specification v0.1

**Purpose:** Convert the Systems 01–09 cross-system synthesis into an enforceable authority model for shared mutable state.

**Status:** Architectural control specification; implementation is not authorized merely by this document. Engine semantics and donor rule paths remain subject to qualification.

**Evidence taxonomy:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN.

---

## 0. Executive directive

Systems 01–09 must not form nine independent controllers writing into a common namespace. The shared namespace is a control-plane resource. Every mutable shared state carrier therefore requires an explicit owner, mutation authority, generation, validity, lifetime, verification source, and conflict policy.

The governing invariant is:

> **One authoritative owner per mutable semantic state; many readers are permitted; mutation occurs only through an authorized transition path; completion is established by observation and verification, not by command issuance.**

This specification is an AEGIS architectural generalization unless a cited donor rule proves the same semantics directly.

---

# 1. Single-writer doctrine

## 1.1 Rule

Every mutable shared semantic state has exactly one authoritative owner at a given architecture generation.

A system may have multiple physical rule sites that write state only when those writes are explicitly subordinate to the same owner and obey the owner's mutation contract.

Therefore:

```text
MULTIPLE RULE SITES
        ↓
SAME AUTHORITY OWNER
        ↓
COMMON MUTATION CONTRACT
        ↓
SINGLE SEMANTIC WRITER
```

A second system writing the same semantic state without delegation is a **CONFLICT**, not a convenience.

## 1.2 Reader freedom

Readers may:

- inspect state;
- derive requirements from state;
- request action based on state;
- report inconsistencies;
- provide observations to the owner.

Readers may not silently normalize, repair, clear, overwrite, or advance authoritative state.

## 1.3 Physical aliases

Different symbols may represent the same semantic state. Numeric identity does not establish semantic identity. Conversely, different semantic states must not be merged merely because they use adjacent or familiar goal channels.

---

# 2. Authority envelope

Every authoritative shared state should conceptually carry:

```text
VALUE
OWNER
GENERATION
VALID
EPOCH
EVIDENCE_LEVEL
LIFETIME
```

For critical transaction/commitment state additionally:

```text
COMMITMENT_ID
TRANSACTION_ID
REQUIREMENT_ID
PRIORITY
EXPIRY
```

The envelope is architectural. The exact physical representation in `.per` must be qualified against available goal/SN/timer channels and engine behavior.

---

# 3. Canonical mutation path

No shared mutable state should be mutated by arbitrary downstream rules.

The canonical path is:

```text
REQUEST
  ↓
AUTHORITY CHECK
  ↓
OWNER / GENERATION CHECK
  ↓
VALIDITY CHECK
  ↓
PRECONDITION CHECK
  ↓
MUTATION AUTHORIZATION
  ↓
STATE MUTATION
  ↓
OBSERVATION
  ↓
VERIFICATION
  ↓
RECONCILIATION
```

For executor state:

```text
REQUIREMENT
 → COMMITMENT
 → TRANSACTION
 → AUTHORIZATION
 → EXECUTOR
 → COMMAND
 → OBSERVATION
 → VERIFICATION
 → RESULT
```

`COMMAND` is never the terminal state.

---

# 4. Conflict classes

| Conflict class | Definition | Required response |
|---|---|---|
| COMPETING_WRITERS | Two systems claim semantic ownership | Freeze promotion; establish owner |
| SHARED_WRITE_SAME_AUTHORITY | Multiple physical writers under one owner | Formalize common mutation path |
| STALE_WRITER | Older generation attempts mutation | Reject/ignore mutation |
| CONDITIONAL_WRITER | Writer exists only under configuration branch | Qualify branch and authority |
| LEGACY_WRITER | Historical path remains reachable | Quarantine or formally delegate |
| DUPLICATE_EXECUTOR | Two paths can issue same operation | Establish one execution authority |
| STRATEGIC_LEAKAGE | Executor/economic subsystem originates objective | Remove or subordinate path |
| BYPASS_PATH | Action bypasses requirement/commitment/authority layer | Classify and eliminate or explicitly authorize |
| PROGRESSION_RACE | Multiple paths advance same cursor | Single progression owner |
| RESERVATION_RACE | Multiple paths reserve/release same resources | Commitment/transaction owner arbitration |
| VERIFICATION_RACE | Multiple paths declare completion | One verification authority per result class |
| RESET_COLLISION | Independent paths clear shared state | Owner-only reset |
| EXPIRY_COLLISION | Multiple lifetimes govern one state | Establish canonical expiry |
| TELEMETRY_MUTATION | Diagnostic code changes control state | Prohibit unless explicitly authorized |
| ALIAS_COLLISION | Different symbols map to same physical semantic slot | Registry reconciliation required |
| SEMANTIC_COLLISION | Same symbol is used for incompatible meanings | Split state or quarantine use |

---

# 5. Precedence model

Precedence is semantic authority, not merely source order.

```text
1. HARD SAFETY / ENGINE CONSTRAINT
2. BOUNDED EMERGENCY AUTHORITY
3. STRATEGIC AUTHORITY
4. COMMITMENT AUTHORITY
5. TRANSACTION AUTHORITY
6. SYSTEM EXECUTOR
7. LEGACY / COMPATIBILITY PATH
8. TELEMETRY
```

A lower layer cannot override a higher layer merely because its rule executes later in source order.

## 5.1 Emergency exception

Emergency authority is:

- explicit;
- bounded;
- attributable;
- time-limited;
- reversible where physically possible;
- verified;
- followed by reconciliation.

An emergency path does not acquire permanent ownership by exercising preemption.

## 5.2 Rule order

`up-jump-rule` and source ordering are implementation mechanisms. They are not substitutes for an authority model. Every use that suppresses or preempts another path must identify the authority relationship it implements.

---

# 6. Generation control

Generation prevents stale logical work from mutating newer state.

Canonical model:

```text
STATE(G=7)
   ↓
NEW DECISION
   ↓
STATE(G=8)
```

A pending operation carrying `G=7` cannot overwrite or complete a `G=8` state unless an explicit reconciliation rule permits it.

Generation must advance on material replacement of:

- strategic objective;
- commitment identity;
- requirement identity;
- transaction identity;
- target identity where target generation matters;
- progression work item;
- materially invalidated reservation.

Generation is distinct from time. A newer epoch does not automatically imply a new generation.

---

# 7. Preemption specification

Preemption is an authority transition, not merely a jump to another rule.

```text
ACTIVE
  ↓
PREEMPTION TEST
  ↓
SUSPEND
  ↓
FREEZE NEW FUNDING
  ↓
RECONCILE ATTRIBUTABLE RESERVATIONS
  ↓
AUTHORIZE HIGHER PRIORITY WORK
  ↓
EXECUTE
  ↓
VERIFY
  ↓
REASSESS SUSPENDED WORK
```

A higher-priority condition may preempt when:

```text
higher_priority_score - current_priority_score >= SWITCH_MARGIN
```

or when a defined hard emergency veto applies.

The exact score and margin are AEGIS policy, not donor facts unless separately recovered.

Preemption must not:

- globally clear escrow;
- erase commitment identity;
- advance progression without verification;
- silently consume another commitment's reservation;
- permanently destroy suspended work without cancellation authority.

---

# 8. Resource safety

Resource accounting must distinguish:

```text
GROSS RESOURCE
   − POLICY PROTECTION
   − ACTIVE COMMITMENT RESERVATIONS
   − OTHER GOVERNED HOLDS
   = TRANSACTION-AVAILABLE RESOURCE
```

This is an AEGIS accounting model, not an asserted engine equation.

## 8.1 Reservation ownership

Every attributable reservation must identify:

- owner;
- commitment ID;
- resource type;
- amount;
- minimum viable amount;
- creation epoch;
- expiry;
- consumption predicate;
- release predicate.

## 8.2 Prohibited mutations

No system may:

- spend another commitment's protected resource without release/preemption authority;
- release global escrow to solve a local problem;
- treat gross stock as liquid stock;
- count requested-but-unverified production as capability;
- count an unverified trade as acquired resource;
- advance a requirement merely because funds were reserved.

## 8.3 Consumption and reconciliation

Consumption must be attributable to a transaction. Residual reservation must be released or carried forward explicitly. Partial outcomes create reconciliation work; they do not silently become success.

---

# 9. Progression safety

The progression machine is:

```text
WORK_ITEM_CREATED
 → REQUIREMENT_DECLARED
 → RESERVATION_REQUESTED
 → RESERVATION_FUNDED
 → EXECUTION_AUTHORIZED
 → COMMAND_ISSUED
 → POSTCONDITION_OBSERVED
 → WORK_ITEM_CONFIRMED
 → PROGRESS_ADVANCED
 → NEXT_WORK_ITEM
```

The critical invariant is:

```text
COMMAND ACCEPTED ≠ COMPLETION
COMPLETION ≠ CAPABILITY
CAPABILITY ≠ STRATEGIC SUCCESS
```

Only the progression owner may advance `gl-build-progress` or its AEGIS successor. `gl-current-build-item` identifies work; it does not prove completion. `gl-progression-pause` represents progression control and cannot be interpreted as generic authorization.

A failed or unverified command must leave progression at the appropriate pending/unverified state.

---

# 10. Cross-system arbitration matrix

| Boundary | Primary owner | Other system role | Allowed mutation | Verification source | Conflict risk |
|---|---|---|---|---|---|
| S04 Scouting → S03 Targeting | S04 owns observation; S03 owns target state | S04 supplies observations | Observation writer updates observation record; S03 derives target state | Fresh observation + target validity | MEDIUM |
| S05 Food → S06 Labor | S05 owns food-source/continuity requirement; S06 owns labor allocation | S05 requests workers | S06 changes worker assignment | Observed productive food flow | MEDIUM |
| S05 Food → S07 Construction | S07 owns construction transaction | S05 declares infrastructure requirement | S07 owns construction state | Building/pending/operational observation | LOW/MEDIUM |
| S06 Labor → S07 Construction | S06 owns labor assignment; S07 owns builder requirement/transaction | S07 requests builder | S06 assigns worker; S07 tracks builder requirement | Builder assignment + construction observation | MEDIUM |
| S07 Construction → S08 Research | S07 owns infrastructure state | S08 consumes prerequisite availability | S07 mutates construction state only | Verified building capability | LOW |
| S08 Research → S07 Infrastructure | S08 owns research requirement; S07 owns infrastructure | S08 requests prerequisite infrastructure | S07 executes construction | Verified building state | MEDIUM |
| S08 Research → S09 Market | S08 owns technology requirement | S09 services liquidity requirement | S09 executes exchange only | Observed resource delta + research preflight | MEDIUM |
| S07 Construction → S09 Market | S07 owns infrastructure requirement | S09 services liquidity requirement | S09 executes exchange only | Resource delta + construction verification | MEDIUM |
| Production Authority → S09 Market | Production Authority owns capability requirement | S09 services liquidity deficit | S09 may execute authorized exchange | Resource delta + downstream production verification | HIGH |
| S09 Market → S06 Labor | S09 owns exchange transaction | S06 supplies economic productivity state | S09 cannot assign labor | Resource delta; labor verification remains S06 | LOW |
| S06 Economy → S09 Market | S06 owns productive allocation state | S09 consumes surplus/deficit information | S06 writes productivity; S09 writes transaction | Observed resource state | HIGH |
| S02 State Authority → S01–S09 | State owner is domain-specific | S02 owns registry/authority contract, not every domain value | S02 governs namespace; domain owners mutate values | Domain-specific verifier | HIGH |
| S01 Configuration → S02 State | S01 owns configuration | S02 classifies runtime state | Configuration initialization only | Load/definition qualification | MEDIUM |
| Any executor → strategic state | Strategic owner | Executor reports result | No direct strategic objective mutation | Strategic reassessment | CRITICAL if violated |

**Interpretation:** System 02 is the authority/namespace governance layer, not a second strategic brain. Domain systems retain ownership of their semantic state.

---

# 11. Canonical ownership boundaries

| State class | Canonical owner |
|---|---|
| Environment/configuration | S01 |
| Shared state registry/authority metadata | S02 |
| Target state | S03 |
| Observation/scouting state | S04 |
| Food-source/food-continuity state | S05 |
| Worker/labor allocation state | S06 |
| Construction/infrastructure state | S07 |
| Research/technology transaction state | S08 |
| Market/resource-exchange transaction state | S09 |
| Strategic objective | AEGIS strategic layer; outside Shadow systems |
| Production composition authority | AEGIS/Production Authority; outside Shadow systems |

These are architectural ownership assignments, not claims that the historical donor already implements them this cleanly.

---

# 12. Verification authority

Verification must remain close to the physical consequence being verified.

| Result | Verification authority |
|---|---|
| Scout movement | S04, with observation evidence for information success |
| Observation freshness | S04 |
| Target validity | S03 using observation evidence |
| Food productivity | S05 using observed resource flow |
| Worker productivity | S06 |
| Building completion | S07 using building/pending/world-state evidence |
| Research completion | S08 using research/technology state |
| Market transaction | S09 using observed economic deltas |
| Production capability | Production/AEGIS authority using verified unit/capability evidence |
| Strategic effect | AEGIS strategic layer; never inferred solely by executor |

A verifier must not certify a state merely because the executor reported success.

---

# 13. Conflict-resolution algorithm

For any contested mutation:

```text
1. IDENTIFY semantic state.
2. RESOLVE canonical owner.
3. IDENTIFY writer and generation.
4. CHECK writer authorization.
5. CHECK generation against current state.
6. CHECK validity and lifetime.
7. CHECK preconditions.
8. CHECK competing commitment/transaction.
9. APPLY precedence/preemption policy.
10. MUTATE only through authorized path.
11. OBSERVE expected postcondition.
12. VERIFY.
13. RECONCILE resources/progression.
14. PUBLISH result.
15. REASSESS downstream requirements.
```

If any required step cannot be represented or qualified in `.per`, the implementation is not yet proven safe.

---

# 14. Deadlock and starvation controls

Shared authority must expose at least:

- oldest active commitment age;
- oldest transaction age;
- reservation age;
- resource starvation age;
- production starvation age;
- worker starvation/idle cause;
- infrastructure starvation;
- strategic commitment starvation;
- escrow concentration;
- blocked prerequisite count;
- repeated failed transaction count;
- repeated unverified completion count.

These are telemetry/control candidates. They become authoritative only when explicitly designated as such.

A system must not hide deadlock by repeatedly reissuing the same command.

---

# 15. Qualification gates

No shared-state implementation is considered qualified until it passes the following gates.

### Q1 — Symbol identity

Every shared symbol has a unique semantic classification and physical channel.

### Q2 — Writer inventory

Every actual writer is recovered statically. Missing evidence is `UNRECOVERED`, not `NONE`.

### Q3 — Reader inventory

Every material reader and downstream dependency is identified.

### Q4 — Ownership

Exactly one canonical semantic owner is assigned, or the conflict is explicitly unresolved.

### Q5 — Mutation path

Every mutation has an authorized transition path.

### Q6 — Precedence

Competing writers have explicit precedence or are prohibited.

### Q7 — Generation

Stale state cannot overwrite current state.

### Q8 — Lifetime

Creation, persistence, reset, expiry, and invalidation are defined.

### Q9 — Resource attribution

Every reservation and consumption path is attributable.

### Q10 — Progression safety

No command path can advance progression without its required postcondition.

### Q11 — Verification

A sufficient world-state or engine-state postcondition is defined for every executor action.

### Q12 — Failure handling

Rejected, failed, partial, unverified, expired, blocked, and preempted outcomes have explicit states.

### Q13 — Bypass audit

All legacy/ordinary executor paths are classified as authorized, low-cost unreserved, emergency, quarantined, or unauthorized.

### Q14 — Runtime ABI qualification

Engine-specific state and commands are qualified against the target AoE2DE build before being treated as runtime facts.

### Q15 — Integrated vertical slice

At least one cross-system path demonstrates:

```text
REQUIREMENT
 → COMMITMENT
 → RESOURCE CONTROL
 → EXECUTOR
 → COMMAND
 → OBSERVATION
 → VERIFICATION
 → RECONCILIATION
 → REASSESSMENT
```

### Q16 — Adversarial review

A separate review must attempt to demonstrate:

- duplicate authority;
- stale mutation;
- double reservation;
- hidden bypass;
- progression race;
- verification false positive;
- resource leakage;
- starvation/deadlock.

Failure of any critical invariant blocks promotion.

---

# 16. Implementation rules for Muse

Muse must not interpret this specification as permission to create nine autonomous subsystems with shared writable goals.

Implementation order should be:

```text
STATE REGISTRY
  ↓
OWNER / WRITER-READER GRAPH
  ↓
AUTHORITY / GENERATION CONTRACT
  ↓
MUTATION PATHS
  ↓
RESOURCE / COMMITMENT INTERFACES
  ↓
VERIFICATION INTERFACES
  ↓
ONE VERTICAL SLICE
  ↓
STATIC AUDIT
  ↓
RUNTIME QUALIFICATION
  ↓
EXPANSION
```

Do not implement broad strategic behavior while shared-state ownership remains ambiguous.

Do not solve an authority conflict by adding another goal merely to preserve both writers. First determine whether the states are genuinely distinct. If they are, split them semantically. If they are not, establish one owner.

Do not use `up-jump-rule` as a substitute for ownership. A jump can suppress execution; it does not establish who owns the suppressed state.

Do not use a timer as a substitute for expiry semantics. A timer is only a temporal mechanism until its state transition is defined.

Do not use telemetry as control merely because it is convenient to read.

---

# 17. Hard invariants

**AR-01 — Single semantic owner.** Every mutable shared state has one canonical owner.

**AR-02 — Authorized mutation.** Only the owner or explicitly delegated mutation path may change authoritative state.

**AR-03 — Reader non-interference.** Reading shared state does not confer mutation authority.

**AR-04 — Generation monotonicity.** Stale generations cannot overwrite newer state.

**AR-05 — Command/completion separation.** Command acceptance is never completion proof.

**AR-06 — Verification separation.** Executor acknowledgement is not independent verification.

**AR-07 — Resource attribution.** Reservation, consumption, release, and return are attributable.

**AR-08 — No global reset.** Local failure cannot destroy unrelated commitments or reservations.

**AR-09 — Progression verification.** Progress advances only after sufficient postcondition evidence.

**AR-10 — Strategic containment.** Shadow executors and economic subsystems do not originate strategic objectives.

**AR-11 — Explicit preemption.** Preemption is an authority transition with reconciliation.

**AR-12 — Bypass visibility.** Every bypass path is classified and auditable.

**AR-13 — Lifetime visibility.** Shared state cannot persist indefinitely without an explicit lifetime policy.

**AR-14 — Failure visibility.** Repeated failure must become observable state, not infinite retry.

**AR-15 — Evidence discipline.** Static existence, command acceptance, world-state mutation, capability, and strategic effect remain separate evidence levels.

**AR-16 — Runtime humility.** Unqualified engine semantics remain UNCERTAIN.

---

# 18. Definition of done

This specification is operationally satisfied only when the implementation can answer, for every shared state:

1. What exactly does it mean?
2. What physical channel carries it?
3. Who owns it?
4. Who writes it?
5. Who reads it?
6. Who is forbidden to write it?
7. What mutation transitions are legal?
8. What preconditions apply?
9. What generation does it belong to?
10. What is its lifetime?
11. What expires it?
12. What invalidates it?
13. What higher-priority state can preempt it?
14. What resource reservations depend on it?
15. What transactions depend on it?
16. What executor consumes it?
17. What world-state observation verifies it?
18. What happens on rejection?
19. What happens on partial completion?
20. What happens on unverified completion?
21. What happens on stale generation?
22. What happens on cancellation?
23. What happens on preemption?
24. What happens on deadlock?
25. What happens on starvation?
26. Which legacy paths can bypass it?
27. Which `up-jump-rule` paths suppress it?
28. Which timers guard it?
29. Which other systems depend on it?
30. What evidence supports each claim?

Any unanswered item remains an implementation or qualification gap.

---

# 19. Final engineering directive

The purpose of the Shadow architecture is not to make every subsystem autonomous. It is to make **economic and execution mechanisms composable under explicit AEGIS authority**.

The correct architecture is therefore:

```text
AEGIS STRATEGIC AUTHORITY
          ↓
     REQUIREMENT
          ↓
     COMMITMENT
          ↓
   RESOURCE CONTROL
          ↓
   SYSTEM AUTHORITY
          ↓
      EXECUTOR
          ↓
       COMMAND
          ↓
     WORLD STATE
          ↓
    OBSERVATION
          ↓
    VERIFICATION
          ↓
   RECONCILIATION
          ↓
     REASSESSMENT
```

The shared namespace must implement that chain rather than bypass it.

**Do not optimize the number of rules. Optimize the integrity of authority, state ownership, resource accounting, verification, and recovery.**

Until those properties are demonstrable, additional strategic sophistication is architectural debt rather than capability.