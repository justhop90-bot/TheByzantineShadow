# ShadowSource Control-Region Atlas v0.1

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per` on `main`  
**Canonical source SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Canonical source size:** 615,773 UTF-8 bytes / 22,604 lines / 1,956 `defrule` blocks  
**Historical donor:** Shadow DC7, commit `1d9f45b3b9ac03adc24103df2b21c84b92a45fb6`  

## 0. Purpose

This atlas defines the first control-region decomposition of the canonical Shadow rule machine. It is deliberately **not** a proposed software-module architecture. A control region is a connected behavioral neighborhood in the source-order/control-flow/dataflow machine; it may cross conceptual subsystem boundaries and may share state with other regions.

The atlas records, for each recovered region:

- canonical source/rule range;
- entry conditions;
- exit/re-entry conditions;
- explicit jump edges;
- persistent state reads/writes;
- engine observations and commands;
- escrow operations;
- completion observations;
- release/restoration behavior;
- cross-region dependencies;
- evidence/qualification status.

### Evidence rule

A source range is authoritative only where the underlying source window has been recovered. Where the exact outer boundary has not yet been exhaustively recovered, the atlas marks the boundary **PROVISIONAL** rather than inventing a line/rule endpoint. Rule-level evidence is stronger than semantic naming.

This document therefore supersedes the earlier assumption that Shadow should be reconstructed as a stack of independent `requirements -> capital -> escrow -> authority -> execution -> verification` modules. Those are useful analytical stages, but the donor is implemented as a persistent sequential/reactive machine whose behavioral regions share goals, timers, strategic numbers, jumps, engine observations, and execution primitives.

---

# 1. Machine model

The canonical machine is best represented as:

```text
ENGINE / WORLD
     |
     v
OBSERVATION REGIONS
     |
     v
PERSISTENT SHADOW STATE
(goals / timers / strategic numbers / coordinates / cursors)
     |
     v
SOURCE-ORDER CONTROL FLOW
(normal successor + up-jump-rule + disable-self)
     |
     +----------------+----------------+----------------+
     v                v                v                v
 ECONOMY          RESEARCH        CONSTRUCTION      MILITARY
     |                |                |                |
     +----------------+----------------+----------------+
                              |
                              v
                    ESCROW / PROGRESSION
                              |
                              v
                         ENGINE COMMAND
                              |
                              v
                       WORLD OBSERVATION
                              |
                              +------> RE-ENTRY
