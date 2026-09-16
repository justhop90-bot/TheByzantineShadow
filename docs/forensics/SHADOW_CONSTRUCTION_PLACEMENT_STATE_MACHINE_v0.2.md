# Shadow Construction + Placement State Machine v0.2

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per` on `main`  
**Canonical source SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Scope:** construction and placement control machine, with explicit state ownership, readers/writers, source-order/jump edges, completion, failure, and re-entry.

## 0. Status

**FORENSIC DESIGN BASELINE — STATIC — SUFFICIENT TO DESIGN THE CONTROL CONTRACT, NOT YET RUNTIME-QUALIFIED.**

This artifact is the current construction/placement design boundary. It supersedes any interpretation that `04_construction.per` or `07_placement.per` already reproduce Shadow. Those files are reconstruction scaffolding; this document records the donor machine that the eventual module contracts must preserve.

Evidence classes used here:

- **DIRECT:** exact predicate/action or source-state relationship recovered from `ShadowSource.per`.
- **COMPOSED:** multiple direct rules establish a state transition or dependency chain.
- **INFERRED:** architectural interpretation required to connect distributed rules.
- **UNKNOWN:** the source window or engine contract is insufficient to assert semantics.

Command issuance is never treated as completion. `release-escrow` is never treated as proof that escrow is physically zero. A skipped source region is not called a runtime failure unless the source establishes a failure/recovery predicate.

---

# 1. Executive machine model

Shadow construction is a persistent sequential/reactive machine. The active construction transaction is represented primarily by two persistent registers:

```text
                 STRATEGY / BUILD POLICY
                         |
                         v
                 gl-build-progress
                         |
                         v
                 gl-current-build-item
                         |
          +--------------+--------------+
          |              |              |
          v              v              v
      feasibility      search        preemption
          |              |              |
          v              v              v
      escrow        target object    SPLIT / pause
          |              |
          +------+-------+
                 v
          placement context
                 |
                 v
           build command
                 |
                 v
          WORLD OBSERVATION
          /       |        \
     pending   building    dropsite
      state      count      distance
          \       |        /
           +------+-------+
                  v
          progression reconcile
             /          \
          advance       rollback
             \          /
               re-entry
```

The important consequence is that **construction intent, resource commitment, search, placement, execution, completion, and recovery are coupled through persistent state and source-order control flow**. They are not independent transactions with a stack or return mechanism.

---

# 2. Persistent state ownership map

| State | Direct writers in recovered construction region | Readers / guards | Role | Status |
|---|---|---|---|---|
| `gl-current-build-item` | progression-selection rules for `FARMS`, `FARMS2`, `LC1`–`LC4`, `MILL1`, `GOLDMC1`, `GOLDMC2`, `STONEMC1` | construction executors, completion rules, skipped-state recovery, resource policy | active construction milestone | DIRECT |
| `gl-build-progress` | completion increments; skipped-state rollback; milestone correction | milestone selectors; construction triggers; trade/resource rules | ordered progression cursor | DIRECT |
| `gl-progression-pause` | distributed progression/interruption rules | construction/research executors and entry guards | temporary progression interruption gate | DIRECT existence; complete writer closure OPEN |
| `gl-escrow-state` | recovered setup/default rules and command preparation | `up-build ... gl-escrow-state` paths | engine accounting-mode selector | DIRECT; not logical commitment owner |
| `SPLIT` | farm and mining-camp arbitration rules | immediately following transaction rules | transient serialization scratch state | DIRECT |
| `goal gl-strategy` | broader strategic machine | almost every strategy-specific construction family | selects FLUSH/KRUSH/SIEGE behavior | DIRECT shared state |
| placement strategic numbers | construction/placement rules | engine placement executor | zone/failure/adjacency/separation configuration | DIRECT writer evidence |
| search target / search result | search rules | candidate-selection and point-transfer rules | candidate resource/build target | DIRECT |
| `t-build-delay` | construction timer rules | build/search entry predicates | anti-repeat timing gate | DIRECT |
| `MILL` | mill policy rules | mill construction / farm rules | mill request latch | DIRECT |
| `gl-dark-build` | dark-age build selection | LC1/MILL1 progression and rollback | initial construction branch | DIRECT |

No claim is made that each listed state has a single global owner. In Shadow, duplicate writers can be competing authorities and must be resolved by source order and predicates before transplantation.

---

# 3. Master construction state machine

## 3.1 State sequence

```text
S0  NO ACTIVE / PREVIOUS MILESTONE
 |
 | progression rule matches
 v
