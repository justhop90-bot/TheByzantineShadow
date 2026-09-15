# The Byzantine Shadow — System 06: Villager Economy & Labor Allocation Forensics v0.1

**Status:** Forensic engineering specification  
**System:** 06 — Villager Economy / Labor Allocation  
**Predecessors:** System 01 — Initialization / Configuration; System 02 — State Namespace / Authority; System 03 — Target Acquisition; System 04 — Scouting / Information Acquisition; System 05 — Food Logistics / Food Continuity  
**Primary disposition:** PRESERVE + FORMALIZE + IMPROVE  
**Evidence standard:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN  
**Source donor:** `Shadow DC7(1).per`  
**Source SHA-256:** `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`  
**Donor baseline:** 22,603 lines; 1,956 rules; 1,503 constants; 1,193 goal writes; 440 strategic-number writes; 188 jump calls.  

---

# 0. Purpose and forensic standard

System 06 isolates the donor's **villager economy and labor-allocation subsystem**: the machinery that turns resource requirements into civilian-worker allocation, changes worker distribution among food/wood/gold/stone and infrastructure tasks, maintains economic thresholds, reacts to shortages and surpluses, and supplies the production/construction/research systems with the labor and resource conditions required for execution.

The donor-wide forensic decomposition identifies **villager economy** as a distinct system alongside food logistics, scouting, target acquisition, strategy, enemy inference, threat/defense, composition, tactical missions, progression, escrow, research, construction, market balancing, emergency response, telemetry, and rule-order arbitration. The economic audit further establishes that the donor couples resource saving to progression/work-item state and uses affordability as a feasibility gate rather than proof of strategic correctness or completion.

System 05 established that food logistics is a specialized continuity controller. System 06 now moves one level upward and examines the **labor market that makes the resource system possible**.

The forensic objective is not to invent a generic villager allocator. It is to recover the donor's actual worker-allocation mechanisms, identify what is controlled by raw resource thresholds versus progression requirements, expose hidden ownership and precedence, distinguish assignment from productivity, and define an AEGIS-compatible economic labor interface.

**Forensic rule:** static presence establishes code/state existence only. It does not establish runtime reachability, writer precedence, actual worker reassignment, gather productivity, economic optimality, strategic success, or compatibility with the current AoE2DE runtime.

---

# 1. Executive finding

The villager economy should be treated as a **resource-production and labor-allocation control system**, not as a table of desired villager counts.

The core control problem is:

```text
RESOURCE / CAPABILITY REQUIREMENT
          ↓
ECONOMIC DEMAND
          ↓
CURRENT SUPPLY / PRODUCTION STATE
          ↓
LABOR DEFICIT OR SURPLUS
          ↓
WORKER ALLOCATION
          ↓
EXECUTION / TRAVEL / GATHER
          ↓
OBSERVED PRODUCTIVITY
          ↓
RESOURCE STATE UPDATE
          ↓
REASSESSMENT
```

The critical architectural distinction is:

```text
DESIRED ALLOCATION
        ≠
ASSIGNED ALLOCATION
        ≠
PRODUCTIVE ALLOCATION
        ≠
OBSERVED RESOURCE FLOW
```

A villager being assigned to wood does not prove that wood income increased. A villager being counted as a food worker does not prove food continuity improved. A construction assignment does not prove a building was completed.

System 06 therefore becomes the economic **labor-control boundary** between strategic/resource requirements and the concrete villager executor.

**Disposition:** preserve donor worker/resource knowledge; formalize demand and allocation semantics; separate policy from state; add attribution, temporal state, productivity evidence, transition costs, starvation observability, and bounded emergency behavior; qualify a minimal labor loop before broad redesign.

---

# 2. System boundary

## 2.1 In scope

System 06 owns forensic analysis and future interface design for:

1. villager population state;
2. civilian-worker allocation;
3. resource worker targets;
4. food/wood/gold/stone allocation;
5. construction worker allocation;
6. repair/build labor where economically relevant;
7. worker reassignment;
8. worker transition state;
9. resource-income observation;
10. resource demand estimation;
11. economic deficits and surpluses;
12. economic timing/thresholds;
13. worker availability;
14. idle/unproductive worker detection;
15. labor starvation;
16. infrastructure-dependent labor allocation;
17. interaction with food continuity;
18. interaction with escrow and commitments;
19. interaction with production/research/construction requirements;
20. economic telemetry and starvation/deadlock indicators.

## 2.2 Explicitly out of scope

System 06 does not own:

- strategic doctrine selection;
- target-player selection;
- scouting movement;
- military composition selection;
- strategic commitment selection;
- production authority;
- concrete unit training execution;
- complete building placement/execution;
- market strategy as a whole;
- strategic threat valuation;
- final tactical control.

System 06 may expose economic feasibility and labor requirements to those systems. It must not silently become their strategic decision-maker.

