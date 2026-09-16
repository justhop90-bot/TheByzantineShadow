# Document 2 — Chapter-by-Chapter Apprenticeship Outline

## Editorial / instructional specification for `Doc2-Per-Apprenticeship.txt`

This outline converts the Three-Bot Apprenticeship Plan into the actual teaching spine of Document 2. It preserves the existing conceptual material but changes the reader's journey from **reference exposure** to **guided construction → reconstruction → architectural comparison → independent engineering**.

The central rule is: **introduce a concept immediately before the learner needs it, make the learner use it, break it, repair it, and later require retrieval without naming it.**

The three builds are:

1. **Bot 1 — Stock Apprentice:** direct, compact, historically Stock-like construction.
2. **Bot 2 — Naga Apprentice:** modular construction with explicit contracts and boundaries.
3. **Bot 3 — Independent Engineer:** requirements-first design with no prescribed architecture.

The outline is intentionally dependency-ordered rather than command-dictionary-ordered. A concept may therefore be introduced in a small form, revisited at a larger scale, and formalized only after the learner has concrete experience with it.

---

# PART I — LEARNING TO SEE THE LANGUAGE

## Chapter 1 — Before the First Rule
**Learning objective:** Replace the beginner's "code is a list of instructions" model with the correct first mental model: `.per` is a repeatedly evaluated rule-and-state machine whose behavior emerges from relationships.

**Introduce here:** the observation → state → rule → action → world loop; the distinction between syntax fluency and engineering fluency; the scale ladder `token → expression → rule → mechanism → state → subsystem → architecture → behavior`.

**Worked example:** one tiny `defrule` that reacts to a simple condition and changes an observable game state. Trace it literally, then trace what it means as a control loop.

**Exercise:** learner labels each part of a five-line rule as observation, condition, action, state, or world effect.

**Checkpoint:** explain, without looking at the chapter, the difference between "what this line does" and "why this mechanism exists."

---

## Chapter 2 — What a `.per` Program Actually Is
**Learning objective:** Understand the complete native-AI execution model before learning large syntax families.

**Introduce here:** WORLD → ENGINE OBSERVATION → `.per` FACTS/STATE → RULE EVALUATION → COMMAND/STATE WRITE → ENGINE EFFECT → WORLD.

**Worked example:** villager production from observation through command to the next observed villager count.

**Exercise:** draw the loop for one building command and identify which steps are proven versus merely assumed.

**Checkpoint:** distinguish AI state from world state and command acceptance from world-state completion.

---

## Chapter 3 — Your First Rule: Facts, Actions, and the Arrow
**Learning objective:** Read and write a minimal rule without treating syntax as magic.

**Introduce here:** `defrule`, condition/action separation, `=>`, basic predicates, basic actions, rule firing.

**Worked example:** a minimal train-if-capable rule, followed by a deliberate false-condition case.

**Exercise:** complete three partially written rules; then predict which fire before running them.

**Checkpoint:** for any rule, answer: what must be true, what changes, what state is touched, and what world effect should follow?

---

## Chapter 4 — The Seven Places Information Can Live
**Learning objective:** Build precise vocabulary for constants, goals, strategic numbers, timers, facts, rule-control state, and world state.

**Introduce here:** the seven-store model.

**Worked example:** the same conceptual value—"desired archers"—represented as a constant, goal, SN, and actual unit count; explain why those are not interchangeable.

**Exercise:** classify fifteen values from sample AI fragments.

**Checkpoint:** learner must stop saying "the variable" and identify the actual store for every value discussed.

---

## Chapter 5 — Constants, Goals, Strategic Numbers, and the Prefix Problem
**Learning objective:** Prevent one of the most damaging classes of `.per` bugs: reading or writing the wrong store while remaining syntactically valid.

**Introduce here:** `c:`, `g:`, `s:`; constant-as-value versus goal-as-storage; goal-to-goal copying versus writing a constant value.

**Worked example:** intentionally wrong prefix usage that produces a legal but semantically wrong result; repair it.

**Exercise:** trace five expressions and identify source store, destination store, and resulting value.

**Checkpoint:** learner can explain why parser acceptance does not establish semantic correctness.

---

## Chapter 6 — Passes, Source Order, and Why Time Exists Without a Clock
**Learning objective:** Understand repeated evaluation, source-order effects, disable/enable behavior, and positional control flow.

**Introduce here:** pass model, source-order sensitivity, positional jumps, rule-stream topology.

**Worked example:** a jump that skips a fixed number of rules; insert one rule and show why the destination changes.

**Exercise:** calculate the destination of several jump distances before and after an edit.

**Checkpoint:** identify a jump as a structural address, not a semantic label.

---

## Chapter 7 — Loading a Bot: The Moment a Folder Becomes a Program
**Learning objective:** Understand root files, load order, visibility, and the difference between file organization and state ownership.

**Introduce here:** `(load ...)`, root/load graph, dependency direction, modular versus monolithic organization.

**Worked example:** assemble a four-file miniature AI in dependency order.

**Exercise:** given a broken load graph, identify missing module and wrong-order failures.

**Checkpoint:** draw the root/load graph for the training bot and state what each module is allowed to assume about earlier modules.

---

## Chapter 8 — The First Debugging Habit: Never Guess What a Value Means
**Learning objective:** Move from suspicious-line debugging to state-centered investigation.

**Introduce here:** writer → reader tracing; state provenance; consumer identification; semantic naming.

**Worked example:** "bot trains too many skirmishers" traced backward from command to producer to demand to state writer.

**Exercise:** reconstruct the origin of one unexplained goal value from a sample corpus.

**Checkpoint:** learner produces a writer/reader chain rather than changing code by intuition.

---

# PART II — LEARNING TO SEE PATTERNS

