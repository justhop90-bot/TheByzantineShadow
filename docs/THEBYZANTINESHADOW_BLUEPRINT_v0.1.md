# The Byzantine Shadow — Blueprint v0.1

## Purpose

The Byzantine Shadow is the economic commitment and escrow substrate for AEGIS. It is not a second strategic brain and it is not a replacement executor. Its job is to convert authorized strategic requirements into disciplined economic reservations, bounded execution authority, and independently verified resource transactions.

The target control loop is:

WORLD → OBSERVE → CLASSIFY → BELIEF → OBJECTIVE → CAPABILITY REQUIREMENT → COMMITMENT → RESOURCE REQUIREMENT → RESOURCE CONTROL → SAVE / ESCROW → FEASIBILITY → AUTHORITY → EXECUTOR → STATE MUTATION → VERIFY → RELEASE / CONSUME / RETAIN → REASSESS.

AEGIS owns strategic interpretation and objective selection. Byzantine policy owns civilization-specific doctrine. The Byzantine Shadow owns economic commitment discipline. AIByzBuild remains the production/build executor.

## Evidence Doctrine

Every claim must be tagged DIRECT, COMPOSED, INFERRED, AEGIS-GENERALIZATION, or UNCERTAIN, with optional CONFIRMED, PROBABLE, PLAUSIBLE, DISPROVEN, OBSOLETE, ENGINE-SPECIFIC, or HISTORICAL status.

Never promote command acceptance to state mutation, state mutation to strategic success, or historical donor behavior to guaranteed current-engine semantics without evidence.

## Donor Mechanisms

KEEP/ADAPT:
- `set-strategic-number sn-resource-control` as an economic actuator/lock.
- `set-escrow-percentage` and native escrow accounting.
- `escrow-amount` as observable reservation state.
- `release-escrow` for reservation release.
- `can-train-with-escrow` for escrow-aware training feasibility.
- `can-research-with-escrow` for escrow-aware research feasibility.
- `can-build-with-escrow` where current-engine availability is qualified.
- `up-modify-escrow` / `up-release-escrow` where qualified.
- Shadow save-resource sequencing around strategic commitments.
- Rule-order arbitration: condition → state/authority mutation → affordability → escrow release → executor → reset/retry.

REPLACE/FORMALIZE:
- implicit commitment ownership;
- unbounded reservations;
- hidden cancellation;
- hidden expiry;
- blind global escrow release;
- strategic decisions embedded inside production rules;
- verification by command issuance alone;
- unregistered goal/SN namespaces;
- duplicate executors;
- donor conventions treated as engine law.

## Module Map

### 00_bs_constants.per — Namespace / ABI Registry
Reserve every Shadow goal, strategic number, state, channel, priority, threshold, transaction state, and composition identifier. Every mutable symbol has one canonical owner and an explicit writer policy. Undefined or duplicate control-plane symbols are qualification failures until classified.

### 01_bs_state.per — Economic State Model
Separate observed state, desired state, authority state, transaction state, and verification state. Track current resources, escrow, free capacity, active commitments, transaction status, pressure, and starvation indicators.

### 02_bs_resource_control.per — Economic Actuator
Retain `sn-resource-control`, but make it an economic actuator rather than a strategic-objective namespace. Every writer must identify its owning commitment. Clearing, reset, expiry, and preemption semantics must be explicit.

### 03_bs_escrow.per — Reservation Engine
Use native escrow primitives as the funding substrate. Logical channels are BASE, SURVIVAL, MILITARY, STRATEGIC, and EMERGENCY. Strategic semantics live in commitment state; escrow represents funding capacity, not strategic intent.

### 04_bs_saving.per — Saving / Affordability
Translate requirements into save-resource behavior. Canonical sequence: COMMITMENT → REQUIREMENT → RESOURCE CONTROL → SAVE → ESCROW → AFFORDABILITY. Saving must be bounded by starvation and expiry rules.

### 05_bs_commitment.per — Commitment Lifecycle
Explicit lifecycle: CANDIDATE → PREPARING → COMMITTED → FUNDED → EXECUTING → VERIFIED → RETIRING → RETIRED. Exceptional exits: CANCELLED, EXPIRED, INVALIDATED, PREEMPTED, FAILED, BLOCKED. Each commitment requires owner, purpose, priority, requirements, activation, release, expiry, verification, and fallback predicates.

### 06_bs_hysteresis.per — Anti-Oscillation
Every reversible commitment gets activation, maintain, and release thresholds; optionally a minimum dwell time. Emergency override is explicit. Thresholds are empirical parameters, not axioms.

