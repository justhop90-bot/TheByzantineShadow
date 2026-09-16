# Shadow → ShadowByzantine Donor-to-Implementation Topology Diff v0.1

**Status:** STATIC FORENSIC DIFF / DESIGN-GATING / NOT RUNTIME QUALIFICATION

**Repository:** `justhop90-bot/TheByzantineShadow`

**Audit basis:** current `main` after machine-index reconciliation

**Canonical donor:** `ShadowSource.per`

**Canonical donor SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

**Donor machine:** 1,956 ordered `defrule` blocks

**Current runtime root:** `ShadowByzantine.per`

---

## 1. Purpose

This document is the first explicit donor-to-implementation topology comparison. It answers a narrower question than the blueprint:

> For each recovered Shadow machine model, where does the corresponding mechanism currently exist in ShadowByzantine, is it actually loaded, and what topology has changed?

It is **not** a quality score. It does not rank mechanisms. It identifies preservation, adaptation, absence, and architectural divergence.

The donor remains the authority. A ShadowByzantine mechanism is not considered donor-faithful merely because it implements a similar concept.

---

## 2. Current runtime topology

The current root entrypoint is:

```text
ShadowByzantine.per
    |
    v
ShadowByzantine/ShadowByzantine.per
    |
    +--> 01_constants.per
    +--> 01b_byz_constants.per
    +--> 02_state.per
    +--> 03_economy.per
    +--> 04_construction.per
    +--> 16_pass1_transaction.per
```

The inner file explicitly describes itself as a Pass-1 runtime module orchestrator and deliberately does not load the older `05`–`15` module family. Consequently, repository presence and runtime presence must be treated as different states.

The current runtime is therefore a **small executable vertical slice**, not a reconstructed equivalent of Shadow's ordered 1,956-rule machine.

---

## 3. Topology classification vocabulary

| Classification | Meaning |
|---|---|
| PRESERVED | Donor mechanism exists in the current design/implementation with its essential topology intact. |
| PARTIAL | A donor mechanism exists, but important donor state, ordering, lifecycle, or dependency closure is absent. |
| ADAPTED | Donor mechanism is retained while civilization-specific policy changes its inputs or objective selection. |
| MOVED | Donor mechanism is represented elsewhere; topology must be checked before accepting the move as equivalent. |
| CHANGED | Current implementation deliberately changes donor topology or semantics. |
| ADDED | No direct donor analogue; engineering/Byzantine extension. |
| LOST | Donor mechanism is not currently represented in the implementation. |
| DOCUMENTED-ONLY | Repository artifacts describe the mechanism, but the current runtime does not load it. |
| UNKNOWN | Evidence is insufficient to classify fidelity. |

---

## 4. Model-by-model donor diff

