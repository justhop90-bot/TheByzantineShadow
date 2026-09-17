# Shadow Construction Forensic Closure — 2026-09-17

## Status

**FORENSICALLY CLOSED — STATICALLY QUALIFIED**

Runtime qualification remains pending. This status means the authenticated donor interval has been independently compared against the current `ShadowByzantine/04_construction.per`, its source-order and jump topology have been qualified, compatibility constants have been audited, and the qualification was executed against the current `main` checkout. It does not assert AoE2DE runtime completion or behavioral equivalence in a live match.

## Repository provenance

Repository: `justhop90-bot/TheByzantineShadow`
Branch: `main`
Verified qualification checkout: `15e55df863fbebf3f4bad68256f6ba0453f8a2a5`

Canonical donor: `ShadowSource.per`
Authenticated Git blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`
Authenticated donor rule count: `1,956`

The qualification workflow explicitly checked the Git blob identity before extracting donor rules. The current `main` checkout was used by the rerun, rather than relying on the historical workflow head commit.

## Authenticated construction interval

Implementation interval: **1794–1949**, exactly 156 rules.

Authoritative R07 boundary: **1794–1896**.

Post-R07 authenticated continuation: **1897–1949**.

Therefore the implementation must not be described as an R07 implementation for the entire 1794–1949 interval. Rules 1897–1949 are authenticated donor continuation beyond the R07 boundary. The interval remains one contiguous authenticated transplant slice for qualification purposes.

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

## Remaining runtime work

The static construction slice is closed. The next qualification tier is runtime/replay evidence. That work must establish actual engine acceptance, pending-object behavior, world-state completion, progression advancement, escrow release/reallocation, placement/search behavior, interruption/re-entry, and recovery under live AoE2DE execution. Those facts are intentionally not promoted from static evidence in this closure artifact.
