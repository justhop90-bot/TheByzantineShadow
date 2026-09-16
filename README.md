# The Byzantine Shadow

**A forensic reconstruction and Byzantine adaptation of the FireBall/Shadow Age of Empires II AI machine.**

> **AI contribution rule:** Read [`docs/AI_SCRIPTER_OPERATING_DOCTRINE.md`](./docs/AI_SCRIPTER_OPERATING_DOCTRINE.md) **before inspecting, editing, generating, or recommending `.per` code. It is mandatory.**

The Byzantine Shadow is not a generic AI framework and it is not merely an escrow library. The project exists to **deconstruct the original Shadow control machine, preserve the mechanisms that made it unusually effective, reconstruct those mechanisms faithfully in `.per`, and then adapt the resulting machine to the Byzantine civilization without replacing Shadow's underlying control style with a modern abstraction invented from scratch.**

> **Source of truth:** this repository. Claims about Shadow behavior should be traceable to `ShadowSource.per`, preserved donor material, forensic documents, or qualified runtime evidence.

---

## 1. Project objective

The project has four linked objectives:

1. **Recover Shadow.** Determine how the original FireBall37 Shadow AI actually worked: its state carriers, rule ordering, positional jumps, timers, goals, search loops, escrow mechanisms, production sequencing, construction progression, research progression, military control, interruption, and recovery paths.
2. **Reconstruct the machine.** Rebuild the important control regions in clean Byzantine code while preserving the original `.per` execution model rather than hiding it behind a new transaction framework.
3. **Adapt the machine to Byzantines.** Replace civilization-specific assumptions with Byzantine production, composition, economy, infrastructure, technology, and military requirements while retaining Shadow's control discipline.
4. **Improve only where the evidence supports it.** New behavior is an explicit adaptation or improvement, not retroactively attributed to Shadow. Static inference, runtime qualification, and speculation remain separate.

The end product is intended to be a **Shadow-style Byzantine AI**, not an AI that happens to contain an escrow subsystem.

---

## 2. Why Shadow?

The donor is historical FireBall37 Shadow. The important discovery is that Shadow is not best understood as a pile of independent rules. Its behavior emerges from a **large sequential control machine** encoded directly in the `.per` rule stream.

Several properties make the machine distinctive:

### Escrow is part of control flow

Shadow couples resource reservation to progression state, affordability, transaction mode, command issuance, world-state observation, and progression advancement. It uses `gl-escrow-state`, percentage policy, transaction-specific escrow mutation, `can-*-with-escrow` feasibility gates, engine commands, release/restoration, and progression variables as parts of one distributed control process.

### Goals are working memory

Shadow uses goals as persistent AI-side state. Progression cursors, tactical state, production state, strategy state, and interruption state survive across rule evaluations through the goal namespace.

### Rule order is executable structure

`up-jump-rule` is not cosmetic. Positive jumps skip concrete rule regions; negative jumps can form loops. Source order therefore participates in arbitration and control flow.

### Completion is observed

Shadow distinguishes command issuance from later observation that the intended world state exists. Construction and progression frequently advance only after counts or research state demonstrate completion.

### Recovery is distributed

There is no single magic recovery routine. Recovery emerges from re-reading state, bypassing invalid paths, re-entering sequential regions, restoring resources, changing progression state, and continuing through the rule machine.

---

## 3. Why this machine fits Byzantines

Byzantines reward correct allocation and timely response across competing requirements: economy, infrastructure, technology, military production, and counter-composition.

Shadow's native mechanisms map directly onto those problems:

- **Flexible counter-production:** production arbitration, emergency branches, composition-dependent production, and jump-based preemption.
- **Resource-sensitive transitions:** escrow protects future requirements while current commitments execute.
- **Verified commitments:** expensive technology, infrastructure, siege, and military transitions benefit from issue → observe → reconcile → advance.
- **Small Byzantine policy layer:** Byzantine code should state what the civilization needs; the reconstructed Shadow machine should determine how that requirement is safely executed.

That separation is the central design principle.

---

## 4. Repository map

Start here. These are the primary working surfaces; historical archives and numbered experiments are not expanded into a giant catalog.

| Area | Path | Purpose |
|---|---|---|
| **AI doctrine** | [`docs/AI_SCRIPTER_OPERATING_DOCTRINE.md`](./docs/AI_SCRIPTER_OPERATING_DOCTRINE.md) | Mandatory pre-read and operating contract for AI contributors |
| **Runtime** | [`ShadowByzantine/`](./ShadowByzantine/) | Authoritative Byzantine runtime modules and reconstruction work |
| **Runtime entrypoint** | [`ShadowByzantine.per`](./ShadowByzantine.per) | AoE2 `.per` entrypoint and runtime load boundary |
| **Donor source** | [`ShadowSource.per`](./ShadowSource.per) | Canonical preserved FireBall37 Shadow source |
| **Donor references** | [`SourceRef`](./SourceRef) · [`SourceShaRef`](./SourceShaRef) | Source authentication and reference material |
| **Forensics** | [`docs/forensics/`](./docs/forensics/) | Control-flow, escrow, production, construction, military, ownership, and runtime evidence |
| **Architecture** | [`docs/architecture/`](./docs/architecture/) | Reconstruction architecture derived from forensic evidence |
| **ABI / contracts** | [`docs/abi/`](./docs/abi/) | Explicit boundaries and contracts for reconstructed systems |
| **Project docs / system studies** | [`docs/`](./docs/) | Project-level specifications, audits, and supporting documents |
| **Tools** | [`tools/`](./tools/) | Static extraction and forensic analysis utilities |
| **Research corpus** | [repository root](./) | Preserved external AI archives and research references; there is no `research/` directory |

