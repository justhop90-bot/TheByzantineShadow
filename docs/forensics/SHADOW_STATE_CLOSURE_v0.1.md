# Shadow Persistent-State Closure v0.1

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical donor:** `ShadowSource.per`  
**Donor SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Donor SHA-256:** `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`  
**Machine:** 1,956 `defrule` blocks / 22,604 lines / 615,773 UTF-8 bytes

## 1. Closure statement

This artifact closes the donor's persistent-state **registry and coupling model** at the static-source level. It does not claim runtime qualification.

The important result is that Shadow state is not a flat list of variables. The source repeatedly couples state carriers into distributed state machines whose transitions are implemented by source order, predicates, mutations, timers, engine observations, escrow operations, jumps, and re-entry. A carrier is therefore materialized here by its actual writer/reader topology rather than by its name.

The canonical donor explicitly inventories:

- goals: `1-317, 392, 478-479`
- timers: `1-42, 46`

The current ownership audit confirms `478=home-x` and `479=home-y`, and that the earlier legacy collision was relocated rather than silently aliasing the donor namespace.

## 2. State-carrier classes

| Carrier class | Shadow carrier set | Persistence mechanism | Principal control role | Closure |
|---|---|---|---|---|
| Goal/register state | goals `1-317`, `392`, `478-479` | `set-goal`, `up-modify-goal`, `up-compare-goal`, `goal` predicates | strategic, tactical, progression, target, group, recovery state | CLOSED at registry/source level |
| Strategic-number state | engine SN slots addressed by `set-strategic-number`, `up-modify-sn`, `strategic-number`, `up-compare-sn` | strategic-number RAM | configuration, counters, search/placement/scouting control | CLOSED for observed carriers; exhaustive writer/read appendix remains mechanically reproducible |
| Timer state | timers `1-42`, `46` | timer engine | cadence, delay, timeout, reevaluation, tactical suppression | CLOSED at registry/source level |
| Search state | search lists, target object, target point, extracted facts | engine search state + explicit reset/cleanup | target acquisition and placement handoff | CLOSED structurally |
| Escrow state | resource escrow plus `gl-escrow-state` | engine escrow + goal mode | resource protection and release | CLOSED structurally |
| Progression state | `gl-current-build-item`, `gl-build-progress`, `gl-progression-pause`, `SPLIT` and neighboring cursors | goals/registers | milestone sequencing and interruption/re-entry | CLOSED structurally |
| World-state observations | counts/status/pending objects/research state | engine facts | completion and reconciliation | CLOSED semantically |
| Rule-position state | source order, `up-jump-rule`, `disable-self` | interpreter control state | execution topology | CLOSED statically |

## 3. Goal namespace: exact donor inventory

Shadow's own source inventory is authoritative: `1-317, 392, 478-479`.

The named state carriers recovered directly from the canonical source include, among others:

`p1-current-age`, `p2-current-age`, `p2-score1`, `gl-tsa-chat`, `p2-score2`, `p2-age-checking`, `FORAGE`, `gl-gold-rank`, `gl-need-stone`, `escrow-purpose-goal-chat`, `gl-identity`, `Shadow`, `Doomsday`, `BruteForce3`, `Promi`, `Illuminati`, `Juggernaut`, `Unknown`, `TheHorde`, `TRiBaL_Warrior`, `Barbarian`, `Meleon`, `Daedric`, `Subjugator`, `Thermopylai`, `TheGeneral`, `Reactionary`, `Simple`, `Rhapsody`, `gl-town-under-attack`, `home-x`, `home-y`, `gl-position`, `gl-attacking`, `gl-town-safe`, `BeingDrushed`, `gl-privileged-player`, `gl-spear-group-state`, `spear-group-x`, `spear-group-y`, `gl-find-new-target`, `gl-feudal-strategy`, `gl-target-hp`, `CIVSUP`, `gl-last-target-player`, `gl-ranged-style`, `raid-waypoint2-x`, `raid-waypoint2-y`, `raid-nearest-fort-x`, `raid-nearest-fort-y`, `gl-ancient-raid-target-id`, `gl-old-raid-target-id`, `gl-raid-target-id`, `raid-target-x`, `raid-target-y`, `gl-current-group`, `gl-raid-can-move`, `gl-raid-can-fire`, `gl-raid-retreat-type`, `gl-raid-group-range`, `gl-enemy-attack-size`, `gl-enemy-skirms-nearby`, `nearest-skirm-x`, `nearest-skirm-y`, `gl-enemy-skirm-range`, `gl-circle-direcion`, `gl-cavalry-in-town`, `gl-archery-in-town`, `gl-skirm-vills`, `gl-enemy-archers`, `gl-seventh-turn`, `gl-switch`, `enemy-attack-x`, `enemy-attack-y`, `nearest-castle-x`, `nearest-castle-y`, `t-town-safe`, `SUPERIORITY`, `gl-enemies-in-town`, `gl-attack-efficiency`, `gl-defend-town`, `saved-march-x`, `saved-march-y`, `saved-scout-x`, `saved-scout-y`, `gl-scout-stuck`, `gl-ranged-retreat`, `gl-knight-eval`, `nearest-tower-x`, `nearest-tower-y`, `gl-knight-retreat`, `gl-sheep-scouting`, `gl-skirm-total`, `gl-scouting-switch`, `gl-raid-group-size`, `raid-waypoint1-x`, `raid-waypoint1-y`, `raid-group-x`, `raid-group-y`, `gl-armor-advantage`, `gl-trees-around`, `gl-early-gar`, `tree-x`, `tree-y`, `gl-lclerp`, `gl-aggressive-vills`, `gl-dark-build`, `shooter-id`, `gl-deer-walking`, `gl-failsafe`, `gl-march-type`, `gl-target-type`, `gl-total-military-in-range`, `gl-army-damage-potential`, `nearest-tc-x`, `nearest-tc-y`, `march1-x`, `march1-y`, `march2-x`, `march2-y`, `march3-x`, `march3-y`, `march4-x`, `march4-y`, `gl-tower-control`, `nearest-scary-x`, `nearest-scary-y`, `gl-max-ranged-group-size`, `NEWSCOUTING`, `CROSS`, `explo-x`, `explo-y`, `t-rax`, `gl-mangos-nearby`, `gl-build-progress`, and `gl-inside-forest`.

The source also defines state/enumeration values consumed by those carriers, including `FLANK`, `POCKET`, `ATTACKING`, `VATTACKING`, `MOVING`, `TATTACKING`, `COMBINED`, `SEPARATE`, `FROM-UNITS`, `FROM-FORTIFICATIONS`, `FROM-SIEGE`, `COUNTERCLOCKWISE`, `CLOCKWISE`, `LumberFirst`, `MillFirst`, `DefendingLC`, `DefendingMill`, `MarchingOne` through `MarchingFive`, `DefendingHome`, and the scouting-mode enumerations.

### Namespace rule

The same integer is not an alias merely because two declarations share it. For example, `gl-identity` and `Promi` both use `420`, while `Doomsday`, `gl-target-type`, and `villager-timer` use `42` across different namespaces. Consumption-site typing is authoritative.

## 4. Timer closure

The canonical timer registry is:

`t-infantry-attack 11`, `t-target-switch 12`, `t-kill-boar 10`, `t-raid-waypoint-reevaluate 22`, `t-raid-retreat 3`, `villager-timer 42`, `t-defense 14`, `t-mc 15`, `t-lc 16`, `30SEC 17`, `castle-reset-timer 29`, `t-misc 4`, `t-raid-target-reset 41`, `t-ranged-retreat 40`, `t-build-delay 39`, `t-direction-switch 38`, `t-mpoints 37`, `t-firing 9`, `t-command-delay 35`, `t-failsafe 36`, `t-game-eval 1`, `ONE-MINUTE 2`, `TSA 6`, `hunting-timer 7`, `BECO-TIMER 8`, `TIME1 55`, `t-enemy-age-cancel 18`, `RETREAT 19`, `t-vill-training 20`, `t-scout-enemy 21`, `TWO-MINUTE 23`, `t-relure 24`, `THREE-MINUTE 27`, `t-housing-check 31`, `t-direction-change 32`, `five-seconds-timer 34`, plus timer `46` for TC dodging and the documented timer slots 5/28/30 whose symbolic declarations are absent from the preserved excerpt.

