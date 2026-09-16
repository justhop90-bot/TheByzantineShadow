# Shadow Source-Order Machine Index Reconciliation v0.4

**Status:** RECONCILED / CANONICAL-SOURCE-IDENTITY VERIFIED / STATIC MACHINE INDEX AVAILABLE

**Repository:** `justhop90-bot/TheByzantineShadow`

**Current `main` ref at audit:** `2cc0e88ad4236b2aaa1b7c646143add5fe16c8b1`

**Canonical donor path:** `ShadowSource.per`

**Canonical donor SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

**Canonical donor SHA-256:** `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`

**Canonical donor:** 22,604 lines / 615,773 UTF-8 bytes / 1,956 `defrule` blocks.

**Existing machine index:** `docs/forensics/SHADOW_SOURCE_ORDER_MATRIX_v0.3.md`

**Generator:** `tools/forensics_shadow_source_matrix.py`

---

## 1. Reconciliation result

The repository already contains the required 1,956-rule source-order machine index. The important forensic question was therefore not whether another rule table should be generated, but whether the existing matrix is still authoritative for the current canonical `ShadowSource.per`.

### Result: YES — source identity is cryptographically reconciled.

The existing matrix was generated from the preserved historical donor object `Shadow DC7.per` at commit `1d9f45b3b9ac03adc24103df2b21c84b92a45fb6` and records the preserved Git blob SHA-1 as:

`70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

The current `ShadowSource.per` has the same Git blob SHA-1. `SourceShaRef` also resolves to the same SHA-1 and source SHA-256. Therefore the historical path name and the current canonical path are not competing donor versions for this matrix: they resolve to the same source object.

This closes the previously open concern that the matrix might describe an older or different Shadow source.

---

## 2. What the machine index actually contains

`SHADOW_SOURCE_ORDER_MATRIX_v0.3.md` contains one row for each of the 1,956 extracted `defrule` blocks and records:

```text
rule ordinal
source line interval
entry predicates
state writes
escrow mutations
commands
jump expression
normal successor
jump successor
release behavior
completion condition
forensic status
creator-intent interpretation
```

The generator additionally establishes the extraction method:

```text
Git object
  -> UTF-8 source
  -> comment/string masking
  -> balanced-parenthesis rule extraction
  -> defrule ordinalization
  -> top-level predicate/action extraction
  -> state / escrow / command / observer classification
  -> jump successor calculation
  -> source-order matrix
```

The generator uses the donor Git object rather than a connector excerpt, so the matrix is not dependent on the truncated source views returned by repository inspection tools.

---

## 3. Rule-count closure

The following identity is now established:

```text
ShadowSource.per
    SHA-1 70a18a3b69e8ea46bd5132673fe9fcf8a36595ee
    SHA-256 c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4
    22,604 source lines
    615,773 UTF-8 bytes
    1,956 defrule blocks
          |
          v
SHADOW_SOURCE_ORDER_MATRIX_v0.3.md
    1,956 numbered rule rows
```

No new competing rule index is required.

---

## 4. Jump semantics reconciliation

The matrix generator explicitly models the donor jump idiom as:

```text
jump target = current rule ordinal + 1 + Δ
```

Thus a `up-jump-rule 1` skips the immediate successor and lands on the following rule, while `up-jump-rule -1` returns to the current rule. The matrix records both the original jump expression and the calculated successor.

This is sufficient as a **static donor control-flow index**. It does not by itself establish runtime reachability. Disabled rules, predicates, timers, engine state, and source-order interactions remain separate qualification dimensions.

---

## 5. Completion semantics reconciliation

The matrix deliberately does not promote commands into completion facts.

The distinction is:

```text
command issued
    !=
pending object observed
    !=
world object/unit/research state observed
    !=
progression reconciled
    !=
escrow released
```

Where a rule itself contains an observable completion predicate, the matrix records it. Otherwise the completion field remains `not established in this rule`.

This is consistent with the repository's construction/escrow doctrine and prevents the machine index from becoming a false transaction model.

---

## 6. What is reconciled vs. what remains open

| Machine-index field | Reconciliation state | Evidence |
|---|---|---|
| Canonical source identity | CLOSED | Current `ShadowSource.per` SHA-1/SHA-256; `SourceShaRef` |
| Source line count | CLOSED | 22,604 |
| UTF-8 byte count | CLOSED | 615,773 |
| Rule count | CLOSED | 1,956 `defrule` blocks |
| Rule ordinal sequence | CLOSED | Generated source-order matrix |
| Source line ranges | CLOSED | Matrix rows |
| Predicate/action extraction | CLOSED STATICALLY | Matrix generator |
| State-write classification | CLOSED AS STATIC CLASSIFICATION | Generator `STATE_WRITES` set |
| Escrow-operation classification | CLOSED AS STATIC CLASSIFICATION | Generator `ESCROW` set |
| Command classification | CLOSED AS STATIC CLASSIFICATION | Generator command-head set |
| Observer classification | CLOSED AS STATIC CLASSIFICATION | Generator observer set |
| Jump successor calculation | CLOSED AS STATIC CALCULATION | Generator |
| Runtime reachability | OPEN | Requires runtime/trace evidence |
| Dynamic engine-side effects | OPEN | Static `.per` cannot prove them |
| Complete semantic type of every symbol | OPEN | Requires writer/reader graph |
| Donor-vs-implementation topology equivalence | OPEN | Separate donor→ShadowByzantine diff |

The important correction is therefore: **the 1,956-rule machine index is not missing; it exists and is source-authenticated. The remaining gap is semantic closure and implementation reconciliation, not source-order extraction.**

---

## 7. Authoritative artifacts after reconciliation

The evidence chain is now:

```text
ShadowSource.per
    |
    +-- SourceRef
    +-- SourceShaRef
    |
    v
SHADOW_SOURCE_ORDER_MATRIX_v0.3.md
    |
    +-- tools/forensics_shadow_source_matrix.py
    |
    v
SHADOW_SOURCE_ORDER_RECONCILIATION_v0.4.md
    |
    v
SHADOW → ShadowByzantine topology diff
```

The matrix remains the rule-level source-order authority. This document is the reconciliation record and must not become a second rule table.

---

## 8. Next machine-level closure

The next forensic operation is no longer "extract the 1,956 rules." It is to consume the reconciled matrix and construct the semantic/control comparison:

```text
rule ordinal
  -> donor reads/writes
  -> jump edges
  -> escrow signatures
  -> search signatures
  -> progression signatures
  -> current ShadowByzantine location
  -> runtime load status
  -> topology delta
  -> evidence class
```

That comparison is the donor-to-ShadowByzantine diff and is maintained separately from the source-order matrix.

---

## 9. Evidence discipline

This artifact intentionally makes no claim that all 1,956 rules are live, strategically important, or intended to be transplanted. The source itself contains explicit commentary that unused experimental code may remain.

Likewise, a row in the matrix does not establish runtime qualification. The machine index establishes **what exists in the canonical source and where it exists**. Reachability, semantic coupling, and implementation fidelity require subsequent evidence.
