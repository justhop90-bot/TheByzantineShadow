# The Byzantine Shadow — Blueprint v0.2

## 0. Revision Status

This revision incorporates a direct forensic pass over the supplied `Shadow DC7(1).per` donor. It corrects an important v0.1 attribution error: `sn-resource-control` is a historical stock/Promisory mechanism, not a mechanism actually present in this Shadow donor. It remains a possible external donor for a future economic actuator, but is no longer classified as a Shadow KEEP item.

The donor is best understood not as a generic escrow library, but as a tightly coupled economic transaction/progression scheduler whose state is carried through goals, progression markers, escrow state, global escrow percentages, affordability predicates, and `up-*` transactional commands.

The architectural objective remains: extract the donor's useful economic discipline, remove accidental coupling, formalize its implicit state machine, and connect it to AEGIS without allowing the economic substrate to become a second strategic brain.

---

## 1. Direct Donor Findings

### 1.1 Shadow has a real escrow-control state carrier

The donor defines `gl-escrow-state` and passes it directly into transactional primitives such as `up-build`, `up-research`, `up-train`, and their escrow-aware preflight forms. The state is explicitly switched between `with-escrow` and `without-escrow`.

This is more important than the raw escrow percentage constants: Shadow treats escrow participation as a transaction-mode decision injected into execution.

### 1.2 Shadow uses two different reservation mechanisms

The donor combines:

1. percentage-based global escrow policy through `set-escrow-percentage`; and
2. absolute/transaction-specific escrow modification through `up-modify-escrow`.

These must not be conflated in AEGIS.

Percentage escrow is background economic policy. `up-modify-escrow` is much closer to a discrete reservation request. The target architecture preserves that distinction.

### 1.3 Shadow contains an implicit progression transaction machine

The recurring pattern is:

`STRATEGY / CONDITION → gl-current-build-item → gl-progression-pause → escrow preparation → can-X-with-escrow → up-X → observed completion → gl-build-progress advance → next item`.

`gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause` therefore form an implicit transaction scheduler. They are not miscellaneous goals.

This is the donor's most strategically valuable economic mechanism after escrow itself.

### 1.4 Shadow uses completion observation to advance progression

For construction, Shadow generally does not advance progression immediately after issuing `up-build`; it waits for an observed building count to reach the expected level, then increments `gl-build-progress`.

For research, it commonly waits for research status to reach the expected pending/completed state before advancing progression.

This is a primitive form of post-command verification and must be extracted separately from command issuance.

### 1.5 Shadow deliberately releases irrelevant resource escrow

Many progression rules set selected resource escrow percentages while explicitly zeroing and releasing other resources. This is an economic reallocation policy: the current progression item is allowed to dominate selected resource protection while unrelated reservations are relaxed.

AEGIS should preserve the mechanism but replace implicit global side effects with attributable commitment ownership.

### 1.6 Shadow has four principal percentage levels

The donor defines:

- `LOW-ESCROW = 25`
- `MID-ESCROW = 35`
- `MID-HIGH-ESCROW = 40`
- `HIGH-ESCROW = 60`

These are donor policy parameters, not engine constants and not universal AEGIS truths. They become named tunable policy coefficients in the new registry.

### 1.7 Shadow has mixed production governance

The donor does not uniformly route every unit through escrow-aware training. Some rules use ordinary `can-train` / `train`, while others use `up-can-train gl-escrow-state` / `up-train gl-escrow-state`.

Therefore escrow-aware training cannot be treated as proof that all production is governed by Shadow. Every production path must be classified as escrow-governed, ordinary/unreserved, emergency bypass, legacy, or unauthorized.

### 1.8 Shadow uses escrow-aware construction broadly

The donor uses `can-build-with-escrow` and `up-build` with `gl-escrow-state` across substantial infrastructure logic, including stables, monasteries, markets, siege workshops, barracks, farms, houses, camps, and universities.

Construction therefore belongs inside the Shadow economic architecture rather than being treated as a production afterthought.

### 1.9 Shadow uses jump/order arbitration

`up-jump-rule` is repeatedly used to suppress lower-priority production or research branches when economic or strategic conditions indicate another branch should be considered first.

This is procedural arbitration. AEGIS must expose that priority explicitly rather than hiding it in branch order.

### 1.10 Shadow contains a substantial legacy namespace

The donor contains approximately 1,500 distinct `defconst` names and duplicate names. Some duplicates are legitimate conditional definitions; others are suspicious semantic duplicates.

