# ShadowSource Military Control-Region Atlas v0.1

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per`  
**Canonical source SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Canonical source:** 615,773 UTF-8 bytes / 22,604 lines / 1,956 `defrule` blocks  
**Historical donor:** Shadow DC7, commit `1d9f45b3b9ac03adc24103df2b21c84b92a45fb6`  

## 0. Scope and forensic rule

This document maps the **Military control region as implemented by the canonical Shadow rule machine**, not as a proposed software module. Shadow's military behavior is distributed through several source-order neighborhoods and deliberately crosses scouting, economy, construction, research, production, and defense. A single contiguous `.per` module would therefore misrepresent the donor.

The map below records the military region as a **distributed control closure**. Exact source windows are given where directly recovered. Where a military behavior resumes after an intervening non-military source block, it is recorded as a separate slice with an explicit cross-region edge.

Evidence rules:

1. Source order is executable control topology; normal successor is the next rule.
2. `up-jump-rule Δ` is a control edge, not a semantic priority label.
3. Command issuance is never treated as completion unless a subsequent engine/world predicate establishes the observed result.
4. Search-state counts, positions, object IDs, target data, group state, timers, and enemy composition are observations/state—not implicit completion.
5. A `release`, `stop`, `move`, or `attack` command is not itself proof that the intended world state resulted.
6. Constants and state declarations establish the namespace; rule writers establish behavioral ownership.

---

# 1. Military control-region topology

```text
                         SHADOW MILITARY MACHINE
                                  |
             +--------------------+--------------------+
             |                    |                    |
       TACTICAL MEMORY       WORLD OBSERVATION     STRATEGY INPUT
             |                    |                    |
             +--------------------+--------------------+
                                  |
                          RANGED EVALUATION
                                  |
             +--------------------+--------------------+
             |                    |                    |
       GROUP CONTROL         TARGET CONTROL       RANGE / POWER
             |                    |                    |
             +--------------------+--------------------+
                                  |
                           MARCH / RAID STATE
                                  |
                    +-------------+-------------+
                    |                           |
               ATTACK STATE                DEFENSE STATE
                    |                           |
                    +-------------+-------------+
                                  |
                         MILITARY EXECUTION
                                  |
       +-------------+------------+-------------+-------------+
       |             |                          |             |
     ATTACK         MOVE                    STOP/GARRISON   PATROL
       |             |                          |             |
       +-------------+------------+-------------+-------------+
                                  |
                         WORLD OBSERVATION
                                  |
                    +-------------+-------------+
                    |                           |
               CONTINUE / REFORM          RETREAT / RECOVER
                    |                           |
                    +-------------+-------------+
                                  |
                              RE-ENTRY