---

# 3. Forensic basis

The donor-wide forensic decomposition identifies villager economy as a distinct machine. The economic audit establishes that the donor contains resource saving, escrow-aware affordability, transaction sequencing, construction, research, production, market balancing and progression machinery. These systems necessarily interact with labor allocation, but interaction must not be mistaken for ownership.

The food-logistics forensic specification established a critical lower-layer boundary: food logistics determines how food continuity is maintained; villager economy determines how available civilian labor is allocated to satisfy resource requirements, including food requirements supplied by System 05.

The strategic audit establishes the higher-level replacement target:

```text
OBSERVATION → BELIEF → THREAT / OPPORTUNITY → OBJECTIVE → CAPABILITY → PRIORITY → COMMITMENT → SHADOW ECONOMIC SUBSTRATE
```

System 06 sits inside the economic substrate. Its job is to make the chosen economic requirements physically productive, not to decide which strategic requirement should exist.

---

# 4. Labor allocation is a control loop

The canonical System 06 model is:

```text
ECONOMIC REQUIREMENT
        ↓
RESOURCE DEMAND
        ↓
CURRENT VERIFIED SUPPLY
        ↓
PROJECTED DEFICIT / SURPLUS
        ↓
TARGET LABOR ALLOCATION
        ↓
AVAILABLE WORKERS
        ↓
ALLOCATION DECISION
        ↓
WORKER TRANSITION
        ↓
OBSERVED PRODUCTIVITY
        ↓
RESOURCE FLOW
        ↓
REASSESSMENT
```

This must remain distinct from the command/execution layer.

System 06 answers:

> **How should civilian labor be distributed to satisfy authorized economic requirements?**

Shadow commitment/transaction machinery answers:

> **Which resources are protected, reserved, and made transactionally available?**

AIByzBuild or the relevant executor answers:

> **How is the concrete villager action issued?**

Verification answers:

> **Did the expected economic state actually change?**

---

# 5. Resource stock is not resource income

The economy must distinguish instantaneous stock from production flow.

Minimum conceptual dimensions:

```text
FOOD_STOCK
WOOD_STOCK
GOLD_STOCK
STONE_STOCK

FOOD_INCOME
WOOD_INCOME
GOLD_INCOME
STONE_INCOME

FOOD_DEMAND
WOOD_DEMAND
GOLD_DEMAND
STONE_DEMAND
```

A large stock can conceal a collapsing income rate. A low stock can be acceptable when a large committed transaction is already funded and verified income is recovering.

Therefore a labor allocator should not react mechanically to:

```text
resource < threshold → add villager
```

without considering:

- current commitments;
- protected escrow;
- pending transactions;
- expected consumption;
- verified income;
- worker transition cost;
- infrastructure availability;
- strategic urgency supplied from above.

This flow-oriented model is an **AEGIS-GENERALIZATION** until each donor component is statically traced.

---

# 6. Economic demand must be explicit

Labor allocation becomes unstable when every subsystem independently writes desired resource-worker counts.

The stronger interface is:

```text
DEMAND SOURCE
  ↓
RESOURCE REQUIREMENT
  ↓
REQUIRED RATE / AMOUNT
  ↓
DEADLINE / HORIZON
  ↓
PRIORITY CONTEXT
  ↓
LABOR REQUIREMENT
```

Demand sources may include:

- villager production;
- military production;
- research;
- construction;
- farms/food continuity;
- existing commitments;
- emergency survival requirements;
- recovery from economic deficits.

The labor system should consume these requirements rather than infer strategic purpose from a raw resource deficit whenever possible.

---

# 7. Demand and commitment are different

A resource demand is not automatically a strategic commitment.

For example:

```text
WOOD DEMAND = 300
```

may originate from:

- several routine houses;
- a farm transition;
- a strategic military commitment;
- an emergency defensive structure;
- a technology;
- an unowned legacy branch.

System 06 must preserve attribution where the upstream system provides it.

Conceptually:

```text
COMMITMENT_ID
OBJECTIVE
REQUIREMENT
RESOURCE
AMOUNT
DEADLINE
PRIORITY
OWNER
```

The allocator then computes labor consequences without assuming ownership of the strategic commitment itself.

---

# 8. Worker-state taxonomy

A raw `villager-count` is insufficient for labor control.

At minimum distinguish:

```text
TOTAL_CIVILIANS
AVAILABLE_CIVILIANS
ASSIGNED_FOOD
ASSIGNED_WOOD
ASSIGNED_GOLD
ASSIGNED_STONE
ASSIGNED_BUILDING
ASSIGNED_REPAIR
TRANSITIONING
IDLE
UNAVAILABLE
DEAD / LOST
```

Where possible, also distinguish productive state:

```text
PRODUCTIVE
TRAVELING
BLOCKED
WAITING
SOURCE_EXHAUSTED
INFRASTRUCTURE_BLOCKED
UNKNOWN
```