### Reading order

```text
README.md
   ↓
docs/AI_SCRIPTER_OPERATING_DOCTRINE.md   ← mandatory for AI contributors
   ↓
ShadowSource.per
   ↓
docs/forensics/
   ↓
docs/architecture/ + docs/abi/
   ↓
ShadowByzantine/
   ↓
tools/ + repository-root research archives
```

The donor source is historical evidence. The forensic layer explains what was recovered. Architecture and ABI documents state how those findings are reconstructed. The runtime is implementation. Tools and the preserved root-level research corpus support investigation but do not automatically become runtime dependencies.

> **Directory names are evidence boundaries, not decorative folders.** If a document contradicts the donor source, investigate the contradiction; do not silently rewrite history.

---

## 5. Runtime model

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

The present Pass 1 objective is a **single complete Byzantine Spearman transaction**, from objective through resource preparation and escrow, authority, execution, world-state verification, release, and return to idle. Remaining numbered modules stay research/scaffolding until their dependency and authority relationships are sufficiently coherent to enter the authoritative runtime graph.

Loading every half-finished module because the filenames look complete is how `.per` projects acquire three writers for the same goal and then spend a week pretending the parser is haunted.

---

## 6. Evidence discipline

This project distinguishes:

- **DIRECT** — explicitly present in the donor source or observed runtime behavior;
- **COMPOSED** — assembled from multiple direct observations;
- **INFERRED** — reasoned interpretation not directly demonstrated;
- **BYZANTINE-GENERALIZATION** — donor mechanism adapted to Byzantine requirements;
- **UNCERTAIN** — unresolved until better evidence exists.

Two rules are non-negotiable:

> **Command issuance is not completion.**

> **Static source-order reachability is not runtime firing proof.**

Likewise, `release-escrow` does not by itself prove escrow reached zero; `can-*-with-escrow` proves feasibility, not success; and a pending object is not automatically a completed world-state mutation.

---

## 7. Reconstruction philosophy

The project does **not** aim to redesign Shadow into a conventional software architecture.

```text
Shadow donor
    ↓
forensic extraction
    ↓
control-region reconstruction
    ↓
preserve state + order + jumps + search + escrow + observers + re-entry
    ↓
Byzantine adaptation
    ↓
runtime qualification
    ↓
measured improvement
```

Large coherent control regions are preferred over artificially tiny transaction abstractions. Shadow's behavior is distributed across production, research, construction, military, economy, and shared state; cutting every operation into a generic wrapper would erase the machine being reconstructed.

---

## 8. What makes the project different

Most AoE2 AI work asks: **what rules should the bot have?**

The Byzantine Shadow asks first:

> **What machine is already hidden inside a successful historical `.per` AI, and how can that machine be recovered without destroying its control semantics?**

The repository is simultaneously:

1. a Byzantine AI implementation;
2. a preserved Shadow donor corpus;
3. a forensic reconstruction of a historical `.per` control machine;
4. a runtime qualification project;
5. a research environment for AoE2 AI tooling and replay analysis.

The target is not more code. It is **more demonstrated behavior per rule**.

---

## 9. Roadmap

### Phase I — Donor recovery

Authenticate the canonical source; map state and goal ownership; recover source-order and jump topology; recover escrow dependency closure; recover construction, research, production, and military regions; identify legacy and dead paths.

### Phase II — Shadow reconstruction

Transplant coherent economic/progression, production/composition, research, construction, and military/scouting regions while preserving arbitration and preemption edges.

### Phase III — Byzantine adaptation

Map Byzantine requirements into the reconstructed machine; implement civilization-specific composition and economic policy; preserve Shadow-style execution and verification; add Byzantine-specific emergency and counter-composition behavior.

### Phase IV — Qualification

```text
STATIC → RUNTIME-CANDIDATE → RUNTIME-QUALIFIED
                                      ↘ RUNTIME-QUALIFIED-CONDITIONAL
```

Failures remain visible. Donor behavior, reconstructed behavior, and new Byzantine improvements remain separately attributable.

---

## 10. Attribution

**Shadow / FireBall37:** original Shadow machine, historical control idioms, donor behavior, and source-specific mechanisms.

**The Byzantine Shadow:** reconstruction and Byzantine adaptation of those mechanisms.

**New improvements:** behavior added by this project beyond demonstrated donor behavior. Improvements must be identified as adaptations rather than disguised as historical Shadow behavior.

---

## 11. Status

The repository is an active reconstruction project, not a claim that ShadowByzantine is already a finished competitive AI.

The canonical donor source is preserved. The forensic corpus is substantially developed. The Byzantine runtime exists as a deliberately narrow controlled reconstruction, with broader modules retained until their dependency and authority relationships are sufficiently understood.

The rule remains:

> **Recover the machine. Then make it Byzantine. Then make it better. Prove each step.**
