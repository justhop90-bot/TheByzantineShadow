# Shadow Construction Runtime / Replay Qualification Matrix v0.1

## Status

**SPECIFICATION — RUNTIME QUALIFICATION PENDING**

This document defines the evidence required to promote the authenticated Shadow construction transplant from **FORENSICALLY CLOSED — STATICALLY QUALIFIED** to **RUNTIME-QUALIFIED**.

It is a test specification, not a runtime result. No row is promoted by source presence, parser acceptance, static rule reachability, rule firing, command issuance, pending-object state, or a plausible replay narrative alone.

## Scope and authoritative basis

Repository: `justhop90-bot/TheByzantineShadow`

Canonical donor: `ShadowSource.per`

Authenticated donor Git blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

Authenticated donor rule count: `1,956`

Construction transplant under qualification: rules **1794–1949**, exactly 156 rules.

Authoritative R07 boundary: **1794–1896**.

Post-R07 authenticated continuation: **1897–1949**.

Current static closure: `docs/forensics/SHADOW_CONSTRUCTION_FORENSIC_CLOSURE_2026-09-17.md`.

Existing escrow transition substrate: `docs/forensics/SHADOW_BYZANTINE_ESCROW_RUNTIME_QUALIFICATION_MATRIX_v0.1.md`.

The construction region is a contiguous authenticated transplant. Runtime qualification must nevertheless establish the engine lifecycle that static equivalence cannot establish: command acceptance, pending representation, world-state completion, progression observation, escrow reconciliation, search/placement behavior, interruption, recovery, and re-entry.

## Evidence hierarchy

Use the project's evidence hierarchy without promotion by implication:

1. **RUNTIME-QUALIFIED** — captured from actual AoE2DE execution/replay and satisfying the row's pass criteria, including contradictory/competing-writer checks.
2. **DIRECT** — exact donor or engine evidence establishing the tested primitive or rule behavior.
3. **COMPOSED** — multiple direct facts combined into a documented transition model.
4. **INFERRED** — interpretation required to connect observed/source facts.
5. **BYZANTINE-GENERALIZATION** — behavior required by the Byzantine adaptation but not directly demonstrated by Shadow.
6. **HYPOTHESIS** — testable but presently unsupported proposition.
7. **UNKNOWN** — evidence absent or insufficiently discriminating.

Runtime evidence is itself graded:

- **RUNTIME-CANDIDATE** — capture exists or test is instrumented, but the acceptance criteria are not all satisfied.
- **RUNTIME-QUALIFIED** — all required observables and pass criteria are satisfied for the tested branch/objective family.
- **RUNTIME-QUALIFIED-CONDITIONAL** — qualified only for the explicitly tested branch, resource regime, placement mode, map class, or objective family.
- **UNQUALIFIED** — failed, absent, contradictory, or non-discriminating evidence.

## Non-negotiable qualification laws

1. Rule firing is not command acceptance.
2. Command acceptance is not pending state.
3. Pending state is not world-state completion.
4. World-state completion must be established by an observable appropriate to the objective; disappearance of a pending object is insufficient by itself.
5. Progression advancement is not completion unless the replay establishes the causal completion observer/control path.
6. `can-*-with-escrow` proves feasibility/admission, not physical reservation.
7. `set-escrow-percentage` and `up-modify-escrow` prove reservation commands, not necessarily protected accounting state.
8. `release-escrow` proves a release command, not necessarily resource availability.
9. A release cannot be credited as completion merely because it occurs after a command; completion evidence must precede the logical release transition.
10. Search success is not placement success.
11. Placement acceptance is not construction completion.
12. Construction failure is not necessarily search failure, and search failure is not necessarily construction failure.
13. Interruption must be distinguishable from normal completion.
14. Recovery must be causally tied to observed contradiction, timeout, failure, or interruption; it must not be inferred from later source-order movement alone.
15. Re-entry must identify the actual progression/control region re-entered; generic retry behavior is not evidence of donor re-entry topology.
16. Static source order is never promoted to runtime priority without trace evidence.
17. Every promotion requires before/after state capture sufficient to exclude a competing writer.
18. Replay evidence must identify the loaded bot/source version and executable environment; an otherwise valid trace from another `.per` corpus is not evidence for this implementation.