```

Escrow is therefore an actuator shared by multiple control regions, not a standalone strategic owner. `gl-escrow-state` is an engine accounting-mode selector (`with-escrow` / `without-escrow`), not a logical transaction owner. The physical resource-protection mechanism is distributed through `up-modify-escrow`, `set-escrow-percentage`, and `release-escrow`, coordinated by progression state such as `gl-progression-pause`, `gl-current-build-item`, and `gl-build-progress`.

---

# 2. Region index

| ID | Control region | Canonical source/rule range | Boundary status | Primary role |
|---|---|---|---|---|
| R00 | Bootstrap / global declarations | file header through early declarations; rules 1–3 explicitly recovered | PARTIAL | constants, timers, goal namespace, one-time initialization |
| R01 | Engine-state acquisition / economic telemetry | rules 4–8; source L1791–1845 | CONFIRMED WINDOW | home/scout/resource/escrow state acquisition |
| R02 | Military baseline / tactical initialization | rules 14–27; source L1938–2064 | CONFIRMED WINDOW | group state, ranges, tactical baselines, ranged evaluation entry |
| R03 | Ranged tactical evaluation | begins rule 27; source L2058 onward | PROVISIONAL OUTER BOUNDARY | combat-state scoring, group/range evaluation, jump-based bypass |
| R04 | Economic/progression control substrate | representative recovered rules 581–591 and 1165–1167; broader boundary still being mapped | PROVISIONAL | resource allocation, drops, progression state, gatherer policy |
| R05 | Technology/progression and escrow interruption | rules 1165–1250; source L14127–14508+ | CONFIRMED CORE WINDOW | FLUSH/KRUSH progression, research interruption, escrow-aware research |
| R06 | Research-family completion/reconciliation | rules 1172–1250, with shared progression writers/readers | CONFIRMED CORE WINDOW | cursor correction, current item, research status, progress advancement |
| R07 | Construction progression | rules 1794–1896; source L20920–22200 | CONFIRMED | farms, housing, lumber camps, mills, mining camps, university/ballistics |
| R08 | Placement/search submachine | embedded in construction, especially mining camps; rules around GOLDMC1/GOLDMC2/STONEMC1 | CONFIRMED CORE | search reset, candidate selection, point resolution, placement policy |
| R09 | Military/scouting/tactical control | broad source-order neighborhood; exact outer boundary remains to be segmented | PROVISIONAL | scouting, groups, raids, targets, march, attack, retreat |
| R10 | Defense/emergency interruption | distributed across military/economic/building neighborhoods | PROVISIONAL | town-under-attack, defensive posture, preemption, resource/progression interruption |
| R11 | Global recovery/re-entry | distributed; no single contiguous block established | PROVISIONAL | state reconciliation, progression recovery, re-entry after exceptional paths |

**Important:** R05 and R06 are analytically separable but are not independent donor modules. Their source paths repeatedly interleave trigger, cursor, escrow, command, observation, release, and re-entry behavior.

---

# 3. R00 — Bootstrap / global declarations

## Source

- File header and declaration section.
- Explicit recovered rule 1: L1–L5.
- Explicit recovered rule 2: L7–L13.
- Explicit recovered initializer rule 3: L1451–L1456.

## Entry

Initial engine evaluation / source-order entry.

## State reads

Global engine identity and initialization predicates.

## State writes

The declaration section establishes the semantic namespace for major persistent state, including:

- strategy/group state;
- attack and defense state;
- target IDs and coordinates;
- raid/march coordinates;
- scouting state;
- build progression;
- economic thresholds;
- timers;
- escrow policy constants.

Rule 3 initializes `gl-scout-unit` and self-disables.

## Engine operations

Rules 1–2 are diagnostic/taunt instrumentation. They do not constitute strategic authority.

## Jump edges

No strategic jump is established in the recovered initializer itself.

## Completion/release

Not applicable.

## Cross-region edges

This region supplies the namespace and initial values consumed by every later region. The declaration layer is therefore global substrate, not a behavior module.

## Qualification

**DIRECT / STATIC / CONFIRMED** for the recovered rules and declarations. It does not prove runtime firing of every declaration-dependent path.

---

# 4. R01 — Engine-state acquisition / economic telemetry

## Source

- Rule 4: L1791–1800.
- Rule 5: L1802–1810.
- Rule 6: L1812–1819.
- Rule 7: L1821–1832.
- Rule 8: L1834–1845.

## Entry

Rule 4 requires a Town Center; rule 5 requires a Scout Cavalry population. Rules 6–8 are unconditional observation/update rules in the recovered source window.

## State reads

- Town Center count.
- Scout Cavalry count.
- engine escrow amounts for food/wood/gold/stone.
- total resource amounts.
- map center / map size / positional state.

## State writes

- home/scout coordinates;
- `gl-food-escrow`, `gl-wood-escrow`, `gl-gold-escrow`, `gl-stone-escrow`;
- total resource registers;
- net resource registers after subtracting escrow;
- map-coordinate state.

## Engine commands/observations

- `up-full-reset-search`
- `up-find-local`
- `up-set-target-object`
- `up-get-object-data`
- `up-get-point`
- `up-get-fact` for escrow/resource quantities.

These are primarily observations/state acquisition, not strategic execution.

## Escrow operations

No physical escrow mutation is performed here. The region observes actual escrow and computes net resources.

## Completion

Observation completion is the presence of the required engine fact; no strategic transaction is declared complete here.

## Cross-region edges

The resulting resource/escrow state feeds economic feasibility, production, construction, research, and military decision regions. This is a key shared-state boundary.

## Qualification

**DIRECT / STATIC / CONFIRMED WINDOW.**

---

# 5. R02 — Military baseline / tactical initialization

## Source

- Rules 14–27; recovered windows L1938–2064.
- Rule 16 L1957–1978 is the principal one-time military initializer.
- Rule 27 L2058–2064 is the first confirmed jump-based ranged-evaluation bypass.

## Entry

Global source-order evaluation reaches military initialization. Some preceding diagnostic rules are explicitly disabled/false and are not treated as live strategic entry paths.

## State reads

- military group existence/size;
- current group;
- Town safety;
- group positions;
- completed technologies;
- local tactical geometry.

## State writes

Representative persistent state established by rule 16:

- `gl-defend-town`;
- `gl-current-group`;
- `sn-number-tasked-units`;
- `gl-max-ranged-group-size`;
- `gl-range-advantage`;
- `gl-ranged-group-state`;
- `gl-can-fire` / `gl-raid-can-fire`;
- enemy and own tower ranges;
- ranged/raid group ranges;
- march type;
- close-ranged-group range.

Rules 17–26 build tactical tracking/range state from geometry and completed technologies.

## Engine operations

- group-size queries;
- point-distance queries;
- research completion observations;
- search/fact operations in some branches.

## Jump edges

Rule 27: `up-jump-rule 44` → rule 72 under the recovered jump semantics. This is an explicit control-flow bypass, not merely a priority annotation.

## Completion/release

No resource transaction completion is established in this region. It prepares tactical state used by later military regions.

## Cross-region edges

- Research completion changes tactical ranges.
- Military state can affect construction/economic defense.
- Group/tactical state feeds target selection and combat execution.

## Qualification

**DIRECT / STATIC / CONFIRMED WINDOW.**

---

# 6. R03 — Ranged tactical evaluation

## Source

- Begins at least at rule 27 / L2058–2064.
- Continues through the ranged evaluation neighborhood; exact terminal rule is not yet declared authoritative in this atlas.

## Entry

Rule 27 enters this region when ranged-group existence/geometry makes the preceding state inappropriate; otherwise it can jump over the evaluation block.

## State reads

- ranged group size;
- ranged/enemy group coordinates;
- research status;
- `gl-ranged-eval`;
- tracking/range state;
- tactical geometry;
- military state.

## State writes

- `gl-ranged-eval`;
- tactical scoring registers;
- group/range decisions;
- downstream combat-state variables.

## Engine operations

- point-distance and group-size queries;
- research-state observations;
- search operations in diagnostic/conditional branches.

## Jump edges

Rule 27 → rule 72 is explicitly confirmed.

The broader source-order matrix contains additional jump-based control flow; exact region-local jump closure remains a follow-up segmentation task.

## Escrow

No direct escrow mutation is established in the confirmed opening window.

## Completion/release

This region produces tactical state rather than a terminal economic transaction.

## Cross-region edges

Research completion alters tactical range evaluation; tactical output feeds attack/retreat/target regions and can indirectly alter production/construction priorities.

## Qualification

**STATIC / PROVISIONAL OUTER BOUNDARY.**

---

# 7. R04 — Economic/progression control substrate

## Source evidence

Representative recovered source-order windows include:

- rules 581–591, source L7950–8074: lumber-camp/range/forced-resource drops and progression conditions;
- rules 1165–1167, source L14127–14163: FLUSH progression and gatherer-percentage transitions.

The complete economic-region outer boundary is not yet certified as one contiguous source range because Shadow repeatedly interleaves economic progression with research, construction, production, and tactical state.

## Entry

Resource amounts, strategy, age, timers, build item, and progression state.

## State reads

- `gl-strategy`;
- `gl-build-progress`;
- `gl-current-build-item`;
- resource amounts;
- age/age-time;
- timers;
- escrow/net-resource state.

## State writes

- gatherer percentages;
- progression cursor;
- current build item;
- resource drops;
- temporary economic policy;
- timers and economic switches.

## Engine commands

- `up-drop-resources`;
- strategic-number writes;
- engine fact observations.

## Escrow

Economic policy is a major writer of escrow percentages and release behavior, but the exact full writer closure is distributed.

## Completion

Economic progression commonly uses observed resource/building/research state rather than command issuance as its closure condition.

## Cross-region edges

This region is a principal shared-state substrate for research, construction, and production. `gl-strategy`, `gl-build-progress`, and resource/escrow state are read by all three.

## Qualification

**COMPOSED / STATIC / PROVISIONAL boundary.**

---

# 8. R05 — Technology/progression + escrow interruption

## Source

Core confirmed interval:

- rules 1165–1167: L14127–14163;
- rules 1172–1250: approximately L14294 onward through the research-family closure.

The active research escrow families are:

- F01 Scale Mail: 1172–1174;
- F02 Chain Mail: 1175–1177;
- F03 Iron Casting KRUSH: 1178–1182;
- F04 Iron Casting FLUSH: 1183–1187;
- F05 Forging FLUSH/KRUSH branches: 1188–1197;
- F06/F07/F08 Chain Barding branches: 1198–1207;
- F09 Scale Barding KRUSH: 1208–1212;
- F10 Fletching: 1236–1240;
- F11 Leather Archer Armor: 1241–1245;
- F12 Padded Archer Armor: 1246–1250.

## Entry

Typical entry predicates combine:

- `gl-strategy` (FLUSH/KRUSH);
- age and age-time;
- `gl-progression-pause == -1`;
- prerequisite buildings/technologies;
- enemy strategic/composition observations;
- `gl-current-build-item`;
- research status;
- progression milestones.

## State reads

- `gl-strategy`;
- `gl-progression-pause`;
- `gl-build-progress`;
- `gl-current-build-item`;
- research status/completion;
- enemy strategy/composition;
- age/timers;
- `gl-escrow-state` at command time.

## State writes

- `gl-progression-pause`;
- `gl-build-progress`;
- `gl-current-build-item`;
- resource escrow percentages/amounts;
- temporary strategic policy.

## Escrow operations

Confirmed operations include:

- `up-modify-escrow`;
- `set-escrow-percentage`;
- `release-escrow`;
- `can-research-with-escrow`.

Examples:

```text
Scale Mail:
trigger -> pause=SCALEMAIL -> food escrow +100 -> can-research -> up-research
-> pause=-1 -> food escrow percentage 0 -> release food