S1  MILESTONE SELECTED
     gl-current-build-item = X
 |
 | prerequisites + strategy + age + resources
 | + pending guards + pause guards
 v
S2  CONSTRUCTION AUTHORIZED / FEASIBLE
 |
 | ordinary building
 |       OR
 | resource-dependent building
 v
S3A DIRECT BUILD PATH       S3B SEARCH PATH
       |                         |
       |                         v
       |                    S4 SEARCH PREPARED
       |                         |
       |                    S5 CANDIDATE SELECTED
       |                         |
       |                    S6 POINT RESOLVED
       |                         |
       +-----------+-------------+
                   v
S7  PLACEMENT CONFIGURED
 |
 | escrow/release / placement data / builders
 v
S8  ENGINE BUILD COMMAND
 |
 +-------------------------+
 |                         |
 v                         v
S9  WORLD STATE             F-FAIL / NOT YET MATERIALIZED
OBSERVATION                    |
 |                              |
 | count / distance /            | failsafe / rollback / re-entry
 | pending state                 |
 v                              v
S10 COMPLETION RECOGNIZED     S11 PROGRESSION CORRECTED
 |                              |
 | progress +1                  | progress rewind / item restoration
 v                              |
S12 NEXT MILESTONE <------------+
 |
 v
S0 / S1 RE-ENTRY
```

This is a forensic state abstraction, not a claim that Shadow stores enumerated states `S0`–`S12`.

---

# 4. S1 — Milestone selection / intent

## Primary register

`gl-current-build-item`.

## Direct examples

The construction machine explicitly selects:

- `FARMS`;
- `FARMS2`;
- `LC1`;
- `LC2`;
- `LC3`;
- `LC4`;
- `MILL1`;
- `GOLDMC1`;
- `GOLDMC2`;
- `STONEMC1`.

## Writer pattern

```text
if strategy / dark-build / progression cursor identifies milestone X
and current item != X
    -> set current item X
    -> optionally establish LOW-ESCROW
```

Examples recovered directly:

- FLUSH farm selection sets `gl-current-build-item FARMS` and `LOW-ESCROW`.
- LC1 selection sets `gl-current-build-item LC1` and `LOW-ESCROW`.
- LC2/LC3 selection follows the same cursor-driven pattern.
- GOLDMC1/GOLDMC2 selection uses the progression cursor and strategy.

## Readers

The current item gates execution and completion. A construction executor can be reached only when the active item matches the transaction being executed.

## Important property

`gl-current-build-item` is therefore **intent/serialization state**, not proof that the corresponding building exists.

**Evidence:** DIRECT.

---

# 5. S2 — Feasibility and authorization gate

The construction command is downstream of several independent guards.

Typical guards include:

```text
strategy
+ age / time
+ current-build-item
+ gl-progression-pause
+ can-build / can-build-with-escrow
+ resource amount
+ pending-object / pending-placement count
+ existing building count
+ timer state
+ contextual priority
```

Examples:

- LC1 requires civilian-population / housing conditions, current item `LC1`, and `can-build-with-escrow lumber-camp`.
- GOLDMC1 requires current item, strategy, progression pause clear, `can-build-with-escrow mining-camp`, and building-count conditions.
- STONEMC1 requires fifth-turn, progression pause clear, current item, and `can-build-with-escrow mining-camp`.
- farm rules use `up-pending-objects c: farm < N` to prevent duplicate construction.

## Critical distinction

`can-build-with-escrow` establishes **feasibility under the current escrow/accounting context**. It does not establish that construction has started or completed.

**Evidence:** DIRECT.

---

# 6. S3 — Direct build path

Not every construction target requires a search transaction.

Examples include:

```text
build farm
build lumber-camp
build mill
up-build place-normal ...
up-build place-control ...
```

## Direct build sequence

```text
current item
 -> feasibility
 -> pending guard
 -> placement data / strategic numbers if required
 -> escrow release/rebalance
 -> build / up-build
 -> later world-state observation