Observed duplicate classes include map-conditional constants, repeated state enumerations, and suspicious repeated constants such as `home-x`, `home-y`, `gl-position`, and multiple firing-threshold definitions.

The donor is therefore not namespace-safe as a direct source of truth. Its mechanisms must be extracted into a clean ABI.

---

## 2. Corrected Donor Classification

| Donor mechanism | v0.2 classification | AEGIS treatment |
|---|---|---|
| `gl-escrow-state` transaction mode | KEEP / FORMALIZE | Canonical escrow transaction-mode carrier |
| `set-escrow-percentage` | KEEP / CONSTRAIN | Background resource-protection policy |
| `up-modify-escrow` | KEEP / FORMALIZE | Attributable reservation primitive |
| `release-escrow` | KEEP / CONSTRAIN | Owner-aware release |
| `can-*-with-escrow` | KEEP | Feasibility gate |
| `up-can-*` with escrow state | KEEP | Transaction preflight |
| `up-build` / `up-research` / `up-train` with escrow state | KEEP AS EXECUTION INTERFACE | Never becomes strategic authority |
| `gl-current-build-item` | KEEP / REFACTOR | Transaction work-item identity |
| `gl-build-progress` | KEEP / REFACTOR | Progress ledger / completion cursor |
| `gl-progression-pause` | KEEP / REFACTOR | Pending economic/production commitment state |
| ordinary `train/research/build` paths | AUDIT / CLASSIFY | Explicit bypass registry |
| `up-jump-rule` arbitration | EXTRACT / EXPLICITATE | Priority/preemption semantics |
| rule-order priority | EXTRACT / EXPLICITATE | Authority precedence table |
| donor percentage values 25/35/40/60 | ADAPT | Tunable coefficients only |
| donor constants wholesale | REPLACE | New namespace registry |
| donor duplicate definitions | QUARANTINE | No direct transplant |
| historical `sn-resource-control` | NOT A SHADOW MECHANISM | Optional external donor only |

---

## 3. Revised System Model

The Shadow should be modeled as five coupled but separable machines.

### Machine A — Economic Policy

`resource state → policy mode → escrow percentages → free-resource envelope`.

This machine must never directly choose a strategic objective.

### Machine B — Commitment Machine

`candidate → preparing → committed → funded → executing → verified → retiring → retired`.

Exceptional exits: `cancelled / expired / invalidated / preempted / failed / blocked / deadlocked`.

### Machine C — Transaction Machine

`requested → reserving → reserved → preflight → authorized → issued → observing → confirmed`.

Failure states: `rejected / failed / partial / unverified / expired / released`.

### Machine D — Progression Machine

`work-item → requirement → funding → execution → observed completion → progress++ → next work-item`.

This formally replaces the donor's implicit `gl-current-build-item + gl-build-progress + gl-progression-pause` machine.

### Machine E — Verification Machine

`command accepted → engine state mutation → expected postcondition → verified outcome`.

No upstream system may treat the first event as equivalent to the last.

---

## 4. Policy Escrow vs Commitment Escrow

This distinction is mandatory.

### Policy Escrow

Percentage-based protection such as 25%, 35%, 40%, or 60%.

Purpose:
- preserve liquidity;
- maintain background economic priorities;
- protect future affordability;
- bias resource allocation.

Policy escrow does not identify a specific strategic owner.

### Commitment Escrow

An explicitly attributable reservation for a particular requirement.

Record:
- commitment ID;
- resource;
- amount;
- priority;
- creation epoch;
- expiry epoch;
- purpose;
- minimum viable amount;
- release predicate;
- consumption predicate.

### Transaction Escrow

A short-lived amount released specifically to permit the next executor transaction.

Lifecycle:

`reserved → transaction-authorized → released-to-executor → consumed-or-returned`.

Transaction escrow must never silently become permanent commitment escrow.

---

## 5. Commitment Ownership Contract

Every resource reservation must answer:

1. Who requested it?
2. Which strategic objective created the requirement?
3. Which commitment owns it?
4. Which resource is protected?
5. How much is reserved?
6. What is the minimum viable reservation?
7. What operation may consume it?
8. When does it expire?
9. What observed event proves consumption?
10. What event releases the remainder?
11. Which higher-priority commitment may preempt it?
12. What happens if the executor never consumes it?

If these answers do not exist, the reservation is not a fully governed AEGIS commitment.

---

## 6. Progression Contract

The donor's progression machinery becomes an explicit reusable interface:

`WORK_ITEM_CREATED`
→ `REQUIREMENT_DECLARED`
→ `RESERVATION_REQUESTED`
→ `RESERVATION_FUNDED`
→ `EXECUTION_AUTHORIZED`
→ `COMMAND_ISSUED`
→ `POSTCONDITION_OBSERVED`
→ `WORK_ITEM_CONFIRMED`
→ `PROGRESS_ADVANCED`
→ `NEXT_WORK_ITEM`.

If the expected postcondition is absent:

`COMMAND_ISSUED → UNVERIFIED`, not `PROGRESS_ADVANCED`.

If the observed result is smaller than required:

`PARTIAL → RECONCILE → REMAINING_REQUIREMENT → REPLAN`.

This turns Shadow's existing progression discipline into a general transaction framework for production, research, and construction.

---

## 7. Resource Arbitration

Arbitration must distinguish four quantities:

`gross resources`
`policy escrow`
`commitment escrow`
`transaction-available resources`.

Conceptually:

`transaction_available = gross - policy_protection - active_commitment_reservations`.

The exact engine semantics of this equation must be qualified before being implemented as an engine-level claim. It is the AEGIS accounting model, not an assumed statement about hidden engine internals.

A commitment is not funded merely because `can-X-with-escrow` returns true. Funding requires the reservation ledger to agree with the economic state.

---

## 8. Production Contract

`THREAT / OBJECTIVE`
→ `CAPABILITY REQUIREMENT`
→ `COMPOSITION TARGET`
→ `TRUE DEFICIT`
→ `RESOURCE REQUIREMENT`
→ `COMMITMENT`
→ `FUNDING`
→ `PRODUCTION AUTHORITY`
→ `AIByzBuild`
→ `COMMAND`
→ `OBSERVED QUEUE / UNIT MUTATION`
→ `VERIFICATION`
→ `RESERVATION CONSUMPTION`
→ `REASSESSMENT`.

`TRUE DEFICIT` means:

`Demand − CurrentVerifiedCapability − VerifiedCommittedCapability`.

Requested-but-unverified production is not capability.

---

## 9. Construction Contract

`Need infrastructure`
→ `requirement`
→ `commitment`
→ `wood/stone reservation`
→ `can-build-with-escrow`
→ `up-build`
→ `pending object`
→ `building observation`
→ `verified building`
→ `consume reservation`
→ `remaining deficit`.

Placement is its own verification layer. A valid build command does not establish that a building exists.

---

## 10. Research Contract

`TECH REQUIREMENT`
→ `COMMITMENT`
→ `RESOURCE RESERVATION`
→ `can-research-with-escrow`
→ `up-research`
→ `research status observation`
→ `VERIFIED`
→ `release residual escrow`
→ `REASSESS`.

Research prerequisites may themselves create commitment dependencies. The registry must represent these dependency edges rather than treating technologies as isolated transactions.

---

## 11. Bypass Governance

Every ordinary `train`, `research`, or `build` path that bypasses Shadow transaction state must be classified.

Allowed classifications:

- `MANDATORY_CORE`
- `EMERGENCY_BYPASS`
- `LOW_COST_UNRESERVED`
- `LEGACY_QUARANTINED`
- `DUPLICATE_EXECUTOR`
- `UNAUTHORIZED`

Only the first three may survive into the final architecture, and `EMERGENCY_BYPASS` must be explicitly bounded.

This prevents the classic failure mode in which an escrow architecture appears to govern production while legacy rules silently continue spending resources outside it.

---

## 12. Preemption Model

The donor's jump-based priority behavior becomes explicit preemption.

A commitment may be preempted when:

`higher_priority_score - current_score >= SWITCH_MARGIN`

or when a hard emergency veto fires.

Preemption sequence:

`ACTIVE`
→ `SUSPEND`
→ `freeze new funding`
→ `release attributable excess escrow`
→ `restore economic policy`
→ `fund emergency`
→ `execute emergency`
→ `verify`
→ `reconsider suspended commitment`.

Preemption must not erase historical state. The suspended commitment remains a known object with an explicit reason.

---

## 13. Hysteresis Must Apply to Money

Every reversible commitment should have:

- activation threshold;
- maintain threshold;
- release threshold;
- preemption threshold;
- minimum dwell time;
- minimum viable reservation;
- maximum reservation age.

This prevents oscillation such as `reserve → release → reserve → release` caused by small resource fluctuations around an affordability boundary.

---

## 14. Starvation and Deadlock

Starvation must be measured against opportunity cost, not merely absolute resource balance.

Track:

- resource starvation age;
- production starvation age;
- villager starvation;
- infrastructure starvation;
- strategic commitment starvation;
- escrow concentration;
- oldest active reservation;
- percentage of gross resource capacity unavailable to general economy.

A commitment that remains funded but cannot make progress is a candidate for `DEADLOCKED`, not indefinite `ACTIVE` status.

---

## 15. Verification Model

Verification must be action-specific.

### Train

Possible postconditions:
- production queue changed;
- unit count increased;
- resource delta occurred;
- expected unit became observable.

### Research

Possible postconditions:
- research status changed;
- technology completed;
- prerequisite state changed.

### Build

Possible postconditions:
- pending object created;
- placement occurred;
- building count increased;
- building became operational.

The verifier must declare which postcondition is sufficient for the relevant commitment. Acknowledgement alone is never sufficient.

---

## 16. State Taxonomy

### Commitment
`CANDIDATE / PREPARING / COMMITTED / FUNDED / EXECUTING / SUSPENDED / VERIFIED / RETIRING / RETIRED / CANCELLED / EXPIRED / INVALIDATED / PREEMPTED / FAILED / BLOCKED / DEADLOCKED`

### Transaction
`REQUESTED / RESERVING / RESERVED / PREFLIGHT / AUTHORIZED / ISSUED / OBSERVING / CONFIRMED / PARTIAL / REJECTED / FAILED / UNVERIFIED / RELEASED / EXPIRED`

### Verification
`NOT_STARTED / PENDING / PASS / PARTIAL / FAIL / UNKNOWN`

Do not collapse these dimensions into a single goal.

---

## 17. Revised Module Map

### 00_bs_constants.per
Canonical ABI and namespace registry.

### 01_bs_state.per
Economic state kernel.

### 02_bs_policy_escrow.per
Percentage-based background escrow policy.

### 03_bs_commitment_escrow.per
Attributable reservation ledger.

### 04_bs_transaction_escrow.per
Short-lived transaction funding.

### 05_bs_commitment.per
Commitment lifecycle and ownership.

### 06_bs_progression.per
Formal replacement for `gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause`.

### 07_bs_arbitration.per
Explicit replacement for hidden rule-order / `up-jump-rule` priority.

### 08_bs_hysteresis.per
Activation, maintain, release, switch and dwell thresholds.

### 09_bs_preemption.per
Emergency and higher-priority takeover.

### 10_bs_cancellation.per
Owner-aware cancellation and release.

### 11_bs_expiry.per
Lease and reservation expiry.

### 12_bs_starvation.per
Economic survival and deadlock detection.

### 13_bs_transaction.per
General transaction coordinator.

### 14_bs_verification.per
Independent postcondition verification.

### 15_bs_production_bridge.per
Composition → resource requirement → Production Authority.

### 16_bs_construction_bridge.per
Infrastructure requirements → funding → AIByzBuild construction.

### 17_bs_research_bridge.per
Technology requirements → funding → research executor.

### 18_bs_byzantine_policy_bridge.per
Civilization-specific doctrine supplied by AEGIS/Byzantine policy.

### 19_bs_bypass_registry.per
Every non-Shadow production/research/build path classified and governed.

### 20_bs_telemetry.per
Decision, reservation, transaction and verification observability.

---

## 18. Symbol Registry Requirements

The next registry must be mechanical, not prose-derived.

For every relevant Shadow symbol record:

`SYMBOL`
`KIND`
`VALUE / SCALE`
`DEFINITION LINE`
`CONDITIONAL CONTEXT`
`WRITERS`
`READERS`
`TRANSACTION CONSUMERS`
`ESCROW EFFECT`
`PRECEDENCE`
`RESET`
`EXPIRY`
`COMPLETION PREDICATE`
`FAILURE PREDICATE`
`BYPASS PATH`
`SIDE EFFECTS`
`DONOR PURPOSE`
`TARGET PURPOSE`
`EVIDENCE CLASS`
`STATUS`
`CONFLICT GENERATION`
`CANONICAL OWNER`
`MIGRATION ACTION`.

The registry must distinguish `DONOR SEMANTIC STATE`, `ENGINE PRIMITIVE`, `AEGIS POLICY`, and `AEGIS-GENERALIZATION`.

---

## 19. Static Qualification Requirements

The Shadow qualification suite must report:

- escrow-state writers = 1 canonical owner;
- escrow-state readers classified;
- every `set-escrow-percentage` attributed to policy owner;
- every `up-modify-escrow` attributed to commitment owner;
- every `release-escrow` attributed to a release cause;
- every escrow-aware `up-*` mapped to a transaction;
- every ordinary `train/research/build` bypass classified;
- every progression counter writer classified;
- every progression counter increment linked to a completion predicate;
- every jump-based arbitration path translated to explicit precedence;
- duplicate constants classified as conditional, intentional, conflict, or obsolete;
- no dead reservation without expiry/release path;
- no lock without consumer;
- no ACK-without-verification;
- no verified capability based solely on requested action.

P0 failures:

`UNRESOLVED SYMBOL`
`UNAUTHORIZED ESCROW WRITER`
`UNCLASSIFIED BYPASS`
`UNVERIFIED COMPLETION`
`ORPHAN RESERVATION`
`DUPLICATE EXECUTOR`
`UNDECLARED PREEMPTION`
`DEADLOCKED COMMITMENT WITHOUT RECOVERY`.

---

## 20. Evidence Doctrine

The donor demonstrates mechanisms; it does not demonstrate that those mechanisms are optimal for AEGIS.

### DIRECT
Observed directly in Shadow source.

### COMPOSED
Semantics obtained by tracing multiple Shadow rules together.

### INFERRED
Behavior inferred from repeated source patterns but not demonstrated by runtime observation.

### AEGIS-GENERALIZATION
A new abstraction intentionally derived from the donor but not present in the donor as such.

### UNCERTAIN
Engine semantics, hidden ordering, or effects that remain unresolved.

A donor mechanism must never be promoted from DIRECT to confirmed engine semantics without engine evidence.

---

## 21. What Shadow Actually Contributes to AEGIS

The high-value transplant is now defined precisely:

1. economic reservation discipline;
2. resource-protection policy;
3. escrow-aware feasibility;
4. transaction-mode injection into build/research/train;
5. multi-step progression sequencing;
6. post-command progression checks;
7. economic arbitration through priority/order;
8. resource reallocation when strategic work changes;
9. construction/research/production economic unification;
10. a donor pattern for separating `can afford` from `execute`.

Shadow does not contribute a complete strategic planner, threat classifier, battlefield optimizer, or universal commitment ledger. Those remain AEGIS responsibilities.

---

## 22. Escrow Byzantine King Architecture

The final organism is:

`AEGIS Strategic Cognition`
↓
`Byzantine Doctrine`
↓
`Capability / Composition Requirements`
↓
`Economic Commitment Arbiter`
↓
`Policy Escrow + Commitment Escrow`
↓
`Transaction Coordinator`
↓
`Production / Construction / Research Authority`
↓
`AIByzBuild Executor`
↓
`Observed Engine Mutation`
↓
`Verification`
↓
`Updated Capability State`
↓
`AEGIS Reassessment`.

The economic king is not created by adding more escrow calls. It is created when every consequential resource commitment has ownership, funding semantics, temporal validity, execution authority, verification, and a controlled path back into strategic reassessment.

---

## 23. Immediate Next Artifact

Build:

`docs/THEBYZANTINESHADOW_SYSTEM_REGISTRY_v0.1.md`

The registry should be generated from the actual donor, not manually authored from this blueprint.

Minimum first-pass coverage:

1. all `defconst` symbols;
2. all goal writers/readers;
3. all escrow writers/readers;
4. all `gl-escrow-state` consumers;
5. all `gl-current-build-item` writers/readers;
6. all `gl-build-progress` writers/readers;
7. all `gl-progression-pause` writers/readers;
8. every `can-*-with-escrow` path;
9. every escrow-aware `up-build`, `up-research`, and `up-train` path;
10. every ordinary bypass path;
11. every `up-jump-rule` arbitration path;
12. every observed completion predicate;
13. duplicate-constant classification;
14. rule/load order;
15. donor-to-AEGIS migration disposition.

Only after that registry exists should individual Shadow modules be implemented.

The registry becomes the authoritative bridge from forensic donor → economic ABI → AEGIS integration.

---

## 24. Final Doctrine

**Extract mechanisms, not mythology.**

**Preserve proven economic discipline, not accidental coupling.**

**Make implicit state explicit.**

**Make every reservation attributable.**

**Make every bypass visible.**

**Make every completion observable.**

**Make every preemption reversible.**

**Make every failure diagnosable.**

**Make every strategic claim earn its evidence.**

The Byzantine Shadow becomes the economic nervous system of AEGIS only when the donor's implicit economic machine has been reconstructed as a formally owned, bounded, observable, verifiable control substrate.
