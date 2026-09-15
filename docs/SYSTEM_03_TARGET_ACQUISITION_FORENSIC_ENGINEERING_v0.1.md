# The Byzantine Shadow — System 03: Target Acquisition Forensic Engineering v0.1

## 0. Purpose and forensic standard

This document is the third system-level forensic engineering specification in the Shadow reconstruction sequence. It isolates the donor's **target acquisition subsystem**: the machinery that identifies an opposing player/target, maintains target identity and associated metadata, selects spatially relevant enemy objects, switches targets, and supplies target state to downstream military and strategic systems.

Source donor: `Shadow DC7(1).per`  
Source SHA-256: `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`  
Physical source size: 615,773 bytes  
Physical line count: 22,603  

The existing military audit reports that the main target section contains approximately **147 rules** and that the donor maintains target player, target age, target type, coordinates, target HP, nearest TC/castle/tower, enemy units in range, raid targets, and target switching. fileciteturn27file0L2-L2

Evidence rule: all donor claims in this document are **DIRECT static evidence** unless explicitly labeled otherwise. Static presence does not prove runtime reachability, writer precedence, successful target acquisition, freshness, strategic correctness, or tactical success.

The purpose of System 03 is therefore not to redesign targeting in the abstract. It is to determine what the donor actually knows how to do, isolate the reusable target-state machinery, expose its hidden authority and temporal assumptions, and define the interface by which AEGIS may consume target information without allowing target acquisition to become an uncontrolled strategic brain.

---

# 1. Executive finding

Target acquisition is a **strategic information interface**, not merely a list of coordinates.

The donor's target subsystem appears to maintain a bundle of related state:

- target player identity;
- target age;
- target type/classification;
- target coordinates;
- target hit points or target-health information;
- nearest important enemy infrastructure;
- enemy units in relevant range;
- raid targets;
- target switching state.

The military audit correctly classifies this system as **PRESERVE + FORMALIZE**. fileciteturn27file0L2-L2

The central engineering problem is not that Shadow cannot find targets. It is that the target interface can collapse several distinct concepts into one mutable state channel:

`WHO are we targeting?`  
`WHAT object are we targeting?`  
`WHERE is it?`  
`HOW fresh is that information?`  
`WHY is it relevant?`  
`WHAT evidence established it?`  
`WHEN should we switch?`

AEGIS must not inherit that ambiguity.

The target system should therefore be reconstructed as a **Target Information Service** with explicit identity, validity, freshness, confidence/evidence, objective linkage, spatial metadata, and switching policy. It should provide information upward and mission-ready target state downward without acquiring authority to select strategic objectives independently.

**Disposition: PRESERVE donor knowledge → FORMALIZE target contract → SEPARATE target identity from target object → ADD validity/freshness/evidence → expose switching semantics → qualify before strategic dependence.**

---

# 2. System boundary

## 2.1 In scope

System 03 owns forensic analysis and future interface design for:

1. opponent/player target identity;
2. target-player metadata;
3. target-object identity and classification;
4. target coordinates and spatial state;
5. target-health state where available;
6. nearest/high-value enemy infrastructure selection;
7. enemy-in-range target information;
8. raid-target acquisition;
9. target switching and replacement;
10. target validity and stale-state handling;
11. interface between targeting and scouting;
12. interface between targeting and threat/defense;
13. interface between targeting and tactical groups;
14. interface between targeting and AEGIS strategic objectives.

## 2.2 Explicitly out of scope

System 03 does not own:

- scouting movement execution;
- strategic objective selection;
- military composition selection;
- combat-control execution;
- resource commitment;
- production authorization;
- tactical group movement/firing execution;
- strategic threat valuation as a whole.

Those systems may consume or invalidate target state, but they do not become part of the target subsystem merely because they write target-related variables.

---

# 3. Forensic baseline

The Shadow forensic deep dive characterizes the overall donor as a distributed control system containing target acquisition, scouting, food logistics, economy, strategy, enemy inference, threat/defense, composition, tactical missions, force evaluation, progression, escrow, research, construction, market balancing, emergency response, telemetry, and procedural arbitration. fileciteturn21file0L2-L2

The military audit isolates target acquisition as its first military system and identifies approximately 147 rules in the main target section. It explicitly states that the target subsystem maintains target player, target age, target type, coordinates, target HP, nearest TC/castle/tower, enemy units in range, raid targets, and target switching. fileciteturn27file0L2-L2

