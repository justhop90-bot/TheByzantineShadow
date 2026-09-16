# The Byzantine Shadow

**A forensic reconstruction and Byzantine adaptation of the FireBall/Shadow Age of Empires II AI machine.**

The Byzantine Shadow is not a generic AI framework and it is not merely an escrow library. The project exists to **deconstruct the original Shadow control machine, preserve the mechanisms that made it unusually effective, reconstruct those mechanisms faithfully in `.per`, and then adapt the resulting machine to the Byzantine civilization without replacing Shadow's underlying control style with a modern abstraction invented from scratch.**

> **Source of truth:** this repository. Claims about Shadow behavior should be traceable to `ShadowSource.per`, preserved donor material, forensic documents, or qualified runtime evidence.

---

## 1. Project Objective

The project has four linked objectives:

1. **Recover Shadow.** Determine how the original FireBall37 Shadow AI actually worked: its state carriers, rule ordering, positional jumps, timers, goals, search loops, escrow mechanisms, production sequencing, construction progression, research progression, military control, interruption, and recovery paths.
2. **Reconstruct the machine.** Rebuild the important control regions in clean Byzantine code while preserving the original `.per` execution model rather than hiding it behind a new transaction framework.
3. **Adapt the machine to Byzantines.** Replace civilization-specific assumptions with Byzantine production, composition, economy, infrastructure, technology, and military requirements while retaining Shadow's control discipline.
4. **Improve only where the evidence supports it.** New behavior is an explicit adaptation or improvement, not retroactively attributed to Shadow. Static inference, runtime qualification, and speculation remain separate.

The end product is intended to be a **Shadow-style Byzantine AI**, not an AI that happens to contain an escrow subsystem.

---

## 2. Why Shadow?

The donor is historical FireBall37 Shadow. Its source explicitly identifies Shadow as an Age of Empires II AI by FireBall37 and documents the original author's use of the AI scripting community and other AIs as learning sources.

The important discovery is that Shadow is not best understood as a pile of independent rules. Its behavior emerges from a **large sequential control machine** encoded directly in the `.per` rule stream.

Several properties make the machine distinctive:

### Escrow is part of control flow

Shadow does not treat resource reservation as a detached accounting service. Escrow policy, progression state, affordability, transaction mode, command issuance, world-state observation, and progression advancement are coupled across the live rule stream.

Important mechanisms include:

- `gl-escrow-state` as a transaction-mode carrier;
- percentage-based `set-escrow-percentage` policy;
- transaction-specific `up-modify-escrow` reservation;
- `can-*-with-escrow` feasibility gates;
- `up-build`, `up-research`, and `up-train` execution paths;
- `release-escrow` and resource restoration;
- progression variables such as `gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause`.

The donor therefore behaves more like a **procedural economic scheduler** than a conventional production queue.

### Goals are working memory

Shadow uses goals as persistent AI-side state. They are not merely configuration constants. Progression cursors, tactical state, production state, strategy state, and interruption state survive across rule evaluations through this goal namespace.

### Rule order is executable structure

`up-jump-rule` is not a cosmetic optimization. Positive jumps skip concrete rule regions; negative jumps can create loops. Source order therefore participates in arbitration and control flow.

A Shadow transplant that preserves predicates but destroys ordering or jump destinations is not a faithful transplant. It is a rewrite wearing Shadow's name tag.

### Completion is observed

Shadow distinguishes the act of issuing a command from the later observation that the intended world state exists. Construction and progression frequently advance only after counts or research state demonstrate completion.

That makes Shadow unusually valuable as a donor for a robust `.per` AI: it already contains primitive forms of **commitment, execution, verification, progression, interruption, and re-entry**.

### Recovery is distributed

There is no single magic `RECOVERY()` routine. Recovery emerges from re-reading state, bypassing invalid paths, re-entering sequential regions, restoring resources, changing progression state, and continuing through the rule machine.

That distributed behavior is part of what must be learned rather than abstracted away.

---

## 3. Why This Machine Fits Byzantines

Byzantines are a particularly useful target for Shadow's control style because the civilization rewards **correct allocation and timely response** more than a single narrow production script.

The Byzantine design problem naturally creates competing requirements:

- maintain a viable economy while preserving resources for military responses;
- switch composition as enemy technology and unit mix change;
- exploit a broad counter-oriented roster;
- maintain infrastructure without starving military production;
- sequence technology and production without accidentally consuming resources reserved for the next requirement;
- distinguish immediate tactical requirements from longer progression commitments.

