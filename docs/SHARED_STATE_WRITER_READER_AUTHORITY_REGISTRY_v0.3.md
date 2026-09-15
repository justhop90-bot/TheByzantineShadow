# The Byzantine Shadow — Shared State / Writer-Reader Authority Registry v0.4

**Status:** AUTHORITATIVE SUPERSESSION OF v0.3 FOR `gl-escrow-state` PRECEDENCE/LIFETIME

**Parent:** `docs/SHARED_STATE_WRITER_READER_AUTHORITY_REGISTRY_v0.3.md`  
**Precedence forensic artifact:** `docs/GL_ESCROW_STATE_PRECEDENCE_AND_LIFETIME_FORENSICS_v0.1.md`  
**Static occurrence trace:** `docs/GL_ESCROW_STATE_FORENSIC_TRACE_v0.1.md`  
**Source of truth:** `SourceShaRef`, blob `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`.

---

## 1. Authoritative `gl-escrow-state` row

| Field | Value |
|---|---|
| stable_id | `SSAR-S02-010` |
| system | S02 / Shadow transaction-executor interface |
| semantic type | MODE |
| physical channel | goal 205 |
| definition | line 1571: `(defconst gl-escrow-state 205)` |
| writers | W1=15477, W2=15538, W3=15545, W4=17855, W5=20301, W6=20897 |
| `without-escrow` writer | W1 only |
| `with-escrow` writers | W2, W3, W4, W5, W6 |
| owner | Single semantic Shadow transaction/executor mode state |
| conflict status | `MULTIPLE_WRITERS_SAME_SEMANTIC_STATE` |
| source-order status | STATIC-QUALIFIED |
| effective same-pass winner | RUNTIME-OPEN |
| lifetime model | Writer-defined; no explicit TTL/epoch recovered |
| clear/reset | No undefined/neutral clear recovered; W1 is alternate-mode write; W2-W6 restore `with-escrow` |
| latest unconditional writer | W6 at 20897 |
| one-shot writer | W4 at 17855 (`disable-self`) |
| qualification | Q7 lifetime/precedence OPEN; Q11 verification OPEN; Q14 runtime ABI OPEN |

---

## 2. Precedence reconstruction

Static source order is:

```text
1571  definition
15477 W1  current-age >= castle-age → WITHOUT
15538 W2  SPLIT == 2 → TRAIN → WITH
15545 W3  true → WITH
17855 W4  true → WITH → disable-self
20301 W5  ESKIRMS + research-feasibility → RESEARCH → WITH
20897 W6  true → WITH
```

Value-level asymmetry:

```text
WITHOUT-ESCROW: W1 only
WITH-ESCROW:    W2/W3/W4/W5/W6
```

Static overwrite candidates therefore form:

```text
W1 → W2/W3/W4/W5/W6
W2 → W3
W3 → W4/W5/W6
W4 → W5/W6
W5 → W6
```

These are **potential overwrite edges**, not runtime-proven same-pass execution edges.

---

## 3. Writer semantics

### W1 — line 15477

```text
(current-age >= castle-age)
→ set-goal gl-escrow-state without-escrow
```

Classification: contextual mode exception.  
Potential lifetime: until a later writer changes goal 205.

### W2 — line 15538

```text
goal SPLIT == 2
→ up-train gl-escrow-state c: skirmisher-line
→ set-goal gl-escrow-state with-escrow
→ set-goal SPLIT 0
```

Classification: post-training restoration.

### W3 — line 15545

```text
true
→ set-goal gl-escrow-state with-escrow
→ set-goal SPLIT 0
```

Classification: unconditional baseline/reset candidate.  
Precedence significance: immediate later writer after W2.

### W4 — line 17855

```text
true
→ set-strategic-number sn-enable-patrol-attack 1
→ set-goal gl-escrow-state with-escrow
→ disable-self
```

Classification: one-shot military initialization/restoration.  
`disable-self` qualifies the writer rule's lifetime, not necessarily the goal value's lifetime.

### W5 — line 20301

Requires `gl-current-build-item == ESKIRMS` and at least one of ordinary, escrow-aware, or `up-can-research` feasibility predicates for elite skirmisher research; then:

```text
up-research gl-escrow-state c: ri-elite-skirmisher
→ set-goal gl-escrow-state with-escrow
```

Classification: post-research restoration.

### W6 — line 20897

```text
true
→ set-goal gl-escrow-state with-escrow
→ set-goal SPLIT 0
```

Classification: later unconditional baseline/reset candidate. It is the latest recovered unconditional writer.

---

## 4. Lifetime / reset semantics

No explicit goal-205 clear, undefined state, TTL, or epoch expiry was recovered.

The reconstructed state behavior is therefore:

```text
WITH
  ↓ W1 when Castle Age predicate becomes true
WITHOUT
  ↓ W2/W3/W4/W5/W6 when their rules execute
WITH
```

W4 is the only writer whose rule explicitly self-terminates. W2 and W3/W6 manipulate `SPLIT` as local control state; they do not clear goal 205.

The exact persistence interval of `WITHOUT` remains runtime-open.

---

## 5. Authority decision

**Single semantic owner, multiple authorized physical writers** remains the authoritative ownership model.

The six donor writers must not become six independent AEGIS authorities. Their physical multiplicity must be represented as registered mutation sites with explicit reason, precedence class, and lifetime.

Recommended implementation rule:

```text
A physical write to goal 205 is legal only when its mutation reason,
context, precedence, and expected lifetime are registered.
```

---

## 6. Remaining qualification gates

| Gate | Status | Required proof |
|---|---|---|
| Q1 Symbol identity | PASS | goal 205 / line 1571 |
| Q2 Writer inventory | PASS | six direct writes recovered |
| Q4 Ownership | PASS | single semantic owner |
| Q5 Mutation path | PASS | direct goal mutation + executor consumption |
| Q7 Lifetime / precedence | **OPEN** | rule scheduling, overwrite window, jump effects |
| Q9 Resource attribution | PASS statically | goal mode distinct from escrow amount accounting |
| Q11 Verification | **OPEN** | prove downstream executor interprets intended mode |
| Q14 Runtime ABI | **OPEN** | target-engine `EscrowState` semantics and timing |

**No claim of runtime-qualified effective winner is authorized until Q7/Q11/Q14 close.**
