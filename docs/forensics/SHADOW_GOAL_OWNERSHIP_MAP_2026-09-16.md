# Shadow Goal Ownership Map — Collision Audit

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Scope:** Shadow DC7 goal IDs versus legacy goal namespace

## Audit conclusion

The `478 / 479` collision previously identified was the **only remaining Shadow-versus-legacy numeric goal-ID collision found in the current registry**.

Shadow DC7 / `SourceShaRef` explicitly inventories its used goals as:

```text
GOALS: 1-317, 392, 478-479
```

and directly declares:

```text
home-x = 478
home-y = 479
```

The current legacy registry occupies `450-496`, with the two former collision slots vacated and relocated to `520-521`. Comparing that complete legacy range with the Shadow source inventory produces no additional overlap.

## Ownership table

| ID / range | Current owner | Status | Notes |
|---:|---|---|---|
| `1-317` | Shadow source | **SOURCE-OWNED** | Explicitly included in Shadow source inventory |
| `318-391` | None established by Shadow source inventory | **UNASSIGNED** | Not source-owned; requires separate allocation audit before use |
| `392` | Shadow source | **SOURCE-OWNED** | `gl-attacking` |
| `393-449` | None established by Shadow source inventory | **UNASSIGNED** | Not source-owned; requires allocation audit before use |
| `450-477` | Legacy migration namespace | **NON-COLLIDING / MIGRATION-ONLY** | Outside Shadow source-used IDs |
| `478` | Shadow source | **SOURCE-OWNED / RESERVED** | `home-x` |
| `479` | Shadow source | **SOURCE-OWNED / RESERVED** | `home-y` |
| `480-496` | Legacy migration namespace | **NON-COLLIDING / MIGRATION-ONLY** | Outside Shadow source-used IDs |
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

Current legacy IDs in `01_constants.per` are:

```text
450 AEGIS-OBJECTIVE
451 AEGIS-REQUIREMENT
452 AEGIS-TRANSACTION
453 AEGIS-AUTHORITY
454 AEGIS-VERIFICATION
455 AEGIS-ESCROW-STATE
456 AEGIS-FEUDAL-STATE
457 AEGIS-BARRACKS-STATE
458 AEGIS-SPEARMAN-STATE
459 AEGIS-GROSS-FOOD
460 AEGIS-GROSS-WOOD
461 AEGIS-GROSS-GOLD
462 AEGIS-GROSS-STONE
463 AEGIS-COMMITTED-FOOD
464 AEGIS-COMMITTED-WOOD
465 AEGIS-COMMITTED-GOLD
466 AEGIS-COMMITTED-STONE
467 AEGIS-LIQUID-FOOD
468 AEGIS-LIQUID-WOOD
469 AEGIS-LIQUID-GOLD
470 AEGIS-LIQUID-STONE
471 AEGIS-RESERVE-FOOD
472 AEGIS-RESERVE-WOOD
473 AEGIS-RESERVE-GOLD
474 AEGIS-RESERVE-STONE
475 AEGIS-TRANSACTION-FOOD
476 AEGIS-TRANSACTION-WOOD
477 AEGIS-TRANSACTION-GOLD
478 [VACATED]
479 [VACATED]
480 AEGIS-TRANSACTION-ID
481 AEGIS-DISCRETIONARY-FOOD
482 AEGIS-DISCRETIONARY-WOOD
483 AEGIS-DISCRETIONARY-GOLD
484 AEGIS-DISCRETIONARY-STONE
485 AEGIS-RESERVE-POLICY
486 AEGIS-DEMAND-FOOD
487 AEGIS-DEMAND-WOOD
488 AEGIS-DEMAND-STONE
489 AEGIS-DEMAND-GOLD
490 AEGIS-CAPITAL-FEASIBILITY
491 AEGIS-DEMAND-ACTIVE
492 AEGIS-ESCROW-STATUS
493 AEGIS-ESCROW-RELEASE-REQUEST
494 AEGIS-EXECUTION-STATE
495 AEGIS-EXECUTION-BASELINE
496 AEGIS-RECOVERY-STATE
520 AEGIS-TRANSACTION-STONE
521 AEGIS-TRANSACTION-ACTIVE
```

Thus the former conflict is resolved as:

```text
478 -> home-x
479 -> home-y
520 -> AEGIS-TRANSACTION-STONE
521 -> AEGIS-TRANSACTION-ACTIVE
```

## Authority rule

`01_constants.per` is the declaration point for the current project registry. Shadow source IDs take precedence over legacy compatibility IDs.

`478` and `479` are permanently reserved to `home-x` and `home-y` unless a future source-level audit proves otherwise. No migration or new subsystem may silently reuse them.

The project extension IDs `497`, `500-503`, `507`, and `508` are outside the Shadow DC7 source-used set and are therefore not Shadow-versus-legacy collisions. They remain project-owned and must continue to be tracked centrally.

## Parser-safety decision

**No additional executable `.per` fix is required by this audit.**

The existing fix in `01_constants.per` is parser-minimal: only the two legacy numeric assignments were moved from `478/479` to `520/521`; symbolic names were preserved. The current audit found no second Shadow-versus-legacy overlap requiring another code edit.

This commit therefore updates the forensic ownership map only and does not alter executable behavior.

## Verification requirements

1. `home-x` resolves to `478`.
2. `home-y` resolves to `479`.
3. No legacy symbol resolves to `478` or `479`.
4. `AEGIS-TRANSACTION-STONE` resolves to `520`.
5. `AEGIS-TRANSACTION-ACTIVE` resolves to `521`.
6. No second declaration claims `478` or `479`.
7. New project IDs are checked against the Shadow source inventory before allocation.
8. Legacy AEGIS symbols remain migration-only and are not silently promoted into the Shadow implementation.

## Scope boundary

This audit concerns **Shadow-versus-legacy numeric goal ownership**. It does not classify repeated numeric values among Shadow's own symbolic constants as legacy collisions. Those aliases may warrant a separate semantic namespace audit, particularly where goal IDs, timer IDs, and ordinary symbolic values coexist.

## Evidence

- Shadow DC7 / `SourceShaRef`: used goal inventory `1-317, 392, 478-479`; direct declarations `home-x 478` and `home-y 479`.
- Current `01_constants.per`: complete legacy declarations and relocated `520/521` compatibility IDs.

## Commit history

- Collision fix: `4a779db9866fb9aca0c6710a9b90e5edd6928d90`
- Prior ownership map: `f356b02a524a18086337776c328e6c95a1e1ece0`