```

The machine is not a simple `observe -> classify -> attack` pipeline. It repeatedly constructs observations, writes persistent tactical state, chooses a target or march state, issues an engine action, and then uses later observations/timers/state conditions to continue, stop, retreat, retarget, or change march mode.

---

# 2. Region-slice index

| Slice | Canonical source window | Primary behavior | Boundary |
|---|---:|---|---|
| M01 | L1938-L2064 | military initialization, ranged-group baseline, tactical range state | CONFIRMED |
| M02 | L2058-L~3300 | ranged evaluation, target statistics, combat geometry, target acquisition | CONFIRMED CORE / interleaved search subsections |
| M03 | L3300-L~4300 | target-location acquisition, march geometry, attack/defense state, march progression | CONFIRMED CORE |
| M04 | L4300-L4364 | military/production boundary: skirmisher cancellation | CONFIRMED |
| M05 | L4850-L~5200 | TC garrisoning, enemy-attack estimation, villager retreat | CONFIRMED CORE |
| M06 | L5000-L~5450 | skirmisher/villager defense, enemy-attack center-of-gravity, anti-scout | CONFIRMED CORE |
| M07 | L5450-L~5680 | hurt-scout micro, anti-luring, ram response | CONFIRMED |
| M08 | L5680-L~5700 | terminal ram action before QSHEEP begins | CONFIRMED |

**Important boundary fact:** the military region is **distributed**, not contiguous. Construction/economic source code is interleaved between military slices. The intervening code is not silently classified as military merely because military state is later consumed by it.

---

# 3. M01 — Military initialization and tactical memory

## Source

**L1938-L2064**, rules 14–27 in the recovered source-order matrix.

The source explicitly labels the surrounding area with military/group sections including `QSKIRMS`, `QDEFENSE`, `QMANGOS`, `QSPEARS`, `QSCOUT`, `QKNIGHT GROUP`, `QEVAL`, `QRAIDING`, `QRANGED`, `QINITIALIZING GROUP`, `QREGROUPING`, `QMOVING`, `QMARCH`, and `QCOMBAT MODE`. The initialization rule sets the baseline tactical state. fileciteturn375file0L2-L2

## Entry conditions

The region is entered by normal source-order evaluation after global setup/diagnostic rules. The principal initializer is unconditional and self-disables after writing the tactical baseline.

## State reads

- `gl-current-group`;
- group existence/size;
- `gl-town-safe`;
- ranged-group and enemy-group coordinates;
- research completion for Fletching, Bodkin Arrow, Elite Skirmisher, Crossbow;
- positional geometry.

## State writes

The principal initializer writes:

- `gl-defend-town = NO`;
- `gl-current-group = RangedGroup`;
- `sn-number-tasked-units = 40`;
- `gl-max-ranged-group-size = 40`;
- `gl-range-advantage = 0`;
- `gl-ranged-group-state = FIRING`;
- `gl-can-fire = NO`;
- `gl-raid-can-fire = NO`;
- `gl-enemy-tower-range = 9`;
- `gl-my-tower-range = 9`;
- `gl-ranged-group-range = 4`;
- `gl-raid-group-range = 4`;
- `gl-march-type = DefendingLC`;
- `gl-close-ranged-group-range = 3`.

Tracking range is then initialized and adjusted by town safety, distance, and completed technologies. Fletching and Bodkin explicitly modify tactical ranges; the relevant rules self-disable after their one-time range expansion. fileciteturn375file0L2-L2

## Engine observations

- `up-group-size`;
- `up-point-distance`;
- `research-completed`;
- target/group coordinates;
- search-state operations in later military subsections.

## Engine commands

No combat command is issued by the baseline initializer itself. It establishes the persistent control state consumed by later command regions.

## Completion observation

Initialization completion is represented by `disable-self`; this is a control latch, not a world-state observation. Technology-derived tactical completion is observed directly through `research-completed` predicates.

## Recovery/re-entry

No independent recovery action here. Later military slices consume and mutate the initialized state.

## Cross-region edges

- **Research → Military:** completed Fletching/Bodkin/Elite Skirmisher modify range/tactical state.
- **Military → Research:** enemy composition/threat conditions later trigger research interruptions.
- **Military → Production:** tactical capability/deficit conditions inform production requirements.
- **Military → Defense:** `gl-defend-town` and march state feed emergency behavior.

---

# 4. M02 — Ranged evaluation and combat-state scoring

## Source

Core recovered interval begins at **L2058** and continues through the large ranged-evaluation neighborhood into the target/group subsections before march control. The source explicitly shows the first control bypass as `up-jump-rule 44`. fileciteturn375file0L2-L2

## Entry conditions

The key entry test is:

```text
RangedGroup < 1
OR
Distance(RangedGroup, EnemyGroup) > 15
```

which sets `gl-ranged-eval = WinningFight` and performs `up-jump-rule 44`. This is a real control-flow bypass, not a priority marker. fileciteturn375file0L2-L2

## State reads

### Tactical state

- `gl-ranged-group-size`;
- `gl-enemy-group-size`;
- `gl-ranged-group-range`;
- `gl-close-ranged-group-range`;
- `gl-tracking-range`;
- `gl-target-distance`;
- `gl-ranged-group-state`;
- `gl-can-fire`;
- `gl-can-move`;
- `gl-range-advantage`;
- `gl-armor-advantage`;
- `gl-army-damage-potential`;
- `SUPERIORITY`;
- `UP-FIRST`;
- `RETREATING`.

### Enemy observations

- enemy ranged units;
- skirmishers;
- infantry;
- cavalry/scout cavalry;
- monks;
- knights;
- mangonels;
- enemy Town Centers;
- enemy castles;
- enemy towers;
- wolves/neutral hazards;
- builders;
- villagers.

## State writes

The evaluation region computes or mutates:

- `gl-ranged-eval`;
- `gl-range-advantage`;
- `gl-armor-advantage`;
- `gl-units-in-close-range`;
- `gl-total-units-in-range`;
- `gl-total-military-in-range`;
- `gl-melee-in-range`;
- `gl-cavalry-attacking`;
- `gl-mangos-nearby`;
- `gl-enemy-group-size`;
- target ID/type/class/HP/distance/coordinates;
- `gl-highest-next-attack`;
- `gl-lowest-next-attack`.

The source directly calculates range, armor, army-size, damage-potential, tower, TC, knight, monk, villager, and other tactical terms. For example, it adds enemy/own group sizes and damage potential into `gl-ranged-eval`, and separately computes range advantage through searches. fileciteturn376file0L2-L2

## Engine commands / observations

The principal operations are observation/search primitives:

- `up-full-reset-search`;
- `up-set-target-point`;
- `up-filter-distance`;
- `up-find-remote`;
- `up-find-local`;
- `up-find-status-remote`;
- `up-set-target-object`;
- `up-get-object-data`;
- `up-get-point`;
- `up-get-point-distance`;
- `up-get-search-state`;
- `up-remove-objects`;
- `up-clean-search`;
- `up-filter-include`;
- `up-reset-filters`.

The target-statistics path explicitly reads object class, type, ID, HP, position, and distance into persistent Shadow state. fileciteturn378file0L2-L2

## Combat execution commands

The evaluation region eventually feeds engine actions including:

- `up-target-objects ... action-default`;
- `up-target-point ... action-move`;
- `up-target-point ... action-stop`;
- `up-target-point ... action-patrol`;
- `up-target-point ... action-garrison`.

The source therefore contains a complete observation-to-command path, but command issuance remains distinct from world-state completion.

## Firing/movement arbitration

The source maintains a local two-state control:

```text
CAN-FIRE
CAN-MOVE
```

The state changes according to target distance, next-attack thresholds, and a failsafe timer. If the target is close enough and the next-attack threshold is favorable, `gl-can-fire` becomes `YES` and `gl-can-move` becomes `NO`. If the target is outside range, movement is enabled. The failsafe timer can force either transition. fileciteturn377file0L2-L2

This is an explicit tactical arbitration machine, not merely a target selector.

## Jump closure

Confirmed jump edges in this region include:

| Edge | Meaning |
|---|---|
| `+44` from the QADVANTAGE entry | bypasses a large evaluation block when the ranged group is absent/far from the enemy group |
| `+12` from the QGROUP/QNA entry | bypasses ranged-group analysis when no ranged group exists |
| `+56` from the QTARGET entry | bypasses target acquisition when no ranged group exists |
| `-5` in repeated target-category searches | loops the focus-player search until all relevant players are scanned |
| `-4` in MILITARY CLOSE search | repeats player-scoped military search |
| `-3` in VILLS CLOSE search | repeats villager search |
| `-7` in MILITARY ALL / QUICKIES | repeats the complete player-scoped target search |
| `-2` in repeated enemy-player search loops | increments focus-player and re-enters the search |

These are control-flow edges. They are not equivalent to priority declarations. The canonical source-order matrix independently establishes the jump model `target = current + 1 + Δ`. fileciteturn349file0L2-L2

## Completion observation

There is no single `combat-complete` predicate. Tactical continuation/closure is established through observations such as:

- target count/search state;
- target ID/type/class/HP/distance;
- group size;
- enemy group size;
- `gl-ranged-group-state`;
- next-attack state;
- distance/range predicates;
- timer expiration;
- retreat/stop conditions.

## Recovery behavior

Recovery is embedded in the same control region:

- failsafe timer can force movement/fire state;
- target searches can be repeated;
- target lists are rebuilt when empty/stale;
- focus-player loops advance to the next player;
- `MINI-RETREAT` changes target filtering;
- target state can be reconstructed from search results.

This is **stateful recovery/re-entry**, not a separate recovery subsystem.

---

# 5. M03 — Target acquisition, march geometry, attack and defense state

## Source

Primary recovered window **L3300-L4300**. This includes nearest-TC/castle/tower resolution, enemy-group sizing, march-point maintenance, attack geometry, march-mode progression, and defense return paths. fileciteturn379file0L2-L2 fileciteturn380file0L2-L2

## Entry

The target/march machine is entered when the ranged group exists or when the broader military state requires a target, march point, or defense path.

## State reads

- `gl-ranged-group-size`;
- `gl-enemy-group-size`;
- `gl-ranged-group-state`;
- `gl-defend-town`;
- `gl-attacking`;
- `gl-march-type`;
- `gl-enemy-strategy`;
- `enemy-x`;
- `nearest-tc-x/y`;
- `nearest-castle-x/y`;
- `nearest-tower-x/y`;
- `march1-x/y` through `march4-x/y`;
- `march-x/y`;
- `saved-march-x/y`;
- `home-x/y`;
- game-time / turn timers;
- enemy building counts.

## State writes

- nearest target coordinates;
- enemy position;
- march points;
- saved march point;
- `gl-march-type`;
- `gl-defend-town`;
- `gl-attacking`;
- `gl-current-group`;
- `SPLIT` temporary arbitration state.

## Engine commands / observations

Target-location resolution uses:

- `up-find-status-remote`;
- `up-find-remote`;
- `up-clean-search`;
- `up-set-target-object`;
- `up-get-point`;
- `up-point-contains`;
- `up-cross-tiles`;
- `up-lerp-tiles`;
- `up-bound-point`.

The march geometry rules explicitly construct four approach points around the enemy Town Center and derive a march point from them. fileciteturn380file0L2-L2

## March-state machine

The source contains a persistent march-mode progression:

```text
MarchingOne
    ↓