### 07_bs_cancellation.per — Cancellation
Terminate commitments cleanly, release only attributable escrow, restore resource-control state, and force reassessment. Causes include invalid objective, vanished threat, starvation, higher-priority emergency, completed transition, lost feasibility, executor failure, and timeout.

### 08_bs_expiry.per — Temporal Validity
Every reservation has an explicit expiry, completion predicate, renewable lease, or documented indefinite status. Renewal requires continuing objective validity, authority, feasibility, and non-starvation.

### 09_bs_starvation.per — Survival / Fairness Guard
Protect hard survival floors, villager production, mandatory infrastructure, and bounded reservation age/share. Distinguish normal shortage, structural starvation, and dead commitment. Dead commitments must be expired/cancelled and released.

### 10_bs_transaction.per — Transaction Coordinator
Canonical transaction: REQUESTED → RESERVING → RESERVED → AUTHORIZED → ISSUED → OBSERVING → CONFIRMED. Failure states: FAILED, RELEASED, EXPIRED, INVALIDATED, THREAT-BLOCKED. ISSUED is not completion; CONFIRMED requires independent observation of the expected mutation.

### 11_bs_verification.per — Verification
Separate command accepted, object/unit/building changed, resource delta, queue change, research state, strategic state, and downstream consequence. Completion is granted only by an action-appropriate verification predicate.

### 12_bs_composition_bridge.per — Strategic Demand Adapter
Translate threat/strategy outputs into economic requirements without becoming an executor. Example: cavalry threat → response candidates → composition target → unit/infrastructure/upgrade requirements → resource demand → commitment → escrow.

Candidate responses must include more than counter-units: counter-unit, fortification, mobility, denial, relocation, retreat, counterattack, siege, technology, delay, or mixed composition.

### 13_bs_production_bridge.per — Production Authority Adapter
Connect Shadow funding to the existing Production Authority and AIByzBuild. No parallel executor. Interface: COMPOSITION AUTHORITY → RESOURCE REQUIREMENT → SHADOW FUNDING → PRODUCTION AUTHORITY → AIByzBuild → OBSERVED STATE → VERIFICATION.

### 14_bs_byzantine_tech.per — Technology Adapter
Retain Shadow's escrow-aware research mechanism while replacing donor-specific strategic policy. Research follows OBJECTIVE → TECH REQUIREMENT → COMMITMENT → ESCROW → CAN-RESEARCH-WITH-ESCROW → TRANSACTION → EXECUTOR → OBSERVE → VERIFY.

### 15_bs_debug.per — Telemetry
Expose commitment, objective, priority, requirement, reserved amount, free amount, resource-control mode, executor request, command status, observed mutation, verification state, cancellation, expiry, and failure reason.

## Authority Hierarchy

Priority classes:
1. SURVIVAL / EMERGENCY
2. CRITICAL DEFENSE
3. PRIMARY STRATEGIC OBJECTIVE
4. MILITARY COMPOSITION
5. INFRASTRUCTURE / TECHNOLOGY
6. SECONDARY / OPTIMIZATION

Normal operation targets at most three active strategic commitments: PRIMARY, SECONDARY, EMERGENCY. This is an engineering complexity ceiling, not an engine limitation.

Reservation arbitration order:
1. protect survival floor;
2. preserve mandatory economic production;
3. evaluate PRIMARY;
4. admit EMERGENCY when threshold is crossed;
5. evaluate candidate transitions;
6. compare candidates with active commitments;
7. switch only when superiority margin is sufficient;
8. allocate escrow;
9. release obsolete reservations;
10. authorize execution;
11. verify mutation;
12. reassess.

Escrow maximalism is rejected: maximize strategic control through escrow, not escrow volume.

## Interfaces

### Production
Composition authority must be active; commitment must be funded/authorized; Production Authority must permit the target; AIByzBuild must have an executor path; escrow-aware feasibility must pass; transaction escrow is released at the correct point; the executor issues the command; mutation is observed; the reservation is consumed or retained according to verification.

### Research
Same transaction discipline as production. Strategic technology cannot bypass commitment arbitration merely because resources happen to be available.

### Construction
BUILD REQUIREMENT → COMMITMENT → RESERVATION → AUTHORITY → CAN-BUILD-WITH-ESCROW → EXECUTOR → PLACEMENT / OBJECT OBSERVATION → VERIFY. Placement success is not inferred from command issuance.

## Preemption / Cancellation / Expiry

