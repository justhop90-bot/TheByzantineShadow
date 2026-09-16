# Shadow Goal Ownership Map — 478 / 479 Collision Resolution

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Scope:** Shadow DC7 goal IDs 478–479 versus legacy transaction namespace

## Finding

Shadow DC7 explicitly declares and uses:

```text
home-x = 478
home-y = 479
```

The source's own inventory states that goals `478-479` are used. These IDs are therefore source-owned Shadow state and cannot simultaneously be assigned to the legacy transaction subsystem.

The former registry incorrectly assigned:

```text
AEGIS-TRANSACTION-STONE   = 478
AEGIS-TRANSACTION-ACTIVE  = 479
```

That created a semantic collision: the same engine-global goal ID could be interpreted as either Shadow spatial state or legacy transaction state.

## Resolved ownership

| Goal ID | Symbol | Owner | Status | Reason |
|---:|---|---|---|---|
| 478 | `home-x` | Shadow source | **SOURCE-OWNED** | Directly evidenced by Shadow DC7; spatial home-coordinate state |
| 479 | `home-y` | Shadow source | **SOURCE-OWNED** | Directly evidenced by Shadow DC7; spatial home-coordinate state |
| 520 | `AEGIS-TRANSACTION-STONE` | Legacy migration layer | **MIGRATION-OWNED** | Moved out of Shadow's 478 slot; temporary compatibility state |
| 521 | `AEGIS-TRANSACTION-ACTIVE` | Legacy migration layer | **MIGRATION-OWNED** | Moved out of Shadow's 479 slot; temporary compatibility state |

## Authority rule

`01_constants.per` is the declaration point. Shadow source IDs retain precedence over legacy compatibility IDs.

No downstream module may redefine 478 or 479 for another semantic purpose. Future migration work must treat these IDs as reserved for `home-x` and `home-y` unless a new source-level audit proves otherwise.

## Parser-safety decision

The fix changes only constant values and comments. It does not introduce rules, operators, conditional compilation, aliases, or duplicate definitions. The resulting declarations remain ordinary `.per` `defconst` forms.

The legacy symbolic names are intentionally retained so existing POC modules remain resolvable during migration. Their numeric IDs are now 520 and 521.

## Verification requirements

Before any module writes Shadow home coordinates:

1. `home-x` must resolve to `478`.
2. `home-y` must resolve to `479`.
3. No legacy transaction constant may resolve to `478` or `479`.
4. `AEGIS-TRANSACTION-STONE` must resolve to `520`.
5. `AEGIS-TRANSACTION-ACTIVE` must resolve to `521`.
6. No second `defconst` declaration may claim 478 or 479.
7. The legacy transaction subsystem remains migration-only until its namespace and ownership are fully retired.

## Source evidence

Shadow DC7 / `SourceShaRef` identifies the used goal range as `1-317, 392, 478-479` and directly declares `home-x 478` and `home-y 479`.

## Commit

Collision fix committed in `01_constants.per` as:

`4a779db9866fb9aca0c6710a9b90e5edd6928d90`