MarchingTwo
    ↓
MarchingThree
    ↓
MarchingFour
```

with exceptional transitions back to One or Four based on enemy KRUSH/POSSIBLE-KRUSH, age, elapsed time, player-valid conditions, and proximity to the march point. The transitions are explicitly implemented with `SPLIT` plus jumps. fileciteturn380file0L2-L2 fileciteturn381file0L2-L2

## Defense re-entry

When `gl-defend-town = YES`, the ranged group is sent home and the original march point is preserved in `saved-march-x`. When defense ends, the saved march point is restored. The source also changes between `DefendingLC` and `DefendingMill` by locating local economic buildings near the group. fileciteturn380file0L2-L2

This establishes a direct military ↔ economy/defense cross-region edge.

## Jump closure

Confirmed march-control jumps include:

- large positive jump out of attack/march calculation when attack/defense prerequisites are absent;
- `+10`, `+7`, `+6`, `+4`, `+2` transitions used to skip between march-state cases;
- `+12` to bypass march geometry when defense/attack/target prerequisites fail;
- `-2` loops over enemy-player target searches.

The important property is that the march machine uses jumps to serialize mutually exclusive march-state cases. Removing the jumps would execute multiple case bodies rather than the intended state transition.

## Completion observation

March completion is not a command acknowledgement. The source uses:

- point-distance between group and march point;
- `gl-march-type`;
- defense/attack flags;
- enemy Town Center presence;
- enemy strategy;
- age/time;
- group size.

These conditions cause the machine to advance or retreat between march states.

## Recovery behavior

- return home when defending;
- restore saved march point after defense;
- downgrade march mode under KRUSH pressure;
- restore larger march mode when conditions permit;
- recalculate enemy coordinates when the enemy loses its Town Center;
- rebuild nearest-target coordinates when no candidate exists.

This is the military machine's principal **recovery/re-entry mechanism**.

---

# 6. M04 — Military/production boundary: skirmisher cancellation

## Source

**L4300-L4364**, with the explicit `Cancel skirms` rule visible immediately before the QHOUSES construction section. fileciteturn372file0L2-L2

## Entry

- Castle Age;
- `gl-current-build-item = ESKIRMS`;
- archery range exists;
- Elite Skirmisher is research-available;
- at least two skirmishers are pending;
- Elite Skirmisher research is not yet pending.

## Engine action

The rule searches the archery range, resolves its point, and issues:

```text
up-target-point 0 action-stop -1 -1
```

This is a direct production-queue/military-policy intervention: military composition/progression state can terminate an existing skirmisher action before construction/economic logic resumes.

## Completion/recovery

The rule self-disables after issuing the stop command. It does **not** claim research completion or unit cancellation as a world-state fact. The completion semantics are therefore command-side only unless later world observation establishes the queue state.

## Cross-region edges

```text
military composition
      ↓
