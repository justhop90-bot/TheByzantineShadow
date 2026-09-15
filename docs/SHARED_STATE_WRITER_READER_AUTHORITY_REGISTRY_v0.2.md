# The Byzantine Shadow — Shared State / Writer-Reader Authority Registry v0.2

**Status:** AUTHORITATIVE SUPERSESSION of `SHARED_STATE_WRITER_READER_AUTHORITY_REGISTRY_v0.1.md`

**Scope:** Systems 01–09

**Purpose:** Promote recovered line-level donor occurrence evidence into the shared-state authority registry and eliminate unsupported `UNRECOVERED` classifications wherever the donor source now provides evidence.

**Source of truth:** Shadow donor `SourceShaRef`, SHA/blob `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`, 615,773-byte source. Line references below are source-file line numbers, not registry line numbers.

**Companion machine-readable extraction:** `docs/SHARED_STATE_STATIC_OCCURRENCE_EXTRACTION_v0.1.csv`.

---

## 1. Promotion rule

This version supersedes v0.1 for all rows listed below.

Three dispositions are now explicit:

1. **DONOR OCCURRENCE RECOVERED** — literal symbol occurrence and source rule are established at line level.
2. **AEGIS-GENERALIZATION / NO LITERAL DONOR STATE** — the registry state is an AEGIS semantic object rather than a donor symbol; `UNRECOVERED` is therefore the wrong classification.
3. **DONOR WRITER STILL UNRECOVERED** — the donor symbol is known and consumed, but no writer occurrence has yet been recovered from the available evidence. This status remains a genuine forensic gap.

The registry must never convert category 2 into category 3 merely because an AEGIS abstraction has no one-to-one donor symbol.

---

# 2. Corrected critical shared-state rows

| stable_id | symbol | owner | recovered writers | recovered readers / consumers | mutation path | verification source | conflict status | qualification | evidence |
|---|---|---|---|---|---|---|---|---|---|
| SSAR-S02-007 | `gl-build-progress` | Shadow progression layer | **R1851 [21481–21487]** `set-goal`; **R1853 [21499–21505]** `up-modify-goal`; **R1893 [21989–21995]** `set-goal`; **R1895 [22007–22013]** `up-modify-goal` | R1851 reads progress for skipped-build recovery; R1852 [21489–21497] reads progress as next-item gate; R1893 reads progress for skipped gold-camp recovery; R1894 [21997–22005] reads progress as next-item gate | `WORK ITEM → VERIFIED BUILD COUNT → progress mutation → NEXT ITEM` | observed building count / verified construction result | **MULTIPLE_WRITERS_SAME_SEMANTIC_STATE** | Q2,Q4,Q5,Q6,Q10,Q11,Q14 | DIRECT; CONFIRMED |
| SSAR-S02-008 | `gl-current-build-item` | Shadow progression layer | **R1852 [21489–21497]** `set-goal`; **R1894 [21997–22005]** `set-goal` | R1705 [19938–19945], R1706 [19947–19953], R1794 [20851–20857], R1852, R1853 [21499–21505], R1894, R1895 [22007–22013] | `REQUIREMENT / PROGRESSION → current work item → executor gating` | work-item completion/invalidation | **MULTIPLE_WRITERS_SAME_SEMANTIC_STATE** | Q2,Q4,Q5,Q6,Q8,Q10,Q11,Q14 | DIRECT; CONFIRMED |
| SSAR-S02-009 | `gl-progression-pause` | Shadow progression layer | **R1374 [16400–16406]**, **R1375 [16408–16422]**, **R1376 [16424–16438]** set `MARKET`; **R1381 [16464–16476]** clears to `-1` | R1375/R1376 test `gl-progression-pause == -1`; R1381 tests `== MARKET` and then clears it | `PAUSE REQUEST → economic/infrastructure work → EXECUTE → CLEAR` | downstream build/transaction state | **MULTIPLE_WRITERS_SAME_SEMANTIC_STATE** | Q2,Q4,Q5,Q6,Q8,Q10,Q11,Q14 | DIRECT; CONFIRMED |
| SSAR-S02-010 | `gl-escrow-state` | Shadow transaction/executor interface | **WRITER STILL UNRECOVERED** | R0273/R0283/R0285 [4690–4717] `up-can-build-line gl-escrow-state`; R0287/R0288 [4732–4747] same; R0290/R0292 [4749–4780] same; R1381 [16464–16476] `up-build ... gl-escrow-state`; R1704–R1708 [19927–19980] `up-train gl-escrow-state`; R1794–R1796 [20851–20882] build path; R1849–R1854 [21464–21522] construction path | `STATE SET/SELECTED → escrow-aware preflight → executor command → reconciliation` | transaction/resource observation | **WRITER_UNRECOVERED; CONSUMER_CONFIRMED** | Q2,Q4,Q5,Q9,Q11,Q14 | DIRECT consumption; writer UNCERTAIN |