---

# Required runtime evidence envelope

Every test execution must preserve, at minimum:

| Field | Requirement |
|---|---|
| `test_id` | Exact matrix ID. |
| `bot_commit` | Git commit of the tested `.per` corpus. |
| `loaded_per_sha256` | SHA-256 of the actual loaded corpus/entrypoint as applicable. |
| `aoe2de_build` | Exact executable/build identifier. |
| `map_settings` | Map, size, resources, victory condition, game speed, starting age/resources, and relevant settings. |
| `opponents` | Civilizations/AI identities and relevant difficulty/configuration. |
| `replay_id_hash` | Replay identifier/hash sufficient to identify the evidence artifact. |
| `game_time` | Timestamp/frame/turn window for each transition. |
| `current_age` | Age at transition. |
| `objective_identity` | Building/objective or construction item being tested. |
| `rule_event` | Rule identity or trace event when instrumentation permits. |
| `command_event` | Exact command family and target when observable. |
| `engine_acceptance` | Evidence that the engine accepted/queued the requested action. |
| `pending_state` | Pending object/placement evidence where applicable. |
| `world_state` | Actual object existence/location/count or other completion-grade state. |
| `progression_state` | `gl-current-build-item`, `gl-build-progress`, `gl-progression-pause`, and relevant state before/after. |
| `escrow_state` | Reservation/release state and resource balances before/after where observable. |
| `search_state` | Search reset, filters, candidate/target object, point, result/failure state where applicable. |
| `competing_writers` | Relevant alternative rules/writers active in the same observation interval. |
| `contradictory_evidence` | Any observation inconsistent with the proposed transition. |
| `qualification` | PASS / FAIL / CONDITIONAL / UNKNOWN plus evidence class. |

A replay without sufficient state correlation is **RUNTIME-CANDIDATE**, not runtime-qualified.

---

# Construction lifecycle matrix

## C01 — Rule reachability → command candidate

**Evidence class:** DIRECT / STATIC; runtime promotion requires RUNTIME evidence.

**Required observable:** The intended construction rule fires under a satisfied predicate while the correct progression/objective state is active.

**Pass:** Rule firing is attributable to the tested construction objective and precedes the expected command path without a competing rule being the actual issuer.

**Fail:** Static reachability is the only evidence; the command is attributed to an unrelated rule; objective identity is ambiguous.

**Promotion gate:** Traceable rule event + pre-state + objective identity + competing-writer check.

## C02 — Command candidate → command issued

**Evidence class:** DIRECT runtime event.

**Required observable:** The construction command is actually issued, including command family (`up-build`, `build`, or exact donor command), target/objective identity, and placement mode when applicable.

**Pass:** The expected command is emitted exactly once for the attempt while its prerequisite state is active.

**Fail:** Only rule firing is observed; command identity is unknown; duplicate command issuance occurs before verification; a different rule issues the command.

**Promotion gate:** Command event correlated to the firing rule and objective.

## C03 — Command issued → engine accepted/queued

**Evidence class:** RUNTIME-CANDIDATE until engine state is demonstrated.

**Required observable:** A post-command engine state demonstrating that the request was accepted/queued, rather than merely emitted by the AI rule machine.

**Pass:** The engine exposes a state transition consistent with accepting the construction request, and that state is causally downstream of the command.

**Fail:** Trace records only AI command emission; command may have been rejected/ignored; no discriminating engine state follows.

**Promotion gate:** Command event + subsequent engine-side acceptance/queue evidence.

## C04 — Accepted command → pending state

**Evidence class:** DIRECT runtime evidence for the engine's pending representation.

**Required observable:** `up-pending-objects`, `up-pending-placement`, or the strongest available completion-independent pending observable identifies the requested construction attempt.

**Pass:** Pending state appears after accepted command and identifies the same objective/placement attempt.

**Fail:** Pending state is absent, unrelated, or interpreted as completed world state.

**Promotion gate:** Temporal ordering `accepted command < pending state`; objective correlation required.

## C05 — Pending state → world-state completion

**Evidence class:** RUNTIME-QUALIFICATION REQUIRED.

