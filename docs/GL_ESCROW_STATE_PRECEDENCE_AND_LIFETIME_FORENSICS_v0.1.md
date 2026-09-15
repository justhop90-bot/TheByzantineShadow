# The Byzantine Shadow — `gl-escrow-state` Precedence & Lifetime Forensics v0.1

**Status:** STATIC-QUALIFIED / RUNTIME-OPEN  
**Source:** `SourceShaRef` on `main`  
**Source blob:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Symbol definition:** line 1571 — `(defconst gl-escrow-state 205)`  
**Purpose:** reconstruct the six direct writers to `gl-escrow-state`, their local predicates, source ordering, overwrite relationships, reset behavior, and lifetime semantics without promoting static source order into unqualified runtime fact.

---

## 1. Executive finding

The donor contains **six direct writers** to one physical goal channel, goal **205**:

| Writer | Source line | Assigned value | Local role |
|---|---:|---|---|
| W1 | 15477 | `without-escrow` | Castle-Age mode switch in general/skirmisher section |
| W2 | 15538 | `with-escrow` | Post-skirmisher-training restoration |
| W3 | 15545 | `with-escrow` | Unconditional restoration / baseline reset |
| W4 | 17855 | `with-escrow` | One-shot military initialization |
| W5 | 20301 | `with-escrow` | Post-elite-skirmisher research restoration |
| W6 | 20897 | `with-escrow` | Farm-section unconditional restoration |

The strongest static conclusion is:

> `gl-escrow-state` is a **mode latch with multiple physical writers**, not a resource register. Five writers assign `with-escrow`; one writer assigns `without-escrow`.

The strongest precedence conclusion that can be established **without runtime rule-engine qualification** is based on source order and local rule structure:

1. W1 can establish `without-escrow` at line 15477 when Castle Age is reached.
2. W2 can subsequently restore `with-escrow` at line 15538 when `SPLIT == 2` fires.
3. W3 is an unconditional `true` rule immediately after W2 and therefore is the principal **static later-write candidate** capable of overwriting W2 on the same rule-evaluation pass if ordinary source-order execution applies.
4. W4, W5, and W6 occur substantially later in the source and each independently writes `with-escrow` in their own execution contexts.
5. No direct writer later than W1 assigns `without-escrow`.
6. No direct clear-to-undefined/reset-to-neutral operation for goal 205 was recovered.

Therefore the donor's **static terminal tendency is strongly `with-escrow`**, but the exact per-tick winner and persistence interval remain runtime qualification questions because source-order execution, repeated-rule behavior, `disable-self`, and jump semantics must be qualified against the target engine.

---

## 2. Physical state definition

**Source line 1571:**

```text
(defconst gl-escrow-state 205)
```

The goal is therefore a physical state carrier at **goal 205**.

The donor uses the carrier as the `EscrowState` argument to escrow-aware commands, including `up-can-*` and `up-*` construction, research, and training operations. The static occurrence inventory is recorded separately in `docs/GL_ESCROW_STATE_FORENSIC_TRACE_v0.1.md`.

The carrier has two recovered values:

```text
without-escrow
with-escrow
```

These are **mode values**, not food/wood/gold/stone escrow quantities.

---

## 3. Writer W1 — Castle-Age mode switch

**Source line 15477:**

```text
(defrule
    (current-age >= castle-age)
=>
    (set-goal gl-escrow-state without-escrow)
)
```

### Predicate

```text
current-age >= castle-age
```

### Mutation

```text
205 := without-escrow
```

### Static interpretation

W1 is a broad contextual writer. Once its predicate is true, the rule remains eligible unless some engine/rule lifecycle behavior prevents repeated firing.

It is located immediately before the `QSKIRMS` production policy. Its apparent role is to switch the default mode for the Castle-Age skirmisher decision section.

### Precedence

W1 precedes W2 and W3 by 61 and 68 source lines respectively. Therefore W1 is **earlier**, not later, than the restoration writers.

### Lifetime

The source does **not** contain a paired local reset of W1 to `with-escrow` within the same rule. Its persistence is therefore controlled by later writers, not by an explicit lifetime field.

**Status:** DIRECT / CONFIRMED for predicate and mutation; COMPOSED for mode-switch interpretation; RUNTIME-OPEN for persistence duration.

