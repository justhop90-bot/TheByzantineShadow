# The Byzantine Shadow — System 04: Scouting & Information Acquisition Forensics v0.1

**Status:** Forensic engineering specification  
**System:** 04 — Scouting / Information Acquisition  
**Predecessors:** System 01 — Initialization / Configuration; System 02 — State Namespace / Authority; System 03 — Target Acquisition  
**Primary disposition:** PRESERVE + IMPROVE  
**Evidence standard:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN  

---

## 0. Purpose and forensic standard

System 04 isolates the Shadow donor's **scouting subsystem**: the machinery that acquires spatial and enemy information through scout behavior, exploration patterns, recovery behavior, and map-aware search policy, and then exposes those observations to target acquisition, threat inference, strategic reasoning, and tactical systems.

The existing forensic decomposition identifies scouting as a distinct donor system and classifies it **PRESERVE + IMPROVE**. The military audit states that Shadow contains sheep scouting, new scouting, circle scouting, enemy scouting, border/flank/mirror/opposite/corner/center patterns, stuck recovery, and scouting switches; it also reports that map configuration changes exploration distances. fileciteturn27file0L2-L2

The system-level forensic baseline independently classifies scouting as an **active information-acquisition policy with multiple scout modes**, rather than a passive movement subsystem. fileciteturn32file0L2-L2

These observations establish the core engineering conclusion:

> **Scouting is an information-production system. Movement is its actuator; information acquisition is its purpose.**

The donor should therefore not be transplanted as a collection of scout movement rules. Its valuable behavior is the relationship between uncertainty, exploration policy, spatial coverage, mode selection, recovery, and the observations subsequently consumed by the target/threat/strategic layers.

Static donor evidence does **not** establish that every scouting rule is reachable, that every mode is mutually exclusive, that every exploration distance is correct in the current DE runtime, or that any particular scouting policy produces superior strategic outcomes. Those require qualification.

---

# 1. Executive finding

Shadow's scouting subsystem is best understood as an **active sensing controller**:

```text
INFORMATION NEED
       ↓
SCOUTING MODE
       ↓
EXPLORATION / MOVEMENT POLICY
       ↓
WORLD OBSERVATION
       ↓
OBSERVATION RECORD
       ↓
TARGET / THREAT / BELIEF UPDATE
       ↓
NEW INFORMATION NEED
```

This differs materially from:

```text
SCOUT → MOVE RANDOMLY → SEE SOMETHING
```

The donor's named scouting modes indicate that exploration is conditioned on information geometry and strategic context. The military audit specifically records sheep scouting, enemy scouting, circle scouting, directional/geometric patterns, stuck recovery, and mode switching. fileciteturn27file0L2-L2

The principal improvement target is therefore **not scout movement sophistication for its own sake**. It is the interface between:

1. what information is currently known;
2. what information is missing;
3. what observation would reduce that uncertainty;
4. where a scout should go to obtain it;
5. how the resulting observation changes authoritative state.

**Disposition:** preserve donor exploration knowledge; formalize scouting as information acquisition; separate observation from interpretation; add ownership, freshness, evidence, mission, and failure semantics; qualify the smallest complete observation loop before broad strategic dependence.

---

# 2. System boundary

## 2.1 In scope

System 04 owns the forensic/design boundary for:

1. scout role/mode selection;
2. sheep/food-location scouting;
3. enemy scouting;
4. geometric exploration patterns;
5. border/flank/mirror/opposite/corner/center exploration;
6. circle/search-pattern behavior;
7. map-aware exploration distance;
8. scouting switches;
9. scout progress/coverage state;
10. stuck detection and recovery;
11. information-request semantics;
12. scout observation production;
13. observation freshness;
14. observation provenance;
15. handoff into Target Acquisition;
16. handoff into Threat/Defense and enemy inference;
17. information-priority arbitration;
18. scouting failure and degraded-information states.

## 2.2 Explicitly out of scope

System 04 does not own:

- strategic objective selection;
- strategic threat valuation as a whole;
- target-object selection after observations are established;
- military composition;
- tactical combat execution;
- economic commitment/escrow;
- production authorization;
- final strategic doctrine selection.

Scouting may respond to an information requirement generated elsewhere, but it must not silently acquire strategic authority merely because it controls the scout actuator.

---

# 3. Forensic evidence hierarchy

The following distinctions are mandatory.

### DIRECT

A scouting mode, rule, variable, condition, timer, geometry operation, or recovery path is explicitly present in the donor source.

### COMPOSED

Multiple directly observed donor mechanisms combine into a higher-level behavior that is structurally established by the source.

### INFERRED

The behavior is strongly suggested by interactions among donor mechanisms but is not explicitly declared as such.

### AEGIS-GENERALIZATION

A design requirement introduced to make the donor behavior safer, more explicit, or compatible with AEGIS architecture.

### UNCERTAIN

The available evidence cannot establish the semantic or runtime behavior.