production queue
      ↓
research/progression
      ↓
construction/economic source-order continuation
```

This is strong evidence that Production and Military cannot be cleanly separated into independent strategic managers.

---

# 7. M05 — TC garrison and pre-attack villager protection

## Source

**L4850-L5200**. The recovered QGARRISONING TC / QVILLS region explicitly measures nearby military units, selects villagers, garrisons them, and later ungarrisons them. fileciteturn382file0L2-L2

## Entry

`gl-garrison-tc` is the persistent control state. The machine searches for nearby enemy units around home, then searches for candidate villagers.

## State reads

- `gl-garrison-tc`;
- `home-id`;
- `sn-focus-player-number`;
- enemy military presence near home;
- villager distance to home;
- villager target/resource exclusions;
- sheep/deer context.

## State writes

- `gl-garrison-tc` from `-1` → `1` → `-1`;
- `gl-saved-focus-player`;
- `SPLIT`;
- focus-player strategic number;
- `gl-enemy-attack-size`;
- retreat threshold `goal`.

## Engine commands

- search/filter operations;
- `up-set-target-by-id home-id`;
- `up-target-objects ... action-garrison`;
- `up-ungarrison c: town-center`.

## Completion observation

Garrison completion is inferred from a subsequent search state: after the garrison command, the machine searches for units near home and ungarrisons when no qualifying units remain. The command itself is not completion proof.

## Recovery

If no enemy units are found, the focus-player loop advances. If no villagers qualify, the state remains eligible for subsequent evaluation. This is a search-driven retry mechanism rather than a separate recovery routine.

## Cross-region edges

- Defense → economy: villagers are removed from exposed economic positions.
- Military → construction/economy: enemy attack changes the safe operating envelope for civilian work.
- Military → scouting: focus-player scanning is shared with other military searches.

---

# 8. M06 — Enemy-attack estimation and villager retreat

## Source

**L5000-L5450**, including enemy-attack centroid construction, weak-villager retreat, skirmisher defense, and anti-scout transition. fileciteturn373file0L2-L2 fileciteturn383file0L2-L2

## Entry

The region first computes the enemy attack center from nearby military units and then uses that center to evaluate civilian exposure.

## State reads

- enemy military unit positions;
- `gl-enemy-attack-size`;
- `enemy-attack-x/y`;
- home position;
- villager HP;
- villager action/target state;
- current age and age-time;
- player validity;
- focus-player number.

## State writes

- `enemy-attack-x/y`;
- `gl-enemy-attack-size`;
- `goal`, `goal1`, `lt`, `rt` scratch counts;
- villager retreat/garrison state;
- `gl-aggressive-vills`;
- `SPLIT`;
- focus-player traversal state.

## Engine operations

The centroid algorithm repeatedly:

1. searches nearby enemy military units;
2. accumulates their coordinates;
3. counts sampled points;
4. divides accumulated X/Y by the count;
5. writes `enemy-attack-x`.

The source explicitly loops through players using `up-jump-rule -2` and `-4`, then derives the centroid. fileciteturn373file0L2-L2

## Completion observation

The centroid is considered available when `goal1 > 0`; civilian protection rules then use distance from the calculated enemy center.

## Recovery

- no enemy units → continue focus-player scan;
- insufficient nearby military → no retreat action;
- enemy center moves → later search recomputes it;
- weak villagers → move toward home and away from attacker;
- military threat persists → transition into skirmisher/infantry/scout response.

This is an explicit observe → aggregate → classify exposure → act → reassess loop.

---

# 9. M07 — Anti-scout, hurt-infantry, and local villager combat

## Source

**L5200-L5680**, with the anti-scout, Hurt Militia/MAA, Hurt Careless Enemy Scout, anti-luring, and ram-response subsections. fileciteturn383file0L2-L2 fileciteturn384file0L2-L2

## Entry

Enemy scout/infantry/ram observations and local civilian vulnerability conditions.

## State reads

- enemy scout/cavalry/eagle presence;
- enemy militia/spearman presence;
- villager HP;
- villager IDs reserved as `lurer-id` / `shooter-id`;
- `gl-aggressive-vills`;
- current enemy age/age-time;
- threat-time;
- battering-ram count.

## State writes

- `goal`, `goal1`, `goal2`, `lt`, `rt` search counters;
- `SPLIT`;
- `gl-aggressive-vills`;
- focus-player number;
- `gl-threat-time` is consumed as a gating state;
- timers such as `t-infantry-attack`.

## Engine commands

- `up-target-objects ... action-default` for local attacks;
- `up-target-point home-x action-stop` for disengagement;
- `up-target-point home-x action-garrison` for civilian protection;
- search/filter/target operations;
- `enable-timer t-infantry-attack`.

The infantry response explicitly attacks selected enemy infantry, starts `t-infantry-attack`, sets `gl-aggressive-vills = 3`, and later stops the villagers when the timer expires, they are too far from home, or the qualifying enemy disappears. fileciteturn383file0L2-L2

## Jump closure

Confirmed local-control edges include:

- enemy-player search loops with `-2`;
- skip from Hurt Militia/MAA when enemy age/age-time makes the routine obsolete (`+8`);
- skip from one-vill scout response to two-vill response (`+5`);
- repeated scout-search loops with `-2`;
- ram-search loop with `-2`.

## Completion observation

- target search count (`rt`, `lt`, `goal1`);
- enemy presence;
- villager count near target;
- villager HP;
- distance to home;
- attack timer status;
- enemy ram count.

## Recovery

The source explicitly stops aggressive villagers and returns them home when the attack condition ceases. It also transitions from one-vill to two-vill scout handling based on age and current aggression state. This is direct recovery behavior, not inferred retry logic. fileciteturn384file0L2-L2

---

# 10. M08 — Ram-response terminal military slice

## Source

The RAM RAMMING subsection ends immediately before the `QSHEEP` section, at approximately **L5680-L5700**. fileciteturn385file0L2-L2

## Entry

- enemy player is valid;
- enemy has one or more battering rams;
- a ram is within the defined home-area search radius.

## State reads

- battering-ram count;
- ram position;
- villager IDs/HP;
- lurer/shooter exclusions.

## Engine action

The machine selects qualifying villagers and issues:

```text
up-target-objects 1 action-default -1 -1
```

The intended effect is local ram attack. The source does not supply an explicit `ram-destroyed` completion predicate in this slice.

## Completion/recovery

Completion is therefore **not established by the command**. Subsequent source-order military/defensive observations must establish whether the ram remains. This is a clean example of the distinction between command issuance and world-state completion.

## Boundary

The next source section is `QSHEEP`, which is economic/scouting behavior rather than military combat. The ram slice is therefore the terminal military slice in this recovered late-source neighborhood. fileciteturn385file0L2-L2

---

# 11. Military state read/write registry

## Primary persistent military writers

| State | Principal writer family | Principal consumers |
|---|---|---|
| `gl-current-group` | M01/group setup | target/march/combat |
| `gl-ranged-group-state` | M01 + combat transitions | firing/movement/retreat |
| `gl-ranged-eval` | M02 evaluation | target selection / attack behavior |
| `gl-can-fire` | M02 firing arbitration | ranged execution |
| `gl-can-move` | M02 firing/movement arbitration | movement execution |
| `gl-target-distance` | M02 target stats | fire/move decision |
| `target-id` | M02 target stats | target execution |
| `gl-target-type/class/hp` | M02 target stats | target scoring/action |
| `gl-march-type` | M03 march-state machine | movement/defense |
| `march-x/y` | M03 maintenance | movement |
| `saved-march-x/y` | M03 defense return | post-defense re-entry |
| `gl-defend-town` | M01/M03 defense logic | march/retreat |
| `gl-attacking` | M03 attack-state logic | attack/defense |
| `enemy-x` | M03 enemy-location logic | march geometry |
| `nearest-tc-x/y` | M03 target acquisition | attack approach |
| `nearest-castle-x/y` | M03 target acquisition | target scoring |
| `nearest-tower-x/y` | M03 target acquisition | tactical scoring |
| `gl-enemy-group-size` | M02/M03 search | evaluation / superiority |
| `gl-total-military-in-range` | M02 range search | tactical assessment |
| `gl-melee-in-range` | M02 range search | tactical assessment |
| `gl-cavalry-attacking` | M02 range search | tactical assessment |
| `gl-mangos-nearby` | M02 range search | tactical assessment |
| `enemy-attack-x/y` | M06 centroid | civilian retreat / defense |
| `gl-enemy-attack-size` | M05/M06 | retreat threshold |
| `gl-aggressive-vills` | M06/M07 | local civilian combat/recovery |
| `gl-garrison-tc` | M05 | garrison/ungarrison |

## Shared scratch state

The machine heavily reuses:

- `goal`;
- `goal1`;
- `goal2`;
- `goal3`;
- `goal5`;
- `goal6`;
- `goal7`;
- `goal8`;
- `goal9`;
- `lt`;
- `rt`;
- `SPLIT`;
- `sn-focus-player-number`.

These are not independent namespaces. Their semantics are determined by the current source-order neighborhood. A transplant must therefore preserve the surrounding rule closure rather than simply copying variable names.

---

# 12. Engine command inventory

The military control region directly uses or participates in the following command families.

### Search / observation

```text
up-full-reset-search
up-set-target-point
up-set-target-object
up-set-target-by-id
up-find-local
up-find-remote
up-find-status-remote
up-find-resource
up-filter-distance
up-filter-status
up-filter-include
up-reset-filters
up-clean-search
up-remove-objects
up-get-search-state
up-get-object-data
up-get-point
up-get-point-distance
up-point-contains
```

### Tactical geometry

```text
up-copy-point
up-lerp-tiles
up-cross-tiles
up-bound-point
```

### Combat / movement execution

```text
up-target-objects ... action-default
up-target-point ... action-move
up-target-point ... action-stop
up-target-point ... action-patrol
up-target-point ... action-garrison
up-ungarrison
```

### Control flow

```text
up-jump-rule
set-goal
up-modify-goal
set-strategic-number
up-modify-sn
set-goal SPLIT
```

### Temporal control

```text
enable-timer
disable-timer
up-timer-status
timer-triggered
```

This is a substantial executor surface. It is not merely a classification layer.

---

# 13. Completion-observation model

Shadow does not expose a single military completion bit. Completion is distributed by objective.

| Objective | Command | Observable closure |
|---|---|---|
| target acquisition | search/target selection | target count + target data |
| fire/move cycle | target-point actions | distance + next-attack state + timer |
| march | movement/position state | distance to march point + march type |
| defense | move home | `gl-defend-town`, group position, subsequent state |
| garrison | `action-garrison` | later local search / release condition |
| ungarrison | `up-ungarrison` | subsequent search/state |
| villager retreat | `action-move` | position/distance state |
| local infantry attack | `action-default` | enemy presence + attack timer + villager state |
| scout attack | `action-default` | enemy scout presence + nearby villager count |
| ram attack | `action-default` | later ram presence; no explicit terminal predicate in the slice |
| skirmisher cancellation | `action-stop` | source does not establish queue completion itself |

This table is intentionally conservative: it does not promote command acceptance to world realization.

---

# 14. Recovery / re-entry architecture

Military recovery is distributed through the same control machine that performs execution.

```text
                     MILITARY OBJECTIVE
                            |
                            v
                       OBSERVE STATE
                            |
                  +---------+---------+
                  |                   |
               VALID               INVALID
                  |                   |
                  v                   v
             EXECUTE              RESELECT
                  |                   |
                  v                   |
             REOBSERVE <-------------+
                  |
          +-------+--------+
          |                |
       CONTINUE          THREAT / STALE
          |                |
          v                v
        REFORM          RETREAT / STOP
          |                |
          +-------+--------+
                  |
                  v
                RE-ENTER