These states have different economic meanings.

A worker assigned to gold but waiting for a mining camp is not equivalent to a productive gold miner.

---

# 9. Desired workers versus productive workers

This is a primary System 06 invariant.

```text
DESIRED_WOOD_WORKERS = 8
ASSIGNED_WOOD_WORKERS = 8
PRODUCTIVE_WOOD_WORKERS = 3
```

does not constitute an eight-worker wood economy.

Likewise:

```text
DESIRED_FOOD_WORKERS = 10
ASSIGNED_FOOD_WORKERS = 10
```

does not prove that food continuity is adequate.

The labor controller should therefore expose at least:

```text
TARGET_ALLOCATION
ASSIGNED_ALLOCATION
OBSERVED_PRODUCTIVE_ALLOCATION
```

The difference between them is operationally meaningful.

---

# 10. Worker transition is a real economic cost

Changing worker assignments has a temporal cost.

A worker moving:

```text
WOOD → GOLD
```

is unavailable for productive gathering during the transition.

The allocator must therefore avoid pathological oscillation such as:

```text
FOOD SHORTAGE
→ move wood worker to food
→ wood shortage
→ move food worker to wood
→ food shortage
→ repeat
```

The correct architecture requires hysteresis and, where practical, minimum dwell time.

This is **AEGIS-GENERALIZATION** unless the donor's exact transition mechanism is recovered.

---

# 11. Allocation should be driven by marginal economic need

The labor system should not attempt to maximize every resource simultaneously.

A useful conceptual abstraction is:

```text
RESOURCE_DEFICIT
= REQUIRED_RESOURCE_FLOW
  − VERIFIED_RESOURCE_FLOW
```

and then:

```text
LABOR_REQUIREMENT
≈ deficit adjusted by
   worker productivity
   source accessibility
   transition cost
   infrastructure readiness
   deadline
   commitment priority
```

This is not a proposed engine formula. It is an analytical model for determining whether the donor's existing worker rules can be improved without destroying their useful empirical behavior.

The donor's actual coefficients, thresholds, and allocation rules must be extracted before replacing them.

---

# 12. Food interface

System 05 produces food-continuity requirements.

System 06 consumes those requirements and allocates civilian labor accordingly.

The interface should conceptually be:

```text
SYSTEM 05
FOOD REQUIREMENT
      ↓
SYSTEM 06
FOOD LABOR TARGET
      ↓
WORKER ALLOCATION
      ↓
SYSTEM 05
FOOD PRODUCTIVITY / CONTINUITY OBSERVATION
      ↓
SYSTEM 06 REASSESSMENT
```

System 06 must not duplicate sheep/luring/forage/farm source-selection logic merely to determine which villagers should gather food.

Conversely, System 05 should not directly rewrite global worker allocation without passing through the labor authority boundary.

---

# 13. Wood is infrastructure-sensitive labor

Wood demand has a distinctive property: it often represents **future production capacity**, not merely current consumption.

Wood may be required for:

- houses;
- camps;
- farms;
- military buildings;
- economic buildings;
- walls and defensive structures;
- production infrastructure;
- technology/progression prerequisites.

Therefore a wood deficit can be either:

```text
CURRENT OPERATING DEFICIT
```

or:

```text
FUTURE CAPACITY / COMMITMENT REQUIREMENT
```

The labor allocator should preserve upstream attribution where possible.

A strategic commitment to infrastructure may justify temporary wood prioritization; routine wood demand should not automatically preempt higher-priority protected commitments.

---

# 14. Gold and stone are commitment-sensitive resources

Gold and stone frequently support discrete high-value transactions.

Consequently the labor allocator should interact with commitment state rather than merely chase instantaneous stock thresholds.

Conceptually:

```text
GOLD / STONE COMMITMENT
       ↓
REQUIRED AMOUNT
       ↓
PROTECTED / UNPROTECTED PORTION
       ↓
REQUIRED INCOME RATE
       ↓
LABOR ALLOCATION
```

A fully funded commitment should not continue attracting labor indefinitely merely because the raw resource remains below an unrelated threshold.

Likewise, a large unprotected stockpile does not necessarily eliminate the need to produce the resource if a future authorized requirement has a deadline.

---

# 15. Infrastructure readiness is part of labor feasibility

Worker allocation depends on infrastructure state.

Conceptually:

```text
LABOR REQUIREMENT
      ↓
SOURCE / BUILDING REQUIREMENT
      ↓
INFRASTRUCTURE READY?
      ↓
YES → ASSIGN
NO  → DECLARE INFRASTRUCTURE REQUIREMENT
```

Examples:

- gold workers may require a mining camp;
- food workers may require a mill/farm infrastructure;
- wood workers require accessible wood;
- construction labor requires an executable building transaction.

