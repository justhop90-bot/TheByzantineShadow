# Document 2 Companion — Three-Bot Apprenticeship Plan

## Purpose

The current `Doc2-Per-Apprenticeship.txt` is now a strong conceptual foundation: it teaches the reader to see `.per` as a control system rather than as a bag of syntax. It is not yet, however, the complete apprenticeship the project requires.

The missing element is **construction through progressively less guidance**.

The learner should not merely finish the book knowing what Stock and Naga do. The learner should build three increasingly capable bots with the instructor, while repeatedly returning to the same concepts at greater depth. The three bots become the spine of the course.

The target graduate is not someone who can recite `.per` commands. The target graduate is someone who can open a mature Stock- or Naga-style AI, understand what each major piece is doing, extend it safely, and eventually design a competent bot without needing a template.

This document defines the construction curriculum that should be woven into Document 2.

---

# 1. The Central Teaching Decision

The course should be organized around **three builds**, not around a dictionary of language features.

The learner should encounter a concept immediately before needing it, use it in a real bot, revisit it when the bot becomes more complicated, and finally be required to use it without step-by-step instructions.

The progression is:

**Bot 1 — Stock Apprentice**

Build a small but complete Stock-style AI from first principles. The goal is to learn the fundamental grammar of a functioning AoE2DE AI: initialization, economy, age progression, construction, production, military activity, timers, state, and simple strategic decisions.

**Bot 2 — Naga Apprentice**

Build a modular Naga-style AI. The learner takes the same fundamental game problems and reorganizes them into explicit modules, shared state contracts, helper libraries, demand/producer patterns, reusable control structures, and cleaner architecture.

**Bot 3 — Independent Engineer**

Build a new AI without being given its architecture in advance. Stock and Naga become the reference corpus. The learner must decide what to borrow, what to reject, what to improve, how to divide modules, how to define state ownership, and how to prove that the resulting system works.

The instructor supplies progressively less implementation detail across the three builds.

The first bot is demonstrated heavily.
The second bot is constructed collaboratively.
The third bot is designed by the learner and reviewed adversarially.

That is the transition from apprenticeship to engineering.

---

# 2. Why Three Bots Instead of One

A single project can create the illusion of understanding.

A learner can follow a tutorial, reproduce its code, and still be unable to recognize the same problem when it appears in a different architecture.

Three bots expose the learner to **variation**.

The same requirement appears three times:

- first as a direct Stock-style solution;
- then as a modular Naga-style solution;
- finally as a design problem with no prescribed answer.

This creates an important form of discrimination learning. The learner must distinguish:

- engine requirement from author convention;
- necessary mechanism from optional architecture;
- policy from execution;
- reusable idiom from historical accident;
- state from world state;
- module boundary from authority boundary;
- a good abstraction from an abstraction that merely looks elegant.

The third bot is therefore not simply "Bot 2 but better." It is the first point at which the learner has to construct an architecture from requirements.

---

# 3. Human Learning Architecture

The curriculum should be deliberately designed around established findings from learning science rather than around the order in which a reference manual happens to list commands.

The relevant principles are:

1. **Reduce unnecessary cognitive load for novices.** Introduce only the interacting elements needed for the current task. High-interactivity technical material benefits from strong guidance and worked examples early in learning.

2. **Use worked examples before demanding independent problem solving.** The instructor should build complete pieces in front of the learner, explaining the reasoning rather than merely displaying finished code.

3. **Fade the scaffolding.** As competence increases, remove pieces of the solution. The learner first fills in a line, then a rule family, then a module, then an architecture.

4. **Use retrieval practice.** Before introducing a new system, require the learner to recall the purpose and connection of previously learned systems without reopening the reference.

5. **Space and revisit important ideas.** State ownership, timers, demand/producer separation, and verification should appear repeatedly rather than being taught once and forgotten.

6. **Interleave related problems.** Once the learner has basic fluency, alternate economy, military, construction, and strategy problems so that the learner must identify the underlying pattern instead of relying on topic-specific memorization.

7. **Use concrete examples before abstraction, then return to abstraction.** Show a real villager-production problem before introducing the general producer/consumer model. Later ask the learner to identify the same model in military and construction systems.

8. **Require explanation, not just code.** The learner must be able to explain why a mechanism exists, what it reads, what it writes, who owns it, and how it is verified.

9. **Give immediate, specific feedback.** Failed exercises should identify the broken reasoning layer: syntax, store selection, control flow, state lifecycle, authority, execution, or verification.

10. **Use increasingly authentic problems.** Early exercises are narrow and clean. Later exercises deliberately contain legacy code, competing writers, timing hazards, and incomplete evidence.

These principles are supported by the worked-example literature, cognitive-load research, retrieval/spacing/interleaving research, and deliberate-practice literature. The course should therefore behave less like a reference manual and more like a technical apprenticeship.

Useful evidence includes the worked-example literature summarized by Cambridge University Press and the learning-strategy summaries published by the American Psychological Association. These sources emphasize worked examples for complex novice tasks, fading guidance as expertise develops, retrieval practice, spacing, interleaving, concrete/abstract integration, and feedback-driven practice.

---

# 4. The Teaching Loop for Every New Concept

Every major concept in the revised Document 2 should use the same human-readable teaching loop.

## Step 1 — Show the problem

Start with a bot behaving badly or lacking a capability.

Example:

> The bot can train one spearman, but once that spearman dies the bot never rebuilds it.

Do not begin with the word "latch."

Let the learner understand the problem first.