---

## 4. Writer W2 — post-training restoration

**Source line 15538:**

```text
(defrule
    (goal SPLIT 2)
=>
    (up-modify-goal gl-skirm-total c:+ 1)
    (up-train gl-escrow-state c: skirmisher-line)
    (set-goal gl-escrow-state with-escrow)
    (set-goal SPLIT 0)
)
```

### Predicate

```text
goal SPLIT == 2
```

### Operations, in source order

1. Increment `gl-skirm-total`.
2. Execute `up-train gl-escrow-state c: skirmisher-line`.
3. Set goal 205 to `with-escrow`.
4. Set `SPLIT` to 0.

### Static significance

W2 is the clearest **transaction-local restoration writer** in the six-writer set. The mode is consumed by the training command and then explicitly restored to `with-escrow` immediately afterward.

This strongly supports the following local sequence:

```text
SPLIT 2
  → escrow-aware skirmisher training
  → restore gl-escrow-state = with-escrow
  → SPLIT = 0
```

This is a source-level sequence, not proof that the engine samples goal 205 at exactly the intended point inside command execution.

---

## 5. Writer W3 — unconditional restoration / baseline reset

**Source line 15545:**

```text
(defrule
    (true)
=>
    (set-goal gl-escrow-state with-escrow)
    (set-goal SPLIT 0)
)
```

### Predicate

```text
true
```

### Mutation

```text
205 := with-escrow
SPLIT := 0
```

### Static significance

W3 is the most important precedence finding in the six-writer set.

It is:

- unconditional;
- immediately after W2;
- later than W1;
- a direct write to the same physical channel;
- another write of the same semantic value as W2, W4, W5, and W6.

Under ordinary source-order rule evaluation, W3 is therefore the strongest candidate for the **effective end-of-section baseline** for goal 205.

However, this must not be stated as engine-proven same-tick precedence until runtime qualification establishes:

- whether all eligible rules execute in source order;
- whether `set-goal` mutations are immediately visible to later rules in the same evaluation pass;
- whether rules are evaluated once or repeatedly within a cycle;
- whether an unconditional rule can fire repeatedly without an implicit rule cooldown;
- whether `SPLIT` mutation affects evaluation of neighboring rules during the same pass.

**Important:** W3 is not merely “another initialization.” Its position and unconditional predicate make it a **persistent baseline/reset candidate**.

---

## 6. Writer W4 — one-shot military initialization

**Source line 17855:**

```text
(defrule
    (true)
=>
    (set-strategic-number sn-enable-patrol-attack 1)
    (set-goal gl-escrow-state with-escrow)
    (disable-self)
)
```

### Predicate

```text
true
```

### Operations, in source order

1. Enable patrol attack.
2. Set goal 205 to `with-escrow`.
3. Disable this rule.

### Lifetime semantics

`disable-self` provides strong static evidence that the **writer rule itself is one-shot** after successful firing, unlike W3/W6 which have no local self-disable.

This does **not** prove that `gl-escrow-state` becomes permanently `with-escrow`. It only proves that W4 ceases to be an available writer after its own disable operation, subject to engine semantics.

W4 is therefore best classified as:

```text
ONE-SHOT INITIALIZATION / RESTORATION WRITER
```

rather than a persistent owner of the state.

---

## 7. Writer W5 — post-research restoration

**Source line 20301:**

```text
(defrule
    ;	(goal gl-progression-pause -1)
    (goal gl-current-build-item ESKIRMS)
    (or	(can-research ri-elite-skirmisher)
    (or	(can-research-with-escrow ri-elite-skirmisher)
    (up-can-research gl-escrow-state c: ri-elite-skirmisher)))
=>
    (up-research gl-escrow-state c: ri-elite-skirmisher)
    ;	(chat-to-player me "Elite Skirmishers")
    (set-goal gl-escrow-state with-escrow)
)
```

### Predicate set

The rule requires:

```text
gl-current-build-item == ESKIRMS
```

and at least one of:

```text
can-research ri-elite-skirmisher
can-research-with-escrow ri-elite-skirmisher
up-can-research gl-escrow-state c: ri-elite-skirmisher
```

### Mutation sequence

