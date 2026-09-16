# Shadow DC7 — Escrow Transplant Slices v0.1

## Purpose

This document converts the recovered Shadow escrow/control-flow evidence into transplantable behavioral slices for The Byzantine Shadow. The objective is **not** to copy Shadow wholesale and not to replace Shadow's economic machinery with a cleaner but unproven AEGIS abstraction. The objective is to isolate the smallest reusable behavioral units that preserve the creator's successful economic-control strategy while allowing Byzantine-specific cognition to replace Viking-specific strategic intent.

## Forensic basis

- Historical Shadow source commit: `1d9f45b3b9ac03adc24103df2b21c84b92a45fb6`
- Historical Git blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`
- Extracted source SHA-256: `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`
- Source: 22,604 lines / 615,773 UTF-8 bytes
- Extracted rules: 1,956 `defrule` blocks
- Primary companion artifact: `docs/forensics/SHADOW_LIVE_CONTROL_FLOW_AND_ESCROW_v0.2.md`
- Primary graph artifact: `docs/forensics/SHADOW_LIVE_CONTROL_FLOW_v0.2.svg`

## Evidence rule

Static source reachability is not runtime proof. Command issuance is not completion. An escrow mutation is not proof that the intended amount was successfully protected. A release command is not proof that the engine released the resource. These slices therefore terminate in **observed state**, not merely issued commands.

## Core decomposition

Shadow's recoverable economic mechanism decomposes into six orthogonal functions:

1. **Requirement trigger** — strategic/progression state identifies a temporary need.
2. **Interruption cursor** — `gl-progression-pause`, `gl-current-build-item`, and `gl-build-progress` preserve where the larger progression machine was interrupted.
3. **Physical protection** — `up-modify-escrow` and escrow-percentage operations protect or redirect actual engine resources.
4. **Escrow-aware execution** — `up-research gl-escrow-state ...` / `up-train gl-escrow-state ...` execute through the engine's escrow accounting mode.
5. **Reconciliation** — research/production status is observed and progression state advances or is restored.
6. **Release/return** — temporary escrow is zeroed/released and the broader strategy resumes.

The reusable unit is therefore **not** a rule. It is a state transition chain.

## Slice matrix

| Slice | Observed Shadow mechanism | Strategic payload | Reusable substrate | Byzantine adaptation |
|---|---|---|---|---|
| S01 — Temporary research reservation | Set interruption state -> modify escrow -> escrow-aware research -> clear interruption -> release | Vikings/Shadow progression decision | Requirement interruption, physical reservation, escrow-aware execution, release | Replace trigger with Byzantine capability gap: e.g. anti-cavalry, anti-archer, defensive survival, Imperial timing |
| S02 — Multi-resource reservation | Set interruption -> reserve food + gold -> escrow-aware research -> clear -> zero/release both | Chain Mail progression | Multi-resource reservation and atomic-ish release sequence | Candidate for Byzantine tech/counter transitions whose cost vector spans food/gold or food/wood/gold |
| S03 — Progression cursor recovery | Detect skipped research -> restore `gl-build-progress` -> restore `gl-current-build-item` | Shadow strategy-specific build progression | Re-entry/reconciliation mechanism | Preserve generic cursor logic; Byzantine policy supplies the progression milestones |
| S04 — Resource rebalancing | Change escrow percentages by progression phase; release no-longer-required resource | Shadow economic pacing | Dynamic protection rather than fixed reservation | Use to protect Byzantine transition reserves while permitting adaptive counter production |
| S05 — Research completion reconciliation | Observe research status >= pending/completed threshold -> increment progression | Shadow upgrade sequencing | Completion-driven state advancement | Bind to Byzantine tech requirement verification, never to command issuance |
| S06 — Temporary interruption return | Clear pause and release protected resources after execution | Shadow's strategic continuity | Interruption -> execute -> restore | Required for Byzantine reactive switching without destroying long-horizon progression |
| S07 — Command accounting mode | `gl-escrow-state` passed into `up-research`/`up-train` | Engine accounting choice | Execution mode parameter | Preserve as engine interface; do not reinterpret as logical commitment owner |
| S08 — Release discipline | Set escrow percentage to zero and issue resource-specific release | Shadow economic cleanup | Resource-specific release | Preserve physical escrow ownership in Shadow substrate unless runtime evidence proves otherwise |

## Proven concrete exemplars

### S01 — Scale Mail

Recovered source-order path:

```text
1172  strategic/progression trigger
  -> gl-progression-pause = SCALEMAIL
1173  physical reservation
  -> up-modify-escrow food c:max 100
1174  execution + cleanup
  -> up-research gl-escrow-state c: ri-scale-mail
  -> clear gl-progression-pause
  -> set food escrow percentage 0
  -> release food
```

This is the cleanest single-resource example of Shadow treating a temporary strategic requirement as an economic transaction without creating a separate executor.

### S02 — Chain Mail

```text
1175  strategic/progression trigger
  -> gl-progression-pause = CHAINMAIL
1176  physical reservation
  -> up-modify-escrow food c:max 200
  -> up-modify-escrow gold c:max 100