## Step 2 — Show the smallest working mechanism

Build the smallest `.per` mechanism that solves the problem.

## Step 3 — Explain the mechanism literally

What does each condition do?
What does each action write?
What does the engine do?
What happens on the next pass?

## Step 4 — Name the pattern

Only after the learner has seen it working:

> This is a state latch.

The name becomes a compression of an already understood idea.

## Step 5 — Trace the connection

Show where the state is produced, who reads it, and what world effect follows.

## Step 6 — Break it deliberately

Remove the re-arm.
Change the prefix.
Introduce a second writer.
Move a rule.
Expire the state too early.

Then observe the failure.

## Step 7 — Repair it

The learner should make the repair with decreasing assistance.

## Step 8 — Transfer it

Ask where the same pattern could be used in economy, construction, military, or strategy.

## Step 9 — Retrieve it later

Several chapters later, present a new problem whose solution requires the same pattern without naming it.

This is the fundamental pedagogy of the course.

---

# 5. The Three-Bot Curriculum at a Glance

| Stage | Bot | Instructor behavior | Learner behavior | Main competence |
|---|---|---|---|---|
| 0 | No bot | Demonstrate and orient | Observe, predict, trace | Mental model |
| 1 | Stock Apprentice | Build beside learner | Reproduce and explain | Native fluency |
| 2 | Stock Apprentice | Fade instructions | Complete subsystems | System reasoning |
| 3 | Naga Apprentice | Co-design modules | Build and connect modules | Architecture |
| 4 | Naga Apprentice | Review, inject faults | Diagnose and repair | Forensics |
| 5 | Independent Bot | Specify requirements | Design architecture | Engineering |
| 6 | Independent Bot | Adversarial review | Defend and revise design | Professional competence |

---

# 6. BOT 1 — THE STOCK APPRENTICE

## 6.1 Purpose

Bot 1 should deliberately resemble the direct, historically evolved style of the Stock AI.

It should not begin with sophisticated architecture.

The learner needs to experience why architecture becomes necessary.

Bot 1 should therefore start small, grow organically, and expose the pain of shared state, repeated logic, long rule regions, and direct policy/execution coupling.

This is pedagogically important. If modularity is introduced before the learner experiences the problem it solves, modules become ceremonial folders rather than engineering tools.

## 6.2 Target Bot 1 capability

By the end of Bot 1, it should be able to:

- initialize its strategic state;
- maintain a villager-producing economy;
- gather basic resources;
- progress through ages;
- construct required buildings;
- maintain basic military production;
- maintain a simple composition target;
- scout and retain basic enemy information;
- recognize a small set of threats;
- produce a corresponding counter;
- attack when sufficiently prepared;
- retreat under a simple danger condition;
- recover basic lost infrastructure;
- use timers for recurring work;
- maintain state across passes;
- verify important world-state changes.

It does not need to be a competitive super-AI.

It needs to be **complete enough that every important kind of `.per` problem appears naturally.**

---

# 7. Bot 1 Construction Order

The construction order matters. It should follow dependency rather than topic taxonomy.

## Lesson 1 — The smallest living AI

Build:

- root `.per` file;
- constants;
- one initialization rule;
- one recurring rule;
- one observable action;
- one diagnostic output.

The learner sees the entire machine run before learning any large subsystem.

### Questions the learner must answer

- What starts the AI?
- What causes a rule to fire?
- What survives between passes?
- What is merely text?
- What is engine state?
- What is AI state?

---

## Lesson 2 — Constants and naming

Introduce:

- symbolic constants;
- unit/building identifiers;
- named strategic values;
- naming conventions.

Exercise:

Take an intentionally unreadable rule block and rename its constants without changing behavior.

Purpose:

Teach that naming is not decoration. It is how the engineer creates a conceptual map of the machine.

---

## Lesson 3 — Goals as memory

Build a small state machine using goals.

Example states:

- startup;
- economy established;
- military preparation;
- attack preparation;
- attack active.

The learner should watch the value change over time.

Then deliberately create an impossible transition and diagnose it.

---

## Lesson 4 — The first economy

Build only the economic skeleton:

- villager production;
- food demand;
- wood demand;
- gold demand;
- housing awareness;
- age-up resource awareness.

Do not introduce a sophisticated economy manager yet.

The learner should understand the raw problem:

> Resources are finite, but many systems want them at the same time.

That observation becomes the motivation for later arbitration.

---

## Lesson 5 — Construction

Build a direct construction chain:

requirement → prerequisite → builder availability → construction command → completion observation.

Explicitly distinguish:

- wanting a building;
- deciding to build it;
- assigning a builder;
- issuing a construction command;
- the building actually existing.

This is the first introduction to the principle that **a command is not a completed world state**.

---

## Lesson 6 — Production

Build direct military production.

Start with one unit.

Then add a second unit.

Then add composition pressure.

The learner should initially experience direct production rules:

    if condition A → train X
    if condition B → train Y

Then ask:

> What happens when A and B are both true?

This creates the natural need for precedence.

---

## Lesson 7 — Timers

Introduce:

- one-shot initialization;
- heartbeat;
- cooldown;
- retry;
- timeout.

Every timer must be documented with:

- owner;
- purpose;
- enable condition;
- firing rule;
- re-arm behavior;
- consumers;
- expiry/reset behavior.

The learner should deliberately break a heartbeat by removing its re-arm.

---

## Lesson 8 — Scouting and observation

Build the first observation system.

Do not start with strategy.

First answer:

> What does the AI actually know?

Build:

observation → stored observation → expiry.

Then add:

observation → classification.

The learner should see that a raw enemy-unit count is not yet a strategic decision.

---

## Lesson 9 — Threat response

Build the first complete loop:

    observe cavalry
        ↓
    classify cavalry pressure
        ↓
    decide a counter requirement
        ↓
    increase counter demand
        ↓
    produce counter unit
        ↓
    observe counter-unit count
        ↓
    reassess

This is the first major architecture lesson even though Bot 1 implements it directly.

---

## Lesson 10 — Military state

Build a simple attack state machine.

Minimum states:

- gathering;
- assembling;
- attacking;
- retreating;
- regrouping.

Introduce hysteresis so that the bot does not oscillate between attack and retreat from a single changing observation.

The learner should explicitly identify:

- state entry;
- state maintenance;
- state exit;
- expiry;
- re-entry.

---

## Lesson 11 — Recovery

Break the bot intentionally.

Examples:

- stable destroyed;
- military count falls below target;
- threat information expires;
- desired production remains high after the threat disappears;
- attack authorization becomes stale.

Build recovery rules.

The learner learns that mature bots are not merely decision systems. They are **state-maintenance systems operating in a changing world**.

---

## Lesson 12 — Bot 1 forensic pass

Before beginning Bot 2, the learner must reconstruct Bot 1 from the outside.

Without opening implementation details, the learner must produce:

- root/load diagram;
- state registry;
- timer registry;
- writer/reader map;
- production flow map;
- construction flow map;
- threat flow map;
- military state machine;
- failure table;
- command-to-world verification table.

The instructor then compares the learner's reconstruction against the actual implementation.

This is the first graduation gate.

---

# 8. BOT 2 — THE NAGA APPRENTICE

## 8.1 Purpose

Bot 2 takes the same underlying RTS problems and rebuilds them with a Naga-like modular philosophy.

The learner now knows enough about direct implementation to understand why the architecture exists.

The design should emphasize:

- small modules;
- explicit load graph;
- reusable helper functions/patterns;
- domain-specific state;
- observation modules;
- policy modules;
- demand/producer separation;
- shared contracts;
- explicit state ownership;
- reusable control-flow structures.

The point is not to copy Naga's filenames.

The point is to reconstruct the engineering reasons behind its organization.

---

# 9. Bot 2 Module Construction Order

The learner should build modules in dependency order.

## Module 00 — Root

Responsibilities:

- define load order;
- establish the architecture;
- make module dependencies visible.

Teaching question:

> If I delete this root, what tells the engine what the AI is?

---

## Module 01 — Constants / Registry

Contains:

- symbolic IDs;
- state IDs;
- goal allocations;
- timer allocations;
- strategic-number aliases where justified;
- unit/building constants;
- sentinel values.

Teaching point:

A namespace is architecture.

The learner should never create state in an undocumented slot once Bot 2 begins.

---

## Module 02 — Initialization

Owns:

- default goals;
- initial timers;
- initial strategic state;
- initialization guards;
- initialization completion marker.

No normal policy should be responsible for initialization.

This is the first explicit ownership boundary.

---

## Module 03 — Shared State / Lifecycle

Defines semantic state families and lifecycle conventions.

For every important state:

- birth;
- writer;
- readers;
- valid values;
- transition rules;
- expiration;
- reset;
- re-entry;
- verification.

This module is not a dumping ground for arbitrary globals.

It is the contract layer.

---

## Module 04 — Observation

Collects raw engine information.

Examples:

- unit counts;
- building counts;
- resource state;
- age;
- military presence;
- enemy observations;
- local danger.

Observation should answer:

> What is happening?

It should not decide:

> What should we do about it?

That separation becomes a recurring design discipline.

---

## Module 05 — Census

Transforms repeated observations into stable aggregate state.

Examples:

- military census;
- economy census;
- infrastructure census;
- enemy composition census.

The learner should implement at least one indexed census using a bounded loop.

This is where negative jumps and computed dispatch become practical rather than theoretical.

---

## Module 06 — Classification

Transforms observations into categories.

Examples:

- enemy cavalry pressure;
- enemy ranged pressure;
- local attack;
- infrastructure deficit;
- economy deficit.

The classifier should have explicit validity windows.

A classification without an expiry rule becomes stale strategic state.

---

## Module 07 — Requirements

Transforms classification into capability gaps.

Example:

    enemy cavalry pressure
        ↓
    insufficient anti-cavalry capability
        ↓
    requirement: increase anti-cavalry capacity

This module answers:

> What capability is missing?

It does not yet decide exactly how to buy it.

---

## Module 08 — Policy

Defines what the bot wants.

Examples:

- desired spearmen;
- desired skirmishers;
- desired archers;
- minimum villagers;
- infrastructure floors;
- technology priorities.

Policy is persistent intent.

It should not impersonate execution.

---

## Module 09 — Capital / Feasibility

Examines whether requirements can currently be satisfied.

Consider:

- resources;
- prerequisites;
- production capacity;
- age;
- builder availability;
- competing commitments.

This teaches the learner why a desire can be valid while an execution attempt is infeasible.

---

## Module 10 — Production Dials

Introduce demand/producer separation.

Policy writes:

    desired quantity

Production reads:

    desired quantity
    current quantity
    feasibility

and decides whether execution is possible.

The learner should explicitly compare this architecture with Bot 1's direct production rules.

---

## Module 11 — Construction Producer/Consumer

