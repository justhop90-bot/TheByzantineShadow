# The Byzantine Shadow — System 07: Construction & Infrastructure Forensic Engineering v0.1

**Status:** Forensic engineering specification  
**System:** 07 — Construction / Infrastructure  
**Predecessors:** System 01 — Initialization / Configuration; System 02 — State Namespace / Authority; System 03 — Target Acquisition; System 04 — Scouting / Information Acquisition; System 05 — Food Logistics; System 06 — Villager Economy / Labor Allocation  
**Primary disposition:** PRESERVE + IMPROVE  
**Evidence standard:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN  
**Source donor:** Shadow donor corpus previously audited; exact mechanism attribution must be re-established against the frozen donor before implementation.

---

## 0. Purpose and forensic standard

System 07 isolates the Shadow donor's **construction and infrastructure control boundary**: the machinery that converts an economic or strategic infrastructure requirement into a funded construction transaction, obtains an executor action, observes the resulting pending/placed/building state, and reconciles the associated commitment.

The existing Shadow forensic baseline identifies substantial infrastructure construction governance, including stables, monasteries, markets, siege workshops, barracks, farms, houses, camps, universities, escrow-aware construction, progression state, and fallback behavior for cases where the ordinary rebuild system occasionally fails. These findings establish that construction is materially more than a list of `build` commands.

The core engineering conclusion is:

> **Construction is a spatially constrained, resource-funded, worker-mediated transaction whose completion must be established through world-state observation.**

Static source presence does not establish that a construction rule is reachable, that placement succeeds, that a villager reaches the site, that the building completes, or that the resulting infrastructure satisfies the strategic requirement. Those are separate evidence boundaries.

System 07 therefore recovers the donor's construction knowledge while formalizing the boundary between **infrastructure requirement, commitment, transaction, placement, execution, and verification**.

---

# 1. Executive finding

The construction subsystem should be treated as an **infrastructure transaction controller**, not as an unconditional building executor.

The canonical architecture is:

```text
STRATEGIC / ECONOMIC REQUIREMENT
          ↓
INFRASTRUCTURE REQUIREMENT
          ↓
BUILDING CANDIDATE
          ↓
FEASIBILITY / PREREQUISITES
          ↓
COMMITMENT
          ↓
RESOURCE RESERVATION
          ↓
CONSTRUCTION AUTHORITY
          ↓
PLACEMENT / BUILDER ASSIGNMENT
          ↓
COMMAND / TRANSACTION
          ↓
PENDING OBJECT
          ↓
PLACEMENT CONFIRMATION
          ↓
BUILDING OBSERVATION
          ↓
OPERATIONAL VERIFICATION
          ↓
RESERVATION RECONCILIATION
          ↓
REQUIREMENT SATISFACTION / REASSESSMENT
```

This explicitly prevents the common false transition:

```text
build command issued → building exists → requirement satisfied
```

The correct model preserves the intermediate states.

**Disposition:** preserve donor construction interfaces and fallback knowledge; formalize building requirements and ownership; separate funding from placement; separate command issuance from pending-object observation and completed-building verification; qualify one narrow infrastructure vertical slice before broad transplantation.

---

# 2. System boundary

## 2.1 In scope

System 07 owns the forensic/design boundary for:

1. infrastructure requirements;
2. building candidate selection after higher-level authorization;
3. prerequisite and feasibility checks;
4. construction commitment creation;
5. wood/stone/resource reservation for construction;
6. builder availability requirements;
7. construction transaction preparation;
8. escrow-aware construction predicates;
9. `up-build` execution interfaces;
10. placement state;
11. pending construction objects;
12. building completion observation;
13. operational-building verification;
14. construction retry/failure handling;
15. rebuild/fallback behavior;
16. construction cancellation and abandonment;
17. infrastructure completion and requirement satisfaction;
18. interaction with food, production, research, and economic requirements;
19. construction telemetry and starvation/deadlock indicators.

## 2.2 Explicitly out of scope

System 07 does not own:

- global strategic doctrine;
- target-player selection;
- scouting movement;
- military composition selection;
- final strategic priority;
- unrestricted villager labor policy;
- production execution as a whole;
- research execution as a whole;
- strategic commitment selection.

Construction may consume an authorized commitment and declare feasibility failures. It must not silently invent a new strategic objective because a building is unavailable.