Chain Mail:
trigger -> pause=CHAINMAIL -> food+200/gold+100
-> can-research -> up-research -> clear pause -> zero percentages -> release
```

## Engine commands

Primary modern path:

`up-research gl-escrow-state c: <research>`.

Legacy mixed-generation paths exist for Fletching and Padded Archer Armor using `research` rather than the exact modern `up-research` form.

## Completion observations

Research families use `up-research-status` / `research-completed` state. For Iron Casting, Forging, Chain Barding, Scale Barding, Leather Archer Armor, and Padded Archer Armor families, completion/reconciliation rules explicitly advance `gl-build-progress` after the required research status is observed.

Command issuance is not completion.

## Release behavior

Release is explicit and commonly occurs in the command/reconciliation sequence. `release-escrow` itself is an operation, not proof that the physical escrow has reached zero.

## Re-entry

Clearing `gl-progression-pause`, advancing `gl-build-progress`, and setting the next `gl-current-build-item` return control to the broader progression machine.

## Cross-region edges

- Military/threat state can trigger research interruptions.
- Economic resource/escrow policy supplies feasibility.
- Research completion modifies military capability/range state.
- Construction/progression consumes the same `gl-build-progress` / `gl-current-build-item` substrate.
- Production eligibility is affected by research/progression state.

## Qualification

**DIRECT + COMPOSED / STATIC / CONFIRMED CORE.** Runtime firing is not established solely by source reachability.

---

# 9. R06 — Research completion / progression reconciliation

## Source

Same research interval, especially the cursor/current-item/completion rules surrounding 1179–1212 and 1237–1250.

## Entry

Observed research status indicates either:

1. progression has advanced beyond the expected milestone; or
2. the current build item is not aligned with the stored progression cursor.

## State reads

- `gl-build-progress`;
- milestone constants;
- `gl-current-build-item`;
- `gl-strategy`;
- research status.

## State writes

- rollback/correction of `gl-build-progress`;
- restoration of `gl-current-build-item`;
- increment of `gl-build-progress` after observed completion.

## Engine operations

Research-status predicates and completion facts; no completion inference from command issuance.

## Escrow

Reads the shared escrow policy context; some rules modify/release escrow, but completion reconciliation itself is conceptually distinct from the physical escrow operation.

## Completion

`up-research-status >= research-pending` or corresponding completion predicates establish the observed progression condition used by the family.

## Cross-region edges

This region is the bridge between research and construction/progression. It demonstrates that `gl-build-progress` is a recoverable cursor, not a write-once build-order counter.

## Qualification

**DIRECT / STATIC / CONFIRMED.**

---

# 10. R07 — Construction progression machine

## Source

Rules 1794–1896. The canonical source interval was recovered through source windows L20920–22200.

Confirmed windows:

- L20920–21180: farms, FLUSH/KRUSH farm state, housing preemption/placement, QLC entry;
- L21181–21480: lumber camps LC1–LC4, timer path, market/trading, mill progression, first mining-camp entry;
- L21481–21780: mill/mining-camp machinery and GOLDMC1 search/build;
- L21781–22000: GOLDMC1 KRUSH/FLUSH, GOLDMC2 transition, disabled GOLDMC2 experiment, STONEMC1 setup;
- L22001–22200: GOLDMC2/STONEMC1 completion, additional mining camp, university, ballistics, terminal timer marker.

## Entry

Construction intent is established through:

- `gl-current-build-item`;
- `gl-build-progress`;
- strategy (`FLUSH`/`KRUSH`);
- age/time;
- building counts;
- pending object/placement state;
- resource/escrow feasibility;
- housing pressure and other preemption conditions.

## State reads

- `gl-current-build-item`;
- `gl-build-progress`;
- `gl-strategy`;
- `gl-progression-pause`;
- building counts;
- pending objects/placement;
- dropsite distances;
- resource amounts;
- escrow state;
- timers.

## State writes

- current build item;
- build progress;
- `SPLIT` scratch arbitration state;
- placement strategic numbers;
- search state;
- builder/placement context;
- escrow percentages/releases.

## Engine commands

Both high-level and lower-level construction forms occur:

- `build`;
- `up-build`;
- `up-full-reset-search`;
- `up-set-target-point`;
- `up-filter-distance`;
- `up-find-remote`;
- `up-clean-search`;
- `up-remove-objects`;
- `up-set-target-object`;
- `up-get-point`.

Placement modes include `place-normal`, `place-control`, and `place-point`.

## Escrow operations

Construction frequently uses:

- `can-build-with-escrow`;
- `set-escrow-percentage`;
- `release-escrow`;
- `up-build` with an escrow-state argument in applicable paths.

## Completion observations

Completion is established by world-state proxies such as:

- building counts;
- dropsite-distance conditions;
- research/building status around university/ballistics.

The command itself is not completion proof.

## Release behavior

Resource protection is released or rebalanced around the engine-facing build operation. Some rules explicitly release wood immediately before construction. The source does not prove that every escrow mutation is atomic with construction.

## Recovery/re-entry

A major defining feature is rollback:

- if expected construction has not materialized, `gl-build-progress` can be rewound;
- skipped-state correction can restore the expected current item;
- `SPLIT` serializes multi-step construction decisions;
- timer and pending-object guards prevent duplicate/repeated construction.

## Cross-region edges

- Economic resource/escrow state gates construction.
- Housing pressure can preempt ordinary economic construction.
- Construction progression shares `gl-build-progress` and `gl-current-build-item` with research.
- University/ballistics bridge physical construction into technology progression.
- Military/emergency conditions can alter construction priorities.

## Qualification

**DIRECT + COMPOSED / STATIC / CONFIRMED.**

---

# 11. R08 — Placement/search submachine

## Source

Embedded primarily in the construction interval 1794–1896; the strongest recovered instances are GOLDMC1, GOLDMC2, and STONEMC1.

## Entry

Construction objective requires a resource-dependent placement target.

## State reads

- home coordinates;
- target-player context;
- current build item;
- resource object type;
- distance constraints;
- placement strategic numbers.

## State writes

- search result state;
- target object;
- target point;
- placement policy strategic numbers.

## Engine operations

Canonical search pipeline:

```text
up-full-reset-search
 -> up-set-target-point
 -> up-filter-distance
 -> up-find-remote
 -> up-clean-search
 -> up-remove-objects
 -> up-set-target-object
 -> up-get-point
 -> up-set-target-point
