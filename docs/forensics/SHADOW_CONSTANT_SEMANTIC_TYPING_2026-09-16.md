# Shadow Constants Semantic Typing Audit — 2026-09-16

**Repository:** `justhop90-bot/TheByzantineShadow`  
**Primary registry:** `01_constants.per`  
**Reference:** Shadow DC7 / `SourceShaRef`  
**Purpose:** distinguish true symbolic aliases from cross-domain numeric reuse before any renumbering or cleanup.

## Result

The current constants registry does not establish any duplicate symbolic declaration that is safe to delete.

The repeated numeric values fall into several distinct semantic classes. Numeric equality alone is insufficient evidence of aliasing because Shadow uses compact integer namespaces for goals/state slots, timers, enumerations, group selectors, geometry, and ordinary scalar thresholds.

## Classification

| Symbol family / example | Numeric value | Semantic class | Disposition |
|---|---:|---|---|
| `home-x` | 478 | Shadow goal / coordinate state | SOURCE-OWNED; preserve |
| `home-y` | 479 | Shadow goal / coordinate state | SOURCE-OWNED; preserve |
| `gl-identity` | 420 | Shadow source symbol | SOURCE-PRESERVED; usage proof required before consolidation |
| `Promi` | 420 | Shadow source symbol | SOURCE-PRESERVED; usage proof required before consolidation |
| `Doomsday` | 42 | Shadow source symbol | SOURCE-PRESERVED; do not equate with goal/timer merely by value |
| `gl-target-type` | 42 | Shadow goal/state symbol | SOURCE-PRESERVED; separate semantic consumer required |
| `villager-timer` | 42 | Shadow timer | TIMER-NAMESPACE; not a goal collision |
| `ATTACKING` | 1 | Enumeration/state value | ENUMERATION; preserve |
| `FLANK` | 1 | Enumeration/state value | ENUMERATION; preserve |
| `COMBINED` | 1 | Enumeration/state value | ENUMERATION; preserve |
| `LumberFirst` | 1 | Policy mode value | ENUMERATION; preserve |
| `MarchingOne` | 1 | Movement state value | ENUMERATION; preserve |
| `RangedGroup` | 1 | Group selector | GROUP-NAMESPACE; preserve |
| `POCKET` | 2 | Enumeration/state value | ENUMERATION; preserve |
| `VATTACKING` | 2 | Enumeration/state value | ENUMERATION; preserve |
| `SEPARATE` | 2 | Enumeration/state value | ENUMERATION; preserve |
| `ONE-MINUTE` | 2 | Timer duration | SCALAR/TIME; preserve |
| `KnightGroup` | 2 | Group selector | GROUP-NAMESPACE; preserve |

## Alias decision rule

A pair is classified as a true compatibility alias only when at least one of the following is established:

1. The Shadow source explicitly uses the symbols interchangeably for the same engine slot.
2. A current executable rule consumes both names as equivalent representations of one state.
3. A compatibility requirement explicitly requires the old symbolic name to resolve to the newer canonical value.

If none of these conditions is met, numeric equality is classified as cross-domain reuse or unresolved source residue, not an alias.

## High-risk cases

### `gl-identity` / `Promi` = 420

The registry proves equal numeric values but does not, by declaration alone, prove semantic equivalence. Both symbols therefore remain source-preserved. No renaming, deletion, or canonicalization is justified from the registry alone.

### `Doomsday` / `gl-target-type` / `villager-timer` = 42

These demonstrate why raw integer collision detection is insufficient. The three names occupy visibly different conceptual domains. They must not be merged merely because their values match.

### Value `1` and value `2` clusters

The same small integers are reused for attack/formation states, policy modes, movement states, timers, and group selectors. This is compatible with Shadow's source style and is not evidence of duplicate declarations.

## Parser-safe remediation

**No executable `.per` modification is warranted by this pass.**

Renumbering any of the source-derived values would alter behavior unless every consumption site were first reconstructed and the engine namespace proved. The safe action is therefore documentation plus preservation.

The existing migration-only relocation remains:

```text
AEGIS-TRANSACTION-STONE 478 -> 520
AEGIS-TRANSACTION-ACTIVE 479 -> 521
```

No new aliases or numeric IDs were introduced.

## Required next audit

The next level is consumption-site typing, not declaration cleanup. For each nontrivial source constant, trace every read/write and classify the actual engine interface used:

- `set-goal` / `up-get-goal` / `up-compare-goal` → goal/state namespace
- timer access → timer namespace
- strategic-number access → strategic-number namespace
- object/group/geometry access → corresponding engine namespace
- literal comparisons without engine state access → scalar/enum value

Only after that trace may an unresolved pair be promoted to `CANONICAL-ALIAS`, `DUPLICATE-RESIDUE`, or `INTENTIONAL-CROSS-DOMAIN-REUSE`.

## Verification requirements

1. Every claimed alias has a consumption-site proof.
2. No integer is renumbered solely because another symbol shares it.
3. `478/479` remain reserved to `home-x/home-y`.
4. `520/521` remain migration-only legacy IDs.
5. Shadow source-derived symbols remain unchanged until their runtime namespace is proven.
6. The registry continues to contain one declaration per symbol.