This establishes a significant point for the reconstruction:

> Target acquisition is already a reusable subsystem with meaningful internal state. It should not be discarded simply because AEGIS is replacing the donor's strategic arbitration.

---

# 4. Target acquisition is a state-establishment pipeline

The correct abstraction is not simply:

`find enemy → set target`.

The donor should be interpreted as performing some version of:

```text
OBSERVATION
    ↓
ENEMY / OBJECT IDENTIFICATION
    ↓
TARGET CLASSIFICATION
    ↓
TARGET STATE WRITE
    ↓
SPATIAL ASSOCIATION
    ↓
VALIDITY / RELEVANCE CHECK
    ↓
TARGET RETENTION OR SWITCH
    ↓
DOWNSTREAM CONSUMPTION
```

The exact predicates and sequencing must be recovered from source-level tracing before implementation claims stronger semantics.

This sequence is consistent with the broader AEGIS canonical loop:

`OBSERVATION → CLASSIFICATION → STATE WRITE → AUTHORITY EFFECT → RESOURCE / PRODUCTION CONSEQUENCE → TEMPORAL GUARD → REASSESSMENT`.

For targeting specifically, the target state is an intermediate belief/state representation. It is not equivalent to truth merely because the variable was written.

---

# 5. Separate the target dimensions

A critical System 03 requirement is to prevent several distinct concepts from becoming one overloaded goal or strategic number.

## 5.1 Target player

**Definition:** the opposing player currently associated with a strategic or tactical targeting context.

Example semantic role:

```text
TARGET_PLAYER = opponent identity
```

This is not itself a unit/building target.

## 5.2 Target object

**Definition:** the concrete enemy entity or object that a mission may interact with.

Examples include:

- unit;
- town center;
- castle;
- tower;
- raidable economic object;
- strategic building.

A target player can remain stable while target objects change.

## 5.3 Target type

Target type/classification describes what kind of object the current target represents.

It must not be confused with strategic objective. For example:

```text
TARGET_TYPE = TOWER
```

does not imply:

```text
OBJECTIVE = DESTROY_TOWER
```

The latter requires strategic authority.

## 5.4 Target coordinates

Coordinates describe spatial state associated with the target.

They must carry freshness semantics. A coordinate remembered from an earlier observation is not necessarily the target's current location.

## 5.5 Target health

Target HP is an observation-derived value and therefore requires temporal semantics. It is not a permanent property of the target state.

## 5.6 Nearby infrastructure

Nearest TC/castle/tower information is a derived spatial relationship. It should not overwrite primary target identity merely because an infrastructure object is closer.

## 5.7 Enemy units in range

This is a local-context observation, not necessarily the current mission target.

## 5.8 Raid target

Raid target is a mission-specific target selection. It should be distinguishable from the global/strategic target player and from tactical combat targets.

---

# 6. Required target-state contract

Muse should establish a canonical semantic target record even if the final `.per` representation must encode it through goals/SNs.

Minimum fields:

```text
TARGET_ID
TARGET_PLAYER
TARGET_KIND
TARGET_X
TARGET_Y
TARGET_HP / HEALTH_STATE
TARGET_VALID
TARGET_CONFIDENCE
TARGET_EVIDENCE_LEVEL
TARGET_OBSERVED_EPOCH
TARGET_LAST_REFRESH_EPOCH
TARGET_SOURCE
TARGET_OBJECTIVE_ID
TARGET_MISSION_ID
TARGET_GENERATION
TARGET_PRIORITY
TARGET_SWITCH_REASON
TARGET_EXPIRY
```

Not every field must necessarily be a literal runtime slot. The requirement is semantic separation and an implementation mapping that can be audited.

---

# 7. Target identity versus target evidence

The most important epistemic rule for System 03 is:

> **A target record is a belief/state representation derived from observations; it is not ground truth merely because it exists in memory.**

A target coordinate may be:

- directly observed;
- inferred from related observations;
- stale;
- invalidated;
- unknown.

Similarly, target HP may be:

- directly observed;
- estimated;
- stale;
- unavailable.

The target interface must therefore carry evidence/freshness semantics wherever downstream decisions materially depend on them.

Required classification vocabulary:

`DIRECT`  
`COMPOSED`  
`INFERRED`  
`AEGIS-GENERALIZATION`  
`UNCERTAIN`

The system must not promote `INFERRED` target state to `DIRECT` merely because the target is convenient to use.

---

# 8. Freshness is a first-class target property