**Required observable:** Actual construction materializes as the required world object/building at the intended location or otherwise reaches an objective-specific completion-grade world state.

**Pass:** World-state evidence exists after pending state; the pending representation is no longer treated as the completion oracle; object identity/location/count is consistent with the objective.

**Fail:** Pending state disappears without world object; command is used as completion proof; object is incomplete/incorrect/unrelated.

**Promotion gate:** Completion-grade world-state observation tied to the same objective.

## C06 — World-state completion → progression observation

**Evidence class:** COMPOSED; runtime causality required.

**Required observable:** A rule/control cycle observes completion-grade world state and then changes progression state.

**Pass:** Completion evidence precedes the progression mutation; `gl-current-build-item`, `gl-build-progress`, and/or `gl-progression-pause` changes in the donor-supported manner; competing writers are excluded.

**Fail:** Cursor advances before completion; cursor change occurs but no completion observer can be established; a different writer explains the change.

**Promotion gate:** Before/after progression snapshot + completion event + causal trace.

## C07 — Progression reconciliation → escrow release

**Evidence class:** COMPOSED / BYZANTINE-GENERALIZATION where the strict completion-before-release contract exceeds direct donor proof.

**Required observable:** Completion/reconciliation occurs before `release-escrow` or equivalent release/rebalancing mutation.

**Pass:** The objective is demonstrably complete, logical commitment/progression is reconciled, then release occurs; no premature release is observed.

**Fail:** Release occurs while incomplete; release is attributed only to command issuance; escrow is released by an unrelated writer.

**Promotion gate:** Completion → progression reconciliation → release causal chain.

## C08 — Escrow release → resource reavailability

**Evidence class:** RUNTIME-QUALIFIED REQUIRED for full transaction qualification.

**Required observable:** Post-release resource/escrow state reflects restored availability to subsequent arbitration or consumption.

**Pass:** Physical/logical escrow state is reconciled and a subsequent independent objective can legitimately use the released resources.

**Fail:** Release command occurs but resources remain unavailable; stale logical commitment blocks a subsequent objective; unexplained resource disappearance occurs.

**Promotion gate:** Pre-release and post-release resource/escrow snapshots + subsequent independent consumer.

## C09 — Release → next construction admission

**Evidence class:** COMPOSED runtime evidence.

**Required observable:** A second independent construction objective is admitted after the first objective's release/reconciliation.

**Pass:** Second objective does not inherit stale reservation state and is admitted using current resources/state.

**Fail:** Stale escrow/cursor/pause blocks the second objective or causes duplicate commitment.

**Promotion gate:** Two-objective replay with first completion/release and second admission.

---

# Search and placement matrix

## C10 — Placement request → search initialization

**Evidence class:** DIRECT / COMPOSED.

**Required observable:** Search state is reset/initialized before candidate discovery, with the correct target/reference and filters.

**Pass:** Search begins from a clean state associated with the current construction objective.

**Fail:** Stale candidate/target/point from a previous attempt contaminates the search.

**Promotion gate:** Search-state trace or replay-correlated state snapshots showing initialization.

## C11 — Search initialization → candidate/target discovery

**Evidence class:** RUNTIME-QUALIFIED REQUIRED for search qualification.

**Required observable:** Candidate discovery identifies an actual target object/point satisfying the donor-supported search predicates.

**Pass:** Candidate is found and associated with the active objective; filters and target identity are observable.

**Fail:** Search success is inferred solely from later placement; no candidate/target evidence exists.

**Promotion gate:** Search event + candidate/target identity + active objective.

## C12 — Search failure → controlled failure path

**Evidence class:** INFERRED / BYZANTINE-GENERALIZATION unless direct donor failure trace exists.

**Required observable:** A deliberately impossible or unavailable search produces a distinguishable failure state and does not fabricate a target point.

**Pass:** Search failure is recognized as search failure; construction is not falsely marked complete; control proceeds to a donor-supported or explicitly generalized retry/recovery path.

**Fail:** Stale target reused; arbitrary point treated as valid; failure silently becomes completion.

**Promotion gate:** Controlled failure replay + failure classification + bounded subsequent behavior.

