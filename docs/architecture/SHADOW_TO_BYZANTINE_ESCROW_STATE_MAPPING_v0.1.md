# Shadow → Byzantine Escrow State Mapping v0.1

## Status

Concrete reconstruction specification. This document maps recovered Shadow escrow/progression/construction evidence onto the proposed Byzantine escrow state machine.

It is intentionally stricter than a normal architecture document: every transition has an evidence contract. A transition is not considered implemented merely because a rule fires or a command is issued.

## Evidence rule

The Byzantine state machine may generalize Shadow's control idiom, but it may not silently promote an engine action into world-state truth.

The governing distinctions are:

- **command issuance ≠ completion**
- **`can-build-with-escrow` / `can-research-with-escrow` ≠ completion**
- **`release-escrow` ≠ proof of release**
- **`gl-escrow-state` ≠ commitment owner**
- **`up-pending-objects` / `up-pending-placement` ≠ completed world state**
- **source-order reachability ≠ runtime firing proof**
- **timeout ≠ impossibility**
- **recovery ≠ silent cancellation**

The existing Shadow closure identifies `gl-strategy`, `gl-build-progress`, `gl-current-build-item`, `gl-progression-pause`, and the physical escrow namespace as shared substrate. The Byzantine machine therefore treats the escrow lifecycle as a connected control system rather than a resource helper.

---

# 1. Byzantine state machine

```text
IDLE
  |
  | objective accepted + arbitration permits commitment
  v
RESERVING
  |
  | required protection established and still valid
  v
PROTECTED
  |
  | feasibility + authority + execution preconditions proven
  v
EXECUTING
  |
  | engine command issued
  v
VERIFYING
  |                    \
  | completion evidence  \ contradictory/stale evidence
  v                       v
RELEASE                TIMEOUT
  |                       |
  | release verified      v
  |                    RECOVERY
  |                  /    |     \
  |               retry substitute cancel
  |                  \    |     /
  +-------------------\---+----/
                       v
                  IDLE / RESERVING
```

`TIMEOUT` is a diagnostic state entered when the commitment no longer has sufficient evidence of progress. It is not itself a failure verdict.

---

# 2. State semantics

| State | Semantic meaning | Shadow evidence class | Byzantine invariant |
|---|---|---|---|
| `IDLE` | no active protected commitment | progression/re-entry | no resource may be attributed to a dead commitment |
| `RESERVING` | attempting to establish resource protection | `set-escrow-percentage`, reservation writers | reservation is provisional until observed |
| `PROTECTED` | objective has an active protected economic allocation | escrow configuration + cursor/pause state | competing actions cannot silently consume protected capacity |
| `EXECUTING` | selected engine action has been admitted/issued | `up-research`, `up-build`, `build`, train/research commands | command is an event, not completion |
| `VERIFYING` | waiting for world-state evidence | `research-status`, building counts, pending-object/placement observations | no completion state without post-command evidence |
| `RELEASE` | release/reconciliation requested | `release-escrow`, zeroing percentage, cursor cleanup | release request must itself be verified |
| `TIMEOUT` | progress evidence expired or contradictory | timer/turn/progress evidence | stale commitment cannot remain protected indefinitely |
| `RECOVERY` | explicit resolution of failed/stale commitment | release/reconcile/retry/substitute paths | recovery must restore coherent state before re-entry |

---

# 3. Transition matrix

## T00 — IDLE → RESERVING

### Shadow evidence

Primary evidence is the family trigger preceding reservation configuration:

- research families: 1172, 1175, 1179, 1184, 1189, 1194, 1199, 1204, 1209, 1237, 1242, 1247
- construction/progression families: 1795, 1799, 1891–1896

Representative construction path:

```text
1795: requirement conditions satisfied
  → SPLIT = 1
1796: SPLIT 1 → SPLIT 2 after threshold
1797: SPLIT 2 → up-build ... farm
1798: escrow-state = with-escrow; SPLIT = 0
```

The research families use strategic predicates such as strategy, age, pause, prerequisite completion, enemy context, current item, and progression cursor before writing reservation state.

### Required Byzantine evidence