Target state has a different failure mode from static configuration: **staleness**.

A target may remain syntactically valid while becoming strategically invalid because:

- the target moved;
- the target died;
- the target changed state;
- the target player became irrelevant;
- a more urgent threat emerged;
- the observation is too old;
- the tactical mission moved away from the original context.

Therefore validity cannot be implemented as a simple permanent boolean.

Recommended semantic model:

```text
OBSERVED
   ↓
FRESH
   ↓
AGING
   ↓
STALE
   ↓
INVALID / UNKNOWN
```

The exact timing thresholds are policy parameters and must not be presented as engine facts until qualified.

---

# 9. Target validity contract

A target is valid only when the minimum conditions required by its consumer are satisfied.

A useful generic predicate is:

```text
TARGET_VALID =
    IDENTITY_KNOWN
    AND CLASSIFICATION_KNOWN
    AND POSITION_USABLE
    AND FRESHNESS_WITHIN_LIMIT
    AND OWNER_STILL_VALID
    AND OBJECTIVE/MISSION_STILL_ACTIVE
```

The exact predicate must be specialized by consumer.

For example, a raid waypoint may tolerate older coordinates than a close-range attack target. A strategic enemy-player identity may remain valid even after a particular building target becomes invalid.

Therefore do not implement one universal freshness threshold for all target types.

---

# 10. Target acquisition and scouting interface

The military audit identifies scouting as active information acquisition rather than merely movement. fileciteturn27file0L2-L2

That means the correct interface is:

```text
SCOUTING
   ↓
OBSERVATION
   ↓
TARGET ACQUISITION
   ↓
TARGET STATE
   ↓
THREAT / MISSION / STRATEGIC CONSUMERS
```

Scouting should provide observations. Target acquisition should classify and retain target state. Strategic systems should interpret the resulting evidence.

Do not allow target acquisition to secretly command scouts merely because it needs fresh information. If the implementation needs a refresh request, expose it as an information-acquisition requirement rather than silently embedding a second scouting planner.

---

# 11. Target switching is arbitration, not housekeeping

The donor explicitly contains target switching. fileciteturn27file0L2-L2

Target switching should therefore be treated as a formal transition:

```text
CURRENT TARGET
      ↓
REASSESS
      ↓
KEEP / SWITCH / INVALIDATE / DEFER
```

A switch must have a reason.

Recommended switch reasons:

```text
TARGET_DEAD
TARGET_INVALID
TARGET_STALE
OBJECTIVE_CHANGED
MISSION_CHANGED
HIGHER_PRIORITY_TARGET
TARGET_UNREACHABLE
TARGET_NO_LONGER_RELEVANT
BETTER_EVIDENCE
TACTICAL_FAILURE
EMERGENCY
```

The exact reasons supported by the donor should be recovered through static tracing before being claimed as donor-native semantics. The list above is an AEGIS-generalization/design contract.

---

# 12. Hysteresis for target switching

Naive target switching creates oscillation.

If two targets alternate between slightly different utility values, the tactical system can thrash:

```text
A → B → A → B → A
```

Therefore switching should require either:

1. a hard invalidation of the current target;
2. a meaningful priority advantage for the replacement;
3. an explicit mission change;
4. an emergency override.

Conceptual rule:

```text
SWITCH IF
    current target invalid
    OR emergency veto
    OR
    (replacement score - current score) >= SWITCH_MARGIN
```

`SWITCH_MARGIN` is an AEGIS-generalized policy parameter, not a donor fact unless recovered directly.

The donor's existing target-switching behavior must be traced before replacing it, because procedural ordering may already provide implicit hysteresis.

---

# 13. Strategic target versus tactical target

This distinction is mandatory.

## Strategic target

Answers:

> Which opponent/objective is relevant to the current strategic plan?

## Tactical target

Answers:

> Which concrete enemy object should this mission interact with right now?

The relationship is:

```text
STRATEGIC OBJECTIVE
        ↓
TARGET SET / TARGET CLASS
        ↓
TACTICAL TARGET
```

Not:

```text
TACTICAL TARGET
        ↓
STRATEGIC OBJECTIVE
```

unless an explicitly authorized upward inference mechanism exists.

This prevents a nearby enemy unit from accidentally becoming a strategic doctrine switch.

---

# 14. Target-player selection

Target-player selection is a higher-level decision than selecting a specific enemy object.

The target-player state should be based on a coherent selection policy incorporating, where available:

- enemy presence;
- enemy activity;
- observed military threat;
- strategic relevance;
- proximity;
- objective linkage;
- target availability;
- information freshness.

However, **target player ≠ threat level** and **target player ≠ strategic objective**.

A player can be the primary target while a different player's local force creates the immediate tactical threat. AEGIS must retain the ability to represent these independently.

---

# 15. Target-player persistence

Do not unnecessarily switch target player whenever a new enemy observation appears.

A target player should persist until one of the following occurs:

- explicit strategic replacement;
- target invalidation;
- objective termination;
- stronger authorized target-player selection;
- emergency condition;
- loss of meaningful evidence.

This persistence is an AEGIS-generalized requirement. Muse must determine whether the donor already implements equivalent behavior through rule order, timers, or target-switching conditions.

---

# 16. Spatial target state

Target coordinates are not merely decorative metadata. They drive downstream tactical geometry.

The target contract should distinguish:

```text
TARGET_POSITION_OBSERVED
TARGET_POSITION_ESTIMATED
TARGET_POSITION_STALE
TARGET_POSITION_UNKNOWN
```

Derived spatial relationships should not overwrite the source observation.

For example:

```text
TARGET_X / TARGET_Y
```

should remain the target's coordinate record, while:

```text
DISTANCE_TO_TARGET
NEAREST_TC_DISTANCE
DISTANCE_TO_HOME
```

are derived values.

This separation matters for debugging and prevents derived values from becoming false observations.

---

# 17. Infrastructure targeting

The donor explicitly tracks nearest TC/castle/tower information. fileciteturn27file0L2-L2

This should be represented as a family of derived target candidates rather than a single universal `TARGET`.

Conceptual structure:

```text
TARGET_PLAYER
   ├── PRIMARY_OBJECT_TARGET
   ├── NEAREST_TC
   ├── NEAREST_CASTLE
   ├── NEAREST_TOWER
   └── RAID_TARGET
```

Each candidate requires its own validity/freshness semantics.

A nearby tower can be relevant for tactical pathing while the strategic objective remains economic disruption. The existence of the tower must not force the strategic objective to become “destroy tower.”

---

# 18. Enemy units in range

`enemy units in range` is a local observation context.

It should feed:

- tactical threat evaluation;
- target selection;
- retreat/engagement decisions;
- mission validity;
- emergency response.

It should not automatically rewrite the strategic target player or strategic objective.

The target subsystem should therefore distinguish:

```text
CURRENT_TARGET
```

from:

```text
LOCAL_ENEMY_CONTEXT
```

This is especially important for raids and defensive reactions.

---

# 19. Raid-target interface

Raid targets are explicitly identified in the military audit. fileciteturn27file0L2-L2

A raid target should be treated as a mission-scoped target object:

```text
RAID_MISSION
   ↓
RAID_TARGET
   ↓
RAID_TARGET_VALID
   ↓
WAYPOINT / APPROACH
   ↓
TACTICAL EXECUTION
```

Raid target selection may use strategic information, but tactical execution must not mutate strategic objective state merely because a raid target was changed.

When a raid target becomes invalid, the correct response is normally mission-level reassessment, not automatic strategic failure.

---

# 20. Target state ownership

System 02 established the general requirement that critical state requires explicit ownership. System 03 applies that requirement to target state.

Recommended ownership model:

| State | Primary owner | Permitted consumers | Strategic authority? |
|---|---|---|---|
| Target player | Target-selection authority | Strategy, threat, missions | No, unless explicitly delegated |
| Target object | Target acquisition / mission layer | Tactical executor | No |
| Target classification | Target acquisition | Threat, mission, strategy | No |
| Target coordinates | Observation/target state | Geometry, mission | No |
| Target freshness | Target state/observation layer | All consumers | No |
| Target confidence | Evidence layer | Strategy, threat, missions | No |
| Raid target | Raid mission authority | Raid executor | No |
| Strategic objective | AEGIS | Targeting, Shadow, executor | **Yes** |
| Mission | Tactical/military authority | Targeting, executor | Bounded |

The implementation may map these into .per goals/SNs, but it must preserve the ownership semantics.

---

# 21. Generation control

Target state is particularly vulnerable to stale writes because multiple systems may update it over time.

A target record should therefore have a logical generation or equivalent mechanism:

```text
TARGET_GENERATION = G
```

When a new target context is created:

```text
G → G + 1
```