## C13 — Search result → valid placement

**Evidence class:** RUNTIME-QUALIFIED REQUIRED.

**Required observable:** Returned target/point is accepted by the engine as a legal placement and produces a pending construction state.

**Pass:** Search result leads to placement acceptance and the expected pending representation.

**Fail:** Search result exists but placement is rejected, yet the test records search as placement success.

**Promotion gate:** Search result → placement command/acceptance → pending state.

## C14 — Placement rejection → retry/recovery

**Evidence class:** INFERRED / BYZANTINE-GENERALIZATION where donor evidence does not fully specify the generalized failure semantics.

**Required observable:** Deliberately invalid or obstructed placement produces rejection and a bounded corrective path.

**Pass:** Invalid placement is distinguished from successful placement; stale target state is cleared or corrected; retry/recovery is observable and bounded.

**Fail:** Infinite same-point retry; stale placement state; false completion; escrow leak.

**Promotion gate:** Controlled rejection replay with explicit failure and subsequent corrective state.

## C15 — Placement completion → progression

**Evidence class:** COMPOSED runtime evidence.

**Required observable:** Actual world object at the intended location precedes progression advancement for the placement objective.

**Pass:** World object is observable before construction progression advances.

**Fail:** Search result, placement command, or pending state advances progression without world-state completion.

**Promotion gate:** Spatial/world-object completion + progression causal ordering.

---

# Interruption, timeout, recovery, and re-entry matrix

## C16 — Executing → interruption

**Evidence class:** RUNTIME-CANDIDATE; direct donor semantics must be distinguished from project-level test injection.

**Required observable:** A controlled interruption occurs while the construction attempt is active, with snapshots of progression, escrow, pending state, and objective identity.

**Pass:** Interruption is distinguishable from normal completion and leaves a recoverable state consistent with the observed world.

**Fail:** Interruption is indistinguishable from completion; progression advances as if successful; escrow is released as if completed.

**Promotion gate:** Controlled interruption + before/after state capture.

## C17 — Interruption → recovery classification

**Evidence class:** COMPOSED / BYZANTINE-GENERALIZATION.

**Required observable:** The next control cycle recognizes the discrepancy between expected construction state and actual world state and routes it into recovery/reconciliation.

**Pass:** Recovery is attributable to the interruption/contradiction and does not silently continue the stale attempt.

**Fail:** Stale attempt continues indefinitely; no corrective state mutation; interruption is ignored.

**Promotion gate:** Interruption event → observed contradiction → recovery state/control event.

## C18 — Executing → stalled/timeout

**Evidence class:** BYZANTINE-GENERALIZATION unless a direct donor timeout branch is identified.

**Required observable:** Expected completion does not occur within a defined, reproducible objective-specific deadline.

**Pass:** Timeout is recorded once, no false completion is declared, and control proceeds to recovery/reconciliation.

**Fail:** Infinite execution loop; false completion; blind release; timeout after valid completion has already been observed.

**Promotion gate:** Timestamped command + defined deadline + absent completion evidence + timeout + recovery.

## C19 — Contradiction → recovery state mutation

**Evidence class:** COMPOSED / INFERRED.

**Required observable:** Observed world state contradicts the current progression cursor/objective, and a specific state writer corrects the contradiction.

**Pass:** The stale cursor/attempt is corrected; the correction is attributable to the expected control region; escrow remains accounted for.

**Fail:** Cursor remains stale; invalid command repeats; escrow remains orphaned.

**Promotion gate:** Contradiction snapshot → corrective state write → post-correction state.

## C20 — Recovery → fresh reservation/retry

**Evidence class:** COMPOSED / BYZANTINE-GENERALIZATION.

**Required observable:** A failed attempt is closed/reconciled before a new attempt is admitted and, where applicable, re-reserved.

**Pass:** New attempt is distinguishable from the old attempt; stale escrow is not silently reused; current feasibility is reevaluated.

**Fail:** Same attempt loops without re-arbitration; duplicate reservation; stale objective identity survives recovery.

**Promotion gate:** Two-attempt replay with old-attempt reconciliation and new reservation evidence.

## C21 — Recovery → abandonment/idle