| Model | Shadow donor mechanism | Current ShadowByzantine location | Runtime status | Topology classification | Principal delta |
|---|---|---|---|---|---|
| M00 Source identity / ordered program | `ShadowSource.per`, 1,956 ordered rules | Root repository/source chain | N/A | PRESERVED | Canonical source is preserved; current runtime is not one-file ordered Shadow. |
| M01 Initialization / register bootstrap | QID/QGENERAL/QPOSITION initialization and early state writes | `01_constants`, `02_state`, `03_economy`, Pass-1 initialization | LOADED | PARTIAL / MOVED | Donor initialization is split across files; exact donor writer precedence is not preserved. |
| M02 Sequential control / jump machine | Source-order fall-through, `up-jump-rule`, negative loops, self-disabling rules | No equivalent complete control stream | NOT LOADED | LOST / DOCUMENTED-ONLY | Modular file loading replaces the donor's single ordered program topology. |
| M03 Persistent state / register machine | Shared goals, strategic numbers, timers and distributed state | `01_constants`, `02_state`, Pass-1 AEGIS state | LOADED | CHANGED / PARTIAL | New AEGIS state namespace is introduced; donor shared state has not been fully reconstructed. |
| M04 Temporal control | Donor timer-driven cadence and re-entry | No complete equivalent in Pass 1 | NOT LOADED | LOST | Pass-1 does not reproduce the donor temporal machine. |
| M05 Escrow / reservation | `gl-escrow-state`, escrow mutation, `can-*-with-escrow`, release/re-entry | `16_pass1_transaction`; `10_escrow` exists but is not loaded | LOADED, narrow | PARTIAL / ADDED STRUCTURE | Pass 1 demonstrates a transaction-shaped escrow lifecycle, but it is not yet the donor-wide distributed escrow topology. |
| M06 Progression cursor | `gl-current-build-item`, `gl-progression-pause`, build/progression state | `04_construction`, Pass 1 transaction state | LOADED, narrow | PARTIAL / CHANGED | Explicit AEGIS transaction state replaces rather than reproduces donor cursor topology. |
| M07 Resource arbitration | QECONOMY plus local escrow/resource gates | `03_economy`, AEGIS capital state in Pass 1 | LOADED | PARTIAL / ADDED | Deterministic 60/40 gatherer baseline and transaction feasibility are extensions, not donor-wide arbitration. |
| M08 Search machine | reset → filter → find → inspect → cleanup/remove → target → point | No complete loaded search module | NOT LOADED | LOST / DOCUMENTED-ONLY | Placement/search artifacts exist, but current runtime does not load the donor search machine. |
| M09 Placement machine | `place-normal`, `place-point`, `place-control`, search state and retry/re-entry | `07_placement.per`, ABI docs | NOT LOADED | DOCUMENTED-ONLY | Placement is researched but absent from current Pass-1 runtime. |
| M10 Construction machine | QBUILDINGS, QMARKET, QSTABLE, QMONASTERY and farm/camp/mill progression | `04_construction` | LOADED | PARTIAL | Basic house/barracks/farm behavior exists; donor construction cursor/escrow/search/placement topology is not transplanted. |
| M11 Research machine | Research escrow, feasibility, command, completion and progression | `06_research.per` | NOT LOADED | DOCUMENTED-ONLY | Repository design exists, runtime path absent. |
| M12 Production machine | QUNITS production families, escrow-aware training, completion/re-entry | `05_production.per`, Pass 1 Spearman kernel | Narrow Pass 1 only | PARTIAL | One Byzantine Spearman transaction is executable; full QUNITS topology is not. |
| M13 Production preemption / priority | QSKIRMS/QSPEARS/QARCHERS/QMANGOS positional bypasses | No complete loaded analogue | NOT LOADED | LOST / DOCUMENTED-ONLY | Known donor jump topology has not entered the runtime. |
| M14 Military group initialization | Ranged/Raid group state, ranges, tactical registers | `06_military.per` | NOT LOADED | DOCUMENTED-ONLY | Donor military initialization remains research, not runtime. |
| M15 Military evaluation / advantage | QADVANTAGE, ranged evaluation, superiority/distance state | `06_military.per` | NOT LOADED | DOCUMENTED-ONLY | No loaded equivalent. |
| M16 Target acquisition / search | Military target acquisition and target-state persistence | `06_military.per` / forensic docs | NOT LOADED | DOCUMENTED-ONLY | Search and target state not active in Pass 1. |
| M17 March / attack / defense | March states, attack/retreat/defense transitions | `06_military.per` | NOT LOADED | DOCUMENTED-ONLY | No runtime military control path. |
| M18 Civilian protection / local defense | Town-under-attack, attack centroid, garrison/retreat | `06_military.per` / docs | NOT LOADED | DOCUMENTED-ONLY | Not in current runtime. |
| M19 Raid machine | Economic target acquisition, waypoints, retreat/reset | Forensic docs / no loaded dedicated module | NOT LOADED | DOCUMENTED-ONLY | Donor raid topology absent from runtime. |
| M20 Siege response | QRAMS/QMANGOS production and tactical response | `05_production` / `06_military` | NOT LOADED | DOCUMENTED-ONLY | Donor siege machinery not executable in current graph. |
| M21 Scouting / intelligence | QSCOUT, exploration, stuck recovery, information state | No loaded dedicated module | NOT LOADED | DOCUMENTED-ONLY | Scouting topology remains forensic/design work. |
| M22 Agriculture / food transition | Farm arbitration, hunting/farm transitions, farm progression | `04_construction` basic farm rule | LOADED, narrow | PARTIAL / ADAPTED | Basic farm construction is present, but donor farm arbitration is not. |
| M23 Recovery / failsafe | Distributed timers, negative loops, rollback/re-entry, failsafe state | `14_recovery.per` | NOT LOADED | DOCUMENTED-ONLY | Current runtime does not contain donor recovery topology. |
| M24 Reassessment / re-entry | Distributed repeated evaluation and local re-entry | Pass-1 terminal idle/reassess state | LOADED, narrow | CHANGED / PARTIAL | Pass-1 has a transaction lifecycle; donor's distributed source-order re-entry has not been reconstructed. |
| M25 Shared strategic state | Donor shared goals linking economy/military/build/progression | AEGIS state namespace | LOADED, narrow | CHANGED | AEGIS introduces centralized-looking state carriers; donor ownership topology remains incomplete. |
| M26 Byzantine policy | No direct donor equivalent | `01b_byz_constants`, composition policy and AEGIS objective state | PARTIAL | ADDED | Civilization-specific layer is legitimate extension, but it must remain upstream of donor-derived execution. |
| M27 Verification / qualification | Donor world-state observers and completion predicates | Pass-1 verification state; `13_verification.per` not loaded | LOADED, narrow | PARTIAL / ADDED | Pass 1 proves one transaction's world-state closure; donor-wide observer topology remains incomplete. |

---

## 5. Most important topology deltas

### 5.1 Shadow's single ordered program became a module graph

This is the largest architectural delta.

Shadow's donor identity is one ordered `.per` program whose source order, fall-through, positional jumps, self-disabling rules, and local state create executable control topology.

ShadowByzantine currently presents:

```text
root entrypoint
    -> nested loader
        -> numbered modules
            -> Pass-1 transaction kernel
```

That is not a cosmetic refactor. It changes the control surface. A donor jump such as `up-jump-rule 44` cannot be preserved merely by putting the destination logic in another module; its positional meaning is part of the machine.

**Architecture verdict:** the nested orchestrator remains ARCHITECTURE-REVIEW-REQUIRED. It has not passed the repository's direct-donor analogue and topology gates.

---

### 5.2 Shadow's distributed escrow became an explicit transaction namespace

Pass 1 intentionally introduces:

```text
AEGIS-TRANSACTION
AEGIS-ESCROW-STATUS
AEGIS-AUTHORITY
AEGIS-EXECUTION-STATE
AEGIS-VERIFICATION
AEGIS-RECOVERY-STATE
```

This is useful as an experimental vertical slice, but these state carriers are not themselves evidence that Shadow contained a transaction coordinator with equivalent semantics.

The correct classification is therefore:

```text
Shadow escrow mechanism
        ↓
reconstructed Pass-1 transaction experiment
        ↓
engineering extension / partial donor mapping
```

not:

```text
Shadow contained the AEGIS transaction architecture.
```

---

### 5.3 Construction is only the beginning of donor transplantation

`04_construction.per` explicitly acknowledges that the complete donor construction state machine is not transplanted. In particular, `gl-current-build-item`, `gl-progression-pause`, `up-assign-builders`, and `place-control` remain outside the current implementation boundary.

Therefore the presence of house/barracks/farm rules must not be counted as equivalent to QBUILDINGS/QSTABLE/QMONASTERY donor coverage.

---

### 5.4 Production is a vertical slice, not QUNITS reconstruction

Pass 1 demonstrates:

```text
objective
 → progression request
 → capital feasibility
 → escrow mutation
 → escrow observation
 → authority
 → baseline
 → escrow-aware training
 → world-state verification
 → release request
 → release observation
 → idle/reassess
```

That is valuable executable evidence, but it does not reconstruct the donor's QUNITS machine, production preemption, positional bypasses, unit-family loops, or military-production boundary.

---

## 6. Donor topology currently absent from runtime

The following donor mechanisms are presently documented or represented in repository modules but are **not in the Pass-1 load graph**:

```text
sequential jump machine
complete timer machine
complete search machine
placement machine
research machine
full production machine
production preemption
military group machine
military evaluation
military target acquisition
march/attack/defense
civilian protection
raid machine
siege response
scouting machine
recovery/failsafe machine
complete reassessment/re-entry topology
```

This is the principal reason the current runtime should be treated as a controlled reconstruction kernel rather than as a complete ShadowByzantine implementation.

---

## 7. Donor mechanisms currently preserved most clearly

The strongest current evidence is concentrated in:

1. canonical donor source identity and ordered source index;
2. pending-vs-world-state distinction in construction;
3. resource feasibility preceding escrow mutation in Pass 1;
4. escrow observation before logical commitment in Pass 1;
5. command-vs-completion distinction;
6. world-state closure of the Spearman transaction;
7. explicit release request followed by release observation;
8. basic construction state observation;
9. a deterministic baseline economic allocation.

These should be treated as the current executable reconstruction nucleus, not as proof of complete donor coverage.

---

## 8. Donor mechanisms currently changed or added

The most consequential additions are:

```text
AEGIS objective/requirement/transaction namespace
AEGIS authority state
AEGIS verification state
AEGIS execution baseline
AEGIS recovery state
Byzantine-specific constants and policy
numbered module decomposition
nested runtime loader
Pass-1 transaction kernel
```

These are engineering artifacts. They require donor-topology justification before they can become permanent architecture.

---

## 9. Required next topology gate

The next implementation gate should not be "load all numbered modules."

Instead:

```text
1. Take each donor machine region from the 1,956-rule matrix.
2. Recover its state writers/readers and jump edges.
3. Locate its current ShadowByzantine representation, if any.
4. Compare source order and control dependencies.
5. Determine whether the representation is PRESERVED, MOVED, CHANGED, ADDED, LOST, or UNKNOWN.
6. Reconstruct the donor mechanism before loading more modules.
7. Only then qualify the resulting topology at runtime.
```

The architectural objective is **donor topology closure**, not module-count growth.

---

## 10. Definition of topology closure

ShadowByzantine should not be considered donor-reconstructed until every material donor control region has a traceable disposition:

```text
DONOR RULE INTERVAL
    ↓
DONOR STATE / JUMP / ESCROW / SEARCH SIGNATURE
    ↓
CURRENT IMPLEMENTATION LOCATION
    ↓
LOAD-PATH STATUS
    ↓
TOPOLOGY DIFFERENCE
    ↓
EVIDENCE CLASS
    ↓
RUNTIME QUALIFICATION STATUS
```

The 1,956-rule source-order matrix supplies the first column. This diff supplies the first model-level comparison. The remaining work is to close the rule-level semantic and topology mapping without inventing unsupported abstractions.