```

Exact order varies by family, but the recovered mining-camp paths establish this as a concrete control submachine.

## Escrow

Placement is downstream of `can-build-with-escrow` in applicable construction paths and is coupled to release/build operations.

## Completion

The placement submachine itself does not prove construction completion. It produces a candidate/point consumed by the construction executor; world-state construction rules close the objective.

## Cross-region edges

Placement is owned by construction behavior but depends on engine search semantics and feeds the construction executor. It should not become a separate strategic authority in ShadowByzantine unless the executor contract requires it.

## Qualification

**DIRECT / STATIC / CONFIRMED CORE.**

---

# 12. R09 — Military/scouting/tactical control

## Source

Distributed. Confirmed state vocabulary in the canonical declarations includes:

- `gl-current-group`;
- `gl-attacking`;
- `gl-find-new-target`;
- `gl-target-hp`;
- raid target IDs and coordinates;
- `gl-raid-can-move` / `gl-raid-can-fire`;
- retreat type;
- enemy attack size;
- enemy skirmisher/archer/cavalry state;
- town defense state;
- march type;
- total military in range;
- army damage potential;
- knight/ranged retreat state;
- target type;
- scouting switches and coordinates.

The exact contiguous outer rule range remains **PROVISIONAL** because the donor deliberately interleaves military, scouting, diagnostic, and progression rules.

## Entry

Engine/world observations: enemy units, groups, positions, town safety, enemy attack, technology, and current tactical state.

## State reads

Group state, target state, tactical geometry, enemy composition, defense state, march/raid state, timers, technology-derived range state.

## State writes

- current group;
- target IDs/types;
- march type;
- raid waypoints;
- attack/retreat state;
- firing/movement permissions;
- tactical evaluation values.

## Engine commands

The broader donor contains group/movement/attack/targeting primitives; exact command closure should be extracted in the next military pass rather than inferred from constants alone.

## Escrow

No claim is made here that military execution itself owns escrow. Production/construction/economic regions provide the resource-control substrate used to create military capability.

## Completion

Combat completion is generally state-based rather than a single command acknowledgement: target state, group state, enemy state, damage/position observations, and retreat conditions participate.

## Cross-region edges

Military is a major **requirement generator** for research and production: enemy composition and threat state can cause research interruptions and change desired production. Conversely, completed technologies and produced units alter military capability.

## Qualification

**DIRECT state vocabulary + COMPOSED behavior; outer boundary PROVISIONAL.**

---

# 13. R10 — Defense/emergency interruption

## Source

Distributed across military, economic, construction, and progression neighborhoods. `gl-town-under-attack`, `gl-defend-town`, defensive march states, attack-size variables, and retreat constants are explicit global state.

## Entry

Threat observations such as town attack, enemy attack size, dangerous tactical proximity, or insufficient defensive capability.

## State reads

- town-under-attack;
- enemy attack size;
- military-in-range;
- army damage potential;
- group/target state;
- economic/build progression state.

## State writes

- defensive posture;
- current group/march state;
- attack/retreat permissions;
- potentially shared progression/production state through cross-region policy.

## Engine commands

Exact command closure is not yet certified in this atlas.

## Escrow

The important architectural finding is indirect: emergency state can compete with the economic progression machine, so any transplant must preserve the ability to interrupt lower-priority progression rather than treating escrow as a permanently fixed reserve.

## Completion/release

Threat cessation and restored strategic conditions are the relevant re-entry observations; no single global emergency completion predicate is claimed.

## Cross-region edges

This region crosses military ↔ economy ↔ construction ↔ production. It is therefore a strong candidate for a later explicit ShadowByzantine preemption/recovery mechanism, but that would be a Byzantine generalization rather than a direct claim about Shadow's implementation.

## Qualification

**INFERRED/COMPOSED control region; DIRECT state substrate; PROVISIONAL.**

---

# 14. R11 — Global recovery / re-entry

## Source

Distributed rather than a single contiguous block. The strongest direct evidence is the repeated use of:

- skipped-state correction;
- progression rollback;
- current-item restoration;
- clearing `gl-progression-pause`;
- escrow release/rebalancing;
- `disable-self` latches;
- jump-based bypass/re-entry.

## Entry

Observed state conflicts with the current progression cursor, current objective, or temporary interruption.

## State reads

- progression cursor;
- current item;
- research/building/unit status;
- pause state;
- strategic mode;
- pending objects;
- resource/escrow state.

## State writes

- cursor rollback;
- current-item restoration;
- pause reset;
- escrow release/rebalance;
- one-shot latch state;
- next progression milestone.

## Engine commands

Depends on the owning region. Recovery is not an independent engine executor.

## Completion/release

Recovery closes when the observed state is again consistent with a valid progression/transaction entry condition. A `release-escrow` command is not treated as proof of physical release.

## Cross-region edges

Potentially every major region. This is why a clean global `recovery.per` cannot be declared as Shadow-faithful without first proving the distributed writer/reader topology.

## Qualification

**COMPOSED / INFERRED; PROVISIONAL outer boundary.**

---

# 15. Cross-region edge matrix

| Edge | Source mechanism | Direction | Evidence |
|---|---|---|---|
| Observation → economy | resource/escrow facts | R01 → R04 | DIRECT |
| Observation → military | groups/positions/enemy facts | R01/R02 → R09 | DIRECT/COMPOSED |
| Research → military | `research-completed` modifies tactical ranges/evaluation | R05/R06 → R02/R09 | DIRECT |
| Military → research | enemy strategy/composition triggers research exceptions | R09 → R05 | DIRECT in research triggers; military writer closure partly unresolved |
| Economy → research | resources/escrow/feasibility | R04/R01 → R05 | DIRECT |
| Research → construction | `gl-build-progress`, current item, technology prerequisites | R06 → R07 | DIRECT |
| Construction → progression | building counts/dropsite observations advance or rewind progress | R07 → R06/R04 | DIRECT |
| Economy → construction | resource/escrow and housing pressure | R04/R01 → R07 | DIRECT |
| Construction → economy | farms/dropsites alter economic state | R07 → R04 | COMPOSED |
| Military → production | threat/composition requirement | R09 → production region | COMPOSED; production outer boundary still being segmented |
| Production → military | observed unit populations/capability | production → R09 | COMPOSED |
| Defense → economy | emergency preemption can interrupt economic progression | R10 → R04 | COMPOSED/INFERRED |
| Any region → jump topology | `up-jump-rule` | distributed | DIRECT |
| Any region → re-entry | state cursor/pause/current-item reconciliation | distributed | DIRECT/COMPOSED |

---

# 16. Escrow operation map

Shadow's escrow semantics are distributed across regions.

```text
                 STRATEGIC / PROGRESSION STATE
                    /       |        \
                   /        |         \
          research      construction   production
              |               |             |
              v               v             v
       can-research     can-build      can-train
       -with-escrow     -with-escrow   -with-escrow
              |               |             |
              +-------+-------+-------------+
                      |
                      v
               ESCROW POLICY
       up-modify-escrow / set-escrow-percentage
                      |
                      v
              ENGINE ACCOUNTING MODE
                 gl-escrow-state
                      |
                      v
                  COMMAND
                      |
                      v
             OBSERVED PROGRESSION
                      |
                      v
                 RELEASE / REBALANCE