The allocator should not falsely report labor capacity when the required infrastructure is absent or non-operational.

Construction remains a separate execution system; System 06 declares the dependency.

---

# 16. Idle-worker control

Idle civilians represent lost economic capacity and should be treated as an explicit operational state.

However:

```text
IDLE
```

is not automatically equivalent to:

```text
MISALLOCATED
```

A worker may be intentionally idle because:

- the current source is exhausted;
- a construction assignment is pending;
- a higher-priority reassignment is being prepared;
- the worker is transitioning;
- no valid economic assignment exists;
- the economy is temporarily saturated.

Therefore idle-worker correction must be classified by cause before forcing reassignment.

---

# 17. Worker starvation and economic starvation

The labor system requires multiple starvation indicators.

At minimum:

```text
FOOD_LABOR_STARVATION_AGE
WOOD_LABOR_STARVATION_AGE
GOLD_LABOR_STARVATION_AGE
STONE_LABOR_STARVATION_AGE
INFRASTRUCTURE_LABOR_STARVATION_AGE
COMMITMENT_FUNDING_STARVATION_AGE
IDLE_WORKER_AGE
```

A resource is economically starved when the system has an unresolved requirement but cannot obtain sufficient productive labor or infrastructure to satisfy it.

This is distinct from:

```text
RESOURCE STOCK = LOW
```

and from:

```text
RESOURCE INCOME = LOW
```

The distinction permits better diagnosis of whether the problem is:

- insufficient workers;
- poor source access;
- missing infrastructure;
- resource depletion;
- commitment competition;
- strategic overcommitment;
- executor failure.

---

# 18. Escrow and labor allocation

Escrow changes the meaning of apparent resource availability.

The economic audit establishes percentage escrow, direct escrow modification, releases, escrow-aware affordability, and transaction sequencing. It also establishes that escrow is an economic commitment-enforcement mechanism rather than a strategic decision-maker.

Therefore the labor allocator should reason over at least:

```text
GROSS RESOURCE
POLICY-PROTECTED RESOURCE
COMMITMENT-RESERVED RESOURCE
TRANSACTION-AVAILABLE RESOURCE
```

These are conceptual AEGIS accounting states until engine-level semantics are qualified.

A labor reallocation that increases current income must not silently consume the resources protected for an authorized higher-priority commitment.

Conversely, stale or abandoned commitments must not permanently distort labor policy through resources that are no longer legitimately protected.

---

# 19. Economic hysteresis

Labor allocation is particularly vulnerable to oscillation because resource values change continuously.

Each major resource allocation policy should therefore have, where applicable:

```text
ACTIVATION THRESHOLD
MAINTENANCE THRESHOLD
RELEASE THRESHOLD
SWITCH MARGIN
MINIMUM DWELL TIME
MINIMUM VIABLE ALLOCATION
MAXIMUM STALE ALLOCATION AGE
```

Conceptual rule:

```text
switch allocation only when
new requirement materially exceeds
current requirement
```

or when the current allocation is invalid, infeasible, emergency-preempted, or strategically superseded.

Do not invent arbitrary numerical hysteresis coefficients before extracting donor behavior.

---

# 20. Emergency labor policy

Emergency states can legitimately invert normal labor priorities.

For example:

```text
NORMAL
  ↓
SURVIVAL THREAT
  ↓
PROTECT ESSENTIAL CAPABILITY
  ↓
TEMPORARY LABOR REALLOCATION
  ↓
VERIFY THREAT STATE
  ↓
RESTORE / REASSESS
```

The military audit establishes that town safety and defensive state can alter military and economic behavior and that survival has priority-inversion authority over normal economic behavior.

The correct implementation boundary is:

```text
THREAT AUTHORITY
      ↓
EMERGENCY ECONOMIC REQUIREMENT
      ↓
SYSTEM 06 LABOR REALLOCATION
```

not:

```text
SYSTEM 06 OBSERVES LOW RESOURCE
      ↓
SYSTEM 06 INVENTS MILITARY STRATEGY
```

Emergency authority must be bounded, attributable, reversible, and observable.

---

# 21. Market interaction

Market behavior changes effective resource availability but should not be collapsed into labor allocation.

The economic audit identifies age-sensitive need/excess/trading thresholds and classifies market behavior as liquidity management rather than an independent strategic objective.

The correct interface is:

```text
RESOURCE DEFICIT / EXCESS
        ↓
MARKET FEASIBILITY / POLICY
        ↓
EFFECTIVE RESOURCE STATE
        ↓
LABOR ALLOCATION REASSESSMENT
```

A market transaction can temporarily change the need for a resource without changing the underlying labor requirements that support long-term production.

System 06 should consume verified post-market resource state rather than assume that a trade command permanently solved an economic deficit.

---

# 22. Villager production itself is a resource commitment

Producing another villager has an economic cost and creates future labor capacity.