A higher-priority commitment may preempt a lower-priority commitment only through an explicit authority transition. The lower commitment is suspended/cancelled, attributable escrow is released, resource-control state is restored, the higher commitment is funded, execution proceeds, and the lower commitment is reconsidered afterward.

Global blind release is forbidden except through a formally defined catastrophic path.

## Byzantine Specialization

Byzantine policy sits above the generic economic substrate and supplies civilization-specific response valuation, composition elasticity, defensive substitutions, technology dependencies, strategic reserves, anti-cavalry/anti-archer response, siege requirements, naval commitments, and fortification policy. Shadow supplies the economic discipline that funds those decisions.

## Symbol Governance

For every mutable goal/SN record:
- canonical owner;
- every writer;
- every reader;
- semantic type;
- lifecycle;
- reset behavior;
- precedence;
- side effects;
- escrow interaction;
- executor interaction;
- verification dependency;
- evidence class/status;
- legacy/conflict classification.

Multiple writers require explicit classification as arbitration, override, additive update, reset, compatibility alias, or obsolete legacy writer.

## Failure Taxonomy

NO-CANDIDATE; REJECTED; UNFUNDED; BLOCKED; ISSUED; MUTATION-UNCONFIRMED; FAILED; EXPIRED; CANCELLED; PREEMPTED; COMPLETED.

These states must not be collapsed into a single boolean.

## Qualification

Static qualification:
- balanced syntax;
- valid primitives;
- defined symbols;
- duplicate definitions classified;
- load order known;
- writer graph complete;
- no forbidden executor duplication.

Semantic qualification:
- rule order mapped;
- state transitions mapped;
- escrow effects mapped;
- resets/retries mapped;
- precedence conflicts resolved;
- starvation paths identified.

Runtime qualification:
- command acceptance separated from mutation;
- resource deltas observed;
- production/research/build state observed;
- verification transitions demonstrated.

Strategic qualification:
- economic actions produce intended capability;
- validated threats cause appropriate commitment transitions;
- hysteresis prevents pathological oscillation;
- failed/invalid commitments recover correctly.

## Complexity Ceiling

Initial target: ≤3 active strategic commitments, 5 escrow channels, 4 resources, approximately 10–15 strategic state families, 4–6 transition classes per doctrine, one Production Authority, one AIByzBuild executor, and one economic commitment substrate.

## Implementation Order

1. Freeze namespace / ABI registry.
2. Inventory donor symbols and writers.
3. Build state model.
4. Formalize resource-control ownership.
5. Formalize escrow channels and reservation accounting.
6. Implement commitment lifecycle.
7. Implement cancellation and expiry.
8. Implement starvation protection.
9. Implement hysteresis.
10. Implement transaction coordinator.
11. Implement verification.
12. Connect composition demand.
13. Connect Production Authority.
14. Connect Byzantine technology policy.
15. Instrument telemetry.
16. Run static graph analysis.
17. Perform minimal runtime probes.
18. Promote only evidence-supported behavior.

## End State — The Escrow Byzantine King

The strategic brain determines WHAT is happening, WHY it matters, WHAT capability is required, WHEN a transition is worthwhile, and WHICH response dominates alternatives.

The Byzantine Shadow determines WHETHER that response can be economically committed, HOW much capacity may be reserved, WHICH commitment owns the reservation, WHEN it must be released, WHAT can preempt it, and WHETHER the transaction actually produced the expected mutation.

The executor determines HOW an authorized action is issued. Verification determines WHETHER reality changed as expected.

The closed loop is:

REAL WORLD → OBSERVATION → BELIEF → OBJECTIVE → CAPABILITY REQUIREMENT → ECONOMIC COMMITMENT → ESCROW → AUTHORITY → EXECUTION → OBSERVED MUTATION → VERIFICATION → UPDATED BELIEF → REASSESSMENT.

The goal is not a giant rule pile. It is a layered control organism: AEGIS supplies the brain, Byzantine policy supplies doctrine, The Byzantine Shadow supplies economic discipline, AIByzBuild supplies execution, and verification closes the causal loop.

## Next Artifact

Build `THEBYZANTINESHADOW_SYSTEM_REGISTRY_v0.1` mechanically from the Shadow donor and the target AEGIS/ByzBuilder corpus. For every relevant symbol/rule, record file, load position, definition, writers, readers, conditions, side effects, precedence, reset behavior, escrow interaction, executor interaction, verification dependency, evidence classification, confidence/status, conflict generation, and proposed owner. The registry—not intuition—must drive Blueprint v0.2 and subsequent implementation.