The following statement is **DIRECT** from the military audit:

> Shadow's scouting includes sheep scouting, new scouting, circle scouting, enemy scouting, border/flank/mirror/opposite/corner/center patterns, stuck recovery, and scouting switches, with map configuration affecting exploration distances. fileciteturn27file0L2-L2

The following is **AEGIS-GENERALIZATION**:

> A scout movement decision should be represented as an information-acquisition action whose expected value is tied to an explicit information deficit.

Do not silently promote the latter into a claim that the donor already implements an information-theoretic utility model.

---

# 4. Scouting is an information-production pipeline

The canonical System 04 model is:

```text
WORLD
  ↓
UNKNOWN / UNCERTAIN REGION
  ↓
INFORMATION REQUIREMENT
  ↓
SCOUTING AUTHORIZATION
  ↓
SCOUT MODE
  ↓
ROUTE / GEOMETRY
  ↓
MOVEMENT EXECUTION
  ↓
OBSERVATION
  ↓
OBSERVATION RECORD
  ↓
CLASSIFICATION / TARGET / BELIEF UPDATE
  ↓
INFORMATION DEFICIT REASSESSMENT
```

This must remain distinct from target acquisition.

System 04 answers:

> **Where and how should information be acquired?**

System 03 answers:

> **What target state can be established from available observations?**

AEGIS answers:

> **What does that information mean strategically, and what capability/commitment should follow?**

---

# 5. Observation is not interpretation

The scouting layer should produce observations without prematurely encoding strategic conclusions.

For example:

```text
SCOUT OBSERVES:
enemy stable at X,Y
```

is different from:

```text
BELIEF:
enemy is cavalry-focused
```

and different again from:

```text
OBJECTIVE:
prepare anti-cavalry capability
```

The causal direction should be:

```text
SCOUTING
   ↓
OBSERVATION
   ↓
TARGET / CLASSIFICATION / BELIEF
   ↓
AEGIS
   ↓
CAPABILITY REQUIREMENT
```

A scout should not become an implicit strategic inference engine simply because it sees a stable.

---

# 6. Required observation contract

Every strategically meaningful observation should have a semantic contract.

Minimum conceptual fields:

```text
OBSERVATION_ID
SOURCE_SCOUT_ID
OBSERVATION_KIND
LOCATION_X
LOCATION_Y
OBSERVED_ENTITY / CLASS
OBSERVED_PLAYER
OBSERVED_STATE
OBSERVED_EPOCH
LAST_REFRESH_EPOCH
VALID
EVIDENCE_LEVEL
CONFIDENCE
SOURCE_MODE
SCOUT_MISSION_ID
OBSERVATION_GENERATION
EXPIRY
```

Not every field must become a literal `.per` slot. The implementation must nevertheless preserve the distinctions where downstream behavior depends on them.

A simple boolean such as:

```text
ENEMY_FOUND = 1
```

is insufficient if downstream systems need to know **what enemy, where, when, by whom, and with what evidence**.

---

# 7. Scouting modes are policies, not strategic objectives

The donor explicitly contains multiple scouting modes. fileciteturn27file0L2-L2

The mode should answer:

> **How should information be acquired under the current information requirement?**

It should not answer:

> **What is our overall strategic plan?**

Conceptual mode taxonomy:

```text
SHEEP_SEARCH
ENEMY_SEARCH
LOCAL_REFRESH
CIRCLE_SEARCH
BORDER_SEARCH
FLANK_SEARCH
MIRROR_SEARCH
OPPOSITE_SEARCH
CORNER_SEARCH
CENTER_SEARCH
RECOVERY
```

The listed modes are donor-grounded where explicitly reported by the audit; the semantic interpretation of each as a policy class is an architectural abstraction.

Muse must map each mode to actual donor rules before implementation and identify whether modes are mutually exclusive, nested, sequential, or priority-arbitrated.

---

# 8. Information requirement is the correct control input

The major architectural improvement is to make scouting responsive to an explicit information deficit.

Conceptual examples:

```text
NEED = FIND_HOME_SHEEP
NEED = LOCATE_ENEMY_BASE
NEED = REFRESH_ENEMY_MILITARY
NEED = CHECK_FLANK
NEED = REFRESH_RAID_TARGET
NEED = VERIFY_LAST_KNOWN_POSITION
```

The actual donor may encode these indirectly through goals, strategic numbers, modes, timers, or rule order. That indirection must be recovered, not assumed away.

The AEGIS-generalized abstraction is:

```text
INFORMATION REQUIREMENT
        ↓
SCOUTING POLICY
```

rather than:

```text
STRATEGY
  ↓
HARDCODED SCOUT ROUTE
```

---

# 9. Information value and search priority

A future AEGIS scouting controller should prioritize information according to expected decision value.

Conceptually:

```text
INFORMATION_VALUE =
    expected decision improvement
  × probability information can be acquired
  − acquisition cost
  − tactical risk
```

