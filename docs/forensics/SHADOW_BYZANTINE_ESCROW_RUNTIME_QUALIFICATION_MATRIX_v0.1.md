# Shadow → Byzantine Escrow Runtime Qualification Matrix v0.1

## Purpose

This matrix converts the static Shadow escrow reconstruction into falsifiable runtime tests. A row is **RUNTIME-QUALIFIED** only when the specified observable is captured from an actual AoE2DE execution/replay and the pass criteria are satisfied. Static rule presence, command issuance, pending-object state, or source-order reachability alone never promotes a row.

## Evidence grades

- **STATIC** — source evidence only.
- **RUNTIME-CANDIDATE** — a test has been specified and instrumentation/replay capture exists, but pass criteria are not yet demonstrated.
- **RUNTIME-QUALIFIED** — the exact observable was captured, the expected transition occurred, and negative/contradictory evidence was checked.
- **RUNTIME-QUALIFIED-CONDITIONAL** — behavior is qualified only for the tested branch/strategy/resource/objective family.
- **UNQUALIFIED** — test failed, evidence is absent, or the observable cannot distinguish the claimed transition from a weaker event.

## Global qualification rules

1. A rule firing is not completion.
2. `can-*-with-escrow` is feasibility/admission evidence, not proof that the resource was reserved.
3. `set-escrow-percentage` / `up-modify-escrow` is a reservation command, not proof of protected state.
4. `release-escrow` is a release command, not proof that the escrow balance actually became available.
5. `up-research` / `research` is command issuance, not research completion.
6. `up-build` / `build` is command issuance, not construction completion.
7. `research-pending` is not interchangeable with completion-grade world state.
8. `up-pending-objects` / `up-pending-placement` prove pending state, not completed world state.
9. Every qualification requires before/after state capture sufficient to establish causality and exclude a competing writer.
10. Static source order is never treated as runtime priority without trace evidence.

## Required capture envelope for every test

Each test should record:

- AoE2DE build/version;
- bot/source commit and SHA-256 of the loaded `.per` corpus;
- map/settings/opponents;
- game time and current age;
- relevant goals immediately before and after the candidate transition;
- relevant strategic numbers immediately before and after;
- resource balances;
- escrow amounts/percentages where observable;
- pending objects/placements;
- research status or world-object counts;
- rule/trace event that fired, if instrumentation permits;
- competing writers active in the same observation window;
- replay identifier/hash;
- exact timestamp/frame/turn window.

---

## Transition T01 — IDLE → RESERVING

### Shadow families
1172–1174, 1175–1177, 1178–1187, 1188–1197, 1198–1212, 1236–1250; construction families 1795–1800 and 1891–1892.

### Test
Force/engineer a valid objective whose Shadow-equivalent trigger is satisfied while the relevant progression gate is idle. Observe the first state-changing rule and the subsequent reservation writer.

### Exact observable
A requirement trigger is followed by the intended progression/cursor state (`gl-progression-pause`, `gl-current-build-item`, or equivalent Byzantine objective identity) and then by the family-specific escrow writer, with no intervening competing commitment.

### Pass
The objective is admitted exactly once; the intended cursor/pause becomes active; the corresponding escrow reservation writer follows; no unrelated resource commitment is attributed to the transition.

### Fail
Trigger occurs but no reservation; reservation occurs without the intended objective; another commitment wins without an observable authority decision; duplicate reservations occur.

### Promotion evidence
Replay trace containing trigger → state write → escrow write, plus before/after state snapshot and competing-writer check.

### Classification
**COMPOSED**. Shadow supplies the pieces; `RESERVING` is the reconstructed semantic state.

---

## Transition T02 — RESERVING → PROTECTED

### Shadow families
1173, 1176, 1181/1186, 1191/1196, 1201/1206, 1211, 1239, 1244, 1249, 1892.

### Test
Trigger one escrow family and observe the physical escrow state immediately before and after the reservation command.

### Exact observable
Actual engine/accounting escrow allocation/percentage changes to the requested protection level and remains associated with the active objective through at least the next control cycle.

### Pass
Physical escrow state reflects the requested reservation; the same objective remains active; competing consumers cannot consume the protected amount during the observation interval; no premature release occurs.

### Fail
Only the command is observed; physical escrow remains unchanged; reservation is immediately overwritten; protected resources are consumed by an unrelated objective.