## Chapter 9 — The Shape of an Experienced AI
**Learning objective:** Recognize recurring rule shapes before learning their names.

**Introduce here:** initialization, heartbeat, guard, latch, timer, search, dispatch, census, classification, demand, producer, recovery.

**Worked example:** three small mechanisms solving different problems but sharing the same control shape.

**Exercise:** classify unfamiliar rule blocks by shape, not by filename.

**Checkpoint:** learner can name the likely pattern from a new fragment and explain the evidence.

---

## Chapter 10 — One-Shot Initialization
**Learning objective:** Build reliable startup state without allowing initialization to overwrite live state later.

**Introduce here:** initialization guard, one-shot marker, default-state writes.

**Worked example:** initialize goals and enable a heartbeat exactly once.

**Exercise:** remove the initialization guard and observe/reset the resulting behavior.

**Checkpoint:** identify the complete lifecycle: trigger → writes → completion marker → permanent suppression.

---

## Chapter 11 — Heartbeats, Timers, and the Difference Between "Once" and "Again"
**Learning objective:** Understand recurring work as a lifecycle rather than a single timer command.

**Introduce here:** timer enable, timer condition, re-arm, cooldown, timeout, retry.

**Worked example:** periodic economy maintenance heartbeat.

**Exercise:** diagnose a heartbeat that fires once, a timer that never fires, and a timer that fires too often.

**Checkpoint:** every timer explanation must include owner, purpose, trigger, consumer, re-arm, and reset/expiry.

---

## Chapter 12 — Remembering What the World Just Told You
**Learning objective:** Understand why transient observations need persistent AI-side state.

**Introduce here:** event → state write → later reader; memory of observation; timestamp/age of information.

**Worked example:** remember that enemy cavalry was seen, then expire the observation.

**Exercise:** build a temporary "recent enemy archers" memory.

**Checkpoint:** distinguish current world fact from stored historical observation.

---

## Chapter 13 — Hysteresis, Cooldowns, and the Art of Not Changing Your Mind Too Quickly
**Learning objective:** Prevent oscillation caused by noisy or rapidly changing conditions.

**Introduce here:** entry threshold, exit threshold, cooldown, hysteresis, minimum dwell time.

**Worked example:** attack at one army threshold, retreat at a lower threshold.

**Exercise:** create an oscillating attack/retreat bot, then repair it with hysteresis.

**Checkpoint:** learner can identify the difference between a threshold and a state-stability mechanism.

---

## Chapter 14 — Loops, Search, and the Dangerous Beauty of Negative Jumps
**Learning objective:** Read native rule-stream loops and understand why negative jumps require topology-level reasoning.

**Introduce here:** cursor movement, backward jump, search cursor, loop termination, guard against infinite loops.

**Worked example:** search through candidate unit categories until one qualifies.

**Exercise:** trace a loop by hand and diagnose an infinite loop caused by a missing cursor update.

**Checkpoint:** learner can draw the rule topology and identify entry, body, progress, exit, and landing point.

---

## Chapter 15 — Guard-Skips and Computed Dispatch
**Learning objective:** Understand how native `.per` approximates structured control flow without conventional functions/switch statements.

**Introduce here:** guard-skip, mutually exclusive dispatch, computed jump, selector/state cursor.

**Worked example:** one strategic mode dispatches into three behavior regions.

**Exercise:** convert an overlapping set of rules into explicit mutually exclusive dispatch.

**Checkpoint:** explain why dispatch can be safer than allowing unrelated rule families to compete continuously.

---

## Chapter 16 — The Preprocessor: One Source, Several Programs
**Learning objective:** Understand compile-time specialization and its impact on rule topology.

**Introduce here:** conditional preprocessing, configuration-dependent rule existence, version/build variants, topology changes across configurations.

**Worked example:** one source producing two configurations with different rule regions.

**Exercise:** find a positional jump whose target changes under preprocessing.

**Checkpoint:** distinguish runtime state from source-configuration state.

---

## Chapter 17 — Deficit Correction and the Quiet Mathematics of Control
**Learning objective:** Recognize feedback control as a recurring AI design pattern.

**Introduce here:** target − current = deficit; bounded correction; minimum/maximum; proportional versus threshold-like behavior; saturation.

**Worked example:** desired military count versus current count.

**Exercise:** derive demand from a target and current census while preventing runaway demand.

**Checkpoint:** learner can explain a rule as a feedback controller rather than as an isolated `if` statement.

---

# PART III — HOW A BOT THINKS

## Chapter 18 — Observation Comes Before Strategy
**Learning objective:** Separate what the engine exposes from what the AI concludes.

**Introduce here:** observation layer; direct engine facts; observation freshness; observation versus interpretation.

**Worked example:** raw enemy unit observations without strategic response.

**Exercise:** list which facts are direct observations and which are interpretations.

**Checkpoint:** no strategic conclusion may be presented as an observation.

---

## Chapter 19 — Census: Turning a World Into Numbers
**Learning objective:** Build reliable counts that downstream systems can consume.

**Introduce here:** census queries, current counts, desired counts, infrastructure counts, enemy counts.

**Worked example:** count military categories and store results.

**Exercise:** build a small census for villagers, military, production buildings, and enemy cavalry.

**Checkpoint:** every census value has an identified writer, freshness behavior, and consumer.

---

## Chapter 20 — Classification: Turning Numbers Into Meaning
**Learning objective:** Turn observations into bounded strategic categories without confusing classification with policy.

**Introduce here:** classification states, threat categories, local-versus-global context, stale classification.

**Worked example:** enemy cavalry count → cavalry-pressure classification.

**Exercise:** classify a synthetic set of enemy observations and identify ambiguous cases.

**Checkpoint:** learner can show exactly where raw observation ends and classification begins.

---