This is **AEGIS-GENERALIZATION**, not donor-native mathematics.

Muse should not invent a complex numerical information-utility system before establishing what the donor's existing mode arbitration already accomplishes.

The first improvement should be semantic:

```text
WHY ARE WE SCOUTING THIS AREA?
```

If the answer cannot be represented, the scout controller is still procedurally opaque.

---

# 10. Sheep scouting

The military audit explicitly identifies sheep scouting. fileciteturn27file0L2-L2

Sheep scouting is not merely generic exploration. It is an information acquisition task with an economic consequence:

```text
UNKNOWN FOOD LOCATION
       ↓
SCOUT
       ↓
OBSERVE FOOD / SHEEP
       ↓
RESOURCE INFORMATION
       ↓
FOOD LOGISTICS
```

The correct interface is therefore:

```text
SCOUTING → OBSERVATION → FOOD LOGISTICS
```

not:

```text
SCOUTING → DIRECT VILLAGER COMMAND
```

unless a separate authorized logistics mechanism performs the latter.

The economic value of sheep information is donor-relevant because Shadow's food logistics system is itself identified as a major subsystem. fileciteturn32file0L2-L2

---

# 11. Enemy scouting

Enemy scouting produces observations relevant to:

- enemy location;
- enemy infrastructure;
- military presence;
- economic structure;
- strategic inference;
- threat evaluation;
- target acquisition.

The safe chain is:

```text
ENEMY SCOUT
    ↓
OBSERVATION
    ↓
CLASSIFICATION
    ↓
TARGET / BELIEF UPDATE
    ↓
THREAT / AEGIS
```

An observed stable should not itself authorize camel production. The observation becomes evidence that may contribute to a broader cavalry-threat classification.

This preserves the AEGIS threat → capability architecture.

---

# 12. Geometric search patterns

The donor contains border/flank/mirror/opposite/corner/center patterns and circle scouting. fileciteturn27file0L2-L2

These are valuable because they encode spatial search knowledge.

They should be treated as **search operators**:

```text
SEARCH_OPERATOR(region, objective, geometry)
```

rather than as strategic doctrines.

For example:

```text
FLANK_SEARCH
```

means a particular spatial acquisition policy.

It does not mean:

```text
STRATEGY = FLANK_ATTACK
```

This distinction prevents spatial exploration policy from contaminating strategic control.

---

# 13. Map-aware geometry

The donor reportedly changes exploration distances according to map configuration. fileciteturn27file0L2-L2

This is important evidence that scouting is not a fixed route table.

However, the exact semantics of those distances remain subject to static tracing and runtime qualification.

Required classification for every geometry parameter:

```text
ENGINE FACT
MAP FACT
DONOR POLICY
DERIVED VALUE
TEMPORAL STATE
UNKNOWN
```

Do not transplant a donor exploration distance merely because it appears numerically reasonable.

A parameter may encode:

- map size;
- player count;
- spawn geometry;
- scout position;
- search phase;
- heuristic safety margin;
- historical compensation for engine behavior.

Its meaning must be recovered.

---

# 14. Spatial frames must be explicit

Scouting geometry becomes unsafe when coordinate frames are ambiguous.

The implementation should distinguish:

```text
WORLD_COORDINATE
HOME_RELATIVE_COORDINATE
TARGET_RELATIVE_COORDINATE
SEARCH_CENTER
SEARCH_RADIUS
WAYPOINT
```

Derived geometry should not overwrite source coordinates.

This connects directly to System 02's requirement that coordinates be typed rather than treated as arbitrary integers, and to System 03's requirement that target coordinates retain provenance and freshness.

---

# 15. Scouting and Target Acquisition interface

System 03 established that target acquisition should consume scouting observations rather than command the scout actuator directly.

Canonical interface:

```text
SYSTEM 04
SCOUTING
   ↓
OBSERVATION
   ↓
SYSTEM 03
TARGET ACQUISITION
   ↓
TARGET STATE
   ↓
TACTICAL / THREAT / AEGIS
```

If Target Acquisition needs fresh information, it should create or propagate an **information requirement** rather than secretly embedding a new movement policy.

This produces a clean authority boundary:

- scouting owns information acquisition;
- targeting owns target-state construction;
- AEGIS owns strategic interpretation.

---

# 16. Scouting and threat inference

Enemy observations may feed threat classification.

The correct direction is:

```text
OBSERVATION
   ↓
ENEMY CLASSIFICATION
   ↓
THREAT BELIEF
   ↓
AEGIS CAPABILITY REQUIREMENT
```

The military audit records enemy-strategy inference and threat/defense as separate systems from scouting. fileciteturn32file0L2-L2

Therefore scouting must not become a hidden replacement for those systems.

A scout sees cavalry; the scouting subsystem reports cavalry.

The threat subsystem determines whether this constitutes a meaningful cavalry threat.

