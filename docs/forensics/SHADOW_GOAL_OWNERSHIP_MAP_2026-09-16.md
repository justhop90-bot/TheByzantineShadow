# Shadow Goal Ownership Map — Collision & Namespace Audit

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Scope:** Shadow DC7 goal ownership, legacy compatibility IDs, and the semantic namespace of `01_constants.per`

## Audit conclusion

The prior `478 / 479` Shadow-versus-legacy collision was the **only numeric goal-ID collision found between the current legacy registry and the Shadow DC7 goal inventory**.

The second-pass constants audit finds **no duplicate symbolic definitions in `01_constants.per`**: each declared symbol has one declaration site in the current registry.

The registry does contain many **repeated numeric values across different semantic domains**. These are not automatically duplicate definitions. Shadow's source uses the same small integers independently for goal/state values, enum values, timer IDs, geometry/group selectors, and ordinary scalar constants. Treating every repeated number as a collision would destroy valid Shadow semantics.

The audit therefore distinguishes:

1. **Duplicate symbolic definition** — the same symbol declared more than once. None found.
2. **Same-domain numeric alias** — different symbols intentionally representing the same semantic value. Only retain when source evidence or an explicit compatibility requirement supports it.
3. **Cross-domain numeric reuse** — the same integer used independently by different namespaces (for example a timer ID and a goal/state value). This is Shadow-compatible and is not a goal collision.
4. **Legacy compatibility constant** — an AEGIS-era symbol retained for migration/build compatibility. It is not part of Shadow's behavioral authority.
5. **Unproven residue** — a symbolic value whose meaning is not established strongly enough to promote or rename safely. Preserve it; do not silently normalize it.

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

The current project extensions are outside that source-used set.

| ID / range | Current owner | Status | Notes |
|---:|---|---|---|
| `1-317` | Shadow source | **SOURCE-OWNED** | Explicitly included in Shadow source inventory |
| `318-391` | None established by Shadow source inventory | **UNASSIGNED** | Do not allocate without registry audit |
| `392` | Shadow source | **SOURCE-OWNED** | `gl-attacking` |
| `393-449` | None established by Shadow source inventory | **UNASSIGNED** | Do not allocate without registry audit |
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

The legacy AEGIS declarations remain numerically separated from Shadow's source-owned `478/479` pair. The relocation is:

```text
478 -> home-x
479 -> home-y
520 -> AEGIS-TRANSACTION-STONE
521 -> AEGIS-TRANSACTION-ACTIVE
```

The legacy symbols remain **migration-only**. Their presence in the constants registry does not grant them Shadow behavioral authority.

## Constants namespace audit

### A. Duplicate symbolic definitions

**Result: none found.**

No symbol is declared twice in the current `01_constants.per` registry. There is therefore no parser-safe duplicate-definition deletion to perform.

### B. Source-preserved same-value aliases / identity symbols

The registry contains source-preserved symbols sharing values. The most important examples are:

```text
gl-identity = 420
Promi       = 420
```

and:

```text
Doomsday       = 42
gl-target-type = 42
```

These are **not promoted as new goal IDs** merely because their numeric values resemble other registry entries. Their semantic interpretation must remain tied to the Shadow source usage site. They are therefore classified as **SOURCE-PRESERVED / SEMANTICALLY UNRESOLVED**, not as executable collisions.

This is deliberately conservative: without a source-usage proof that two symbols occupy the same engine namespace and are intended to be interchangeable, renaming or deduplicating them would be an unsafe behavioral change.

### C. Cross-domain numeric reuse

The registry repeatedly reuses small integers across distinct namespaces. Examples include:

```text
ATTACKING / FLANK / COMBINED / LumberFirst / MarchingOne / RangedGroup = 1
POCKET / VATTACKING / SEPARATE / ONE-MINUTE / KnightGroup = 2
RaidGroup / MarchingThree / t-raid-retreat / gl-tower-control = 3
Doomsday / gl-target-type / villager-timer = 42
Unknown / nearest-tc-y = 69
```

These are **cross-domain numeric reuses**, not duplicate symbolic definitions and not Shadow-versus-legacy goal collisions. The same integer is legal when consumed by separate engine namespaces or when representing independent enumerated values.

Accordingly, no numeric renumbering was performed.

### D. Compatibility aliases

No new compatibility alias was introduced by this audit.

The only deliberate migration remap remains:

```text
AEGIS-TRANSACTION-STONE   478 -> 520
AEGIS-TRANSACTION-ACTIVE  479 -> 521
```

The symbolic names were preserved to avoid unnecessary downstream edits, while the numeric IDs were moved out of Shadow-owned goal space.

### E. Accidental residue / unproven semantics

The registry contains historical/experimental names and values whose semantics are not independently established by the current project architecture. They are retained because the supplied Shadow source is the authoritative behavioral reference and because deleting or renaming them without a usage audit could break parser-visible or runtime-visible references.

These entries are therefore classified as **PRESERVE / DO NOT PROMOTE**, rather than silently cleaned up.

## Authority rule

`01_constants.per` is the declaration point for the current project registry.

Priority is:

1. Shadow source evidence.
2. Explicitly verified Shadow project extensions.
3. Migration-only compatibility declarations.
4. Unproven historical residue.

A repeated integer does not override this hierarchy. A symbol becomes a Shadow goal only when its engine namespace and source usage establish that fact.

`478` and `479` remain permanently reserved to `home-x` and `home-y` unless a future source-level audit proves otherwise.

## Parser-safety decision

**No executable `.per` fix was required by this audit.**

The existing `478/479 -> 520/521` change remains the minimal parser-safe executable correction. This pass changes only the forensic ownership map and does not alter `01_constants.per`.

This is intentional: eliminating source-preserved aliases or repeated cross-domain values without proving their runtime namespace would be a semantic rewrite, not a parser-safe cleanup.

## Verification requirements

1. `home-x` resolves to `478`.
2. `home-y` resolves to `479`.
3. No legacy symbol resolves to `478` or `479`.
4. `AEGIS-TRANSACTION-STONE` resolves to `520`.
5. `AEGIS-TRANSACTION-ACTIVE` resolves to `521`.
6. No symbol is declared twice in `01_constants.per`.
7. Repeated numeric values are classified by semantic namespace before any renumbering.
8. Source-preserved aliases are not renamed or deleted without usage-site evidence.
9. New project goal IDs are checked against the Shadow source inventory before allocation.
10. Legacy AEGIS symbols remain migration-only and are not silently promoted into the Shadow implementation.

## Scope boundary

This audit covers the current constants registry's declaration uniqueness, repeated-value patterns, Shadow-vs-legacy goal ownership, and parser-safe remediation.

It does **not** claim that every historical Shadow constant has a fully reconstructed runtime type. A future semantic-typing pass should trace each nontrivial constant to its consumption sites and classify its engine namespace explicitly before any cleanup or consolidation.

## Evidence

- Shadow DC7 / `SourceShaRef`: used goal inventory `1-317, 392, 478-479`; direct declarations `home-x 478` and `home-y 479`.
- Current `01_constants.per`: centralized registry, source-preserved Shadow constants, legacy compatibility declarations, and relocated `520/521` IDs.

## Commit history

- Collision fix: `4a779db9866fb9aca0c6710a9b90e5edd6928d90`
- Prior ownership map: `f356b02a524a18086337776c328e6c95a1e1ece0`
- Numeric collision audit update: `eb01f7fb949e2ce66c4842af03533ca7c73bb52c`
- This semantic namespace audit: pending