## Chapter 21 — Capability Gaps and Requirements
**Learning objective:** Express strategy as a capability requirement rather than jumping directly from observation to command.

**Introduce here:** threat → capability gap → requirement; counter-unit requirement; infrastructure requirement.

**Worked example:** cavalry pressure → anti-cavalry requirement → spear demand.

**Exercise:** derive requirements for three threats without writing production commands.

**Checkpoint:** learner must produce a requirement artifact before implementation.

---

## Chapter 22 — Policy: What the Bot Wants
**Learning objective:** Separate desired strategic outcomes from engine execution.

**Introduce here:** policy state, targets, composition intent, economic priorities, strategic regimes.

**Worked example:** policy sets desired spearmen/skirmishers/archers without training them directly.

**Exercise:** rewrite a direct executor so that policy owns the desired quantity.

**Checkpoint:** learner identifies policy writer and executor reader separately.

---

## Chapter 23 — Authorization: What the Bot Is Actually Allowed to Do
**Learning objective:** Distinguish desire from permission.

**Introduce here:** authorization state, feasibility gates, emergency overrides, authority ownership.

**Worked example:** policy wants ten spearmen, but authorization permits only four because resources/infrastructure are constrained.

**Exercise:** add an authorization gate without changing policy intent.

**Checkpoint:** explain why a desired quantity is not itself an authorization.

---

## Chapter 24 — Execution: Let the Existing Machine Execute
**Learning objective:** Learn the boundary between cognition/authorization and the native executor.

**Introduce here:** executor as mechanical layer; command issuance; existing production/construction/military execution.

**Worked example:** policy → demand → existing producer → train command.

**Exercise:** trace a command all the way to its native executor and identify which layer should be modified when behavior is wrong.

**Checkpoint:** no new strategic logic is placed inside an executor merely because the executor is convenient.

---

## Chapter 25 — Verification: Did the World Change?
**Learning objective:** Make verification a first-class engineering stage.

**Introduce here:** command acceptance versus world effect; pending object; completion observation; verification windows.

**Worked example:** construction command issued, but building count remains unchanged; classify the result as unverified rather than complete.

**Exercise:** create a verification rule for a trained unit and one for a completed building.

**Checkpoint:** learner can state what evidence is sufficient to promote an intended action to completed world state.

---

## Chapter 26 — Reassessment: The Bot's Most Important Habit
**Learning objective:** Close the loop and prevent stale decisions.

**Introduce here:** verification → capability coverage → reassessment; state refresh; re-entry after failure.

**Worked example:** cavalry threat disappears after counter-production; demand should fall rather than persist forever.

**Exercise:** repair a demand state that remains permanently elevated.

**Checkpoint:** learner draws the full loop and identifies where stale state can survive.

---

# PART IV — HOW MATURE BOTS ARE ORGANIZED

## Chapter 27 — Why There Are So Many Files
**Learning objective:** Understand file boundaries as a human engineering tool.

**Introduce here:** module purpose, cohesion, dependency direction, root graph.

**Worked example:** split the Bot 1 monolith into conceptual modules without changing behavior.

**Exercise:** propose module boundaries for economy, military, observation, and recovery.

**Checkpoint:** every proposed module has a reason for existing beyond "clean code."

---

## Chapter 28 — Module Boundaries Are Not State Boundaries
**Learning objective:** Prevent the common mistake of equating separate files with separate ownership.

**Introduce here:** shared state, cross-module writers, state contracts.

**Worked example:** two modules in separate files both writing the same goal.

**Exercise:** construct a writer/reader graph and identify hidden coupling.

**Checkpoint:** learner can state which module owns a state variable independently of where the variable is physically referenced.

---

## Chapter 29 — Initialization, Maintenance, Policy, Execution, Telemetry, Arbitration, Recovery
**Learning objective:** Learn the major functional roles that recur in mature AIs.

**Introduce here:** seven-role architectural vocabulary.

**Worked example:** map Bot 1's rules into these roles.

**Exercise:** classify a mixed Stock/Naga fragment into roles and explain ambiguous cases.

**Checkpoint:** role classification is based on behavior and authority, not filename.

---

## Chapter 30 — Producer and Consumer
**Learning objective:** Understand decoupled demand/production as a reusable architectural pattern.

**Introduce here:** producer, consumer, desired quantity, current quantity, stop condition, reconciliation.

**Worked example:** desired archer count written by policy and consumed by a military producer.

**Exercise:** build a producer/consumer pair for a construction requirement.

**Checkpoint:** identify writer, reader, unit of quantity, termination condition, and stale-demand failure mode.

---

## Chapter 31 — Dials: Separating Desire From Feasibility
**Learning objective:** Understand tunable production targets as interfaces rather than commands.

**Introduce here:** production dials, target quantities, floors, ceilings, priority changes.

**Worked example:** policy changes a dial while executor remains unchanged.

**Exercise:** create three policy states that alter dials but share one executor.

**Checkpoint:** learner explains why dials are valuable only when their ownership and consumers are clear.

---

## Chapter 32 — Reservation, Escrow, and the Difference Between Intention and Money
**Learning objective:** Separate policy reserve, logical commitment, physical escrow, authorization, and execution accounting.

**Introduce here:** the ledger model; physical escrow; commitment lifecycle; resource reconciliation.

**Worked example:** a unit is desired, logically committed, physically escrowed, then trained; show every ledger transition.

**Exercise:** diagnose resource drift caused by decrementing a policy target instead of reconciling physical escrow.

**Checkpoint:** learner can state which ledger is authoritative for each question: "what do we want?", "what have we promised?", "what resources are actually reserved?", "what happened?"

---

## Chapter 33 — Ownership: The Question That Solves More Bugs Than Another Rule
**Learning objective:** Make ownership the first architectural debugging question.

**Introduce here:** single-writer principle; semantic owner; executor owner; observer owner; authority owner.