```

Critical distinctions:

1. `gl-escrow-state` is **not** a logical commitment owner.
2. `can-* -with-escrow` is an execution gate, not completion.
3. `up-research` / `up-train` / `up-build` are commands, not completion facts.
4. `release-escrow` is an operation, not proof of zero escrow.
5. The same physical escrow namespace is shared by multiple strategic regions.
6. Therefore a ShadowByzantine transplant must preserve **writer closure**, not copy isolated escrow rules.

---

# 17. Control-flow edge semantics

The donor's normal successor is source order. Explicit jumps add alternate edges.

The documented jump model is:

```text
jump target = current rule + 1 + Δ
```

Therefore:

- `up-jump-rule 1` skips the next rule;
- `up-jump-rule -1` loops to the current rule;
- large positive jumps bypass entire source regions.

The source-order matrix confirms examples such as:

```text
rule 27 --jump +44--> rule 72
```

and construction/search loops around `gl-lclerp` with `up-jump-rule -1`.

A transplant that retains predicates/actions while deleting these edges is **not behaviorally equivalent**.

---

# 18. Completion / release contract observed in Shadow

The atlas identifies the following recurring sequence:

```text
INTENT
  ↓
PROGRESSION / INTERRUPTION
  ↓
RESOURCE PROTECTION
  ↓
