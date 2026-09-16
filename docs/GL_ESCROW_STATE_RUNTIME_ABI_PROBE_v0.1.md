# `gl-escrow-state` Runtime ABI Probe v0.1

**Repository:** `justhop90-bot/TheByzantineShadow`  
**Subject:** `gl-escrow-state` / goal 205  
**Runtime target:** AoE2DE 101.103.48987.0 / BuildID 24094652  
**Status:** PROBE-SPECIFICATION / NOT-RUNTIME-QUALIFIED

## 1. Purpose

This probe isolates the unresolved runtime semantics of donor goal 205. Static archaeology has established six direct writers, their source ordering, and the critical W1→W2→W3 consumption window. It has **not** established same-pass mutation visibility, executor sampling semantics, or the effect of `up-jump-rule` on traversal.

The probe therefore separates four questions that must not be conflated:

1. Does a `set-goal` mutation become visible to a later goal predicate?
2. Does an `up-can-*` consumer sample the mutated goal value?
3. Does the donor-shaped W1→W2→W3 window expose `without-escrow` to its consumer?
4. Can jump traversal suppress or bypass the consumer?

A command being accepted is W0/W1 evidence only. It is not proof of resource mutation, completion, capability, or strategic effect.

## 2. Safety constraints

- Do not modify the untouched stock AI installation.
- Do not transplant the complete donor production section into the probe.
- Do not use real economy outcomes as the primary ABI signal.
- Do not assume diagnostic goal numbers are globally free merely because repository search finds no textual declaration.
- Diagnostic goals must be selected from a namespace audit of the actual loaded AI.
- The fixture must be independently removable after qualification.
- Record raw observations before assigning an interpretation.

## 3. Diagnostic contract

The fixture requires:

```text
TARGET_GOAL = 205
PROBE_WRITER_FLAG
PROBE_READER_FLAG
PROBE_STAGE
PROBE_JUMP_FLAG
```

The diagnostic channels are placeholders until the loaded AI's goal namespace is audited. They must not be hard-coded to arbitrary numbers solely for convenience.

The target values are:

```text
without-escrow
with-escrow
```

## 4. Test A — pure mutation visibility

Minimal topology:

```text
R1: set 205 := without-escrow; mark WRITER
R2: if 205 == without-escrow; mark READER
```

### Question

Can a later rule predicate observe a goal mutation performed by an earlier rule in the same relevant evaluation interval?

### Positive observation

```text
WRITER observed
READER observed with 205 == WITHOUT
```

This establishes goal-predicate visibility only.

### Negative observation

A missing reader does **not** alone prove invisibility. It can also result from scheduling, rule eligibility, diagnostic collision, or an evaluation model in which the relevant rules were not traversed.

## 5. Test B — executor sampling

Topology:

```text
R1:
    set 205 := without-escrow
    mark WRITER

R2:
    ordinary predicate confirms 205 == without-escrow
    controlled escrow-aware up-can-* operation samples goal 205
```

The controlled operation must use a known-valid, harmless operation and must not rely on an actual economic consequence as the ABI signal.

Record separately:

```text
ordinary goal predicate sees WITHOUT: YES/NO
up-can-* samples WITHOUT: YES/NO/UNRESOLVED
```

This distinguishes goal-language visibility from the executor's parameter sampling behavior.

## 6. Test C — donor-shaped consumption window

Reproduce only the local semantic topology established by the donor:

```text
W1'
    predicate becomes true
    set 205 := without-escrow

C'
    test 205 == without-escrow
    mark CONSUMER

W2'
    controlled up-train(205, known-unit)
    set 205 := with-escrow

W3'
    unconditional set 205 := with-escrow
```

The essential observation is whether `C'` executes **after W1' and before restoration** while observing `without-escrow`.

The real donor establishes the analogous W2 ordering as:

```text
up-train gl-escrow-state c: skirmisher-line
set-goal gl-escrow-state with-escrow
set-goal SPLIT 0
```

and W3 immediately follows as an unconditional restoration rule.

### Interpretation