```

### Farm example

The standard FLUSH farm path establishes `SPLIT`, checks farm-count/strategy conditions, then invokes:

`up-build place-normal gl-escrow-state c: farm`

A separate unconditional cleanup rule restores:

`gl-escrow-state = with-escrow` and `SPLIT = 0`.

The castle-age farm path uses `build farm` and then resets `SPLIT`.

### Lumber-camp example

LC1/LC2/LC3/LC4 use `build lumber-camp`, with explicit escrow percentages/releases and placement-related strategic-number changes in the later paths.

**Evidence:** DIRECT.

---

# 7. S3B–S6 — Placement/search state machine

The mining-camp families provide the clearest donor placement machine.

## 7.1 Search preparation

The canonical GOLDMC1 search path establishes:

```text
up-full-reset-search
 -> up-set-target-point home-x
 -> up-filter-distance -1 30
 -> focus-player setup
 -> up-find-remote gold-mine 40
 -> focus-player restoration
 -> up-clean-search search-remote 44 search-order-asc
 -> up-remove-objects search-remote -1 > 0
```

The STONEMC1 path uses the same structural pattern for `stone-mine` with its own search distance and cleanup parameters.

### State writes

- search set contents;
- target point/origin;
- focus-player context;
- filtered candidate ordering;
- removed-object state.

### State reads

- home point;
- candidate object types;
- target-player data;
- candidate distance;
- search ordering state.

**Evidence:** DIRECT.

---

# 8. Candidate selection

After search preparation, the build rule requires a target object:

`up-set-target-object search-remote c: 0`

This is a separate state transition from search preparation.

The machine therefore distinguishes:

```text
SEARCH SET
   !=
SELECTED TARGET OBJECT
```

The first surviving candidate is copied into target-object context. It is not correct to collapse `up-find-remote` into "choose the mine"; the subsequent cleanup and explicit target selection are separate source operations.

**Evidence:** DIRECT.

---

# 9. Point resolution

For the selected object, Shadow explicitly transfers object position into placement state:

```text
up-get-point position-object point-x
up-set-target-point point-x
```

This creates a second distinction:

```text
TARGET OBJECT
      ↓
TARGET POINT
```

The placement executor then consumes the target point.

This is strongest in GOLDMC1/GOLDMC2/STONEMC1.

**Evidence:** DIRECT.

---

# 10. Placement policy state

Shadow does not merely select a point. It writes placement configuration immediately before execution.

Recovered examples include:

```text
sn-placement-zone-size
sn-placement-fail-delta
sn-allow-adjacent-dropsites
sn-dropsite-separation-distance
```

Examples:

### GOLDMC1 KRUSH

- zone size `5`;
- fail delta `0`;
- adjacent dropsites `0`;
- separation `10`.

### GOLDMC2

- zone size `15`;
- fail delta `2`;
- adjacent dropsites `0`;
- separation `25`.

### STONEMC1

- zone size `5`;
- fail delta `10`;
- adjacent dropsites `0`;
- separation `10`.

### Housing

Housing additionally uses `up-set-placement-data` and `up-set-placement-data me -1 ...` variants, then `place-control` execution.

## Architectural consequence

The prior statement that placement geometry/failure policy is merely an external policy input is **not donor-proven**. Shadow itself writes placement parameters in the construction control region. Ownership of those parameters in ShadowByzantine remains a design decision that must be justified by the donor dependency graph.

**Evidence:** DIRECT for writer existence; ownership interpretation UNKNOWN.

---

# 11. S7 — Execution modes

Three distinct lower-level placement modes are directly established:

| Mode | Recovered use | Meaning established |
|---|---|---|
| `place-normal` | farms, lumber camps, failsafe mining camp | normal building placement | DIRECT |
| `place-control` | houses, mills | controlled placement context | DIRECT command form; exact engine semantics require reference validation |
| `place-point` | mining camps | explicit target-point placement | DIRECT |

The executor call is not itself a completion observer.

Examples:

```text
up-build place-point 0 c: mining-camp
up-build place-normal gl-escrow-state c: farm
up-build place-control gl-escrow-state c: house
```

The numeric/control argument is an engine ABI question and must be validated against AI Reference / AI Encyclopedia before implementation.

**Evidence:** DIRECT syntax; engine semantic meaning partly UNKNOWN.

---

# 12. Builder assignment state

Shadow explicitly calls:

```text
up-assign-builders c: house c: 1
up-assign-builders c: house c: 2
up-assign-builders c: house c: 3
up-assign-builders c: mill c: 1
```

This establishes builder assignment as an actual donor operation, not merely an inferred executor detail.

## Known behavior

- baseline house builder assignment exists as an unconditional rule;
- emergency housing paths use different builder counts;
- mill placement assigns one builder;
- house placement can change placement data before assigning builders.

## Unknown

The current source alone does not establish the full ABI semantics of the builder-count argument, whether assignment persists after failed placement, or whether another subsystem subsequently reclaims those builders.

Therefore `up-assign-builders` must be included in the module contract but its exact executor ownership remains **OPEN**.

---

# 13. S8 — Resource commitment / escrow boundary

Construction has multiple physical resource operations.

Typical pattern:

```text
set-escrow-percentage wood 0 / LOW-ESCROW
        |
        v