---

# 3. Evidence hierarchy

### DIRECT

A construction command, predicate, state carrier, building condition, placement check, fallback path, or progression operation is explicitly present in the donor.

### COMPOSED

Multiple directly observed mechanisms establish a construction transaction or lifecycle when their interaction is structurally demonstrated.

### INFERRED

The construction behavior is strongly suggested by state/ordering interactions but its semantic purpose is not explicitly stated.

### AEGIS-GENERALIZATION

A design requirement introduced to make construction attributable, auditable, verifiable, or compatible with AEGIS.

### UNCERTAIN

The evidence is insufficient to establish semantic meaning or runtime behavior.

Mandatory rule:

> Do not convert a building rule into a strategic fact merely because its condition mentions a strategic-looking variable.

Likewise, do not convert a `build` command into evidence that construction completed.

---

# 4. Construction is a transaction plus a spatial execution problem

Construction differs from training and research because it has a physical placement and builder component.

The transaction layer is:

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

The spatial/execution layer is independently:

```text
SITE REQUIRED
→ SITE CANDIDATE
→ SITE VALID
→ BUILDER AVAILABLE
→ BUILDER ASSIGNED
→ MOVING
→ PLACING
→ PENDING OBJECT
→ BUILDING
→ COMPLETED
→ OPERATIONAL
```

These state machines must not be collapsed.

For example:

```text
TRANSACTION = ISSUED
```

does not imply:

```text
BUILDING = COMPLETED
```

Similarly:

```text
SITE VALID
```

does not imply:

```text
BUILDER AVAILABLE
```

---

# 5. Building requirement versus building identity

A strategic requirement such as:

```text
PRODUCTION CAPACITY REQUIRED
```

is not the same object as:

```text
BUILD STABLE
```

and neither is the same as:

```text
STABLE AT X,Y
```

nor:

```text
STABLE #3 IS OPERATIONAL
```

The architecture must preserve these distinctions:

```text
REQUIREMENT
BUILDING TYPE
BUILDING INSTANCE
BUILD SITE
BUILD TRANSACTION
BUILDING STATE
OPERATIONAL CAPABILITY
```

This prevents infrastructure identity from becoming an accidental strategic controller.

---

# 6. Infrastructure requirement contract

Every strategically meaningful construction request should have a conceptual requirement record.

Minimum fields:

```text
REQUIREMENT_ID
ORIGINATING_OBJECTIVE
REQUIRED_CAPABILITY
BUILDING_CLASS
MINIMUM_COUNT
DESIRED_COUNT
CURRENT_VERIFIED_COUNT
VERIFIED_COMMITTED_COUNT
TRUE_DEFICIT
PREREQUISITES
RESOURCE_REQUIREMENT
BUILDER_REQUIREMENT
SITE_REQUIREMENT
PRIORITY_CONTEXT
CREATION_EPOCH
EXPIRY_CONDITION
INVALIDATION_CONDITION
COMPLETION_CONDITION
OWNER
GENERATION
EVIDENCE_LEVEL
```

The important quantity is the verified deficit:

```text
TRUE INFRASTRUCTURE DEFICIT
= required capability
  − current verified infrastructure
  − verified committed infrastructure
```

A requested building whose transaction has merely been issued is not automatically part of verified capability.

This follows the project's general capability rule and is an AEGIS-GENERALIZATION until runtime-qualified in the implementation.

---

# 7. Construction commitment

Once a building requirement wins strategic/economic arbitration, construction becomes a commitment.

Conceptually:

```text
CANDIDATE
→ PREPARING
→ COMMITTED
→ FUNDED
→ EXECUTING
→ VERIFIED
```

A construction commitment must identify:

- owner;
- requirement;
- building class;
- resource requirement;
- minimum viable funding;
- creation epoch;
- generation;
- priority;
- site policy;
- builder policy;
- completion predicate;
- expiry;
- cancellation predicate;
- retry policy;
- preemption policy.

No construction reservation should exist without an attributable commitment.

---

# 8. Resource reservation and escrow

The Shadow donor's economic architecture contains escrow-aware construction interfaces. The forensic baseline identifies `gl-escrow-state` as a transaction-mode carrier passed into `up-build`, and identifies `can-build-with-escrow`-style predicates as feasibility/preflight mechanisms.

