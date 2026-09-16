# Shadow → ShadowByzantine Coverage Ledger v0.1

## Status

**Purpose:** provide a measurable cross-reference between the canonical Shadow control machine, the forensic reconstruction work, and the current ShadowByzantine implementation.

**Repository basis:** `main`, inspected immediately before creation of this ledger. The repository's current state is authoritative for implementation/file presence; prior conversation state is not treated as current implementation evidence.

**Canonical donor:** `ShadowSource.per`.

**Classification vocabulary:**

- `DIRECTLY TRANSPLANTED` — current implementation demonstrably reproduces a donor mechanism/control region, with source anchors and implementation evidence.
- `PARTIALLY TRANSPLANTED` — a meaningful donor mechanism exists in the implementation, but donor topology, dependency closure, or lifecycle is incomplete.
- `BYZANTINE EXTENSION` — civilization-specific behavior added on top of, or adjacent to, a Shadow-derived mechanism.
- `DOCUMENTED ONLY` — the mechanism is researched/specified in repository artifacts but is not yet demonstrated as implemented in the current ShadowByzantine runtime.
- `UNRECOVERED` — the required donor mechanism has not yet been sufficiently reconstructed to support implementation claims.
- `UNKNOWN` — repository evidence is insufficient to classify the item.

This ledger is a coverage instrument, not a quality score. It does not rank subsystems or imply that one category is more valuable than another.

---

## 1. Control-machine coverage matrix

| Shadow control domain | Canonical donor evidence to anchor | Current ShadowByzantine implementation / artifact | Status | Required completion evidence |
|---|---|---|---|---|
| Initialization / heartbeat | Shadow initialization and recurring control rules | `ShadowByzantine.per`, `01_constants.per`, `02_state.per`; reconstruction docs | PARTIALLY TRANSPLANTED | Exact donor startup order, timers, first-pass writes, and re-entry reproduced and statically traced |
| Rule order / sequential machine | Full `ShadowSource.per` rule stream; `up-jump-rule` topology | `SHADOW_MACHINE_RECONSTRUCTION_v0.1.md`; current modular `.per` tree | DOCUMENTED ONLY | Rule-by-rule donor CFG mapped to reconstructed source order and cross-file execution order |
| Jump topology | All positive jumps, negative loops, bypasses, fall-through edges | Forensic research and architecture doctrine | DOCUMENTED ONLY | Complete donor jump graph mapped to current implementation with unexplained-edge count = 0 |
| Persistent state / registers | Goals, strategic numbers, timers, coordinates, mode selectors | `02_state.per`, `01_constants.per`, supporting docs | PARTIALLY TRANSPLANTED | Complete writer/reader/mutation/lifetime graph and no unexplained competing writers |
| Escrow control | `gl-escrow-state`, escrow mutations, `can-*-with-escrow`, releases, objective-local paths | `10_escrow.per`; escrow forensic/architecture docs | PARTIALLY TRANSPLANTED | Corpus-wide objective trace from trigger through reservation, feasibility, command, completion, release/re-entry |
| Progression control | `gl-current-build-item`, `gl-build-progress`, `gl-progression-pause` and donor progression regions | `04_construction.per`, related architecture docs | PARTIALLY TRANSPLANTED | Representative construction/research/production progressions traced end-to-end, including interruption and re-entry |
| Resource arbitration | Donor thresholds, escrow percentages, priority/fallback behavior | `03_economy.per`, `07_strategic reserve.per`, `08_requirements.per` | PARTIALLY TRANSPLANTED / BYZANTINE EXTENSION | Donor arbitration graph plus explicit Byzantine deviations and competing-writer analysis |
| Search state machine | Search reset/filter/find/inspect/cleanup/remove/select/point extraction pipelines | Search forensic research; placement/construction implementation | DOCUMENTED ONLY | Dedicated donor search topology mapped and each implementation use traced to engine command |
| Placement | `place-normal`, `place-point`, `place-control`, placement search and completion | `05_placement.per`, `CONSTRUCTION_PLACEMENT_ABI_v0.1.md`, interface matrix | PARTIALLY TRANSPLANTED | Every placement path has target resolution, command, completion observer, failure/re-entry path |
| Construction | Donor construction/progression regions including farm/camp/mill/market/monastery/stable patterns | `04_construction.per` | PARTIALLY TRANSPLANTED / BYZANTINE EXTENSION | Exact donor region mapping for each transplanted objective; no command/completion conflation |
| Research | Donor research progression, escrow, feasibility, completion observers | `06_research.per`; research forensic docs | PARTIALLY TRANSPLANTED | Representative technologies trace objective → escrow → research → `research-completed` → progress/release/re-entry |
| Production arbitration | QUNITS donor regions; unit feasibility, escrow, training, completion, bypass | `05_production.per`, `08_requirements.per` | PARTIALLY TRANSPLANTED / BYZANTINE EXTENSION | Donor production topology mapped for monks/mangos/rams/archers/skirms/spears/etc.; completion observers verified |
| Requirements / demand | Donor feasibility/resource requirements plus Byzantine desired-composition demand | `08_requirements.per`, `PRODUCTION_DEMAND_INTERFACE_v0.1.md` | BYZANTINE EXTENSION | Show exact donor baseline where applicable and isolate added composition-demand behavior |
| Capital / infrastructure priority | Donor building progression and capital constraints | `09_capital.per` | BYZANTINE EXTENSION / PARTIALLY TRANSPLANTED | Donor infrastructure arbitration identified; Byzantine capital policy explicitly separated |
| Strategic reserve | Donor resource protection / fallback mechanisms | `07_strategic reserve.per` and reserve docs | BYZANTINE EXTENSION | Donor analogue identified for every reservation rule; no invented universal transaction semantics |
| Authority / execution boundary | Donor distributed authority through ordered rules, state, escrow, and commands | `11_authority.per`, `12_execution.per` | DOCUMENTED ONLY / ENGINEERING EXTENSION | Direct donor analogue for every abstraction; architecture veto passed; no unsupported central authority |
| Verification | Donor world-state observers and progression evidence | `13_verification.per` | DOCUMENTED ONLY / ENGINEERING EXTENSION | Each observer tied to an exact donor completion mechanism and engine semantics |
| Recovery / failsafe | Distributed donor interruption, timeout, rollback, re-entry, and bypass rules | `14_recovery.per`; forensic docs | DOCUMENTED ONLY / ENGINEERING EXTENSION | Donor recovery topology reconstructed before centralization or abstraction |
| Reassessment | Donor re-entry and repeated objective evaluation | `15_reassessment.per`; forensic docs | DOCUMENTED ONLY / ENGINEERING EXTENSION | Exact donor re-entry edges and triggers mapped; no generic scheduler introduced |
| Military control | Shadow military initialization, target acquisition, march/attack/defense, group state, tactical re-entry | `06_military.per`, military forensic docs | PARTIALLY TRANSPLANTED | Donor M01–M08 regions mapped to implementation and battlefield observers verified |
| Scouting / information acquisition | Shadow scouting control, geometry, exploration, enemy-state observation | Forensic research; no dedicated current module established by this ledger inspection | DOCUMENTED ONLY | Dedicated donor scouting topology and current implementation path identified |
| Intelligence / threat classification | Donor observations/searches feeding strategic/tactical state | Forensic research; current threat/requirements work | DOCUMENTED ONLY / BYZANTINE EXTENSION | Donor observation-to-state paths mapped and current Byzantine threat policy separated |
| Endgame | Donor late-game objective/re-entry behavior | No complete dedicated reconstruction established | UNRECOVERED | Recover donor endgame control region and prove implementation coverage |
| Root entrypoint / load topology | Shadow direct entry behavior and source order | root/subdirectory `ShadowByzantine.per` artifacts | PARTIALLY TRANSPLANTED | Verify exact AoE2DE load path, loaded files, order, and absence of unsupported loader-of-loaders behavior |

