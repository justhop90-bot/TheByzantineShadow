# Shadow Construction Forensic Closure — 2026-09-17

## Status

**FORENSICALLY CLOSED — STATICALLY QUALIFIED**

Runtime qualification remains pending. This status means the authenticated donor interval has been independently compared against the current `ShadowByzantine/04_construction.per`, its source-order and jump topology have been qualified, compatibility constants have been audited, and the qualification was executed against the current `main` checkout. It does not assert AoE2DE runtime completion or behavioral equivalence in a live match.

## Repository provenance

Repository: `justhop90-bot/TheByzantineShadow`
Branch: `main`
Verified qualification checkout: `15e55df863fbebf3f4bad68256f6ba0453f8a2a5`

Canonical donor: `ShadowSource.per`
Authenticated Git blob SHA-1 (raw bytes, CRLF): `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`
Normalized SHA-1 (LF, as computed by `tools/forensics/module_qualification.py`
over UTF-8 text): `99a8f5de08bf31f84f418fea188ab08ab6180a67`
Both forms denote identical content; the pipeline checks the normalized form.
Authenticated donor rule count: `1,956`

The qualification workflow explicitly checked the Git blob identity before extracting donor rules. The current `main` checkout was used by the rerun, rather than relying on the historical workflow head commit.

## Authenticated construction interval

Implementation interval: **1794–1956**, exactly 163 rules
(extended 2026-09-17 from 1794–1949 by the donor timer/turn tail,
rules 1950–1956; re-qualified, see Amendment record below).

Authoritative R07 boundary: **1794–1896**.

Post-R07 authenticated continuation: **1897–1956**.

Therefore the implementation must not be described as an R07 implementation for the entire interval. Rules 1897–1956 are authenticated donor continuation beyond the R07 boundary. The interval remains one contiguous authenticated transplant slice for qualification purposes.

The source-boundary structure already recorded in `04_construction.per` is:

- 1794–1805: R07 farm progression
- 1806–1823: R07 QHOUSE construction/control
- 1824–1858: R07 QLC and construction/progression continuation
- 1859–1896: R07 placement/search/construction continuation
- 1897–1949: authenticated donor continuation beyond R07

## Exact qualification result

The authenticated qualification rerun against current `main` produced:

- `AUTHENTICATED_DONOR_SHA=70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`
- `DONOR_RULE_COUNT=1956`
- `DONOR_INTERVAL=1794-1949`
- `R07_BOUNDARY=1794-1896`
- `POST_R07_INTERVAL=1897-1949`
- `IMPLEMENTATION_RULE_COUNT=156`
- `RULE_IDENTITY=PASS`
- `RULE_BODY_EQUIVALENCE=PASS`
- `PREDICATE_EQUIVALENCE=PASS`
- `ACTION_EQUIVALENCE=PASS`
- `DISABLE_SELF_EQUIVALENCE=PASS`
- `UP_JUMP_EQUIVALENCE=PASS`
- `SOURCE_ORDER=PASS`
- `NO_MISSING_RULES=PASS`
- `NO_UNEXPECTED_RULES=PASS`
- `DUPLICATE_RULE_IDS=NONE`
- `PARSER_BALANCE=PASS`
- `STATIC_DONOR_EQUIVALENCE=PASS`
- `RUNTIME_SEMANTICS=NOT_PROVEN`
- `RUNTIME_QUALIFICATION=PENDING`

The exact explicit jump topology is:

- `1795 -> 1796` (`+1`)
- `1850 -> 1854` (`+4`)
- `1891 -> 1896` (`+5`)

There are exactly 3 explicit jump edges in the authenticated interval. The interval has 155 normal internal fall-through edges, with cross-boundary source-order fall-through `1793 -> 1794` and `1949 -> 1950`. No explicit jump crosses either interval boundary.

## 1806–1814

Rules 1806–1814 are present at their actual donor identities and are included in the exact 1794–1949 qualification. The authenticated transplant ledger classifies all nine rules as `DIRECT_DONOR_TEXT` with `DIRECT_DONOR_SOURCE_ORDER` and `runtime_qualification=PENDING`.

This closes the former implementation gap. They are not reconstructed approximations or inferred QHOUSE rules.

## State/dataflow parity

The strengthened qualifier independently counted donor/implementation touches for the principal persistent state symbols. All counts matched:

| State symbol | Donor | Implementation |
|---|---:|---:|
| `gl-current-build-item` | 65 | 65 |
| `gl-build-progress` | 54 | 54 |
| `gl-progression-pause` | 15 | 15 |
| `gl-escrow-state` | 12 | 12 |
| `SPLIT` | 13 | 13 |
| `gl-strategy` | 62 | 62 |
| `gl-target-age` | 21 | 21 |
| `gl-target-age-checking` | 10 | 10 |
| `gl-target-score1` | 10 | 10 |
| `gl-target-score2` | 3 | 3 |