These should be preserved as economic primitives, not strategic authorities.

The conceptual sequence is:

```text
CONSTRUCTION COMMITMENT
        ↓
RESOURCE REQUIREMENT
        ↓
COMMITMENT RESERVATION
        ↓
TRANSACTION ESCROW
        ↓
CAN-BUILD-WITH-ESCROW
        ↓
UP-BUILD
```

Policy escrow, commitment escrow, and transaction escrow must remain distinguishable.

A failed placement must not silently convert transaction escrow into permanent commitment escrow. Conversely, cancellation must not release resources belonging to another commitment.

---

# 9. Builder allocation is separate from construction authority

Construction requires a worker capable of executing the physical action.

System 06 owns general labor allocation. System 07 declares construction labor requirements and consumes an authorized builder assignment.

The conceptual interface is:

```text
CONSTRUCTION REQUIREMENT
        ↓
BUILDER REQUIREMENT
        ↓
LABOR AUTHORITY
        ↓
BUILDER ASSIGNED
        ↓
CONSTRUCTION EXECUTION
```

Do not allow construction to silently rewrite global labor policy merely because it needs a builder.

Emergency builder allocation may exist, but it must be explicit, bounded, reversible, and attributable.

---

# 10. Placement is its own verification boundary

A building can fail before construction begins because a location is invalid.

Therefore:

```text
RESOURCE FEASIBLE
```

does not imply:

```text
SITE FEASIBLE
```

and:

```text
SITE FEASIBLE
```

does not imply:

```text
PLACEMENT SUCCEEDED
```

The forensic implementation must distinguish at least:

```text
SITE_UNKNOWN
SITE_CANDIDATE
SITE_CHECKING
SITE_VALID
SITE_INVALID
PLACEMENT_REQUESTED
PLACEMENT_ACCEPTED
PLACEMENT_REJECTED
PENDING_OBJECT_OBSERVED
```

Exact engine semantics remain UNCERTAIN until qualified.

Do not infer pending-object or placement success from command acknowledgement alone.

---

# 11. Pending-object state

A pending construction object is an important intermediate evidence boundary.

Conceptually:

```text
COMMAND ISSUED
      ↓
PENDING OBJECT OBSERVED
      ↓
PLACEMENT CONFIRMED
      ↓
BUILDING PROGRESS
      ↓
BUILDING COMPLETED
```

The donor's construction/progression machinery already provides evidence that construction can wait for observed building state before progression advances. Preserve that behavior.

This yields the critical invariant:

> **A construction command may authorize an attempt; only the appropriate observed postcondition may advance the work item.**

---

# 12. Construction completion

Completion must be defined by the requirement, not merely by the command.

Possible postconditions include:

```text
PENDING OBJECT EXISTS
BUILDING COUNT INCREASED
BUILDING INSTANCE IDENTIFIED
BUILDING IS COMPLETE
BUILDING IS OPERATIONAL
REQUIRED CAPABILITY IS AVAILABLE
```

These are not equivalent.

For example, a required production building may need to be operational before the production requirement is considered satisfied.

The verifier must therefore specify the minimum sufficient postcondition for each building class and downstream use.

---

# 13. Rebuild and fallback behavior

The donor contains a documented fallback concept for construction because the ordinary rebuild system can occasionally fail. This is strategically important evidence: the donor recognizes that a nominally valid construction pathway can fail in practice.

The replacement architecture should preserve the **failure recognition**, not blindly preserve an opaque fallback implementation.

Conceptually:

```text
PRIMARY CONSTRUCTION PATH
        ↓
NO EXPECTED POSTCONDITION
        ↓
DIAGNOSE FAILURE
        ↓
RETRY / ALTERNATIVE SITE / ALTERNATIVE BUILDER / FALLBACK
        ↓
OBSERVE
        ↓
VERIFY
```

A fallback must not become an uncontrolled duplicate construction authority.

Every fallback must identify:

- why it activated;
- what state it owns;
- what resources it can consume;
- whether it supersedes the primary transaction;
- how it expires;
- how it reconciles the original transaction;
- what happens to unused escrow.

---

# 14. Retry semantics

A construction failure does not automatically mean the infrastructure requirement failed.

Use separate identities:

```text
R7 = infrastructure requirement
C7 = construction commitment
T7-1 = first transaction
T7-2 = retry transaction
```

