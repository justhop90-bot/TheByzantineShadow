# The Byzantine Shadow — System 08: Research & Technology Forensic Engineering v0.1

**Status:** Forensic engineering specification  
**System:** 08 — Research / Technology  
**Predecessors:** System 01 — Initialization / Configuration; System 02 — State Namespace / Authority; System 03 — Target Acquisition; System 04 — Scouting / Information Acquisition; System 05 — Food Logistics; System 06 — Villager Economy / Labor Allocation; System 07 — Construction / Infrastructure  
**Primary disposition:** PRESERVE + IMPROVE  
**Evidence standard:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN  
**Source donor:** Shadow donor corpus previously audited; exact rule-level attribution must be re-established against the frozen donor before implementation.

---

## 0. Purpose and forensic standard

System 08 isolates the Shadow donor's **research and technology control boundary**: the machinery that converts an authorized technology requirement into a funded research transaction, satisfies prerequisites, issues the research operation, observes research state, verifies completion, reconciles resources, and feeds the resulting capability back into the control plane.

The economic forensic baseline establishes that Shadow's armor, ranged, economic, age, and military technologies participate in the same transaction/progression architecture as other economic operations. Escrow-aware research, affordability predicates, progression state, and post-command completion observation are therefore part of the donor's reusable economic machinery rather than an isolated strategic technology planner. fileciteturn43file0L2-L2

The central engineering conclusion is:

> **Research is a capability-acquisition transaction constrained by prerequisites, resources, temporal opportunity cost, and strategic authority.**

Static presence of a research rule does not establish that its prerequisite chain is reachable, that affordability is sufficient, that the technology is actually initiated, that research completes, or that the resulting capability changes strategic outcomes. Each is a separate evidence boundary.

System 08 therefore preserves the donor's research transaction discipline while replacing implicit strategic priority with explicit AEGIS-controlled requirements and commitments.

---

# 1. Executive finding

Research should be treated as a **technology transaction and capability-state machine**, not as a list of `research` commands.

The canonical architecture is:

```text
OBSERVATION / OBJECTIVE
        ↓
CAPABILITY REQUIREMENT
        ↓
TECHNOLOGY CANDIDATE
        ↓
PREREQUISITE GRAPH
        ↓
FEASIBILITY
        ↓
STRATEGIC / ECONOMIC AUTHORIZATION
        ↓
COMMITMENT
        ↓
RESOURCE RESERVATION
        ↓
ESCROW-AWARE PREFLIGHT
        ↓
RESEARCH TRANSACTION
        ↓
RESEARCH STATE OBSERVATION
        ↓
VERIFIED TECHNOLOGY
        ↓
CAPABILITY UPDATE
        ↓
RESERVATION RECONCILIATION
        ↓
REASSESSMENT
```

This explicitly rejects:

```text
research command issued → technology completed → capability acquired
```

as a single state transition.

The proper model separates intent, eligibility, funding, transaction issuance, research progress, completion, and strategic effect.

**Disposition:** preserve donor research interfaces and progression behavior; formalize technology identity and prerequisite dependencies; make strategic intent explicit; distinguish affordability from desirability; verify completion before capability credit; qualify one narrow technology vertical slice before broad transplantation.

---

# 2. System boundary

## 2.1 In scope

System 08 owns the forensic/design boundary for:

1. technology requirements;
2. technology candidate identity;
3. research prerequisites;
4. age/prerequisite dependencies;
5. research affordability;
6. research resource reservation;
7. escrow-aware research preflight;
8. `up-research` execution interfaces;
9. research state observation;
10. technology completion verification;
11. research transaction failure/retry;
12. technology cancellation/invalidation;
13. research progression;
14. residual escrow release;
15. technology-to-capability mapping;
16. interaction with infrastructure requirements;
17. interaction with villager/resource allocation;
18. interaction with military/economic capability requirements;
19. research starvation/deadlock telemetry;
20. technology priority and preemption interfaces.

