# Shadow Machine Reconstruction — Architecture v0.1

## Status

**Purpose:** establish the reconstruction architecture for ShadowByzantine before further implementation.

**Authority:** `ShadowSource.per` is the current canonical source candidate. `Shadow DC7.zip` remains historical source material until the archive/member reconciliation procedure establishes its exact relationship to `ShadowSource.per`.

**Design rule:** architecture is derived from Shadow's observed mechanisms. No abstract subsystem boundary is authoritative merely because it is conceptually convenient.

---

## 1. Project Objective

ShadowByzantine is a reconstruction of FireBall37's Shadow control machine adapted to Byzantines, with deliberate engineering improvements added only after the reconstructed Shadow behavior is understood.

The project has three distinguishable contributions:

1. **FireBall37 / Shadow** — original control idioms and mechanisms recovered from the source corpus.
2. **ShadowByzantine reconstruction** — faithful reproduction/adaptation of those mechanisms for Byzantines.
3. **Engineering extensions** — explicitly identified changes introduced by this project and evaluated against the reconstructed baseline.

The project must never silently merge these categories.

---

## 2. Architectural Principle

The unit of architecture is the **control mechanism**, not the conceptual noun.

Do not begin by creating independent modules named `economy`, `escrow`, `authority`, `verification`, `recovery`, etc. Those concepts may exist inside Shadow, but their actual boundaries must be derived from rule topology, shared state, ordering, jumps, and engine interactions.

In particular:

- source order may be computationally significant;
- `up-jump-rule` edges are part of control flow;
- goals and strategic numbers can cross conceptual subsystems;
- module boundaries do not imply state boundaries;
- engine commands do not prove world-state completion;
- escrow state is not automatically an ownership/authority abstraction;
- pending objects/placement are observations, not completion proofs;
- a parser-valid rule is not necessarily runtime-valid behavior.

---

## 3. Reconstruction Stack

```text
                         ShadowSource.per
                               |
                               v
                    +-----------------------+
                    | FORENSIC CORPUS       |
                    | rules / constants /   |
                    | goals / SNs / timers  |
                    | commands / jumps      |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | SHADOW MACHINE MODEL  |
                    |                       |
                    | sequential control    |
                    | jump topology         |
                    | state/register use    |
                    | escrow behavior       |
                    | progression           |
                    | search/placement      |
                    | command/re-entry      |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | SHADOWBYZANTINE       |
                    |                       |
                    | reconstructed machine|
                    | + Byzantine facts     |
                    | + Byzantine policy    |
                    +-----------+-----------+
                                |
                                v
                    +-----------------------+
                    | CONTROLLED EXTENSIONS |
                    |                       |
                    | tested improvements   |
                    +-----------------------+
```

---

## 4. Shadow Machine Components To Recover

These are **forensic domains**, not predetermined source-code modules.

### 4.1 Initialization and heartbeat

Recover:

- initialization rules;
- first-pass state writes;
- timers;
- recurring heartbeat behavior;
- startup ordering;
- initialization assumptions imported from the engine/AI environment.

Question: what state does Shadow establish before its main reactive machine becomes active?

### 4.2 Sequential control and jump topology

Recover:

- source-order dependencies;
- fall-through regions;
- `up-jump-rule` edges;
- jump guards;
- re-entry points;
- loops and bounded loops;
- disabled/self-disabling rule regions.

Question: how does Shadow use the rule stream as a control-flow machine?

### 4.3 State/register architecture

Recover every important goal, strategic number, timer, and constant as a data-flow object:

```text
writer -> stored value -> reader -> resulting action
```

Identify:

- state variables;
- state enumerations;
- counters;
- coordinates;
- mode selectors;
- temporary/scratch registers;
- cross-domain registers.

### 4.4 Escrow machine

Recover the exact semantics of:

- escrow percentage changes;
- escrow release;
- escrow-aware feasibility predicates;
- escrow state selectors;
- resource-specific reservation behavior;
- interaction with progression;
- interaction with construction/research/training;
- resource release paths;
- failure/re-entry behavior.

The question is not merely "where is escrow used?" The question is:

> What role does escrow play in Shadow's arbitration and commitment behavior?

### 4.5 Progression machine

Recover construction/progression as a control mechanism:

```text
current objective
    -> feasibility
    -> resource protection
    -> target resolution
    -> engine command
    -> pending/world observation
    -> progression update
    -> next objective / re-entry
```

Identify the exact role of state such as `gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause` rather than assuming they constitute a generic state machine.

### 4.6 Resource arbitration

Recover how Shadow resolves competing resource demands.

Inventory:

- thresholds;
- escrow percentages;
- feasibility predicates;
- release conditions;
- priority selectors;
- fallback rules;
- technology/building/unit conflicts.

The desired output is an arbitration graph, not simply a list of economic rules.

### 4.7 Search and placement

Recover the complete target-resolution pipelines:

```text
reset search
 -> establish origin/target
 -> filter
 -> find
 -> modify/order
 -> clean
 -> select object/point
 -> issue placement command
```

Preserve distinctions among:

- `build` vs `up-build`;
- `place-normal` vs `place-point`;
- object targeting vs point targeting;
- pending objects vs pending placement;
- target resolution vs command issuance.

### 4.8 Production and research

Recover the actual arbitration mechanisms that decide:

- whether production/research is feasible;
- what resource protection applies;
- what takes precedence;
- how commands are issued;
- how progression is recognized;
- how competing objectives re-enter control.

Do not impose a generic production manager unless the corpus demonstrates one.

### 4.9 Military control

Recover:

- group states;
- target selection;
- threat observations;
- attack/retreat transitions;
- march/raid states;
- target switching;
- positional state;
- combat timers;
- re-entry after tactical events.

### 4.10 Scouting and information acquisition

Recover:

- scout state;
- search geometry;
- exploration modes;
- target acquisition;
- enemy-state observations;
- information decay/reset;
- interactions with military/economic decisions.

### 4.11 Recovery and failsafes

Recover actual Shadow mechanisms for:

- failed placement;
- unavailable resources;
- stale target state;
- stalled progression;
- timeout;
- state reset;
- objective substitution;
- re-entry.

Recovery must be derived from observed rules rather than invented as a generic subsystem.

---

## 5. Escrow-Unique Shadow Style

The central research target is Shadow's use of escrow as a behavioral control primitive.

For every escrow operation record:

```text
rule id
source offset
resource
operation
precondition
associated goal/state
associated command
preceding progression state
following progression state
release path
re-entry path
```

Then derive recurring patterns.

Candidate patterns must be treated as hypotheses until supported across the corpus, for example:

```text
resource reservation
        |
        v
objective protection
        |
        v
feasibility gate
        |
        v
command
        |
        v
observation / progression
        |
        v
release or reallocation
```

No claim that this is Shadow's universal architecture is permitted until the forensic corpus demonstrates it.

---

## 6. Byzantine Reconstruction

After the Shadow machine is sufficiently recovered, Byzantine adaptation enters at the points where civilization-specific facts actually enter the machine.

These include:

- technology availability;
- unit availability;
- building availability;
- costs;
- technology prerequisites;
- civilization bonuses;
- strategic priorities;
- composition choices;
- Byzantine-specific military/economic responses.

The underlying control idioms should remain Shadow-derived unless a documented extension deliberately changes them.

---

## 7. Improvement Protocol

Every proposed improvement receives an independent record:

```text
ID
Shadow baseline mechanism
Observed limitation
Hypothesis
Modified mechanism
Expected effect
Static verification
Runtime verification
Replay evidence
Regression result
Disposition
```

Allowed dispositions:

- `ADOPTED`
- `REJECTED`
- `DEFERRED`
- `UNRESOLVED`

An improvement is not considered successful because it is cleaner, more modular, or theoretically superior. It must demonstrate a relevant behavioral benefit without violating the reconstructed machine's required invariants.

---

## 8. Source/Architecture Evidence Rules

Evidence hierarchy:

```text
DIRECT
COMPOSED
INFERRED
UNCERTAIN
```

Static evidence must not be promoted to runtime fact without runtime evidence.

In particular:

```text
command issued != command completed
pending object != completed construction
building-type-count-total > 0 != necessarily fully operational
escrow configured != escrow exhausted/released
parser-valid != runtime-correct
reachable in CFG != observed firing in replay
```

---

## 9. Development Sequence

### Phase 0 — Source identity

Complete `ShadowSource.per` versus `Shadow DC7.zip` reconciliation.

### Phase 1 — Rule atlas

Index every rule and its reads/writes/actions/jumps/commands.

### Phase 2 — Control topology

Construct rule-order, jump, state, progression, and command graphs.

### Phase 3 — Escrow reconstruction

Build the escrow corpus and derive recurring escrow idioms.

### Phase 4 — Shadow machine specification

Describe the machine without Byzantine assumptions.

### Phase 5 — Minimal reconstruction

Reconstruct the Shadow control mechanisms before adding Byzantine strategy.

### Phase 6 — Byzantine adaptation

Introduce civilization-specific facts and policy.

### Phase 7 — Controlled improvements

Add and test improvements one mechanism at a time.

### Phase 8 — Runtime/replay validation

Validate actual behavior and regressions against the reconstructed baseline.

---

## 10. Immediate Engineering Task

The next implementation artifact is **not** another Byzantine `.per` module.

It is the forensic reconstruction layer needed to answer:

1. Which rules constitute Shadow's actual control regions?
2. Which goals/SNs/timers form its persistent state?
3. Where does escrow enter and leave those control regions?
4. Which commands are protected by escrow?
5. How does Shadow recognize progression?
6. Where does control re-enter after an action?
7. Which patterns recur across economy, construction, production, research, and military behavior?

Only after those questions have machine-generated answers should source-code boundaries be selected.

---

## 11. Non-Goals

This architecture does **not** authorize:

- copying a generic RTS architecture onto Shadow;
- creating an abstract transaction/ABI layer without corpus evidence;
- treating escrow as a universal ownership abstraction;
- separating every conceptual concern into a module;
- replacing source-order control with a new scheduler merely for cleanliness;
- adding Byzantine behavior before the corresponding Shadow mechanism is understood;
- treating theoretical improvements as proven improvements.

---

## 12. Definition of Done for v0.1 Reconstruction

The architecture is considered sufficiently reconstructed when we can trace representative Shadow behaviors end-to-end from observation through state change, resource protection, command issuance, progression evidence, and re-entry, and can distinguish the original mechanism from later engineering modifications.

At that point ShadowByzantine can be built from the recovered machine rather than from an imposed architecture.