If `T7-1` fails:

```text
T7-1 → FAILED / UNVERIFIED
C7 persists
R7 persists
```

A retry creates a new transaction identity rather than overwriting history.

If repeated failures establish infeasibility, the commitment may transition to `BLOCKED`, `FAILED`, `EXPIRED`, `CANCELLED`, or another explicitly authorized terminal state.

There is no justified universal “two failures means abandon” rule.

---

# 15. Partial construction and interruption

Construction may be interrupted after resources have been committed but before the building becomes operational.

Examples include:

- builder reassignment;
- emergency preemption;
- placement invalidation;
- enemy pressure;
- economic reprioritization;
- missing prerequisite;
- transaction failure.

The system must reconcile:

```text
RESOURCE RESERVED
RESOURCE CONSUMED
RESOURCE REMAINING
BUILD PROGRESS
BUILDER OWNERSHIP
BUILDING STATE
```

Never release the entire original reservation merely because the transaction did not complete if some portion has actually been consumed or remains attributable to an active construction commitment.

---

# 16. Infrastructure preemption

Construction can compete with military, food, research, production, and emergency commitments.

Preemption therefore follows the same authority rule established by the broader Shadow architecture:

```text
HIGHER PRIORITY REQUIREMENT
        ↓
SUSPEND LOWER PRIORITY CONSTRUCTION
        ↓
FREEZE NEW FUNDING
        ↓
RECONCILE ATTRIBUTABLE ESCROW
        ↓
EXECUTE HIGHER PRIORITY WORK
        ↓
REASSESS SUSPENDED CONSTRUCTION
```

Preemption must preserve commitment identity and history.

If a building is already physically under construction, the system must not assume that “suspend” means the engine can necessarily pause construction itself. That engine capability is UNCERTAIN until qualified.

The architecture may suspend **new funding/authority** even when physical construction cannot be paused.

---

# 17. Infrastructure dependencies

Buildings frequently form dependency graphs.

Conceptually:

```text
REQUIREMENT A
   ↓
PREREQUISITE BUILDING B
   ↓
TECH / AGE / RESOURCE CONDITION
   ↓
BUILDING C
   ↓
CAPABILITY
```

Dependency state must distinguish:

```text
REQUIRED
AVAILABLE
COMMITTED
UNDER CONSTRUCTION
VERIFIED
INVALIDATED
```

A downstream commitment must not count an unverified prerequisite as operational capability.

This is particularly important for production and research infrastructure.

---

# 18. Building count is not always capability count

A raw building count is an observation, not necessarily a capability proof.

Examples:

```text
COUNT = 2
```

may still fail to establish:

```text
CAPABILITY = AVAILABLE
```

if buildings are incomplete, inaccessible, disabled, strategically invalid, or otherwise unable to satisfy the requirement.

Therefore construction verification should expose both:

```text
VERIFIED_BUILDING_COUNT
```

and, where required:

```text
VERIFIED_OPERATIONAL_CAPABILITY
```

The distinction is an AEGIS-GENERALIZATION pending exact donor/runtime qualification.

---

# 19. Construction deadlock

Construction deadlock occurs when a requirement waits on resources or labor that it indirectly prevents from becoming available.

Examples:

```text
NEED FARM
→ NEED WOOD
→ TOO MANY VILLAGERS REQUIRED ELSEWHERE
→ WOOD DEFICIT
→ FOOD DEFICIT
→ MORE FOOD WORKERS
→ FARM STILL UNFUNDED
```

or:

```text
NEED PRODUCTION BUILDING
→ NEED WOOD
→ WOOD RESERVED FOR FARM
→ FARM WAITING ON BUILDER
→ BUILDER RESERVED ELSEWHERE
```

System 07 must expose construction starvation/deadlock indicators to the economic arbitration layer rather than recursively increasing its own priority.

Useful diagnostics include:

- construction starvation age;
- oldest construction commitment;
- resources unavailable due to other commitments;
- builder starvation age;
- site-failure count;
- prerequisite wait age;
- transaction retry count;
- reservation age;
- blocked duration.

These are AEGIS-GENERALIZATION unless donor-native equivalents are recovered.

---

# 20. Food integration

System 05 may generate a farm infrastructure requirement when natural food continuity is insufficient.