```

Directly demonstrated recovery mechanisms include:

- repeated focus-player search loops;
- target-list rebuilding;
- `MINI-RETREAT` filtering;
- failsafe timer transitions;
- movement/attack state reversal;
- march downgrade from Four/Three/Two to One under KRUSH pressure;
- march restoration after defense;
- garrison followed by later ungarrison;
- aggressive-villager stop/release;
- recomputation of enemy attack center;
- recomputation of enemy/TC/castle/tower targets.

There is therefore no defensible basis for transplanting Military as a one-shot `attack` routine.

---

# 15. Jump closure ledger

The following edges are the **certified military-region jump closure from the recovered source windows**. Large positive jumps are listed by semantic destination because the canonical source-order formula is the authoritative address calculation.

| Source slice | Jump | Closure purpose |
|---|---:|---|
| M01 QADVANTAGE | `+44` | bypass extended ranged-evaluation block |
| M02 QGROUP/QNA | `+12` | bypass ranged-group analysis when no group exists |
| M02 QTARGET | `+56` | bypass target acquisition when no ranged group exists |
| M02 enemy-player search | `-2` | scan next focus player |
| M02 BUILDERS | `-5` | repeat focus-player search |
| M02 MILITARY CLOSE | `-4` | repeat military target search |
| M02 VILLS CLOSE | `-3` | repeat villager target search |
| M02 MILITARY ALL | `-7` | repeat broad military target search |
| M02 MILITARY QUICKIES | `-7` | repeat quick-target search |
| M02 nearest-TC/castle/tower searches | `-2` | repeat player search |
| M03 march/attack prerequisite bypass | `+12` | skip march construction when prerequisites fail |
| M03 March One → later case | `+10` / `+7` | serialize march-state cases |
| M03 March Two → later case | `+4` | advance march-state case |
| M03 March Three → later case | `+2` | advance march-state case |
| M05 garrison focus-player loop | `-3` | scan players for nearby military |
| M05 garrison prerequisite bypass | `+11` | skip garrison routine when disabled |
| M05 enemy-attack prerequisite bypass | `+9` | skip civilian retreat when no enemy attack point |
| M06 enemy-centroid search | `-2` / `-4` | rescan focus players and accumulate attack points |
| M06 Hurt Militia | `+8` | bypass obsolete infantry routine at late enemy age |
| M07 scout one-vill path | `+5` | enter two-vill path under exclusion condition |
| M07 scout search | `-2` | repeat focus-player scan |
| M07 ram search | `-2` | repeat focus-player scan |

**Known explicit source-order example:** rule 27 uses `up-jump-rule 44`, producing rule 72 under the repository's documented jump semantics. fileciteturn375file0L2-L2

The complete closure must retain both these jump edges and the normal source-order successor. Deleting a jump changes which subsequent predicates are evaluated and therefore changes the machine even if every copied rule body remains textually identical.

---

# 16. Cross-region edge matrix

| Military edge | External region | Mechanism | Evidence |
|---|---|---|---|
| Research → Military | Research/progression | `research-completed` modifies tactical ranges and evaluation | DIRECT |
| Military → Research | Research/progression | enemy composition/strategy conditions trigger research interruptions | DIRECT in research triggers; writer closure distributed |
| Military → Production | Production/composition | skirmisher cancellation; observed military capability/deficit | DIRECT + COMPOSED |
| Production → Military | Production | unit populations and capability alter group/tactical evaluation | COMPOSED |
| Military → Economy | Economy | `gl-defend-town`, enemy-attack center, villager retreat/garrison | DIRECT |
| Economy → Military | Economy | resource/age/strategy state changes military eligibility and march behavior | COMPOSED |
| Military → Construction | Construction | defense/emergency state competes with civilian construction/progression | COMPOSED |
| Construction → Military | Construction | building counts/positions affect target selection and tactical geometry | COMPOSED |
| Scouting → Military | Scouting | scout IDs/positions, enemy observations, target information | DIRECT |
| Military → Scouting | Scouting | military command/search filters and enemy observations alter scouting safety | COMPOSED |
| Defense ↔ Military | Defense | `gl-defend-town`, march points, garrison state | DIRECT |
| Military ↔ Global control | Global | timers, `SPLIT`, focus-player traversal, shared goals | DIRECT |

---

# 17. Architectural finding

The canonical evidence does **not** support the model:

```text
Military = observation/classification
        ↓