Construction becomes:

    requirement
      ↓
    policy
      ↓
    construction demand
      ↓
    feasibility
      ↓
    builder selection
      ↓
    command
      ↓
    world completion
      ↓
    verification

This module should teach that the same architecture can serve buildings, units, and technology.

---

## Module 12 — Escrow / Commitment

Introduce the distinction between:

- policy reserve;
- logical commitment;
- physical escrow;
- authorization;
- execution;
- verification.

Do not collapse these concepts.

The learner should trace one military production commitment from desire to actual resource expenditure.

---

## Module 13 — Authority

Create a deliberate arbitration layer.

Example competing demands:

- villager production;
- military production;
- infrastructure;
- technology;
- emergency defense.

Define precedence explicitly.

The learner should be able to answer:

> If economy, defense, and technology all request the same wood, which subsystem has authority and why?

If the answer is "whichever rule happens to run last," Bot 2 has failed its architecture test.

---

## Module 14 — Military Controller

Separate:

- military observation;
- composition requirement;
- production policy;
- attack authorization;
- tactical execution;
- retreat/recovery.

The learner should build a military state machine with explicit entry/exit conditions.

---

## Module 15 — Scouting / Threat Controller

Build:

- scout assignment;
- exploration state;
- enemy census;
- threat classification;
- threat expiry;
- response requirement.

This becomes the source of strategic information rather than a collection of unrelated scout rules.

---

## Module 16 — Technology

Technology should be treated as another consumer of strategic capital.

Build:

- requirement detection;
- policy preference;
- feasibility;
- authorization;
- execution;
- verification.

The learner should see that research is structurally similar to production even though the engine commands differ.

---

## Module 17 — Recovery / Watchdogs

Add watchdogs for:

- stale state;
- impossible commitments;
- missing production;
- lost infrastructure;
- expired threat state;
- interrupted military action;
- unreconciled demand.

Recovery should be bounded and explicit.

---

## Module 18 — Telemetry

Add engineering instrumentation.

At minimum:

- state transition logging;
- demand logging;
- threat classification logging;
- authority decisions;
- command attempts;
- verification observations.

The learner should learn to debug the bot through traces instead of by staring at source code.

---

# 10. The Naga Study Method

While building Bot 2, every module should be paired with a **Naga comparison card**.

Each card asks:

1. What problem does Naga solve here?
2. Where does Naga place the responsibility?
3. What state crosses the module boundary?
4. What is the load-order dependency?
5. What pattern is reusable?
6. What appears to be Naga-specific?
7. What is engine-required versus author convention?
8. What would break if this module disappeared?
9. What other modules consume its output?
10. Could the same behavior be implemented another way?

This prevents the learner from treating Naga as scripture.

Naga is a masterwork specimen, not an engine specification.

---

# 11. BOT 3 — THE INDEPENDENT ENGINEER

Bot 3 begins with requirements, not filenames.

The learner is told what the bot must accomplish but not how it should be organized.

The requirements should include enough interaction to force architecture.

Minimum requirements:

- reliable opening economy;
- age progression;
- adaptive resource allocation;
- enemy composition recognition;
- counter-composition;
- production scaling;
- infrastructure recovery;
- attack/retreat state machine;
- technology decisions;
- emergency defense;
- commitment/resource accounting;
- verification;
- telemetry;
- recovery from interrupted plans.

The learner must submit an architecture before writing implementation code.

---

# 12. Bot 3 Design Review Gate

Before implementation, the learner must produce:

## Architecture

- root/load graph;
- module boundaries;
- dependency direction;
- authority domains.

## State

- goal registry;
- timer registry;
- SN registry;
- state lifecycles;
- sentinel values;
- ownership.

## Data flow

For every major capability:

    observation
      → classification
      → requirement
      → policy
      → feasibility
      → arbitration
      → commitment
      → authorization
      → execution
      → world state
      → verification
      → reassessment

## Failure model

For every subsystem:

- what can become stale?
- what can conflict?
- what can fail silently?
- what can become impossible?
- what clears it?
- what recovers it?

## Verification model

For every command-producing subsystem:

- what proves the command was issued?
- what proves the engine accepted it?
- what proves the intended world effect occurred?
- what proves the strategic state reconciled afterward?

Only after these documents are reviewed should implementation begin.

---

# 13. Progressive Removal of Scaffolding

The three bots should deliberately reduce assistance.

## Bot 1

The book supplies:

- architecture;
- file names;
- state names;
- most rules;
- explanations;
- expected outputs.

The learner supplies:

- small edits;
- predictions;
- diagnostics;
- explanations.

## Bot 2

The book supplies:

- architectural principles;
- module contracts;
- selected Naga examples;
- design constraints.

The learner supplies:

- most module implementation;
- state allocation;
- rule families;
- connections;
- debugging.

## Bot 3

The book supplies only:

- requirements;
- evidence sources;
- constraints;
- review criteria.

The learner supplies:

- architecture;
- contracts;
- implementation;
- testing;
- forensic diagnosis;
- redesign.

This is the intended **fade from worked example to independent performance**.

---

# 14. The Common Code-Type Quick Reference

The final apprenticeship book should contain a prominent quick-reference section organized by **problem**, not by command name.

The learner should be able to ask "I need the bot to remember something" and immediately find the relevant code pattern.

## A. I need the bot to do something once

Pattern:

- unconditional/initial condition;
- perform initialization;
- disable or mark initialization complete.

Use for:

- defaults;
- initial state;
- initial timer setup;
- one-time registration.

