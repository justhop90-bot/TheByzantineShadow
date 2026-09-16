# Shadow Creator Intent + Live Path Control-Flow Forensics v0.2

**Status:** Research baseline; no runtime claims beyond the retained source corpus.

**Scope:** Deconstruction of Shadow DC7 as a competitive, tested `.per` AI, with emphasis on what its creator was actually trying to accomplish rather than merely cataloguing commands.

**Primary donor artifact:** `SourceShaRef` / Shadow DC7 source, SHA-256 `8127c4243b071fa80853f258fb3cf5959399ca86`, 84,371 bytes.

**Purpose:** Recover the behavioral design implicit in Shadow's state, escrow, progression, interruption, production, and control-flow machinery so The Byzantine Shadow can transplant the *mechanism* without blindly transplanting Viking-specific assumptions.

---

## 1. Executive finding

Shadow should not be understood as a conventional build-order script with some escrow sprinkled on top.

It is better understood as a **persistent reactive economic-control machine** whose creator was trying to make a fixed `.per` rule engine behave as though it could maintain a strategic plan while temporarily suspending, financing, executing, and then resuming subordinate objectives.

The important achievement is not simply:

```text
reserve resources -> research something -> release resources
```

It is:

```text
strategic posture
    -> ordered progression
    -> detect an exceptional requirement
    -> interrupt progression
    -> protect the resources needed by that requirement
    -> execute through an escrow-aware engine command
    -> observe enough state to treat the step as complete
    -> restore the interrupted progression
    -> continue
```

That is the behavior The Byzantine Shadow should preserve.

The creator was effectively solving a hard `.per` problem: **how do you maintain long-horizon economic intent while still reacting to a changing battlefield without destroying the original plan every time a new fact appears?**

The source strongly suggests that Shadow's answer was stateful interruption and resource reservation, not a giant flat priority list.

---

## 2. Creator intent: what the source says, and what it implies

### 2.1 DIRECT evidence from the author

The source header identifies Shadow as an AoE2 AI by FireBall37 and explicitly says the author learned from the AIscripters community and from other AIs. The author also warns that unused code from earlier experiments may remain.

The supported-settings header is unusually revealing: Shadow was explicitly built around a constrained competitive test environment, including 1v1, Tiny Arabia, standard resources, 200 population, and Vikings.

That matters because the code should be read as a **competitive control system tuned around a known test envelope**, not as a general-purpose academic AI framework.

### 2.2 INFERRED creator objective

The source architecture indicates the creator was trying to solve several interacting problems simultaneously:

1. **Maintain an economic/progression plan.**
2. **Respond to enemy composition and battlefield conditions.**
3. **Avoid spending protected resources accidentally on lower-value actions.**
4. **Temporarily redirect the economy toward a strategic exception.**
5. **Resume the original progression after the exception.**
6. **Prevent incompatible actions from firing while an exceptional state is active.**
7. **Use rule jumps and state variables to make a flat rule file behave like a control-flow graph.**

This is the central design insight.

Shadow's author was not merely writing rules that say "if X, do Y." The author was constructing **persistent state so that the same rules could mean different things depending on where the bot currently was in its strategic process.**

---

## 3. The live behavioral path

The reconstructed high-level path is:

```text
WORLD OBSERVATION
      |
      v
STRATEGIC STATE
(gl-strategy)
      |
      v
PROGRESSION STATE
(gl-build-progress)
      |
      v
CURRENT BUILD ITEM
(gl-current-build-item)
      |
      +------------------------------+
      |                              |
      | normal progression           | exceptional requirement
      v                              v
CURRENT ITEM ESCROW POLICY     PROGRESSION INTERRUPTION
      |                       (gl-progression-pause)
      |                              |
      v                              v
CAN-AFFORD / CAN-EXECUTE      TEMPORARY RESOURCE RESERVATION
      |                              |
      +---------------+--------------+
                      |
                      v
             ESCROW-AWARE COMMAND
        (up-research / up-train)
                      |
                      v
             WORLD-STATE CHANGE
                      |
                      v
             COMPLETION OBSERVATION
                      |
                      v
             RELEASE / RESTORE
                      |
                      v
             PROGRESSION ADVANCE
                      |
                      v
                 REASSESS
```

This is not a claim that Shadow literally implements these stages as named software modules. It is the recovered behavioral graph formed by its persistent goals, guards, escrow commands, release operations, completion conditions, and jump-based control flow.

---

## 4. State variables are the actual architecture

### `gl-strategy`

This is the strategic mode. The source initializes and changes strategy state, including FLUSH and KRUSH paths.

**Interpretation:** the creator wanted the same downstream machinery to behave differently under different strategic postures rather than maintaining completely separate AIs.

### `gl-build-progress`