### Promotion evidence
Runtime trace of escrow state before/after reservation plus objective identity and competing-writer exclusion. Command issuance alone cannot promote this row.

### Classification
**DIRECT** for reservation issuance; **INFERRED** for the stronger `PROTECTED` state.

---

## Transition T03 — PROTECTED → EXECUTING

### Shadow families
1174, 1177, 1178/1183, 1189/1194, 1199/1204, 1209, 1237–1240, 1241–1245, 1246–1250, 1797, 1895.

### Test
With an objectively verified protected reservation, satisfy the relevant `can-research-with-escrow` or `can-build-with-escrow` predicate and observe the engine command.

### Exact observable
The intended research/build command occurs while the intended escrow state and objective are active.

### Pass
Exactly the intended command is issued under the correct commitment; no second command for the same attempt is issued before verification.

### Fail
Command occurs without protection; wrong objective/resource is used; duplicate command fires before verification; command is attributed to a different writer.

### Promotion evidence
Trace showing protected-state observation → feasibility predicate → command issuance, with command identity and no competing writer.

### Classification
**DIRECT** for the Shadow execution gate.

---

## Transition T04 — EXECUTING → VERIFYING

### Shadow families
Research completion families 1182, 1187, 1192, 1197, 1202, 1207, 1212, 1240, 1245, 1250; construction 1893.

### Test
Issue one execution command and capture the subsequent observer/control cycle before any release is accepted.

### Exact observable
A post-command observer reads research status, building count, pending/world state, or equivalent completion evidence before the commitment is closed.

### Pass
The command is temporally followed by an observation phase; no completion claim is made solely from command issuance.

### Fail
The bot immediately marks the commitment complete solely because the command fired; no distinguishable post-command observation exists.

### Promotion evidence
Replay trace with command event followed by a distinct observation/control event and state snapshots.

### Classification
**COMPOSED**.

---

## Transition T05 — VERIFYING → RELEASE

### Shadow families
1174/1177 release paths; research-status/progression families 1182, 1187, 1192, 1197, 1202, 1207, 1212, 1240, 1245, 1250; construction reconciliation 1893.

### Test
Allow the objective to complete normally and observe the evidence used to close the commitment and release resources.

### Exact observable
Research reaches completion-grade status or construction reaches the required world-state count/object existence; only then does escrow release/rebalancing occur.

### Pass
Completion evidence precedes logical completion and release; released resources become available after reconciliation.

### Fail
Release occurs while research/build remains incomplete; `research-pending`, pending object, or command issuance is treated as completion; release occurs before world-state evidence.

### Promotion evidence
A replay segment containing pre-completion state, completion transition, post-completion state, and release/reconciliation event in causal order.

### Classification
**COMPOSED** for Shadow; the strict completion-before-release contract is **BYZANTINE-GENERALIZATION**.

---

## Transition T06 — VERIFYING → TIMEOUT

### Shadow families
Temporal/progression guards including `gl-fifth-turn`, progression pause, pending-state and status guards; no single Shadow timeout rule establishes the generalized state.

### Test
Create a controlled stalled execution where the expected completion signal does not arrive within a defined objective-specific deadline.

### Exact observable
Deadline expires while the commitment remains active and expected completion evidence is absent.

### Pass
The bot records timeout exactly once, does not falsely declare completion, and routes the stale commitment to recovery without silently consuming/releasing it as if successful.

### Fail
No timeout; repeated execution indefinitely; false completion; blind release; timeout while valid completion evidence already exists.

### Promotion evidence
Controlled replay with known deadline, timestamped command, absent completion evidence, timeout event, and subsequent recovery state.

### Classification
**BYZANTINE-GENERALIZATION**.

---

## Transition T07 — VERIFYING → RECOVERY

### Shadow families
1891–1893 and broader progression/cursor reconciliation families.

### Test
Create a controlled contradiction between expected progression and observed world state, e.g. cursor advanced beyond a required building/research state, then observe correction.

### Exact observable
World-state evidence causes the progression/cursor state to be corrected rather than blindly continuing the stale path.

### Pass
Contradiction is detected; recovery/reconciliation mutates the stale cursor; subsequent control re-enters from the corrected state.

### Fail
Stale cursor persists; bot repeatedly issues the invalid action; resource protection remains attached to the invalid objective without reconciliation.

### Promotion evidence
Before/after snapshots showing contradiction → corrective rule → corrected cursor → re-entry.