release-escrow wood
        |
        v
build / up-build
```

Mining-camp STONEMC1 additionally uses:

`set-escrow-percentage wood 0`

immediately around the build path.

`gl-escrow-state` is passed to some `up-build` calls but is not the owner of the logical milestone.

## Non-claims

The source does not prove:

- atomicity between release and build;
- physical escrow reaching zero immediately after `release-escrow`;
- that command success means resource deduction has occurred;
- that a failed placement automatically restores escrow.

Those are engine-semantics questions.

**Evidence:** DIRECT operation sequence; atomicity UNKNOWN.

---

# 14. S9/S10 — Completion observation

Shadow closes construction using **world-state proxies**, not the build command.

## Primary completion observations

### Building counts

Examples:

```text
building-type-count-total farm >= 4
building-type-count-total farm >= 7
building-type-count-total lumber-camp >= 1/2/3/4
building-type-count-total mill >= 1
building-type-count-total mining-camp >= 3
```

### Dropsite distance

GOLDMC1/GOLDMC2/STONEMC1 also use:

```text
dropsite-min-distance gold ...
dropsite-min-distance stone ...
```

These are particularly important because the construction objective is partly geometric/resource-access based rather than only a raw building count.

## Completion transition

```text
current item X
 + observed world state satisfies X
      -> gl-build-progress += 1
```

Examples:

- `LC1` count >= 1 → progress +1;
- `LC2` count >= 2 → progress +1;
- `LC3` count >= 3 → progress +1;
- `LC4` count >= 4 → progress +1;
- `MILL1` count >= 1 → progress +1;
- `GOLDMC1` distance condition → progress +1;
- `GOLDMC2` mining-camp count >= 3 → progress +1.

The source thereby demonstrates a persistent distinction:

```text
COMMAND
  !=
COMPLETION
```

**Evidence:** DIRECT.

---

# 15. S11 — Failure / skipped-state recovery

The donor contains several different recovery mechanisms. They must not be collapsed into a generic "failure" state.

## 15.1 Progression rollback

Canonical pattern:

```text
if expected building is absent
and gl-build-progress > milestone
    -> set gl-build-progress = milestone
```

Examples:

- farms reset to `FarmsNumber` / `KrushFarmsNumber`;
- LC1/LC2/LC3/LC4 reset to their corresponding milestone constants;
- MILL1 resets according to `MillFirst` / `LumberFirst` branch;
- GOLDMC1/GOLDMC2/STONEMC1 have analogous correction rules.

This proves that `gl-build-progress` is a **recoverable cursor**, not a monotonic completed-build counter.

## 15.2 Current-item restoration

Canonical pattern:

```text
if gl-build-progress == X
and current item != expected item
    -> set current item = expected item
```

This repairs a progression/item mismatch.

## 15.3 Failsafe build path

Mining-camp families contain explicit failsafe rules. For example, GOLDMC1 has a path that, under a time/strategy condition and with a mining camp already present, invokes a normal mining-camp build rather than the remote-search placement path.

This is not equivalent to search failure; it is a **separate alternate executor path**.

## 15.4 Timer suppression

`up-timer-status t-build-delay != timer-running` and related timer writes suppress repeated construction attempts.

The timer therefore participates in control-state stabilization.

## 15.5 Pending-object suppression

Predicates such as:

`up-pending-objects c: farm < 1`

prevent the machine from issuing duplicate construction commands while an object is pending.

This is an anti-duplication guard, not completion.

## 15.6 Actual placement failure semantics

**UNKNOWN.** The recovered source establishes failsafes, rollback, pending guards, and re-entry, but does not by itself prove that a failed `place-point` command produces a specific engine failure event or that Shadow explicitly receives such an event.

The engine ABI must be established before defining a separate placement-failure state in ShadowByzantine.

---

# 16. S12 — Re-entry

Shadow's re-entry is distributed.

The principal paths are:

```text
WORLD OBSERVATION
      |
      +--> completion
      |       |
      |       +--> progress +1
      |       +--> next current item
      |
      +--> expected state absent
              |
              +--> progress rollback
              +--> current-item restoration
              +--> re-run feasibility/search/execution