**Evidence class:** BYZANTINE-GENERALIZATION unless direct donor path establishes equivalent behavior.

**Required observable:** An unrecoverable construction objective is cancelled/reconciled and returns control to an idle/available state.

**Pass:** No stale objective, escrow, pause, pending commitment, or progression cursor remains that can contaminate the next independent objective.

**Fail:** Residual state survives cancellation; subsequent objective inherits stale state.

**Promotion gate:** Full pre/post state dump + subsequent independent objective.

## C22 — Recovery → donor control-region re-entry

**Evidence class:** RUNTIME-QUALIFIED REQUIRED for re-entry qualification.

**Required observable:** After recovery, the next active rule/control region corresponds to the expected donor source-order/jump topology and current progression state.

**Pass:** Re-entry is traceable to a valid donor-supported region; no invented centralized recovery dispatcher is required to explain the transition.

**Fail:** Re-entry jumps to an unsupported region; stale source position is resumed; centralized control behavior appears without donor analogue.

**Promotion gate:** Rule/control trace + progression state + source-order/jump correlation.

## C23 — Re-entry → successful second attempt

**Evidence class:** RUNTIME-QUALIFIED-CONDITIONAL until repeated across relevant branches.

**Required observable:** A recovered objective can re-enter construction, execute, complete, and reconcile without residual state from the failed attempt.

**Pass:** Second attempt completes normally and all C02–C09 conditions relevant to the branch are satisfied.

**Fail:** Re-entry succeeds syntactically but stale escrow/search/progression state corrupts the second attempt.

**Promotion gate:** Failure → recovery → re-entry → second successful completion trace.

---

# Adversarial and regression matrix

## C24 — Escrow reuse under sequential objectives

**Required observable:** Objective A reserves resources, completes, releases/reconciles, and Objective B subsequently consumes the same resource class.

**Pass:** No resource double-counting, stale reservation, or release leak is observed.

**Fail:** B cannot legitimately access released resources or A's escrow remains logically active.

**Evidence class:** RUNTIME-QUALIFIED REQUIRED.

## C25 — Competing objective during protected construction

**Required observable:** A second objective becomes eligible while A is protected/executing.

**Pass:** Arbitration is attributable and resource-safe; A is preserved, interrupted, superseded, or allowed to complete according to the actual tested donor/Byzantine policy path.

**Fail:** Silent state overwrite, double allocation, or orphaned escrow.

**Evidence class:** INFERRED / BYZANTINE-GENERALIZATION unless the exact donor arbitration path is directly exercised.

## C26 — Repeated successful constructions

**Required observable:** At least multiple sequential construction transactions traverse command acceptance, pending, world completion, progression, release, and next admission.

**Pass:** The same causal contract holds without accumulating stale state.

**Fail:** First transaction succeeds but later transactions reveal state leakage or ordering dependence.

**Evidence class:** RUNTIME-QUALIFIED-CONDITIONAL until the tested objective family is repeated.

## C27 — Mixed placement modes

**Required observable:** Separate successful traces for NORMAL, POINT, and CONTROL placement modes where those modes are actually reachable in the transplanted interval.

**Pass:** Each tested mode establishes its own search/placement/acceptance/completion chain; no mode is inferred from another.

**Fail:** One mode is used as evidence for another without direct execution evidence.

**Evidence class:** RUNTIME-QUALIFIED-CONDITIONAL.

## C28 — Negative-control construction

**Required observable:** A construction request that should not be admitted under the selected state/resource/placement conditions.

**Pass:** No false construction command/pending object/world object occurs, and no escrow is incorrectly committed.

**Fail:** Bot constructs despite failed prerequisite, falsely reserves, or advances progression.

**Evidence class:** RUNTIME-QUALIFIED REQUIRED for boundary confidence.

## C29 — Replay determinism / repeatability

**Required observable:** Repeated equivalent scenarios produce the same lifecycle ordering for the tested branch, subject to explicitly documented engine nondeterminism.

**Pass:** Required causal ordering remains stable across repeated runs; any variation is identified and bounded.

**Fail:** Qualification depends on an unreproducible timing accident or unexplained race.

