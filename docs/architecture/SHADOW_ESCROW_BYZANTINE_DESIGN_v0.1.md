# ShadowByzantine — Escrow-First Reconstruction Design v0.1

## Executive position

I have written enough conventional AoE2 `.per` to distrust conventional architecture.

Most bots are built as a pile of intentions: economy rules, build rules, military rules, then increasingly desperate priority exceptions when those independent intentions collide. The result is not arbitration; it is rule-order roulette with resource starvation hiding underneath.

Shadow demonstrates a different possibility. Its escrow usage appears to make resource protection part of the control machine itself. That is worth reconstructing for Byzantines—but only after the mechanism is proved across the corpus.

The design target is therefore:

> **Shadow control machine + Byzantine policy, with escrow treated as a candidate commitment/arbitration primitive rather than as a bookkeeping subsystem.**

This document does not claim that every Shadow decision is escrow-driven. It defines how the hypothesis will be tested and, if confirmed, transplanted.

---

## 1. The machine we actually want

The desired Byzantine bot is not:

```text
Economy -> Production -> Military
```

with an emergency priority flag taped across the top.

It is closer to:

```text
OBSERVE
   |
   v
CLASSIFY OBJECTIVE / PRESSURE
   |
   v
SELECT CURRENT COMMITMENT
   |
   v
PROTECT REQUIRED RESOURCES
   |
   v
CHECK FEASIBILITY
   |
   v
ISSUE ENGINE ACTION
   |
   v
OBSERVE ACTUAL WORLD STATE
   |
   v
ADVANCE / RELEASE / ABORT / RE-ENTER
```

The important word is **commitment**. A bot that repeatedly changes its mind before an action becomes executable is not strategically flexible; it is self-sabotaging.

Escrow may provide the engine-facing resource protection needed to make commitment concrete.

---

## 2. Why Byzantine is a natural target

Byzantine strategy contains many situations where resource protection matters more than a static build-order list:

- early military buildings competing with farms;
- defensive buildings competing with military production;
- counter-unit production competing with technology;
- Castle Age preparation competing with immediate defense;
- expensive late-game technologies competing with army replacement;
- multiple production buildings competing with infrastructure;
- siege and elite upgrades competing with reinforcement cycles.

The civilization-specific layer should therefore specify **what the bot wants**. Shadow-derived control should govern **how the bot commits, protects, executes, observes, and re-enters**.

---

## 3. Separation of contributions

Every reconstructed mechanism carries provenance.

### SHADOW-DERIVED

Control idioms recovered from FireBall37's source:

- source-order sequencing;
- jump topology;
- escrow-aware feasibility;
- resource protection;
- progression registers;
- search/placement idioms;
- release/re-entry patterns;
- temporal gates;
- state reset patterns.

### BYZANTINE POLICY

Civilization-specific facts and preferences:

- available technologies;
- unit/building roster;
- costs and prerequisites;
- civilization bonuses;
- composition policy;
- threat responses;
- economic priorities.

### ENGINEERING EXTENSION

Our changes are explicitly tagged and tested. No improvement gets smuggled into the reconstruction merely because it looks cleaner.

---

## 4. Escrow as a candidate commitment primitive

The conventional interpretation is:

```text
escrow = resource accounting
```

The reconstruction hypothesis is stronger:

```text
escrow
   |
   +--> protects resource availability
   |
   +--> stabilizes a selected objective
   |
   +--> constrains competing actions
   |
   +--> permits a protected command path
   |
   +--> remains coupled to progression/release
```

That hypothesis is accepted only when repeated source evidence supports the entire relationship.

A single `set-escrow-percentage` call proves only that the command exists.

A recurring chain such as:

```text
select objective
 -> configure escrow
 -> can-build-with-escrow
 -> issue action
 -> observe progression
 -> release/reallocate
```

is much stronger evidence of a control idiom.

---

## 5. The Byzantine commitment record

When we eventually implement the reconstruction, a commitment should be represented by existing `.per` primitives and source-derived state, not by an invented software object unless the engine permits it.

Conceptually the commitment contains:

```text
objective
resource(s) protected
required capability
feasibility state
command state
world-state evidence
progression evidence
release condition
expiry/failure condition
re-entry target
```

This is a conceptual forensic model, not a proposed set of arbitrary new goals.

The exact goal/SN encoding must be selected only after the Shadow data-flow atlas identifies safe, semantically appropriate state slots.

---

## 6. Priority arbitration

A conventional bot often computes:

```text
if attack then military
else if build then construction
else economy
```

That is inadequate for the reconstruction.

The Shadow-inspired model asks which objective currently owns the scarce resource and what evidence is required to release that ownership.

Example:

```text
Threat detected
    |
    v
Need counter-unit
    |
    v
Can afford counter-unit while preserving infrastructure?
    |
   no ----> protect infrastructure / defer counter
    |
   yes
    v
reserve/protect resources
    |
    v
issue production
    |
    v
verify production/progression
    |
    v
release reservation
```

The actual precedence must come from the reconstructed Shadow machine plus Byzantine policy. It must not be hard-coded from this diagram.

---

## 7. Anti-patterns explicitly forbidden

### 7.1 The priority integer

Do not solve arbitration with a single `priority = 100` variable and pretend the problem is finished.

### 7.2 The giant emergency block

Do not append 400 emergency rules to the bottom of the file because the first architecture could not arbitrate.

### 7.3 Permanent escrow

Do not reserve resources indefinitely. Every reservation requires a release, transition, timeout, or verified failure path.

### 7.4 Command-as-completion

`build`, `up-build`, `train`, or `research` means an engine action was requested. It does not mean the world reached the desired state.

### 7.5 Pending-as-completion

Pending objects and pending placement are useful evidence, but they are not interchangeable with completed world state.

### 7.6 Architecture by noun

Do not create `economy.per`, `escrow.per`, `military.per`, and `verification.per` merely because those nouns sound organized. If Shadow's control topology crosses those boundaries, the reconstruction must cross them too.

---

## 8. Byzantine adaptation points

The adaptation layer should eventually answer:

### Capability

What can Byzantines produce/research/build now?

### Need

What capability is required by the current threat/objective?

### Commitment

Which objective should receive protected resources?

### Execution

Which native Shadow-derived command path performs it?

### Verification

What observable world state proves meaningful progress?

### Release

When can the protected resources be made available to the next objective?

These are questions for the reconstructed machine, not independent modules by default.

---

## 9. Engineering improvements we should actually pursue

Once the baseline works, improvements should target known failure modes rather than architectural fashion.

### Improvement A — stale commitment detection

If a protected objective remains infeasible or unprogressed beyond a demonstrated temporal bound, force reassessment rather than starving the entire economy forever.

### Improvement B — resource starvation detection

Detect when protection for one objective prevents essential replacement, worker production, or survival requirements.

### Improvement C — explicit evidence separation

Maintain separate states for:

```text
requested
pending
observed
completed
failed
```

only where the engine/source supports the distinction.

### Improvement D — Byzantine capability substitution

If a required capability is unavailable, select a documented alternative rather than allowing a dead commitment to persist.

### Improvement E — regression preservation

Every improvement must be compared against the Shadow-derived baseline so we know whether we improved behavior or merely changed behavior.

---

## 10. Implementation gate

Do not begin serious ShadowByzantine `.per` reconstruction until these are available:

1. complete rule atlas;
2. source identity reconciliation;
3. jump/control graph;
4. goal/SN/timer data-flow;
5. escrow graph;
6. progression traces;
7. representative end-to-end Shadow traces;
8. documented safe adaptation points.

If one of these is missing, the correct response is more forensics—not another pile of `.per`.

---

## 11. Definition of success

The reconstruction succeeds when we can explain a Byzantine decision in the following form:

```text
Observed condition
 -> Shadow-derived classification/control path
 -> Byzantine policy selection
 -> resource commitment/protection
 -> feasibility
 -> engine action
 -> world-state evidence
 -> progression/release
 -> reassessment
```

And, critically, we can point to the exact evidence showing which portions came from Shadow and which portions are ours.

That is how you build a serious bot instead of a large `.per` file.