Common failure:

- initialization repeats every pass.

---

## B. I need something to happen repeatedly

Pattern:

- timer/heartbeat;
- guarded work;
- re-arm.

Use for:

- census;
- maintenance;
- scouting updates;
- periodic reconciliation.

Common failure:

- timer fires once and never returns.

---

## C. I need the bot to remember that something happened

Pattern:

- observation;
- goal/state write;
- timestamp or validity marker;
- later read.

Use for:

- threats;
- events;
- attack state;
- completion state.

Common failure:

- stale state treated as current.

---

## D. I need the bot to stop oscillating

Pattern:

- separate entry and exit thresholds;
- cooldown;
- hysteresis;
- optional minimum dwell time.

Use for:

- attack/retreat;
- production modes;
- economic transitions;
- threat responses.

Common failure:

- one threshold used for both directions.

---

## E. I need to search through many categories

Pattern:

- index goal;
- inspect current category;
- process;
- increment;
- bounded negative jump.

Use for:

- unit categories;
- production targets;
- threat types;
- resource classes.

Common failure:

- unbounded loop;
- wrong jump distance;
- index not reset.

---

## F. I need to skip expensive logic when a cheap condition fails

Pattern:

- cheap guard;
- forward skip/jump.

Use for:

- fast rejection;
- staged evaluation;
- expensive queries.

Common failure:

- jump target changes after insertion.

---

## G. I need to choose one behavior from many options

Pattern:

- selector/index;
- dispatch region;
- action branch;
- return/continue convention.

Use for:

- strategies;
- unit classes;
- threat responses;
- technology choices.

Common failure:

- selector has no valid fallback.

---

## H. I need the bot to want more of something

Pattern:

- policy/requirement writes demand;
- producer reads demand.

Use for:

- units;
- buildings;
- workers;
- technology.

Common failure:

- demand has no executor;
- demand never expires;
- competing writer lowers it unexpectedly.

---

## I. I need a producer to stop when enough exists

Pattern:

    desired quantity - current quantity

plus feasibility and authority guards.

Common failure:

- current quantity measured from wrong category;
- desired quantity never reconciled;
- queued/committed items ignored.

---

## J. I need several systems to compete for resources

Pattern:

- requirement;
- feasibility/capital analysis;
- precedence;
- commitment;
- authorization.

Common failure:

- accidental source-order arbitration.

---

## K. I need to reserve resources

First decide which concept is required:

- policy reserve;
- logical commitment;
- physical escrow.

Do not use one variable to represent all three.

Common failure:

- reservation survives after commitment dies;
- physical escrow and logical intent diverge.

---

## L. I need to issue a command and know it worked

Pattern:

    command attempt
      ↓
    engine acceptance evidence
      ↓
    world-state observation
      ↓
    reconciliation

Common failure:

- treating command issuance as completion.

---

## M. I need to handle a threat

Pattern:

    observe
      ↓
    classify
      ↓
    determine capability gap
      ↓
    requirement
      ↓
    policy
      ↓
    production/fortification/mobility/retreat response
      ↓
    verify

Common failure:

- jumping directly from observation to execution without a stable state contract.

---

## N. I need a state to expire

Pattern:

- state value;
- timestamp or timer;
- validity guard;
- expiry transition;
- re-entry rule.

Common failure:

- clearing the state without restoring the conditions necessary to recreate it.

---

## O. I need to pause something without losing its strategic intention

Pattern:

- preserve authorization/commitment;
- set pause state;
- block execution;
- periodically re-check feasibility;
- resume if valid;
- cancel only when the commitment is genuinely invalid.

Common failure:

- pause implemented as cancellation.

---

## P. I need to debug a mysterious value

Never begin by changing the rule.

Trace:

    definition
      ↓
    initialization
      ↓
    writers
      ↓
    transformations
      ↓
    readers
      ↓
    commands
      ↓
    world effect

Then determine whether the value itself is wrong or whether its consumer is wrong.

---

# 15. The Engineer's Common-Problem Index

The final book should include a table of symptoms and first investigations.

| Symptom | First question | Likely class |
|---|---|---|
| Works once, then stops | Is the heartbeat re-armed? | Timer lifecycle |
| Value appears wrong | Which store does the operand read? | Prefix/store error |
| Demand stays forever | Who clears/reconciles it? | Lifecycle |
| Two systems fight | Who owns the state? | Authority |
| Adding a rule breaks behavior | Are there positional jumps? | Control-flow topology |
| Bot reacts too late | Is observation cadence too slow? | Timing |
| Bot changes strategy constantly | Are entry/exit thresholds separated? | Hysteresis |
| Unit production never starts | Who writes demand? | Producer chain |
| Unit production never stops | Is current/queued/committed quantity counted? | Reconciliation |
| Command logged, effect absent | What proves world completion? | Verification |
| Threat response persists after threat | Does classification expire? | Stale state |
| Infrastructure never rebuilt | Is the requirement regenerated after loss? | Recovery |
| Technology starves military | Where is capital arbitration? | Authority |
| Jump lands in wrong behavior | Did rule topology change? | Jump hazard |
| Only one build configuration works | Did preprocessing alter the rule stream? | Preprocessor |
| A module seems independent but causes conflicts | What shared stores does it touch? | Hidden coupling |
| Bot gets stuck in a mode | What is the exit transition? | State machine |
| Repeated command spam | What prevents duplicate commitment? | Commitment lifecycle |
| Resource accounting drifts | Are logical and physical reservations reconciled? | Escrow/accounting |