Writes associated with an older generation must not overwrite the new target context.

This is an AEGIS-generalized engineering requirement. It is not claimed as donor-native behavior until direct evidence is recovered.

If .per constraints make explicit generations expensive, Muse should design the closest robust equivalent using existing state/identity/cursor mechanisms and document the limitation.

---

# 22. Target lifecycle

The canonical target lifecycle should be modeled as:

```text
UNKNOWN
  ↓
OBSERVED
  ↓
CLASSIFIED
  ↓
VALID
  ↓
ACTIVE
  ↓
AGING
  ↓
REFRESHED ─────────┐
  ↓                │
STALE              │
  ↓                │
INVALID / LOST     │
  ↓                │
REPLACED ←─────────┘
```

This is a semantic model. The actual `.per` implementation may use fewer states, but the implementation must preserve the distinctions needed to avoid stale-target execution.

---

# 23. Target switching and objective changes

The most important upward interface is:

```text
TARGET CHANGE
     ↓
DOES OBJECTIVE CHANGE?
     ↓
YES → AEGIS REASSESSMENT
NO  → MISSION/TARGET RESELECTION ONLY
```

A target change must not automatically imply an objective change.

Example:

```text
Objective = disrupt enemy economy
Target A = exposed villager
Target A dies
Target B = exposed farm / economic building
```

The objective remains stable while the tactical target changes.

Conversely:

```text
Objective = attack enemy infrastructure
Enemy emergency force appears
```

The tactical target may change to a defensive withdrawal while the strategic objective remains suspended rather than deleted.

This separation is essential for AEGIS's capability-oriented control model.

---

# 24. Interface with threat/defense

The donor's threat system tracks cavalry in town, archery in town, enemies in town, attack size, nearby skirmishers and mangonels, town safety, and defensive state. fileciteturn27file0L2-L2

Target acquisition should provide observations and target candidates to threat evaluation.

Threat evaluation may then produce:

```text
THREAT = HIGH
```

but should not mutate the target record into a strategic objective without an explicit authority transition.

Recommended direction:

```text
TARGET / LOCAL ENEMY OBSERVATION
            ↓
       THREAT EVALUATOR
            ↓
      THREAT BELIEF
            ↓
          AEGIS
```

not:

```text
TARGET
  ↓
THREAT
  ↓
AUTOMATIC STRATEGIC ACTION
```

---

# 25. Interface with tactical groups

The military audit identifies stateful tactical groups with identity, size, coordinates, waypoints, target switching, regrouping, retreat, movement, firing, and combat modes. fileciteturn27file0L2-L2

This is valuable donor behavior and should not be rebuilt merely because strategic arbitration is being replaced.

The interface should become:

```text
MISSION AUTHORITY
      ↓
TARGET CONTRACT
      ↓
TACTICAL GROUP
      ↓
EXECUTION
      ↓
OBSERVATION / RESULT
```

The tactical group may request target refresh or report target invalidity, but it should not silently redefine the strategic objective.

---

# 26. Target acquisition as capability support

AEGIS's strategic model should reason in capabilities rather than individual targets.

For example:

```text
OBSERVATION: enemy cavalry
        ↓
THREAT: cavalry pressure
        ↓
CAPABILITY REQUIREMENT: anti-cavalry
```

Target acquisition then supplies the spatial/identity information needed by whichever candidate solution is selected.

Possible candidate solutions include:

- counter-unit;
- fortification;
- mobility;
- denial;
- relocation;
- retreat;
- counterattack;
- siege;
- technology;
- delay.

The military audit explicitly recommends this capability abstraction. fileciteturn27file0L2-L2

Target acquisition should therefore be **solution-agnostic**. It should not assume that the existence of a target means direct attack is the correct response.

---

# 27. Target scoring

A future target-selection score may be useful, but it must be distinguished from strategic priority.

A target score can incorporate:

```text
TARGET_SCORE =
    relevance
  + accessibility
  + freshness
  + vulnerability
  + mission compatibility
  - tactical danger
  - distance cost
  - uncertainty penalty
```

This is an **AEGIS-GENERALIZATION**, not a claim about the donor's exact formula.

Muse must first recover any donor-native scoring/evaluation behavior before replacing it. The forensic military audit separately identifies attack efficiency, damage potential, and superiority as an embryonic utility/risk evaluator. fileciteturn27file0L2-L2

Target scoring should therefore remain a bounded selection mechanism beneath strategic authority.

---