Therefore civilian production belongs on the same commitment/transaction continuum as other economic actions:

```text
LABOR CAPACITY REQUIREMENT
      ↓
VILLAGER PRODUCTION REQUIREMENT
      ↓
RESOURCE REQUIREMENT
      ↓
COMMITMENT / TRANSACTION
      ↓
PRODUCTION AUTHORITY
      ↓
VILLAGER TRAINING
      ↓
OBSERVED VILLAGER COUNT / STATE
      ↓
AVAILABLE LABOR CAPACITY
```

This does not mean System 06 should own production authority. It means the labor system must expose when worker capacity is insufficient for authorized economic requirements.

A newly trained villager is not automatically productive until assigned, reaches a valid source/task, and produces observable economic work.

---

# 23. Labor allocation and strategic commitments

The correct strategic bridge is:

```text
AEGIS
  ↓
STRATEGIC COMMITMENT
  ↓
RESOURCE REQUIREMENT
  ↓
SHADOW ECONOMIC SUBSTRATE
  ↓
LABOR REQUIREMENT
  ↓
SYSTEM 06
  ↓
PRODUCTIVE RESOURCE FLOW
```

The labor system should not answer:

> Which military capability should Byzantines choose?

It should answer:

> Given the authorized requirement, what civilian labor distribution is necessary and feasible to fund it without violating higher-priority reservations?

This boundary is central to preventing the economic subsystem from becoming a second strategic brain.

---

# 24. Canonical labor-allocation state contract

Muse should establish a canonical semantic record for each major labor-allocation decision.

Minimum conceptual fields:

```text
ALLOCATION_ID
RESOURCE_CLASS
REQUIREMENT_ID
COMMITMENT_ID
TARGET_WORKERS
ASSIGNED_WORKERS
PRODUCTIVE_WORKERS
AVAILABLE_WORKERS
RESOURCE_DEMAND
RESOURCE_SUPPLY_RATE
RESOURCE_DEFICIT
SOURCE_VALID
SOURCE_ACCESSIBLE
INFRASTRUCTURE_READY
TRANSITION_COST
PRIORITY_CONTEXT
CREATION_EPOCH
LAST_UPDATE_EPOCH
EXPIRY
GENERATION
OWNER
EVIDENCE_LEVEL
```

Not every field must become a literal `.per` slot. The semantic distinction must survive implementation.

Critical fields must have explicit ownership and lifetime.

---

# 25. Labor allocation lifecycle

A canonical allocation should follow:

```text
REQUIREMENT_CREATED
      ↓
ALLOCATION_REQUESTED
      ↓
ALLOCATION_AUTHORIZED
      ↓
WORKERS_SELECTED
      ↓
ASSIGNMENT_ISSUED
      ↓
TRANSITIONING
      ↓
ASSIGNED
      ↓
PRODUCTIVITY_OBSERVED
      ↓
PRODUCTIVE
      ↓
MAINTAIN / REBALANCE
      ↓
RELEASE / REASSIGN
      ↓
VERIFIED_RELEASED
```

Exceptional states include:

```text
BLOCKED
INVALIDATED
PREEMPTED
FAILED
STALE
EXPIRED
UNKNOWN
```

The donor may compress several stages. The forensic task is to identify where those stages are already implicit.

---

# 26. Assignment completion versus economic completion

This is the System 06 equivalent of the Shadow command-verification invariant.

```text
ASSIGNMENT ISSUED
      ≠
WORKER ARRIVED
      ≠
WORKER GATHERING
      ≠
RESOURCE FLOW VERIFIED
      ≠
REQUIREMENT SATISFIED
```

A worker reassignment should not clear a resource deficit merely because the assignment command was accepted.

The appropriate completion evidence depends on the requirement:

- worker reaches source/task;
- source becomes productive;
- resource income changes;
- required resource accumulation occurs;
- downstream transaction becomes fundable;
- commitment requirement is verified.

This preserves the project's W0/W1/W2/W3 evidence boundary.

---

# 27. Multi-resource arbitration

A single villager cannot simultaneously satisfy every resource deficit.

Therefore System 06 is an allocation arbiter among economic requirements, but it is **not** the strategic arbiter among objectives.

Conceptually:

```text
FOOD REQUIREMENT ─┐
WOOD REQUIREMENT ─┼→ LABOR ALLOCATION → WORKERS
GOLD REQUIREMENT ─┤
STONE REQUIREMENT─┘
```

Inputs to economic allocation may include:

- requirement urgency;
- deadline;
- verified deficit;
- worker productivity;
- transition cost;
- infrastructure readiness;
- existing protected commitments;
- emergency state;
- labor availability.

Strategic priority may be supplied as context but should not be reconstructed from raw resource values alone.

---

# 28. Duplicate writers and namespace hazards

Because the donor uses a large distributed namespace and substantial rule-order arbitration, every worker-allocation state must be traced for:

- duplicate definitions;
- multiple writers;
- conditional writers;
- reset rules;
- jump interactions;
- source-order precedence;
- legacy branches;
- civilization/map specialization;
- ordinary versus escrow-aware paths;
- hidden writes from unrelated economic modules.

Classify each writer as:

```text
PRIMARY_OWNER
AUTHORIZED_CONTRIBUTOR
DERIVED_WRITER
EMERGENCY_WRITER
LEGACY_WRITER
CONFLICTING_WRITER
UNKNOWN_WRITER
```

Do not merge duplicate worker goals merely because their names appear equivalent.

---

# 29. Required static forensic extraction

Before implementation, extract every relevant donor mechanism.

For each worker-allocation rule record:

1. file/section/rule identity;
2. resource class;
3. inputs;
4. conditions;
5. state reads;
6. state writes;
7. desired worker calculation;
8. assignment operation;
9. productivity observation;
10. source/infrastructure dependency;
11. timer dependency;
12. jump/preemption effect;
13. escrow interaction;
14. progression interaction;
15. market interaction;
16. villager-production interaction;
17. competing writer;
18. source-order dependency;
19. reset/expiry condition;
20. emergency override;
21. evidence classification;
22. runtime qualification status.

The extraction must produce a **writer → state → reader** graph for every critical labor variable.

---

# 30. Static/runtime boundary

Static analysis can establish:

- worker-count variables exist;
- allocation rules exist;
- resource thresholds exist;
- worker assignment commands exist;
- timers exist;
- food/wood/gold/stone branches exist;
- construction and economic dependencies exist;
- rule ordering exists.

Runtime qualification must establish:

- the allocator actually activates;
- the intended writer wins;
- workers actually change assignment;
- workers reach valid sources/tasks;
- productive gathering occurs;
- resource flow changes;
- the allocation persists appropriately;
- stale allocation is corrected;
- competing requirements arbitrate correctly;
- emergency reallocation recovers correctly;
- downstream commitments benefit.

Static existence is therefore never sufficient to claim economic competence.

---

# 31. Qualification sequence

System 06 qualification should proceed in narrow slices.

### V6-0 — Static inventory

Extract all worker/resource goals, constants, allocation rules, timers, assignment operations, resets, duplicates, and jump dependencies.

### V6-1 — Ownership graph

Determine authoritative writer and readers for each critical worker-allocation state.

### V6-2 — Single-resource allocation

Qualify one resource allocation from requirement through assignment and observed productivity.

Preferred first candidate: **wood**, because it interacts with infrastructure and multiple downstream requirements without requiring the full food-source architecture.

### V6-3 — Food interface

Connect System 05 food continuity requirement to System 06 labor allocation and verify the closed loop.

### V6-4 — Multi-resource arbitration

Qualify competition among at least two resource requirements.

### V6-5 — Infrastructure dependency

Demonstrate that labor allocation recognizes unavailable/unfinished infrastructure rather than falsely claiming productivity.

### V6-6 — Commitment interaction

Verify that labor allocation respects attributable escrow/commitment reservations.

### V6-7 — Hysteresis

Qualify resistance to rapid allocation oscillation.

### V6-8 — Emergency policy

Qualify bounded survival-driven reallocation and restoration.

### V6-9 — Strategic integration

Only after the lower economic loop is qualified, connect an AEGIS commitment to a resource/labor requirement and verify downstream effect.

---

# 32. First implementation slice

The preferred first complete slice is:

```text
AUTHORIZED ECONOMIC REQUIREMENT
        ↓
WOOD DEFICIT
        ↓
TARGET WOOD LABOR
        ↓
AVAILABLE VILLAGER
        ↓
ASSIGN TO WOOD
        ↓
OBSERVE PRODUCTIVE WOOD GATHERING
        ↓
WOOD FLOW UPDATE
        ↓
DEFICIT REASSESSMENT
```

Do not begin by rewriting the entire villager economy.

The purpose of this slice is to establish that the following distinction is real in implementation:

```text
REQUIREMENT
→ ALLOCATION
→ ASSIGNMENT
→ PRODUCTIVITY
→ ECONOMIC CONSEQUENCE
```

Once that loop is proven, add food integration, then multi-resource arbitration, then commitment-aware labor allocation.

---

# 33. Donor preservation matrix

