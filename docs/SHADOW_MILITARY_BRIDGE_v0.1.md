# Shadow Military Strategic Bridge v0.1

## Status

**Implemented on branch:** `production/complete-shadow-model`

**Evidence state:** DOCUMENTED + INFERRED at the interface level; runtime qualification pending.

This module formalizes the boundary between Shadow's military observations and later composition/tactical authority. It does not claim to reproduce the complete donor military subsystem.

## 1. Donor-derived architecture

The Shadow military architecture is treated as:

`observation -> enemy classification -> threat state -> strategic policy -> tactical execution`

The reusable improvement is to make the strategic state explicit before any execution authority is invoked.

The module emits:

1. **Military posture** — buildup, defensive, attack-ready, or emergency.
2. **Capability requirement** — none, anti-cavalry, anti-ranged, anti-siege, anti-infantry, or anti-naval.
3. **Military superiority** — local `military-population` greater than aggregate enemy `military-population`, otherwise inferior.
4. **Threat telemetry** — elapsed time, enemy player, source class, and target class from the most recent threat.

## 2. Encyclopedia / UserPatch cross-reference

The implementation was corrected against the documented command signatures rather than the earlier experimental code.

### Local facts

`up-get-fact` is used in the local-player form. For `military-population`, the documented parameter is `0`:

```lisp
(up-get-fact military-population 0 SHADOW-MIL-POPULATION)
```

For `unit-type-count-total`, the requested unit type itself is the fact parameter, so the form is:

```lisp
(up-get-fact unit-type-count-total militia-line SHADOW-PROD-COUNT-INFANTRY)
```

There is **no additional literal `0`** between `militia-line` and the output goal. This distinction is important because the fact parameter is semantically occupied by the unit type.

### Enemy aggregation

`up-get-fact-sum every-enemy military-population 0 SHADOW-MIL-ENEMY-POPULATION` uses the documented wildcard aggregation form.

### Threat data

`up-get-threat-data` returns four outputs: elapsed time, enemy player, source class, and target class. The UserPatch documentation explicitly distinguishes this from `up-attacker-class`: threat data describes the last threat regardless of where it occurred, whereas `up-attacker-class` is associated with the `town-under-attack` event.

The implementation therefore consumes `up-attacker-class` only while `town-under-attack` is true, preventing the retained last attacker class from being misinterpreted as a new current attack.

### Direct town facts

`up-enemy-units-in-town` and `up-defender-count` are documented facts. They are consumed directly rather than being incorrectly routed through `up-get-fact` with invented parameters.

### Military classes

AIRef/UserPatch defines the relevant class constants used here, including:

- `archery-class` = 900
- `infantry-class` = 906
- `cavalry-class` = 912
- `siege-weapon-class` = 913
- `warship-class` = 922

## 3. Important semantic limitation

`military-population` is an engine-level military-population fact, not a pure combat-power metric. UserPatch history explicitly notes that monks and transport ships are included in military population. Therefore:

**MILITARY-SUPERIOR is not equivalent to COMBAT-POWER-SUPERIOR.**

Likewise, `SHADOW-MIL-ATTACK-READY-MIN-POP` is a policy threshold over the engine's military-population fact, not a claim that ten combat units constitute an adequate Byzantine attack force in every game state.

The later military-composition layer should replace this coarse readiness test with composition-aware capability once the production-demand interface is available.

## 4. Why `attack-now` is not called here

`attack-now` is an execution primitive, not an observation primitive. UserPatch documents that it creates attack groups and that attack-group processing carries continuing execution cost. Shadow's donor architecture also separates military evaluation from tactical execution.

Consequently, this module establishes **attack-ready state** but does not equate that state with an unconditional attack command. A later authority layer must combine strategic readiness, target validity, composition, tactical group state, and execution feasibility before issuing a mission.

## 5. Goal registry

| Goal | Purpose |
|---|---|
| 540 | Local military population |
| 541 | Aggregate enemy military population |
| 542 | Military posture |
| 543 | Capability requirement |
| 544 | Last threat elapsed time |
| 545 | Last threat player |
| 546 | Last threat source class |
| 547 | Last threat target class |
| 548 | Military superiority state |
| 549 | Initialization sentinel |

These IDs are outside the production target/state registry and outside the historical AEGIS 450–496 range.

## 6. Precedence

Military posture is deterministic:

`EMERGENCY > ATTACK-READY > DEFENSIVE > BUILDUP`

Capability is reset to `NONE` each pass and replaced only when an active town attack identifies a relevant attacker class.

## 7. Ownership boundary

This module **owns** military observation normalization and strategic military state.

It **does not own**:

- production targets;
- production site construction;
- escrow;
- training;
- attack-group creation;
- direct targeting;
- retreat execution;
- final tactical mission selection.

That separation prevents military cognition from becoming a second production executor.

## 8. Qualification boundary

Static implementation is complete for this module. Runtime qualification has **not** been claimed because the live installed runtime path has not yet been independently qualified on the current machine.

The aggregate loader now places `01_constants.per` before `06_military.per`; the live machine still needs runtime confirmation. Runtime promotion must demonstrate coherent changes in military population, enemy population, town threat, attacker classification, and strategic posture under actual engine conditions.