**Worked example:** two competing writers create oscillation.

**Exercise:** assign owners to a state registry and resolve three ownership conflicts.

**Checkpoint:** learner cannot add a new writer without documenting why ownership permits it.

---

## Chapter 34 — Competing Writers and Shared State
**Learning objective:** Diagnose arbitration failures created by multiple writers.

**Introduce here:** precedence, conflict, overwrite order, temporal races, source-order races.

**Worked example:** military policy and emergency defense both write a composition target.

**Exercise:** determine final state from competing rule families across several passes.

**Checkpoint:** distinguish deterministic precedence from accidental source-order victory.

---

## Chapter 35 — Authority and Arbitration
**Learning objective:** Separate the right to decide from the mechanisms that execute the decision.

**Introduce here:** authority graph, arbitration, precedence, emergency override, authority versus execution.

**Worked example:** economy, technology, and military all competing for the same capital.

**Exercise:** design an arbitration table with explicit precedence and expiry.

**Checkpoint:** every shared resource decision has a named authority and conflict rule.

---

## Chapter 36 — State Lifecycles: Birth, Use, Staleness, Expiry, Re-entry
**Learning objective:** Treat state as a lifecycle, not a static value.

**Introduce here:** state birth, valid period, stale period, expiry, reset, re-entry, reconciliation.

**Worked example:** threat classification with a finite validity window.

**Exercise:** repair a stale commitment and a stale threat state.

**Checkpoint:** learner can produce a lifecycle table for any nontrivial state variable.

---

## Chapter 37 — Failure Containment and Recovery
**Learning objective:** Design recovery so that one failed subsystem does not corrupt unrelated strategic state.

**Introduce here:** watchdog, timeout, retry, rollback/reconciliation, safe reset, recovery ownership.

**Worked example:** production infrastructure destroyed while military demand remains active.

**Exercise:** build a recovery path that restores infrastructure without erasing strategic intent.

**Checkpoint:** distinguish cancellation, pause, retry, recovery, and re-planning.

---

# PART V — THREE ARCHITECTURES WORTH STUDYING

## Chapter 38 — The Stock AI: A Large Historical Machine
**Learning objective:** Read Stock as a corpus of evolved solutions rather than as a style guide.

**Introduce here:** Stock's directness, large rule families, broad state, timing assumptions, historical accumulation, direct policy/execution coupling where observed.

**Worked example:** trace one real Stock capability from condition through commands and downstream state.

**Exercise:** reconstruct a Stock subsystem without changing it.

**Checkpoint:** distinguish engine requirement, Stock convention, historical artifact, and inferred intent.

---

## Chapter 39 — Naga: Modularity, Libraries, and Reusable Control Structures
**Learning objective:** Read Naga as an architectural response to complexity.

**Introduce here:** root/load graph, helper libraries, domain modules, reusable control structures, shared contracts.

**Worked example:** trace one Naga subsystem across root, helper, state, policy, and executor.

**Exercise:** produce a Naga module card: purpose, inputs, outputs, owner, dependencies, consumers, failure modes.

**Checkpoint:** learner explains what problem each boundary solves and which boundaries remain coupled.

---

## Chapter 40 — Shadow: Density, Scale, and the Power of a Monolith
**Learning objective:** Demonstrate that modularity is not synonymous with capability or correctness.

**Introduce here:** monolithic rule streams, density, zero-load architecture, structural reconstruction from source order.

**Worked example:** find a subsystem in a large monolithic corpus and reconstruct its boundaries from rule relationships.

**Exercise:** identify implicit modules inside a monolith.

**Checkpoint:** learner can read architecture from behavior even when filenames provide no help.

---

## Chapter 41 — Reading the Same Problem in Three Architectural Dialects
**Learning objective:** Learn variation through direct comparison rather than imitation.

**Introduce here:** Stock vs Naga vs Shadow comparison method.

**Worked example:** solve the same production problem three ways and trace observation, state, authority, execution, and verification in each.

**Exercise:** complete a three-column comparison card.

**Checkpoint:** identify which pieces are engine necessities and which are architectural choices.

---

## Chapter 42 — Writing Style as Engineering Evidence
**Learning objective:** Learn to infer design history cautiously from source organization without treating stylistic evidence as proof.

**Introduce here:** evidence hierarchy applied to source style; DIRECT/COMPOSED/INFERRED/AEGIS-GENERALIZATION/UNCERTAIN.

**Worked example:** compare repeated rule idioms and distinguish observed pattern from inferred intent.

**Exercise:** label claims about a real source by evidence class.

**Checkpoint:** no architectural conclusion is accepted without an evidence label.

---

## Chapter 43 — Why Good Engineers Sometimes Leave Ugly Code Alone
**Learning objective:** Understand load-bearing legacy behavior, compatibility constraints, and the difference between improvement and unnecessary refactoring.

**Introduce here:** preservation boundary, behavior-preserving refactor, structural risk, forensic freeze.

**Worked example:** a tuned jump region that looks ugly but is behaviorally coupled to its topology.

**Exercise:** decide which of several ugly fragments should be left untouched and which can be safely isolated.

**Checkpoint:** learner must justify a refactor using evidence and risk, not aesthetics.

---

# PART VI — THE CORPUS AS A TEXTBOOK

## Chapter 44 — What the Symbol Corpus Teaches
**Learning objective:** Use a command/symbol corpus as evidence for engine capability without mistaking documentation for runtime proof.

**Introduce here:** symbol reference, command contract, evidence hierarchy, authoritative versus secondary evidence.

**Worked example:** take one command from the symbol corpus and trace it into a real AI use.

**Exercise:** create a command evidence card with syntax, inputs, effects, failure modes, and confidence.

**Checkpoint:** distinguish "the engine exposes this" from "this AI uses it successfully."