| Observation | Interpretation |
|---|---|
| C' fires and sees WITHOUT | same-pass goal visibility demonstrated for this topology |
| C' absent; removing intervening jump makes it fire | traversal suppression demonstrated |
| C' absent with and without jump | scheduling/visibility remains unresolved; inspect rule eligibility and sampling |
| C' fires but sees WITH | another writer or evaluation phase intervened |

## 7. Test D — jump traversal isolation

First establish a control pair:

```text
R1 → R2
```

Then the jump pair:

```text
R1 → up-jump-rule N → R2
```

Record whether R2 executes.

Repeat with the controlled goal-205 consumer occupying R2.

The test must establish traversal behavior independently of escrow semantics before combining the two.

## 8. Combined donor-shaped jump case

Only after Test D is understood, reproduce:

```text
E1: 205 := WITHOUT
E2: up-jump-rule N
E3: consumer tests 205 == WITHOUT
E4: 205 := WITH
```

The comparison is:

```text
NO-JUMP:  E1 → E3 → E4
JUMP:     E1 → E2 → E3 → E4
```

A difference in E3 execution is evidence about traversal, not automatically evidence about goal lifetime.

## 9. Required telemetry

Every probe event should record, at minimum:

```text
runtime timestamp / tick if available
probe rule identifier
probe stage
writer flag
reader flag
jump flag
observed 205 value
operation attempted
operation result, if exposed
```

The resulting chronology must be reconstructable without relying on the AI's chat output.

## 10. Evidence classification

| Proposition | Initial status |
|---|---|
| Goal 205 is a writable state carrier | DIRECT / CONFIRMED |
| Six donor writers exist | DIRECT / CONFIRMED |
| W1 precedes W2/W3 in source | DIRECT / CONFIRMED |
| W2 restores after `up-train` | DIRECT / CONFIRMED |
| W3 is unconditional | DIRECT / CONFIRMED |
| Goal mutation is visible to a later predicate | ENGINE-SPECIFIC / OPEN |
| `up-can-*` samples the current goal value | ENGINE-SPECIFIC / OPEN |
| W1's `without-escrow` is consumed before W2/W3 | INFERRED / OPEN |
| Jump suppresses the relevant consumer | ENGINE-SPECIFIC / OPEN |
| Actual escrow resource consequence | W2+ / OPEN |

## 11. Promotion rules

Do not promote the state merely because a probe rule fired.

Promotion requires the evidence appropriate to the claim:

```text
W0: command/rule activity observed
W1: pending/accepted transaction evidence
W2: independently observed world-state consequence
W3: demonstrated capability consequence
W4: demonstrated strategic effect
```

For the ABI gate, the primary target is **engine behavior**, not strategic outcome.

## 12. Qualification matrix

| ABI property | Required test | Gate |
|---|---|---|
| Mutation visibility | A | Q14 |
| Same-pass visibility | A + chronology | Q14 |
| Predicate sampling | A | Q14 |
| `up-can-*` sampling | B | Q14 |
| `up-*` sampling | C | Q14 |
| W1 consumption window | C | Q7/Q14 |
| Jump traversal | D | Q14 |
| Jump suppression of consumer | D + combined case | Q14 |
| Restoration W2→W3 | C | Q7/Q11 |
| Resource consequence | independent world-state evidence | Q9/Q11 |

## 13. Stop condition

Once the four ABI questions are decisively answered, stop runtime probing of goal 205 unless a contradiction appears in donor behavior.

The result should then update:

- `docs/GL_ESCROW_STATE_FORENSIC_TRACE_v0.1.md`
- `docs/GL_ESCROW_STATE_PRECEDENCE_AND_LIFETIME_FORENSICS_v0.1.md`
- `docs/SHARED_STATE_WRITER_READER_AUTHORITY_REGISTRY_v0.3.md`

The purpose of this probe is to close an engine-semantics question, not to create a permanent diagnostic subsystem.

## 14. Final disposition before execution

**STATIC JUMP FORENSICS:** CLOSED.  
**STATIC CONSUMPTION WINDOW:** IDENTIFIED / RUNTIME OPEN.  
**GOAL-205 RUNTIME ABI:** NOT QUALIFIED.  
**Next action:** namespace-safe fixture construction followed by the four isolated runtime cases above.