## 2.2 Explicitly out of scope

System 08 does not own:

- global strategic doctrine;
- target-player selection;
- scouting movement;
- strategic threat inference as a whole;
- military composition selection as a whole;
- construction execution;
- general villager labor allocation;
- production execution;
- final strategic commitment arbitration.

System 08 may declare research feasibility and capability effects, but it must not silently decide that a technology is strategically required merely because it is available.

---

# 3. Evidence hierarchy

### DIRECT

A research rule, technology identifier, prerequisite, affordability predicate, escrow operation, state write, command, completion condition, jump, or progression action is explicitly present in the donor.

### COMPOSED

Multiple direct mechanisms establish a research transaction or prerequisite chain when their interaction is structurally demonstrated.

### INFERRED

The strategic or semantic purpose of a research mechanism is strongly suggested by interacting donor state but not explicitly declared.

### AEGIS-GENERALIZATION

A design requirement introduced to make research attributable, auditable, capability-oriented, or compatible with the AEGIS control plane.

### UNCERTAIN

The evidence is insufficient to establish exact semantic or runtime behavior.

Mandatory rule:

> Do not infer strategic necessity from technology availability, and do not infer technology completion from command acceptance.

---

# 4. Research is a capability transaction

The fundamental distinction is:

```text
TECHNOLOGY
        ≠
RESEARCH TRANSACTION
        ≠
CAPABILITY
```

A technology is an available game-system object.

A research transaction is an economic/execution attempt to acquire it.

A capability is the verified strategic or operational consequence that becomes available after completion.

For example:

```text
ENEMY CAVALRY OBSERVED
        ↓
ANTI-CAVALRY CAPABILITY REQUIRED
        ↓
CAMEL-RELATED TECHNOLOGY CANDIDATE
```

does not mean that the technology must be researched. Alternative capabilities may exist.

Conversely:

```text
TECHNOLOGY AVAILABLE
```

does not mean:

```text
RESEARCH STRATEGICALLY JUSTIFIED
```

The strategic layer selects the requirement; System 08 executes and verifies the research transaction.

---

# 5. Technology identity versus technology effect

The architecture must distinguish:

```text
TECHNOLOGY_ID
TECHNOLOGY_CLASS
PREREQUISITES
RESOURCE_COST
RESEARCH_STATE
COMPLETION_STATE
CAPABILITY_EFFECT
```

The technology identifier answers **what is being researched**.

The capability effect answers **what verified capability changes afterward**.

These should not be collapsed into one strategic variable.

A technology may affect multiple capabilities, and a capability may have multiple candidate technologies.

This is an important architectural reason to retain the capability-oriented strategic model established by the Strategic Control Replacement Blueprint.

---

# 6. Research requirement contract

Every strategically meaningful technology request should have a conceptual requirement record.

Minimum fields:

```text
REQUIREMENT_ID
ORIGINATING_OBJECTIVE
REQUIRED_CAPABILITY
TECHNOLOGY_ID
CANDIDATE_CLASS
PRIORITY_CONTEXT
URGENCY
CONFIDENCE
PREREQUISITE_SET
RESOURCE_REQUIREMENT
CURRENT_VERIFIED_CAPABILITY
VERIFIED_COMMITTED_RESEARCH
TRUE_DEFICIT
CREATION_EPOCH
EXPIRY_CONDITION
INVALIDATION_CONDITION
COMPLETION_CONDITION
OWNER
GENERATION
EVIDENCE_LEVEL
```

The important quantity is not merely whether the technology is absent. It is whether the required capability remains deficient after accounting for **verified existing capability and verified committed capability**.

A technology whose transaction has merely been issued is not automatically verified committed capability unless the project's commitment semantics explicitly support that intermediate state.

---

# 7. Prerequisite graph

Research is inherently dependency-oriented.

Conceptually:

```text
CAPABILITY REQUIREMENT
        ↓
TECHNOLOGY A
        ↓
PREREQUISITE B
        ↓
PREREQUISITE C
        ↓
AGE / BUILDING / OTHER CONDITION
```

The prerequisite graph must distinguish:

```text
UNKNOWN
UNAVAILABLE
ELIGIBLE
COMMITTED
IN PROGRESS
COMPLETED
INVALIDATED
```

An unmet prerequisite is a **feasibility condition**, not automatically a strategic failure.

If the prerequisite itself can be acquired through another commitment, the dependency should be represented explicitly rather than hidden inside a research rule.

Example:

```text
TECHNOLOGY A
  requires BUILDING B
    requires WOOD COMMITMENT C
```

The dependency graph then allows the system to explain why Technology A is blocked without incorrectly declaring Technology A strategically undesirable.

---

# 8. Prerequisite ownership

A prerequisite may belong to another system.

Examples:

```text
AGE REQUIREMENT       → progression/strategic authority
BUILDING REQUIREMENT  → System 07
RESOURCE REQUIREMENT  → Shadow / System 06
TECHNOLOGY REQUIREMENT→ System 08
```

System 08 consumes prerequisite state; it does not acquire ownership of every prerequisite merely because research depends upon it.

This prevents a technology branch from silently becoming a second construction or economic controller.

---

# 9. Research affordability versus strategic desirability

The donor's escrow-aware affordability predicates are feasibility gates. The economic audit explicitly establishes that affordability answers whether a transaction can be funded under the current reservation state; it does not establish strategic correctness or completion. fileciteturn43file0L2-L2

Therefore:

```text
AFFORDABLE
```

means approximately:

```text
ECONOMICALLY FEASIBLE TO ATTEMPT
```

not:

```text
STRATEGICALLY CORRECT
```

and not:

```text
COMPLETED
```

The research authority must preserve these epistemic boundaries.

---

# 10. Research commitment

Once an authorized technology requirement wins arbitration, it becomes a commitment.

Conceptually:

```text
CANDIDATE
→ PREPARING
→ COMMITTED
→ FUNDED
→ EXECUTING
→ VERIFIED
```

A research commitment must identify:

- commitment ID;
- originating requirement;
- technology ID;
- required capability;
- priority;
- resource requirement;
- minimum viable funding;
- creation epoch;
- generation;
- prerequisite dependencies;
- completion predicate;
- expiry;
- cancellation predicate;
- retry policy;
- preemption policy;
- owner.

No research reservation should exist without an attributable commitment.

---

# 11. Escrow-aware research transaction

The Shadow donor explicitly uses an escrow-state carrier with transactional research interfaces. The blueprint identifies `gl-escrow-state` as a transaction-mode carrier and `up-research` / escrow-aware preflight as reusable execution interfaces. fileciteturn45file0L2-L2

The canonical transaction is therefore:

```text
RESEARCH COMMITMENT
        ↓
RESOURCE RESERVATION
        ↓
TRANSACTION ESCROW
        ↓
CAN-RESEARCH-WITH-ESCROW
        ↓
UP-RESEARCH
        ↓
OBSERVE
```

The three escrow layers remain distinct:

1. policy escrow;
2. commitment escrow;
3. transaction escrow.

A technology transaction must never silently appropriate another commitment's reservation.

---

# 12. Research progression

The donor's strongest reusable behavior is the separation between transaction issuance and progression advancement.

The blueprint explicitly identifies a recurring pattern in which research waits for relevant observed research state before advancing `gl-build-progress`. fileciteturn45file0L2-L2

The generalized progression contract is:

```text
WORK_ITEM_CREATED
→ REQUIREMENT_DECLARED
→ RESERVATION_REQUESTED
→ RESERVATION_FUNDED
→ EXECUTION_AUTHORIZED
→ COMMAND_ISSUED
→ RESEARCH_STATE_OBSERVED
→ TECHNOLOGY_VERIFIED
→ WORK_ITEM_CONFIRMED
→ PROGRESS_ADVANCED
```