ENGINE FEASIBILITY
  ↓
ENGINE COMMAND
  ↓
WORLD / RESEARCH OBSERVATION
  ↓
PROGRESSION RECONCILIATION
  ↓
RELEASE / REBALANCE
  ↓
RE-ENTRY
```

This is a forensic abstraction, not a claim that Shadow has explicit states with these names.

The source directly supports the separation of:

- intent vs command;
- command vs completion;
- escrow mutation vs logical progression;
- release operation vs observed release;
- progression advancement vs source-order adjacency.

---

# 19. Architecture correction for ShadowByzantine

The atlas invalidates the idea that the finished reconstruction should be centered on:

```text
requirements → capital → escrow → authority → execution → verification → recovery
```

as seven independent donor-faithful modules.

That chain remains a **useful forensic transaction lens**.

The actual reconstruction target is instead:

```text
                    SHADOW MACHINE
                         |
             +-----------+-----------+
             |                       |
      PERSISTENT STATE         CONTROL FLOW
             |                       |
             +-----------+-----------+
                         |
             +-----------+-----------+
             |           |           |
          ECONOMY     RESEARCH   CONSTRUCTION
             |           |           |
             +-----------+-----------+
                         |
                    PRODUCTION
                         |
                    MILITARY
                         |
                  DEFENSE / SCOUT
                         |
                  RE-ENTRY / RECOVERY
