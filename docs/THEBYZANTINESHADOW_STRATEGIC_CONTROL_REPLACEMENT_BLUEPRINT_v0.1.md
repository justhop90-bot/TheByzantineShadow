# The Byzantine Shadow — Strategic Control Replacement Blueprint v0.1

## 0. Executive Thesis

The Byzantine Shadow donor should **not** be treated as an obsolete AI to be rewritten wholesale. Forensic examination indicates that its most valuable architecture lies below the strategic-decision boundary: escrow control, resource protection, transaction sequencing, affordability gating, progression state, execution interfaces, and post-command completion observation form a coherent economic transaction/progression substrate.

The highest-leverage strategic intervention is therefore a **surgical replacement of Shadow's implicit strategic priority controller**, not replacement of its economic machinery.

The target transformation is:

`OBSERVATION / CONDITION → implicit Shadow priority → work item / jump ordering → economic commitment`

into:

`OBSERVATION → BELIEF → THREAT / OPPORTUNITY → OBJECTIVE → REQUIRED CAPABILITY → CANDIDATE SOLUTIONS → PRIORITY → COMMITMENT → Shadow economic substrate`

The objective is not to make Shadow resemble AEGIS. The objective is to make Shadow's existing economic machinery answer to a more explicit, inspectable, capability-oriented strategic control plane.

---

## 1. Scope

This blueprint concerns the strategic-control boundary of the Shadow donor and its integration with AEGIS.

It does **not** authorize:

- wholesale deletion of the Shadow donor;
- wholesale transplantation of AEGIS into Shadow;
- replacement of escrow merely because it is architecturally unfamiliar;
- replacement of production, construction, or research mechanics without functional qualification;
- treating static control evidence as proof of runtime strategic success;
- assuming that an apparently simple `.per` rule is strategically simple without tracing its state, ordering, side effects, and retry behavior.

All conclusions remain subject to the project's evidence taxonomy: DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, and UNCERTAIN, with appropriate status qualifiers.

---

## 2. Forensic Basis

The supplied Shadow donor contains a substantial economic transaction/progression mechanism. The forensic pass identified, among other mechanisms:

- `gl-escrow-state` as an explicit transaction-mode carrier;
- percentage-based escrow policy through `set-escrow-percentage`;
- discrete escrow manipulation through `up-modify-escrow`;
- escrow release operations;
- escrow-aware affordability/preflight predicates;
- escrow-aware `up-build`, `up-research`, and `up-train` execution paths;
- `gl-current-build-item` as work-item identity;
- `gl-build-progress` as progression state;
- `gl-progression-pause` as suspension/pending state;
- observed completion before progression advancement in important construction and research paths;
- `up-jump-rule` and rule ordering as procedural arbitration mechanisms;
- mixed ordinary and escrow-aware production paths;
- substantial infrastructure construction governance;
- a large and partially legacy namespace containing duplicate or conditional definitions.

These findings imply that Shadow is better characterized as a **coupled economic transaction and progression scheduler** than as a simple resource-saving script.

A critical attribution correction is retained from the Shadow Blueprint v0.2: historical `sn-resource-control` belongs to the stock/Promisory corpus and is **not** established as a mechanism present in the Shadow donor. It must not be described as Shadow architecture without new evidence.

---

## 3. Strategic Diagnosis

### 3.1 Primary weakness

The principal strategic weakness is not the absence of economic control. It is the opacity of the mechanism that determines **what deserves economic control next**.

Shadow encodes priority through combinations of:

- rule ordering;
- `up-jump-rule` behavior;
- current work-item state;
- progression markers;
- pauses;
- resource protection policy;
- affordability constraints;
- transaction side effects;
- completion feedback;
- repeated rule evaluation.

This can produce sophisticated emergent behavior, but strategic intent is not represented as a first-class object.

### 3.2 Consequence

The same economic substrate can therefore be difficult to answer in strategic terms:

- What problem is the AI responding to?
- What does it believe is happening?
- What capability does it require?
- Why is that capability more urgent than another?
- Which alternative solutions were available?
- Why was this resource commitment chosen?
- What evidence would invalidate the commitment?
- What event makes the commitment complete?
- What happens if the chosen solution becomes infeasible?

These questions should become explicit control-plane concerns without destroying the donor's existing transaction machinery.

---

## 4. Core Architectural Principle

### Preserve the economic substrate; replace the strategic authority boundary.

Shadow should retain responsibility for mechanisms it already performs well:

`RESOURCE STATE → RESERVATION → AFFORDABILITY → TRANSACTION → EXECUTION → OBSERVATION`

AEGIS should increasingly own:

`OBSERVATION → BELIEF → THREAT / OPPORTUNITY → OBJECTIVE → CAPABILITY → PRIORITY → COMMITMENT`