The critical invariant is:

> **Research command issuance cannot advance strategic or progression state without the required observed postcondition.**

---

# 13. Research state observation

Research requires temporal observation.

Conceptually:

```text
NOT_STARTED
    ↓
ELIGIBLE
    ↓
REQUESTED
    ↓
AUTHORIZED
    ↓
ISSUED
    ↓
IN_PROGRESS / PENDING
    ↓
COMPLETED
    ↓
VERIFIED
```

The exact engine representation of these states must be recovered from the DE runtime and donor semantics before assigning literal numeric channels.

Do not assume that a research-status value has the same meaning across technologies or contexts merely because a donor rule compares it numerically.

---

# 14. Verification contract

Verification must be technology-specific.

Potential evidence includes:

```text
RESEARCH STATUS MUTATED
TECHNOLOGY COMPLETION OBSERVED
PREREQUISITE STATE CHANGED
TECHNOLOGY EFFECT OBSERVED
CAPABILITY STATE UPDATED
```

These evidence levels must not automatically be treated as equivalent.

For example:

```text
RESEARCH STATUS CHANGED
```

may prove that research began or progressed, while:

```text
TECHNOLOGY COMPLETED
```

may be required before the strategic capability is credited.

The verifier must specify the sufficient postcondition for each technology class.

---

# 15. Technology capability mapping

A completed technology should feed a capability registry rather than directly rewriting strategic objectives.

Conceptually:

```text
VERIFIED TECHNOLOGY
        ↓
CAPABILITY EFFECT RECORD
        ↓
CURRENT VERIFIED CAPABILITY
        ↓
REASSESSMENT
```

The effect record should identify, where applicable:

```text
CAPABILITY_ID
SOURCE_TECHNOLOGY
EFFECT_CLASS
EFFECT_MAGNITUDE / MODE
VALID_FROM
VALID_UNTIL
EVIDENCE_LEVEL
GENERATION
```

Do not assume that every technology produces a binary capability.

Some effects may alter:

- efficiency;
- survivability;
- damage potential;
- production feasibility;
- economic throughput;
- research availability;
- infrastructure capability;
- strategic option space.

The exact effect semantics require donor/runtime evidence.

---

# 16. Research and economic demand

Research competes for the same resources needed by:

- villagers;
- production;
- construction;
- farms;
- infrastructure;
- other research;
- emergency response.

Therefore research must declare its economic requirement instead of directly manipulating global worker allocation.

The interface is:

```text
RESEARCH REQUIREMENT
        ↓
RESOURCE REQUIREMENT
        ↓
SHADOW COMMITMENT / ESCROW
        ↓
FEASIBILITY
        ↓
RESEARCH EXECUTION
```

System 06 may respond to an authorized resource requirement by adjusting labor allocation. System 08 must not directly redefine System 06's policy.

---

# 17. Research and infrastructure dependency

Some technologies require infrastructure before research can occur.

The correct dependency is:

```text
TECHNOLOGY REQUIREMENT
        ↓
INFRASTRUCTURE PREREQUISITE
        ↓
SYSTEM 07 REQUIREMENT
        ↓
CONSTRUCTION COMMITMENT
        ↓
VERIFIED BUILDING
        ↓
RESEARCH ELIGIBILITY
```

This dependency must remain visible.

A research branch should not repeatedly attempt a transaction whose prerequisite is structurally unavailable without recording the reason.

Repeated failed preflight should therefore produce a **blocked feasibility state**, not an infinite retry loop.

---

# 18. Research priority and strategic authority

Technology selection belongs above System 08.

AEGIS may determine:

```text
CAPABILITY REQUIRED
```

and the strategic arbiter may select:

```text
TECHNOLOGY A > TECHNOLOGY B
```

under explicit priority semantics.

System 08 then determines:

```text
CAN A BE RESEARCHED?
HOW IS A FUNDED?
HOW IS A TRANSACTION ISSUED?
WHEN IS A VERIFIED?
```

This boundary is essential because Shadow historically uses rule ordering and `up-jump-rule` as procedural arbitration for production/research branches. The blueprint explicitly requires that this implicit priority be extracted and made explicit rather than allowed to remain hidden in source order. fileciteturn45file0L2-L2

---

# 19. Preemption and hysteresis

Research can be preempted when a higher-priority commitment requires the same scarce resources.

Conceptually:

```text
ACTIVE RESEARCH COMMITMENT
        ↓
HIGHER PRIORITY REQUIREMENT
        ↓
SUSPEND / STOP NEW FUNDING
        ↓
RECONCILE RESERVATION
        ↓
EXECUTE HIGHER PRIORITY COMMITMENT
        ↓
REASSESS RESEARCH
```

However, the architecture must distinguish **logical preemption** from actual engine interruption.

If the engine cannot cancel or interrupt an already active research operation, the system may only be able to prevent subsequent funding or suppress competing research requests.

That engine capability is UNCERTAIN until qualified.

Hysteresis remains mandatory for reversible strategic research selection:

- activation threshold;
- maintenance threshold;
- release threshold;
- preemption threshold;
- minimum dwell time;
- reservation age limit.

---

# 20. Cancellation and invalidation

Research cancellation must distinguish at least:

```text
CANCELLED BY STRATEGIC AUTHORITY
INVALIDATED BY BELIEF UPDATE
EXPIRED
BLOCKED BY PREREQUISITE
FAILED TRANSACTION
UNVERIFIED
COMPLETED
```

A strategic belief change should not be represented as an execution failure.

For example:

```text
ENEMY CAVALRY BELIEF REVOKED
        ↓
ANTI-CAVALRY TECHNOLOGY NO LONGER REQUIRED
        ↓
COMMITMENT INVALIDATED
```

That is different from:

```text
RESEARCH COMMAND FAILED
```

Keeping those causes separate is necessary for useful telemetry and correct reassessment.

---

# 21. Retry semantics

A failed research transaction does not automatically invalidate the research requirement.

Use separate identities:

```text
R8 = technology requirement
C8 = research commitment
T8-1 = first transaction
T8-2 = retry transaction
```

If `T8-1` fails:

```text
T8-1 → FAILED / UNVERIFIED
C8 persists
R8 persists
```

A retry creates a new transaction identity.

Repeated failure may eventually establish:

```text
BLOCKED
FAILED
EXPIRED
CANCELLED
DEADLOCKED
```

but the transition must have an explicit predicate or policy.

There is no universal two-failure abandonment rule.

---

# 22. Residual escrow reconciliation

Research costs may differ from a reserved amount because of transaction policy, changing requirements, or failed attempts.

After verification or failure, the transaction must reconcile:

```text
RESERVED
CONSUMED
UNCONSUMED
RELEASED
REMAINING COMMITMENT RESERVATION
```

The Shadow donor's explicit resource-release behavior is valuable evidence that escrow should not remain indefinitely attached to completed or irrelevant work. fileciteturn43file0L2-L2

The AEGIS improvement is attribution:

> Release the remainder belonging to the completed/failed research commitment; do not globally destroy unrelated reservations.

---

# 23. Research starvation and deadlock

Research starvation occurs when a valid research commitment remains unfunded because other requirements continuously consume the relevant resources.

Track at minimum:

```text
RESEARCH_STARVATION_AGE
RESEARCH_COMMITMENT_AGE
RESOURCE_DEFICIT
PREREQUISITE_BLOCK_AGE
COMPETING_COMMITMENT_LOAD
ESCROW_CONCENTRATION
RETRY_COUNT
TIME_SINCE_LAST_PROGRESS
```

Deadlock should be considered when research cannot progress because its prerequisites and competing commitments form a stable dependency cycle.

