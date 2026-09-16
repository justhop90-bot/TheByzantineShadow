# Shadow Goal Ownership Map — Collision & Namespace Audit

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Scope:** Shadow DC7 goal ownership, legacy compatibility IDs, and the semantic namespace of `01_constants.per`

## Audit conclusion

The prior `478 / 479` Shadow-versus-legacy collision was the **only numeric goal-ID collision found between the current legacy registry and the Shadow DC7 goal inventory**.

The constants declaration audit finds **no duplicate symbolic definitions in `01_constants.per`**: each declared symbol has one declaration site in the current registry.

The semantic-typing pass further establishes that repeated numeric values must not be treated as collisions without consumption-site evidence. Shadow reuses compact integers across goals/state slots, timers, enumerations, group selectors, geometry, and scalar values.

## Shadow goal ownership

Shadow DC7 / `SourceShaRef` explicitly inventories its used goals as:

```text
GOALS: 1-317, 392, 478-479
```

and directly declares:

```text
home-x = 478
home-y = 479
```

| ID / range | Current owner | Status | Notes |
|---:|---|---|---|
| `1-317` | Shadow source | **SOURCE-OWNED** | Explicitly included in Shadow source inventory |
| `318-391` | None established | **UNASSIGNED** | Do not allocate without registry audit |
| `392` | Shadow source | **SOURCE-OWNED** | `gl-attacking` |
| `393-449` | None established | **UNASSIGNED** | Do not allocate without registry audit |
| `450-477` | Legacy migration namespace | **MIGRATION-ONLY** | Outside Shadow source-used IDs |
| `478` | Shadow source | **SOURCE-OWNED / RESERVED** | `home-x` |
| `479` | Shadow source | **SOURCE-OWNED / RESERVED** | `home-y` |
| `480-496` | Legacy migration namespace | **MIGRATION-ONLY** | Outside Shadow source-used IDs |
| `497` | Shadow project extension | **SHADOW-EXTENSION** | `SHADOW-PROD-DEMAND-SPEAR` |
| `498-499` | None assigned | **UNASSIGNED** | Available only after registry audit |
| `500-503` | Shadow project extension | **SHADOW-EXTENSION** | Production cost vector |
| `504-506` | None assigned | **UNASSIGNED** | Available only after registry audit |
| `507` | Shadow project extension | **SHADOW-EXTENSION** | Production state |
| `508` | Shadow project extension | **SHADOW-EXTENSION** | Production escrow state |
| `509-519` | None assigned | **UNASSIGNED** | Available only after registry audit |
| `520` | Legacy migration namespace | **MIGRATION-OWNED** | `AEGIS-TRANSACTION-STONE`, relocated from 478 |
| `521` | Legacy migration namespace | **MIGRATION-OWNED** | `AEGIS-TRANSACTION-ACTIVE`, relocated from 479 |

## Legacy declaration audit

The deliberate relocation remains:

```text
478 -> home-x
479 -> home-y
520 -> AEGIS-TRANSACTION-STONE
521 -> AEGIS-TRANSACTION-ACTIVE
```

The legacy AEGIS symbols remain migration-only. Their presence does not grant them Shadow behavioral authority.

## Constants namespace audit

### Duplicate symbolic definitions

**Result: none found.**

No symbol is declared twice in the current `01_constants.per` registry. No duplicate-definition deletion is justified.

### Semantic typing of repeated values

| Example | Value | Classification | Action |
|---|---:|---|---|
| `home-x` | 478 | Shadow goal/state | Preserve; permanently reserved |
| `home-y` | 479 | Shadow goal/state | Preserve; permanently reserved |
| `gl-identity` / `Promi` | 420 | Source-preserved same-value pair | Do not consolidate without usage proof |
| `Doomsday` / `gl-target-type` | 42 | Source symbol + goal/state symbol | Do not merge by numeric equality |
| `villager-timer` | 42 | Timer | Independent timer namespace |
| `ATTACKING` / `FLANK` / `COMBINED` | 1 | Independent enum/state values | Preserve |
| `POCKET` / `VATTACKING` / `SEPARATE` | 2 | Independent enum/state values | Preserve |
| `LumberFirst` / `MarchingOne` / `RangedGroup` | 1 | Policy/movement/group values | Preserve |
| `ONE-MINUTE` / `KnightGroup` | 2 | Time/group values | Preserve |

These are **cross-domain numeric reuses unless consumption-site evidence proves aliasing**.

### Alias rule

A pair may be promoted to `CANONICAL-ALIAS` only when:

1. Shadow source explicitly uses both symbols interchangeably for the same engine slot; or
2. current executable rules consume both names as equivalent representations of one state; or
3. an explicit compatibility requirement requires the old symbol to resolve to the canonical value.

Otherwise classify it as `INTENTIONAL-CROSS-DOMAIN-REUSE`, `SOURCE-PRESERVED`, or `UNPROVEN-RESIDUE`.