This is a progression cursor. The source contains rules that recognize when progress has advanced too far or was skipped and then correct the stored progression state.

**Interpretation:** the creator did not trust a one-way build-order assumption. The bot needs to reconcile its intended progression with the state that actually exists.

### `gl-current-build-item`

This identifies the current progression target. Rules explicitly synchronize it with `gl-build-progress`.

**Interpretation:** the creator separated **where the strategy is** from **what concrete item is currently being pursued**.

### `gl-progression-pause`

This is the most important state for understanding Shadow's design. It represents a temporary interruption of normal progression for a subordinate strategic requirement.

Examples in the source include setting a pause for armor technologies when battlefield conditions justify the interruption, allocating escrow for that requirement, executing it, then resetting the pause.

**Interpretation:** this is a lightweight transaction/interrupt mechanism implemented entirely with goals and rules.

### `gl-escrow-state`

The source uses `with-escrow` and `without-escrow` as the parameter supplied to commands such as:

```lisp
(up-train gl-escrow-state c: skirmisher-line)
(up-research gl-escrow-state c: ri-iron-casting)
```

**Important:** this is **not** a logical owner ID. It is an execution-accounting mode passed into engine commands.

The correct abstraction is:

```text
logical strategic intent
        !=
engine escrow accounting mode
```

This distinction must survive transplantation.

---

## 5. Shadow's escrow is dynamic, not static

The source demonstrates explicit resource reservation and reconfiguration.

### Scale Mail pattern

The source increases food escrow to a target amount, executes the research with escrow, resets the progression pause, sets the relevant escrow percentage to zero, and releases the resource.

Conceptually:

```text
exception identified
 -> reserve food
 -> execute Scale Mail with escrow
 -> clear exception
 -> remove food escrow policy
 -> release food
```

### Chain Mail pattern

The source reserves both food and gold, executes Chain Mail with escrow, clears the pause, removes the relevant escrow percentages, and releases both resources.

Conceptually:

```text
exception identified
 -> reserve food + gold
 -> execute
 -> clear exception
 -> release both resources
```

### Iron Casting / flush pattern

The source uses absolute escrow modifications for food and gold while explicitly releasing wood from escrow.

The significant point is not the particular numbers. The significant point is that Shadow can **reshape its economic protection policy around the current strategic requirement**.

That is substantially more powerful than a permanent "save X food" rule.

---

## 6. Why `can-research-with-escrow` and `can-train-with-escrow` matter

The source repeatedly gates commands through escrow-aware affordability predicates before issuing research or training.

This creates a two-part mechanism:

```text
RESOURCE PROTECTION
        +
EXECUTION AFFORDABILITY
        =
CONTROLLED COMMITMENT
```

The bot is not merely asking whether it has enough resources in the wallet.

It is asking whether the action can be performed under the protected economic posture it has established.

This is one of Shadow's most important reusable mechanisms.

For The Byzantine Shadow, the correct transplant is therefore not "copy Shadow's numbers." It is:

```text
capability requirement
 -> economic reservation
 -> escrow-aware feasibility
 -> existing executor
```

The reservation amounts, percentages, and triggers must be rebuilt around Byzantine economics.

---

## 7. Interruption and re-entry are deliberate features

The strongest evidence of creator intent is the combination of:

- strategic state;
- progression cursor;
- current item;
- progression pause;
- escrow modification;
- escrow-aware command execution;
- release;
- progression advancement.

This forms a primitive but effective **interrupt/return architecture**.

A normal progression step can be temporarily displaced by a higher-context requirement without permanently destroying the progression model.

This is exactly the behavior a reactive Byzantine AI needs.

A Byzantine implementation should therefore prefer:

```text
normal plan
   |
   +--> threat creates capability requirement
            |
            v
      temporary interruption
            |
            v
      fund + execute response
            |
            v
      verify / release
            |
            v
      resume plan
```

rather than rebuilding the entire build order whenever the enemy changes composition.

---

## 8. Progression reconciliation is more important than build-order memorization

Shadow contains corrective rules that move the stored build progression back into alignment with research state.

A representative pattern is:

```lisp
(up-research-status c: ri-iron-casting < research-pending)
(up-compare-goal gl-build-progress > IronCastingNumber)
```

followed by resetting `gl-build-progress` to the appropriate milestone.

This is evidence of an important design philosophy:

> **The strategic state is not sacred. The bot is allowed to reconcile its plan against what the engine says has actually happened.**

That is a major lesson for The Byzantine Shadow.

Do not create a progression cursor that blindly increments because a command was issued. Progression should remain coupled to observable engine state.

---

## 9. Production is governed by the same economic philosophy

Shadow uses `can-train-with-escrow` in conjunction with strategic, age, composition, and progression conditions before issuing training commands.