**Evidence class:** RUNTIME-QUALIFIED-CONDITIONAL.

---

# Minimum scenario suite

The following scenarios are the minimum evidence set before claiming construction runtime qualification:

| Scenario | Exercises |
|---|---|
| S01 Normal successful construction | C01–C09 |
| S02 Successful POINT placement | C10–C15 |
| S03 Search failure | C10–C12 |
| S04 Placement rejection | C13–C15, C19–C20 |
| S05 Interrupted construction | C16–C17, C19–C23 |
| S06 Stalled construction / timeout | C18–C21 |
| S07 Escrow reuse | C07–C09, C24 |
| S08 Competing objective | C25 |
| S09 Repeated construction | C26 |
| S10 Mixed placement modes where reachable | C27 |
| S11 Negative control | C28 |
| S12 Replay repeatability | C29 |

A scenario may satisfy multiple rows, but evidence must still be attributable to each row's exact observable and pass criteria.

---

# Promotion gates

## Gate G0 — Static baseline

**Required:** Current authenticated construction interval remains statically qualified against donor.

**Evidence:** `STATIC_DONOR_EQUIVALENCE=PASS`, source order/jump topology preserved, compatibility constants verified.

**Current status:** PASS as recorded by the construction forensic closure.

## Gate G1 — Command path

**Required:** C01–C03 pass for at least one representative construction branch.

**Promotion:** `RUNTIME-CANDIDATE → COMMAND-QUALIFIED`.

**Not sufficient for:** construction completion.

## Gate G2 — Pending semantics

**Required:** C04 passes and pending state is demonstrated as a post-acceptance, pre-completion representation.

**Promotion:** `COMMAND-QUALIFIED → PENDING-QUALIFIED`.

## Gate G3 — World-state completion

**Required:** C05 passes on a real completed construction.

**Promotion:** `PENDING-QUALIFIED → COMPLETION-QUALIFIED`.

**Hard condition:** pending state must not be used as the completion oracle.

## Gate G4 — Progression causality

**Required:** C06 and C15 pass.

**Promotion:** `COMPLETION-QUALIFIED → PROGRESSION-QUALIFIED`.

**Hard condition:** progression mutation must follow completion-grade world evidence in the causal trace.

## Gate G5 — Escrow reconciliation

**Required:** C07–C09 and C24 pass.

**Promotion:** `PROGRESSION-QUALIFIED → ESCROW-QUALIFIED`.

**Hard condition:** release command and physical/logical resource reavailability must both be evidenced.

## Gate G6 — Search/placement

**Required:** C10–C15 plus the reachable placement modes needed by the transplanted branch.

**Promotion:** `ESCROW-QUALIFIED → PLACEMENT-QUALIFIED`.

**Hard condition:** search success, placement acceptance, and world completion remain separate observables.

## Gate G7 — Interruption and recovery

**Required:** C16–C23, including at least one controlled interruption or stalled execution and one successful recovery/re-entry cycle.

**Promotion:** `PLACEMENT-QUALIFIED → RECOVERY-QUALIFIED`.

**Hard condition:** recovery must not be inferred from ordinary success-path fall-through.

## Gate G8 — Adversarial/regression qualification

**Required:** C25–C29 and repeated successful construction evidence.

**Promotion:** `RECOVERY-QUALIFIED → RUNTIME-QUALIFIED-CONDITIONAL` for the explicitly covered branch/objective family.

## Gate G9 — Full construction runtime qualification

The construction interval may be labeled **RUNTIME-QUALIFIED** only when:

- G1–G8 pass;
- all reachable construction lifecycle classes represented by the authenticated interval have been exercised or explicitly excluded with evidence;
- command acceptance, pending state, world completion, progression, escrow release/reallocation, search, placement, interruption, recovery, and re-entry have each been directly observed at the level required by their rows;
- competing writers have been checked for each promoted transition;
- contradictory observations are recorded rather than omitted;
- replay/source provenance identifies the exact tested bot corpus and AoE2DE build;
- no promotion depends on treating command issuance, pending state, parser acceptance, or static source order as a stronger event than it is;
- repeated execution demonstrates that the observed behavior is not a one-off timing accident.