---

## 2. Cross-cutting control mechanisms

### 2.1 Objective lifecycle

The target lifecycle is not an invented API. It is a forensic trace assembled from demonstrated Shadow mechanisms:

```text
OBSERVATION / DEMAND
    ↓
OBJECTIVE SELECTION
    ↓
PROGRESSION CURSOR / STATE
    ↓
RESOURCE PROTECTION / ESCROW
    ↓
FEASIBILITY
    ↓
TARGET / SEARCH RESOLUTION
    ↓
ENGINE COMMAND
    ↓
WORLD-STATE OBSERVATION
    ↓
PROGRESSION RECONCILIATION
    ↓
RELEASE / RESTORATION
    ↓
REASSESSMENT / RE-ENTRY
```

Coverage requirement: every claimed reconstructed objective must identify the exact donor rules for the relevant stages. A generic implementation diagram is not evidence of a donor lifecycle.

### 2.2 Escrow coverage

For each donor escrow objective, the ledger must eventually contain:

```text
DONOR RULE ID / SOURCE OFFSET
OBJECTIVE
RESOURCE(S)
ESCROW MUTATION
ESCROW MODE
FEASIBILITY GATE
ENGINE COMMAND
COMPLETION OBSERVER
RELEASE / RESTORATION
FAILURE / TIMEOUT PATH
RE-ENTRY PATH
COMPETING WRITERS / JUMPS
CURRENT SHADOWBYZANTINE LOCATION
STATUS
```

No escrow mechanism is `DIRECTLY TRANSPLANTED` until the complete local lifecycle is accounted for.

### 2.3 State coverage

Every important goal, strategic number, and timer entering the reconstructed machine must eventually have:

```text
SYMBOL
DONOR WRITERS
DONOR READERS
DONOR MUTATIONS / CLEAR PATHS
LIFETIME
JUMP DEPENDENCIES
ENGINE OWNERSHIP, IF ANY
CURRENT IMPLEMENTATION WRITERS
CURRENT IMPLEMENTATION READERS
CONFLICT STATUS
```

A symbol existing in a constants file does not establish behavioral coverage.

### 2.4 Jump coverage

For every transplanted jump:

```text
ORIGIN RULE
DELTA
DESTINATION RULE
SKIPPED RULES
DESTINATION PREDICATES
LOOP / BYPASS ROLE
CURRENT IMPLEMENTATION EDGE
TOPOLOGY DIFF
```

Unexplained changed jump destinations are reconstruction defects until proven otherwise.

### 2.5 Search coverage

For every transplanted search mechanism:

```text
RESET
ORIGIN / TARGET POINT
FILTERS
REMOTE / LOCAL SEARCH
INSPECTION
CLEANUP
REMOVAL
TARGET SELECTION
POINT / OBJECT EXTRACTION
ENGINE ACTION
RE-ENTRY
```

`search-remote` or `up-find-*` appearing in a file is not sufficient evidence that the donor search state machine has been reconstructed.

---

## 3. Evidence ledger for implementation status

| Claim type | Minimum evidence before marking implemented |
|---|---|
| File/module exists | Current repository inspection |
| Rule mechanism exists | Exact current rule body + donor anchor |
| Symbol is authoritative | Complete current writer/reader analysis |
| Jump behavior preserved | Origin/destination/skipped-region comparison |
| Escrow behavior preserved | Full objective-local escrow lifecycle |
| Command works | Runtime command observation |
| Action completed | World-state observer |
| Recovery works | Runtime/replay evidence of failed/stalled path |
| End-to-end subsystem works | Representative runtime/replay trace |

This table deliberately prevents a file-count or line-count metric from being used as implementation coverage.

---

## 4. Current gap statement

The repository currently contains substantial Shadow forensic research, architecture doctrine, escrow analysis, construction/placement work, production/requirements work, military research, and Byzantine-specific extensions. That does **not** establish a complete Shadow-machine transplant.

The principal remaining reconstruction gap is the **machine-level closure**:

```text
canonical donor
    ↓
rule atlas
    ↓
jump graph
    ↓
state writer/reader graph
    ↓
escrow objective graph
    ↓
progression graph
    ↓
search/placement graph
    ↓
production/research/military control graphs
    ↓
current ShadowByzantine implementation
    ↓
topology diff
    ↓
runtime qualification
```

Until this closure exists, implementation percentages should be treated as engineering estimates rather than measured coverage.

---

## 5. Required next forensic artifact set

This ledger is the coverage shell. It becomes quantitatively useful when populated with machine-generated anchors.

### Priority A — Rule atlas

For every Shadow rule:

```text
rule ordinal
source offset
rule identity
reads
writes
commands
jumps
escrow operations
search operations
completion observers
control region
current reconstruction location
status
```

### Priority B — State writer/reader graph

Enumerate every goal/SN/timer/coordinate that crosses a control-region boundary.

### Priority C — Jump graph

Enumerate every `up-jump-rule`, including positive skips and negative loops, then compare the donor graph to the reconstructed graph.

### Priority D — Escrow corpus

Enumerate every escrow mutation/feasibility/release sequence and associate it with its objective/progression region.

### Priority E — End-to-end representative traces

Select representative donor behaviors from economy, construction, research, production, military, scouting, and recovery. For each, prove the complete lifecycle rather than only static existence.

---

## 6. Ledger maintenance rule

This ledger must be updated **in place** as reconstruction coverage changes. Do not create a new coverage document for every phase or version.

Before updating it:

1. re-read `docs/AI_SCRIPTER_OPERATING_DOCTRINE.md`;
2. inspect the current repository state;
3. inspect the canonical donor and relevant implementation files;
4. cross-reference existing forensic artifacts;
5. update the affected rows and evidence anchors;
6. state uncertainty rather than filling gaps with inference.

The ledger is subordinate to the canonical donor and does not become evidence merely because a row exists.

---

## 7. Definition of done

The ledger reaches reconstruction-grade completeness when:

- every material Shadow control region has an exact donor anchor;
- every claimed implementation maps to one or more donor mechanisms;
- every important state carrier has writer/reader closure;
- every transplanted jump has origin/destination closure;
- every escrow objective has local lifecycle closure;
- every search path has state-machine closure;
- every completion claim has a world-state observer;
- every recovery claim has a demonstrated recovery path;
- every Byzantine extension is explicitly separated from Shadow-derived behavior;
- every project improvement has a baseline and qualification record;
- unexplained topology differences are zero or explicitly dispositioned;
- runtime/replay qualification distinguishes static reconstruction from observed behavior.

Until then, the ledger is a gap map, not a completion certificate.
