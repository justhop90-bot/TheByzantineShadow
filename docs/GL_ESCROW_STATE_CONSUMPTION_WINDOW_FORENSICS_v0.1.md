# `gl-escrow-state` Consumption-Window Forensics v0.1

**Repository:** `justhop90-bot/TheByzantineShadow`  
**Source:** `SourceShaRef`, blob `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Scope:** W1–W6 writers of `gl-escrow-state` / goal 205; nearby consumers and jump/suppression paths  
**Status:** STATIC-QUALIFIED / RUNTIME-OPEN  
**Evidence discipline:** DIRECT facts are separated from engine-dependent inference. No command acceptance is promoted to completion or strategic effect.

## 1. Executive finding

The jump/suppression audit does **not** establish a direct jump path that prevents W1, W2, W3, W4, W5, or W6 from firing. The important unresolved issue is therefore not jump targeting but **consumption timing**: whether a consumer of `gl-escrow-state` samples the value written by W1 before a later writer restores `with-escrow`.

Static source order establishes the following writer sequence:

`W1 15477 → W2 15538 → W3 15545 → W4 17855 → W5 20301 → W6 20897`.

W1 is the only writer of `without-escrow`; W2–W6 write `with-escrow`.

The strongest local candidate for observing W1's `without-escrow` state is a consumer located **after W1 but before W2/W3**. However, source order alone cannot prove whether the engine evaluates a later rule in the same pass against a goal value mutated by an earlier rule, nor whether rule jumps alter the set/order of rules subsequently evaluated.

## 2. Writer topology

| ID | Source line | Predicate | Mutation | Local control effect | Static interpretation |
|---|---:|---|---|---|---|
| W1 | 15477 | `current-age >= castle-age` | `gl-escrow-state := without-escrow` | none | contextual exception/mode switch |
| W2 | 15538 | `goal SPLIT == 2` | `up-train(gl-escrow-state, skirmisher-line)` then `:= with-escrow`, `SPLIT := 0` | none | transaction-local restoration |
| W3 | 15545 | `true` | `:= with-escrow`, `SPLIT := 0` | none | unconditional baseline/reset candidate |
| W4 | 17855 | `true` | `:= with-escrow` | `disable-self` | one-shot initialization/restoration |
| W5 | 20301 | `current-build-item == ESKIRMS` plus research feasibility | `up-research(gl-escrow-state, ri-elite-skirmisher)` then `:= with-escrow` | none | transaction-local restoration |
| W6 | 20897 | `true` | `:= with-escrow`, `SPLIT := 0` | none | unconditional baseline/reset candidate |

## 3. W1 neighborhood: exact control path

The source ordering around W1 is:

```text
W1 @ 15477
  current-age >= castle-age
  → set-goal gl-escrow-state without-escrow

nearby skirmisher suppression rule
  → up-jump-rule 2

nearby skirmisher suppression rule
  → up-jump-rule 1

skirmisher production state machine
  → SPLIT := 1
  → SPLIT := 2

W2 @ 15538
  goal SPLIT == 2
  → up-train gl-escrow-state skirmisher-line
  → set-goal gl-escrow-state with-escrow
  → SPLIT := 0

W3 @ 15545
  true
  → set-goal gl-escrow-state with-escrow
  → SPLIT := 0
```

The two `up-jump-rule` operations are attached to skirmisher policy predicates. They do not test or mutate `gl-escrow-state`, and no direct target relationship to any W1–W6 writer is established by the source.

**Consequence:** W1 occurs before the nearby jumps, so those jumps cannot suppress W1. W2/W3 occur later, but no source-level evidence identifies either as a jump target. Generic engine jump semantics remain an ABI/runtime question.

## 4. Consumption-window model

There are three distinct static windows that must not be conflated:

### Window A — pre-W1

Consumers before line 15477 necessarily see the pre-existing value of goal 205, subject to engine initialization semantics.

No statement about W1 can be made from this window.

### Window B — W1 → W2/W3

This is the critical window:

```text
205 := WITHOUT
      │
      ├── possible escrow-aware predicates/commands
      │
      └── W2 / W3 restoration
              │
              ▼
          205 := WITH
```

If the engine exposes goal mutations to subsequent rule evaluation in the same relevant evaluation cycle, a consumer in Window B can potentially observe `without-escrow`.

If the engine snapshots goals before evaluating the rule set, or otherwise delays visibility, the static source order does not establish that observation.

### Window C — W3 onward

After W3, static source order contains repeated `with-escrow` writes. Any later escrow-aware consumer cannot be shown from source order alone to observe W1's `without-escrow` state.

## 5. Transaction-local evidence

W2 is the strongest direct evidence that the donor treats `gl-escrow-state` as transaction state rather than a permanently selected global policy:

```text
SPLIT == 2
    ↓
up-train gl-escrow-state skirmisher-line
    ↓
set-goal gl-escrow-state with-escrow
    ↓