| Donor mechanism | Initial disposition | Reason |
|---|---|---|
| Resource-specific worker allocation | PRESERVE + FORMALIZE | Core economic knowledge |
| Food worker management | PRESERVE + INTERFACE | System 05 owns food continuity; System 06 owns labor allocation |
| Wood allocation | PRESERVE + IMPROVE | Broad infrastructure interaction |
| Gold allocation | PRESERVE + FORMALIZE | Commitment-sensitive resource |
| Stone allocation | PRESERVE + FORMALIZE | Discrete infrastructure commitments |
| Villager-count thresholds | PRESERVE + CLASSIFY | Distinguish policy from observed state |
| Idle-worker handling | PRESERVE + IMPROVE | Valuable operational behavior |
| Worker reassignment | PRESERVE + FORMALIZE | Core actuator boundary |
| Economic timers | PRESERVE + TYPE | Temporal guards require semantic classification |
| Escrow interaction | PRESERVE + CONSTRAIN | Labor must respect resource ownership |
| Market interaction | PRESERVE + SEPARATE | Liquidity management, not labor authority |
| Emergency reallocation | PRESERVE + BOUND | Survival priority inversion is valuable |
| Hardcoded worker ratios | AUDIT / PARAMETERIZE | Donor coefficients require provenance |
| Duplicate allocation writers | QUARANTINE / CLASSIFY | Namespace safety |
| Unreachable legacy allocation | QUARANTINE | Preserve evidence without active authority |
| Rule-order arbitration | EXTRACT / EXPLICITATE | Retain behavior while exposing precedence |
| `up-jump-rule` effects | EXTRACT / BOUND | Procedural preemption must have explicit semantics |

---

# 34. Anti-patterns

System 06 must reject the following designs.

### AP-01 — Resource threshold monoculture

`low food → move workers` without demand attribution or continuity context.

### AP-02 — Desired-count completion

Treating target worker count as proof of economic success.

### AP-03 — Assignment equals productivity

Treating a worker assignment command as proof of resource production.

### AP-04 — Global resource maximization

Attempting to maximize every resource simultaneously rather than satisfying authorized requirements.

### AP-05 — Oscillating labor

Repeatedly moving workers between resources around a threshold without hysteresis.

### AP-06 — Strategic leakage

Allowing the labor allocator to choose military strategy merely because one resource becomes scarce.

### AP-07 — Escrow blindness

Treating protected resources as freely spendable.

### AP-08 — Dead reservation blindness

Allowing stale/expired commitments to distort labor allocation indefinitely.

### AP-09 — Infrastructure blindness

Counting workers as productive when their source/building is unavailable.

### AP-10 — Static competence claim

Declaring the economy successful because the relevant rules exist in source.

---

# 35. Hard invariants

### VE-01 — Labor authority is below strategic authority

System 06 allocates workers; it does not select strategic objectives.

### VE-02 — Desired ≠ assigned ≠ productive

These states must not collapse into one variable semantically.

### VE-03 — Stock ≠ flow

Current resource count does not prove economic health.

### VE-04 — Demand must be attributable where possible

Resource requirements should retain their originating commitment/requirement identity.

### VE-05 — Assignment is not completion

Worker reassignment does not prove productive output.

### VE-06 — Infrastructure readiness matters

Workers cannot be treated as productive when required infrastructure is unavailable.

### VE-07 — Escrow ownership is preserved

Labor policy cannot justify unauthorized consumption of protected resources.

### VE-08 — Emergency authority is bounded

Survival overrides must be attributable, reversible, and observable.

### VE-09 — Hysteresis is mandatory where switching is reversible

Economic noise must not produce pathological labor oscillation.

### VE-10 — Legacy writers are not automatically authoritative

Every competing writer must be classified.

### VE-11 — Static evidence is not runtime proof

Source presence and reachability do not establish productive economic behavior.

### VE-12 — Economic feasibility is not strategic correctness

The labor system can establish whether an authorized requirement is economically supportable; it does not decide whether the requirement is strategically correct.

### VE-13 — Verified outcomes feed reassessment

Observed economic consequences must update allocation state.

### VE-14 — Failed allocation is not strategic failure

A resource-labor failure should produce an economic diagnostic and, where appropriate, an upstream feasibility/replanning signal rather than silently corrupting strategic state.

### VE-15 — One worker has one authoritative active labor role

Any exception must be explicit, bounded, and represented in the state model.

---

# 36. Definition of done

System 06 is not complete until the forensic and qualification work can answer, for every critical labor-allocation path:

1. What requirement caused this allocation?
2. Which authority owns the requirement?
3. What resource is being produced?
4. What worker target was requested?
5. What workers were actually assigned?
6. What workers became productive?
7. What source/infrastructure enabled productivity?
8. What resource flow was observed?
9. What commitment or transaction depends on the flow?
10. What competing resource requirements existed?
11. Why did this allocation win?
12. What timer or hysteresis prevents oscillation?
13. What causes reassignment?
14. What causes release?
15. What happens if the source becomes invalid?
16. What happens if infrastructure is unavailable?
17. What happens if the upstream commitment expires?
18. What happens during emergency preemption?
19. What evidence proves the allocation worked?
20. What evidence remains uncertain?

A successful System 06 is therefore not “a villager distribution script.” It is an auditable **labor-allocation control boundary** with explicit economic demand, ownership, state, temporal guards, execution, verification, and reassessment.