These are mechanically derived static touch counts, not runtime proofs of semantic state ownership.

## Compatibility constants

The construction compatibility constants were independently compared with the authenticated donor. Every audited value matched donor text exactly:

- `with-escrow = 0`
- `without-escrow = 1`
- `place-control = 2`
- `place-point = 3`
- `MILL = 225`
- `ESKIRMS = 19`
- `FletchingNumber = 9`
- `goal = 165`
- `gl-enemy-strategy = 170`
- `gl-town-safe = 300`
- `DRUSH = -1`
- `SIEGE = 184`

The qualification classified each as `DIRECT_DONOR_TEXT`. None of these symbols is defined in `01_constants.per`; their definitions remain local to the authenticated construction transplant, matching the current compatibility-layer design.

`01_constants.per` contains a separate central registry of authenticated Shadow identifiers, including direct donor identities such as `gl-current-build-item=121`, `SPLIT=134`, `gl-build-progress=186`, `gl-escrow-state=205`, `gl-progression-pause=272`, and `gl-strategy=273`. The registry explicitly states that registration alone is not a runtime-transplant claim.

Repository-wide duplicate `defconst` names reported by the qualifier are confined to paired example/input artifacts under `aoe2-ai-fmt-master/examples.doc`; none of the audited construction compatibility constants is duplicated there.

## Tooling correction

Three obsolete workflows that mislabeled post-R07 slices as R07 were removed:

- `.github/workflows/qualify-r07-1794-1814.yml`
- `.github/workflows/qualify-r07-1900-1924.yml`
- `.github/workflows/qualify-r07-1925-1949.yml`

The corresponding superseded post-R07 qualifier scripts for 1900–1924 and 1925–1949 were also removed. The repository now uses the authenticated contiguous construction qualifier for 1794–1949, with the independently retained 1815–1849 slice qualifier as a secondary check.

The general qualifier was strengthened to compare rule predicates, actions, `disable-self`, explicit jump topology, source order, state-touch parity, and compatibility constants rather than merely relying on a whole-rule normalized comparison.

## Evidence classification

Direct donor text: authenticated from `ShadowSource.per` and matched mechanically against the implementation.

Mechanically derived: source-order edges, jump destinations, interval boundaries, rule counts, state-touch counts, duplicate-definition inventory.

Documentation classification: R07 ends at 1896; 1897–1949 is donor continuation.

Runtime status: **UNKNOWN / NOT PROVEN**.

No claim is made that command issuance equals construction completion, that pending-object predicates prove completion, or that static donor equivalence establishes live AoE2DE behavioral equivalence.

## Amendment record 2026-09-17 — Tranche A (machine resuscitation)

Static re-qualification after implementation changes (both pipelines green,
see tool outputs retained in CI artifacts):

- `04_construction.per`: appended authenticated donor rules 1950–1956
  (QSPECIAL_TIMERS tail: 30SEC/ONE-MINUTE/THREE-MINUTE/TWO-MINUTE/
  five-seconds-timer re-arms + both turn counters). 163/163 positional
  body/predicate/action/disable-self equivalence; jump topology unchanged
  (3 edges, none cross-boundary); state-touch parity holds. Interval
  tooling updated (`LAST=1956`, config `donor_end=1956`).
- New `ShadowByzantine/03b_strategy_bootstrap.per`: authenticated donor
  rules 1416–1420 (QSTRATEGY: FLUSH default, FFA/taunt/pocket KRUSH
  overrides, preprocessor guard preserved). Loaded before
  `04_construction.per`, preserving donor relative order. Supplies the
  previously unwritten `gl-strategy` family writers.
- `01a_shadow_r07_compat.per`: donor-exact timer/turn/strategy/
  progression/target-tracking constants with donor line citations. No new
  project state; duplicate-with-04 `gl-enemy-strategy=170` noted as the
  same binding (load-order necessity, not a competing writer).
- `02_state.per`: removed two rules writing undefined, unconsumed
  `BASIC-*` goals (no defconst, no reader anywhere in the repository).
- `03_economy.per`: BYZANTINE-GENERALIZATION — villager cap 30 (above
  donor Dark thresholds 23/29) and Feudal gold-share rule (Castle-age
  progression content otherwise unreachable at 0% gold). Revisit with the
  Castle economy transplant.
- `05_production.per`: removed a stray markdown fence line (parser poison,
  module unloaded but fixed for safety).

