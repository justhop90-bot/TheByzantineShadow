# Production-Demand Interface v0.1

## Status

**PROPOSED CONTRACT — not yet wired into runtime production rules.**

The purpose of this interface is to separate **composition policy** from **Production Authority**.

Composition policy decides **what military capability should exist**. Production Authority decides **whether, when, and how that request becomes an engine transaction**.

The contract deliberately does not make composition policy responsible for escrow, affordability, buildings, training queues, or execution.

---

## 1. Authority Boundary

```text
COMPOSITION POLICY
        |
        | requested unit target
        v
PRODUCTION-DEMAND INTERFACE
        |
        | target / withdrawal / status
        v
PRODUCTION AUTHORITY
        |
        +--> prerequisite reservation
        +--> capital posture
        +--> engine feasibility
        +--> escrow admission
        +--> training/build execution
        +--> queued-unit accounting
        +--> completion detection
        +--> escrow release
        |
        v
WORLD STATE
```

### Composition policy owns

- desired unit type or production line;
- desired target count;
- strategic reason for the demand;
- priority among competing demands, when such arbitration is eventually exposed;
- withdrawal/reduction of a demand.

### Production Authority owns

- translating a target into an executable production commitment;
- prerequisite buildings;
- resource reservation;
- escrow percentage/posture;
- affordability checks;
- training-site readiness;
- `up-can-train` / `up-train` admission and execution;
- pending/queued accounting;
- completion detection;
- release of escrow owned by the commitment;
- commitment lifecycle and recovery.

Composition policy **must not** call `build`, `train`, `up-build`, `up-train`, `set-escrow-percentage`, or `release-escrow` as part of this interface.

---

## 2. The Core Semantic Contract

A production request means:

> Maintain at least N units of the requested production target, counting the engine's pending/queued units according to the authoritative `*-count-total` semantics.

It does **not** mean:

> Train N units immediately.

That distinction is fundamental. A target is a **requirement**, not an execution command.

For a target `T` and requested count `N`:

```text
CURRENT + QUEUED >= N
        => demand satisfied

CURRENT + QUEUED < N
        => production authority may create a commitment
```

The interface therefore expresses **desired state**, while Production Authority implements the transition toward that state.

AIRef documents `unit-type-count-total` as including trained and queued units; UserPatch release notes specifically establish that the `*-count-total` family includes pending training. citehttps://airef.github.io/commands/commands-index.htmlhttps://airef.github.io/tables/up-patch-notes.html

---

## 3. v0.1 Request Model

The initial interface should expose three semantic fields per production request:

| Field | Meaning | Writer | Reader |
|---|---|---|---|
| `TARGET` | desired quantity | Composition Policy | Production Authority |
| `ACTIVE` | whether the request currently exists | Composition Policy | Production Authority |
| `STATUS` | lifecycle of the authority's response | Production Authority | Composition Policy / verification |

The important rule is that **STATUS is read-only to policy**.

Policy requests a target. Authority reports what happened to that request.

---

## 4. Target Namespace

v0.1 should not create an arbitrary dynamic unit-ID executor. The first implementation should use explicit production slots whose unit identity is statically known.

Recommended initial slots:

| Slot | Production target | Target goal | Purpose |
|---|---|---:|---|
| P1 | `spearman-line` | Shadow production target | infantry / anti-cavalry baseline |
| P2 | `archer-line` | future target | ranged mass |
| P3 | `skirmisher-line` | future target | anti-ranged mass |
| P4 | cavalry line | future target | mobility / anti-archer / power unit |
| P5 | siege line | future target | siege capability |
| P6 | defensive/other line | future target | civilization-specific extension |

The interface is therefore **generic at the policy boundary but explicit at the executor boundary**.

This is intentional. AoE2 `.per` is not a general-purpose object-oriented runtime. Static slot identity provides a defensible contract without introducing an unverified indirect-dispatch mechanism.