This table should become one of the most-used pages in the book.

---

# 16. The Code-Type Taxonomy the Learner Must Eventually Internalize

The learner should become fluent in these recurring categories:

1. **Initialization rule** — establishes defaults exactly once.
2. **Heartbeat rule** — performs recurring work.
3. **Guard rule** — rejects a path cheaply.
4. **State-transition rule** — moves a state machine between modes.
5. **Latch rule** — remembers an event or condition.
6. **Expiry rule** — invalidates old state.
7. **Hysteresis rule** — prevents oscillation.
8. **Cooldown rule** — prevents immediate re-entry.
9. **Search-loop rule** — scans bounded categories.
10. **Dispatch rule** — selects one of several behaviors.
11. **Census rule** — aggregates observations.
12. **Classification rule** — converts observations into semantic categories.
13. **Requirement rule** — describes a capability deficit.
14. **Policy rule** — establishes desired behavior.
15. **Demand rule** — communicates desired quantity/capability to an executor.
16. **Feasibility rule** — tests whether execution is currently possible.
17. **Producer rule** — turns demand into an engine operation.
18. **Commitment rule** — records that a plan has been accepted.
19. **Escrow rule** — tracks or invokes physical resource reservation semantics.
20. **Authority rule** — resolves competing demands.
21. **Execution rule** — issues the engine-facing action.
22. **Verification rule** — checks resulting world state.
23. **Reconciliation rule** — aligns intended and observed state.
24. **Watchdog rule** — detects a subsystem that stopped progressing.
25. **Recovery rule** — restores a valid state after failure.
26. **Telemetry rule** — makes hidden state observable.
27. **Compatibility rule** — preserves an engine/version or legacy contract.
28. **Structural control-flow rule** — implements jumps, skips, or dispatch topology.
29. **Preprocessor specialization** — changes the generated rule set by build configuration.
30. **Boundary/adapter rule** — translates one subsystem's state vocabulary into another's.

The learner should eventually identify these shapes without being told their names.

That is pattern fluency.

---

# 17. The Repeated Trace Method

For every major system in all three bots, the learner should maintain the same trace sheet:

```text
WORLD OBSERVATION
    ↓
FACT / QUERY
    ↓
STATE WRITE
    ↓
CLASSIFICATION
    ↓
REQUIREMENT
    ↓
POLICY
    ↓
FEASIBILITY
    ↓
ARBITRATION
    ↓
COMMITMENT
    ↓
AUTHORIZATION
    ↓
EXECUTION
    ↓
WORLD-STATE CHANGE
    ↓
VERIFICATION
    ↓
RECONCILIATION
    ↓
REASSESSMENT
```

Not every subsystem requires every stage.

That is itself something the learner must learn.

For example, a trivial initialization may be:

    initialization → state write

A direct producer may be:

    policy → feasibility → execution → verification

A strategic military response may require the entire chain.

The learner should learn to distinguish a missing stage from a deliberately unnecessary stage.

---

# 18. The Three-Bot Comparison Notebook

Throughout the apprenticeship, the learner should maintain a permanent comparison table.

| Problem | Stock solution | Naga solution | Bot 3 solution | Why |
|---|---|---|---|---|
| Initialization | | | | |
| Villager production | | | | |
| Resource allocation | | | | |
| Construction | | | | |
| Military production | | | | |
| Threat observation | | | | |
| Threat classification | | | | |
| Counter composition | | | | |
| Attack state | | | | |
| Retreat | | | | |
| Technology | | | | |
| Escrow | | | | |
| Arbitration | | | | |
| Recovery | | | | |
| Telemetry | | | | |

The learner must fill this from evidence, not memory.

The purpose is to create architectural transfer.

---

# 19. How the Instructor Should Explain Real Stock and Naga Code

Never present a large source excerpt without first giving the reader a question.

Bad teaching:

> Here are 400 lines from the production system.

Better teaching:

> The bot wants archers. Find where that desire originates. Now follow the value until an archer can actually be trained. There are three different layers hiding in this region. Find them.

Then reveal the answer.

For every real source excerpt, use this sequence:

1. **Question** — what should the learner find?
2. **Context** — what subsystem are we in?
3. **Excerpt** — only enough real code to investigate.
4. **Prediction** — what should happen?
5. **Trace** — follow writers/readers.
6. **Explanation** — explain the mechanism.
7. **Architecture** — explain why it belongs there.
8. **Counterexample** — show a plausible wrong implementation.
9. **Exercise** — modify or recreate it.
10. **Transfer** — find the same pattern elsewhere.

This is how source code becomes a teacher rather than wallpaper.

---

# 20. How the Learner Should Encounter Complexity

Complexity should rise along several independent axes.

## Axis 1 — Syntax

Simple conditions → nested conditions → multiple actions → complex operands.

## Axis 2 — State

One value → several related values → state families → lifecycle → competing writers.

## Axis 3 — Time

One-shot → heartbeat → cooldown → expiry → interruption/re-entry.

## Axis 4 — Control flow

Sequential rules → guards → jumps → loops → dispatch → preprocessor-dependent topology.

## Axis 5 — Architecture

One file → several files → explicit contracts → multiple domains → arbitration.

## Axis 6 — Uncertainty

Known engine behavior → observed convention → inferred architecture → incomplete evidence.

## Axis 7 — Debugging

Syntax error → wrong value → wrong writer → wrong consumer → cross-module failure → architectural failure.

The course should not increase all seven axes simultaneously.