---

# 3. Critical finding: the progression state is demonstrably multi-written

The donor evidence now establishes that the three progression carriers are not merely theoretical names.

### `gl-build-progress`

The donor contains both absolute writes and incrementing writes. The absolute writes occur in “come back if skipped” rules; the increments occur after building-count postconditions. Therefore the donor has at least two distinct mutation modes:

```text
RECOVERY / REWIND
    set-goal gl-build-progress <checkpoint>

NORMAL PROGRESSION
    up-modify-goal gl-build-progress c:+ 1
```

This is materially important for AEGIS. A naive single-writer migration that merely chooses one physical rule would destroy the donor's recovery semantics. The correct redesign is a **single semantic owner with multiple authorized mutation operations**.

### `gl-current-build-item`

The donor explicitly changes the current work item when the progression cursor reaches a checkpoint. It also reads the item in production/research jump gates. Therefore this state is both a progression identity and an executor-selection input.

### `gl-progression-pause`

The donor uses it as a cross-subsystem latch: multiple rules request `MARKET`, while the market build rule consumes the latch and clears it. This is a genuine shared control carrier and a direct example of the hidden control-plane coupling the authority architecture is intended to formalize.

---

# 4. `gl-escrow-state` finding

The extraction pass recovered **consumer/executor evidence**, but not a literal writer occurrence.

The distinction is important:

```text
DONOR FACT:
    gl-escrow-state is passed to escrow-aware predicates/commands.

NOT YET PROVEN:
    which donor rule assigns its value.

THEREFORE:
    consumer ownership is confirmed;
    writer ownership remains unresolved.
```

The known source uses include construction feasibility, escrow-aware construction, and escrow-aware training. The jump register independently records skipped executors using `up-train gl-escrow-state`, and records construction/resource-control bypasses around the progression carriers. These establish the symbol's operational role but do not prove its writer.

**Do not invent a writer.** The unresolved writer remains a P0 forensic item.

---

# 5. Constants promoted to line-level evidence

| stable_id | symbol | source lines | definition | value | classification | status |
|---|---|---:|---|---:|---|---|
| SSAR-S09-008 | `LOW-ESCROW` | 361 | `defconst` | 25 | donor policy constant | DIRECT / CONFIRMED |
| SSAR-S09-009 | `MID-ESCROW` | 362 | `defconst` | 35 | donor policy constant | DIRECT / CONFIRMED |
| SSAR-S09-010 | `MID-HIGH-ESCROW` | 363 | `defconst` | 40 | donor policy constant | DIRECT / CONFIRMED |
| SSAR-S09-011 | `HIGH-ESCROW` | 364 | `defconst` | 60 | donor policy constant | DIRECT / CONFIRMED |
| SSAR-S09-012 | `CA-WOOD-TRADING-THRESHOLD` | 378 | `defconst` | 300 | Castle-Age wood trading threshold | DIRECT / CONFIRMED |
| SSAR-S09-013 | `CA-EXCESS-WOOD-THRESHOLD` | 379 | `defconst` | 450 | Castle-Age wood excess threshold | DIRECT / CONFIRMED |
| SSAR-S09-014 | `CA-NEED-WOOD-THRESHOLD` | 380 | `defconst` | 250 | Castle-Age wood need threshold | DIRECT / CONFIRMED |
| SSAR-S09-015 | `CA-NEED-STONE-THRESHOLD` | 383 | `defconst` | 200 | Castle-Age stone need threshold | DIRECT / CONFIRMED |

**Important:** declaration evidence proves existence and value. It does not by itself prove writer/reader causal semantics. Rule-level use sites still require extraction before strategic interpretation.

---

# 6. Generic AEGIS state rows reclassified

The following v0.1 rows were incorrectly represented as if their lack of literal donor writers were an unresolved donor-source problem:

- `target-identity`
- `target-kind`
- `target-position`
- `observation-position`
- `worker-allocation`
- other generic AEGIS requirement/state objects with no literal donor symbol

They are now classified:

```text
AEGIS-GENERALIZATION
NO-LITERAL-DONOR-STATE
```

This means the correct question is not “where is the donor writer?” but:

> Which donor symbols/rules supply evidence that should be mapped into this AEGIS state, and which AEGIS writer contract will own the new semantic object?

