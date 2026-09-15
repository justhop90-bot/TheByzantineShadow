# The Byzantine Shadow — System 01: Initialization & Configuration Deep Dive v0.1

## 0. Purpose and forensic standard

This document is the first system-level deep dive in the Shadow reconstruction sequence. It analyzes the initialization/configuration layer of the supplied `Shadow DC7(1).per` donor at source level.

Source: `Shadow DC7(1).per`  
Source SHA-256: `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`  
Physical source size: 615,773 bytes  
Physical line count: 22,603

Evidence status: **DIRECT static source evidence** unless explicitly marked otherwise. No runtime claim is made here. A constant being defined does not establish that it is active, reachable, or strategically effective at runtime.

---

# 1. Executive finding

The Shadow initialization/configuration layer is more consequential than a conventional "constants section" suggests.

It establishes four distinct classes of control:

1. **Environment contract** — assumptions about game version, map, civ, team structure, population, victory conditions, and map size.
2. **Engine/ABI vocabulary** — symbolic aliases for goals, strategic numbers, unit/building classes, research states, resource selectors, and action states.
3. **Policy coefficients** — thresholds, distances, timers, escrow percentages, retreat distances, and economic limits.
4. **Compile-time feature selection** — `#load-if-defined` branches that select Tiny/Small/Medium/Normal/Large/Giant map behavior, pocket/ally-position behavior, and DE-versus-UP behavior.

The most important architectural discovery is that these categories are mixed in the same namespace. AEGIS should not simply transplant the block. It should **decompose it into typed configuration domains while preserving the validated numerical knowledge**.

The second major finding is a portability hazard: the donor explicitly documents a **Vikings-only, Tiny Arabia, AoC UP 1.6+** operating contract, while also containing conditional DE support. That makes the donor a valuable strategic/economic source but not a drop-in Byzantine/DE configuration baseline.

**Disposition: PRESERVE knowledge → CLASSIFY → VALIDATE → PARAMETERIZE → REUSE. Do not wholesale replace.**

---

# 2. The declared operating contract

At lines 25–40 the donor states:

- Vikings only;
- Hard difficulty;
- AoC UP 1.6+;
- 1v1;
- Tiny map;
- Arabia;
- Standard/Conquest victory;
- Random Map;
- Standard map style;
- population 200;
- Standard starting age;
- Standard starting resources;
- locked teams;
- locked diplomacy.

This is not commentary of negligible importance. It is the author's declared qualification envelope.

## Architectural implication

The source must be treated as a **donor conditioned on an environment**, not as a universal AI policy.

For AEGIS/Byzantine transplantation, every configuration item should receive one of these labels:

`ENGINE-FACT`
`DONOR-ASSUMPTION`
`MAP-PARAMETER`
`CIV-PARAMETER`
`POLICY-COEFFICIENT`
`RUNTIME-STATE`
`DEBUG/TELEMETRY`
`UNKNOWN`

The donor's declared Vikings/Tiny/UP assumptions should never silently become Byzantine/DE architecture.

---

# 3. The QLOAD / source organization layer

The table of contents identifies QLOAD, QTIMERS, QCONSTANTS, QID, QGENERAL, QPOSITION, QDIRECT TARGETING, QSCOUT, QECO, QPRO, QEAGOL, QSHARED GOALS, and QRULES sections.

This establishes a source-level modular organization even though the physical donor is a single `.per` file.

The important point is that **logical modules exist independently of file boundaries**.

This matters for AEGIS because future decomposition should follow behavioral systems rather than arbitrary line ranges.

The first constants are followed by timer definitions, then the large symbolic registry. That ordering establishes a human-readable declaration contract but does not by itself prove engine load-order semantics.

**Evidence classification: DIRECT for physical ordering; UNCERTAIN for any claim that physical order alone determines all engine semantics.**

---

# 4. Identity and diagnostic configuration

Early constants include:

- `gl-identity = 420`;
- `Shadow = 2048`;
- `Doomsday = 42`;
- `BruteForce3 = 1001`;
- `Promi = 420`;
- several additional named identities.

These are not gameplay strategy variables. They are principally identity/diagnostic markers.

There is also `gl-town-under-attack`, `home-x`, `home-y`, `gl-position`, `gl-attacking`, and related state definitions.

## Disposition