Shadow's native mechanisms map directly onto those problems.

### 3.1 Flexible counter-production

Byzantine strength is heavily tied to the ability to answer enemy composition with the appropriate counter rather than committing permanently to one unit family. Shadow already contains production arbitration, emergency branches, composition-dependent production, and jump-based preemption.

The objective is therefore not to bolt a counter-unit table onto Shadow. It is to use Shadow's **existing production control machine** to make Byzantine composition decisions executable and reversible.

### 3.2 Resource-sensitive military transitions

A Byzantine AI can easily produce the right unit at the wrong time if it spends the resources needed for a technology, infrastructure item, age transition, or emergency response. Shadow's escrow/progression machinery is directly relevant because it provides a mechanism for protecting future requirements while still allowing the current transaction to execute.

### 3.3 Expensive commitments benefit from verification

Large Byzantine commitments—technology, infrastructure, siege, elite military transitions, and other high-cost progression items—are precisely the cases where a command that merely entered the engine is not enough. Shadow's observed-completion pattern provides the correct primitive: issue, observe, reconcile, then advance.

### 3.4 Byzantine adaptation can remain small where it should

The donor machine already supplies the hard part: sequencing, arbitration, resource protection, progression, interruption, and re-entry. Byzantine-specific code should therefore describe **what the civilization needs**, while the reconstructed Shadow machine determines **how that requirement is safely executed**.

That separation is the central design principle of this repository.

---

## 4. Repository Map

Start here when navigating the repository. The links below are the **primary working surfaces**; the historical archives and individual numbered experiments are intentionally not expanded into a giant catalog.

| Area | Path | Purpose |
|---|---|---|
| **Runtime** | [`ShadowByzantine/`](./ShadowByzantine/) | Authoritative Byzantine runtime modules and reconstruction work |
| **Runtime entrypoint** | [`ShadowByzantine.per`](./ShadowByzantine.per) | AoE2 `.per` entrypoint and runtime load boundary |
| **Donor source** | [`ShadowSource.per`](./ShadowSource.per) | Canonical preserved FireBall37 Shadow source |
| **Donor references** | [`SourceRef`](./SourceRef) · [`SourceShaRef`](./SourceShaRef) | Source authentication and reference material |
| **Forensics** | [`docs/forensics/`](./docs/forensics/) | Control-flow, escrow, production, construction, military, ownership, and runtime evidence |
| **Architecture** | [`docs/architecture/`](./docs/architecture/) | Reconstruction architecture derived from the forensic record |
| **ABI / contracts** | [`docs/abi/`](./docs/abi/) | Explicit boundaries and contracts for reconstructed systems |
| **System studies** | [`docs/`](./docs/) | Numbered system deep-dives and project-level specifications |
| **Tools** | [`tools/`](./tools/) | Static extraction and forensic analysis utilities |
| **Research corpus** | [`research/`](./research/) | Research material and preserved external AI/tooling corpus, where present |

### Reading order

```text
README.md
   ↓
ShadowSource.per
   ↓
docs/forensics/
   ↓
docs/architecture/ + docs/abi/
   ↓
ShadowByzantine/
   ↓
tools/ + research/
```

The donor source is the historical evidence. The forensic layer explains what was recovered. Architecture and ABI documents state how those findings are being reconstructed. The runtime is the implementation. Tools and research material support the investigation but do not automatically become runtime dependencies.

> **Directory names are evidence boundaries, not decorative folders.** If a document contradicts the donor source, the contradiction gets investigated; it does not silently become the new history.

---

## 5. The Runtime Model

The intended runtime entrypoint is deliberately thin:

```text
ShadowByzantine.per
    |
    +--> ShadowByzantine/ShadowByzantine.per
             |
             +--> constants / Byzantine constants
             +--> state
             +--> economy
             +--> construction
             +--> reconstructed Shadow control regions
             +--> Byzantine production / military policy
```

The current reconstruction is intentionally conservative. The active orchestrator currently loads:

```text
01_constants
01b_byz_constants
02_state
03_economy
04_construction
16_pass1_transaction
```

The present Pass 1 objective is a **single complete Byzantine Spearman transaction**, from objective through resource preparation and escrow, authority, execution, world-state verification, release, and return to idle. The remaining numbered modules are retained as research/scaffolding until their control regions are sufficiently coherent to enter the authoritative runtime graph.