1. A current objective/requirement exists.
2. The objective is authorized by current policy.
3. No higher-precedence commitment owns the required resource.
4. The objective has a known cost vector.
5. The requested resource protection is compatible with current economic floor constraints.
6. The commitment has a unique identity/cursor.
7. The commitment start timestamp/turn is written before reservation begins.
8. The intended execution class is known: research, construction, training, or other supported action.

### Failure

If any prerequisite is absent, remain `IDLE`; do not create partial escrow.

---

# 4. T01 — RESERVING → PROTECTED

### Shadow evidence

Reservation writers include:

- 1173: food reservation for Scale Mail
- 1176: food + gold reservation for Chain Mail
- 1181 / 1186: Iron Casting branch-specific escrow policy
- 1191 / 1196: Forging branch-specific policy
- 1201 / 1206: Chain Barding branch-specific policy
- 1211: Scale Barding policy
- 1239: Fletching reservation
- 1244: Leather Archer Armor reservation
- 1249: Padded Archer Armor rebalancing
- 1892: `set-escrow-percentage wood LOW-ESCROW` for the Gold Mining Camp progression item
- 1895: explicit release/zeroing of wood around mining-camp execution

The closure evidence shows that these writers share a physical escrow namespace with other families; they cannot be treated as private variables.

### Required Byzantine evidence

All of the following must be true:

1. Reservation policy was actually issued.
2. The intended escrow percentages/amounts are observable after the write.
3. Reserved resources satisfy the commitment's minimum protected amount.
4. The commitment cursor still names the same objective.
5. The strategic mode has not changed in a way that invalidates the reservation.
6. No competing authority has superseded the commitment.
7. The reservation has not already exceeded its freshness guard.
8. The protected allocation does not violate emergency-resource floors.

### Important rule

A `set-escrow-percentage` action alone proves **RESERVATION_REQUESTED**, not `PROTECTED`.

`PROTECTED` requires post-write evidence that the reservation exists in the engine/accounting state.

---

# 5. T02 — RESERVING → TIMEOUT

### Shadow-derived basis

Shadow supplies the ingredients but not a universal timeout abstraction:

- progression pause states
- turn/time guards
- `gl-fifth-turn`
- research status predicates
- construction progression guards
- pending-object / pending-placement observations

For example, 1894 requires `gl-fifth-turn 1` and `gl-progression-pause -1` before searching for the stone mining camp. The construction sequence also separates command issuance from subsequent progression evidence.

### Required Byzantine evidence

Timeout requires **absence or invalidation of expected progress**, not merely elapsed time.

At minimum:

1. commitment age exceeds action-specific timeout;
2. expected progress evidence has not appeared;
3. commitment remains active;
4. no valid explanation for the delay exists;
5. the objective has not already completed under another path.

A timeout must record the last verified progress state before entering `TIMEOUT`.

---

# 6. T03 — PROTECTED → EXECUTING

### Shadow evidence

Research:

- 1174: `can-research-with-escrow` → `up-research ...`
- 1177: same pattern for Chain Mail
- 1178 / 1183: Iron Casting execution
- 1188 / 1193: Forging execution
- 1198 / 1203: Chain Barding execution
- 1208: Scale Barding execution
- 1236 / 1246: legacy research command boundary
- 1241: Leather Archer Armor execution

Construction:

- 1797: `up-build place-normal gl-escrow-state c: farm`
- 1895: `release-escrow wood`, `set-escrow-percentage wood 0`, `up-build place-point 0 c: mining-camp`

### Required Byzantine evidence

Before entering `EXECUTING`:

1. commitment is still `PROTECTED`;
2. protected resource state remains valid;
3. action-specific feasibility predicate is true;
4. required production/construction/research authority exists;
5. target or destination evidence exists where applicable;
6. no superseding emergency commitment has won arbitration;
7. execution has not already occurred;
8. the executor interface is known and valid.

The command may then be issued exactly once for the current execution attempt.

### Prohibition

Do not transition directly `PROTECTED → VERIFYING` without recording the actual command issuance.

---

# 7. T04 — EXECUTING → VERIFYING

### Shadow evidence

This transition is inferred from Shadow's downstream observer structure rather than from a single named state.

Research:

- 1182 / 1187 / 1192 / 1197 / 1202 / 1207 / 1212 / 1240 / 1245 / 1250 inspect research status and advance progression.

Construction:

- 1891 observes mining-camp count/progression.
- 1893 observes total mining-camp count and increments `gl-build-progress`.
- 1799–1800 use build feasibility, resource state, and farm counts to continue progression.

### Required Byzantine evidence

Immediately after command issuance:

1. command was recorded as issued;
2. execution attempt ID remains current;
3. expected world-state effect is defined;
4. appropriate observer is selected;
5. no completion assertion has yet been made.

This is deliberately a narrow state. It exists to prevent command-as-completion errors.

---

# 8. T05 — VERIFYING → RELEASE

### Shadow evidence

Research families demonstrate the pattern:

```text
command
  ↓
research-status observation
  ↓
progression mutation
  ↓
release / restoration
  ↓
re-entry
```

The construction family similarly uses world-state counts to reconcile progression:

- 1891: mining-camp count constrains `gl-build-progress`.
- 1893: `building-type-count-total mining-camp >= 3` → progress increment.

### Required Byzantine evidence

A successful verification requires action-specific completion evidence.

Examples:

**Research**
- `up-research-status` / equivalent status reaches the required completion state.
- The target technology is actually complete, not merely pending.

**Construction**
- `building-type-count-total` or equivalent world-state observation proves the building exists in the required state.
- Pending placement/object state is not sufficient by itself.

**Training**
- unit count or another appropriate world-state observation proves the unit exists.

**Production infrastructure**
- the required production building exists and is usable, not merely queued/pending.

Only after that evidence exists may the logical state become `RELEASE`.

---

# 9. T06 — VERIFYING → TIMEOUT

### Shadow-derived evidence

Shadow repeatedly uses progression/time guards rather than assuming that an issued command completed. The construction neighborhood also distinguishes pending placement from completed construction.

### Required Byzantine evidence

1. expected verification signal did not arrive before the action-specific deadline;
2. no alternative completion evidence exists;
3. commitment is still logically active;
4. no newer evidence invalidates the timeout assessment.

If any completion evidence arrives concurrently, `VERIFYING → RELEASE` wins over timeout.

---

# 10. T07 — VERIFYING → RECOVERY

### Shadow evidence

Recovery is generalized from Shadow's reconciliation pattern rather than copied from a single rule:

- 1891 corrects `gl-build-progress` when observed building count contradicts the cursor.
- 1892 restores `gl-current-build-item` and escrow policy.
- 1893 increments progress after world-state evidence.
- 1795–1800 use split-state re-entry when the farm requirement changes.

These are the important Shadow idioms: **observe contradiction → reconcile cursor/state → resume from a coherent point**.

### Required Byzantine evidence

Enter `RECOVERY` when:

1. execution has failed or become contradictory;
2. verification evidence conflicts with expected state;
3. protected resources no longer correspond to the active objective;
4. the target disappeared or became invalid;
5. another authority superseded the commitment;
6. the executor reports an unrecoverable failure;
7. timeout policy demands intervention.

Recovery must identify the failure class before selecting retry/substitute/cancel.

---

# 11. T08 — RELEASE → IDLE

### Shadow evidence

Shadow uses:

- `release-escrow`
- `set-escrow-percentage ... 0`
- progression pause reset
- current-item/progression changes
- subsequent re-entry rules

The exact source pattern varies by family; there is no single universal release rule.

### Required Byzantine evidence

All must be true:

1. release action was issued;
2. physical escrow is verified at the intended post-release level;
3. escrow percentages are verified/reset where applicable;
4. logical commitment is cleared;
5. execution attempt is closed;
6. no stale current-item/current-objective remains authoritative;
7. no pending placement/object is falsely treated as the old commitment's completion;
8. the next arbitration cycle may safely acquire the resources.

Only then is the commitment `RELEASED` and the machine returned to `IDLE`.

---

# 12. T09 — TIMEOUT → RECOVERY

### Required evidence

Timeout is already an explicit finding of insufficient progress. To enter recovery, additionally record:

1. timeout reason;
2. last verified progress marker;
3. resources currently protected;
4. current objective identity;
5. current executor state;
6. whether a superseding objective exists;
7. whether retry is technically feasible.

No blind retry is permitted.

---

# 13. T10 — RECOVERY → IDLE

### Required evidence

Use this exit only when the failed commitment has been fully dismantled:

1. protected resources released or deliberately transferred;
2. escrow percentages reconciled;
3. logical commitment cleared;
4. stale current-item/progression state cleared or reconciled;
5. pending execution attempt closed;
6. failure recorded;
7. no residual authority claims remain.

If any of these remain unresolved, recovery continues.

---

# 14. T11 — RECOVERY → RESERVING

This is the normal retry/substitution path.

### Required evidence

1. failure cause has been classified;
2. original objective is still strategically valid, **or** a replacement objective has been selected;
3. replacement has higher/equal authority than the failed commitment;
4. prior commitment has been released/reconciled;
5. new objective has a new attempt identity;
6. resource feasibility is recomputed from current state;
7. no stale escrow is attributed to the new attempt.

The new reservation is therefore a **new transaction**, not a continuation of a corrupted one.

---

# 15. T12 — PROTECTED → RECOVERY

This is the emergency supersession path.

### Shadow-derived basis

The shared escrow namespace and global progression writers mean that protected resources can be affected by unrelated rules. The closure explicitly identifies competing escrow writers and shared-state writers as part of the dependency closure.

### Required Byzantine evidence

1. a higher-precedence requirement exists;
2. it requires resources protected by the current commitment;
3. the new requirement is authorized;
4. the old commitment can be safely interrupted;
5. the interruption is recorded as supersession, not ordinary completion;
6. release/reconciliation will follow.

This is how Byzantine handles an emergency without allowing arbitrary rules to steal escrow.

---

# 16. T13 — EXECUTING → RECOVERY

### Required evidence

Use when the engine action itself is known to have failed or become invalid.

Required:

- command issuance recorded;
- expected execution effect absent or invalid;
- action is no longer safe to repeat blindly;
- target/placement/technology state rechecked;
- commitment remains attributable to the same attempt.

Do not reissue merely because the next rule evaluation still sees the original predicate.

---

# 17. T14 — RESERVING → RECOVERY

### Required evidence

Use when reservation configuration itself becomes contradictory:

- escrow write succeeded but objective disappeared;
- protected amount exceeds newly established emergency floor;
- strategy changed materially;
- higher authority superseded the reservation;
- reservation target became impossible;
- escrow state cannot be reconciled.

The reservation must be unwound before another commitment acquires those resources.

---

# 18. Shadow rule-to-state mapping

| Shadow evidence | Byzantine state implication | Evidence strength |
|---|---|---|
| 1172–1177 research trigger → pause → escrow → research | `IDLE → RESERVING → PROTECTED → EXECUTING` | DIRECT for source operations; COMPOSED for generalized states |
| 1179–1187 Iron Casting cursor/escrow/command/status | `PROTECTED → EXECUTING → VERIFYING → progression` | DIRECT + COMPOSED |
| 1188–1197 Forging branches | same | DIRECT + COMPOSED |
| 1198–1207 Chain Barding branches | same | DIRECT + COMPOSED |
| 1208–1212 Scale Barding | same | DIRECT + COMPOSED |
| 1236–1240 Fletching | reservation/verification pattern, legacy execution boundary | DIRECT; transplant requires qualification |
| 1241–1245 Leather Archer Armor | reservation → execution → observed progression | DIRECT + COMPOSED |
| 1246–1250 Padded Archer Armor | resource rebalancing + legacy execution | DIRECT; mixed-generation |
| 1795–1800 farm split/build path | requirement arbitration → protected construction execution → re-entry | COMPOSED |
| 1890–1896 mining-camp path | target search → placement → execution → world-state reconciliation | DIRECT + COMPOSED |
| global `gl-progression-pause` | interrupt/arbitration substrate | DIRECT |
| global `gl-current-build-item` | commitment/progression cursor | DIRECT |
| global `gl-build-progress` | ordered milestone/progress register | DIRECT |
| global `gl-escrow-state` | engine accounting-mode dependency | DIRECT |
| `release-escrow` | release operation only | DIRECT |
| research/building count observers | completion evidence | DIRECT |
| timers/turn guards | freshness/timeout substrate | DIRECT for guards; COMPOSED for generalized timeout state |

---

# 19. Evidence classes for the Byzantine implementation

## E0 — Command evidence

The engine command was issued.

Examples:

- `up-research`
- `research`
- `up-build`
- `build`
- `release-escrow`

**Never sufficient for completion.**

## E1 — Reservation evidence