The production logic also contains exclusions tied to progression interruptions and technology state.

This means production is not isolated from the economic control system.

The creator was trying to prevent the following failure mode:

```text
strategy wants X
production blindly trains X
research suddenly becomes necessary
research cannot be funded
```

Instead, the intended behavior is closer to:

```text
strategic context
 -> current economic protection
 -> production eligibility
 -> escrow-aware training
```

This is precisely why replacing Shadow's economic substrate with a cleaner but disconnected production controller would be a regression unless runtime evidence proves otherwise.

---

## 10. `up-jump-rule` is hidden control flow

Shadow contains extensive `up-jump-rule` usage.

Therefore textual rule order cannot be treated as the complete execution model.

The source is effectively implementing a control-flow graph inside a forward-chaining rule language:

```text
rule condition
    -> jump / skip
    -> another rule region
    -> alternate subsystem
    -> return through subsequent evaluation
```

Some jumps bypass irrelevant sections when required unit groups do not exist or when the current tactical context changes.

**Engineering consequence:** a transplant that preserves rules but strips jumps can preserve syntax while destroying behavior.

The correct unit of transplantation is the **control-flow path**, not the individual rule.

---

## 11. `disable-self` is also architectural

The source uses `disable-self` during strategy initialization paths.

This indicates that some rules are intended as one-time state initialization or mode-selection transitions rather than perpetual reactive rules.

The distinction matters:

```text
persistent policy rule
        !=
state transition / initialization rule
```

A reconstruction must preserve this lifecycle distinction.

---

## 12. What the creator was really building

The grumpy-scripter interpretation is blunt:

**The author was fighting the limitations of `.per` and winning by refusing to pretend `.per` was a normal programming language.**

There is no conventional object model. There is no clean event loop. There is no explicit transaction class. There is no formal scheduler.

So the creator manufactured those concepts from:

- integer goals;
- timers;
- strategic modes;
- progression counters;
- conditional rules;
- escrow state;
- engine predicates;
- command parameters;
- explicit release operations;
- jumps;
- self-disabling rules.

That is why the code can look messy while the behavior is sophisticated.

A clean-room rewrite that merely produces prettier `.per` could easily be worse than the original.

The correct question is not:

> "How do we make Shadow's code cleaner?"

The correct questions are:

> "What state machine did the author accidentally—or deliberately—build?"

and:

> "Which invariants made that state machine competitive?"

---

## 13. Shadow's real abstraction

The recovered abstraction is:

```text
STRATEGY
   |
   v
PROGRESSION
   |
   v
CURRENT OBJECTIVE
   |
   +------ normal ------+
   |                    |
   |                    v
   |             ESCROW POLICY
   |                    |
   |                    v
   |             EXECUTION GATE
   |                    |
   +---- interrupt ---> TEMPORARY REQUIREMENT
                         |
                         v
                  RESOURCE RESERVATION
                         |
                         v
                  ESCROW-AWARE EXECUTION
                         |
                         v
                       RELEASE
                         |
                         v
                    RESTORE / ADVANCE
```

This is the core transplant target.

---

## 14. What is DIRECT, what is INFERRED, and what is not present

| Finding | Evidence class | Qualification |
|---|---|---|
| Shadow has persistent strategy state | DIRECT | CONFIRMED in donor source |
| Shadow has progression state | DIRECT | CONFIRMED |
| Shadow has a current build item concept | DIRECT | CONFIRMED |
| Shadow can interrupt progression | DIRECT | CONFIRMED |
| Shadow dynamically modifies escrow | DIRECT | CONFIRMED |
| Shadow releases escrow after protected operations | DIRECT | CONFIRMED |
| Shadow uses escrow-aware research/training gates | DIRECT | CONFIRMED |
| Shadow advances progression from observed research state | DIRECT | CONFIRMED |
| Shadow uses jump-based control flow | DIRECT | CONFIRMED |
| Shadow uses one-shot/self-disabling state transitions | DIRECT | CONFIRMED |
| Shadow has a formal logical commitment ledger | NOT CONFIRMED | No direct evidence |
| Shadow has independent per-requirement engine escrow accounts | NOT CONFIRMED | Engine model does not support this abstraction |
| Shadow implements a formal priority queue | NOT CONFIRMED | Priority/control flow exists, but not a conventional queue |
| Shadow's exact competitive strength is caused solely by escrow | INFERRED | Escrow is clearly important, but causal attribution requires controlled runtime evidence |
| Shadow's creator intended a general-purpose Byzantine architecture | FALSE | Donor is explicitly Viking-specific and test-envelope-specific |
| The mechanism can be generalized to Byzantine capability economics | AEGIS-GENERALIZATION | Strong architectural hypothesis; requires runtime qualification |

---