AEGIS determines what capability response is warranted.

---

# 17. Scouting and enemy-strategy inference

The Shadow forensic baseline identifies enemy-strategy inference as a distinct subsystem, with hypotheses including DRUSH/KRUSH/FC/FLUSH/SCRUSH. fileciteturn32file0L2-L2

This establishes a critical separation:

```text
SCOUTING = evidence acquisition
ENEMY INFERENCE = belief construction
AEGIS = strategic arbitration
```

Do not make scouting responsible for deciding that an enemy is executing a specific strategy.

A scout observation may contribute evidence toward such a hypothesis, but the hypothesis belongs to the inference layer.

---

# 18. Scout identity and ownership

Each scout should be treated as an execution resource with an identity and bounded assignment.

Conceptual state:

```text
SCOUT_ID
SCOUT_OWNER
SCOUT_MODE
SCOUT_MISSION_ID
SCOUT_TARGET_REGION
SCOUT_STATUS
SCOUT_GENERATION
SCOUT_LAST_OBSERVATION_EPOCH
SCOUT_LAST_PROGRESS_EPOCH
SCOUT_STUCK_STATE
```

The exact physical representation is an implementation decision.

The ownership requirement is not.

A scout assigned to an emergency information requirement should not be silently redirected by a lower-priority generic search rule.

---

# 19. Scouting mission lifecycle

A formal semantic lifecycle is recommended:

```text
REQUESTED
   ↓
AUTHORIZED
   ↓
ASSIGNED
   ↓
MOVING
   ↓
OBSERVING
   ↓
REPORTING
   ↓
COMPLETE
```

Exceptional states:

```text
SUSPENDED
PREEMPTED
STUCK
FAILED
EXPIRED
CANCELLED
```

This is **AEGIS-GENERALIZATION**. Muse must trace donor behavior to determine which of these states already exist implicitly.

The key invariant is that a movement command does not prove that the requested information was acquired.

---

# 20. Stuck recovery

The donor explicitly contains stuck recovery. fileciteturn27file0L2-L2

Stuck recovery must be treated as a failure/recovery state, not merely another movement route.

Correct semantic sequence:

```text
EXPECTED PROGRESS
       ↓
NO PROGRESS
       ↓
STUCK DETECTION
       ↓
RECOVERY POLICY
       ↓
RETRY / REPLAN
       ↓
PROGRESS RESTORED
```

The implementation should not mark a scouting mission complete merely because a recovery command was issued.

This follows the same command-lifecycle discipline used throughout AEGIS:

```text
COMMAND ISSUED ≠ WORLD STATE ACHIEVED
```

---

# 21. Scouting progress verification

A scouting mission should have an observable progress predicate.

Examples:

```text
SCOUT MOVED TOWARD ASSIGNED REGION
REGION OBSERVED
EXPECTED ENTITY FOUND
SEARCH SEGMENT COMPLETED
NEW INFORMATION GENERATED
```

A simple movement command is not sufficient proof.

For example:

```text
up-move
```

may establish only:

```text
W0 = command issued
```

A meaningful scouting result requires evidence at a higher state boundary:

```text
W1 = action accepted/pending
W2 = relevant world observation exists
W3 = information changes a usable capability/belief state
W4 = strategic consequence
```

The exact W0-W4 interpretation remains the AEGIS evidence model; runtime qualification must establish which observations are actually available.

---

# 22. Coverage versus knowledge

Scouting must not equate physical coverage with information completeness.

A scout can traverse a region without producing strategically useful information.

Therefore distinguish:

```text
AREA_VISITED
```

from:

```text
AREA_INFORMATIVE
```

and from:

```text
INFORMATION_REQUIREMENT_SATISFIED
```

This is an important architectural improvement because “scout reached waypoint” is not equivalent to “enemy location requirement resolved.”

---

# 23. Information freshness

Every observation that influences target or threat state should have temporal semantics.

Conceptual lifecycle:

```text
UNKNOWN
  ↓
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

Different observations require different freshness windows.

Examples:

- enemy player identity may remain useful for a long period;
- exact unit position may become stale quickly;
- building position may remain useful after a longer interval;
- current military count may require rapid refresh.

Do not impose one global scouting timeout.

---

# 24. Information decay

A scouting system should model the fact that information loses value over time.

Conceptually:

```text
INFORMATION_VALUE(t) ↓ as t - observation_epoch ↑
```

The exact decay function is an AEGIS-generalization.

The donor's existing timers and refresh rules should be extracted first. Historical constants must not be promoted to universal decay coefficients without qualification.

---

# 25. Duplicate observation state

System 02 established that duplicate constants/goals may represent conditional specialization, legitimate duplication, shadowing, conflict, or legacy.

Scouting is particularly susceptible to duplicate state because different modes may maintain overlapping:

- positions;
- waypoints;
- mode values;
- timers;
- search counters;
- target references;
- progress markers.

Every duplicated critical state carrier must therefore be classified before transplant.

Do not merge states merely because their names look similar.

---

# 26. Mode switching authority

The donor contains scouting switches. fileciteturn27file0L2-L2

The key forensic question is:

> **Who is allowed to switch the scout from one information-acquisition mode to another?**

Potential authorities include:

```text
NORMAL SCOUT POLICY
INFORMATION REQUEST
EMERGENCY
TARGET REFRESH
STUCK RECOVERY
MISSION COMPLETION
STRATEGIC PRIORITY CHANGE
```

Muse must reconstruct the actual donor precedence.

The improved architecture should use:

```text
HIGHER-PRIORITY INFORMATION REQUIREMENT
        >