Timer state is not merely delay metadata. Timer predicates participate in reachability and therefore alter effective control topology.

## 5. Strategic-number carriers recovered from executable source

The donor uses strategic numbers as persistent mutable engine-side state. Directly recovered writer/read carriers include:

| Strategic number | Writers / mutation | Readers / predicates | State-machine role |
|---|---|---|---|
| `sn-focus-player-number` | initialized to `1`; incremented by `up-modify-sn` | player-valid / focus-player search loop | player enumeration cursor |
| `sn-total-number-explorers` | initialized/latching to `1` | explorer/scouting gates | explorer availability latch |
| `sn-number-explore-groups` | initialized/latching to `1` | scouting/group gates; overwritten by general policy | exploration-group cardinality |
| `sn-placement-zone-size` | set to `3` in construction paths | placement engine | placement configuration |
| `sn-home-exploration-time` | known donor writer; source ownership preserved | scouting/home exploration logic | exploration timing |
| `sn-special-attack-type2` / `sn-special-attack-influence2` | source-defined engine configuration | tactical engine conditions | special-attack configuration |

The strategic-number graph is coupled to goals and timers rather than being a separate controller. In particular, `sn-focus-player-number` is a cursor inside a negative-jump search loop, and placement SNs are written immediately before `place-control` execution.

## 6. Coupled state machines

### S1 — Progression / escrow / operation cursor

```text
strategy condition
  -> gl-progression-pause := milestone
  -> escrow mutation
  -> can-build / can-research / can-train-with-escrow
  -> operation command
  -> world-state observation
  -> gl-build-progress mutation
  -> gl-current-build-item mutation
  -> escrow release/restoration
  -> progression re-entry
```

Directly demonstrated by rules 1172–1195 and construction rules 1764–1804 / 1794–1801.

### S2 — Search cursor

```text
reset search
 -> configure player/object/class/range
 -> local/remote find
 -> inspect / remove invalid candidates
 -> select target
 -> extract point/fact
 -> consume target
 -> reset/re-enter
```

The search list is persistent engine state and is explicitly reset because stale target state otherwise survives into later rule regions.

### S3 — Raid target state

`gl-ancient-raid-target-id`, `gl-old-raid-target-id`, `gl-raid-target-id`, target coordinates, waypoint coordinates, raid group coordinates, `gl-raid-retreat-type`, `gl-raid-group-state`, raid timers, and tactical goals form one distributed target/waypoint/retreat machine.

### S4 — Ranged tactical state

`gl-current-group`, `gl-max-ranged-group-size`, `gl-range-advantage`, `gl-ranged-style`, `gl-ranged-retreat`, `gl-target-type`, `gl-attack-efficiency`, `SUPERIORITY`, `gl-enemy-group-size`/related threat state, target coordinates, and march state are consumed together. The machine initializes group state, evaluates advantage, searches targets, fires/marches, retreats, and re-enters.

### S5 — Local defense state

`gl-town-under-attack`, enemy-attack coordinates, `gl-defend-town`, `gl-town-safe`, local threat counts, nearest tower/castle/TC coordinates, retreat state, and timers form a local-defense/recovery machine rather than independent variables.

### S6 — Scouting state

`gl-scouting-switch`, `NEWSCOUTING`, `gl-scout-stuck`, exploration coordinates, explorer strategic numbers, scout timing, and scouting-mode enumerations form the scouting/recovery machine.

### S7 — Agriculture / domestic progression