```

Additional re-entry mechanisms include:

- clearing `gl-progression-pause`;
- resetting `SPLIT` to `0`;
- releasing/rebalancing escrow;
- timer expiration;
- source-order fall-through into the next progression rules;
- jump-based bypass of inappropriate source regions.

There is no return stack. A jump is a control-flow edge to a source-order location; re-entry is achieved because persistent state makes later predicates true again.

**Evidence:** DIRECT/COMPOSED.

---

# 17. Explicit jump edges affecting construction

## Rule 1794

```text
rule 1794
   |
   | up-jump-rule 1
   v
skip rule 1795
```

The predicate tests whether the current item is `MARKET1`, a blacksmith placement is pending, or strategy is not FLUSH. Therefore the farm arbitration block immediately following is bypassed under those conditions.

This is a **source-level bypass edge**, not a semantic priority label.

## Lumber-camp fourth-stage bypass

A `true` rule containing:

`up-jump-rule 4`

is immediately before the LC4 executor. This explicitly bypasses a source region before LC4 execution. The exact semantic reason must be preserved as control flow even where the predicate is unconditional.

## Broader construction jump closure

The 1794–1896 interval contains additional source-order coupling, but the present artifact does not promote unbounded or truncated source windows to exact jump edges. Any jump not directly recovered is marked OPEN rather than inferred.

**Evidence discipline:** source order and explicit jump operands are authoritative; conceptual priority is not substituted for them.

---

# 18. Construction families as concrete state machines

## 18.1 FARMS / FARMS2

```text
strategy=KRUSH
 -> current item FARMS
 -> dark-age feasibility
 -> pending farm guard
 -> release wood
 -> build farm
 -> farm count >= 4
 -> progress +1
 -> next milestone / restoration if skipped

strategy=KRUSH
 -> current item FARMS2
 -> feasibility
 -> release wood
 -> build farm
 -> farm count >= 7
 -> progress +1
```

FLUSH has a corresponding farm sequence with different resource thresholds and `LOW-ESCROW` policy.

## 18.2 LC1–LC4

```text
LC1
 -> select from dark-build + progress
 -> LOW-ESCROW
 -> feasibility
 -> placement adjacency policy
 -> release wood
 -> build lumber camp
 -> count >= 1
 -> progress +1

LC2
 -> select
 -> resource/time/housing gate
 -> placement policy
 -> release wood
 -> build
 -> count >= 2
 -> progress +1

LC3
 -> select
 -> pause clear + feasibility
 -> placement policy
 -> release wood
 -> build
 -> count >= 3
 -> progress +1

LC4
 -> select
 -> pause clear + feasibility
 -> release wood
 -> build
 -> count >= 4
 -> progress +1
```

Each stage has skipped-state rollback and current-item restoration.

## 18.3 MILL1

```text
select MILL1
 -> resource-found food OR SkipMillTime
 -> timer clear
 -> placement adjacency policy
 -> release wood
 -> build mill
 -> mill count >= 1
 -> progress +1
 -> re-entry
```

Separate mill policy can later request additional mills using farm-count thresholds and pending-placement guards.

## 18.4 GOLDMC1

```text
select GOLDMC1
 -> pause clear
 -> can-build-with-escrow
 -> search gold
 -> filter/order/remove
 -> select candidate
 -> distance condition
 -> SPLIT
 -> resolve point
 -> placement policy
 -> release wood
 -> place-point
 -> observe dropsite geometry
 -> progress +1
```

There is also a normal-placement failsafe path under explicit conditions.

## 18.5 GOLDMC2

```text
progress reaches GoldMC2Number
 -> restore current item GOLDMC2
 -> LOW-ESCROW
 -> search/placement transaction
 -> mining-camp world-state observation
 -> progress +1
```

The canonical rule 1890 is explicitly `(false)` and therefore must not be represented as active runtime behavior merely because its body is a placement transaction.

## 18.6 STONEMC1

```text
current item STONEMC1
 -> fifth-turn + pause clear
 -> can-build-with-escrow
 -> search stone
 -> filter/order/remove
 -> select candidate
 -> resolve point
 -> placement policy
 -> release wood
 -> escrow percentage 0
 -> place-point
 -> observe stone dropsite distance
 -> progression correction / re-entry