Production = execution
```

Nor does it support:

```text
Military
  ↓
Authority
  ↓
Execution
```

The actual donor contains military-owned execution choreography:

```text
OBSERVE
  ↓
AGGREGATE
  ↓
EVALUATE
  ↓
SELECT
  ↓
RESOLVE TARGET / POINT
  ↓
MUTATE PERSISTENT TACTICAL STATE
  ↓
ISSUE ENGINE ACTION
  ↓
REOBSERVE
  ↓
CONTINUE / STOP / RETREAT / RETARGET
  ↓
RE-ENTER
```

At the same time, resource/progression ownership remains distributed to economic, research, construction, and production regions.

Therefore the correct ShadowByzantine reconstruction unit is a **large military control region**, not a generic military transaction service.

---

# 18. What must be transplanted together

A faithful Military transplant must preserve at least these coupled families:

### A. Tactical state foundation

`gl-current-group`, `gl-ranged-group-state`, range variables, firing/movement state, march state.

### B. Tactical evaluation

`gl-ranged-eval`, superiority, damage potential, range/armor advantage, enemy/own group sizes, close-range counts.

### C. Target acquisition

target class/type/id/HP/position/distance plus nearest TC/castle/tower and target-player traversal.

### D. Group/march control

`gl-march-type`, march points, defense return point, enemy coordinates, march-state jumps.

### E. Defense/emergency

garrison, villager retreat, enemy attack centroid, town-defense transitions.

### F. Local tactical micro

anti-scout, hurt-infantry, ram response, aggressive-villager timer, stop/re-entry paths.

### G. Control topology

All relevant `up-jump-rule` edges, normal source-order succession, `disable-self`, timers, and focus-player loops.

Omitting any of these creates a different machine even if the visible attack behavior initially resembles Shadow.

---

# 19. Runtime qualification boundary

This atlas is **STATIC / DIRECT / COMPOSED** forensic evidence. It is not a runtime firing proof.

Specifically not established solely by this source reconstruction:

- that every military rule fires in a particular game;
- that `up-target-objects` immediately produces the intended unit action;
- that attack/move commands complete successfully;
- that garrison commands are accepted in every state;
- that a ram is destroyed after the ram-response command;
- that skirmisher cancellation always removes the pending queue item;
- that every recovery path is reachable under live engine scheduling.

The correct promotion boundary remains:

```text
STATIC SOURCE
    ↓