### Classification
**COMPOSED / INFERRED**.

---

## Transition T08 — RELEASE → IDLE

### Shadow families
1174, 1177, 1181/1186 release/rebalancing, 1188/1193, 1198/1203, 1208, 1895 and related release paths.

### Test
Complete one objective and observe both physical escrow reconciliation and logical commitment cleanup.

### Exact observable
Escrow returns to the intended post-commitment state; active objective/pause/cursor is cleared or advanced; resources are again available to arbitration.

### Pass
Physical and logical states converge; no stale commitment remains; a subsequent independent objective can use the released resource.

### Fail
Release command fires but protected balance remains; logical commitment remains active; next objective is blocked by stale state.

### Promotion evidence
Before/after escrow balances, logical-state snapshots, and a subsequent independent consumer demonstrating restored availability.

### Classification
**DIRECT** for release commands; **BYZANTINE-GENERALIZATION** for verified return to `IDLE`.

---

## Transition T09 — TIMEOUT → RECOVERY

### Shadow families
No direct Shadow timeout transition; temporal/progression substrate only.

### Test
Allow T06 timeout to occur and observe the next state mutation.

### Exact observable
Timeout record causes explicit failure classification/recovery rather than silent continuation.

### Pass
Recovery receives the timed-out objective with its last-known-good state and protected resources intact until recovery chooses an outcome.

### Fail
Timeout disappears; resources leak; command repeats without a new attempt; timeout is treated as success.

### Promotion evidence
Trace of timeout record → recovery classification → resource/commitment reconciliation decision.

### Classification
**BYZANTINE-GENERALIZATION**.

---

## Transition T10 — RECOVERY → RESERVING

### Shadow families
1891–1892 re-entry/cursor correction; research `come back if skipped` families.

### Test
Force a recoverable failure where retry remains feasible and observe creation of a new execution attempt.

### Exact observable
Old attempt is closed/reconciled; a new objective/attempt identity enters reservation logic; escrow is re-established from current costs/state.

### Pass
Retry does not reuse stale protected state blindly; a fresh reservation decision is observable.

### Fail
Retry fires with stale escrow; duplicate commitment identity; old command is replayed without re-arbitration.

### Promotion evidence
Two distinguishable attempts in replay with old-attempt closure and new reservation evidence.

### Classification
**COMPOSED / BYZANTINE-GENERALIZATION**.

---

## Transition T11 — PROTECTED → RECOVERY

### Shadow families
Global competing escrow writers; shared `gl-escrow-state`; progression interruption mechanisms.

### Test
Create a higher-authority objective while an existing commitment is protected, then observe whether supersession is explicit and safe.

### Exact observable
The old commitment is marked superseded/interrupted; protected resources are reconciled; recovery receives the old commitment rather than silently consuming its escrow.

### Pass
Supersession is ordered, attributable, and resource-safe.

### Fail
Two objectives consume the same protected resource; old escrow remains orphaned; new objective silently overwrites old state.

### Promotion evidence
Trace of both objectives, authority decision, old-state reconciliation, and new commitment establishment.

### Classification
**INFERRED / BYZANTINE-GENERALIZATION**.

---

## Transition T12 — EXECUTING → RECOVERY

### Shadow families
Post-command reconciliation and progression correction, especially 1891–1893.

### Test
Make the engine command execute without producing the expected world-state effect, then observe recovery behavior.

### Exact observable
Execution attempt is identified as unsuccessful/contradictory and routed to recovery rather than repeated blindly.

### Pass
No uncontrolled command loop; attempt closes or becomes recoverable; resource protection remains accounted for.

### Fail
Same command repeats indefinitely; bot assumes success; escrow is released despite failed execution.

### Promotion evidence
Trace with command, absent/contradictory effect, recovery classification, and bounded subsequent behavior.

### Classification
**INFERRED / BYZANTINE-GENERALIZATION**.

---

## Transition T13 — RESERVING → RECOVERY

### Shadow families
Reservation writers and competing state writers; no direct Shadow equivalent.

### Test
Cause reservation establishment to become impossible or contradictory after the request is issued.

### Exact observable
The partial reservation is reconciled and the objective is routed to recovery without being treated as protected.

### Pass
No orphaned escrow; logical state records failed reservation; recovery can cancel or retry.

### Fail
Partial escrow remains permanently attached; bot enters execution without a valid reservation; objective silently disappears.