## 15. What must be transplanted

### Preserve as mechanism

1. Persistent strategic state.
2. Progression cursor and reconciliation.
3. Current-objective state.
4. Temporary progression interruption.
5. Dynamic escrow reservation.
6. Both absolute and percentage escrow manipulation where appropriate.
7. Explicit selective release.
8. Escrow-aware affordability gates.
9. Escrow-aware engine commands.
10. Completion-driven progression advancement.
11. Production suppression/eligibility around incompatible progression states.
12. Jump-based control flow where it is semantically required.
13. One-shot initialization/state-transition behavior.
14. Re-entry into the interrupted strategic path.

### Do not transplant blindly

1. Viking-only unit assumptions.
2. Viking-only cost/discount assumptions.
3. Fixed FLUSH/KRUSH timings as Byzantine policy.
4. Shadow's exact technology ordering as Byzantine doctrine.
5. Donor map-size assumptions.
6. Donor strategic thresholds without requalification.
7. Donor priority numbers merely because they exist.
8. Donor goal IDs when they collide with The Byzantine Shadow registry.
9. Donor executor assumptions when Byzantine production/building mechanics differ.
10. Any behavior whose only justification is that it exists in Shadow.

---

## 16. Byzantine reconstruction hypothesis

The Byzantine version should preserve Shadow's economic machinery while replacing the donor's fixed strategic interpretation with capability-driven requirements.

Target:

```text
ENEMY / WORLD OBSERVATION
        |
        v
CAPABILITY GAP
        |
        v
CANDIDATE BYZANTINE RESPONSES
        |
        v
ENGINE COST
        |
        v
BYZANTINE COST / CAPABILITY EFFICIENCY
        |
        v
CAPITAL ARBITRATION
        |
        v
SHADOW ECONOMIC POSTURE
        |
        v
PHYSICAL ESCROW
        |
        v
EXISTING EXECUTOR
        |
        v
OBSERVED WORLD RESULT
        |
        v
VERIFICATION
        |
        v
RELEASE + REASSESSMENT
```

The key design change is therefore **not** replacing Shadow's economic system.

It is replacing the donor's fixed strategic interpretation with a Byzantine-specific capability model while retaining the proven reservation/execution/release substrate.

---

## 17. The banker architecture must not destroy the donor architecture

The current AEGIS + Shadow architecture defines a separation between cognition/arbitration and economic execution.

That separation should be sharpened rather than used as an excuse to duplicate Shadow.

```text
AEGIS
  = observation interpretation
  + capability classification
  + requirement formation
  + cross-requirement arbitration
  + authorization
  + verification

SHADOW
  = economic posture
  + progression
  + resource protection
  + physical escrow
  + interruption
  + execution integration
  + release
  + restoration
```

This is a deliberate conservation strategy.

The more Shadow machinery is replaced, the less certain we become that we are preserving the behavior that made Shadow competitive.

The burden of proof therefore belongs to the replacement.

---

## 18. Required next forensic pass

Before additional implementation, the donor should be reconstructed into an exact numbered live-path matrix containing, for every relevant rule:

- source location / rule number;
- prerequisite facts;
- state reads;
- state writes;
- escrow mutations;
- release mutations;
- engine command;
- command parameterization;
- jump target;
- downstream rules reached or skipped;
- progression effect;
- production effect;
- interruption effect;
- re-entry condition;
- evidence class;
- Byzantine transplant disposition.

The next pass must also identify all writers of the relevant Shadow state symbols and resolve whether any apparent dead/duplicate code is actually reachable through jumps, conditional loading, or strategy-specific paths.

Do not call a rule dead merely because it is not on the obvious textual path.

---

## 19. Bottom line

Shadow's creator was not merely building a good build order.

He was building a **resource-protected reactive strategy machine** inside a primitive rule language.

The clever part was the ability to say, in effect:

```text
"I have a plan.
Something more important just happened.
I will temporarily protect the resources needed to answer it.
I will execute the answer without losing control of my economy.
Then I will release those resources and return to the plan."
```

That is the behavior The Byzantine Shadow should inherit.

The Byzantine contribution should be the intelligence that determines **which capability deserves that interruption**, **why**, **against what observed threat**, **at what opportunity cost**, and **whether the resulting capability was actually achieved**.

Do not turn Shadow into a museum piece.

Do not turn AEGIS into a second Shadow.

Recover the machine the original author built, preserve the parts that demonstrably work, and make the Byzantine layer smarter about when to use them.

**Evidence status:** Donor behavioral mechanisms above are DIRECT/CONFIRMED from the retained Shadow source unless explicitly marked otherwise. Creator motivation beyond explicit comments is INFERRED from code structure and should remain labeled as such until corroborated by author documentation or controlled runtime experiments.
