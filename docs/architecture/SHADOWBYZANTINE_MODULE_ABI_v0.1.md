# ShadowByzantine Module ABI v0.1

## Status

**Purpose:** freeze the source-level module boundaries, state ownership, mutation authority, command authority, progression authority, escrow authority, and inter-module interfaces required to implement the reconstructed Shadow control machine for Byzantines.

**Authority order:**

1. canonical `ShadowSource.per` and authenticated forensic derivatives;
2. exact donor control-flow, state, escrow, progression, search/placement, command, and completion evidence;
3. this ABI as the implementation contract derived from that evidence;
4. Byzantine policy and capability facts;
5. explicitly identified engineering extensions.

This document is an **implementation ABI**, not a claim that the current repository already implements every listed module. Current repository presence and current runtime loading are tracked separately.

**Canonical donor:** `ShadowSource.per`.

**Current implementation basis:** the live repository contains a modular `ShadowByzantine` tree. The current Pass-1 runtime graph loads `01_constants`, `01b_byz_constants`, `02_state`, `03_economy`, `04_construction`, and `16_pass1_transaction`. Other numbered modules may exist as research/reconstruction artifacts without being live runtime modules. Their presence must not be counted as runtime coverage.

---

## 1. Architectural thesis

The unit of architecture is the **control mechanism**, not the conceptual noun.

A module is therefore an implementation boundary around a set of rules that share a demonstrable control/data-flow responsibility. A module is **not** an autonomous software object and must not be interpreted as an independent scheduler.

The Shadow machine remains an ordered `.per` control stream whose semantics may depend on:

- source order;
- normal fall-through;
- `up-jump-rule` topology;
- persistent goals and strategic numbers;
- timers and temporal guards;
- search and placement state;
- escrow configuration and resource protection;
- progression cursors;
- engine commands;
- world-state observations;
- re-entry and recovery paths.

Splitting the source into files must not silently change those semantics.

### 1.1 Non-negotiable invariants

1. **Source order is semantic.** Moving a rule across a control boundary can change behavior even when the rule body is unchanged.
2. **Jump targets are positional.** Any source transformation that changes rule ordinals must re-resolve all affected `up-jump-rule` edges.
3. **State ownership is exclusive for mutation.** A persistent state carrier has one authoritative writer domain unless a donor-derived multi-writer pattern is explicitly documented.
4. **Reads do not imply authority.** A module may observe state without owning it.
5. **Command issuance is not completion.** `build`, `up-build`, `train`, `research`, and related engine actions establish requests, not completed world state.
6. **Pending state is not completion.** Pending objects and pending placement are intermediate observations.
7. **World-state observers establish completion evidence.** Progression must consume observable evidence appropriate to the objective.
8. **Escrow configuration is not ownership.** `gl-escrow-state` is an engine accounting-mode selector; physical resource protection and release remain distributed through donor-derived mechanisms.
9. **Progression authority is not generic scheduling authority.** The progression layer may advance a demonstrated control path but must not become an invented global scheduler.
10. **Byzantine policy chooses what is wanted; Shadow-derived control governs how the selected objective is protected, executed, observed, and released.**
11. **Engineering extensions must remain identifiable.** They cannot silently become part of the reconstructed Shadow baseline.

---

## 2. ABI vocabulary

### 2.1 Authority classes

| Authority | Meaning |
|---|---|
| `READ` | May inspect a state/world fact without mutating it. |
| `WRITE` | May establish or modify persistent state owned by the module. |
| `CONTROL` | May select or alter a control/progression mode within the module's demonstrated domain. |
| `COMMAND` | May issue an engine action for which the module is the demonstrated command authority. |
| `ESCROW` | May configure, reserve, release, or otherwise mutate escrow for an objective-local lifecycle. |
| `VERIFY` | May consume world-state evidence and establish completion/failure evidence. |
| `POLICY` | May select a Byzantine-specific desired capability/objective but may not directly bypass the execution ABI. |

### 2.2 Evidence classes

Every ABI statement is classified as one of:

- `DIRECT` — directly represented in donor/current source;
- `COMPOSED` — assembled from multiple direct facts without adding a new behavioral premise;
- `INFERRED` — interpretation of recurring source behavior;
- `ENGINEERING_EXTENSION` — new behavior introduced by this project;
- `UNRESOLVED` — insufficient evidence to authorize the behavior.