CURRENT SCOUTING MISSION
```

with hysteresis against unnecessary switching.

---

# 27. Scout-mode hysteresis

Without hysteresis, a scout can oscillate between search modes:

```text
ENEMY → SHEEP → ENEMY → SHEEP → ...
```

The AEGIS-generalized rule is:

```text
SWITCH IF
    current mission invalid
    OR emergency
    OR mission completed
    OR replacement priority exceeds current by SWITCH_MARGIN
```

A minimum dwell time or completion threshold may be appropriate.

Again, these are architectural requirements, not claims that the donor already uses this exact mechanism.

---

# 28. Multiple scouts and information allocation

If multiple scouts exist, the problem becomes allocation rather than independent movement.

Conceptual model:

```text
INFORMATION REQUIREMENTS
       ↓
SCOUT ALLOCATION
       ↓
SCOUT MISSIONS
       ↓
OBSERVATIONS
```

The allocator should avoid redundant assignments unless redundancy has positive information value.

Potential states:

```text
UNASSIGNED
ASSIGNED
ACTIVE
DUPLICATE
REDUNDANT
PREEMPTED
FAILED
COMPLETE
```

The donor's actual multi-scout arbitration must be traced before implementation claims equivalent behavior.

---

# 29. Information redundancy

Two scouts observing the same region may be useful under uncertainty, but redundant scouting should not occur accidentally.

The improved controller should distinguish:

```text
DUPLICATE COVERAGE
```

from:

```text
INDEPENDENT CONFIRMATION
```

Independent confirmation can increase confidence; accidental duplication merely wastes scout capacity.

This is a future AEGIS-generalization and should not be retrofitted as a complex confidence system before the donor observation graph is understood.

---

# 30. Emergency scouting

Emergency defense may require immediate information acquisition.

Examples include:

- unexpected enemy army near base;
- uncertain attack direction;
- missing flank information;
- suspected raid route;
- sudden loss of target confidence.

Emergency scouting should follow the same bounded-preemption discipline established in Shadow's broader architecture:

```text
NORMAL SCOUT MISSION
       ↓
EMERGENCY INFORMATION NEED
       ↓
SUSPEND / PREEMPT
       ↓
EMERGENCY SCOUT MISSION
       ↓
OBSERVE
       ↓
REPORT
       ↓
RESUME / REASSESS
```

The prior mission must not be destructively erased unless policy explicitly requires cancellation.

---

# 31. Scouting failure taxonomy

System 04 must distinguish:

### NO TARGET REGION

The information requirement cannot currently identify where to search.

### NO SCOUT AVAILABLE

The information requirement is valid but no scout can be assigned.

### STUCK

A scout fails to make expected spatial progress.

### SEARCH EXHAUSTED

The current search operator has completed without resolving the information requirement.

### OBSERVATION FAILED

The scout reached the intended region but did not acquire usable evidence.

### INFORMATION STALE

Previously acquired information is no longer sufficiently current.

### CONFLICTING OBSERVATIONS

Different scouts or observations disagree.

### PREEMPTED

Higher-priority information need interrupted the mission.

### CANCELLED

The information requirement no longer exists.

These distinctions prevent the common error of treating all scouting failures as movement failures.

---

# 32. Conflicting observations

Two observations may disagree without either being malicious or erroneous.

Example:

```text
Scout A: enemy army near X
Scout B: enemy army near Y
```

The system should not simply overwrite A with B.

Required behavior is:

```text
OBSERVATION A
OBSERVATION B
      ↓
CONFLICT / RECONCILIATION
      ↓
CURRENT BELIEF
```

This belongs primarily to the belief/inference layer, but System 04 must preserve enough provenance for reconciliation to occur.

---

# 33. Observation provenance

Every important observation should preserve at least:

```text
WHO observed it
WHEN
WHERE
WHAT was observed
UNDER WHICH SCOUTING MODE
```

Where possible:

```text
HOW CONFIDENT
WHAT PRIOR OBSERVATION IT CONFIRMS / CONTRADICTS
```

This enables downstream systems to distinguish fresh direct evidence from historical or inferred state.

---

# 34. Target refresh requests

System 03 may determine that a target is stale. That should produce an information requirement:

```text
TARGET_STALE
    ↓
