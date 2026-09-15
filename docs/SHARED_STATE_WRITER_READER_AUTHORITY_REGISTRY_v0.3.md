# The Byzantine Shadow — Shared State / Writer-Reader Authority Registry v0.3

**Status:** AUTHORITATIVE SUPERSESSION FOR THE `gl-escrow-state` ROW IN v0.2

**Scope:** Systems 01–09; this revision specifically closes the `gl-escrow-state` writer gap.

**Parent registry:** `docs/SHARED_STATE_WRITER_READER_AUTHORITY_REGISTRY_v0.2.md`

**Forensic trace:** `docs/GL_ESCROW_STATE_FORENSIC_TRACE_v0.1.md`

**Source of truth:** `SourceShaRef`, blob `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`.

---

## 1. Superseding row

| stable_id | system | state_class | symbol_name | physical_channel | owner | writers | readers / consumers | mutation path | verification source | conflict status | qualification gates | evidence | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SSAR-S02-010 | S02 | MODE | `gl-escrow-state` | goal **205** | Shadow transaction/executor interface | **R15477 [15477] `set-goal ... without-escrow`**; **R15545 [15545] `set-goal ... with-escrow`**; **R15538 [15538] `set-goal ... with-escrow`**; **R17855 [17855] `set-goal ... with-escrow`**; **R20301 [20301] `set-goal ... with-escrow`**; **R20897 [20897] `set-goal ... with-escrow`** | Construction feasibility: [4698], [4744], [4751], [4760]. Research executors: [14319], [14353], [14370], [14418], [14467], [14517], [14567], [14617], [14668], [14720], [15030], [15127], [20297], [20299], [22152]. Training: [15248], [15267], [15441], [15460], [15468], [15513], [15537], [15587], [15592], [15646], [15653], [19957], [19963], [19975], [19977], [19985], [19991]. Construction executors: [15798], [15860], [15946], [16000], [16075], [16127], [16191], [16262], [16333], [16473], [20369], [20536], [20846], [20890], [20935], [20941], [21096], [21108], [21515], [21518], [21778], [21869], [22087], [22094], [22106] | `MODE SET → escrow-aware preflight → executor command → engine interprets EscrowState → resource/transaction consequence → reassessment` | Goal mutation is statically proven; executor/resource postconditions remain runtime qualification | **MULTIPLE_WRITERS_SAME_SEMANTIC_STATE**; all recovered writers are direct `set-goal` operations | Q1,Q2,Q4,Q5,Q7,Q9,Q11,Q14 | DIRECT / CONFIRMED for definition, writers, and consumers; runtime semantics QUALIFY | STATIC-QUALIFIED; RUNTIME-QUALIFICATION-REQUIRED |

---

## 2. Exact writer evidence

### W1 — `without-escrow`

**Source line 15477**:

```text
(set-goal gl-escrow-state without-escrow)
```

Context: the preceding rule is in the general/skirmisher production section and triggers at Castle Age. The operation explicitly selects the non-escrow execution mode.

### W2 — `with-escrow`

**Source line 15538**:

```text
(set-goal gl-escrow-state with-escrow)
```

Context: after the skirmisher training command in the `SPLIT 2` branch. The same rule performs `up-train gl-escrow-state ...` before setting the mode for subsequent execution.

### W3 — unconditional initialization/reset-to-mode

**Source line 15545**:

```text
(set-goal gl-escrow-state with-escrow)
```

Context: unconditional rule; also clears `SPLIT`.

### W4 — unconditional initialization in military setup

**Source line 17855**:

```text
(set-goal gl-escrow-state with-escrow)
```

Context: unconditional rule that also enables patrol attack and disables itself.

### W5 — technology completion / escrow-mode restoration

**Source line 20301**:

```text
(set-goal gl-escrow-state with-escrow)
```

Context: after `up-research gl-escrow-state c: ri-elite-skirmisher`; restores the mode after the research transaction.

### W6 — farm executor initialization/restoration

**Source line 20897**:

```text
(set-goal gl-escrow-state with-escrow)
```

Context: unconditional rule immediately following the general farm build path.

The exact surrounding source confirms W1 and W2/W3 in the skirmisher section, W4 in the military setup, W5 after elite-skirmisher research, and W6 in the farm section. fileciteturn195file0L2-L2 fileciteturn196file0L2-L2 fileciteturn197file0L2-L2 fileciteturn198file0L2-L2

---

## 3. Definition evidence

**Source line 1571**:

```text
(defconst gl-escrow-state 205)
```

Therefore the physical channel is **goal 205**. The source places this definition in `QECONOMY`. The exact donor occurrence is also recorded in the static trace.

---

## 4. Reader / consumer authority

The donor uses the carrier in three major executor families.

### Construction

