# The Byzantine Shadow — System Forensic Deep Dive v0.1

Static forensic decomposition of `Shadow DC7(1).per`.

Source SHA-256: `c6431af3f16597b3de223e65e7b60db6c0b22266c0684915ed435bbb054f55b4`.

Baseline: 22,603 lines; 1,956 rules; 1,503 constants; 1,193 goal writes; 440 strategic-number writes; 188 jump calls; 178 escrow-percentage writes; 107 escrow releases; 43 escrow-aware builds; 28 escrow-aware researches; 4 escrow-aware trains.

This is static evidence, not runtime proof. The source itself warns that unused legacy code may remain, so deletion requires reachability and precedence qualification.

## Executive finding

Shadow is a distributed control system, not merely a build order. Its major machines are configuration, state storage, target selection, scouting, food logistics, villager economy, strategy selection, enemy-strategy inference, threat/defense, military composition, tactical missions, force evaluation, progression, escrow, research, construction, market balancing, emergency response, telemetry, and procedural arbitration.

The architectural thesis is therefore surgical: preserve the economic/transaction substrate; expose and improve the strategic authority boundary.

## System disposition

| System | Finding | Disposition |
|---|---|---|
| Initialization/configuration | map/team/environment policy defines feasible behavior | PRESERVE + FORMALIZE |
| State namespace | goals/SNs encode facts, modes, counters, coordinates and state machines | PRESERVE semantics; REBUILD registry |
| Target acquisition | maintains target player, age, type, coordinates, nearby threats and raid targets | PRESERVE + FORMALIZE |
| Scouting | active information-acquisition policy with multiple scout modes | PRESERVE + IMPROVE |
| Food logistics | sheep/luring/forage/farm system manages food continuity under uncertainty | PRESERVE + IMPROVE |
| Villager economy | adaptive gathering/building/drop-site policy | PRESERVE + IMPROVE |
| Strategy selection | explicit FLUSH/KRUSH doctrine selection | REPLACE as primary authority; preserve modes |
| Enemy strategy | DRUSH/KRUSH/FC/FLUSH/SCRUSH hypotheses from observations | PRESERVE + GENERALIZE |
| Threat/defense | town safety, enemy presence and cost-of-ignoring concepts | PRESERVE + FORMALIZE |
| Composition | unit-specific production policies | SUBORDINATE to capability arbitration |
| Raiding/tactical missions | stateful groups, waypoints, retreat and combat modes | PRESERVE + interface |
| Attack evaluation | attack efficiency, damage potential, superiority | PRESERVE evaluation; rebuild decision interface |
| Progression | current item, progress and pause form implicit scheduler | PRESERVE + FORMALIZE |
| Escrow | reservation and transaction-funding substrate | KEEP + FORMALIZE |
| Research | progression-integrated escrow-aware transactions | PRESERVE execution; subordinate priority |
| Construction | placement, pending objects and escrow-aware builds | PRESERVE execution |
| Market | age-sensitive liquidity balancing | PRESERVE + IMPROVE |
| Emergency/failsafe | anti-trush, garrison, cancellation and survival behavior | PRESERVE + FORMALIZE |
| Telemetry | extensive inspection of strategic/economic state | PRESERVE + NORMALIZE |
| Rule order/jumps | procedural arbitration across domains | RETAIN primitive; expose semantics |
| Legacy/conflicts | duplicate and historical paths exist | QUARANTINE pending proof |

## Core conclusion

Shadow's principal limitation is not absence of strategic mechanisms. It is that authority is distributed across goals, strategic numbers, timers, thresholds, rule order, jumps, progression state, escrow and executor side effects. The correct AEGIS intervention is extraction and augmentation, not wholesale transplantation.

> Do not replace Shadow's knowledge merely because it is encoded procedurally. Extract it, expose its authority, improve its representation, and replace only the decision boundary that prevents reasoning about competing capabilities.