That would overwhelm the learner.

Instead, each new difficulty should be introduced while the others remain relatively stable.

Later, the axes should be deliberately combined.

That is how the learner moves from isolated skill to systems competence.

---

# 21. Deliberate Practice Structure

Each subsystem should have five practice modes.

## Mode A — Recognition

Identify a pattern in existing code.

Example:

> Which rules form the heartbeat?

## Mode B — Explanation

Explain why the pattern exists.

## Mode C — Completion

Finish a partially implemented rule family.

## Mode D — Repair

Diagnose a deliberately broken implementation.

## Mode E — Generation

Design the subsystem from requirements without a template.

Bot 1 should emphasize A–C.
Bot 2 should emphasize B–D.
Bot 3 should emphasize D–E.

---

# 22. Retrieval Questions

At the beginning of later chapters, ask the learner to answer questions from memory.

Examples:

- What is the difference between a constant and a goal?
- What does the arrow in `defrule` represent?
- Why can a parser-valid expression still be semantically wrong?
- What makes a timer a lifecycle problem?
- What is the difference between demand and execution?
- Why is a module not automatically an authority boundary?
- What proves that a command actually succeeded?
- Why can source order become part of a contract?
- When should a state expire?
- Why is pause different from cancel?

Only then introduce the next layer.

The learner should repeatedly retrieve old knowledge while learning new material.

---

# 23. Fault-Injection Curriculum

Each bot should be deliberately broken in increasingly sophisticated ways.

## Bot 1 faults

- missing initialization;
- missing timer re-arm;
- wrong constant;
- wrong goal;
- wrong unit ID;
- impossible guard.

## Bot 2 faults

- duplicate writer;
- missing module load;
- wrong load order;
- stale classification;
- orphaned demand;
- producer/consumer mismatch;
- conflicting authority;
- bad jump topology;
- broken recovery.

## Bot 3 faults

- hidden architectural cycle;
- ambiguous ownership;
- resource-accounting divergence;
- stale strategic commitment;
- command accepted but world state not verified;
- recovery that corrupts unrelated state;
- preprocessor-specific control-flow break;
- version-sensitive command assumption.

The learner must diagnose before being shown the fault.

---

# 24. Graduation Requirements

The learner should not graduate because the bot runs.

The learner graduates when they can explain and defend the system.

## Practical test 1 — Read

Given an unfamiliar Stock-style section, identify:

- purpose;
- inputs;
- state;
- outputs;
- control flow;
- lifecycle;
- likely hazards.

## Practical test 2 — Trace

Given a strategic requirement, trace it from observation to world effect.

## Practical test 3 — Diagnose

Given a replay symptom, identify the smallest state transition that could explain it, then trace outward until the responsible subsystem is established.

## Practical test 4 — Modify

Add a new unit target without creating uncontrolled competing writers.

## Practical test 5 — Architect

Design a new subsystem with a state contract and module boundary before writing code.

## Practical test 6 — Verify

Demonstrate that a command-producing subsystem changes the intended world state and reconciles afterward.

## Practical test 7 — Defend

Explain why the chosen architecture is preferable to at least one plausible alternative for the specific requirements.

The learner should be judged on reasoning, not line count.

---

# 25. The Standard for Every New Module

Before a module is considered complete, its documentation should answer:

### Purpose

Why does this module exist?

### Inputs

What facts/state does it consume?

### Outputs

What state/commands does it produce?

### Ownership

What does it own?

### Non-ownership

What must it never modify?

### Lifecycle

How is its state initialized, maintained, expired, and recovered?

### Dependencies

Which modules must precede it?

### Consumers

Who reads its outputs?

### Authority

Can it override other modules?

### Failure modes

How can it fail?

### Verification

How do we know it worked?

### Evidence

Which claims are CONFIRMED, DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, or UNCERTAIN?

This becomes the professional module contract.

---

# 26. What the Learner Must Learn to See in Stock

Stock should teach the learner to recognize historical accumulation.

The learner should learn to look for:

- large rule families;
- repeated direct actions;
- timing machinery;
- state variables with broad scope;
- source-order assumptions;
- strategic-number usage;
- production decisions embedded close to execution;
- military state machinery;
- recovery sections;
- legacy compatibility patterns.

The question is not:

> Why isn't Stock cleaner?

The question is:

> What problem was this structure solving, and what other code now depends on it?

Stock teaches the consequences of a mature historical system.

---

# 27. What the Learner Must Learn to See in Naga

Naga should teach the learner to recognize explicit architecture.

Look for:

- root/load graph;
- helper libraries;
- domain modules;
- shared contracts;
- reusable control structures;
- computed dispatch;
- producer/consumer relationships;
- strategic state families;
- modular strategy.

The question is not:

> Why should every bot use Naga's modules?

The question is:

> What human problem does each boundary solve, and what machine-level coupling remains despite the boundary?

Naga teaches architecture as a deliberate human engineering choice.

---

# 28. The Final Synthesis

By the end of Bot 3, the learner should be able to look at a mature AI and mentally perform the following transformation:

```text
SOURCE TEXT
    ↓
RULE SHAPES
    ↓
STATE STORES
    ↓
CONTROL FLOW
    ↓
MODULES / REGIONS
    ↓
WRITER-READER GRAPH
    ↓
AUTHORITY GRAPH
    ↓
LIFECYCLE MODEL
    ↓
STRATEGIC DATA FLOW
    ↓
WORLD EFFECTS
    ↓
VERIFICATION / FAILURE MODEL
    ↓
ARCHITECTURAL UNDERSTANDING
```