AIRef establishes that unit identifiers are engine-defined object/unit identifiers and that `up-train` accepts a unit ID dynamically; however, the production executor should only generalize dynamic dispatch after the exact goal/operator form has been directly qualified in the Shadow runtime. citehttps://airef.github.io/parameters/parameters-index.htmlhttps://airef.github.io/commands/commands-index.html

---

## 5. Lifecycle

Each slot has the following conceptual lifecycle:

```text
INACTIVE
   |
   | policy writes ACTIVE + TARGET
   v
REQUESTED
   |
   | authority accepts demand
   v
RESERVING
   |
   | prerequisite/capital requirements satisfied
   v
ADMITTED
   |
   | engine feasibility + site readiness
   v
EXECUTING
   |
   | queued/current count reaches target
   v
SATISFIED
   |
   | policy withdraws/reduces target
   v
INACTIVE / RESERVING
```

A failed transaction is not silently equivalent to completion:

```text
RESERVING / ADMITTED / EXECUTING
          |
          v
        FAILED
          |
          v
       RECOVERY
          |
          v
       RESERVING
```

The authority must distinguish **command issued** from **world state achieved**.

---

## 6. Target Semantics

Targets are absolute desired quantities, not production increments.

Example:

```text
Policy target = 8 spearmen
Current + queued = 3
Authority deficit = 5
```

If two more are queued:

```text
Current + queued = 5
Authority deficit = 3
```

If eight are queued/completed in total:

```text
Current + queued = 8
Authority status = SATISFIED
```

The authority must **not** blindly train the difference every rule pass. It must test the live total each pass.

This preserves idempotence at the demand level: repeatedly observing the same target does not create an ever-growing production queue once the target is met.

---

## 7. Target Reduction / Withdrawal

Policy may reduce a target at any time.

Example:

```text
TARGET = 8
CURRENT + QUEUED = 5
```

Policy changes the request to:

```text
TARGET = 3
```

Production Authority must not interpret this as an instruction to cancel already-issued training automatically.

Instead:

```text
CURRENT + QUEUED >= TARGET
        => demand becomes SATISFIED
        => authority releases unused reservation
```

Cancellation is a separate capability and must not be smuggled into the target interface.

This distinction matters because `up-reset-building` can cancel training, but cancellation is a consequential executor action and therefore requires its own authority contract. citehttps://airef.github.io/tables/up-patch-notes.html

---

## 8. Reservation Semantics

The target interface does **not** reserve resources.

Production Authority derives the economic requirement from the engine's actual object costs.

For a requested target:

```text
TARGET
  -> ENGINE COST VECTOR
  -> REQUIRED CAPITAL
  -> SHADOW RESERVATION
  -> PHYSICAL ESCROW
```

The production module may use `up-setup-cost-data`, `up-add-object-cost`, and `up-get-cost-delta` to derive cost information. UserPatch explicitly defines the four-goal cost-data order as food, wood, stone, gold and documents `up-add-object-cost` for dynamically constructing cost sets. citehttps://airef.github.io/tables/up-patch-notes.html

The interface must therefore never contain manually maintained food/wood/gold prices for units.

---

## 9. Escrow Semantics

Escrow is a physical economic mechanism owned by Production Authority.

Policy may say:

```text
TARGET = 8 spearmen
```

Policy must not say:

```text
set food escrow = 35%
release wood escrow
```

Production Authority determines the resource posture from the production transaction.

This preserves the Shadow distinction between strategic intent and economic machinery. The preserved Shadow corpus contains explicit escrow constants and selectively releases resource escrow rather than treating escrow as a universal strategic switch.

The active Shadow repository also explicitly separates strategic reserve from engine escrow in its reserve architecture. fileciteturn389file0

---

## 10. Admission Contract

A production request can only transition from reservation toward execution when the authority has independently established:

1. target is still active;
2. target deficit still exists;
3. required prerequisite exists or can be legally created;
4. prerequisite construction is not already pending;
5. required capital is available through the authority's escrow posture;
6. the training site is ready when applicable;
7. `up-can-train` or the appropriate engine feasibility predicate succeeds.

