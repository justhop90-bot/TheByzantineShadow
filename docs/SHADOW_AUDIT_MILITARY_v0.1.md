# Shadow Military Audit v0.1

## Scope

This artifact isolates target acquisition, scouting, threat detection, composition, tactical groups, raiding, attack evaluation, defense and emergency military systems in `Shadow DC7(1).per`.

## 1. Target acquisition

The donor maintains target player, target age, target type, coordinates, target HP, nearest TC/castle/tower, enemy units in range, raid targets and target switching. The main target section contains approximately 147 rules.

Finding: target selection is a strategic interface. Preserve the underlying knowledge, then expose target validity, confidence, freshness and objective linkage.

Disposition: PRESERVE + FORMALIZE.

## 2. Scouting

Shadow contains sheep scouting, new scouting, circle scouting, enemy scouting, border/flank/mirror/opposite/corner/center patterns, stuck recovery and scouting switches. Map configuration changes exploration distances.

Finding: scouting is active information acquisition, not only movement.

Disposition: PRESERVE + IMPROVE.

## 3. Threat detection

The donor tracks cavalry in town, archery in town, enemies in town, attack size, nearby skirmishers and mangonels, town safety and defensive state. Named costs quantify consequences of ignoring several threats.

Finding: threat valuation is already consequence-sensitive.

Disposition: PRESERVE + FORMALIZE.

## 4. Composition

Dedicated modules cover archers, skirmishers, spears, scouts, knights, mangonels, rams, monks, militia and ranged groups. They combine enemy state, unit counts, goals, strategic numbers and procedural priority.

Finding: this is valuable unit-domain knowledge, but strategic meaning is too tightly coupled to specific units.

Disposition: SUBORDINATE + REBUILD the interface around capability requirements.

## 5. Tactical groups

Raid and ranged-group state tracks identity, size, coordinates, waypoints, target switching, regrouping, retreat, movement, firing and combat modes.

Finding: Shadow already has stateful tactical mission execution. Rebuilding this merely because AEGIS is replacing strategic arbitration would waste proven behavior.

Disposition: PRESERVE + FORMALIZE interface.

## 6. Attack evaluation

Attack efficiency, army damage potential, military superiority and military-in-range state estimate whether offensive action is justified.

Finding: this is an embryonic utility/risk evaluator.

Disposition: PRESERVE evaluation; rebuild terminal decision interface.

## 7. Defense and anti-trush

Town safety, TC garrisoning, anti-trush, defensive groups and threat proximity alter military behavior and economic policy.

Finding: survival has priority-inversion authority over normal economic behavior.

Disposition: PRESERVE + FORMALIZE emergency authority.

## 8. Military strategic bridge

The donor's existing chain is approximately:

observation → enemy classification → target/threat state → military policy → tactical execution.

AEGIS should improve this to:

observation → belief → threat/opportunity → capability requirement → candidate solutions → strategic selection → tactical mission.

## 9. Capability abstraction

For cavalry, the strategic object should not be a particular counter-unit. The requirement is anti-cavalry capability. Candidate solutions can include counter-unit, fortification, mobility, denial, relocation, retreat, counterattack, siege, technology and delay.

This allows military execution to remain modular while strategic selection becomes capability-oriented.

## 10. Conclusion

The military donor contains substantial reusable knowledge. The main improvement target is the interface between threat interpretation and selected capability. Existing scouting, target, tactical-group and combat-evaluation mechanisms should be preserved unless later forensic qualification proves a specific mechanism inadequate.