SPLIT := 0
```

The order is significant. The restoration occurs **after** the escrow-aware training command in the same rule body. This supports, but does not by itself prove, a design in which the executor samples the current goal during `up-train` and the subsequent write restores the normal mode.

The remaining uncertainty is engine evaluation semantics, not donor source order.

## 6. W3: why it matters

W3 immediately follows W2 and is unconditional. Consequently, any interpretation that requires `without-escrow` to persist through multiple subsequent rule evaluations must account for W3.

Static evidence supports two possibilities:

1. **Persistent baseline interpretation:** W3 executes as a normal unconditional rule and repeatedly restores `with-escrow`; W1 is therefore a temporary exception whose useful lifetime is bounded by later rule evaluation.
2. **Same-pass transaction interpretation:** W1 can affect one or more earlier/later rules during a pass before W3 restores the value.

The source alone cannot choose between these runtime models.

## 7. W4, W5, W6 consumption implications

W4 is an unconditional one-shot writer that sets `with-escrow` and disables itself. Its disabling operation proves only that W4's rule is no longer eligible after successful execution; it does not establish expiration of goal 205.

W5 explicitly performs an escrow-aware elite-skirmisher research command and then restores `with-escrow`. This is another direct transaction-local pattern.

W6 is another unconditional `with-escrow` writer in the farm subsystem. It reinforces the conclusion that the donor repeatedly restores a normal escrow mode rather than maintaining a symmetric two-state arbitration system.

## 8. Jump/suppression findings

### Direct suppression of writers

No direct source-level jump-to-writer relationship was recovered for W1–W6.

| Writer | Direct `up-jump-rule` suppression recovered? |
|---|---|
| W1 | NO |
| W2 | NO |
| W3 | NO |
| W4 | NO |
| W5 | NO |
| W6 | NO |

### What the jumps actually establish

The nearby jumps belong to skirmisher production policy. They encode suppression of lower-priority production branches under strategic/resource conditions. They do not form an escrow authority mechanism.

Therefore it would be incorrect to label the jumps as the cause of W1's apparent short lifetime without runtime evidence.

## 9. Required runtime qualification

The next qualification should be a **single-pass visibility experiment**, not another broad static search.

The experiment must distinguish at least these hypotheses:

```text
H1: W1 write is visible to a subsequent escrow-aware predicate/command
    before W3 restores WITH.

H2: W1 write is not visible until a later evaluation phase, so W3
    effectively neutralizes it before relevant consumers sample it.

H3: jump processing changes rule traversal such that the apparent
    source-order window is not the actual consumption window.
```

The probe should instrument only existing goal/state telemetry and an otherwise harmless escrow-aware predicate/command path. It must separately record:

- W1 eligibility and execution;
- observed goal 205 value immediately after W1;
- any Window-B `up-can-*` evaluation;
- any Window-B `up-*` command;
- W2 execution;
- W3 execution;
- first later observation of goal 205 as `with-escrow`;
- whether either `up-jump-rule 1/2` changes traversal of W2/W3.

A successful command is W0/W1 evidence only. A change in actual affordability/resource accounting requires independent world-state evidence.

## 10. Evidence classification

| Finding | Evidence level | Status |
|---|---|---|
| Six direct writers exist | DIRECT | CONFIRMED |
| Writer source ordering | DIRECT | CONFIRMED |
| W1 is the only `without-escrow` writer | DIRECT | CONFIRMED |
| W2 restores after `up-train` | DIRECT | CONFIRMED |
| W3 is unconditional | DIRECT | CONFIRMED |
| W4 is one-shot via `disable-self` | DIRECT | CONFIRMED |
| W5 restores after `up-research` | DIRECT | CONFIRMED |
| W6 is unconditional | DIRECT | CONFIRMED |
| Nearby jumps are skirmisher-policy suppression | DIRECT/COMPOSED | CONFIRMED |
| Jumps directly suppress W1–W6 | DIRECT | NOT RECOVERED |
| W1 is actually consumed before W3 | INFERRED | RUNTIME OPEN |
| W3 makes W1 semantically ineffective | INFERRED | RUNTIME OPEN |
| Same-pass goal visibility | ENGINE-SPECIFIC | RUNTIME OPEN |
| Actual escrow/resource consequence | W2+ | RUNTIME OPEN |

## 11. For AEGIS

Do **not** transplant W1–W6 as six independent authorities.

The donor evidence supports a cleaner abstraction:

```text
ESCROW MODE
    │
    ├── BASELINE: WITH
    │
    └── TEMPORARY EXCEPTION: WITHOUT
             │
             └── bounded transaction/consumer window
```

The authoritative AEGIS implementation should therefore define explicitly:

- owner;
- mode generation/epoch;
- activation predicate;
- consumption boundary;
- expiry/restore condition;
- executor sampling point;
- verification source;
- recovery if execution fails;
- precedence relative to strategic and safety authorities.

The donor's repeated `with-escrow` writes are evidence of a transaction convention, not sufficient evidence for an AEGIS state-machine implementation.

## 12. Final disposition

**STATIC JUMP FORENSICS: CLOSED.** No direct jump path to W1–W6 was established.

**STATIC CONSUMPTION FORENSICS: QUALIFIED BUT NOT CLOSED.** The critical W1→consumer→W2/W3 window is identified, but actual goal visibility and traversal order remain engine-dependent.

**NEXT GATE:** runtime qualification of same-pass goal visibility and executor sampling for `gl-escrow-state` (goal 205).