The ABI never upgrades an inferred mechanism into a direct donor fact.

---

## 3. Module inventory and authority matrix

The following is the **target implementation ABI**. `Runtime status` describes the live repository at the time this ABI was drafted; it is not an implementation score.

| Module | Primary responsibility | State authority | Command authority | Progression authority | Escrow authority | Runtime status |
|---|---|---|---|---|---|---|
| `01_constants.per` | immutable engine/Shadow constants | immutable definitions only | none | none | constant inputs only | LIVE |
| `01b_byz_constants.per` | immutable Byzantine capability/cost facts | immutable definitions only | none | none | constant inputs only | LIVE |
| `02_state.per` | persistent shared state declarations/initial state mechanisms | foundational state initialization; no arbitrary subsystem arbitration | none | state initialization only | none | LIVE |
| `03_economy.per` | resource observation and economy-side arbitration | economy-local state only | economy-authorized economic commands where donor evidence permits | none beyond economy-local gates | may request/use objective protection; no global escrow ownership | LIVE |
| `04_construction.per` | construction/progression control | construction/progression state within its donor-derived region | construction/placement commands | construction progression | objective-local construction escrow lifecycle | LIVE |
| `05_production.per` | unit production control | production-local state | training commands | production progression | production objective-local protection | RECONSTRUCTION ARTIFACT / NOT PASS-1 LOADED |
| `06_military.per` | military control and tactical re-entry | military-local state | military movement/attack commands where donor-derived | tactical progression/re-entry | only where donor path demonstrates it | RECONSTRUCTION ARTIFACT / NOT PASS-1 LOADED |
| `07_placement.per` | placement/search interface | placement-local scratch/search state | placement commands | placement completion handoff only | consumes construction-owned escrow state; no independent escrow policy | RECONSTRUCTION ARTIFACT / NOT PASS-1 LOADED |
| `08_requirements.per` | feasibility/capability predicates and Byzantine demand | no ownership of persistent execution state | none | none | read-only feasibility view of protected resources | RECONSTRUCTION ARTIFACT / NOT PASS-1 LOADED |
| `09_capital.per` | infrastructure/capital policy | capital-policy state only | none directly unless donor path proves it | none | may request protection through owning executor | RECONSTRUCTION ARTIFACT / NOT PASS-1 LOADED |
| `10_escrow.per` | escrow forensic/reconstruction boundary | **not a global state owner**; only objective-local escrow mechanisms assigned by ABI | escrow engine primitives only where authorized by objective owner | none | escrow operations under objective owner; no universal transaction manager | RECONSTRUCTION ARTIFACT / NOT PASS-1 LOADED |
| `11_authority.per` | execution-boundary research/extension | no independent global authority state unless explicitly justified | no commands by default | no global scheduling | no escrow ownership | ENGINEERING EXTENSION / NOT PASS-1 LOADED |
| `12_execution.per` | execution-boundary research/extension | no universal command queue | only commands explicitly assigned by ABI | no global scheduling | none by default | ENGINEERING EXTENSION / NOT PASS-1 LOADED |
| `13_verification.per` | world-state evidence and completion observation | verification evidence only | none | may publish completion/failure evidence; may not advance arbitrary objectives | none | ENGINEERING EXTENSION / NOT PASS-1 LOADED |
| `14_recovery.per` | failure/timeout/re-entry mechanisms | recovery-local state | only recovery commands demonstrated by donor path | may reset/re-enter an owning control region; no generic scheduler | may release/reset escrow only through authorized owner/path | ENGINEERING EXTENSION / NOT PASS-1 LOADED |
| `15_reassessment.per` | objective re-evaluation and re-entry | reassessment-local state | none | may request re-entry; does not own execution progression | none | ENGINEERING EXTENSION / NOT PASS-1 LOADED |
| `16_pass1_transaction.per` | current narrow vertical integration slice | slice-local state only | commands inside its explicitly bounded path | slice-local progression | narrow lifecycle only; not corpus-wide Shadow escrow | LIVE PASS-1 SLICE |

**Important:** the inventory does not require all rows to become separate runtime files. If forensic reconstruction demonstrates that two responsibilities share a control region whose separation would alter source semantics, they may remain physically colocated. The ABI governs authority, not file count.

---

