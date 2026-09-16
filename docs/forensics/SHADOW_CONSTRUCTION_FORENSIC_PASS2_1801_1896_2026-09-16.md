# Shadow Construction Forensic Pass 2 — Rules 1801–1896

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per` on `main`  
**Canonical source blob SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

## Scope

This pass recovered the complete canonical source interval beginning immediately after rule 1800 and continuing through rule 1896. The interval was read through bounded source fetches covering source lines 20920–22200. The canonical source remains the authority for exact rule text; this artifact records the forensic synthesis rather than replacing the source.

## Source windows recovered

- 20920–21180: farm progression, FLUSH/KRUSH farm state, housing preemption/placement, QLC entry.
- 21181–21480: lumber-camp progression LC1–LC4, additional lumber-camp timer path, market/trading, mill progression, first mining-camp entry.
- 21481–21780: continuation through mill and mining-camp state machinery, including the first GOLDMC1 search/build transaction.
- 21781–22000: GOLDMC1 KRUSH/FLUSH transactions, GOLDMC2 transition, disabled GOLDMC2 search/build experiment, STONEMC1 transaction setup.
- 22001–22200: completion of GOLDMC2/STONEMC1, additional mining-camp path, university, ballistics, end-of-script timer marker.

## Core finding: construction is a state machine, not a single build call

The source does not implement construction as simply `build <object>`. It repeatedly decomposes a construction objective into distinct state transitions:

`strategy / progression` → `gl-current-build-item` → search preparation → candidate selection → placement configuration → escrow/resource release → engine-facing build operation → world-state proxy → `gl-build-progress` advancement → next construction item.

The same source also contains rollback/recovery transitions in which observed construction state forces `gl-build-progress` backward when the expected building is absent. This is direct evidence that the progression variable is intended to represent a recoverable construction sequence rather than merely a write-once plan counter.

## Commitment / transaction structure

### 1. Intent state

`gl-current-build-item` is the explicit construction intent register. The source repeatedly assigns named milestones such as `FARMS`, `FARMS2`, `LC1`–`LC4`, `MILL1`, `GOLDMC1`, `GOLDMC2`, and `STONEMC1`.

### 2. Progress state

`gl-build-progress` is the ordered progression register. Completion rules increment it when an observed world-state proxy reaches the expected threshold. Recovery rules reduce it when the expected construction has not materialized.

### 3. Feasibility / escrow state

Construction rules commonly require `can-build-with-escrow`, then explicitly alter escrow policy and/or release wood immediately before the build command. This creates a visible resource-commitment boundary.

### 4. Search state

Mining-camp transactions explicitly reset search state, establish an origin point, constrain distance, search for a resource object, copy the target-player context, order the result set, remove invalid objects, and finally select the first surviving candidate.

### 5. Placement state

Selected objects are converted into a build point through `up-get-point position-object point-x` followed by `up-set-target-point point-x`. Placement behavior is then parameterized with strategic numbers such as placement zone size, failure delta, adjacency policy, and dropsite separation distance.

### 6. Execution state

The source uses both high-level `build` and lower-level `up-build` forms. The lower-level construction transactions demonstrate explicit placement modes (`place-normal`, `place-control`, `place-point`) and explicit escrow-state arguments in some paths.

### 7. Verification state

The source does not use the issued build command itself as completion proof. Completion is subsequently inferred from building counts or resource-dropsite distance, followed by a `gl-build-progress` update. This is materially aligned with the AEGIS requirement not to equate command issuance with completed world state.

## Major construction families recovered

### Farms

The farm subsystem contains strategy-specific construction sequences for KRUSH and FLUSH, with separate milestones for early farm groups and explicit skipped-state recovery. Housing pressure can act as an alternate trigger for farm construction. Later farm rules can also be entered through a `SPLIT` arbitration state, demonstrating that construction priority can be temporarily serialized through a shared scratch state.

### Housing

Housing is not merely a passive prerequisite. Multiple rules directly preempt other economic construction when housing headroom becomes low, while placement policy is changed according to context. Builder assignment is explicit in several housing rules.

### Lumber camps

LC1–LC4 form an ordered construction chain. Each milestone has some combination of: current-build-item selection, resource/escrow policy, construction command, count-based completion, skipped-state rollback, and transition to the next milestone. Additional lumber-camp construction is independently timer-gated and uses dropsite-distance checks.

### Mills

MILL1 has a search/skip decision, timer gating, escrow release, construction, completion advancement, and rollback. A later policy loop can request additional mills when farm counts exceed thresholds and no pending mill placement exists.

### Mining camps

Mining camps provide the clearest complete transaction architecture. GOLDMC1 and STONEMC1 contain explicit search preparation and candidate selection. GOLDMC1 then uses a `SPLIT` state to serialize the final placement transaction. GOLDMC2's canonical rule 1890 is a disabled (`false`) placement rule, not a jump rule; the canonical sequence remains a GOLDMC2 placement transaction followed by STONEMC1.

### University / Ballistics

University and Ballistics show that the same progression machinery extends beyond physical construction into technology milestones. Their completion is tied to building-count or research-status observations, while resource escrow policy is changed around the milestone.

## Priority and preemption findings

1. `gl-current-build-item` functions as a single active construction milestone, creating an implicit serialization mechanism.
2. `gl-build-progress` is not monotonic in all circumstances; recovery rules intentionally rewind it.
3. Housing pressure can bypass normal economic sequencing.
4. `SPLIT` is used as transient arbitration state for multi-step construction decisions.
5. Timer guards are used to prevent repeated or overly rapid construction attempts.
6. Strategy predicates (`FLUSH`, `KRUSH`) select alternate construction policies over the same building type.
7. Pending-object / pending-placement predicates are used as anti-duplication guards.
8. Resource escrow is coupled to the selected construction milestone, but the source does not by itself establish whether every escrow mutation is atomic with engine construction.

## AEGIS transplantation implications

The source supports a clean separation into the following AEGIS control stages:

1. **Construction intent:** choose a named construction transaction.
2. **Authorization:** verify strategy, age, prerequisites, resource feasibility, pending state, and priority.
3. **Commitment:** establish escrow policy and resource reservation/release boundary.
4. **Search:** derive candidate resource/build location.
5. **Placement policy:** configure placement constraints.
6. **Execution:** invoke the existing executor primitive.
7. **Observation:** inspect pending/world-state proxies.
8. **Verification:** advance only after an appropriate observable completion condition.
9. **Recovery:** rewind, retry, re-search, or preempt when the expected state does not materialize.
10. **Reassessment:** allow higher-priority constraints to replace the active construction transaction.

The first implementation should therefore **not** transplant the Shadow rule block wholesale. It should preserve the demonstrated control boundaries while giving AEGIS explicit ownership of cognition/authorization and leaving engine execution with the proven executor until its contract is established.

## Code-readiness gate

**Status: NOT YET READY FOR IMPLEMENTATION.**

The Shadow construction state machine is now sufficiently recovered to specify the AEGIS-side construction contract, but one forensic gate remains before code should be written:

- establish the exact current AiBuilder executor contract for `build`, `up-build`, `up-assign-builders`, placement modes, pending-object/pending-placement state, and builder ownership;
- identify existing AiByz writers for the same construction authority/state variables;
- resolve which Shadow semantics are safe to transplant directly, which require engine-semantic confirmation, and which should be deliberately improved by AEGIS;
- then write the construction module against a declared authority matrix rather than against Shadow syntax alone.

No implementation code is introduced by this pass.