Preserve identity constants only where they support diagnostics or compatibility. They should not enter the strategic-control model unless downstream rules actually use them as policy inputs.

---

# 5. State-slot declarations versus policy declarations

The donor defines goals such as:

- current age;
- town-under-attack;
- position;
- attacking;
- town-safe;
- target HP;
- last target;
- ranged style;
- raid state;
- enemy attack size;
- cavalry/archery-in-town;
- attack efficiency;
- defense state;
- build progress;
- dark-build state;
- target type;
- total military in range;
- army damage potential.

It simultaneously defines policy constants such as:

- retreat distances;
- costs of ignoring threats;
- scouting distances;
- escrow percentages;
- market thresholds;
- villager timing thresholds;
- farming delays.

This is a fundamental namespace issue.

A goal representing `town-safe` is conceptually different from a constant representing `CostOfIgnoringTCs = 50` even if both are expressed through `defconst`.

## AEGIS requirement

Create a typed registry with at least:

`SYMBOL`
`KIND`
`DOMAIN`
`VALUE`
`OWNER`
`WRITERS`
`READERS`
`LIFETIME`
`RESET RULE`
`PRECEDENCE`
`ENGINE DEPENDENCY`
`EVIDENCE STATUS`

This is a configuration problem only because the configuration layer currently carries multiple semantic categories.

---

# 6. Engine vocabulary registry

The donor aliases engine concepts such as:

- `game-time`;
- `population-cap`;
- `food-amount`;
- `wood-amount`;
- `gold-amount`;
- `escrow-amount`;
- `current-age`;
- `player-number`;
- `player-in-game`;
- `unit-count`;
- `unit-type-count`;
- `building-count`;
- `military-population`;
- `civilian-population`;
- `player-distance`;
- `enemy-buildings-in-town`;
- `enemy-units-in-town`;
- `building-type-in-town`;
- `unit-type-in-town`.

These are effectively an **ABI vocabulary layer**.

They should be treated differently from strategic constants because they are interface symbols into the AI engine rather than Shadow's strategic inventions.

**Disposition: KEEP / PROTECT.**

Any migration must verify the target AoE2DE ABI before changing these aliases.

---

# 7. Research and action-state enumerations

The donor declares research states:

`research-unavailable = 0`
`research-available = 1`
`research-pending = 2`
`research-complete = 3`

It also declares action modes:

`aggressive = 0`
`defensive = 1`
`stand-ground = 2`
`no-attack = 3`

These are compact enumerations.

They should not be interpreted as strategic intelligence. They are state/action vocabulary used by downstream systems.

**Disposition: KEEP; classify as ENGINE/INTERFACE ENUMERATION where verified.**

---

# 8. Unit/building class registry

The donor aliases classes for scouts, villagers, buildings, towers, walls, gates, infantry, archery, cavalry, cavalry archers, cavalry cannon, monasteries, siege, scorpions, trebuchets, petards, warships, dangerous animals, transport ships, trees, stone mines, and gold mines.

This registry is one of the reasons the donor is strategically reusable: higher-level rules can reason in class space rather than enumerating every unit.

For AEGIS, this supports the capability abstraction:

`OBSERVATION → CLASS → THREAT/CAPABILITY`

rather than:

`OBSERVATION → hard-coded unit identity`.

**Disposition: KEEP + EXTEND only when engine semantics are verified.**

---

# 9. Tactical state enumerations

The donor defines states such as:

`ATTACKING`
`VATTACKING`
`MOVING`
`TATTACKING`

and retreat source categories:

`FROM-UNITS`
`FROM-FORTIFICATIONS`
`FROM-SIEGE`.

These are important because they provide a finite-state vocabulary for tactical execution.

They belong below strategic authority.

AEGIS should request a mission/capability; tactical machinery should continue to operate on these states.

**Disposition: PRESERVE.**

---

# 10. Compile-time map specialization

The donor contains a map-size branch for scout health:

- Tiny: minimum scout HP 12/15;
- otherwise: minimum scout HP 20/23.

It also defines `max-circle-scout-distance` conditionally:

- Giant: 110;
- Large: 94;
- Normal: 80;
- Medium: 72;
- Small: 60;
- Tiny: 50.

This is a genuine configuration matrix.

The important observation is that **map size changes information-acquisition policy**.

That means configuration is not merely cosmetic. It alters the geometry and timing of the scouting subsystem.