## 4. State ownership ABI

### 4.1 Ownership rule

For every persistent goal, strategic number, timer, coordinate, cursor, or mode selector:

```text
AUTHORITATIVE WRITER
        |
        +----> readers
        |
        +----> derived actions
        |
        +----> completion/recovery paths
```

The authoritative writer owns mutation semantics. Readers must not independently normalize, reset, or reinterpret the value unless that behavior is itself a documented writer operation.

### 4.2 Core state ownership

| State carrier | Owner | Allowed readers | Allowed writers | Notes |
|---|---|---|---|---|
| `gl-current-build-item` | progression/construction control | construction, economy, production/research adapters as donor topology permits | progression owner only | Objective/progression cursor; not merely last completed building. `DIRECT/COMPOSED`. |
| `gl-build-progress` | progression owner | construction and dependent progression regions | progression owner; explicit donor reconciliation paths | Recoverable progression cursor; may reconcile backward when observed world state is below expectation. `DIRECT`. |
| `gl-progression-pause` | progression owner | construction/production/research/recovery paths where donor reads it | progression/recovery paths demonstrated by donor | Interruption/hold state, not generic scheduler state. `DIRECT/COMPOSED`. |
| `gl-escrow-state` | escrow/progression control boundary | objective execution regions | only authenticated donor-derived escrow-mode writers | Engine accounting-mode selector, not physical ownership. `DIRECT`. |
| `SPLIT` | local control arbitration region | only regions demonstrated to read it | local arbitration rules | Scratch/control state; not a strategic global priority. `DIRECT`. |
| placement search scratch | placement/search owner | placement/construction path | placement/search path | Must not become persistent strategic policy. `COMPOSED`. |
| pending-object observations | engine/world-state observer | owning objective and recovery | engine/world state; AI should not fabricate completion | Observation only. `DIRECT`. |
| completion evidence | verification/objective owner | progression/reassessment | owning observer path | Must identify actual world-state predicate. `COMPOSED`. |
| Byzantine demand/policy state | Byzantine policy layer | requirements/execution arbitration | Byzantine policy rules | Must not directly issue engine commands. `ENGINEERING/COMPOSED`. |

### 4.3 State mutation restrictions

A module **must not**:

- reset another module's persistent state because its own objective changed;
- write `gl-current-build-item` merely because it wants an objective executed;
- write `gl-build-progress` merely because a command was issued;
- set completion state merely because an object became pending;
- alter `gl-escrow-state` as a generic “transaction begin/end” signal;
- treat `SPLIT` as a universal priority variable;
- create duplicate writers for an existing authoritative state carrier without a topology-diff record.

---

## 5. Command authority ABI

### 5.1 Command lifecycle

Every engine action follows the conceptual contract:

```text
OBJECTIVE
   ↓
STATE / COMMITMENT
   ↓
ESCROW / RESOURCE PROTECTION, IF REQUIRED
   ↓
FEASIBILITY
   ↓
TARGET / PLACEMENT RESOLUTION
   ↓
COMMAND ISSUANCE
   ↓
PENDING / INTERMEDIATE OBSERVATION
   ↓
WORLD-STATE COMPLETION OBSERVATION
   ↓
PROGRESSION / RELEASE / RE-ENTRY
```

A command-authorized module owns **issuance**, not proof of completion.

### 5.2 Command ownership

| Command family | Primary authority | Preconditions | Completion authority |
|---|---|---|---|
| `build` | construction/progression path | capability + resource feasibility + donor guards | world-state observer |
| `up-build place-normal` | construction/placement path | objective selected + escrow/feasibility + target class | world-state observer |
| `up-build place-point` | construction/placement path | point resolved + feasibility | world-state observer |
| `up-build place-control` | construction/placement path | placement configuration + objective state | world-state observer |
| `train` / production commands | production path | unit feasibility + resource protection | trained-unit/world observer |
| `research` | research path | technology feasibility + resource protection | `research-completed` or equivalent world observer |
| military movement/attack | military path | tactical state + target resolution | battlefield/world observer, not command issuance |
| search commands | owning search/placement/military path | search state initialized | target/object/point observation |

No module may claim completion solely from command issuance.

---

## 6. Progression authority ABI

### 6.1 Progression ownership

Progression authority is assigned to the control region that demonstrably owns the corresponding progression cursor.