The requested escrow policy is observable after configuration.

Examples:

- escrow amount/percentage changed as intended;
- resource protection remains associated with the active commitment.

## E2 — Feasibility evidence

The engine reports the action can currently proceed.

Examples:

- `can-research-with-escrow`
- `can-build-with-escrow`
- appropriate production feasibility facts.

**Not completion evidence.**

## E3 — Pending evidence

The engine reports an action/object is pending.

Examples:

- `up-pending-objects`
- `up-pending-placement`
- research pending.

**Not completion evidence.**

## E4 — World-state evidence

The intended object/state exists in the game world.

Examples:

- completed technology status;
- `building-type-count-total` change consistent with construction;
- completed unit count;
- valid target/world object state.

This is the normal minimum for `VERIFYING → RELEASE`.

## E5 — Reconciliation evidence

The world state has been reconciled with the logical cursor.

Examples:

- building count forces `gl-build-progress` correction;
- current item is restored to match observed progression;
- stale commitment is cleared.

## E6 — Release evidence

Physical escrow and logical commitment have both been reconciled.

A release command without post-release evidence remains `RELEASE_REQUESTED`.

---

# 20. Required invariants

### I1 — One active commitment

A resource may be protected by at most one authoritative commitment unless explicit partitioning is implemented.

### I2 — Every reservation has an owner

No anonymous escrow.

### I3 — Every reservation has an exit

Every `RESERVING`/`PROTECTED` path must reach release, timeout, or recovery.

### I4 — Every execution has verification

No command may permanently advance logical progression without an observer.

### I5 — Completion is world-state based

Pending and command states cannot satisfy completion predicates.

### I6 — Release is verified

The logical state cannot become `IDLE` solely because `release-escrow` was issued.

### I7 — Recovery is explicit

A superseded commitment cannot silently disappear.

### I8 — Re-entry uses reconciled state

Retry begins from current world state, not stale cached intent.

### I9 — Policy and substrate remain separate

Byzantine-specific thresholds determine **what** should be protected. Shadow-derived escrow machinery determines **how** protection, execution, verification, and release are controlled.

### I10 — No architecture-by-noun

A state exists only because an observable transition requires it. Do not create additional modules/states merely because the names sound clean.

---

# 21. What is genuinely Shadow-derived vs Byzantine-generalized

## Direct Shadow evidence

- resource reservation through escrow configuration;
- progression cursor/state;
- pause/arbitration state;
- escrow-aware feasibility gates;
- command issuance after protected state;
- downstream research/building observation;
- progression reconciliation;
- release/re-entry behavior;
- shared escrow namespace;
- timer/turn guards;
- construction search/placement/execution separation.

## Byzantine generalization

- explicit `IDLE`, `RESERVING`, `PROTECTED`, `EXECUTING`, `VERIFYING`, `RELEASE`, `TIMEOUT`, `RECOVERY` labels;
- transaction/attempt identity;
- explicit timeout state;
- explicit recovery reason taxonomy;
- explicit supersession authority;
- generalized support for research + construction + production;
- invariant that every reservation has an owner and exit.

## Not yet proven

- that Shadow itself has one universal eight-state machine;
- that every Shadow escrow family uses identical release semantics;
- that every timeout can be represented by one universal numeric threshold;
- that all escrow resources should be protected with identical Byzantine policies;
- that the full machine can be implemented with a single goal without collisions or priority loss.

These remain hypotheses until the complete rule atlas and runtime/replay evidence validate them.

---

# 22. Implementation order

Do not implement all states at once.

1. Implement commitment identity and `IDLE`/`RESERVING`.
2. Prove reservation observability.
3. Implement `PROTECTED` and competing-resource arbitration.
4. Add one execution class: research.
5. Add `VERIFYING` with hard completion evidence.
6. Add verified `RELEASE`.
7. Add timeout only after normal completion/release works.
8. Add recovery and retry.
9. Generalize the same substrate to construction.
10. Generalize to production only after the first two execution classes survive replay testing.

The first implementation target should therefore be **one complete research transaction**, preferably an analogue of Shadow's Iron Casting/Forging pattern, because those families expose cursor, escrow policy, command, status observation, and progression mutation in one connected control sequence.

Do not transplant the Viking technology predicates. Transplant the control idiom and supply Byzantine policy predicates separately.