---

## Chapter 45 — Reading a Symbol Without Turning It Into a Dictionary Entry
**Learning objective:** Connect commands to the systems that make them useful.

**Introduce here:** command → preconditions → state → executor → world effect → verification.

**Worked example:** a train command embedded in a production lifecycle.

**Exercise:** explain a symbol in architectural terms rather than defining it.

**Checkpoint:** every command explanation identifies at least one producer of its inputs and one verifier of its effect.

---

## Chapter 46 — Command Contracts and Failure Modes
**Learning objective:** Treat commands as contracts with preconditions and observable consequences.

**Introduce here:** accepted, rejected, deferred, partially effective, completed, unverified.

**Worked example:** command accepted but resulting object absent.

**Exercise:** classify several hypothetical command outcomes.

**Checkpoint:** learner never equates command issuance with completion.

---

## Chapter 47 — Timers as Control-System Components
**Learning objective:** Move from timer syntax to temporal architecture.

**Introduce here:** timer state machine; periodic sampling; debounce/cooldown; freshness windows.

**Worked example:** threat telemetry with a validity interval.

**Exercise:** design a timer lifecycle for a periodic census.

**Checkpoint:** explain why timer ownership is part of subsystem ownership.

---

## Chapter 48 — Goals as Software State
**Learning objective:** Treat goals as a native state machine substrate.

**Introduce here:** state IDs, enum-like states, counters, cursors, modes, bookmarks, sentinels.

**Worked example:** military regime state machine.

**Exercise:** encode a five-state lifecycle using goals and guards.

**Checkpoint:** identify legal transitions and impossible states.

---

## Chapter 49 — Strategic Numbers as Engine-Facing State
**Learning objective:** Understand SNs as a distinct state interface with engine-facing consequences.

**Introduce here:** SN ownership, slot semantics, command-side use, strategic configuration versus runtime state.

**Worked example:** a real strategic-number writer/reader chain.

**Exercise:** distinguish SN, goal, and constant in ambiguous code.

**Checkpoint:** learner documents semantic ownership before allocating a new slot.

---

## Chapter 50 — Jumps as a Native Control-Flow Language
**Learning objective:** Read positional jumps as structured control flow encoded directly in the rule stream.

**Introduce here:** topology, relative addressing, computed dispatch, loop construction, jump fragility.

**Worked example:** reconstruct a nontrivial jump region into pseudo-code and then back into `.per`.

**Exercise:** safely insert a rule into a jump-heavy region and revalidate all destinations.

**Checkpoint:** learner can explain a jump region without relying on the original author's comments.

---

## Chapter 51 — Common Idioms and What They Reveal
**Learning objective:** Build pattern-recognition fluency.

**Introduce here:** initialization guards, heartbeats, latches, deficit correction, producer/consumer, census/classification, dispatch, watchdogs, recovery, compatibility adapters.

**Worked example:** ten short idioms from Stock/Naga-like corpora.

**Exercise:** identify the idiom and reconstruct its lifecycle.

**Checkpoint:** learner can recognize a known pattern in unfamiliar code without blindly copying it.

---

## Chapter 52 — Negative Knowledge: Learning From What Does Not Work
**Learning objective:** Make failure evidence part of engineering knowledge.

**Introduce here:** parser-valid but wrong, stale state, duplicate writers, wrong load order, broken jumps, missing re-arm, orphaned demand, unverified command, preprocessor-specific breakage.

**Worked example:** one failed design reconstructed from symptom → hypothesis → test → evidence → repair.

**Exercise:** maintain a failure notebook with symptom, violated contract, evidence, repair, and prevention rule.

**Checkpoint:** learner can explain not only the working pattern but the tempting incorrect alternative and why it fails.

---

# PART VII — BECOMING AN ENGINEER

## Chapter 53 — The Eleven Failures of Local Reasoning
**Learning objective:** Recognize when a bug cannot be solved by editing the suspicious line.

**Introduce here:** hidden coupling, wrong owner, stale state, source-order dependency, wrong store, authority conflict, missing consumer, missing verifier, lifecycle leak, resource-accounting divergence, recovery corruption.

**Worked example:** one symptom with three plausible local fixes, only one of which preserves architecture.

**Exercise:** choose the correct investigation layer for eleven failure scenarios.

**Checkpoint:** learner must state the first question before proposing a code change.

---

## Chapter 54 — Engineering Mysteries
**Learning objective:** Practice evidence-driven diagnosis under incomplete information.

**Introduce here:** hypothesis table; evidence collection; competing explanations; confidence updates.

**Worked example:** "bot suddenly stops producing military at 18:00" with incomplete telemetry.

**Exercise:** investigate several mysteries while explicitly labeling DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, or UNCERTAIN conclusions.

**Checkpoint:** no hypothesis may be promoted to fact without supporting evidence.

---

## Chapter 55 — How to Read an Unfamiliar AI Without Getting Lost
**Learning objective:** Develop a repeatable forensic reading procedure.

**Introduce here:** root → load graph → registries → state → writers/readers → control flow → subsystem boundaries → world effects.

**Worked example:** cold-read a small unfamiliar AI in stages, deliberately postponing details until architecture is visible.

**Exercise:** produce a one-page architecture map before reading individual rules deeply.

**Checkpoint:** learner can locate the likely owner of a behavior without reading the entire corpus linearly.

---

## Chapter 56 — How to Design a Bot From a Blank Folder
**Learning objective:** Begin independent architecture design from requirements rather than from copied code.

**Introduce here:** requirements decomposition; capability model; state contracts; architecture decision record; implementation order.

**Worked example:** design a bot requiring economy, age progression, military composition, threat response, and recovery.

**Exercise:** produce architecture, registry, lifecycle model, authority map, and verification plan before writing implementation.