For construction, the minimum reconstructed sequence is:

```text
current objective
 → feasibility
 → resource protection
 → target/placement resolution
 → engine command
 → pending/intermediate observation
 → world-state milestone
 → progress update/reconciliation
 → release/restoration
 → re-entry
```

R07 construction rules 1794–1896 provide the first authenticated implementation-level example of this contract.

### 6.2 Progression mutations

A progression owner may:

- advance a progression cursor after its required world-state milestone;
- reconcile a cursor against actual observed world state where donor rules explicitly do so;
- pause/resume progression through donor-derived interruption state;
- reset/re-enter a demonstrated progression region through its documented control edges.

It may not:

- infer completion from command issuance;
- advance progress solely because escrow was configured;
- advance progress solely because a pending object exists;
- globally reorder unrelated objectives without a donor-derived control edge;
- introduce a generic scheduler under the name of progression.

---

## 7. Escrow authority ABI

### 7.1 Escrow is an actuator, not a universal owner

Escrow operations remain coupled to the objective/progression path that requires resource protection.

The ABI distinguishes:

```text
ESCROW MODE
    = engine accounting-mode state

RESOURCE PROTECTION
    = actual objective-local reservation/configuration

RELEASE
    = explicit restoration/reallocation path
```

These concepts must not be collapsed into one “transaction” abstraction without donor evidence.

### 7.2 Authorized escrow operations

An objective owner may, where donor evidence authorizes the path:

1. configure escrow percentages;
2. enter the appropriate escrow accounting mode;
3. use escrow-aware feasibility predicates;
4. issue the protected engine command;
5. release objective-local escrow when the demonstrated release condition occurs;
6. restore accounting mode through the demonstrated control path;
7. re-enter/reallocate after failure or completion.

### 7.3 Forbidden escrow behavior

No module may:

- reserve resources permanently;
- use escrow as a generic lock unrelated to an objective;
- interpret `gl-escrow-state = 205` as proof that resources are physically owned by a transaction;
- release another objective's reservation without an authorized cross-boundary path;
- create a second independent escrow manager;
- equate configured escrow with completed action;
- use a priority integer as a substitute for the demonstrated escrow/arbitration mechanism.

### 7.4 Objective-local escrow interface

The conceptual interface is:

```text
REQUEST_PROTECTION(objective, resource-set, required-capability)
        ↓
CONFIGURE / RESERVE
        ↓
CAN_EXECUTE_WITH_PROTECTION?
        ↓
ISSUE COMMAND
        ↓
OBSERVE PROGRESS
        ↓
RELEASE / RESTORE / ABORT
```

This is a composed ABI description. Exact goal/SN encoding must be taken from the relevant donor region rather than invented globally.

---

## 8. Inter-module interfaces

### 8.1 Policy → Requirements

```text
INPUT:
    desired capability/objective
    Byzantine context

OUTPUT:
    required building/unit/technology capability
    resource requirements
    acceptable alternatives, if explicitly supported

AUTHORITY:
    policy selects intent;
    requirements evaluates feasibility.

FORBIDDEN:
    direct engine command issuance.
```

### 8.2 Requirements → Execution owner

```text
INPUT:
    capability requirements
    current world state
    available/protected resources

OUTPUT:
    feasibility result / required resources / unmet prerequisite

AUTHORITY:
    read-only feasibility unless a donor-derived state write is explicitly part of the path.
```

### 8.3 Construction → Placement

```text
CONSTRUCTION OWNS:
    objective
    progression
    construction-local escrow lifecycle

PLACEMENT OWNS:
    search
    target object/point resolution
    placement configuration
    placement command interface

RETURN:
    resolved target / point
    command-issued evidence
    placement failure/intermediate evidence
```

Placement must not silently acquire construction progression ownership.

### 8.4 Placement → World observation

```text
PLACEMENT COMMAND
       ↓
PENDING / TARGET OBSERVATION
       ↓
WORLD-STATE COMPLETION PREDICATE
```

The placement interface terminates at evidence production; completion is consumed by the owning progression path.

### 8.5 Production → Progression

Production reports:

```text
command issued
pending/training evidence
completed unit/world-state evidence
failure/stall evidence
```

Progression may advance only when the production path's required milestone is satisfied.

### 8.6 Research → Progression

Research reports:

```text
research command
research pending/intermediate state
research-completed evidence
```

The research path must not mutate unrelated construction or military progression cursors.

### 8.7 Escrow → Objective owner

Escrow exposes engine-facing resource protection operations, but objective selection remains outside escrow.

```text
OBJECTIVE OWNER
     │
     ├── required resources
     ├── feasibility
     └── release condition
          │
          ▼
     ESCROW PRIMITIVES
          │
          ▼
     ENGINE ACCOUNTING / RESOURCE PROTECTION
```

Escrow cannot independently decide which objective deserves protection.

### 8.8 Verification → Progression

Verification publishes evidence:

```text
OBSERVED / NOT OBSERVED
COMPLETED / NOT COMPLETED
FAILED / STALLED, where demonstrable
```

It must not directly manufacture progression state. The owning progression path consumes the evidence and performs the appropriate donor-derived transition.

### 8.9 Recovery → Owning control region

Recovery may:

- clear/reset explicitly owned recovery state;
- release escrow through an authorized release path;
- redirect execution to a documented re-entry point;
- trigger reassessment where the donor/control topology supports it.

Recovery may not become a global exception scheduler.

### 8.10 Reassessment → Policy/execution

Reassessment may request that the objective be reconsidered.

It may not:

- directly issue arbitrary engine commands;
- rewrite another module's authoritative state;
- bypass required feasibility;
- silently invalidate escrow without its release path.

---

## 9. Source-order and jump ABI

### 9.1 Physical file boundaries are not control-flow boundaries

A module split is valid only if the resulting loaded source stream preserves the required control topology or deliberately replaces it with an explicitly qualified equivalent.

For every transplanted jump:

```text
origin rule
jump delta
resolved destination
skipped rules
source-order position
new implementation position
```

must be recorded.

### 9.2 Cross-module jump prohibition

Cross-module `up-jump-rule` edges are prohibited by default because module loading can alter positional semantics.

If a donor behavior requires a cross-file control transfer, the implementation must either:

1. preserve the relevant rules in one ordered control region; or
2. replace the edge with a proven equivalent mechanism and record it as an engineering extension.

No silent translation is permitted.

### 9.3 Fall-through preservation

A normal fall-through edge is part of the donor machine even though it is not written as a jump command. When rules are split across files, the implementation must preserve the intended successor relationship or explicitly account for the changed topology.

---

## 10. Current Pass-1 boundary

The current live runtime slice is intentionally treated as a bounded integration target rather than as proof that the complete architecture is implemented.

Current live load boundary:

```text
root entry
   ↓
ShadowByzantine runtime entry
   ↓
01_constants
01b_byz_constants
02_state
03_economy
04_construction
16_pass1_transaction
```

This ABI therefore treats `16_pass1_transaction` as a **vertical integration slice**, not as a universal transaction architecture.

The following remain outside the Pass-1 runtime until separately qualified:

- full production reconstruction;
- full military reconstruction;
- dedicated placement runtime;
- full requirements/demand runtime;
- corpus-wide escrow transplant;
- authority/execution extensions;
- verification extension;
- recovery extension;
- reassessment extension;
- scouting/intelligence;
- endgame.

---

## 11. Implementation order

The implementation sequence is:

### Stage 1 — ABI foundation

1. `01_constants.per`
2. `01b_byz_constants.per`
3. `02_state.per`

Freeze symbols and ownership before adding behavior.

### Stage 2 — first closed control slice

4. `03_economy.per`
5. `04_construction.per`
6. placement interface required by construction
7. objective-local escrow path
8. world-state completion observers

Use R07 as the first exact control-region qualification target.

### Stage 3 — production/research

9. production control
10. requirements/capability predicates
11. research progression

### Stage 4 — military/information

12. military control
13. scouting/information acquisition
14. threat/intelligence adaptation

### Stage 5 — recovery and reassessment

15. donor-derived recovery
16. re-entry/reassessment
17. only then consider engineering extensions.

This order is deliberately not the same thing as module numbering.

---

## 12. Module acceptance criteria

A module is not accepted merely because its `.per` parses.

### Static acceptance