# 28. Evidence and confidence propagation

Target acquisition should preserve provenance.

Example:

```text
SCOUT OBSERVATION
    evidence = DIRECT
    epoch = 1200
    ↓
TARGET RECORD
    confidence = high
    freshness = fresh
    ↓
MISSION
```

Later:

```text
epoch = 1450
freshness = stale
```

The target may remain a known historical location while no longer being a sufficiently reliable current tactical target.

The implementation should not erase provenance merely because a consumer wants a simple boolean.

---

# 29. Temporal guards

Target state should be governed by temporal guards.

Examples:

```text
TARGET_REFRESH_INTERVAL
TARGET_STALE_TIMEOUT
TARGET_SWITCH_COOLDOWN
MISSION_TARGET_TIMEOUT
TARGET_RECHECK_AFTER_COMBAT
TARGET_RECHECK_AFTER_RETREAT
```

These are policy concepts. Their numerical values require qualification.

The donor already contains a large timer registry, including target switching and tactical reevaluation timing. System 01 established that Shadow's timers are best understood as temporal guards rather than arbitrary delays. Therefore target timing should be extracted as named semantic categories rather than copied as unexplained numbers.

---

# 30. Failure modes

System 03 must explicitly account for:

### 30.1 False persistence

A dead or moved target remains active.

### 30.2 False switching

Minor changes cause repeated target oscillation.

### 30.3 Target conflation

Target player, target object, raid target, and local enemy context share one state channel.

### 30.4 Stale coordinates

Old location is treated as current position.

### 30.5 Stale health

Old HP estimate is treated as current.

### 30.6 Strategic leakage

A tactical target silently changes strategic objective.

### 30.7 Unauthorized overwrite

A lower-priority subsystem overwrites target state established by an authoritative mission.

### 30.8 Generation collision

A delayed/old rule writes state belonging to an earlier target context.

### 30.9 Emergency corruption

Emergency defensive targeting destroys the state of a suspended offensive mission rather than creating a bounded emergency context.

### 30.10 No-target deadlock

A mission remains active after its target becomes invalid and repeatedly attempts impossible execution.

---

# 31. Emergency targeting

Defense has priority-inversion authority in the donor's military architecture. The military audit explicitly classifies survival behavior as requiring formalized emergency authority. fileciteturn27file0L2-L2

Emergency targeting should therefore use a bounded override:

```text
NORMAL MISSION
     ↓
EMERGENCY DETECTED
     ↓
SUSPEND / OVERRIDE
     ↓
EMERGENCY TARGET CONTEXT
     ↓
EXECUTE / VERIFY
     ↓
RECONSIDER PRIOR MISSION
```

Do not overwrite the prior mission's target state destructively if it may resume.

This connects directly to the Shadow commitment/preemption architecture: emergency action should be a bounded preemption, not an uncontrolled state reset.

---

# 32. Target invalidation and mission recovery

When a target becomes invalid:

```text
TARGET_INVALID
      ↓
STOP NEW TARGET-DEPENDENT ACTIONS
      ↓
REASSESS
      ↓
KEEP OBJECTIVE?
   ├── YES → ACQUIRE NEW TARGET
   └── NO  → TERMINATE / SUSPEND MISSION
```

This distinction is critical.

Target failure does not necessarily imply mission failure.

Mission failure does not necessarily imply strategic commitment failure.

Strategic commitment failure does not necessarily imply strategic objective failure.

This mirrors the failure separation established in Shadow's economic kernel.

---

# 33. Static forensic work Muse must perform before implementation

The existing repository artifacts identify the target system conceptually. Muse must now deepen the forensic layer at source level before claiming a final implementation mapping.

Required extraction:

1. Enumerate every target-related goal and strategic-number symbol.
2. Enumerate every writer to each target symbol.
3. Enumerate every reader.
4. Record rule order for every writer.
5. Record every `up-jump-rule` affecting target acquisition.
6. Record every timer/temporal guard affecting target creation, retention, switching, or invalidation.
7. Record every condition that changes target player.
8. Record every condition that changes target type.
9. Record every coordinate writer.
10. Record every HP writer.
11. Record every nearest-TC/castle/tower writer.
12. Record every raid-target writer.
13. Record every downstream consumer.
14. Identify ordinary versus emergency target paths.
15. Identify any target-state writes from outside the target section.
16. Identify duplicate target symbols and conditional definitions.
17. Identify target state that is reset only implicitly by rule order.
18. Identify target state whose lifetime crosses strategy/mission boundaries.
19. Identify target state whose meaning changes by map/civ/DE conditional.
20. Construct the target dependency graph.