REFRESH_TARGET_POSITION
    ↓
SCOUTING
    ↓
NEW_OBSERVATION
    ↓
TARGET_REFRESH
```

Scouting should not itself decide whether the strategic objective remains valid.

The objective remains owned by AEGIS; scouting fulfills the information requirement where possible.

---

# 35. Information requirements as first-class objects

AEGIS should eventually represent information requirements explicitly.

Minimum conceptual fields:

```text
INFO_REQUEST_ID
REQUEST_TYPE
PRIORITY
REGION / ENTITY
REQUIRED_FRESHNESS
CREATION_EPOCH
EXPIRY_EPOCH
OWNER
ASSIGNED_SCOUT
STATUS
SATISFACTION_PREDICATE
EVIDENCE_RESULT
```

Suggested lifecycle:

```text
CREATED
→ PRIORITIZED
→ ASSIGNED
→ ACQUIRING
→ OBSERVATION_RECEIVED
→ SATISFIED
```

Exceptions:

```text
BLOCKED
EXPIRED
CANCELLED
FAILED
PARTIAL
UNRESOLVED
```

This is an AEGIS-generalization and must be mapped to available `.per` state without assuming an object-oriented runtime exists.

---

# 36. Scouting and strategic arbitration

The strategic authority boundary should remain:

```text
WORLD
 ↓
OBSERVATION
 ↓
BELIEF / THREAT / OPPORTUNITY
 ↓
AEGIS OBJECTIVE
 ↓
INFORMATION REQUIREMENT
 ↓
SCOUTING
```

This may appear circular because observations can influence objectives that later create new information requirements. That is intentional:

```text
OBSERVE
 → BELIEVE
 → OBJECTIVE
 → INFORMATION NEED
 → OBSERVE AGAIN
```

The loop is closed through reassessment, not through a single permanently dominant subsystem.

---

# 37. Scouting must not become strategic authority

The following shortcuts are prohibited in the new architecture:

```text
SCOUT SEES STABLE → PRODUCE CAMELS
SCOUT SEES CASTLE → ATTACK CASTLE
SCOUT SEES ARMY → CHANGE STRATEGY
SCOUT FINISHES ROUTE → ASSUME THREAT ABSENT
SCOUT REACHES WAYPOINT → ASSUME INFORMATION ACQUIRED
```

The correct transitions require explicit intermediate evidence and authority.

For example:

```text
SCOUT SEES CAVALRY
      ↓
OBSERVATION
      ↓
THREAT CLASSIFICATION
      ↓
AEGIS CAPABILITY REQUIREMENT
      ↓
STRATEGIC ARBITRATION
```

---

# 38. Static forensic extraction required from donor

Before Muse writes a broad System 04 implementation, the following source-level inventory must be produced.

1. Every scouting-related `defconst`.
2. Every scouting-related goal write.
3. Every scouting-related strategic-number write.
4. Every scout mode definition.
5. Every mode-switch writer.
6. Every mode-switch reader.
7. Every movement command associated with scouting.
8. Every geometry calculation.
9. Every distance parameter.
10. Every map-size/map-type conditional affecting scouting.
11. Every sheep-search rule.
12. Every enemy-search rule.
13. Every circle-search rule.
14. Every border/flank/mirror/opposite/corner/center rule.
15. Every stuck detector.
16. Every stuck recovery path.
17. Every scouting timer.
18. Every scouting reset.
19. Every scouting completion condition.
20. Every external writer to scouting state.
21. Every consumer of scouting state.
22. Every target-acquisition dependency.
23. Every threat/inference dependency.
24. Every tactical dependency.
25. Every `up-jump-rule` affecting scouting.
26. Every duplicate or conditional scouting symbol.
27. Every apparently dead scouting rule.
28. Every writer whose effective precedence depends on source order.
29. Every state whose lifetime crosses scouting missions.
30. Every point where scouting state can become stale without an explicit reset.

This inventory is mandatory because the donor's global scale is substantial: the forensic baseline contains 1,956 rules, 1,503 constants, 1,193 goal writes, 440 strategic-number writes, and 188 jump calls. fileciteturn32file0L2-L2

---

# 39. Required scouting dependency graph

Muse must construct the concrete symbol-level graph:

```text
INFORMATION REQUIREMENT
        │
        ▼
SCOUT MODE AUTHORITY
        │
        ▼
SCOUT ASSIGNMENT
        │
        ▼
GEOMETRY / ROUTE POLICY
        │
        ▼
MOVEMENT EXECUTOR
        │
        ▼
WORLD OBSERVATION
        │
        ├───────────────┐
        ▼               ▼
TARGET ACQUISITION   ENEMY INFERENCE
        │               │
        └───────┬───────┘
                ▼
          THREAT / AEGIS
                │
                ▼
        NEW INFORMATION NEED