```text
up-research gl-escrow-state c: ri-elite-skirmisher
→ set-goal gl-escrow-state with-escrow
```

### Static significance

W5 is the research analogue of W2: it explicitly restores the mode after an escrow-aware transaction interface call.

Its write is contextual, not unconditional.

---

## 8. Writer W6 — farm-section unconditional restoration

**Source line 20897:**

```text
(defrule
    (true)
=>
    (set-goal gl-escrow-state with-escrow)
    (set-goal SPLIT 0)
)
```

### Predicate

```text
true
```

### Mutation

```text
205 := with-escrow
SPLIT := 0
```

### Static significance

W6 is structurally similar to W3 but occurs in the later farm section.

It therefore creates a second unconditional baseline writer after W3 and after W4/W5.

If the source is evaluated in ordinary top-to-bottom order, W6 is the **latest recovered unconditional writer** and therefore the strongest static candidate for the final `with-escrow` value whenever its rule is reached and fired.

Again, this is a source-order inference, not yet an engine-qualified same-pass guarantee.

---

## 9. Complete source-order graph

```text
Definition
  1571
    │
    ▼
W1 15477  current-age >= castle-age
    │      set 205 := without-escrow
    │
    ▼
W2 15538  SPLIT == 2
    │      up-train(...205...)
    │      set 205 := with-escrow
    │
    ▼
W3 15545  true
    │      set 205 := with-escrow
    │      set SPLIT := 0
    │
    │   [large donor source interval]
    ▼
W4 17855  true
    │      set 205 := with-escrow
    │      disable-self
    │
    │   [large donor source interval]
    ▼
W5 20301  current-build-item == ESKIRMS
    │      AND research feasibility
    │      up-research(...205...)
    │      set 205 := with-escrow
    │
    ▼
W6 20897  true
           set 205 := with-escrow
           set SPLIT := 0
```

### Static overwrite relationships

```text
W1(without)
   ├── may be overwritten by W2(with)
   ├── may be overwritten by W3(with)
   ├── may be overwritten by W4(with)
   ├── may be overwritten by W5(with)
   └── may be overwritten by W6(with)

W2(with)
   └── may be redundantly rewritten by W3(with)

W3(with)
   ├── may be redundantly rewritten by W4(with)
   ├── may be redundantly rewritten by W5(with)
   └── may be redundantly rewritten by W6(with)

W4(with)
   ├── may be redundantly rewritten by W5(with)
   └── may be redundantly rewritten by W6(with)

W5(with)
   └── may be redundantly rewritten by W6(with)
```

“May be overwritten” is intentionally weaker than “is overwritten.” The latter requires engine-qualified rule scheduling and proof that both writers execute in the relevant temporal window.

---

## 10. Effective-precedence reconstruction

### 10.1 Static precedence tiers

| Tier | Writer(s) | Predicate class | Static role |
|---|---|---|---|
| P1 | W1 | contextual | establishes `without-escrow` after Castle Age |
| P2 | W2 | contextual | restores `with-escrow` after skirmisher transaction |
| P3 | W3 | unconditional | immediate later baseline/reset candidate |
| P4 | W4 | unconditional + self-disable | one-shot military baseline |
| P5 | W5 | contextual | restores `with-escrow` after elite-skirmisher research |
| P6 | W6 | unconditional | latest recovered baseline/reset candidate |

### 10.2 Value-level precedence

There is an important asymmetry:

```text
WITHOUT-ESCROW: W1 only
WITH-ESCROW:    W2, W3, W4, W5, W6
```

Consequently, the six-writer system has **one exceptional mode writer and five restoration/baseline writers**.

This means the donor does not exhibit symmetric mode arbitration. It exhibits a **temporary exception (`without-escrow`) surrounded by repeated restoration to `with-escrow`**.

That is a stronger and more useful reconstruction than simply saying “multiple writers exist.”

---

## 11. Reset behavior

### Explicit resets recovered

There is no recovered operation equivalent to:

```text
set-goal gl-escrow-state undefined
set-goal gl-escrow-state 0
clear-goal gl-escrow-state
```

The only explicit alternate-state reset is:

```text
W1: set-goal gl-escrow-state without-escrow
```

The remaining five writers restore:

```text
with-escrow
```

Therefore the state machine is not:

```text
UNINITIALIZED → WITH → WITHOUT → UNINITIALIZED
```

The recovered source instead supports:

```text
WITH-ESCROW
    │
    │ W1 after Castle Age
    ▼
WITHOUT-ESCROW
    │
    ├── W2 contextual restoration
    ├── W3 unconditional restoration
    ├── W4 one-shot restoration
    ├── W5 contextual restoration
    └── W6 unconditional restoration
    ▼
WITH-ESCROW
```

Whether W1 is intended as a persistent Castle-Age mode or a temporary mode overridden by later sections is **not fully resolvable from the six write sites alone**.

---

## 12. Lifetime model

The donor does not attach an explicit epoch, TTL, or expiration field to goal 205. Its lifetime is therefore **writer-defined and event-defined**.

### W1 lifetime

```text
activation: current-age >= castle-age
termination: next successful writer of goal 205
```

This is the most defensible static lifetime model.

### W2 lifetime

```text
activation: SPLIT == 2
termination: next writer of goal 205
```

W2 also sets `SPLIT := 0`, reducing the local likelihood of immediate repeated W2 firing.

### W3 lifetime

```text
activation: true
termination: next writer / next evaluation state
```

Because W3 has no self-disable or contextual predicate, it is a persistent baseline candidate.

### W4 lifetime

```text
activation: true
termination of writer availability: disable-self
```

The **rule** is explicitly one-shot. The value it writes may persist after the rule disables itself.

### W5 lifetime

```text
activation: ESKIRMS work item + research feasibility
termination: next writer of goal 205
```

### W6 lifetime

```text
activation: true
termination: next writer / next evaluation state
```

Like W3, W6 is an unconditional baseline candidate, but it is later in the source.

---

## 13. Critical precedence question: can W1 actually persist?

The central unresolved question is not whether W1 writes `without-escrow` — that is proven.

The unresolved question is:

> **For how long does W1's `without-escrow` value remain observable to downstream escrow-aware commands?**

There are three plausible source-level regimes:

### Regime A — same-pass later overwrite

```text
W1 fires
→ 205 = without
→ W2/W3 or another later writer fires
→ 205 = with
```

In this regime, `without-escrow` is short-lived.

### Regime B — conditional persistence

```text
W1 fires
→ 205 = without
→ W2/W3 do not execute in the relevant temporal window
→ downstream commands observe without
```

In this regime, W1 is an effective mode switch until a later restoration occurs.

### Regime C — rule scheduling prevents immediate overwrite

The engine may evaluate rules in a manner where source adjacency does not imply immediate same-pass overwrite. In that case, W1's lifetime depends on rule scheduling details not recoverable from static source order alone.

**Runtime qualification is therefore required before AEGIS treats W1 as a usable persistent mode transition.**

---

## 14. Relationship to `up-jump-rule`

The donor's nearby skirmisher section contains jump rules that suppress later production logic:

```text
(up-jump-rule 2)
(up-jump-rule 1)
```

These occur between W1 and W2/W3.

They are therefore relevant to precedence reconstruction because they may alter which subsequent rules execute, but the six writer sites themselves do not contain an explicit `up-jump-rule` operation.

The safe conclusion is:

- W1's predicate is directly proven.
- W2/W3 are directly proven later writes.
- Nearby jump rules are evidence that rule-flow suppression exists in this region.
- It is **not proven solely from these excerpts** that either jump suppresses W2 or W3.
- A complete jump graph is required before assigning a jump-mediated precedence edge.

This distinction prevents a false conclusion that “W1 is immediately reset” merely because jump operations exist nearby.

---

## 15. Authority interpretation

The six writers should **not** be implemented as six independent authorities in AEGIS.

The correct abstraction is:

```text
                    SHADOW TRANSACTION MODE
                            │
                    gl-escrow-state / 205
                            │
             ┌──────────────┴──────────────┐
             │                             │
      temporary exception             baseline mode
       WITHOUT-ESCROW                  WITH-ESCROW
             │                             │
             └────────── restoration ──────┘
```

The donor's physical writer multiplicity is an implementation artifact. AEGIS should expose one semantic state owner and explicit mutation reasons:

```text
SET_MODE_WITHOUT_ESCROW(reason, transaction_context)
SET_MODE_WITH_ESCROW(reason, restoration_context)
```