**Checkpoint:** design review must pass before Bot 3 implementation begins.

---

## Chapter 57 — How to Add a Subsystem to a Living Bot
**Learning objective:** Extend an existing AI without violating hidden contracts.

**Introduce here:** insertion procedure; dependency audit; writer/reader audit; authority audit; load-order audit; verification plan.

**Worked example:** add a threat-classification subsystem to an existing military bot without owning production execution.

**Exercise:** add one subsystem using a formal module contract.

**Checkpoint:** learner demonstrates that the new subsystem has no undocumented writer conflict and has an observable verification path.

---

## Chapter 58 — How to Refactor Without Destroying Load-Bearing Behavior
**Learning objective:** Perform behavior-preserving change in a positional, stateful language.

**Introduce here:** freeze boundaries; semantic equivalence; topology preservation; migration staging; compatibility adapters.

**Worked example:** extract a repeated rule family into a module while preserving order-sensitive behavior.

**Exercise:** refactor a small subsystem and prove that its writer/reader and control-flow graphs remain equivalent.

**Checkpoint:** refactor is accepted only with structural and behavioral evidence.

---

## Chapter 59 — How to Prove a Change Worked
**Learning objective:** Build a verification hierarchy rather than relying on parser success or one successful replay.

**Introduce here:** syntax validation, static contract checks, dependency checks, runtime evidence, world-state verification, regression comparison.

**Worked example:** a production change that parses successfully but fails to increase completed unit count.

**Exercise:** construct a verification plan for a new subsystem.

**Checkpoint:** learner states exactly what evidence would falsify their claim that the change works.

---

## Chapter 60 — From Syntax to Systems: The Three-Bot Apprenticeship
**Learning objective:** Integrate the entire curriculum through the three builds.

**Introduce here:** progressive scaffolding and comparison methodology.

**Worked example:** revisit one identical problem—adaptive military production—in Bot 1, Bot 2, and Bot 3.

**Exercise:** learner fills a three-bot comparison notebook: mechanism, state, authority, executor, verification, failure modes, and architectural rationale.

**Checkpoint:** learner must explain what was learned from the variation itself, not merely what each bot contains.

---

## Chapter 61 — Intuition Drills
**Learning objective:** Convert explicit reasoning into faster recognition without abandoning evidence discipline.

**Introduce here:** recognition → explanation → completion → repair → generation progression.

**Worked examples:** rapid diagnosis cards involving timers, stores, jumps, demand, ownership, authority, and verification.

**Exercise:** timed retrieval rounds followed by full written justification.

**Checkpoint:** speed is scored only after correctness and explanation are established; no intuition is accepted as proof.

---

## Chapter 62 — Graduation Examination
**Learning objective:** Demonstrate independent `.per` engineering competence.

**Exam components:**

1. Read an unfamiliar Stock-style subsystem.
2. Read an unfamiliar Naga-style module.
3. Trace a strategic requirement through state to execution.
4. Diagnose a replay symptom from incomplete evidence.
5. Safely modify a production target.
6. Design a new subsystem.
7. Define state ownership and lifecycle.
8. Identify authority conflicts.
9. Prove a command-to-world-state transition.
10. Design recovery for an interrupted plan.

**Final exercise:** repair a deliberately damaged AI containing multiple simultaneous defects.

**Checkpoint:** graduation requires correct diagnosis, safe implementation, evidence-backed verification, and an explanation of why the chosen architecture is appropriate.

---

## Chapter 63 — The Professional Standard
**Learning objective:** Establish the permanent engineering standard the reader carries beyond the book.

**Introduce here:** the complete engineering loop:

`WORLD → OBSERVATION → CLASSIFICATION → CAPABILITY GAP → REQUIREMENT → EXECUTABLE CANDIDATES → ENGINE COST VECTOR → CAPITAL DEMAND → ARBITRATION → LOGICAL COMMITMENT → SHADOW ECONOMIC STATE → PHYSICAL ESCROW → AUTHORITY → EXISTING EXECUTOR → WORLD-STATE RESULT → VERIFICATION → CAPABILITY COVERAGE → REASSESSMENT`

**Worked example:** reconstruct a complete subsystem using the full loop.

**Exercise:** learner writes a professional subsystem specification before implementation.

**Checkpoint:** the reader is considered competent only when they can move in both directions:

- source → mechanism → architecture → behavior;
- requirement → capability → state contract → module → implementation → verification → recovery.

The final lesson is not "know `.per`." It is: **be able to discover, construct, test, explain, and safely change a native AI whose internal design you did not write.**

---

# APPENDIX A — DESIGN VOCABULARY

Purpose: compact terminology after the learner has encountered every term in context.

Include concise definitions for: rule, condition, action, fact, constant, goal, strategic number, timer, pass, source order, jump, guard, latch, heartbeat, census, classification, requirement, policy, demand, feasibility, arbitration, commitment, escrow, authorization, producer, consumer, executor, verification, reconciliation, watchdog, recovery, telemetry, compatibility adapter, module, contract, authority, lifecycle, topology.

**Teaching rule:** no appendix definition may be the learner's first exposure to a concept. The concept must already have appeared in a chapter and worked example.

---

# APPENDIX B — THE ENGINEER'S TRACE SHEET

Provide reusable blank forms for:

- rule trace;
- state trace;
- writer/reader graph;
- timer lifecycle;
- jump topology;
- module contract;
- authority matrix;
- producer/consumer chain;
- command verification chain;
- failure investigation;
- evidence classification;
- three-bot comparison card.

---

# APPENDIX C — EVIDENCE AND VERIFICATION CHECKLISTS

Provide checklists for:

- parser/static validity;
- symbol/command evidence;
- dependency/load-order validation;
- duplicate writer detection;
- state lifecycle completeness;
- authority completeness;
- resource/escrow reconciliation;
- command-to-world verification;
- replay evidence;
- regression evidence;
- uncertainty labeling.

The appendix should reinforce the permanent rule:

**accepted by the parser ≠ semantically correct ≠ executed ≠ completed ≠ verified.**

---

# APPENDIX D — RECOMMENDED PRACTICE PROJECTS

Projects should be deliberately cumulative and interleaved.

### Project 1 — Tiny Living AI
Build the smallest functioning `.per` AI with initialization, one heartbeat, one state variable, and one observable action.

### Project 2 — Economic Skeleton
Add villager production, basic resource priorities, housing, and age progression.

### Project 3 — Stock Apprentice
Complete Bot 1 through direct rule families.

### Project 4 — Stock Forensic Reconstruction
Ignore the learner's implementation and reconstruct a real Stock subsystem from source evidence.

### Project 5 — Naga Module
Build one modular subsystem with an explicit contract and registry.

### Project 6 — Naga Fault Injection
Repair duplicate writers, missing loads, stale state, broken producer/consumer links, and authority conflicts.

### Project 7 — Three-Way Reconstruction
Implement one requirement in Stock-like, Naga-like, and independent forms and compare the resulting control graphs.

### Project 8 — Independent Bot
Design Bot 3 from requirements only.

### Project 9 — Adversarial Maintenance
Given an unfamiliar AI and a behavioral symptom, diagnose and repair it without rewriting unrelated systems.

### Project 10 — Teach It Back
The learner must explain one subsystem to another engineer using the full trace model. Teaching becomes the final retrieval test.

---

# MASTER CONCEPT-INTRODUCTION MAP

This table is the canonical answer to "when does the learner first need to know this?"

| Concept | First introduction | First concrete use | First deliberate break | First retrieval without naming it | Independent use |
|---|---|---|---|---|---|
| Rule anatomy | Ch. 3 | Ch. 3 | Ch. 3 | Ch. 8 | Ch. 56 |
| Constants | Ch. 5 | Ch. 5 | Ch. 5 | Ch. 8 | Ch. 56 |
| Goals/state | Ch. 4 | Ch. 10 | Ch. 10 | Ch. 21 | Ch. 56 |
| Strategic numbers | Ch. 5 | Ch. 5 | Ch. 5 | Ch. 49 | Ch. 56 |
| Timers | Ch. 11 | Ch. 11 | Ch. 11 | Ch. 26 | Ch. 56 |
| Source order | Ch. 6 | Ch. 6 | Ch. 6 | Ch. 50 | Ch. 58 |
| Loads/modules | Ch. 7 | Ch. 7 | Ch. 7 | Ch. 27 | Ch. 56 |
| Initialization | Ch. 10 | Bot 1 Lesson 1 | Ch. 10 | Ch. 53 | Ch. 56 |
| Heartbeat | Ch. 11 | Ch. 11 | Ch. 11 | Ch. 51 | Ch. 56 |
| State memory | Ch. 12 | Ch. 12 | Ch. 12 | Ch. 20 | Ch. 56 |
| Hysteresis | Ch. 13 | Ch. 13 | Ch. 13 | Ch. 37 | Ch. 60 |
| Jumps/loops | Ch. 14 | Ch. 14 | Ch. 14 | Ch. 50 | Ch. 58 |
| Dispatch | Ch. 15 | Ch. 15 | Ch. 15 | Ch. 51 | Ch. 56 |
| Preprocessor | Ch. 16 | Ch. 16 | Ch. 16 | Ch. 53 | Ch. 58 |
| Feedback/deficit | Ch. 17 | Ch. 17 | Ch. 17 | Ch. 30 | Ch. 56 |
| Observation | Ch. 18 | Ch. 18 | Ch. 18 | Ch. 53 | Ch. 56 |
| Census | Ch. 19 | Ch. 19 | Ch. 19 | Ch. 41 | Ch. 56 |
| Classification | Ch. 20 | Ch. 20 | Ch. 20 | Ch. 54 | Ch. 56 |
| Requirement | Ch. 21 | Ch. 21 | Ch. 21 | Ch. 54 | Ch. 56 |
| Policy | Ch. 22 | Ch. 22 | Ch. 22 | Ch. 53 | Ch. 56 |
| Authorization | Ch. 23 | Ch. 23 | Ch. 23 | Ch. 35 | Ch. 56 |
| Execution boundary | Ch. 24 | Ch. 24 | Ch. 24 | Ch. 57 | Ch. 56 |
| Verification | Ch. 25 | Ch. 25 | Ch. 25 | Ch. 46 | Ch. 56 |
| Reassessment | Ch. 26 | Ch. 26 | Ch. 26 | Ch. 52 | Ch. 56 |
| Module contracts | Ch. 28 | Ch. 39 | Ch. 39 | Ch. 57 | Ch. 56 |
| Producer/consumer | Ch. 30 | Ch. 30 | Ch. 30 | Ch. 53 | Ch. 56 |
| Dials | Ch. 31 | Ch. 31 | Ch. 31 | Ch. 41 | Ch. 56 |
| Commitment | Ch. 32 | Ch. 32 | Ch. 32 | Ch. 54 | Ch. 56 |
| Escrow | Ch. 32 | Ch. 32 | Ch. 32 | Ch. 53 | Ch. 56 |
| Ownership | Ch. 33 | Ch. 33 | Ch. 33 | Ch. 53 | Ch. 56 |
| Arbitration | Ch. 35 | Ch. 35 | Ch. 35 | Ch. 54 | Ch. 56 |
| Lifecycle | Ch. 36 | Ch. 36 | Ch. 36 | Ch. 53 | Ch. 56 |
| Recovery | Ch. 37 | Ch. 37 | Ch. 37 | Ch. 54 | Ch. 56 |
| Stock architecture | Ch. 38 | Ch. 38 | Ch. 38 | Ch. 41 | Ch. 56 |
| Naga architecture | Ch. 39 | Ch. 39 | Ch. 39 | Ch. 41 | Ch. 56 |
| Monolithic architecture | Ch. 40 | Ch. 40 | Ch. 40 | Ch. 41 | Ch. 56 |
| Evidence taxonomy | Ch. 42 | Ch. 42 | Ch. 42 | Ch. 54 | Ch. 56 |
| Command contracts | Ch. 46 | Ch. 46 | Ch. 46 | Ch. 59 | Ch. 56 |
| Professional verification | Ch. 59 | Ch. 59 | Ch. 59 | Ch. 62 | Ch. 63 |