No fabricated donor writer is permitted.

---

# 7. Conflict resolution derived from the occurrence pass

The recovered donor writes demonstrate why the single-writer doctrine cannot mean “one physical rule.”

The correct AEGIS model is:

```text
                 SINGLE SEMANTIC OWNER
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
       RECOVERY      NORMAL ADVANCE   CLEAR/RETIRE
       mutation        mutation         mutation
          │              │              │
          └──────────────┴──────────────┘
                         ↓
                 ONE STATE CONTRACT
```

Therefore:

- Multiple physical writers under one owner are legal.
- Multiple semantic owners are not.
- Absolute checkpoint writes and relative progress increments must be separate authorized operations.
- A legacy recovery rule cannot be allowed to arbitrarily rewrite a newer generation.
- `up-jump-rule` suppression does not grant ownership of the state it skips.

---

# 8. New qualification blockers

The occurrence pass changes the implementation risk assessment.

### P0 — progression ownership

The donor demonstrably has multiple physical writers for `gl-build-progress`, `gl-current-build-item`, and `gl-progression-pause`. Muse must not transplant them independently.

### P0 — escrow-state writer

`gl-escrow-state` consumers are proven; its writer remains unresolved. This is a true source gap and blocks any claim that the complete escrow state machine has been reconstructed.

### P1 — rule-use expansion

The recovered occurrences are sufficient to prove the core roles, but not yet sufficient to claim that every occurrence of these symbols has been enumerated. A full symbol occurrence census remains required before implementation freeze.

### P1 — threshold causal graph

The Castle-Age threshold declarations are proven at lines 378–383. Their individual writers/readers/branches must still be recovered before promoting them from policy constants to causal market rules.

---

# 9. Qualification gates

| gate | requirement | current state |
|---|---|---|
| Q1 | Symbol identity | PASS for recovered rows |
| Q2 | Complete writer inventory | PARTIAL; progression rows recovered, escrow writer unresolved |
| Q3 | Complete reader inventory | PARTIAL; material readers recovered, full census remains |
| Q4 | Single semantic owner | ARCHITECTURE ASSIGNED; donor multi-writer semantics require formalization |
| Q5 | Authorized mutation path | DEFINED; donor recovery/advance paths now evidence-backed |
| Q6 | Precedence | OPEN for competing donor progression writers |
| Q7 | Generation control | OPEN; donor has no proven AEGIS generation field |
| Q8 | Lifetime/reset/expiry | PARTIAL; explicit clears/recovery observed, complete lifecycle not yet proven |
| Q9 | Resource attribution | PARTIAL; escrow-aware commands recovered, attributable reservation model is AEGIS-generalization |
| Q10 | Progression safety | OPEN; donor advances cursor from observed building counts but AEGIS postcondition contract remains to qualify |
| Q11 | Verification | PARTIAL; building-count postconditions recovered; world-state verification still separate |
| Q12 | Failure handling | PARTIAL; skip/recovery paths recovered |
| Q13 | Bypass audit | PASS for recovered jump interactions; complete census remains |
| Q14 | Runtime ABI | OPEN |
| Q15 | Integrated vertical slice | OPEN |
| Q16 | Adversarial review | OPEN |

---

# 10. Required next extraction pass

The next pass is now narrowly defined rather than exploratory:

1. Resolve the writer of `gl-escrow-state`.
2. Enumerate every `gl-build-progress` occurrence, not merely the recovered progression rules.
3. Enumerate every `gl-current-build-item` occurrence.
4. Enumerate every `gl-progression-pause` occurrence.
5. Trace each occurrence into its preceding predicates and following executor/jump effects.
6. Build a writer→reader→executor graph for these four carriers.
7. Recover all threshold use sites for the Castle-Age market constants.
8. Update the registry and occurrence CSV in the same commit.
9. Do not promote any unresolved row to `IMPLEMENTATION-READY`.

---

# 11. Engineering conclusion

The static pass produced a substantive result: **the donor progression control plane is now directly observable at line level.** `gl-build-progress` has both checkpoint-rewind and increment writers; `gl-current-build-item` is explicitly selected at progression boundaries and consumed by downstream production/research gates; `gl-progression-pause` is a real cross-system latch with multiple request writers and an executor-clearing writer. `gl-escrow-state` is demonstrably consumed by escrow-aware build/train interfaces, but its writer remains genuinely unresolved.

That distinction is exactly the evidence boundary the registry is designed to enforce.

The next implementation decision should therefore be made from the recovered writer/reader graph—not from the apparent simplicity of the donor rules.