Examples include:

```text
(up-can-build-line gl-escrow-state ...)
(up-build place-control gl-escrow-state ...)
(up-build place-normal gl-escrow-state ...)
```

Recovered ranges include **4698**, **4744**, **4751**, **4760**, **15798**, **15860**, **15946**, **16000**, **16075**, **16127**, **16191**, **16262**, **16333**, **16473**, **20369**, **20536**, **20846**, **20890**, **20935**, **20941**, **21096**, **21108**, **21515**, **21518**, **21778**, **21869**, **22087**, **22094**, and **22106**.

### Research

The carrier is supplied to `up-can-research` / `up-research` at multiple research stages, including lines **14319–15127**, **19558**, **19608**, **19742**, **19877**, **20297**, **20299**, and **22152**.

### Training

The carrier is supplied to `up-can-train` / `up-train` across military and civilian production, including lines **15248–15653** and **19957–19991**.

The complete literal occurrence list is preserved in `GL_ESCROW_STATE_FORENSIC_TRACE_v0.1.md`; no consumer occurrence should be inferred beyond that static extraction.

---

## 5. Mutation semantics

`gl-escrow-state` is a **mode carrier**, not an escrow amount register.

The donor establishes two mode values:

```text
without-escrow
with-escrow
```

The state is therefore mutated directly by `set-goal`, while the executor commands consume the current value as their `EscrowState` parameter.

This must remain distinct from:

```text
set-escrow-percentage
up-modify-escrow
release-escrow
```

Those commands mutate escrow resource accounting/policy; they do not mutate goal 205.

---

## 6. Authority interpretation

The v0.2 classification `WRITER STILL UNRECOVERED` is **obsolete**.

The donor has a genuine multi-writer physical representation of one semantic state:

```text
                  gl-escrow-state / goal 205
                           │
             ┌─────────────┴─────────────┐
             │                           │
      without-escrow                with-escrow
      W1 / line 15477          W2-W6 / 15538,15545,
                               17855,20301,20897
             │                           │
             └─────────────┬─────────────┘
                           ▼
                  escrow-aware executor
```

The correct AEGIS authority rule is therefore:

> **Single semantic owner, multiple authorized physical writes.**

The donor does not demonstrate competing semantic owners merely because several rules assign the same goal.

---

## 7. Reset / initialization classification

Not all `with-escrow` writes mean the same thing semantically.

| writer | likely role | evidence status |
|---|---|---|
| W1 line 15477 | explicit switch to `without-escrow` at Castle Age | DIRECT; semantic role strongly indicated by predicate context |
| W2 line 15538 | post-training mode restoration | DIRECT; context confirms ordering |
| W3 line 15545 | unconditional default/initialization to `with-escrow` | DIRECT; exact strategic purpose requires broader rule-order interpretation |
| W4 line 17855 | one-shot initialization for military setup | DIRECT; exact lifetime semantics require rule-order/engine qualification |
| W5 line 20301 | post-research restoration | DIRECT; context confirms preceding research command |
| W6 line 20897 | farm-section restoration/default | DIRECT; exact global lifetime semantics require rule-order qualification |

Do **not** collapse W3/W4/W6 into a single “global initialization” claim until source-order and rule-disable behavior are analyzed across the complete donor.

---

## 8. Qualification gates

- **Q1 Symbol identity:** PASS — goal 205.
- **Q2 Writer inventory:** PASS — six direct symbolic writers recovered.
- **Q4 Ownership:** PASS at semantic level only; all writes belong to the donor's common control plane, but AEGIS owner remains the Shadow transaction/executor interface.
- **Q5 Mutation path:** PASS statically — `set-goal` writes mode values; executor commands consume the mode.
- **Q7 Lifetime / generation:** OPEN — exact lifetime interaction among unconditional and contextual writes remains a rule-order question.
- **Q9 Resource attribution:** PASS for separation of goal mode vs escrow amount channels; exact economic consequence remains runtime-qualified.
- **Q11 Verification:** OPEN — command/result postconditions remain separate from goal mutation.
- **Q14 Runtime ABI:** OPEN — `with-escrow` / `without-escrow` numeric/value semantics must be qualified against the target engine.

## 9. Registry disposition

The canonical v0.3 status is:

```text
symbol: gl-escrow-state
goal: 205
writers: 6 direct symbolic writers
resets: W1 is an explicit mode switch to without-escrow; no separate clear-to-undefined operation recovered
readers: construction + research + training executor families
owner: Shadow transaction/executor interface
conflict: multiple physical writers / single semantic state
static status: CONFIRMED
runtime status: OPEN
```

This closes the previous P0 **writer-discovery** gap. The remaining P0/P1 work is now **writer precedence, lifetime, and runtime ABI qualification**, not writer discovery.