---

# 37. Final engineering directive

Do not rebuild Shadow's villager economy because its rules look old, procedural, or inelegant.

First determine which economic behaviors are already valuable.

Then separate:

```text
RESOURCE STATE
→ DEMAND
→ LABOR REQUIREMENT
→ ALLOCATION AUTHORITY
→ WORKER ASSIGNMENT
→ PRODUCTIVITY
→ RESOURCE FLOW
→ COMMITMENT FEASIBILITY
```

Preserve donor knowledge where it is empirically useful. Replace only opaque or unsafe authority boundaries. Formalize hidden state rather than deleting it. Improve the architecture where doing so increases attribution, stability, recoverability, observability, and strategic interoperability.

The correct System 06 role is:

> **Convert authorized economic requirements into productive civilian labor without becoming the strategic decision-maker.**

The next system should build on this boundary rather than bypass it. Production, construction, research, market, and commitment machinery should consume explicit labor/resource feasibility rather than infer economic capability from scattered worker-count goals.

---

# Appendix A — Cross-system interface

```text
SYSTEM 04 — SCOUTING
        ↓
OBSERVATIONS
        ↓
SYSTEM 03 — TARGET / INFORMATION STATE
        ↓
AEGIS — BELIEF / THREAT / OBJECTIVE / CAPABILITY
        ↓
COMMITMENT
        ↓
SHADOW ECONOMIC SUBSTRATE
        ↓
SYSTEM 05 — FOOD CONTINUITY ─────┐
                                  ↓
SYSTEM 06 — VILLAGER ECONOMY → LABOR ALLOCATION
                                  ↓
                        RESOURCE PRODUCTIVITY
                                  ↓
                       ECONOMIC STATE UPDATE
                                  ↓
                         COMMITMENT FEASIBILITY
                                  ↓
                              REASSESSMENT
```

System 05 determines food-source continuity requirements. System 06 turns those requirements, plus other authorized economic demands, into labor allocation. Shadow remains responsible for resource protection, transaction preparation, and commitment funding. Production/construction/research authority remains downstream.

---

# Appendix B — Evidence ledger starter

| Claim | Evidence class | Status | Required qualification |
|---|---|---|---|
| Shadow contains a distinct villager-economy subsystem | DIRECT / COMPOSED from donor forensic decomposition | CONFIRMED at static-analysis level | Runtime activation still separate |
| Resource saving is coupled to progression/work-item state | DIRECT | CONFIRMED donor finding | Trace individual allocation paths |
| Food logistics and labor allocation are separable architectural boundaries | AEGIS-GENERALIZATION supported by subsystem decomposition | PROBABLE architecture | Qualify interface |
| Desired worker counts differ semantically from productive workers | AEGIS-GENERALIZATION | REQUIRED design rule | Runtime instrumentation |
| Worker transitions impose economic cost | AEGIS-GENERALIZATION | PLAUSIBLE | Recover donor transition behavior |
| Resource stock and flow must be separated | AEGIS-GENERALIZATION | REQUIRED analytical model | Runtime flow qualification |
| Emergency survival state can alter economic behavior | DIRECT donor finding | CONFIRMED | Trace exact writer precedence |
| Escrow affects effective resource availability | DIRECT donor finding + AEGIS composition | CONFIRMED conceptually | Qualify current DE semantics |
| Rule order contributes to labor authority | COMPOSED from donor procedural arbitration | PROBABLE | Complete writer/reader graph |
| A worker assignment proves productive gathering | — | DISPROVEN | Must observe postcondition |

---

# Appendix C — Required Muse deliverables

Before implementing broad System 06 behavior, Muse should produce:

1. **Villager State Registry** — every critical worker/resource state with type, owner, writers, readers, lifetime, reset, expiry, and evidence.
2. **Labor Writer/Reader Graph** — complete writer → state → reader graph for resource allocation variables.
3. **Resource Demand Ledger** — every donor rule that creates or modifies economic demand.
4. **Allocation Precedence Matrix** — food/wood/gold/stone/building/emergency competition and explicit precedence.
5. **Worker Transition Matrix** — source → destination transitions, conditions, costs, timers, and release rules.
6. **Infrastructure Dependency Matrix** — labor requirement → required infrastructure → executor → postcondition.
7. **Escrow/Labor Interaction Map** — protected resource → commitment → labor consequence → release.
8. **Idle/Starvation Diagnostic Matrix** — cause-specific idle and starvation states.
9. **Static/Runtime Evidence Ledger** — what source analysis proves versus what still requires runtime qualification.
10. **First vertical-slice implementation** — one requirement → one allocation → one assignment → observed productivity → resource-flow verification → reassessment.

The implementation may differ from the semantic model because `.per` imposes representation constraints. It may not silently collapse the distinctions the model requires.