**Disposition: PRESERVE; convert to explicit environment parameter table.**

---

# 11. Compile-time position specialization

The donor selects `gv-scouting-type` according to compile-time features:

- pocket position → mirror scouting;
- otherwise ally-in-game → flank scouting;
- otherwise → opposite scouting.

This is a direct example of compile-time configuration becoming a strategic-information policy.

The design is efficient but opaque because the resulting strategic assumption is hidden inside preprocessing.

AEGIS should make the resulting policy explicit:

`POSITION CLASS → DEFAULT INFORMATION ACQUISITION POLICY`.

The scout executor can remain unchanged.

**Disposition: PRESERVE behavior + EXPOSE policy derivation.**

---

# 12. DE-versus-UP compatibility configuration

The donor contains `#load-if-defined DE-AVAILABLE` branches in multiple locations.

One firing threshold pair is:

DE: 100 / 2500  
UP: 300 / 2450

Another is:

DE: 700 / 1800  
UP: 650 / 1800

A later DE branch changes the ranged-group fire command sequence relative to the UP branch.

This demonstrates that Shadow is not simply an old UP script with a DE label. The author deliberately maintains engine-specific behavior.

## Critical implication

Engine-specific constants and command sequences must be classified as:

`ENGINE-SPECIFIC / DONOR-VALIDATED / TARGET-ENGINE-REQUIRES-REQUALIFICATION`.

The DE branches are valuable historical evidence, but they do **not** constitute proof for the current AoE2DE build targeted by AEGIS.

**Disposition: PRESERVE as compatibility evidence; requalify against target DE build.**

---

# 13. Economic configuration

The donor defines:

- LOW-ESCROW = 25;
- MID-ESCROW = 35;
- MID-HIGH-ESCROW = 40;
- HIGH-ESCROW = 60;
- `SkipMillTime = 240`;
- late-game time 2500;
- stone delay 300;
- wood/gold/stone distance limits;
- age-specific food/wood/gold trading thresholds;
- villager-count thresholds;
- farm and hunting delays.

These are policy coefficients, not engine constants.

They should therefore be separated from the engine vocabulary registry and made tunable through an explicit policy table.

**Disposition: KEEP KNOWLEDGE + PARAMETERIZE.**

Do not assume the numerical values transfer unchanged to Byzantine AEGIS.

---

# 14. Economic threshold architecture

The age-specific market thresholds demonstrate a structured pattern:

`EXCESS → TRADE`
`NEED → ACQUIRE`
`TRADING THRESHOLD → ACTION BOUNDARY`

For example, Castle Age has distinct wood, gold, food and stone thresholds, while Imperial Age uses another set.

This is not merely a list of numbers. It is a policy function:

`age × resource state → liquidity response`.

That function should be preserved conceptually.

**Disposition: PRESERVE FUNCTION; re-evaluate coefficients.**

---

# 15. Strategic timing configuration

The donor establishes timing constants such as:

- `KrushHomeTime = 630`;
- `home-exploration-time = 400`;
- `LATE-GAME-TIME = 2500`;
- `LATE-TIME = 800`;
- `FARMING-DELAY = 100`;
- `WOOD-DELAY-TIME = 150`;
- `FIRST-MILL-DELAY = 200`;
- `deer-luring-stop-time = 600`.

These parameters create temporal priors for strategy and economy.

AEGIS should not blindly remove them in favor of a more abstract planner. Instead, it should identify which are:

- hard environmental constraints;
- empirical donor timings;
- tactical cooldowns;
- strategic activation thresholds;
- economic recovery delays.

Only the latter two categories are strategic-policy candidates.

---

# 16. Threat-cost configuration

The donor defines a striking sequence of qualitative costs:

`CostOfFightingEarly = 5`
`CostOfDivingBehind = 10`
`CostOfSidlingCloser = 20`
`EnoughToKeepFighting = 20`
`CostOfNotLeavingFights = 22`
`CostOfIgnoringTowers = 25`
`CostOfAllowingKnightsToRoam = 30`
`CostOfAllowingKnightsToGoFree = 40`
`CostOfIgnoringMelee = 40`
`CostOfPausingForRams = 41`
`CostOfIgnoringTCs = 50`
`CostOfIgnoringEverything = 55`

This is strategically important.

These values are evidence that Shadow contains a crude utility/risk scale rather than only binary predicates.