1177  execution + cleanup
  -> up-research gl-escrow-state c: ri-chain-mail
  -> clear gl-progression-pause
  -> zero food/gold escrow percentages
  -> release food/gold
```

The important reusable property is not the specific technology. It is the ability to protect a **vector** of resources for one temporary requirement and restore the economy afterward.

### S03 — Iron Casting / progression reconciliation

Shadow contains parallel KRUSH and FLUSH paths. The recovered sequence includes:

```text
research not pending + build-progress beyond milestone
        -> restore build-progress to milestone
        -> restore current-build-item = IRONCASTING
        -> configure escrow policy
        -> escrow-aware research
        -> observe research state
        -> increment build-progress
```

This demonstrates that Shadow anticipates state drift and does not assume its progression cursor is always correct. That property is more important for a Byzantine adaptive AI than the particular Iron Casting policy.

### S04 — Forging family

The Forging sequence repeats the same architecture with strategy-dependent escrow percentages and resource release. The repetition across separate progression items is strong evidence that the creator was implementing a **general economic interruption pattern**, not a one-off Iron Casting hack.

## What must be transplanted byte-for-byte vs redesigned

### Preserve as substrate

- The physical escrow primitives and their ordering semantics.
- The distinction between escrow accounting mode and escrow amount.
- The progression interruption concept.
- Cursor reconciliation after skipped progression.
- Resource-specific release behavior.
- Completion observation before advancing progression.
- The ability to re-enter a broader strategic sequence after an interruption.

### Do not blindly transplant

- Viking-specific strategy predicates.
- Viking build-order constants.
- Strategy labels whose semantics are not Byzantine-compatible.
- Unit/resource priorities derived from Viking composition.
- Comments or chat messages as if they were executable semantics.
- Any rule whose apparent behavior depends on an unverified external goal writer.

### AEGIS should own

- Capability-gap classification.
- Requirement identity.
- Candidate response generation.
- Byzantine-specific arbitration.
- Logical authorization.
- Verification policy.

### Shadow substrate should own initially

- Physical escrow.
- Resource protection/rebalancing.
- Escrow-aware engine accounting.
- Concrete research/train execution where already proven.
- Release mechanics.
- Progression cursor restoration.

This boundary is evidence-driven. It can change only after a concrete runtime defect and a demonstrated replacement advantage.

## Byzantine-specific requirement model

The transplant target should not be a fixed Byzantine build order. It should be a capability-response loop:

```text
ENEMY / WORLD OBSERVATION
        ↓
THREAT CLASSIFICATION
        ↓
CAPABILITY GAP
        ↓
CANDIDATE RESPONSES
        ↓
ENGINE COST VECTOR
        ↓
BYZANTINE RELATIVE EFFICIENCY
        ↓
AEGIS ARBITRATION
        ↓
TEMPORARY REQUIREMENT
        ↓
SHADOW ECONOMIC INTERRUPTION
        ↓
PHYSICAL ESCROW
        ↓
EXISTING EXECUTOR
        ↓
OBSERVED WORLD RESULT
        ↓
AEGIS VERIFICATION
        ↓
RELEASE / RESTORE
        ↓
REASSESS
```

Byzantine-specific adaptation should exploit the civilization's broad counter access and discounted counter-unit lines rather than hard-code a single answer. The same escrow substrate should be able to finance different requirements at different times.

## Critical anti-patterns

1. **Do not create a second escrow system in AEGIS.** A logical commitment ledger may describe intent, but it must not silently become a competing physical reservation mechanism.
2. **Do not treat `can-research-with-escrow` as proof of completion.** It is a feasibility/affordability gate.
3. **Do not treat `up-research` or `up-train` as completion.** Completion must be observed through engine state.
4. **Do not clear the interruption cursor merely because a command was issued unless the source behavior intentionally uses that as an execution latch and the runtime contract is verified.**
5. **Do not release an escrow resource merely because a release command was emitted.** The engine state must be observed when release correctness matters.
6. **Do not copy all 1,956 rules.** Extract behavioral slices and dependencies; preserve source order only where source order is semantically required.
7. **Do not replace Shadow because its implementation is ugly.** Ugly control flow can still encode a highly effective state machine.

## Transplant qualification levels

- **T0 — Source evidence:** exact Shadow source mechanism identified.
- **T1 — Structural transplant candidate:** dependencies and state variables mapped; no runtime claim.
- **T2 — Static integration candidate:** inserted into Byzantine architecture with namespace/load-order qualification.
- **T3 — Runtime qualified:** observed to execute correctly in AoE2DE.
- **T4 — Behavioral qualified:** repeated runtime evidence demonstrates the intended economic/strategic effect.
- **T5 — Production substrate:** Byzantine policy is using the mechanism as a stable economic actuator.

No slice should be promoted based solely on source similarity.

## Next forensic action

The next extraction should identify the **full dependency closure of each reservation/release family**: every writer of its trigger state, every writer of its escrow mode, every reader of its completion state, every progression cursor it mutates, every jump that can bypass or re-enter it, and every conflicting writer elsewhere in Shadow. That dependency closure is the actual transplant boundary.

The goal is not a Shadow clone. The goal is to recover the economic control architecture that made Shadow adaptable, then give that architecture Byzantine cognition.