CONTROL-FLOW QUALIFICATION
    ↓
RUNTIME COMMAND ACCEPTANCE
    ↓
WORLD-STATE OBSERVATION
    ↓
RUNTIME-QUALIFIED BEHAVIOR
```

No source-order inference should silently promote one level into the next.

---

# 20. Final machine characterization

Shadow's Military region is best understood as a **persistent tactical control machine embedded in the global sequential rule interpreter**.

Its defining properties are:

1. **Persistent tactical memory** — groups, targets, march points, attack/defense flags, range state, timers.
2. **Multi-stage observation** — enemy composition, positions, HP, buildings, military class, technology, attack size.
3. **Numerical tactical evaluation** — superiority, range advantage, armor advantage, damage potential, local counts.
4. **Stateful target selection** — target IDs, target class/type/HP/distance and nearest strategic structures.
5. **Explicit execution** — attack, move, stop, patrol, garrison, ungarrison.
6. **Temporal arbitration** — next-attack thresholds and failsafe/injury timers.
7. **Persistent march-state progression** — MarchingOne through MarchingFour with threat-sensitive reversions.
8. **Distributed recovery** — target reselection, focus-player loops, retreat, stop, garrison, ungarrison, march restoration.
9. **Cross-region coupling** — research changes military capability; military changes research/production/economic priorities; defense changes civilian execution.
10. **Jump-dependent semantics** — large bypasses and local loops are part of the machine, not optional optimization.

The resulting reconstruction target is therefore not `military.per` as an isolated manager. It is the **Military control region plus its writer/reader closure across research, production, economy, construction, scouting, defense, timers, and global control state**.

That is the appropriate unit for the next ShadowByzantine military transplant.