The scale should be extracted into a capability/threat valuation model rather than discarded.

**Disposition: PRESERVE semantic model + IMPROVE representation.**

The exact numeric values remain donor policy coefficients until validated.

---

# 17. Timers as configuration-controlled state machines

The timer registry includes game evaluation, villager training, enemy scouting, target switching, raid waypoint reevaluation, raid retreat, defense, market/economic checks, building delays, direction changes, firing, command delay, failsafe, enemy-age cancellation, housing checks, and multiple long-duration timing constants.

Timers are therefore not just delays. They define **temporal guards** in the control architecture.

The canonical AEGIS interpretation should be:

`STATE + TIMER → TEMPORAL GUARD → REASSESSMENT`.

This aligns directly with the AEGIS canonical cycle.

**Disposition: PRESERVE + TYPE.**

Each timer should eventually be classified as cooldown, debounce, reevaluation interval, timeout, expiry, or temporal activation gate.

---

# 18. The initialization layer already contains hidden strategic doctrine

Several configuration constants directly affect later strategy:

- scouting mode;
- Krush home time;
- map-specific scouting distance;
- threat costs;
- attack percentages;
- strategic timing;
- villager thresholds;
- escrow percentages.

Therefore initialization is not strategically neutral.

It contains **latent priors** that downstream rules operationalize.

This is exactly why AEGIS must preserve the donor's empirical knowledge while making its provenance explicit.

---

# 19. Configuration-to-runtime causal paths

The most important paths are:

### Path A — map → scouting
`MAP-SIZE → max-circle-scout-distance → scouting geometry → information acquisition`

### Path B — position → scouting
`POSITION FEATURE → gv-scouting-type → scout policy → observed information`

### Path C — engine → tactical timing
`DE-AVAILABLE → firing threshold → fire/move transition`

### Path D — economic policy → commitment
`ESCROW COEFFICIENT → resource reservation → affordability → transaction feasibility`

### Path E — strategic timing → doctrine
`TIME / AGE → Krush/Flush thresholds → strategy state`

### Path F — threat coefficient → tactical evaluation
`COST CONSTANT → attack/retreat evaluation → tactical state`

These are the actual reasons the configuration system matters.

---

# 20. Configuration hazards identified

## Hazard 1 — donor environment leakage

The explicit Vikings/Tiny/UP operating contract can contaminate a Byzantine DE port if not separated.

**Action:** quarantine donor assumptions.

## Hazard 2 — policy/engine conflation

Engine aliases and policy constants coexist in the same registry.

**Action:** typed symbol registry.

## Hazard 3 — compile-time opacity

`#load-if-defined` hides which strategic policy is actually compiled.

**Action:** emit a configuration manifest for each target environment.

## Hazard 4 — numeric false certainty

A donor threshold is not automatically an optimal Byzantine threshold.

**Action:** preserve as HISTORICAL/DONOR-POLICY until validated.

## Hazard 5 — duplicate namespace

The donor already contains duplicated names such as `home-x`, `home-y`, `gl-position`, and tactical state symbols in different contexts.

**Action:** resolve through complete writer/reader/reachability analysis before consolidation.

## Hazard 6 — engine-version drift

DE/UP branches prove historical adaptation but do not prove compatibility with the current AEGIS target build.

**Action:** separate engine evidence from donor behavior and requalify target primitives.

---

# 21. What should be transplanted

The following knowledge is high-value:

1. Map-conditioned scouting geometry.
2. Position-conditioned scouting defaults.
3. Engine-specific compatibility branching as a design pattern.
4. Threat-cost scalarization.
5. Age-dependent economic thresholds.
6. Temporal guard taxonomy.
7. Escrow percentage bands.
8. Spatial economic distance limits.
9. Tactical retreat distances.
10. Explicit state enumerations.
11. Engine vocabulary aliases.
12. The separation between environment assumptions and behavioral rules, once formalized.

---

# 22. What should NOT be transplanted blindly

Do not blindly transplant:

1. Vikings-specific assumptions.
2. Tiny Arabia assumptions.
3. AoC UP-specific numerical values.
4. Donor-specific timing values.
5. Donor-specific economic thresholds.
6. Donor identity/debug constants.
7. Any constant whose active writer/reader path has not been qualified.
8. Any DE branch as proof of current AoE2DE runtime compatibility.

---

# 23. Target AEGIS configuration architecture