The `.per` implementation may retain multiple physical writes only if their ownership and precedence are explicitly registered.

---

## 16. Required AEGIS writer metadata

Every future physical write to goal 205 must be registered with:

```text
writer_id
source_file
source_line
predicate
value
reason
transaction_or_context
precedence_class
can_repeat
self_disable
expected_lifetime
allowed_overwriters
verification_requirement
runtime_status
```

The six donor writers map as follows:

| Writer | Precedence class | Repeatability | Semantic reason |
|---|---|---|---|
| W1 | contextual exception | potentially repeatable | switch to `without-escrow` |
| W2 | transaction restoration | bounded by `SPLIT` | restore after skirmisher training |
| W3 | unconditional baseline | potentially repeatable | baseline reset to `with-escrow` |
| W4 | one-shot initialization | self-disabled | military initialization/restoration |
| W5 | transaction restoration | contextual | restore after elite-skirmisher research |
| W6 | unconditional baseline | potentially repeatable | farm-section baseline/reset |

---

## 17. Runtime qualification requirements

Before promoting the precedence model from STATIC-QUALIFIED to RUNTIME-QUALIFIED, establish:

1. exact rule evaluation order;
2. whether source order is execution order;
3. whether goal writes are visible immediately to later rules in the same pass;
4. whether unconditional rules fire every cycle or have implicit one-shot behavior;
5. whether W3 can overwrite W2 in the same cycle;
6. whether W6 can overwrite W5 in the same cycle;
7. whether `disable-self` takes effect before or after remaining rules in the current pass;
8. whether `up-jump-rule` can suppress any of W2/W3/W4/W5/W6;
9. whether `without-escrow` is actually observed by any downstream executor before restoration;
10. the exact engine semantics of the `EscrowState` parameter;
11. whether a goal write itself has any hidden transactional delay;
12. whether goal 205 survives across rule cycles unchanged when no writer fires.

The highest-value probe is therefore **not** “does `set-goal` work?” It is:

```text
W1 writes WITHOUT
→ immediately attempt an escrow-aware command
→ observe command interpretation
→ observe economic consequence
→ determine whether W3/W6 overwrite before consumption
→ repeat across cycles
```

---

## 18. Final forensic verdict

**DIRECT / CONFIRMED:**

- goal 205 is `gl-escrow-state`;
- six direct writers exist;
- W1 is the only direct writer assigning `without-escrow`;
- W2–W6 assign `with-escrow`;
- W1 requires Castle Age;
- W2 requires `SPLIT == 2`;
- W3 and W6 are unconditional;
- W4 is unconditional and self-disables;
- W5 requires `ESKIRMS` work-item context plus research feasibility;
- no direct undefined/neutral clear was recovered.

**COMPOSED / PROBABLE:**

- W2 is a transaction-local restoration;
- W3 is an unconditional baseline reset;
- W4 is one-shot initialization/restoration;
- W5 is a transaction-local restoration;
- W6 is a later unconditional baseline reset;
- `without-escrow` behaves as a temporary exception to a dominant `with-escrow` baseline.

**INFERRED / RUNTIME-OPEN:**

- exact same-pass winner;
- whether W3 overwrites W2 before downstream consumers;
- whether W6 overwrites W5 before downstream consumers;
- actual duration of the `without-escrow` interval;
- whether W1 has strategic significance or is merely a local executor-mode adjustment;
- exact jump-mediated suppression relationships.

### Engineering conclusion

The six-writer problem is no longer a **writer-discovery problem**. It is a **precedence, lifetime, and consumption-window problem**.

The next implementation gate is therefore:

```text
WRITER INVENTORY
      ↓
SOURCE-ORDER GRAPH
      ↓
PREDICATE / JUMP GRAPH
      ↓
EFFECTIVE-WINNER MODEL
      ↓
CONSUMPTION-WINDOW ANALYSIS
      ↓
RUNTIME ABI QUALIFICATION
      ↓
AUTHORITATIVE AEGIS MODE CONTRACT
```

Until that chain is qualified, `gl-escrow-state` may be treated as a statically established mode carrier, but its `without-escrow` persistence must remain **RUNTIME-OPEN**.