### Promotion evidence
Before/after escrow and logical-state snapshots surrounding the failed reservation.

### Classification
**BYZANTINE-GENERALIZATION**.

---

## Transition T14 — RECOVERY → IDLE

### Shadow families
Release and cursor/progression reconciliation substrate; no direct generalized recovery state.

### Test
Force an unrecoverable/cancelled objective and observe complete cleanup.

### Exact observable
Physical escrow, logical objective, progression cursor, pending attempt, and authority state are reconciled before idle.

### Pass
No residual state; subsequent unrelated objective can acquire resources normally.

### Fail
Any stale escrow, cursor, pause, pending commitment, or execution-attempt state remains.

### Promotion evidence
Full before/after state dump plus successful subsequent independent commitment.

### Classification
**BYZANTINE-GENERALIZATION**.

---

# Rule-family qualification matrix

| Family | Representative rules | Primary runtime test | Exact observable | Promotion threshold |
|---|---|---|---|---|
| Scale Mail | 1172–1174 | T01–T05 | pause → food escrow → escrow-aware research → completion → release | all five causal stages observed |
| Chain Mail | 1175–1177 | T01–T05 | pause → food/gold protection → research → completion → dual release | both resources reconciled |
| Iron Casting KRUSH | 1178–1182 | T01–T05/T07 | current item + feasibility → research → pending/status reconciliation → progress | KRUSH branch only qualified if strategy identity persists |
| Iron Casting FLUSH | 1183–1187 | T01–T05/T07 | current item + food/gold escrow → research → progress | FLUSH branch only qualified if strategy identity persists |
| Forging FLUSH | 1188–1192 | T01–T05 | MID-ESCROW food; wood/gold zero/release; research; progress | physical and logical release/re-entry observed |
| Forging KRUSH | 1193–1197 | T01–T05 | KRUSH escrow/research/progress branch | branch-specific trace |
| Chain Barding KRUSH | 1198–1202 | T01–T05 | KRUSH escrow/research/progress | branch-specific trace |
| Chain Barding FLUSH | 1203–1207 | T01–T05 | FLUSH escrow/research/progress | branch-specific trace |
| Scale Barding KRUSH | 1208–1212 | T01–T05 | KRUSH escrow/research/progress | branch-specific trace |
| Fletching | 1236–1240 | T01–T05 | legacy `research`, food/gold release, pending status | must preserve legacy-path distinction |
| Leather Archer Armor | 1241–1245 | T01–T05 | escrow-aware research + MID-HIGH resource policy | physical reservation and release verified |
| Padded Archer Armor | 1246–1250 | T01–T05 | legacy research + conditional food/wood/gold reconciliation | must prove the unusual Fletching completion dependency is not misclassified |
| Farm construction | 1795–1800 | T01–T05/T07 | SPLIT → escrow mode → `up-build place-normal` → farm count | world farm count, not command, closes transaction |
| Gold Mining Camp | 1891–1893 | T01–T05/T07 | build progress → GOLDMC2 → wood policy → mining-camp count → progress | count-based reconciliation |
| Stone Mining Camp | 1894–1896 | T01–T05 | fifth-turn/search → target point → release/zero wood → `up-build place-point` | placement/world-state evidence required |

# Promotion rule

A family moves from **STATIC** to **RUNTIME-QUALIFIED** only when every mandatory observable in its transition path has been captured in at least one controlled execution and the trace rules out the weaker interpretation.

For a stronger generalized Byzantine state, the family remains **RUNTIME-QUALIFIED-CONDITIONAL** until the same semantics have been demonstrated across the relevant resource, strategy, and objective branches.

A successful command trace alone can therefore never promote:

```text
reservation command      → PROTECTED
build/research command   → COMPLETED
release command          → IDLE
pending object           → COMPLETED
source-order adjacency   → priority
```

Those require independent runtime observables.

# Required promotion artifact

Each qualified family should produce a machine-readable record containing:

```text
family_id
shadow_rule_ids
source_sha1
runtime_build
replay_hash
scenario
strategy
objective
resource_vector
pre_state
trigger_event
reservation_observation
execution_event
verification_observation
release_observation
post_state
competing_writer_check
pass_fail
qualification_level
operator_notes
```

The resulting corpus can then support a second-stage **state-transition coverage graph**, where an edge is colored/graded only from observed runtime evidence rather than source inference.