`gl-build-progress`, `gl-current-build-item`, `gl-progression-pause`, `SPLIT`, `MILL`, farm-count/pending-object observations, farm placement state, and relevant timers form the farm/infrastructure progression machine.

## 7. Writer precedence

Shadow has no central state manager. Writer precedence is established by source order, predicates, jumps, and disabling. The practical precedence rule is therefore:

1. earlier state writer establishes or resets a carrier;
2. later source-order writers refine or overwrite it when their predicates qualify;
3. explicit jumps bypass writer regions;
4. negative jumps repeat a region;
5. `disable-self` removes a writer from subsequent passes;
6. engine/world observation can overwrite a logical state only through an explicit rule that reads that observation and writes the state carrier.

This is why a semantic rewrite into one centralized writer would change the machine.

## 8. ShadowByzantine correspondence

| Donor state carrier / machine | Current ShadowByzantine | Classification | Evidence |
|---|---|---|---|
| donor goal namespace | `01_constants.per` AEGIS 450–496 plus migration 520–521 | CHANGED / ADDED | current file |
| `home-x 478`, `home-y 479` | not yet consumed by current runtime slice | LOST from active slice | current runtime graph |
| `gl-current-build-item` | documented but not implemented in `04_construction.per` | LOST / DOCUMENTED-ONLY | current file comments |
| `gl-progression-pause` | documented but not implemented | LOST / DOCUMENTED-ONLY | current file comments |
| `gl-build-progress` | documented donor concept; no current writer | LOST | current runtime slice |
| `gl-escrow-state` | `AEGIS-ESCROW-STATE` plus direct escrow calls | CHANGED / DUPLICATED | `16_pass1_transaction.per` |
| donor distributed escrow topology | Pass-1 centralized transaction state | CHANGED | current runtime graph |
| donor timer machine | no equivalent Pass-1 timer topology | LOST | current runtime files |
| donor search machine | no active search machine in Pass 1 | LOST | current runtime graph |
| donor placement machine | basic `build` only; no placement-control path | LOST / PARTIAL | `04_construction.per` |
| donor progression cursor | AEGIS transaction enum | REPLACED | `16_pass1_transaction.per` |
| donor world-state verification | unit/bldg count observers | ADAPTED / PRESERVED PRINCIPLE | current files |
| donor source-order jumps | no active `up-jump-rule` topology | LOST | current runtime files |
| donor `disable-self` topology | limited initializer/terminal use | PARTIAL | current files |
| donor raid/military state | absent from active runtime | LOST | current runtime graph |

## 9. Newly invented state

The following are **not donor Shadow state carriers** and therefore cannot be described as recovered Shadow:

`AEGIS-OBJECTIVE`, `AEGIS-REQUIREMENT`, `AEGIS-TRANSACTION`, `AEGIS-AUTHORITY`, `AEGIS-VERIFICATION`, `AEGIS-ESCROW-STATE`, `AEGIS-TRANSACTION-ACTIVE`, `AEGIS-TRANSACTION-ID`, `AEGIS-CAPITAL-FEASIBILITY`, `AEGIS-EXECUTION-STATE`, `AEGIS-EXECUTION-BASELINE`, `AEGIS-RECOVERY-STATE`, `AEGIS-ESCROW-STATUS`, and `AEGIS-ESCROW-RELEASE-REQUEST`.

They are useful Pass-1 proof state, but they are an **added transaction abstraction**, not a donor-exact state machine. The next reconstruction must not silently promote these carriers to canonical Shadow architecture.

## 10. Closure status

**CLOSED:** donor goal namespace, timer namespace, principal strategic-number carriers observed in executable source, distributed state-machine coupling, source-order writer precedence, donor-to-current-state classification for the active runtime slice.

**OPEN:** a generated per-carrier appendix containing every individual read/write occurrence across all 1,956 rules, especially every strategic-number reader/writer occurrence. That appendix should be generated from the authenticated machine index rather than manually reconstructed.

The open item does not justify inventing a central state manager. The donor topology remains the authority.