Example:

```text
TECH A
 ↓ requires BUILDING B
 ↓ requires WOOD
 ↓ wood reserved for ECONOMIC COMMITMENT C
 ↓ C cannot complete without TECH A
```

The correct response is diagnosis and arbitration, not indefinite repeated preflight.

---

# 24. Research and strategic reassessment

A completed technology changes the feasible capability set.

Therefore:

```text
TECHNOLOGY VERIFIED
        ↓
CAPABILITY STATE UPDATED
        ↓
TRUE DEFICITS RECALCULATED
        ↓
ACTIVE COMMITMENTS REASSESSED
        ↓
INFORMATION REQUIREMENTS UPDATED
```

The research system should not declare the next strategic objective itself.

It supplies verified state to the strategic control plane.

This preserves the larger architecture:

```text
OBSERVE
→ BELIEVE
→ OBJECTIVE
→ CAPABILITY REQUIREMENT
→ COMMIT
→ EXECUTE
→ VERIFY
→ REASSESS
```

---

# 25. Donor extraction requirements

Before implementation, Muse must extract every research-related mechanism from the frozen donor and classify it.

Required inventory fields:

1. technology identifier;
2. technology class;
3. rule/file location;
4. triggering condition;
5. prerequisite conditions;
6. resource predicates;
7. escrow state used;
8. escrow percentage writes;
9. direct escrow modifications;
10. state reads;
11. state writes;
12. `up-research` calls;
13. `up-can-*` preflight calls;
14. `up-jump-rule` interactions;
15. rule-order dependencies;
16. progression writes;
17. completion predicates;
18. research-state comparisons;
19. resource-release behavior;
20. retry behavior;
21. cancellation behavior;
22. competing research branches;
23. infrastructure dependencies;
24. economic dependencies;
25. strategic dependencies;
26. duplicate definitions;
27. conditional definitions;
28. dead/unreachable candidates;
29. evidence classification;
30. runtime qualification status.

The purpose is not merely to enumerate technologies. It is to reconstruct the **transaction graph and authority graph** around each technology.

---

# 26. Required dependency graph

The research subsystem should ultimately produce a graph of the form:

```text
OBJECTIVE
   ↓
CAPABILITY REQUIREMENT
   ↓
TECHNOLOGY CANDIDATE
   ↓
PREREQUISITE GRAPH
   ├── AGE
   ├── BUILDING
   ├── RESOURCE
   ├── OTHER TECHNOLOGY
   └── STRATEGIC VALIDITY
   ↓
COMMITMENT
   ↓
RESOURCE RESERVATION
   ↓
TRANSACTION
   ↓
RESEARCH STATE
   ↓
VERIFICATION
   ↓
CAPABILITY EFFECT
   ↓
REASSESSMENT
```

Every edge should have an authority owner and evidence level.

This prevents the common failure in which a technology rule appears self-contained while actually depending on hidden progression, infrastructure, resource, or strategic state.

---

# 27. Static versus runtime boundary

Static analysis can establish:

- technology rules exist;
- prerequisite predicates exist;
- research commands exist;
- escrow-aware research interfaces exist;
- progression variables are written/read;
- release operations exist;
- jump/order dependencies exist;
- completion predicates exist in source.

Static analysis cannot establish by itself:

- the selected technology at runtime;
- successful prerequisite satisfaction;
- actual affordability under engine state;
- research command acceptance;
- research initiation;
- research completion;
- capability effect in the world;
- strategic improvement.

Runtime qualification must establish these separately.

---

# 28. Qualification sequence

### R8-0 — Static inventory

Extract all research rules, constants, state channels, commands, prerequisites, releases, jumps, and progression interactions.

### R8-1 — State ownership

Map technology state, commitment state, transaction state, verification state, and progression state to authoritative owners.

### R8-2 — Prerequisite qualification

Select one technology with a small prerequisite chain and establish the actual eligibility path.

