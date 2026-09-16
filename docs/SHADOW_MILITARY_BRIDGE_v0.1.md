# Shadow Military Strategic Bridge v0.1

## Status

**Implemented on branch:** `production/complete-shadow-model`

**Evidence state:** DOCUMENTED + INFERRED at the interface level; runtime qualification pending.

This module formalizes the boundary between Shadow's military observations and later composition/tactical authority. It does not claim to reproduce the complete donor military subsystem.

## 1. Donor-derived architecture

The Shadow military audit identifies a mature chain:

`observation -> enemy classification -> target/threat state -> military policy -> tactical execution`

The donor contains target acquisition, threat detection, tactical groups, attack evaluation, defense, and emergency behavior. The reusable architectural improvement is to expose those observations as explicit state before execution is authorized.

The implementation therefore emits three strategic classes of state:

1. **Military posture** — buildup, defensive, attack-ready, or emergency.
2. **Capability requirement** — none, anti-cavalry, anti-ranged, anti-siege, anti-infantry, or anti-naval.
3. **Military superiority** — local military population greater than the aggregate enemy military population, otherwise inferior.

## 2. Encyclopedia / UserPatch cross-reference

The implementation uses only documented mechanisms:

- `military-population` is a documented AI fact.
- `up-get-fact` reads the local military population into a goal.
- `up-get-fact-sum every-enemy military-population 0 <goal>` aggregates enemy military population.
- `up-compare-goal` compares cached numeric goals.
- `up-get-threat-data` stores elapsed time, enemy player, source class, and target class for the last threat.
- `town-under-attack` identifies an active town-under-attack state.
- `up-attacker-class` identifies the class of the last town attacker and is used only under `town-under-attack`.
- `up-enemy-units-in-town` provides an explicit emergency trigger.
- AIRef defines the relevant military classes, including infantry, archery, cavalry, siege-weapon, and warship classes.

`unit-type-count-total` remains the production authority's mechanism for local composition verification; this military module intentionally does not duplicate production counts.

## 3. Why `attack-now` is not called here

`attack-now` is an execution primitive, not an observation primitive. The UserPatch/AI reference material documents that it creates attack groups and can impose substantial continuing execution cost. Shadow's own architecture also separates attack evaluation from tactical group execution.

Consequently, this module establishes **attack-ready state** but does not equate that state with an unconditional attack command. A later authority layer must combine strategic readiness, target validity, tactical group state, and execution feasibility before issuing a mission.

## 4. Goal registry

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

## 5. Precedence

Military posture is intentionally deterministic:

`EMERGENCY > ATTACK-READY > DEFENSIVE > BUILDUP`

Capability is reset to `NONE` each pass and replaced only when an active town attack identifies a relevant attacker class.

## 6. Ownership boundary

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

That separation preserves the donor's reusable tactical substrate while preventing the military bridge from becoming a second production executor.

## 7. Qualification boundary

Static implementation is complete for this module. Runtime qualification has **not** been claimed because the live aggregate loader and installed runtime path have not yet been independently qualified on the current machine.

Before promotion to runtime-qualified status, the loader must establish that `01_constants.per` precedes `06_military.per`, and the runtime must demonstrate that the cached goals change coherently under military population, enemy population, town-under-attack, and attacker-class conditions.