Production Authority remains the authorization layer between strategic commitment and the existing production executor.

AIByzBuild remains the execution layer.

Verification remains a separate epistemic layer.

The combined architecture is therefore:

`WORLD`
→ `OBSERVATIONS`
→ `BELIEF STATE`
→ `THREAT / OPPORTUNITY MODEL`
→ `OBJECTIVE MODEL`
→ `CAPABILITY REQUIREMENT`
→ `CANDIDATE SOLUTIONS`
→ `STRATEGIC ARBITRATION`
→ `COMMITMENT`
→ `SHADOW ECONOMIC SUBSTRATE`
→ `PRODUCTION / CONSTRUCTION / RESEARCH AUTHORITY`
→ `EXECUTOR`
→ `ENGINE`
→ `VERIFICATION`
→ `BELIEF UPDATE`
→ `REASSESSMENT`

---

## 5. What Must Be Preserved

### 5.1 Escrow

Preserve Shadow's escrow machinery as a core economic primitive.

Do not equate escrow with strategy. Escrow is the enforcement mechanism for a reservation or transaction, not the reason for the reservation.

Distinguish:

1. **Policy escrow** — percentage-based background resource protection.
2. **Commitment escrow** — attributable reservation associated with a strategic requirement.
3. **Transaction escrow** — short-lived funding used to authorize a specific executor transaction.

### 5.2 Saving

Preserve the donor's resource-saving machinery where it can be shown to protect economically meaningful commitments.

The strategic layer should determine the reason and priority for saving; the economic layer should enforce the resulting protection.

### 5.3 Affordability and escrow-aware preflight

Preserve `can-*-with-escrow` and related `up-*` preflight interfaces as feasibility gates.

A successful affordability predicate is evidence of **feasibility**, not evidence of strategic correctness or execution completion.

### 5.4 Transaction interfaces

Preserve the donor's useful execution sequence around:

- `up-build`;
- `up-research`;
- `up-train`;
- escrow-state selection;
- preflight;
- resource release;
- observed completion.

These become reusable transaction interfaces rather than strategic authorities.

### 5.5 Progression state

Preserve the conceptual machinery represented by:

- `gl-current-build-item`;
- `gl-build-progress`;
- `gl-progression-pause`.

Do not preserve their existing semantics blindly. Generalize them into a formal work/commitment progression interface.

### 5.6 Completion observation

Preserve the donor's strongest verification behavior: where it waits for observed state before advancing progression, retain that separation.

This becomes a central AEGIS rule:

**COMMAND ISSUED ≠ STATE MUTATED ≠ OUTCOME VERIFIED.**

---

## 6. What Should Be Replaced

The replacement target is **strategic authority**, not economic execution.

### 6.1 Implicit strategic priority

Replace the use of physical rule ordering as the sole or dominant representation of strategic priority.

Rule order remains an implementation mechanism, but strategic precedence should be represented explicitly in a control structure that can be inspected and audited.

### 6.2 Hidden jump arbitration

`up-jump-rule` may remain as an execution primitive where required by `.per`, but it should no longer be the sole semantic representation of strategic priority.

Its strategic effect must be extracted into an explicit authority/preemption model.

### 6.3 Situation-to-action coupling

Replace strategic patterns of the form:

`condition → specific action`

with:

`observation → belief → requirement → candidate solution → strategic selection → authorized action`.

The final executor can still perform a specific action. The strategic layer should not unnecessarily hard-code the action as the only representation of the problem.

### 6.4 Unstructured economic priority

Replace direct competition among economic branches with explicit capital-allocation semantics where the existing system's behavior proves insufficiently inspectable or strategically expressive.

The objective is not centralization for its own sake. Distributed mechanisms that produce good behavior should be preserved when their semantics can be demonstrated.

---

## 7. Capability-Centered Strategic Model

The new strategic control plane should reason in terms of **capabilities**, not merely units or buildings.

Example:

`ENEMY CAVALRY OBSERVED`

should produce a requirement such as:

`ANTI-CAVALRY CAPABILITY REQUIRED`

rather than immediately producing:

`BUILD CAMELS`.

Candidate solutions may include:

- counter-unit production;
- fortification;
- mobility;
- denial;
- relocation;
- retreat;
- counterattack;
- siege;
- technology;
- delay;
- combinations of the above.

The strategic arbiter selects among feasible candidates using explicit state rather than assuming that one unit is synonymous with the solution.

---

## 8. Strategic Commitment Object

A strategic requirement should become a first-class commitment before it becomes a resource reservation.

Minimum conceptual fields:

- commitment identifier;
- originating observation or belief;
- objective;
- required capability;
- candidate solution;
- priority;
- urgency;
- confidence;
- resource requirement;
- minimum viable amount;
- desired amount;
- current funding;
- verified progress;
- remaining deficit;
- creation epoch;
- expiry condition;
- cancellation condition;
- preemption condition;
- completion condition;
- failure condition;
- strategic reason;
- owning authority.

A commitment is not considered complete because resources were reserved or a command was accepted.

---

## 9. Explicit Arbitration

Strategic arbitration should compare competing requirements before committing scarce resources.

Conceptual candidate dimensions:

- strategic value;
- urgency;
- threat severity;
- confidence;
- feasibility;
- cost;
- opportunity cost;
- reversibility;
- time-to-effect;
- consequence of failure;
- current commitment load;
- capability deficit.

A conceptual scoring model may be used as an analysis aid, but coefficients must not be treated as engine facts until qualified.

The arbiter must answer:

> **Why did this commitment win?**

That question should be answerable from explicit state.

---

## 10. Preemption and Hysteresis

Explicit strategic authority requires controlled switching.

A commitment should not repeatedly alternate between active and inactive merely because resources or observations fluctuate around a boundary.

Each reversible commitment should therefore have, where applicable:

- activation threshold;
- maintenance threshold;
- release threshold;
- preemption threshold;
- minimum dwell time;
- minimum viable commitment;
- maximum reservation age;
- invalidation condition.

Preemption should suspend or retire the commitment according to policy; it should not erase its history.

Conceptual flow:

`ACTIVE`
→ `SUSPEND`
→ `FREEZE NEW FUNDING`
→ `RELEASE ATTRIBUTABLE EXCESS`
→ `FUND HIGHER PRIORITY`
→ `EXECUTE`
→ `VERIFY`
→ `RECONSIDER SUSPENDED COMMITMENT`.

---

## 11. Formalized Shadow Progression Machine

The existing progression mechanism should be generalized to:

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

Failure branches include:

`REJECTED`
`FAILED`
`PARTIAL`
`UNVERIFIED`
`BLOCKED`
`EXPIRED`
`CANCELLED`
`PREEMPTED`
`DEADLOCKED`.

The key invariant is:

**No progress advancement without the appropriate observed postcondition.**

---

## 12. Verification Contract

Verification must be action-specific.

### Training

Potential evidence:

- queue mutation;
- resource mutation;
- unit-count increase;
- expected unit becoming observable.

### Research

Potential evidence:

- research status mutation;
- technology completion;
- prerequisite state mutation.

### Construction

Potential evidence:

- pending object creation;
- valid placement;
- building-count increase;
- operational building state.

The required postcondition must be defined per commitment.

`COMMAND ACCEPTED` is never synonymous with `COMPLETED`.

---

## 13. Integration Boundary

The strategic replacement must stop before the economic executor.

### AEGIS owns

- belief;
- threat/opportunity interpretation;
- objectives;
- capability requirements;
- candidate generation;
- strategic priority;
- commitment selection;
- strategic cancellation/preemption policy.

### Shadow owns

- resource protection;
- escrow mechanics;
- economic saving;
- transaction preparation;
- affordability interaction;
- progression execution support;
- resource release mechanics.

### Production Authority owns

- production permission;
- target ownership;
- precedence among production demands;
- expiration/verification rules at the production boundary.

### AIByzBuild owns

- concrete production execution.

### Verification owns

- distinguishing command issuance from observed state change;
- validating postconditions;
- reporting partial or failed outcomes.

No layer should silently assume the responsibilities of another.

---

## 14. Critical Anti-Regression Rules

### Rule 1 — Do not destroy emergent behavior without proving its replacement is superior.

If Shadow's existing rule interactions produce useful behavior, document and preserve the mechanism until a replacement is qualified.

### Rule 2 — Do not confuse architectural elegance with strategic improvement.

A cleaner state machine is not automatically a better AI.

### Rule 3 — Do not confuse static reachability with runtime success.

A reachable command path is not proof of engine execution or world-state mutation.

### Rule 4 — Do not make AEGIS a monolithic planner.

The objective is explicit strategic authority, not an enormous centralized state machine.

### Rule 5 — Do not duplicate executors.

AEGIS should not create a second production executor when AIByzBuild already performs that role.

### Rule 6 — Do not allow legacy bypasses to remain invisible.

Every ordinary `train`, `build`, or `research` path outside the intended transaction architecture must be classified.

### Rule 7 — Do not equate resource reservation with strategic success.

Reservation proves economic commitment, not capability acquisition.

### Rule 8 — Do not advance progression from command acknowledgement alone.

Verification is mandatory at the appropriate postcondition boundary.

---

## 15. Forensic Work Required Before Implementation

Before replacing any Shadow strategic component, perform a complete functional extraction of its strategic role.

For each candidate mechanism, record:

1. inputs;
2. conditions;
3. state reads;
4. state writes;
5. rule-order dependencies;
6. `up-jump-rule` effects;
7. escrow side effects;
8. resource side effects;
9. transaction effects;
10. completion predicates;
11. retry behavior;
12. cancellation behavior;
13. interaction with competing branches;
14. possible bypass paths;
15. evidence classification;
16. observed strategic purpose;
17. failure modes;
18. whether the behavior is unique to Shadow or reproducible elsewhere.

The purpose is to determine **what Shadow actually does**, not merely what its code appears intended to do.

---

## 16. Strategic Replacement Qualification Test

A candidate replacement is not qualified merely because it compiles or passes static syntax checks.

It must demonstrate, at minimum:

### A. Authority clarity

There is an explicit answer to which strategic commitment owns the scarce resource.

### B. Capability abstraction

The strategic requirement can be represented independently of one particular executor action where multiple solutions exist.

### C. Feasibility separation

Strategic desirability is distinguishable from economic feasibility.

### D. Commitment integrity

Resources cannot remain indefinitely reserved without an owner, purpose, expiry, or release path.

### E. Verification integrity

Progress cannot advance solely because a command was issued.

### F. Preemption integrity

A higher-priority requirement can interrupt lower-priority work without corrupting state.

### G. Bypass visibility

Legacy paths cannot silently circumvent the intended authority model.

### H. Reassessment

Verified world-state changes feed back into strategic evaluation.

---

## 17. Recommended Implementation Sequence

### Phase 1 — Strategic-path extraction

Map every Shadow path that contributes to choosing the next economic/production/research/construction commitment.

Do not modify code yet.

### Phase 2 — Authority graph

Construct an explicit graph:

`OBSERVATION → DECISION INPUT → PRIORITY MECHANISM → COMMITMENT → RESOURCE CONTROL → EXECUTION → VERIFICATION`.

Identify all hidden arbitration edges.

### Phase 3 — Shadow capability preservation

Freeze and characterize the economic substrate that should survive.

### Phase 4 — Strategic control interface

Define the minimal AEGIS-to-Shadow interface:

`CAPABILITY REQUIREMENT → PRIORITY → COMMITMENT REQUEST → RESOURCE REQUIREMENT → EXECUTION CONTRACT`.

### Phase 5 — Replace one strategic decision class

The first recommended pilot is **threat-driven capability acquisition**, because it directly exercises observation, belief, capability reasoning, arbitration, economic commitment, production, and verification.

### Phase 6 — Comparative qualification

Compare old Shadow and AEGIS-supervised Shadow for:

- commitment clarity;
- resource starvation;
- unnecessary switching;
- response latency;
- abandoned reservations;
- bypass frequency;
- verification integrity;
- strategic flexibility.

### Phase 7 — Expand only after evidence

Only after the pilot demonstrates a causal improvement should additional strategic domains be migrated.

---

## 18. First Strategic Pilot

The recommended first pilot is:

**THREAT → ANTI-THREAT CAPABILITY → ECONOMIC COMMITMENT**

Example:

`enemy cavalry observation`
→ `cavalry threat belief`
→ `anti-cavalry capability deficit`
→ `candidate responses`
→ `strategic arbitration`
→ `minimum viable commitment`
→ `Shadow reservation / escrow`
→ `Production Authority`
→ `AIByzBuild`
→ `observed production`
→ `verified capability`
→ `remaining deficit`
→ `reassessment`.

This is strategically superior to simply transplanting a `build camels` rule because it tests whether the architecture can distinguish **problem**, **capability**, **solution**, **commitment**, and **execution**.

---

## 19. Final Architectural Position

The correct relationship between AEGIS and Shadow is not:

`AEGIS replaces Shadow.`

Nor is it:

`Shadow remains the strategic authority.`

The target is:

`AEGIS supervises strategic intent; Shadow enforces economic commitment.`

More precisely:

`AEGIS`
**decides what capability is required and why.**

`Strategic Arbitration`
**decides which requirement deserves scarce capital now.**

`Shadow`
**protects and schedules the capital.**

`Production Authority`
**determines what execution is authorized.**

`AIByzBuild`
**performs the action.**

`Verification`
**determines what actually happened.**

`AEGIS`
**updates its beliefs and decides again.**

The strategic replacement is therefore deliberately narrow but high leverage: **replace the opaque strategic-priority/commitment decision boundary while preserving and improving the Shadow mechanisms that already provide economic discipline, transactional sequencing, progression, and completion feedback.**

The guiding engineering maxim is:

> **Do not replace what we have merely because we can build something cleaner. Replace only what we can demonstrate is strategically limiting—and preserve every mechanism whose behavior gives the combined system capabilities we would otherwise have to rediscover.**