```

---

# 19. Housing is a parallel preemption machine

Housing is not simply another sequential milestone.

Its source rules include:

```text
housing headroom low
 + population headroom nonzero
 + can-build-with-escrow house
 + pending-house guard
      |
      v
place-control
      |
      v
builder assignment
```

Thresholds vary by context (`<5`, `<4`, `<10`, `<15`, etc.). Some rules are strategy-dependent; some use archery-range/stable/siege-workshop state.

One path serializes through `SPLIT` before placement.

Therefore housing can **preempt or compete with the ordinary economic construction progression**.

This is an important cross-region edge: the finished construction module cannot assume `gl-current-build-item` is the sole source of all construction commands.

**Evidence:** DIRECT.

---

# 20. Writer/reader dependency closure

## `gl-current-build-item`

```text
writers:
  progression milestone selectors
  skipped-state restoration rules

readers:
  build executors
  completion observers
  escrow/resource policy
  farm arbitration
  search/placement paths
  trade/resource conditions
```

## `gl-build-progress`

```text
writers:
  completion rules: +1
  skipped-state recovery: set milestone
  skipped-state correction: rewind

readers:
  milestone selectors
  resource/trade rules
  strategy progression
  construction/research transitions
```

## `gl-progression-pause`

```text
writers:
  distributed progression interruption rules

readers:
  construction and research entry predicates
  mining-camp execution
```

Full writer closure remains OPEN.

## `SPLIT`

```text
writers:
  farm arbitration
  mining-camp arbitration
  house arbitration

readers:
  immediately following serialized executor rules

cleanup:
  explicit reset to 0
```

## Placement strategic numbers

```text
writers:
  construction/placement rules

readers:
  engine placement operation

ownership:
  donor writer exists; AEGIS module ownership not yet decided
```

---

# 21. Cross-region dependencies

```text
                    ECONOMIC OBSERVATION
                           |
                           v
                 resource / escrow state
                           |
          +----------------+----------------+
          |                |                |
          v                v                v
     CONSTRUCTION       RESEARCH        PRODUCTION
          |                |                |
          +--------+-------+----------------+
                   |
                   v
            gl-build-progress
                   |
                   v
         gl-current-build-item
                   |
          +--------+--------+
          |                 |
          v                 v
      placement         feasibility
          |                 |
          +--------+--------+
                   v
              execution
                   |
                   v
             world state
                   |
                   v
              completion
                   |
                   v
              progression
```

Military/defense state can enter this graph through preemption and strategic policy, but the complete military→construction edge closure remains a broader forensic task.

---

# 22. What is now design-ready

The following contracts can now be designed without inventing the donor's basic state model:

### Construction authority

Must own or explicitly arbitrate:

- active construction milestone;
- progression cursor;
- construction feasibility;
- pending guards;
- completion observation;
- progression advancement/rollback;
- re-entry.

### Placement authority

Must expose:

- target-object state;
- target-point state;
- search preparation;
- candidate selection;
- placement configuration;
- placement-mode selection;
- failure/retry status once engine semantics are known.

### Execution boundary

Must consume a declared ABI for:

- `build`;
- `up-build`;
- `place-normal`;
- `place-control`;
- `place-point`;
- `up-assign-builders`;
- pending-object/pending-placement observations.

### Verification boundary

Must distinguish:

```text
command issued
    !=
pending
    !=
world object exists
    !=
objective geometry satisfied
    !=
progression milestone accepted
```

### Recovery boundary

Must preserve:

- rollback;
- current-item restoration;
- timer stabilization;
- pending guards;
- failsafe alternate paths;
- source-order re-entry.

---

# 23. What remains before implementation

The construction state machine is sufficiently recovered to design **contracts**, but these items remain engine/source gates before faithful implementation:

1. **Complete writer closure** for `gl-progression-pause`.
2. **Complete jump closure** across rules 1794–1896.
3. **Exact `up-assign-builders` ABI.**
4. **Exact `up-build` ABI** for all three placement modes.
5. **Exact `up-pending-objects` / `up-pending-placement` semantics.**
6. **Search failure semantics:** whether failed/empty searches expose an observable engine state and how Shadow reacts to it.
7. **Builder ownership/reclamation** after placement and failed placement.
8. **Runtime qualification** of at least one direct-build and one point-placement transaction.
9. **Collision audit** against existing ShadowByzantine construction/placement writers.
10. **AI Reference / AI Encyclopedia triangulation** for engine semantics, not architecture invention.

These are now bounded questions rather than an undefined construction problem.

---

# 24. Module-design consequence

The evidence now supports a module design centered on **control regions**, not generic transaction layers:

```text
04_CONSTRUCTION_AUTHORITY
    |
    +-- progression / current-item
    +-- feasibility / pending guards
    +-- construction arbitration
    +-- completion / rollback
    +-- re-entry

