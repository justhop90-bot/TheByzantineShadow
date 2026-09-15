# Shadow Strategy Audit v0.1

Static source analysis of the supplied Shadow donor.

The strategy layer establishes FLUSH and KRUSH modes through game time, age, player validity, allies, taunts, and map-position conditions. This is genuine doctrine selection, but it is not a generalized objective model.

Enemy-strategy inference classifies observed behavior into DRUSH, KRUSH, FC, FLUSH, SCRUSH and possible-KRUSH states using units, buildings, age, military population and score relationships. This is valuable donor knowledge and should be generalized into observation, hypothesis, confidence and threat state.

Target logic maintains target player, target age/type, coordinates, HP, nearby military, fortifications, raid targets and target switching. It should be preserved and formalized as an objective/target interface.

Threat logic tracks cavalry, archery, enemies in town, attack size, town safety, and qualitative costs of ignoring threats. This should become evidence for urgency and capability requirements.

Attack evaluation tracks attack efficiency, damage potential and military superiority. Preserve the evaluation; rebuild only the terminal decision interface.

Progression uses current build item, build progress and progression pause. These form an implicit scheduler: current item is a priority token, progress is sequence state, pause is suspension, and observed completion advances state. Preserve this behavior and formalize it.

Procedural priority is heavily expressed through rule order and jump operations. Static counting found approximately 188 jump calls. Rule order is therefore part of the effective control graph and must be retained as evidence during refactoring.

The strategic replacement target is not Shadow's knowledge. It is the opaque decision boundary that converts observations and conditions into the next protected commitment.

Target architecture:

WORLD → OBSERVATION → BELIEF → THREAT/OPPORTUNITY → OBJECTIVE → CAPABILITY REQUIREMENT → CAPABILITY DEFICIT → CANDIDATES → ARBITRATION → COMMITMENT → SHADOW ECONOMIC SUBSTRATE.

First qualification case: cavalry observation → anti-cavalry capability requirement → deficit → candidate responses → commitment → economic funding → execution → verification → reassessment.