```

Cross-cutting mechanisms—escrow, progression, jumps, timers, search, completion observation, and release—should be mapped **onto** these regions rather than replacing them.

---

# 20. Implementation consequence

Do not enlarge `16_pass1_transaction.per` into the center of the finished AI.

Its one-Spearman vertical slice remains useful as an ABI/transaction proof, but it is not the donor architecture.

The next reconstruction units should be **large coherent control regions**, preferably:

1. complete production/composition region;
2. complete research/progression region;
3. complete construction/progression region;
4. complete military/scouting region;
5. cross-region arbitration/preemption only after the donor edges are mapped.

Each transplant should preserve the complete local closure:

```text
trigger writers
→ trigger readers
→ progression cursor / interruption
→ escrow/resource policy
→ feasibility
→ command
→ completion observer
→ progression mutation
→ release/rebalance
→ re-entry
→ competing writers
→ jump/bypass edges
```

This is the smallest defensible transplant unit for Shadow.

---

# 21. Evidence status and remaining gaps

### Confirmed sufficiently for reconstruction planning

- canonical source identity;
- global persistent-state substrate;
- engine-state acquisition window;
- military initialization window;
- research escrow families 1172–1250;
- construction machine 1794–1896;
- construction search/placement pipeline;
- source-order + jump semantics;
- progression/escrow/release coupling;
- command-vs-completion distinction;
- distributed writer/reader nature of escrow.

### Still requiring a dedicated forensic pass before declaring complete

- exact outer boundaries of the full production region;
- exact outer boundaries of the complete scouting region;
- exact outer boundaries of the complete military execution region;
- full jump closure across those regions;
- complete writer/reader matrix for `gl-strategy`, `gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause` across all 1,956 rules;
- complete production completion/release paths;
- runtime qualification of any reconstructed region.

### Non-claims

This atlas does not claim:

- runtime firing frequency;
- competitive causality;
- that every source rule is live;
- that every disabled/experimental block belongs to the active machine;
- that Shadow had a formal transaction object;
- that the analytical region boundaries are source-level module boundaries.

---

# 22. Primary evidence references

1. `ShadowSource.per` — canonical source.
2. `docs/forensics/SHADOW_SOURCE_ORDER_MATRIX_v0.3.md` — generated source-order/control-flow matrix.
3. `docs/forensics/SHADOW_LIVE_CONTROL_FLOW_AND_ESCROW_v0.2.md` — live CFG/escrow trace.
4. `docs/forensics/SHADOW_ESCROW_DEPENDENCY_CLOSURE_v0.1.md` — escrow dependency closure.
5. `docs/forensics/SHADOW_CONSTRUCTION_RULE_EXTRACTION_1794_1896_2026-09-16.md` — exact construction extraction.
6. `docs/forensics/SHADOW_CONSTRUCTION_FORENSIC_PASS2_1801_1896_2026-09-16.md` — construction state-machine synthesis.
7. `docs/forensics/SHADOW_CREATOR_INTENT_AND_LIVE_PATH_v0.2.md` — strategic interpretation of the donor machine.

**Status:** `FORENSIC BASELINE / STATIC / PARTIALLY COMPLETE REGION SEGMENTATION`

**Do not treat provisional region boundaries as implementation boundaries.**