If only a subset is demonstrated, the correct status is **RUNTIME-QUALIFIED-CONDITIONAL**, with the exact qualified branch and remaining unknowns named.

---

# Appendix T-A — Tranche A S01 run-book (first live probe)

Status of this appendix: procedure, not evidence. No gate is claimed here.

## T-A.1 Bot corpus under test

- Repository: `justhop90-bot/TheByzantineShadow`, branch with Tranche A
  (timer/turn tail 1950–1956, `03b_strategy_bootstrap.per`, compat
  constants, `02_state` stub, `03_economy` caps).
- Install: `ShadowByzantine.ai` (0 bytes) + `ShadowByzantine.per` (root,
  single load line) + `ShadowByzantine/` folder (23 modules) copied to the
  live `ai/` directory. Verify all 8 loaded modules present before launch:
  `01_constants`, `01a_shadow_r07_compat`, `01b_byz_constants`,
  `02_state`, `03_economy`, `03b_strategy_bootstrap`, `04_construction`,
  `16_pass1_transaction`.
- Record `BOT_COMMIT` (git SHA), per-file SHA-256 of the 8 loaded modules,
  and the AoE2DE build number in every evidence packet.

## T-A.2 Match setup (S01 Normal successful construction)

- Map: Arabia, Tiny (2 players). Self: Byzantines + ShadowByzantine bot.
  Opponent: Stock AI, Moderate (non-interfering baseline; no early rush
  expected, so S01 stays a construction probe, not a defense test).
- Speed: Normal (1.7x max for observation fidelity; faster speeds compress
  causal order in replays). Record full replay (`.aoe2record` retained).
- Launch flags for AI telemetry if available: `LOGSYSTEMS=AIScript`
  `VERBOSELOGGING` `CONSTANTLOGGING` (chat-based donor telemetry —
  e.g. "LC1", "Krush Farms Built" — is otherwise the primary trace).

## T-A.3 Observation checklist (maps to rows C01–C09)

1. **Timers live (G0→G1 support):** within the first minute, turn-gated
   donor rules must become eligible — observe any `gl-fifth-turn`-gated
   farm/house rule firing (chat trace or placement). If nothing gated on
   turn goals ever fires, the tail transplant is not executing: stop,
   do not promote.
2. **Strategy default (G1):** `gl-strategy` must read FLUSH (default rule
   1416 fires at game start; KRUSH only via FFA/taunt/pocket). Confirm via
   FLUSH-gated farm rules (FARMS item) progressing `gl-build-progress`
   past `FarmsNumber`.
3. **First command (C01–C03):** first `up-build` for house/farm — record
   T_RULE (issuing rule id), T_COMMAND (engine queue acceptance observable:
   foundation appears / villager assigned via `up-assign-builders`).
4. **Pending (C04):** `up-pending-objects` > 0 while foundation exists but
   building incomplete — pending as post-acceptance, pre-completion state.
5. **Completion (C05):** `building-type-count-total` increments with
   pending back to 0 — world-state oracle, never the pending count.
6. **Progression (C06):** `gl-build-progress` increments only AFTER the
   corresponding world completion (causal order in replay frames).
7. **Escrow (C07–C09):** wood escrow percentage/collect/release cycle
   around the build (LOW-ESCROW set on item set, release on fire);
   record ESCROW_BEFORE/AFTER + RESOURCES_BEFORE/AFTER.
8. **Competing writers:** during the probe, confirm no module outside
   `04_construction.per` writes `gl-build-progress` /
   `gl-current-build-item` (the unloaded 05–15 set must stay unloaded).

## T-A.4 Failure handling

Any deviation is recorded with the ledger reason codes of this matrix
(`COMMAND_ONLY`, `PENDING_ONLY`, `NO_WORLD_COMPLETION`,
`NO_CAUSAL_PROGRESSION`, `NO_ESCROW_RECONCILIATION`, `COMPETING_WRITER`,
...) — never narrated away. A failed S01 returns to static analysis;
a passed S01 promotes exactly one branch (Dark-age farm/house) to G1,
not the interval.

---

# Evidence packet schema

A machine-readable or tabular evidence record should contain:

```text
TEST_ID:
SCENARIO_ID:
EVIDENCE_CLASS:
QUALIFICATION_STATUS:
BOT_COMMIT:
LOADED_PER_SHA256:
AOE2DE_BUILD:
MAP_SETTINGS:
OPPONENTS:
REPLAY_ID_HASH:
OBJECTIVE_IDENTITY:
PLACEMENT_MODE:

T_RULE:
T_COMMAND:
T_ACCEPTED:
T_PENDING:
T_WORLD_COMPLETION:
T_PROGRESSION:
T_RELEASE:
T_REENTRY:

RULE_EVENT:
COMMAND_EVENT:
ENGINE_ACCEPTANCE:
PENDING_STATE:
SEARCH_STATE:
PLACEMENT_STATE:
WORLD_STATE:
PROGRESSION_BEFORE:
PROGRESSION_AFTER:
ESCROW_BEFORE:
ESCROW_AFTER:
RESOURCES_BEFORE:
RESOURCES_AFTER:

COMPETING_WRITERS:
CONTRADICTORY_EVIDENCE:
FAILURE_MODE:
RECOVERY_EVENT:
REENTRY_REGION:

PASS_CRITERIA:
FAIL_CRITERIA:
RESULT:
RATIONALE:
EVIDENCE_ARTIFACT:
```

The timestamps are not required to be literal wall-clock values; replay frame/turn/game-time coordinates are acceptable when they provide an unambiguous causal order.

---

# Qualification ledger rules

For every failed or incomplete row, preserve the reason rather than collapsing it into `UNKNOWN`. Use one of:

- `NO_CAPTURE`
- `NON_DISCRIMINATING_CAPTURE`
- `COMMAND_ONLY`
- `PENDING_ONLY`
- `NO_WORLD_COMPLETION`
- `NO_CAUSAL_PROGRESSION`
- `NO_ESCROW_RECONCILIATION`
- `SEARCH_UNPROVEN`
- `PLACEMENT_UNPROVEN`
- `INTERRUPTION_UNPROVEN`
- `RECOVERY_UNPROVEN`
- `REENTRY_UNPROVEN`
- `COMPETING_WRITER`
- `CONTRADICTORY_TRACE`
- `REPLAY_PROVENANCE_MISMATCH`
- `REPEATABILITY_FAILURE`
- `ENGINE_SEMANTICS_UNKNOWN`

Do not replace an unqualified transition with a narrative assertion that it “obviously” occurred.

---

# Final promotion model

The authoritative progression is:

```text
FORENSICALLY CLOSED — STATICALLY QUALIFIED
        ↓
G1 COMMAND-QUALIFIED
        ↓
G2 PENDING-QUALIFIED
        ↓
G3 COMPLETION-QUALIFIED
        ↓
G4 PROGRESSION-QUALIFIED
        ↓
G5 ESCROW-QUALIFIED
        ↓
G6 PLACEMENT-QUALIFIED
        ↓
G7 RECOVERY-QUALIFIED
        ↓
G8 RUNTIME-QUALIFIED-CONDITIONAL
        ↓
G9 RUNTIME-QUALIFIED
```

This ladder is intentionally asymmetric: each higher state requires a stronger observable than the previous state. No lower-grade event may be substituted for a higher-grade completion oracle.

## Explicit remaining unknowns at document creation

The construction forensic closure establishes static donor equivalence for rules 1794–1949, including rule identity, predicates/actions, `disable-self`, explicit jump topology, source order, and principal state-touch parity. It does **not** establish live AoE2DE semantics for command acceptance, pending representation, actual construction completion, progression causality, escrow release/reallocation, search/placement success or failure, interruption, recovery, re-entry, or replay equivalence. Those remain runtime evidence targets under this matrix.

## Relationship to the existing escrow matrix

This construction matrix is the construction-specific runtime authority for the full lifecycle. The existing `SHADOW_BYZANTINE_ESCROW_RUNTIME_QUALIFICATION_MATRIX_v0.1.md` remains the detailed escrow transition reference. Where the two overlap, this document uses the stricter construction transaction rule: escrow evidence must be correlated to the actual construction objective and its world-state lifecycle rather than qualified in isolation.