```

The final forensic graph must identify every concrete symbol, file, writer, reader, condition, and precedence edge.

---

# 40. Static versus runtime boundary

Static evidence can establish:

- a scout mode exists;
- a movement rule exists;
- a geometric pattern exists;
- a distance is computed;
- a stuck detector exists;
- a switch condition exists;
- a target/scouting dependency exists.

Runtime evidence is required to establish:

- the mode is actually selected;
- the movement command executes;
- the scout reaches the intended region;
- the world observation occurs;
- the observation enters the expected state carrier;
- target acquisition consumes the correct observation;
- stale information is refreshed;
- stuck recovery restores progress;
- information acquisition improves strategic behavior.

Do not promote static path existence to runtime scouting success.

---

# 41. Qualification sequence

System 04 should be qualified incrementally.

## S4-0 — Static inventory

Complete the 30-item donor extraction above.

## S4-1 — State ownership

Establish owner/writer/reader/precedence for every canonical scouting state carrier.

## S4-2 — Mode qualification

Demonstrate which scouting modes can actually become active and how switching occurs.

## S4-3 — Movement qualification

Demonstrate that a selected scout action produces the expected movement state.

## S4-4 — Observation qualification

Demonstrate that movement/search produces an observable information result.

## S4-5 — Target handoff

Demonstrate that a scouting observation correctly updates Target Acquisition state.

## S4-6 — Freshness qualification

Demonstrate stale observation detection and refresh behavior.

## S4-7 — Failure qualification

Demonstrate stuck recovery, no-target, unavailable-scout, and expired-request behavior.

## S4-8 — Strategic qualification

Demonstrate that information can alter AEGIS belief/objective selection without granting scouting strategic authority.

S4-8 must never be inferred from S4-0 through S4-2.

---

# 42. First implementation slice

The first implementation should not attempt to reproduce every donor scouting mode.

Recommended vertical slice:

```text
ONE SCOUT
   ↓
ONE INFORMATION REQUEST
   ↓
ONE SEARCH MODE
   ↓
ONE MOVEMENT PATH
   ↓
ONE OBSERVATION
   ↓
ONE STATE WRITE
   ↓
ONE TARGET / BELIEF CONSUMER
   ↓
VERIFICATION
```

The preferred first slice is **enemy-position refresh**, because it establishes the System 03 → System 04 → System 03 feedback loop without requiring the entire strategic architecture.

Secondary slice: sheep discovery → food-location observation → food-logistics consumer.

---

# 43. Donor preservation policy

| Donor capability | Disposition |
|---|---|
| Sheep scouting | PRESERVE + FORMALIZE information result |
| Enemy scouting | PRESERVE + FORMALIZE evidence interface |
| Circle scouting | PRESERVE search operator |
| Border search | PRESERVE search operator |
| Flank search | PRESERVE search operator |
| Mirror search | PRESERVE search operator |
| Opposite search | PRESERVE search operator |
| Corner search | PRESERVE search operator |
| Center search | PRESERVE search operator |
| Stuck recovery | PRESERVE + FORMALIZE failure lifecycle |
| Scouting switches | PRESERVE + EXPLICITATE authority |
| Map-dependent distances | PRESERVE pending semantic classification |
| Hardcoded unexplained coefficients | QUARANTINE pending provenance |
| Target side effects | SUBORDINATE to System 03 interface |
| Strategic side effects | REMOVE from scouting authority boundary |
| Duplicate state | CLASSIFY before transplant |
| Dead/legacy paths | QUARANTINE pending reachability proof |

---

# 44. Relationship to Systems 01–03

The architecture now forms a coherent information-control chain.

### System 01 — Initialization / Configuration

Defines environmental and engine-facing conditions under which scouting can operate.

### System 02 — State Namespace / Authority

Defines what scouting state means, who owns it, its lifetime, precedence, validity, and evidence semantics.

### System 03 — Target Acquisition

Defines how observations become target identity, target-object state, spatial target state, and target validity.

### System 04 — Scouting / Information Acquisition

Defines how missing information is actively acquired and returned to those consumers.

The resulting loop is:

```text
AEGIS / BELIEF
      ↓
INFORMATION REQUIREMENT
      ↓
SCOUTING
      ↓
OBSERVATION
      ↓
TARGET / BELIEF UPDATE
      ↓
AEGIS REASSESSMENT
```

This is the correct foundation for later threat and capability systems.

---

# 45. Strategic consequence: uncertainty becomes actionable

The most important architectural improvement introduced by System 04 is the transformation:

```text
UNKNOWN
```

from a passive absence of data into an explicit control condition:

```text
UNKNOWN
  ↓
INFORMATION REQUIREMENT
  ↓
SCOUTING ACTION
  ↓
OBSERVATION
  ↓
