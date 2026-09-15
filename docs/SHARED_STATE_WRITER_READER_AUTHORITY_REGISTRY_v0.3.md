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
| SSAR-S02-010 | S02 | MODE | `gl-escrow-state` | goal **205** | Shadow transaction/executor interface | **R15477 [15477] `set-goal ... without-escrow`**; **R15538 [15538] `set-goal ... with-escrow`**; **R15545 [15545] `set-goal ... with-escrow`**; **R17855 [17855] `set-goal ... with-escrow`**; **R20301 [20301] `set-goal ... with-escrow`**; **R20897 [20897] `set-goal ... with-escrow`** | Construction feasibility: [4698], [4744], [4751], [4760]. Research: [14319], [14353], [14370], [14418], [14467], [14517], [14567], [14617], [14668], [14720], [15030], [15127], [19558], [19608], [19742], [19877], [20297], [20299], [22152]. Training: [15248], [15267], [15441], [15460], [15468], [15513], [15537], [15587], [15592], [15646], [15653], [19957], [19963], [19975], [19977], [19985], [19991]. Construction executors: [15798], [15860], [15946], [16000], [16075], [16127], [16191], [16262], [16333], [16473], [20369], [20536], [20846], [20890], [20935], [20941], [21096], [21108], [21515], [21518], [21778], [21869], [22087], [22094], [22106] | `MODE SET → escrow-aware preflight → executor command → engine interprets EscrowState → resource/transaction consequence → reassessment` | Goal mutation statically proven; executor/resource postconditions runtime-qualified | **MULTIPLE_WRITERS_SAME_SEMANTIC_STATE**; all recovered writers are direct `set-goal` operations | Q1,Q2,Q4,Q5,Q7,Q9,Q11,Q14 | DIRECT / CONFIRMED for definition, writers, and consumers; runtime semantics QUALIFY | STATIC-QUALIFIED; RUNTIME-QUALIFICATION-REQUIRED |

---

## 2. Exact writer evidence

### W1 — explicit switch to `without-escrow`

**Source line 15477:**

```text
(set-goal gl-escrow-state without-escrow)
```

This is a direct mode mutation. The surrounding rule is in the general/skirmisher section and is gated by Castle Age.

### W2 — post-training mode restoration

**Source line 15538:**

```text
(set-goal gl-escrow-state with-escrow)
```

The rule first issues `up-train gl-escrow-state c: skirmisher-line` and then writes `with-escrow`.

### W3 — unconditional mode initialization/restoration

**Source line 15545:**

```text
(set-goal gl-escrow-state with-escrow)
```

This is an unconditional rule and therefore has potentially broad precedence implications.

### W4 — one-shot military initialization

**Source line 17855:**

```text
(set-goal gl-escrow-state with-escrow)
```

The same rule enables patrol attack and disables itself, making this a distinct one-shot initialization context.

### W5 — post-research restoration

**Source line 20301:**

```text
(set-goal gl-escrow-state with-escrow)
```

The write follows `up-research gl-escrow-state c: ri-elite-skirmisher`, demonstrating an explicit post-transaction mode restoration.

### W6 — farm-section initialization/restoration

**Source line 20897:**

```text
(set-goal gl-escrow-state with-escrow)
```

This follows the general farm executor path and is another unconditional write.

---

## 3. Definition evidence

**Source line 1571:**

```text
(defconst gl-escrow-state 205)
```

Therefore the physical channel is **goal 205**. The symbol is declared in the donor's `QECONOMY` namespace.

---

## 4. Reader / consumer authority

The complete static trace identifies the following consumer families.

### Construction

Representative forms:

```text
(up-can-build-line gl-escrow-state ...)
(up-can-build gl-escrow-state ...)
(up-build place-control gl-escrow-state ...)
(up-build place-normal gl-escrow-state ...)
```

Recovered consumer lines include **4698, 4744, 4751, 4760, 15798, 15860, 15946, 16000, 16075, 16127, 16191, 16262, 16333, 16473, 20369, 20536, 20846, 20890, 20935, 20941, 21096, 21108, 21515, 21518, 21778, 21869, 22087, 22094, 22106**.

### Research

Recovered `up-can-research` / `up-research` consumers include **14319, 14353, 14370, 14418, 14467, 14517, 14567, 14617, 14668, 14720, 15030, 15127, 19558, 19608, 19742, 19877, 20297, 20299, 22152**.

### Training

Recovered `up-can-train` / `up-train` consumers include **15248, 15267, 15441, 15460, 15468, 15513, 15537, 15587, 15592, 15646, 15653, 19957, 19963, 19975, 19977, 19985, 19991**.

The full literal occurrence inventory is preserved in `GL_ESCROW_STATE_FORENSIC_TRACE_v0.1.md`.

---

## 5. Mutation semantics

`gl-escrow-state` is a **mode carrier**, not an escrow amount register.

The donor directly assigns two semantic modes:

```text
without-escrow
with-escrow
```

The executor commands then consume the current goal value as their `EscrowState` parameter.

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

The correct AEGIS authority rule is:

> **Single semantic owner, multiple authorized physical writes.**

The presence of six physical writers does not by itself establish competing semantic owners.

---

## 7. Reset / initialization classification

| writer | role classification | evidence |
|---|---|---|
| W1 line 15477 | explicit switch to `without-escrow` | DIRECT; surrounding Castle-Age context |
| W2 line 15538 | post-training mode restoration | DIRECT; command ordering establishes relationship |
| W3 line 15545 | unconditional default/initialization | DIRECT; exact precedence requires rule-order analysis |
| W4 line 17855 | one-shot initialization | DIRECT; `disable-self` establishes local lifetime |
| W5 line 20301 | post-research restoration | DIRECT; immediately follows research executor |
| W6 line 20897 | farm-section initialization/restoration | DIRECT; exact global lifetime requires rule-order analysis |

There is **no separate clear-to-undefined operation recovered**. `without-escrow` is a semantic mode, not an absent/uninitialized state.

Do not collapse W3/W4/W6 into one global initializer until full rule-order and disable-self interactions are audited.

---

## 8. Qualification gates

- **Q1 Symbol identity:** PASS — goal 205.
- **Q2 Writer inventory:** PASS — six direct symbolic writers recovered.
- **Q4 Ownership:** PASS at semantic level; AEGIS owner remains Shadow transaction/executor interface.
- **Q5 Mutation path:** PASS statically — `set-goal` writes mode values; executor commands consume them.
- **Q7 Lifetime / generation:** OPEN — precedence among unconditional/contextual writers remains to be reconstructed.
- **Q9 Resource attribution:** PASS for separation of goal mode from escrow amount channels; economic consequence remains runtime-qualified.
- **Q11 Verification:** OPEN — command result remains separate from mode mutation.
- **Q14 Runtime ABI:** OPEN — exact `with-escrow` / `without-escrow` value semantics must be qualified against the target engine.

## 9. Canonical registry disposition

```text
symbol: gl-escrow-state
goal: 205
writers: 6 direct symbolic writers
resets: explicit mode switch to without-escrow; no undefined-clear recovered
readers: construction + research + training executor families
owner: Shadow transaction/executor interface
conflict: multiple physical writers / single semantic state
static status: CONFIRMED
runtime status: OPEN
```

This closes the previous P0 **writer-discovery** gap. Remaining work is **writer precedence, lifetime, and runtime ABI qualification**, not writer discovery.