### R8-3 — Funding qualification

Demonstrate resource reservation and escrow-aware affordability without claiming completion.

### R8-4 — Transaction qualification

Demonstrate research transaction issuance and distinguish command acceptance from research-state mutation.

### R8-5 — Completion qualification

Observe the required technology completion state and verify the postcondition.

### R8-6 — Capability qualification

Demonstrate that the verified technology updates the intended capability record.

### R8-7 — Failure/retry qualification

Qualify blocked prerequisite, failed transaction, residual escrow, and retry semantics.

### R8-8 — Strategic qualification

Demonstrate the complete loop:

```text
REQUIREMENT
→ TECHNOLOGY SELECTION
→ COMMITMENT
→ FUNDING
→ RESEARCH
→ VERIFICATION
→ CAPABILITY UPDATE
→ REASSESSMENT
```

No broad technology transplant should occur before the smallest complete loop is qualified.

---

# 29. First implementation slice

The first implementation should be deliberately narrow.

Recommended slice:

```text
ONE TECHNOLOGY
        ↓
ONE EXPLICIT CAPABILITY REQUIREMENT
        ↓
ONE COMMITMENT
        ↓
ONE RESOURCE RESERVATION
        ↓
ONE ESCROW-AWARE PREFLIGHT
        ↓
ONE RESEARCH TRANSACTION
        ↓
ONE OBSERVED COMPLETION
        ↓
ONE CAPABILITY UPDATE
        ↓
ONE REASSESSMENT
```

Choose a technology whose prerequisites are already satisfied or can be independently verified without introducing an entire new dependency subsystem.

Do not begin by transplanting every technology branch.

The first slice should prove the **transaction and verification architecture**, not maximize technology coverage.

---

# 30. Donor preservation and improvement matrix

| Donor mechanism | Disposition | AEGIS treatment |
|---|---|---|
| escrow-aware research | KEEP | Preserve as transaction interface |
| `gl-escrow-state` | KEEP / FORMALIZE | Canonical transaction-mode carrier |
| `can-research-with-escrow`-style predicates | KEEP | Feasibility/preflight gate |
| `up-can-*` research preflight | KEEP | Transaction preparation |
| `up-research` | KEEP AS EXECUTION INTERFACE | Never strategic authority |
| research progression state | KEEP / REFACTOR | Formal commitment/work-item progression |
| observed research completion | KEEP / STRENGTHEN | Verification boundary |
| research-related escrow release | KEEP / FORMALIZE | Owner-aware reconciliation |
| research `up-jump-rule` priority | EXTRACT / EXPLICITATE | Strategic arbitration interface |
| raw rule-order priority | EXTRACT / EXPLICITATE | Authority precedence registry |
| donor technology coefficients | ADAPT / QUALIFY | Policy values, not engine facts |
| duplicate technology definitions | QUARANTINE | Classify before transplant |
| unexplained numeric state channels | QUARANTINE | ABI qualification required |
| wholesale technology code | REJECT | Surgical extraction only |

---

# 31. Anti-patterns

System 08 must explicitly prevent:

1. **Technology-as-strategy** — researching because a technology exists.
2. **Command-as-completion** — treating `up-research` as proof of completion.
3. **Affordability-as-success** — treating `can-research-with-escrow` as proof of strategic correctness.
4. **Prerequisite opacity** — hiding dependency failures inside repeated research attempts.
5. **Research-as-global-resource-owner** — allowing research to seize resources without commitment authority.
6. **Research-as-labor-controller** — directly rewriting villager allocation.
7. **Research-as-construction-controller** — silently acquiring infrastructure authority.
8. **Jump-rule-as-strategy** — encoding strategic doctrine solely through source order.
9. **Infinite retry** — repeatedly issuing blocked research without aging or diagnosis.
10. **Premature cancellation** — invalidating a strategic requirement because one transaction failed.
11. **False capability credit** — counting a pending research transaction as completed capability.
12. **Global escrow release** — releasing unrelated commitments when one technology completes.
13. **Static/runtime conflation** — treating source reachability as proof of actual research behavior.