Pre-commit veto record (donor-topology preservation): timer tail and
strategy bootstrap have DIRECT donor analogues (rules 1950–1956,
1416–1420); no new authority/dispatcher; no state/jump/escrow/search/
progression topology changes; order preserved. ACCEPT. Hygiene items
touch no donor topology. ACCEPT.

Previously dead rules now live in the loaded graph: turn-gated rules
(173, 327, 479, 1079, 1142, 1176, 1312, 1329), 30SEC consumer (1869),
strategy-gated farm/house/LC/mining rules (gl-strategy now written),
pause-gated mid-game rules resolve naturally once tech pauses cycle.
`gl-progression-pause` boot state verified unnecessary (earliest donor
writers are tech-pause regions; early interval rules do not gate on -1).

Still unwritten in the loaded graph (next tranches, not this one):
`gl-dark-build`, `rt`, `gl-allow-mill`,
`gl-position` (except pocket), QEAGOL score machinery. No new
centralized recovery/orchestration was introduced; modules 05–15 remain
unloaded scaffolding with documented defects, untouched by this tranche.

## Amendment record 2026-09-17 — tech/production slice + QEAGOL finding

- New `ShadowByzantine/03a_donor_tech_production.per`: authenticated
  donor rules 1165–1298 (134/134 positional body equivalence;
  jump topology all in-slice; state-touch parity PASS). Contents:
  R05/R06 tech-escrow pause/fire machine, Feudal (1226) and Castle
  (1229) age-ups, and the unit-production block (monks/siege/scouts/
  knights/archers/spearmen/villagers, 1259–1298 + 1708–1710 refs).
  Loaded before `03b_strategy_bootstrap`, preserving donor relative
  order. Pipeline config carries the donor mapping; 27 modules, 0 failed.
- `01a` gained 5 tech-slice input identifiers (donor-exact values).
  `gl-age-loading`/`gl-need-vills` are written in-slice; `gl-enemy-civ`
  (writers 1503–1505) and `gl-skirm-total` (writer 1501) are dormant
  inputs pending the scouting tranche; `gl-army-damage-potential` has
  no writer anywhere in the donor (legacy input, inert by donor design).
- QEAGOL finding: `gl-target-age-checking` is READ throughout the
  QEAGOL tracker but never WRITTEN by any donor rule — the age tracker
  is dormant donor code (with several `(false)`-gated siblings), not a
  transplant gap. Deliberately NOT activated: wiring it would invent
  behavior. Revisit only as an explicit BYZANTINE improvement with its
  own baseline.
- Byzantine note: every technology and unit in 1165–1298 exists in the
  shipped Byzantine tree (verified against BYZANTINES tech data);
  Bloodlines/Blast Furnace do not appear in this slice. Zero
  substitutions required.
- Identifier audit 2026-09-17 (prompted by invalid line 27,
  `EskirmsNumber`): full mechanical sweep of every identifier read by
  the slice found 38 donor-valued symbols without a repository
  defconst; all registered donor-exact in `01a` (EskirmsNumber 20 plus
  pause/tech/build-item/Number/age/tracker/timer identifiers with
  donor line citations). Remaining unregistered tokens are engine
  builtins (unit/building/resource IDs, engine facts/commands,
  mathOps) needing none. Pipeline gap recorded: the module
  qualifier's unresolved-symbol check covers only `gl-*`/SPLIT, so
  non-goal identifiers require this manual sweep per transplanted
  slice; added to the tranche procedure going forward.

## Amendment record 2026-09-17 — automation collision (append-duplicate)

CI workflow `apply-r07-1875-1899` (bot commit `4bf2b55`) appended 25
duplicate rules (donor 1875–1899 bodies already present in the
authenticated interval) to `04_construction.per` (188 rules), because its
idempotency guard only compared the file tail while Tranche A had
legitimately extended the file past the slice. Duplicates double-fire
side effects and break interval qualification. Resolved: removed the 692
appended lines (file restored to 163 positional rules ending with donor
1956); hardened `tools/forensics/append_r07_1875_1899.py` to refuse when
the slice occurs as a contiguous subsequence anywhere in the target
(verified: now reports SLICE_ALREADY_PRESENT=YES, no diff). Both
qualifiers re-run green after the repair. Lesson recorded: applier
guard-clauses must be containment checks, not tail checks, whenever the
target file has more than one legitimate writer.

## Remaining runtime work

The static construction slice is closed. The next qualification tier is runtime/replay evidence. That work must establish actual engine acceptance, pending-object behavior, world-state completion, progression advancement, escrow release/reallocation, placement/search behavior, interruption/re-entry, and recovery under live AoE2DE execution. Those facts are intentionally not promoted from static evidence in this closure artifact.