---

# MASTER SCAFFOLDING MAP

The instructor's behavior must change as the learner advances.

## Chapters 1–17 — Heavy scaffolding

- Show complete mechanisms.
- Explain every interacting element.
- Ask prediction questions before execution.
- Provide exact file/rule locations for exercises.
- Use small, clean examples.
- Correct misconceptions immediately.

**Learner mode:** recognize → explain → complete.

## Chapters 18–37 — Guided construction

- Start from a concrete capability problem.
- Build the mechanism collaboratively.
- Remove one or two implementation details from worked examples.
- Require writer/reader and lifecycle maps.
- Introduce cross-subsystem reasoning.

**Learner mode:** explain → complete → repair.

## Chapters 38–52 — Corpus apprenticeship

- Replace invented examples with real Stock/Naga/Shadow evidence where available.
- Ask the learner to predict architecture before revealing it.
- Compare multiple implementations of the same requirement.
- Require evidence labels.

**Learner mode:** discriminate → trace → diagnose.

## Chapters 53–60 — Faded guidance

- Give symptoms and requirements, not solutions.
- Learner chooses investigation order.
- Learner proposes architecture before implementation.
- Instructor reviews contracts and failure models rather than supplying code.

**Learner mode:** diagnose → design → implement → verify.

## Chapters 61–63 — Independent engineering

- Minimal hints.
- Adversarial review.
- Unknown code.
- Incomplete evidence.
- Multiple valid architectures allowed if defended and verified.

**Learner mode:** generate → defend → teach.

---

# REQUIRED RECURRING PEDAGOGICAL LOOP

Every major concept chapter should contain these nine beats, even when compressed:

1. **Problem:** show a bot behavior that requires the concept.
2. **Prediction:** ask what the learner thinks will happen.
3. **Smallest mechanism:** show the minimum working implementation.
4. **Literal trace:** walk condition → action → state → next pass.
5. **Name the pattern:** give the formal engineering term only after concrete understanding exists.
6. **Connection:** trace writer → reader → executor → world effect.
7. **Break:** deliberately remove or corrupt one mechanism.
8. **Repair:** learner fixes the defect.
9. **Transfer:** learner identifies another subsystem where the same pattern applies.

Then, several chapters later, retrieve the concept without naming it.

---

# REQUIRED THREE-BOT REPETITION MATRIX

The following problems must appear in all three bots so the learner can discriminate architecture from engine necessity:

| Problem | Bot 1 | Bot 2 | Bot 3 |
|---|---|---|---|
| Initialization | direct startup rules | initialization module | architecture chosen by learner |
| Economy | direct priorities | economic domain + policy/producer split | independent resource model |
| Construction | direct requirement → command | requirement/producer/verification modules | learner-designed construction architecture |
| Military production | direct production rules | demand/producer + arbitration | learner-designed composition controller |
| Scouting | direct observation state | observation/classification modules | learner-designed telemetry model |
| Threat response | direct response rules | classification → requirement → policy | independent capability-gap design |
| Timers | local timer logic | lifecycle-owned timers | learner defines temporal model |
| State | broad goals | registered contracts | learner defines state model |
| Authority | mostly implicit | explicit ownership/arbitration | learner must prove authority graph |
| Escrow | minimal/direct | explicit ledger model | learner chooses and verifies accounting model |
| Verification | simple world checks | formal verification boundaries | evidence-driven proof plan |
| Recovery | direct rebuild/retry | watchdog/recovery modules | independent failure architecture |

The point of repetition is not redundancy. It is **contrast**. The learner should eventually be able to look at a mechanism and say: "This part exists because the engine requires it; this part exists because the author chose this architecture; this part exists because an earlier implementation failed and left a compatibility scar."

---

# FINAL EDITORIAL RULES FOR DOC2

1. Do not teach the language as a dictionary.
2. Do not introduce an abstraction before the reader has seen the concrete problem it solves.
3. Do not let Stock become a template to copy blindly.
4. Do not let Naga become a collection of filenames to imitate.
5. Use Shadow to prove that architecture can be reconstructed from behavior even without modular files.
6. Make the learner predict behavior before revealing the answer.
7. Make the learner break working systems deliberately.
8. Make every important state have an owner and lifecycle.
9. Make every important command have a verification path.
10. Treat parser validity, runtime acceptance, world-state completion, and strategic success as separate claims.
11. Revisit important concepts instead of teaching them once.
12. Increase only one or two complexity axes at a time: syntax, state, time, control flow, architecture, uncertainty, debugging.
13. Move from recognition to explanation to repair to generation.
14. Preserve uncertainty labels wherever evidence is incomplete.
15. Use real source artifacts whenever possible; invented examples are scaffolding, not evidence.
16. Every module must be taught as a solution to a human/system boundary problem, not as a folder convention.
17. Every major subsystem should eventually be read in both directions: source → behavior and requirement → implementation.
18. The final product is not a reader who knows more commands. It is an engineer who can reconstruct, design, verify, repair, and safely extend a native AoE2DE AI.