This is deliberate. Loading every half-finished module because the filenames look complete is how `.per` projects acquire three writers for the same goal and then spend a week pretending the parser is haunted.

---

## 6. Evidence Discipline

This project deliberately distinguishes:

- **DIRECT** — explicitly present in the donor source;
- **COMPOSED** — assembled from multiple direct observations;
- **INFERRED** — a reasoned interpretation of source behavior;
- **BYZANTINE-GENERALIZATION** — an adaptation of a donor mechanism to Byzantine requirements;
- **UNCERTAIN** — unresolved until better evidence exists.

Runtime status is separately tracked where necessary.

Two rules are non-negotiable:

> **Command issuance is not completion.**

> **Static source-order reachability is not runtime firing proof.**

Likewise, `release-escrow` does not by itself prove that escrow reached zero; `can-*-with-escrow` proves feasibility, not success; and a pending object is not automatically a completed world-state mutation.

---

## 7. Reconstruction Philosophy

The project does **not** aim to redesign Shadow into a conventional software architecture.

The reconstruction strategy is:

```text
Shadow donor
    |
    v
forensic extraction
    |
    v
control-region reconstruction
    |
    +--> preserve goals/state carriers
    +--> preserve source ordering
    +--> preserve jump semantics
    +--> preserve search loops
    +--> preserve escrow semantics
    +--> preserve observed completion
    +--> preserve interruption/re-entry
    |
    v
Byzantine adaptation
    |
    v
runtime qualification
    |
    v
measured improvement
```

Large coherent control regions are preferred over artificially tiny transaction abstractions. Shadow's behavior is distributed across production, research, construction, military, economy, and shared state; cutting every operation into a generic request/execute/release wrapper would erase the very machine being reconstructed.

---

## 8. What Makes the Project Different

Most AoE2 AI work asks: **what rules should the bot have?**

The Byzantine Shadow asks a harder question first:

> **What machine is already hidden inside a successful historical `.per` AI, and how can that machine be recovered without destroying its control semantics?**

That changes the engineering target.

The repository is simultaneously:

1. a Byzantine AI implementation;
2. a preserved Shadow donor corpus;
3. a forensic reconstruction of a historical `.per` control machine;
4. a runtime qualification project;
5. a research environment for AoE2 AI tooling and replay analysis.

The intended result is not more code. It is **more demonstrated behavior per rule**.

---

## 9. Roadmap

The reconstruction proceeds by coherent control regions rather than by randomly filling numbered files.

### Phase I — Donor recovery

- authenticate the canonical Shadow source;
- map state and goal ownership;
- recover source-order and jump topology;
- recover escrow dependency closure;
- recover construction, research, production, and military control regions;
- identify legacy and dead paths.

### Phase II — Shadow reconstruction

- transplant complete economic/progression regions;
- reconstruct production/composition control;
- reconstruct research/progression control;
- reconstruct construction/progression control;
- reconstruct military/scouting control;
- preserve arbitration and preemption edges.

### Phase III — Byzantine adaptation

- map Byzantine unit/building/technology requirements into the reconstructed control machine;
- implement civilization-specific composition policy;
- adapt economic priorities and commitments;
- preserve Shadow-style execution and verification;
- add Byzantine-specific emergency and counter-composition behavior.

### Phase IV — Qualification

Every important behavior moves through evidence levels rather than being declared complete because the parser accepted it:

```text
STATIC
  -> RUNTIME-CANDIDATE
  -> RUNTIME-QUALIFIED
  -> RUNTIME-QUALIFIED-CONDITIONAL
```

Failures remain visible. Historical donor behavior, reconstructed behavior, and new Byzantine improvements remain separately attributable.

---

## 10. Attribution

**Shadow / FireBall37:** original Shadow machine, historical control idioms, donor behavior, and source-specific mechanisms.

**The Byzantine Shadow:** reconstruction and Byzantine adaptation of those mechanisms.

**New improvements:** behavior added by this project beyond the demonstrated donor mechanism. Such improvements should be identified as adaptations rather than disguised as historical Shadow behavior.

---

## 11. Status

The repository is an active reconstruction project, not a claim that ShadowByzantine is already a finished competitive AI.

The canonical donor source is preserved. The forensic corpus is substantially developed. The Byzantine runtime exists as a deliberately narrow controlled reconstruction, with broader modules retained until their dependency and authority relationships are sufficiently understood.

The guiding rule is simple:

> **Recover the machine first. Then make it Byzantine. Then make it better. Prove each step.**