The correct interface is:

```text
FOOD CONTINUITY DEFICIT
        ↓
FARM REQUIREMENT
        ↓
SYSTEM 07 CONSTRUCTION
        ↓
FARM VERIFIED
        ↓
SYSTEM 05 FOOD LOGISTICS REASSESSMENT
```

System 07 does not decide that farms are strategically desirable independently of the food requirement.

Similarly, the completion of a farm does not mean food continuity is solved until System 05 observes sufficient operational food flow.

---

# 21. Production integration

Production Authority may require infrastructure such as:

```text
BARRACKS
STABLE
ARCHERY RANGE
SIEGE WORKSHOP
```

System 07 provides the infrastructure transaction. Production Authority remains the owner of production permission.

Correct dependency:

```text
CAPABILITY REQUIREMENT
        ↓
PRODUCTION REQUIREMENT
        ↓
INFRASTRUCTURE DEFICIT
        ↓
CONSTRUCTION COMMITMENT
        ↓
VERIFIED BUILDING
        ↓
PRODUCTION AUTHORITY
        ↓
AIByzBuild
```

Construction must not silently begin producing units because a production building exists.

---

# 22. Research integration

Research may require a prerequisite building.

Correct sequence:

```text
TECH REQUIREMENT
        ↓
PREREQUISITE DEFICIT
        ↓
CONSTRUCTION COMMITMENT
        ↓
VERIFIED INFRASTRUCTURE
        ↓
RESEARCH FEASIBILITY
        ↓
RESEARCH TRANSACTION
```

Again, building completion is evidence that infrastructure is available; it is not evidence that the technology has been researched.

---

# 23. Site selection authority

Site selection is a potentially dangerous authority boundary because placement geometry can encode strategic policy.

The construction layer should distinguish:

```text
SITE FEASIBILITY
```
from:

```text
SITE PREFERENCE
```

and from:

```text
STRATEGIC SITE OBJECTIVE
```

A construction executor may determine whether a proposed site is legal or physically workable. It should not silently decide that a forward castle, defensive wall, production cluster, or economic structure is strategically preferable unless that authority is explicitly assigned.

The donor's exact site-selection predicates, coordinates, geometric constants, and rule ordering must be extracted before transplant.

---

# 24. Placement geometry forensic requirements

For every donor construction rule, extract:

1. building type;
2. placement origin;
3. coordinate source;
4. home-relative/world-relative semantics;
5. distance constraints;
6. adjacency constraints;
7. terrain constraints;
8. obstruction tests;
9. map-specific conditions;
10. builder-location interaction;
11. retry geometry;
12. fallback geometry;
13. constants used;
14. state writers;
15. state readers;
16. jump/order effects;
17. completion predicate.

Do not assume that a numeric coordinate offset is a generic “best placement” rule. It may be donor-specific, map-specific, generation-specific, or an implementation workaround.

---

# 25. Construction authority matrix

Muse should produce an explicit matrix for every construction target.

Minimum columns:

| Target | Requirement writer | Commitment owner | Resource authority | Builder authority | Site authority | Executor | Completion verifier | Failure owner | Preemption owner |
|---|---|---|---|---|---|---|---|---|---|
| Farm | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| Barracks | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| Stable | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| Archery Range | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| Siege Workshop | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| Monastery | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| Market | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| University | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |
| House | TBD | TBD | Shadow | System 06 / construction interface | TBD | AIByzBuild / construction executor | TBD | TBD | AEGIS / authority layer |

`TBD` is intentional until donor extraction and runtime qualification establish the answer. Do not fill it with assumptions.

---

# 26. State registry requirements

Every critical construction state carrier must be classified using the System 02 registry model.

Required fields include:

```text
SYMBOL
PHYSICAL_CHANNEL
SEMANTIC_TYPE
OWNER
WRITERS
READERS
INITIAL_VALUE
VALID_RANGE
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

Particular attention must be given to:

- `gl-current-build-item`;
- `gl-build-progress`;
- `gl-progression-pause`;
- `gl-escrow-state`;
- building-specific goals/SNs;
- placement coordinates;
- pending-construction state;
- builder identity/count state;
- jump/preemption state.

The exact semantics of these symbols must be recovered from donor writer/reader graphs before implementation claims them as canonical.

---

# 27. Duplicate definitions and conflicting generations

Construction code is particularly vulnerable to duplicated building constants and specialized rules.

For each duplicate definition classify:

```text
LEGITIMATE_CONDITIONAL
LEGITIMATE_SPECIALIZATION
SHADOWED
CONFLICTING
LEGACY
UNKNOWN
```

Never resolve duplicates merely by choosing the last textual definition.

For every conflicting writer establish:

```text
WRITER
CONDITION
RULE ORDER
JUMP EFFECT
VALUE
LIFETIME
READER
STRATEGIC CONSEQUENCE
```

Only then determine whether the duplicate is harmless, necessary, or dangerous.

---

# 28. Construction failure taxonomy

Use distinct failure classes:

```text
NO_REQUIREMENT
NO_RESOURCES
NO_BUILDER
NO_VALID_SITE
PREREQUISITE_MISSING
PREFLIGHT_REJECTED
COMMAND_REJECTED
NO_PENDING_OBJECT
PLACEMENT_FAILED
BUILD_INTERRUPTED
BUILDING_NOT_COMPLETED
BUILDING_NOT_OPERATIONAL
VERIFICATION_TIMEOUT
COMMITMENT_EXPIRED
COMMITMENT_INVALIDATED
PREEMPTED
DEADLOCKED
UNKNOWN
```

Failure classification matters because different failures require different recovery.

For example:

```text
NO_VALID_SITE
```

should not automatically trigger:

```text
MORE_RESOURCES
```

and:

```text
NO_RESOURCES
```

should not automatically trigger:

```text
ALTERNATIVE_SITE
```

---

# 29. Construction verification contract

For each construction target define the smallest sufficient evidence chain.

Minimum conceptual sequence:

```text
COMMAND ACCEPTED
        ↓
PENDING OBJECT OBSERVED
        ↓
PLACEMENT OBSERVED
        ↓
BUILDING OBSERVED
        ↓
COMPLETION OBSERVED
        ↓
OPERATIONAL STATE VERIFIED
```

Not every target requires every stage to be separately represented, but no stage may be silently skipped when downstream correctness depends upon it.

The verifier should report:

```text
PASS
PARTIAL
FAIL
UNKNOWN
```

rather than forcing all outcomes into Boolean success/failure.

---

# 30. Construction telemetry

Telemetry must remain subordinate to authority.

Useful observations include:

- construction request count;
- successful pending-object observations;
- placement failures;
- construction completion latency;
- retry count;
- oldest active construction commitment;
- builder idle/transition time;
- resource reservation age;
- resource waste/release amount;
- prerequisite wait duration;
- verification timeout;
- construction starvation age.

Telemetry is not itself strategic authority unless explicitly promoted through an evidence-qualified control path.

---

# 31. Static versus runtime boundary

### Static evidence can establish

- construction rules exist;
- building predicates exist;
- escrow-aware paths exist;
- `up-build` is referenced;
- fallback/rebuild logic exists;
- building constants exist;
- state writers/readers exist;
- placement geometry is encoded;
- progression references construction state.

### Runtime evidence must establish

- the rule is selected;
- the command is issued;
- resources actually mutate;
- a builder is assigned;
- a pending object appears;
- placement succeeds;
- construction progresses;
- the building completes;
- the building becomes operational;
- the requirement is actually satisfied;
- escrow is consumed/released correctly;
- failure/retry paths behave as expected.

The distinction is mandatory.

---

# 32. Qualification sequence

System 07 should be qualified in the following order.

### S7-0 — Static construction inventory

Extract every construction command, building target, prerequisite, coordinate source, geometry predicate, escrow path, fallback, jump, progression write, and completion predicate.

### S7-1 — State ownership

Build the writer/reader/precedence graph for construction state.

### S7-2 — Economic transaction qualification

Qualify resource reservation → affordability → `up-build` interaction.

### S7-3 — Builder qualification

Establish the relationship between construction authority and worker assignment.

### S7-4 — Placement qualification

Establish the actual engine-visible boundary between command, pending object, and valid placement.

### S7-5 — Completion qualification

Establish building-count and/or operational-state evidence sufficient for completion.

### S7-6 — Failure/retry qualification

Qualify no-site, no-builder, rejected-command, interrupted-build, and verification-timeout behavior.

### S7-7 — Dependency qualification

Qualify infrastructure prerequisites and downstream capability consumers.

### S7-8 — Strategic/economic integration

Demonstrate one complete requirement → construction → verified capability → reassessment loop.

Do not broaden implementation before S7-5 is stable.

---

# 33. First vertical slice

The first implementation/qualification slice should be **one civilian infrastructure requirement with a simple placement path**.

Preferred candidate:

```text
FOOD CONTINUITY REQUIREMENT
        ↓