BELIEF UPDATE
```

This allows AEGIS to reason not only about what it believes, but also about **what it does not know and whether acquiring that information is worth the cost/risk**.

That is a substantial capability improvement over a bot that merely reacts to whatever its scouts happen to encounter.

---

# 46. Anti-patterns prohibited

### AP-01 — Randomized scouting disguised as strategy

Do not replace explicit information requirements with random exploration.

### AP-02 — Route completion = information completion

A route ending does not prove the requested information was acquired.

### AP-03 — Observation = belief

Do not skip classification/inference boundaries.

### AP-04 — Belief = strategic objective

Do not allow scouting observations to bypass strategic arbitration.

### AP-05 — Targeting owns movement

System 03 should request information; System 04 owns scout movement.

### AP-06 — Global freshness threshold

Different observations have different temporal validity.

### AP-07 — Mode thrashing

Do not allow every new signal to switch the scout immediately.

### AP-08 — Stuck = mission complete

Recovery commands do not prove information acquisition.

### AP-09 — Duplicate state merging without evidence

Same-looking symbols may have different conditional semantics.

### AP-10 — Static reachability = runtime qualification

Source presence is not runtime proof.

---

# 47. Engineering definition of done

System 04 is complete only when:

1. Every donor scouting mode is inventoried.
2. Every scouting state carrier has an owner and semantic type.
3. Every mode switch has a known writer and precedence or is explicitly unresolved.
4. Every geometry parameter has a documented semantic classification.
5. Scout movement is separated from information-result semantics.
6. Observations carry source/time/provenance semantics where required.
7. Target Acquisition consumes observations through an explicit interface.
8. Enemy-strategy inference remains a separate layer.
9. Threat evaluation remains a separate layer.
10. Stuck recovery has an explicit lifecycle.
11. Information requirements can expire/cancel/fail without corrupting unrelated scout state.
12. Emergency scouting can preempt normal scouting without destructive state loss.
13. Target refresh can request new information without taking control of scout movement.
14. Static and runtime evidence remain explicitly separated.
15. At least one complete scouting → observation → consumer vertical slice is qualified.
16. The donor's valuable geometric/search knowledge is preserved unless forensic evidence proves it defective.
17. New AEGIS abstractions are clearly labeled as generalizations rather than donor facts.

---

# 48. Hard invariants

**SC-01 — Scouting produces information; it does not own strategic interpretation.**

**SC-02 — Movement completion is not information completion.**

**SC-03 — Observation is not belief.**

**SC-04 — Belief is not strategic objective.**

**SC-05 — Target Acquisition and Scouting have separate authority boundaries.**

**SC-06 — Every critical observation has temporal semantics.**

**SC-07 — Stale observations must not be silently treated as current.**

**SC-08 — Scout-mode switching requires explicit authority and precedence.**

**SC-09 — Stuck recovery is a recovery transition, not proof of mission success.**

**SC-10 — Emergency scouting must be bounded and resumable where appropriate.**

**SC-11 — Duplicate scouting state must be classified before architectural reuse.**

**SC-12 — Static scouting logic is not runtime scouting proof.**

**SC-13 — A scouting information requirement may fail without implying strategic failure.**

**SC-14 — A failed scouting mission must not corrupt unrelated target or strategic state.**

**SC-15 — Information acquisition should be driven by explicit information need wherever AEGIS has sufficient authority to provide it.**

---

# 49. Final engineering directive to Muse

Do not reduce Shadow's scouting system to “send the scout around the map.” That throws away the most valuable part of the donor.

The donor already contains meaningful exploration knowledge: sheep search, enemy search, circle search, border/flank/mirror/opposite/corner/center patterns, map-dependent distances, switching, and stuck recovery. The forensic record explicitly identifies scouting as an active information-acquisition policy. fileciteturn27file0L2-L2

Extract that knowledge.

Then improve its architecture.

The correct System 04 boundary is:

```text
INFORMATION NEED
      ↓
SCOUTING AUTHORITY
      ↓
SEARCH MODE
      ↓
GEOMETRY / MOVEMENT
      ↓
OBSERVATION
      ↓
EVIDENCE
      ↓
TARGET / BELIEF UPDATE
      ↓
REASSESSMENT
```

Do not allow the scout subsystem to decide what the observation means strategically. Do not allow Target Acquisition to become a movement controller. Do not let a route-completion flag masquerade as knowledge. Do not let stale observations survive indefinitely. Do not throw away donor geometry merely because it is procedural.

Most importantly, use the new architecture to expose a capability the donor only partially expresses:

> **AEGIS should be able to recognize when it lacks information, determine whether that information matters, request acquisition of it, receive the resulting evidence, update its beliefs, and reassess the decision.**

That is the actual upgrade.

Shadow's scouting subsystem should become an **auditable active-sensing boundary**: donor search knowledge preserved, observation provenance explicit, state ownership controlled, temporal decay represented, failure recoverable, and strategic interpretation kept above the information-acquisition layer.

Do not build System 04 as a larger collection of scout rules. Build it as the mechanism that closes the loop between **uncertainty and observation**.