Then the engineer should be able to reverse the process:

```text
REQUIREMENT
    ↓
CAPABILITY MODEL
    ↓
STATE CONTRACT
    ↓
MODULE BOUNDARY
    ↓
CONTROL PATTERN
    ↓
RULE IMPLEMENTATION
    ↓
EXECUTION
    ↓
VERIFICATION
    ↓
RECOVERY
```

That two-way movement is the actual objective of the apprenticeship.

A person who can only read existing code is an analyst.

A person who can only write isolated rules is a scripter.

A person who can reconstruct a system, explain why it works, modify it safely, and then design a new system from requirements is an engineer.

---

# 29. Required Revision to Document 2

The existing Document 2 should be retained as the conceptual foundation, but its chapters should be reorganized around the three-bot journey.

The preferred macro-structure is:

## BOOK I — LEARNING TO READ THE MACHINE

Short, friendly foundations.

No large abstractions before the learner has seen a real rule execute.

## BOOK II — BUILDING BOT 1: THE STOCK APPRENTICE

A complete guided construction.

Every subsystem is introduced because the bot needs it.

## BOOK III — TAKING BOT 1 APART

Forensic reconstruction and fault injection.

The learner learns why the architecture works and where it is fragile.

## BOOK IV — BUILDING BOT 2: THE NAGA APPRENTICE

Rebuild the same capabilities using modular architecture.

## BOOK V — READING NAGA LIKE AN ENGINEER

Direct source comparisons, reusable patterns, architecture atlas, and module contracts.

## BOOK VI — BOT 3: THE INDEPENDENT BUILD

Requirements first; architecture second; implementation third.

## BOOK VII — THE ENGINEER'S FIELD MANUAL

Quick reference organized by problem, code type, failure symptom, and architectural pattern.

## BOOK VIII — PROFESSIONAL FORENSICS

Stock, Naga, Shadow, corpus analysis, runtime evidence, version drift, and adversarial debugging.

## APPENDICES

- state registry template;
- timer registry;
- writer/reader matrix;
- authority matrix;
- command contract;
- verification checklist;
- common code-pattern atlas;
- jump audit sheet;
- preprocessor audit sheet;
- evidence classification sheet;
- practice project ladder.

The present 63-chapter structure can supply much of the conceptual material, but the learner should encounter it in this construction-centered order rather than as a conventional reference sequence.

---

# 30. The Most Important Editorial Rule

Never allow the book to become a catalog again.

If a command is introduced, give the learner a reason to need it.

If a pattern is introduced, show the problem it solves.

If a module is introduced, explain what would become difficult without it.

If a Stock idiom is shown, explain what historical or engine constraint may have produced it.

If a Naga module is shown, explain the human and architectural problem its boundary solves.

If an abstraction is proposed, show it in at least two different domains before declaring it general.

If a rule is called correct, explain what evidence establishes correctness.

If a command is shown, distinguish command acceptance from world-state completion.

If a subsystem is declared complete, show its verification and recovery path.

And whenever possible, make the reader predict the next behavior before revealing it.

The learner should spend the book repeatedly thinking:

> I know what the bot is trying to do. Let me see how the author made it do that.

That is the mental habit we are trying to create.

---

# 31. Evidence Base for the Learning Design

The instructional design in this plan is not based on the assumption that "more information" automatically produces expertise.

The worked-example literature reports that worked solutions can improve learning on complex tasks for novices, especially when element interactivity is high; as expertise increases, guidance should change rather than remain fixed. Cognitive-load research therefore supports strong early scaffolding followed by increasing learner responsibility.

Learning-science summaries from the American Psychological Association emphasize spacing, retrieval practice, interleaving, concrete/abstract integration, quizzing, and feedback-driven metacognition as useful learning strategies. Deliberate-practice literature emphasizes repeated work on specific skills, feedback, incremental goals, observation of one's own performance, and continuous assessment.

For this domain, these principles map naturally onto:

- worked construction of Bot 1;
- partial completion exercises;
- repeated state/trace questions;
- spaced revisiting of timers, state, authority, and verification;
- comparison of Stock and Naga solutions to the same problem;
- fault injection;
- replay/runtime evidence;
- progressively independent architecture;
- adversarial review of Bot 3.

The instructional objective is therefore not to make the learner read more pages. It is to make the learner perform increasingly difficult acts of engineering until the relevant patterns become available automatically under pressure.

---

# 32. Final Curriculum Definition

The complete apprenticeship should produce the following sequence of transformations:

```text
I can recognize a .per rule.
        ↓
I can explain a .per rule.
        ↓
I can write a .per rule.
        ↓
I can connect rules into a subsystem.
        ↓
I can trace state through a subsystem.
        ↓
I can explain why the subsystem exists.
        ↓
I can diagnose a broken subsystem.
        ↓
I can connect multiple subsystems safely.
        ↓
I can reconstruct an unfamiliar AI.
        ↓
I can recognize Stock and Naga patterns without copying them blindly.
        ↓
I can choose an architecture for a new requirement.
        ↓
I can design state ownership and lifecycles.
        ↓
I can build the system.
        ↓
I can verify it against the actual world.
        ↓
I can recover it when reality invalidates the plan.
        ↓
I can defend the engineering decisions.
        ↓
I can teach the same reasoning to another engineer.
```

That final state — not memorization of syntax, not familiarity with a particular bot, and not code volume — is the definition of an ace `.per` engineer.