FARM REQUIREMENT
        ↓
WOOD COMMITMENT
        ↓
BUILDER ASSIGNMENT
        ↓
CAN-BUILD-WITH-ESCROW
        ↓
UP-BUILD
        ↓
PENDING FARM OBSERVED
        ↓
FARM COMPLETED
        ↓
FARM VERIFIED
        ↓
ESCROW RECONCILED
        ↓
FOOD LOGISTICS REASSESSMENT
```

This slice deliberately crosses Systems 05, 06, and 07 while remaining economically and strategically comprehensible.

If farm placement has unresolved engine semantics, use the simplest donor-qualified building target rather than inventing a placement abstraction.

---

# 34. Donor preservation / improvement disposition

| Donor mechanism | Disposition | Reason |
|---|---|---|
| Escrow-aware construction | PRESERVE / FORMALIZE | Valuable economic transaction interface |
| `can-build-with-escrow` | PRESERVE / QUALIFY | Feasibility boundary |
| `up-build` | PRESERVE / FORMALIZE | Execution interface, not strategic authority |
| `gl-current-build-item` | PRESERVE / REFACTOR | Work-item identity |
| `gl-build-progress` | PRESERVE / REFACTOR | Progress cursor |
| `gl-progression-pause` | PRESERVE / REFACTOR | Pending/suspended progression |
| Building prerequisites | PRESERVE / EXPLICITATE | Dependency knowledge |
| Rebuild fallback | PRESERVE / FORMALIZE | Evidence of real failure handling |
| Rule-order construction priority | EXTRACT / EXPLICITATE | Hidden authority boundary |
| `up-jump-rule` effects | EXTRACT / BOUND | Preemption mechanism |
| Placement constants | PRESERVE PENDING QUALIFICATION | Semantic meaning may be donor-specific |
| Duplicate constants | CLASSIFY / QUARANTINE | Namespace ambiguity |
| Direct strategic side effects | REMOVE / SUBORDINATE | Construction must not become strategic planner |
| Unverified completion assumptions | REPLACE | Violates epistemic boundary |

---

# 35. Anti-patterns

The following are prohibited:

1. `build` command = completed building.
2. resource affordability = construction success.
3. valid coordinates = placement success.
4. building count = operational capability without qualification.
5. builder assigned = productive construction.
6. construction failure = strategic failure.
7. two failed attempts = automatic abandonment.
8. fallback executor = second hidden authority.
9. construction priority = strategic priority.
10. site geometry = strategic doctrine without explicit authority.
11. static reachability = runtime qualification.
12. duplicate constants resolved by textual last-writer assumption.
13. resource release without ownership attribution.
14. construction bypasses that silently evade Production/Commitment Authority.
15. emergency construction that never returns to normal arbitration.
16. deleting donor fallback behavior before understanding why it exists.

---

# 36. Hard invariants

**CN-01 — Requirement separation:** infrastructure requirement is distinct from building command.

**CN-02 — Identity separation:** requirement, building type, building instance, site, and transaction are distinct identities.

**CN-03 — Funding attribution:** every construction reservation has an attributable owner and purpose.

**CN-04 — Placement separation:** resource feasibility does not imply site feasibility.

**CN-05 — Command separation:** command issuance does not imply pending-object observation.

**CN-06 — Completion separation:** pending-object observation does not imply completed building.

**CN-07 — Capability separation:** completed building does not automatically imply every downstream capability is verified.

**CN-08 — Progression integrity:** no work-item progress advance without the required postcondition.

**CN-09 — Retry integrity:** retries receive distinct transaction identity.

**CN-10 — Failure separation:** transaction failure, construction failure, commitment failure, and strategic failure are distinct states.

**CN-11 — Builder boundary:** construction cannot silently rewrite global labor authority.

**CN-12 — Strategic boundary:** construction cannot silently become strategic objective selection.

**CN-13 — Preemption integrity:** preemption preserves commitment history and reconciles resources.

**CN-14 — Fallback integrity:** fallback cannot create an untracked duplicate executor.

**CN-15 — Static/runtime boundary:** source existence is not runtime proof.

**CN-16 — Evidence integrity:** unknown engine semantics remain unknown until qualified.

**CN-17 — Dependency integrity:** unverified prerequisites cannot be counted as verified infrastructure capability.

**CN-18 — Resource integrity:** unused transaction resources are reconciled explicitly.

---

# 37. Definition of done

System 07 is not complete until the forensic/engineering record can answer, for every significant construction target:

1. Who requests the infrastructure?
2. Who owns the commitment?
3. What capability does the building satisfy?
4. What is the verified infrastructure deficit?
5. What resources are required?
6. Which escrow mechanism protects those resources?
7. Who owns builder assignment?
8. Who determines site validity?
9. What exact executor issues construction?
10. What constitutes command acceptance?
11. What constitutes pending-object observation?
12. What constitutes placement success?
13. What constitutes completion?
14. What constitutes operational capability?
15. What happens when placement fails?
16. What happens when the builder disappears?
17. What happens when the command is rejected?
18. What happens on retry?
19. What happens to unused escrow?
20. What event advances progression?
21. What event satisfies the requirement?
22. What event invalidates the requirement?
23. Who may preempt construction?
24. How is preemption reconciled?
25. Which legacy bypasses remain?
26. Which donor constants remain unexplained?
27. Which semantics are static only?
28. Which runtime behaviors remain unqualified?
29. What is the smallest complete vertical slice?
30. What evidence demonstrates that slice actually works?

If these questions cannot be answered, System 07 remains forensic-incomplete regardless of how much `.per` code exists.

---

# 38. Final engineering directive

Do not build Shadow construction as a collection of `build` rules.

Build it as a **verifiable infrastructure transaction boundary**.

The intended architecture is:

```text
REQUIREMENT
   ↓