---

# 32. Hard invariants

### RS-01
A technology is not a strategic objective.

### RS-02
A technology requirement must have an owning authority.

### RS-03
A research transaction must have an attributable commitment.

### RS-04
Prerequisite failure is distinct from strategic invalidation.

### RS-05
Affordability proves feasibility, not completion.

### RS-06
Research command issuance does not prove research completion.

### RS-07
Research completion does not automatically prove every strategic capability effect unless the effect is verified.

### RS-08
A failed transaction does not automatically terminate its requirement.

### RS-09
Retries require distinct transaction identity.

### RS-10
Residual escrow must be reconciled to its owner.

### RS-11
Research cannot silently override unrelated commitments.

### RS-12
Research cannot silently acquire construction or labor authority.

### RS-13
Preemption must preserve commitment history.

### RS-14
Blocked research must expose its blocking dependency.

### RS-15
No progression advance without the required postcondition.

### RS-16
Static source evidence is not runtime qualification.

### RS-17
Technology effects must feed verified capability state before strategic reassessment.

### RS-18
Unqualified numeric research-state channels remain ABI-uncertain.

---

# 33. Definition of done

System 08 is not complete until the following are answered against the donor and, where required, runtime-qualified:

1. What are all research state channels?
2. Who owns each channel?
3. What are the legal states and numeric meanings?
4. Which rules request each technology?
5. Which rules can suppress or preempt another research branch?
6. What prerequisites exist for each technology?
7. Which prerequisites are owned by other systems?
8. How does Shadow reserve research resources?
9. How does escrow state enter the research transaction?
10. What proves affordability?
11. What proves research initiation?
12. What proves research completion?
13. What proves the intended capability effect?
14. What happens when research is blocked?
15. What happens when the transaction fails?
16. How are retries represented?
17. How is residual escrow released?
18. What causes cancellation?
19. What causes invalidation after belief change?
20. What causes preemption?
21. What happens to an already-active research operation during preemption?
22. Which paths bypass escrow governance?
23. Which numeric values are donor policy versus engine semantics?
24. Which duplicate definitions are legitimate versus conflicting?
25. Which research paths are dead or legacy?
26. What is the smallest complete research vertical slice?
27. What runtime evidence qualifies it?
28. How does verified research update capability state?
29. How does that capability update trigger strategic reassessment?
30. Can every material transition be explained by an explicit owner and evidence level?

If any answer remains unknown, mark it **UNCERTAIN** rather than inventing semantics.

---

# 34. System 08 architectural result

The final System 08 boundary is:

```text
AEGIS / STRATEGIC AUTHORITY
        ↓
CAPABILITY REQUIREMENT
        ↓
TECHNOLOGY CANDIDATE / COMMITMENT
        ↓
SYSTEM 08 — RESEARCH CONTROL
        ↓
PREREQUISITE + RESOURCE FEASIBILITY
        ↓
SHADOW ESCROW / TRANSACTION SUBSTRATE
        ↓
UP-RESEARCH EXECUTION INTERFACE
        ↓
ENGINE RESEARCH STATE
        ↓
VERIFICATION
        ↓
CAPABILITY REGISTRY
        ↓
AEGIS REASSESSMENT
```

System 08 therefore does **not** become a technology planner.

It becomes a trustworthy **capability-acquisition transaction boundary**.

The strategic plane decides why the capability is needed. Shadow supplies the economic discipline required to fund it. System 08 determines whether the technology transaction is feasible, executes through the existing interface, verifies what actually happened, reconciles the reservation, and reports the resulting capability evidence upward.

That separation preserves the donor's strongest research machinery while eliminating the ambiguity that currently makes research priority, resource protection, progression, and strategic intent appear to be the same mechanism.