`up-train-site-ready` is specifically documented as a training-site readiness test that does not test cost or unit availability; UserPatch explicitly requires the root unit type rather than a line/class for this fact. citeturn0search0

Therefore:

```text
SITE READY != AFFORDABLE != AUTHORIZED
```

All three must remain conceptually distinct.

---

## 11. Execution Contract

Production Authority is the only module permitted to cross from logical commitment into physical production.

For training:

```text
TARGET DEFICIT
    ↓
RESERVATION
    ↓
SITE READY
    ↓
UP-CAN-TRAIN
    ↓
RELEASE COMMITTED CAPITAL
    ↓
UP-TRAIN
    ↓
OBSERVE QUEUED/CURRENT TOTAL
```

The release and execution operations should remain adjacent in the same rule when they represent one transaction boundary, as in the current Shadow production implementation.

The current `05_production.per` already follows this philosophy for its Spearman commitment: it gates training on explicit production state, site readiness, and `up-can-train`, then releases the resource escrow immediately before `up-train`. That existing pattern is the implementation substrate for this interface.

---

## 12. Completion Contract

Completion is observed from world state, not inferred from issuing a command.

For each request:

```text
unit-type-count-total TARGET >= REQUESTED-TARGET
        => SATISFIED
```

Because `unit-type-count-total` includes queued units, the interface treats a successfully admitted queue position as satisfying the requested production quantity. This is appropriate for the demand contract because the request is for production commitment, not for a completed-body-only military assessment.

A future military/verification layer may separately distinguish:

```text
QUEUED TARGET
vs.
COMPLETED TARGET
vs.
SURVIVING TARGET
```

Those are different measurements and should not be collapsed into this production interface.

---

## 13. Priority and Arbitration

v0.1 intentionally does **not** allow every composition policy to directly seize production.

If multiple policies request:

```text
6 spearmen
4 archers
3 skirmishers
```

Production Authority should eventually receive an **arbitrated target set**, not three independent execution commands.

Recommended future flow:

```text
THREAT / STRATEGY MODULES
        |
        v
COMPOSITION DEMANDS
        |
        v
COMPOSITION ARBITRATOR
        |
        v
FINAL PRODUCTION TARGETS
        |
        v
PRODUCTION AUTHORITY
```

This prevents the common failure mode where several strategic modules independently issue production orders and the executor becomes the accidental arbitrator.

The production executor should never decide strategy merely because it received multiple requests.

---

## 14. Interface Invariants

The implementation should be rejected if it violates any of these invariants:

### I1 — Policy cannot execute
Composition policy writes targets only.

### I2 — Authority owns escrow
Only Production Authority changes production-owned escrow posture.

### I3 — Target is absolute
Targets describe desired quantity, not an incremental train command.

### I4 — Queued units count
Completion/admission uses the authoritative total-count semantics.

### I5 — No phantom completion
Command acceptance is not completion.

### I6 — No stale execution
Every execution rule rechecks that the demand is still active and deficient.

### I7 — No hidden cancellation
Target reduction does not implicitly cancel existing queue orders.

### I8 — Engine cost is authoritative
Unit prices are not manually duplicated in composition policy.

### I9 — Prerequisites remain authority-owned
Policy requests military capability; Production Authority decides whether prerequisite construction is necessary.

### I10 — No second executor
The interface does not replace the existing Shadow/AoE2 production machinery with an independent training system.

---

## 15. v0.1 Recommended Goal Layout

The existing production module uses 500-503 for its four-goal cost vector, 507 for production state, and 508 for escrow state. Those allocations should remain stable.

The next available non-cost goals should be treated as the demand interface rather than repurposing the existing transaction goals.

Recommended conceptual allocation:

```text
497  SHADOW-PROD-DEMAND-SPEAR
498  SHADOW-PROD-DEMAND-ARCHER
499  SHADOW-PROD-DEMAND-SKIRM

504  SHADOW-PROD-DEMAND-CAVALRY
505  SHADOW-PROD-DEMAND-SIEGE
506  SHADOW-PROD-DEMAND-AUX

507  SHADOW-PROD-STATE
508  SHADOW-PROD-ESCROW-STATE
```

Each demand goal contains only the requested target count.

`0` means no requested units for that slot.

This layout deliberately avoids using 509-512 for the first cost-data implementation because UserPatch's historical cost-data commands only accept a first-of-four extended-goal range through 508. Those goals may be ordinary state goals, but they should not be casually introduced into a cost-data vector. citeturn1search1

---

## 16. Composition Policy Example

Composition policy should eventually be able to express something as simple as:

```lisp
; Byzantine composition policy
(defrule
    (some-threat-condition)
=>
    (set-goal SHADOW-PROD-DEMAND-SPEAR 8)
)
```

or:

```lisp
(defrule
    (enemy-archer-pressure)
=>
    (set-goal SHADOW-PROD-DEMAND-SKIRM 6)
)
```

That is the complete policy-side responsibility.

It does **not** become:

```lisp
(set-escrow-percentage food 35)
(set-escrow-percentage wood 35)
(can-train ...)
(up-train ...)
```

Those operations remain below the interface.

---

## 17. Why v0.1 Uses Explicit Slots

A dynamic `TARGET-TYPE + TARGET-COUNT` pair looks elegant, but it is not yet the correct first implementation.

The AI language is strongly typed through command parameters, and the engine translates symbolic unit identifiers into numeric IDs. Goals themselves are integer storage. AIRef documents the distinction between Goal, Const, type operators, UnitId, and GoalId parameters. citeturn0search2turn0search6turn0search7

Therefore a fully dynamic indirect production dispatcher would require proving all of the following in the actual Shadow runtime:

- goal-valued UnitId arguments are accepted by every required command/fact;
- dynamic unit identity remains valid through `up-train-site-ready`;
- dynamic unit identity works consistently through `up-can-train` and `up-train`;
- dynamic prerequisite mapping can be performed without introducing a second executor;
- resource reservation can be derived correctly for every target class.

Until those are directly qualified, explicit slots are the more rigorous engineering choice.

---

## 18. Implementation Sequence

The interface should be implemented in this order:

### Step 1 — Contract
Add demand goals and initialization.

### Step 2 — Policy migration
Change composition policy so it writes target goals instead of issuing production commands.

### Step 3 — Spearman migration
Convert the existing 3-Spearman hardcoded target into `SHADOW-PROD-DEMAND-SPEAR`.

### Step 4 — Completion migration
Make completion compare the live Spearman total against the policy target.

### Step 5 — Additional slots
Add Archer and Skirmisher only after their resource/prerequisite execution paths are individually qualified.

### Step 6 — Arbitration
Introduce a final composition arbitration layer before Production Authority receives the target set.

### Step 7 — Verification
Verify each slot independently in runtime/replay evidence.

No step should silently promote an untested dynamic-dispatch mechanism into the production executor.

---

## 19. Final Contract

The production-demand interface is therefore:

```text
POLICY WRITES:
    TARGET COUNT
    ACTIVE/INACTIVE SEMANTICS

AUTHORITY READS:
    TARGET COUNT

AUTHORITY OWNS:
    DEFICIT
    COST VECTOR
    PREREQUISITE
    CAPITAL RESERVATION
    ESCROW
    ADMISSION
    SITE READINESS
    EXECUTION
    COMPLETION
    RELEASE
    RECOVERY

POLICY READS:
    STATUS / OBSERVED RESULT
```

The governing principle is:

> **Composition policy requests a desired military state. Production Authority converts that request into an economically valid, engine-admitted, observable production commitment.**

That is the boundary required to make production a reusable composition substrate rather than a collection of unit-specific train rules.