CAPABILITY DEFICIT
   ↓
CONSTRUCTION COMMITMENT
   ↓
RESOURCE RESERVATION
   ↓
FEASIBILITY
   ↓
BUILDER / SITE AUTHORIZATION
   ↓
EXECUTION
   ↓
PENDING OBJECT
   ↓
PLACEMENT / BUILD PROGRESS
   ↓
COMPLETION
   ↓
OPERATIONAL VERIFICATION
   ↓
RESOURCE RECONCILIATION
   ↓
CAPABILITY UPDATE
   ↓
REASSESSMENT
```

Muse is responsible for determining the exact `.per` realization. The engineering requirement is that the implementation preserve the donor's useful construction knowledge while improving **ownership, attribution, placement semantics, retry integrity, failure classification, verification, preemption, and strategic separation**.

Do not optimize the appearance of the construction code. Optimize the reliability of the control boundary it represents.

---

## Appendix A — System sequence

```text
01 INITIALIZATION / CONFIGURATION
        ↓
02 STATE NAMESPACE / AUTHORITY
        ↓
03 TARGET ACQUISITION
        ↓
04 SCOUTING / INFORMATION ACQUISITION
        ↓
05 FOOD LOGISTICS / CONTINUITY
        ↓
06 VILLAGER ECONOMY / LABOR ALLOCATION
        ↓
07 CONSTRUCTION / INFRASTRUCTURE
        ↓
08 [NEXT SYSTEM]
```

System 07 consumes explicit economic/labor requirements from Systems 05–06 and exposes **verified infrastructure capability** to production, research, food, and higher-level strategic arbitration.

## Appendix B — Canonical construction loop

```text
OBSERVATION / REQUIREMENT
→ CLASSIFY
→ DEFINE INFRASTRUCTURE DEFICIT
→ COMMIT
→ RESERVE
→ PREFLIGHT
→ AUTHORIZE
→ SELECT BUILDER / SITE
→ ISSUE
→ OBSERVE PENDING OBJECT
→ OBSERVE BUILDING
→ VERIFY COMPLETION
→ RECONCILE ESCROW
→ SATISFY REQUIREMENT
→ REASSESS
```

The central invariant remains:

> **Construction is not complete when the command is issued. Construction is complete when the required world-state postcondition has been observed and verified.**