The donor's configuration should ultimately become four explicit layers:

```text
ENGINE ABI
  ↓
ENVIRONMENT PROFILE
  ↓
DONOR POLICY PRIORS
  ↓
AEGIS POLICY PARAMETERS
```

### ENGINE ABI
Verified engine constants, predicates, action semantics and compatibility features.

### ENVIRONMENT PROFILE
Civ, map, map size, team structure, game mode, population and starting conditions.

### DONOR POLICY PRIORS
Extracted Shadow knowledge retained as historical/probabilistic priors.

### AEGIS POLICY PARAMETERS
Current Byzantine strategic coefficients and thresholds, with explicit ownership and qualification status.

This is materially better than replacing the entire constants layer.

---

# 24. Recommended registry schema

Every configuration symbol should ultimately have:

| Field | Meaning |
|---|---|
| Symbol | exact `.per` identifier |
| Value | literal/current value |
| Kind | ABI / environment / policy / state / debug |
| Domain | economy / scouting / military / strategy / etc. |
| Source | Shadow donor / engine / AEGIS |
| Condition | compile-time condition |
| Readers | consuming rules/modules |
| Writers | runtime writers if mutable |
| Lifetime | static / initialization / transient / persistent |
| Reset | reset mechanism |
| Precedence | duplicate/conditional precedence |
| Evidence | DIRECT / COMPOSED / INFERRED / etc. |
| Status | CONFIRMED / PROBABLE / UNCERTAIN / etc. |
| Target DE qualification | verified/unverified |

---

# 25. Qualification plan

Before modifying any configuration constant, run the following qualification sequence:

### Q1 — Definition
Does the symbol exist and have a unique intended definition?

### Q2 — Reference
Which rules read it?

### Q3 — Reachability
Can those readers execute under the target environment?

### Q4 — Effect
What state or command does the symbol influence?

### Q5 — Competing definitions
Are there alternate definitions or preprocessor branches?

### Q6 — Temporal behavior
Does the value remain static or participate in a state transition?

### Q7 — Engine dependency
Does the value depend on UP/DE or another engine feature?

### Q8 — Strategic leverage
Does changing it alter strategic authority, execution, or merely tuning?

### Q9 — Byzantine transferability
Is the mechanism civilization-independent, civilization-specific, or donor-specific?

### Q10 — Verification
What observable outcome would prove the modified value is actually being used?

---

# 26. First-system verdict

**Initialization/configuration is NOT a system to replace.**

It is a **knowledge extraction and typing problem**.

The donor's strongest configuration contributions are:

- explicit environmental assumptions;
- map/position-conditioned information policy;
- temporal guards;
- threat-cost scalarization;
- economic policy coefficients;
- escrow policy bands;
- engine compatibility branches;
- a broad reusable engine vocabulary.

Its weaknesses are:

- semantic categories mixed together;
- donor assumptions embedded alongside reusable mechanisms;
- compile-time choices obscuring runtime policy;
- numerical priors lacking explicit provenance;
- potential duplicate/conflicting definitions;
- incomplete separation of engine ABI from strategic policy.

Therefore the correct AEGIS transformation is:

```text
SHADOW CONFIGURATION
        ↓
FORENSIC CLASSIFICATION
        ↓
TYPED REGISTRY
        ↓
ENVIRONMENT MANIFEST
        ↓
DONOR POLICY PRIORS
        ↓
AEGIS BYZANTINE PARAMETERS
        ↓
DOWNSTREAM SYSTEMS
```

The strategic consequence is substantial: **configuration becomes an explicit source of priors rather than an invisible source of assumptions.**

---

# 27. Next forensic step

System 02 should be the **State / Namespace system**.

That analysis must go substantially deeper than listing goals. It should reconstruct the state machine represented by goals and strategic numbers and determine:

`SYMBOL → SEMANTIC TYPE → WRITERS → READERS → INITIAL VALUE → RESET → TEMPORAL LIFETIME → PRECEDENCE → JUMP EFFECT → CROSS-DOMAIN EFFECT → EXECUTOR EFFECT`.

The duplicated constants and state-slot collisions should be resolved only after this graph exists.

The critical question is not "which constants are duplicated?" It is:

> **Which symbolic state variables constitute Shadow's actual control plane, and which are merely aliases or historical debris?**

That answer determines the architecture of every subsequent system.