No target variable should be promoted to canonical AEGIS state merely because its name appears authoritative.

---

# 34. Required dependency graph

The final System 03 implementation audit must be able to render at least this conceptual graph:

```text
SCOUT / OBSERVATION SOURCES
        │
        ▼
TARGET ACQUISITION
        │
 ┌──────┼─────────┬───────────┐
 ▼      ▼         ▼           ▼
PLAYER OBJECT   SPATIAL     LOCAL ENEMY
ID      TYPE    STATE        CONTEXT
 │       │        │             │
 └───────┴────────┴─────────────┘
                 │
                 ▼
        VALIDITY / FRESHNESS
                 │
                 ▼
          TARGET SELECTION
                 │
        ┌────────┴────────┐
        ▼                 ▼
  STRATEGIC CONSUMER   TACTICAL MISSION
        │                 │
        ▼                 ▼
      AEGIS            EXECUTOR
```

The actual graph must add every concrete symbol and rule dependency discovered in the donor.

---

# 35. Static versus runtime boundary

The following claims remain static unless separately qualified:

- a target rule exists;
- a target symbol is written;
- a target switch predicate exists;
- a coordinate is assigned;
- a nearest infrastructure rule exists;
- a timer is declared;
- a target score is computed.

The following require runtime evidence:

- the target rule is reached;
- the target symbol receives the expected value;
- the selected target corresponds to the intended world object;
- target coordinates are current;
- target switching actually occurs;
- stale targets are invalidated;
- tactical execution uses the selected target;
- target selection improves strategic outcome.

Never collapse these boundaries.

---

# 36. Qualification plan

System 03 should be qualified in progressively stronger stages.

## T0 — Static target inventory

Deliver the complete target symbol/writer/reader inventory.

## T1 — Ownership qualification

Demonstrate a single intended authority for each canonical target-state dimension, or explicitly document bounded multi-writer arbitration.

## T2 — Target lifecycle qualification

Demonstrate target creation, retention, refresh, invalidation, and replacement semantics at the available runtime evidence boundary.

## T3 — Switching qualification

Demonstrate that target switching occurs for the intended cause and does not oscillate under ordinary reevaluation.

## T4 — Tactical interface qualification

Demonstrate that a tactical mission consumes the intended target state rather than a stale/competing state.

## T5 — Strategic interface qualification

Demonstrate that target observations can inform AEGIS without target selection silently becoming strategic authority.

## T6 — Failure qualification

Demonstrate recovery from target loss, stale information, emergency interruption, and no-target conditions.

No T5/T6 strategic claim may be inferred from T0/T1 static evidence.

---

# 37. First implementation slice

The first `.per` implementation slice should be intentionally small.

Recommended slice:

```text
TARGET_PLAYER
TARGET_KIND
TARGET_X
TARGET_Y
TARGET_VALID
TARGET_FRESHNESS
TARGET_GENERATION
TARGET_OBJECTIVE_LINK
```

Then implement one complete target lifecycle:

```text
OBSERVE
 → CLASSIFY
 → WRITE
 → VALIDATE
 → CONSUME
 → REFRESH
 → INVALIDATE
 → REPLACE
```

Do not implement every target class, raid behavior, infrastructure selector, and tactical exception before the core contract is proven.

---

# 38. Donor preservation policy

The donor contains useful target-selection knowledge and approximately 147 rules in the main target section. fileciteturn27file0L2-L2

The implementation disposition is:

| Donor behavior | Disposition |
|---|---|
| Target-player selection | PRESERVE + FORMALIZE |
| Target age state | PRESERVE if downstream dependency proven |
| Target type/classification | PRESERVE + TYPE |
| Target coordinates | PRESERVE + FRESHNESS |
| Target HP | PRESERVE + TEMPORAL QUALIFICATION |
| Nearest TC/castle/tower | PRESERVE as derived candidate state |
| Enemy units in range | PRESERVE as local observation context |
| Raid targets | PRESERVE + MISSION-SCOPE |
| Target switching | PRESERVE + EXPLICITATE |
| Hidden rule-order arbitration | EXTRACT + DOCUMENT |
| Target timers | PRESERVE + TYPE |
| Duplicate target constants | QUARANTINE pending ownership/reachability proof |
| Strategic side effects | SUBORDINATE to AEGIS authority |
| Tactical executor behavior | PRESERVE unless independently disproven |