### Accidental residue

Historical/experimental symbols remain **PRESERVE / DO NOT PROMOTE** until their consumption sites are reconstructed. Deletion or renumbering without that evidence is not parser-safe in the engineering sense because it can change runtime semantics even when parsing succeeds.

## Parser-safe decision

**No executable `.per` fix is required by the semantic namespace audit.**

`01_constants.per` remains unchanged by this pass. The only executable collision remediation remains the earlier `478/479 -> 520/521` migration relocation.

No new aliases, goal IDs, or renumberings were introduced.

## Consumption-site typing — next required level

For unresolved symbols, classify every read/write by actual engine interface:

- `set-goal`, `up-get-goal`, `up-compare-goal` → goal/state namespace
- timer access → timer namespace
- strategic-number access → strategic-number namespace
- object/group/geometry access → corresponding engine namespace
- literal-only comparisons → scalar/enum value

Only after this trace may a repeated-value pair be declared a canonical alias or accidental duplicate residue.

## Verification requirements

1. `home-x` resolves to `478`.
2. `home-y` resolves to `479`.
3. No legacy symbol resolves to `478` or `479`.
4. `AEGIS-TRANSACTION-STONE` resolves to `520`.
5. `AEGIS-TRANSACTION-ACTIVE` resolves to `521`.
6. No symbol is declared twice in `01_constants.per`.
7. Repeated numeric values are classified by semantic namespace before renumbering.
8. Source-preserved same-value pairs are not renamed or deleted without consumption-site evidence.
9. New project goal IDs are checked against the Shadow source inventory before allocation.
10. Legacy AEGIS symbols remain migration-only.
11. Any future canonical alias has an explicit usage-site proof.

## Evidence

- Shadow DC7 / `SourceShaRef`: goal inventory `1-317, 392, 478-479`; direct `home-x 478` and `home-y 479` declarations.
- Current `01_constants.per`: centralized registry and compatibility declarations.
- `SHADOW_CONSTANT_SEMANTIC_TYPING_2026-09-16.md`: detailed repeated-value and alias classification.

## Commit history

- Collision fix: `4a779db9866fb9aca0c6710a9b90e5edd6928d90`
- Prior ownership map: `f356b02a524a18086337776c328e6c95a1e1ece0`
- Numeric collision audit: `eb01f7fb949e2ce66c4842af03533ca7c73bb52c`
- Semantic namespace audit: `68c50797aa9909c931f099141a49db1a3a12d6cc`
- Semantic typing artifact: `eb84a5c71ef50b9ec398ca6929ab86590bf1d813`

## State-closure extension — 2026-09-16

The state graph is now materially closed at the donor-source level and cross-referenced to the active ShadowByzantine slice. The detailed closure is recorded in `docs/forensics/SHADOW_STATE_CLOSURE_v0.1.md` and the executable rule mapping in `docs/forensics/SHADOW_RULE_TRANSPLANTATION_MAP_v0.1.md`.

### Additional closure findings

- Donor persistent state is distributed across goals, strategic numbers, timers, engine search state, escrow state, progression state, and rule-position state.
- Donor goals remain exactly `1-317, 392, 478-479`; no current ShadowByzantine extension may claim one of those slots without explicit source-usage proof.
- Donor timers are `1-42, 46`; timers participate in effective reachability and therefore are part of the control topology.
- Directly recovered strategic-number carriers include `sn-focus-player-number`, `sn-total-number-explorers`, `sn-number-explore-groups`, `sn-placement-zone-size`, `sn-home-exploration-time`, `sn-special-attack-type2`, and `sn-special-attack-influence2`.
- `gl-current-build-item`, `gl-build-progress`, `gl-progression-pause`, `gl-escrow-state`, `SPLIT`, and world-state observers form a coupled progression/escrow machine rather than independent variables.
- The active ShadowByzantine Pass-1 state vector (`AEGIS-*`) is newly invented state. It is a useful proof slice but is not donor-canonical and must not be promoted to the recovered Shadow architecture.
- `01b_byz_constants.per` adds a second large state namespace (`BYZ-*`) for construction, escrow, placement, verification, recovery, authority, execution, and capital. These are also project extensions, not donor state. They should be removed or reduced when the donor machine is actually transplanted rather than allowed to become a parallel controller state system.

### Current transplantation status

The exact donor construction anchors 1764–1776 and 1794–1801 and the research/progression anchors 1172–1197 are now bound to source offsets. The current ShadowByzantine implementation does not preserve those topologies: jumps, progression cursor state, placement control, distributed escrow, and progress mutation are missing or replaced.

The remaining exact QUNITS production ordinals for the Byzantine Spearman path must be mechanically bound before implementation. They are intentionally marked `UNKNOWN` in the transplantation map rather than fabricated.