07_PLACEMENT_EXECUTION_BOUNDARY
    |
    +-- search state
    +-- target object
    +-- target point
    +-- placement configuration
    +-- placement mode
    +-- builder handoff

CROSS-CUTTING ABI
    |
    +-- escrow
    +-- timers
    +-- engine pending state
    +-- world-state verification
    +-- source-order / jump topology
```

This does **not** mean Shadow itself had files with these names. It means these are now defensible design boundaries for ShadowByzantine because the underlying donor control regions and state dependencies have been recovered sufficiently to specify them.

The implementation must preserve the donor distinctions before introducing Byzantine policy.

---

# 25. Provenance rule for implementation

Every implementation decision derived from this document must be tagged conceptually as one of:

- **SHADOW-DERIVED** — directly preserving donor behavior/control structure;
- **ENGINE-SEMANTICS** — established by AI Reference / AI Encyclopedia / runtime evidence;
- **BYZANTINE-POLICY** — civilization-specific adaptation;
- **PROJECT-IMPROVEMENT** — deliberate new behavior.

A donor mechanism must not be relabeled as a Byzantine requirement merely because Byzantines benefit from it.

---

# 26. Final forensic verdict

The construction/placement problem is no longer "we need a construction module." The donor machine is now understood as:

```text
PROGRESSION CURSOR
      ↓
ACTIVE MILESTONE
      ↓
FEASIBILITY + PENDING GUARD
      ↓
  +---+----------------+
  |                    |
DIRECT BUILD       SEARCH BUILD
  |                    |
  |              SEARCH PREP
  |                    |
  |              CANDIDATE
  |                    |
  |              TARGET POINT
  |                    |
  +--------+-----------+
           ↓
   PLACEMENT CONFIG
           ↓
   ESCROW / BUILDERS
           ↓
      ENGINE COMMAND
           ↓
    WORLD OBSERVATION
      /          \
 COMPLETE       NOT MATERIALIZED
   /   |              |
 +1  NEXT        ROLLBACK / FAILSAFE
   \   |              /
    \  +-------------+
       RE-ENTRY
```

The major architectural fact is that **completion and recovery are part of the construction machine itself**. They cannot be bolted on after the executor.

The major placement fact is that **search, candidate selection, point transfer, placement configuration, and placement-mode execution are separate source-level operations**.

The major evidence gap is now narrow: **engine ABI + full jump/writer closure + runtime qualification**. Once those are closed, the construction and placement modules can be implemented against explicit contracts rather than reconstructed from intuition.

---

## Primary evidence

- `ShadowSource.per`, canonical blob `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`.
- `docs/forensics/SHADOW_CONSTRUCTION_RULE_EXTRACTION_1794_1896_2026-09-16.md`.
- `docs/forensics/SHADOW_CONSTRUCTION_FORENSIC_PASS2_1801_1896_2026-09-16.md`.
- `docs/forensics/SHADOWSOURCE_CONTROL_REGION_ATLAS_v0.1.md`.
- `docs/AI_SCRIPTER_OPERATING_DOCTRINE.md`.

## Verification

- Exact construction rule bodies already recovered for 1794–1800 and 1890–1896.
- Construction interval 1801–1896 recovered through bounded source windows recorded in the forensic pass.
- World-state completion and skipped-state rollback are explicitly represented in source.
- Point-placement search pipeline is explicitly represented for mining camps.
- Disabled rule 1890 is preserved as disabled rather than promoted to active behavior.

## Uncertainty

- Runtime firing is not established by source order.
- Engine semantics of placement/build arguments remain partly unresolved.
- Search-empty/failure signaling remains unresolved.
- Full writer closure and jump closure remain incomplete.
- No claim is made that the current ShadowByzantine implementation reproduces this machine.