---

# 39. Relationship to System 01 and System 02

System 01 established that Shadow's configuration layer mixes environment contract, engine vocabulary, policy coefficients, runtime state, and compile-time specialization. System 03 must therefore classify any target parameter according to the same taxonomy rather than importing donor assumptions blindly.

System 02 established that state must have explicit ownership, writers, readers, lifetime, reset, precedence, and evidence semantics. Target acquisition is one of the first major consumers of that discipline because target state is both highly mutable and highly consequential.

The dependency is therefore:

```text
SYSTEM 01
Configuration / ABI
       ↓
SYSTEM 02
State / Authority
       ↓
SYSTEM 03
Target Acquisition
       ↓
SYSTEM 04+
Scouting / Information Acquisition / Threat
```

System 03 should not invent a second state registry. It should consume the canonical state/authority registry established by System 02.

---

# 40. Engineering definition of done

System 03 is not complete when Muse has written a target-selection function.

It is complete when the following are true:

1. Every critical donor target variable has been inventoried.
2. Every writer and reader is known or explicitly unresolved.
3. Target-player identity is separated from target-object identity.
4. Target type is separated from strategic objective.
5. Coordinates have freshness semantics.
6. Target evidence has provenance semantics.
7. Target switching has explicit causes.
8. Target switching has anti-thrashing protection.
9. Target invalidation is distinguishable from strategic failure.
10. Emergency target contexts do not destructively corrupt suspended normal missions.
11. Target generation or an equivalent stale-write defense exists.
12. Tactical groups consume bounded target state rather than strategic authority.
13. AEGIS can consume target evidence without giving targeting an implicit strategic mandate.
14. Static and runtime evidence are explicitly separated.
15. The first lifecycle slice is qualified before broad target behavior is enabled.

---

# 41. Hard invariants

**TA-01 — Target identity is not target object.**

A target player may remain constant while target objects change.

**TA-02 — Target object is not strategic objective.**

Selecting an object does not authorize a strategic plan.

**TA-03 — Coordinate is not truth.**

Coordinates are observations with freshness and provenance.

**TA-04 — Target existence is not target validity.**

A stored target can be stale or invalid.

**TA-05 — Target failure is not mission failure.**

A lost target may trigger replacement rather than mission termination.

**TA-06 — Mission failure is not commitment failure.**

Strategic commitment state remains owned by the appropriate authority.

**TA-07 — Emergency target state must be bounded.**

Emergency defense may preempt normal targeting without erasing the suspended context.

**TA-08 — Target switching requires an explicit reason.**

Do not permit unexplained oscillation.

**TA-09 — Stale writers must not overwrite newer target generations.**

Use generation or an equivalent state identity mechanism.

**TA-10 — Static target logic is not runtime target proof.**

Source reachability and runtime behavior remain separate evidence classes.

---

# 42. Final engineering directive to Muse

Do not rewrite Shadow's target system because it is old. **Extract it.**

The donor has already accumulated valuable target knowledge: opponent identity, target classification, coordinates, infrastructure relationships, local enemy context, raid targets, and target switching. The correct engineering task is to preserve this knowledge while removing the ambiguity caused by distributed writers, implicit timing, hidden procedural precedence, and accidental strategic side effects.

Build the target subsystem as an **information and selection boundary**:

```text
OBSERVE
  ↓
CLASSIFY
  ↓
ESTABLISH TARGET STATE
  ↓
VALIDATE / AGE
  ↓
SELECT / RETAIN / SWITCH
  ↓
SERVE TARGET STATE
```

Then make the interfaces explicit:

```text
SCOUTING → TARGET ACQUISITION → THREAT / MISSION / AEGIS
                                  ↓
                              EXECUTION
```

Do not allow the target subsystem to decide that because an enemy object was found, that object is strategically worth attacking. That decision belongs to the strategic/control plane.

At the same time, do not make the opposite mistake and reduce targeting to a passive coordinate store. Target acquisition is an active control interface with identity, validity, freshness, switching, spatial relationships, and mission context. Preserve that capability.

The engineering objective is therefore:

> **Turn Shadow's implicit target state into an explicit, auditable, freshness-aware target information service that preserves donor knowledge, prevents stale/competing writes, supports tactical execution, and remains subordinate to AEGIS strategic authority.**

The next system should build on this boundary rather than bypass it.