- symbols are defined before use under the actual load order;
- no unauthorized state writers exist;
- no duplicate authoritative writers exist;
- commands are issued only by authorized paths;
- escrow mutations have objective-local provenance;
- progression writes have world-state or donor-derived transition evidence;
- jump topology is preserved or explicitly dispositioned;
- no accidental cross-module control-flow dependency exists;
- comments do not conceal executable semantics;
- the module is actually loaded if it is being claimed as runtime implementation.

### Runtime acceptance

Where applicable:

- module loads in AoE2DE;
- command issuance is observed;
- pending/intermediate state is distinguished from completion;
- world-state completion is observed;
- progression changes only at the required milestone;
- escrow is released/restored through the intended path;
- failure/stall behavior reaches a documented recovery/re-entry path.

### Replay acceptance

Representative replays must demonstrate the relevant lifecycle and regression behavior. A static rule path is not replay evidence.

---

## 13. ABI violation classes

| Violation | Severity | Required response |
|---|---|---|
| Unauthorized persistent-state writer | CRITICAL | Remove or explicitly reassign ownership before runtime qualification |
| Command issued outside command authority | CRITICAL | Re-route through owning control path |
| Progress advanced without required world evidence | CRITICAL | Correct completion/progression boundary |
| Escrow released without authorized lifecycle | CRITICAL | Restore objective-local release path |
| Donor jump target changed without disposition | CRITICAL | Reconstruct topology or document qualified replacement |
| Module reads state it is supposed to own | HIGH | Review ownership/interface boundary |
| Module file exists but is not loaded while claimed as runtime | HIGH | Correct status claim/load graph |
| Pending state treated as completion | HIGH | Introduce actual observer/evidence boundary |
| Byzantine policy directly issues engine command | HIGH | Return command authority to execution owner |
| Engineering extension silently presented as Shadow-derived | HIGH | Add provenance and extension record |
| Additional abstraction with no donor evidence | MEDIUM/HIGH | Forensic review before adoption |

---

## 14. Provenance and extension protocol

Every non-donor mechanism introduced into a module must be tagged in its design record as:

```text
ENGINEERING_EXTENSION
```

and carry:

```text
baseline mechanism
observed limitation
modified mechanism
expected effect
static verification
runtime verification
replay evidence
regression result
```

A cleaner abstraction is not sufficient justification for changing the machine.

---

## 15. Open ABI closures before full-machine implementation

The ABI is sufficiently defined to begin implementation, but the following evidence must still be closed before claiming full-machine reconstruction:

1. corpus-wide Shadow state writer/reader closure;
2. complete donor jump topology mapped to the physical implementation;
3. full escrow objective lifecycle corpus;
4. production/research end-to-end traces;
5. military/scouting control-region reconstruction;
6. recovery/re-entry topology;
7. endgame control region;
8. final root/load topology qualification;
9. runtime qualification of each loaded vertical slice.

These are **implementation-qualification gaps**, not reasons to postpone all coding.

---

## 16. Definition of ABI compliance

ShadowByzantine is ABI-compliant when:

```text
Every persistent state carrier has a known owner
        AND
Every mutation has an authorized path
        AND
Every engine command has a command owner
        AND
Every progression mutation has a valid evidence path
        AND
Every escrow mutation belongs to an objective-local lifecycle
        AND
Every inter-module boundary preserves required donor control semantics
        AND
Every changed jump/control edge is explicitly dispositioned
        AND
Every Byzantine policy decision is separated from execution authority
        AND
Every engineering extension is provenance-tagged
```

Only then is the modular source tree a faithful implementation boundary around the reconstructed Shadow machine rather than a conventional RTS architecture imposed on it.

---

## 17. Immediate implementation gate

**Approved to begin implementation:** yes, for bounded, evidence-closed control regions.

**First implementation target:** construction/progression using the authenticated R07 control region and its 107-edge state-transition matrix.

**Not yet authorized:** inventing generic `authority`, `transaction`, `verification`, `recovery`, or `reassessment` managers merely because corresponding filenames exist.

The first implementation cycle should therefore be:

```text
R07 donor evidence
    ↓
module ABI mapping
    ↓
04_construction / placement boundary
    ↓
state-owner audit
    ↓
escrow-owner audit
    ↓
command-owner audit
    ↓
completion-observer audit
    ↓
static qualification
    ↓
runtime qualification
    ↓
replay regression
```

That produces the first genuinely closed ShadowByzantine implementation slice and establishes the pattern for the remaining machine.
