# Shadow → Byzantine Escrow Transition Rule Audit v0.1

**Date:** 2026-09-16  
**Repository:** `justhop90-bot/TheByzantineShadow`  
**Canonical source:** `ShadowSource.per`  
**Canonical blob SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Scope:** rule-level evidence for every recovered Shadow rule used to justify a Byzantine escrow state transition.

## 1. Evidence contract

This is a static forensic audit. It does not claim that any rule fired in a live AoE2DE run. The classifications are:

- **DIRECT** — the exact Shadow rule establishes the relevant predicate/action relationship.
- **COMPOSED** — multiple Shadow rules together establish the transition pattern.
- **INFERRED** — the proposed Byzantine state semantics are a reasoned abstraction over Shadow evidence, but Shadow does not explicitly encode that state/transition.
- **BYZANTINE-GENERALIZATION** — new control semantics required by the reconstructed Byzantine machine; not established by Shadow itself.

The most important proof boundary is unchanged: **command issuance is not completion; escrow mutation is not proof of successful reservation; `release-escrow` is not proof of physical release; `gl-escrow-state` is an engine accounting-mode selector, not a logical commitment owner.**

---

## 2. Byzantine transition contract

```text
IDLE
  ↓ authorized requirement
RESERVING
  ↓ reservation observed
PROTECTED
  ↓ feasibility + authority + target validity
EXECUTING
  ↓ command issued
VERIFYING
  ├─ completion-grade world evidence → RELEASE
  ├─ deadline/progress failure       → TIMEOUT
  └─ contradiction/failure           → RECOVERY

RELEASE
  ↓ physical + logical reconciliation
IDLE

TIMEOUT → RECOVERY
RECOVERY → RESERVING | IDLE
```

`PROTECTED`, `VERIFYING`, `TIMEOUT`, and explicit transaction-style recovery are not literal Shadow states. They are reconstruction states. The Shadow evidence is the substrate from which those states are derived.

---

# 3. Rule-by-rule transition table — research escrow families

## F01 — Scale Mail, rules 1172–1174

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1172** | `IDLE → RESERVING` trigger | `(goal gl-strategy FLUSH)`; `(game-time >= 1080)`; `(current-age >= feudal-age)`; `(goal gl-progression-pause -1)`; `(building-type-count blacksmith > 0)`; `(or (player-valid 5) (or (goal gl-enemy-strategy KRUSH) (goal gl-enemy-strategy POSSIBLE-KRUSH)))`; `(up-research-status c: ri-scale-mail < research-pending)` | `(set-goal gl-progression-pause SCALEMAIL)` | **DIRECT** for requirement admission; **COMPOSED** for Byzantine `IDLE→RESERVING` | No runtime proof that this predicate fires; no proof that Scale Mail is still the correct Byzantine requirement when the action executes; no proof of exclusivity against competing pause writers. |
| **1173** | `RESERVING → PROTECTED` reservation write | `(goal gl-progression-pause SCALEMAIL)` | `(up-modify-escrow food c:max 100)` | **DIRECT** for escrow mutation; **INFERRED** for successful protection | No observation proving escrow increased to the intended amount, persisted, remained owned by this requirement, or did not conflict with another food escrow writer. |
| **1174** | `PROTECTED → EXECUTING` and source-local release latch | `(goal gl-progression-pause SCALEMAIL)`; `(can-research-with-escrow ri-scale-mail)` | `(up-research gl-escrow-state c: ri-scale-mail)`; `(set-goal gl-progression-pause -1)`; `(set-escrow-percentage food 0)`; `(release-escrow food)` | **DIRECT** for gate/command/release ordering; **COMPOSED** for `PROTECTED→EXECUTING`; **BYZANTINE-GENERALIZATION** for verified release | No proof the research command was accepted; no proof research completed; no proof escrow release reached zero; no proof clearing pause did not race with another writer; no proof world state reflects the technology. |

## F02 — Chain Mail, rules 1175–1177

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1175** | `IDLE → RESERVING` trigger | `(goal gl-strategy FLUSH)`; `(goal gl-progression-pause -1)`; `(research-completed ri-pikeman)`; `(up-research-status c: ri-chain-mail < research-pending)`; `(up-research-status c: ri-scale-mail >= research-pending)`; `(up-research-status c: ri-bodkin-arrow >= research-pending)`; `(or (players-building-type-count any-enemy stable >= 2) (or (players-unit-type-count any-enemy knight-line >= 4) (players-unit-type-count any-enemy scout-cavalry-line >= 6)))` | `(set-goal gl-progression-pause CHAINMAIL)` | **DIRECT** trigger; **COMPOSED** transition | No runtime proof of trigger firing or that threat telemetry remained valid through reservation. |
| **1176** | `RESERVING → PROTECTED` | `(goal gl-progression-pause CHAINMAIL)` | `(up-modify-escrow food c:max 200)`; `(up-modify-escrow gold c:max 100)` | **DIRECT** mutation; **INFERRED** protection | No proof both resource reservations were actually established atomically or retained for Chain Mail. |
| **1177** | `PROTECTED → EXECUTING` + release | `(goal gl-progression-pause CHAINMAIL)`; `(can-research-with-escrow ri-chain-mail)` | `(up-research gl-escrow-state c: ri-chain-mail)`; `(set-goal gl-progression-pause -1)`; `(set-escrow-percentage food 0)`; `(set-escrow-percentage gold 0)`; `(release-escrow food)`; `(release-escrow gold)` | **DIRECT** command/release pattern; **COMPOSED** state transition | No proof command accepted/completed; no proof food/gold release completed; no proof progression cursor correctly resumed. |

## F03 — Iron Casting KRUSH, rules 1178–1182

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1178** | `PROTECTED → EXECUTING` | `(goal gl-strategy KRUSH)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item IRONCASTING)`; `(can-research-with-escrow ri-iron-casting)` | `(up-research gl-escrow-state c: ri-iron-casting)` | **DIRECT** | No proof command accepted or completed; no proof escrow mode corresponded to intended logical owner. |
| **1179** | `VERIFYING → RECOVERY` / cursor correction | `(goal gl-strategy KRUSH)`; `(up-research-status c: ri-iron-casting < research-pending)`; `(up-compare-goal gl-build-progress > KrushIronCastingNumber)` | `(set-goal gl-build-progress KrushIronCastingNumber)` | **DIRECT** reconciliation; **COMPOSED** recovery semantics | No proof the observed status was stale rather than genuinely incomplete; no proof rewinding progress was safe relative to other commitments. |
| **1180** | `RECOVERY → RESERVING` / restore cursor | `(goal gl-strategy KRUSH)`; `(up-compare-goal gl-current-build-item != IRONCASTING)`; `(up-compare-goal gl-build-progress == KrushIronCastingNumber)` | `(set-goal gl-current-build-item IRONCASTING)` | **DIRECT** cursor restoration; **COMPOSED** re-entry | No proof the restored item remained valid; no attempt identity or stale-commitment protection. |
| **1181** | `RESERVING → PROTECTED` policy | `(goal gl-strategy KRUSH)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == IRONCASTING)` | `(set-escrow-percentage food LOW-ESCROW)`; `(set-escrow-percentage gold LOW-ESCROW)`; `(set-escrow-percentage wood 0)`; `(release-escrow wood)` | **DIRECT** | No proof LOW-ESCROW produced the intended physical reserve; no proof wood release completed. |
| **1182** | `VERIFYING → RELEASE/REASSESS` completion observer | `(goal gl-strategy KRUSH)`; `(goal gl-current-build-item IRONCASTING)`; `(up-research-status c: ri-iron-casting >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** observer; **COMPOSED** transition | `research-pending` is not completion-grade proof; no proof research completed; no proof release occurred; no proof increment was not duplicated. |

## F04 — Iron Casting FLUSH, rules 1183–1187

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1183** | `PROTECTED → EXECUTING` | `(goal gl-strategy FLUSH)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item IRONCASTING)`; `(can-research-with-escrow ri-iron-casting)` | `(up-research gl-escrow-state c: ri-iron-casting)` | **DIRECT** | No command acceptance/completion proof. |
| **1184** | `VERIFYING → RECOVERY` / cursor correction | `(goal gl-strategy FLUSH)`; `(up-research-status c: ri-iron-casting < research-pending)`; `(up-compare-goal gl-build-progress > IronCastingNumber)` | `(set-goal gl-build-progress IronCastingNumber)` | **DIRECT** reconciliation | No runtime proof rewind was needed or safe. |
| **1185** | `RECOVERY → RESERVING` / restore cursor | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-current-build-item != IRONCASTING)`; `(up-compare-goal gl-build-progress == IronCastingNumber)` | `(set-goal gl-current-build-item IRONCASTING)` | **DIRECT** | No runtime proof current-item restoration was correct. |
| **1186** | `RESERVING → PROTECTED` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == IRONCASTING)` | `(up-modify-escrow food c:max 220)`; `(up-modify-escrow gold c:max 120)`; `(set-escrow-percentage wood 0)`; `(release-escrow wood)` | **DIRECT** | No proof 220/120 reservations actually existed or remained associated with Iron Casting. |
| **1187** | `VERIFYING → REASSESS` | `(goal gl-strategy FLUSH)`; `(goal gl-current-build-item IRONCASTING)`; `(up-research-status c: ri-iron-casting >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** observer; **COMPOSED** state transition | `research-pending` does not prove completion; no runtime proof progression advanced exactly once. |

## F05 — Forging FLUSH, rules 1188–1192

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1188** | `PROTECTED → EXECUTING` | `(goal gl-strategy FLUSH)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item FORGING)`; `(can-research-with-escrow ri-forging)` | `(up-research gl-escrow-state c: ri-forging)` | **DIRECT** | No proof command accepted/completed. |
| **1189** | `VERIFYING → RECOVERY` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-build-progress > ForgingNumber)`; `(up-research-status c: ri-forging < research-pending)` | `(set-goal gl-build-progress ForgingNumber)` | **DIRECT** reconciliation | No proof stale/incorrect progress was actually observed at runtime. |
| **1190** | `RECOVERY → RESERVING` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-current-build-item != FORGING)`; `(up-compare-goal gl-build-progress == ForgingNumber)` | `(set-goal gl-current-build-item FORGING)` | **DIRECT** | No proof restored item was still valid. |
| **1191** | `RESERVING → PROTECTED` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == FORGING)` | `(set-escrow-percentage food MID-ESCROW)`; `(set-escrow-percentage wood 0)`; `(set-escrow-percentage gold 0)`; `(release-escrow wood)`; `(release-escrow gold)` | **DIRECT** | No proof MID escrow protected the intended amount or release completed. |
| **1192** | `VERIFYING → REASSESS` | `(goal gl-strategy FLUSH)`; `(goal gl-current-build-item FORGING)`; `(up-research-status c: ri-forging >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** observer; **COMPOSED** | No completion-grade runtime proof. |

## F06 — Forging KRUSH, rules 1193–1197

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1193** | `PROTECTED → EXECUTING` | `(goal gl-strategy KRUSH)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item FORGING)`; `(can-research-with-escrow ri-forging)` | `(up-research gl-escrow-state c: ri-forging)` | **DIRECT** | No command acceptance/completion proof. |
| **1194** | `VERIFYING → RECOVERY` | `(goal gl-strategy KRUSH)`; `(up-research-status c: ri-forging < research-pending)`; `(up-compare-goal gl-build-progress > KrushForgingNumber)` | `(set-goal gl-build-progress KrushForgingNumber)` | **DIRECT** | No runtime proof rewind was required/safe. |
| **1195** | `RECOVERY → RESERVING` | `(goal gl-strategy KRUSH)`; `(up-compare-goal gl-current-build-item != FORGING)`; `(up-compare-goal gl-build-progress == KrushForgingNumber)` | `(set-goal gl-current-build-item FORGING)` | **DIRECT** | No proof current item remained valid. |
| **1196** | `RESERVING → PROTECTED` | `(goal gl-strategy KRUSH)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == FORGING)` | `(set-escrow-percentage food LOW-ESCROW)`; `(set-escrow-percentage wood 0)`; `(set-escrow-percentage gold 0)`; `(release-escrow wood)`; `(release-escrow gold)` | **DIRECT** | No proof LOW reserve established or releases completed. |
| **1197** | `VERIFYING → REASSESS` | `(goal gl-strategy KRUSH)`; `(goal gl-current-build-item FORGING)`; `(up-research-status c: ri-forging >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | No completion-grade proof; no duplicate-increment proof. |

## F07 — Chain Barding KRUSH, rules 1198–1202

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1198** | `PROTECTED → EXECUTING` | `(goal gl-strategy KRUSH)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item CHAINBARDING)`; `(can-research-with-escrow ri-chain-barding)` | `(up-research gl-escrow-state c: ri-chain-barding)` | **DIRECT** | No proof command accepted/completed. |
| **1199** | `VERIFYING → RECOVERY` | `(goal gl-strategy KRUSH)`; `(up-research-status c: ri-chain-barding < research-pending)`; `(up-compare-goal gl-build-progress > KrushChainBardingNumber)` | `(set-goal gl-build-progress KrushChainBardingNumber)` | **DIRECT** | No runtime proof correction was needed/safe. |
| **1200** | `RECOVERY → RESERVING` | `(goal gl-strategy KRUSH)`; `(up-compare-goal gl-current-build-item != CHAINBARDING)`; `(up-compare-goal gl-build-progress == KrushChainBardingNumber)` | `(set-goal gl-current-build-item CHAINBARDING)` | **DIRECT** | No proof current-item restore was correct. |
| **1201** | `RESERVING → PROTECTED` | `(goal gl-strategy KRUSH)`; `(current-age-time >= 460)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == CHAINBARDING)` | `(set-escrow-percentage food LOW-ESCROW)`; `(set-escrow-percentage gold LOW-ESCROW)`; `(set-escrow-percentage wood 0)`; `(release-escrow wood)` | **DIRECT** | No proof age-time guard remained valid through execution; no proof escrow established. |
| **1202** | `VERIFYING → REASSESS` | `(goal gl-strategy KRUSH)`; `(goal gl-current-build-item CHAINBARDING)`; `(up-research-status c: ri-chain-barding >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | Pending threshold is not completion; no runtime proof. |

## F08 — Chain Barding FLUSH, rules 1203–1207

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1203** | `PROTECTED → EXECUTING` | `(goal gl-strategy FLUSH)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item CHAINBARDING)`; `(can-research-with-escrow ri-chain-barding)` | `(up-research gl-escrow-state c: ri-chain-barding)` | **DIRECT** | No proof command accepted/completed. |
| **1204** | `VERIFYING → RECOVERY` | `(goal gl-strategy FLUSH)`; `(up-research-status c: ri-chain-barding < research-pending)`; `(up-compare-goal gl-build-progress > ChainBardingNumber)` | `(set-goal gl-build-progress ChainBardingNumber)` | **DIRECT** | No runtime proof rewind was needed/safe. |
| **1205** | `RECOVERY → RESERVING` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-current-build-item != CHAINBARDING)`; `(up-compare-goal gl-build-progress == ChainBardingNumber)` | `(set-goal gl-current-build-item CHAINBARDING)` | **DIRECT** | No runtime proof. |
| **1206** | `RESERVING → PROTECTED` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == CHAINBARDING)` | `(set-escrow-percentage food MID-HIGH-ESCROW)`; `(set-escrow-percentage gold MID-HIGH-ESCROW)`; `(set-escrow-percentage wood 0)`; `(release-escrow wood)` | **DIRECT** | No proof reserve established or wood release completed. |
| **1207** | `VERIFYING → REASSESS` | `(goal gl-strategy FLUSH)`; `(goal gl-current-build-item CHAINBARDING)`; `(up-research-status c: ri-chain-barding >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | No completion-grade proof. |

## F09 — Scale Barding KRUSH, rules 1208–1212

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1208** | `PROTECTED → EXECUTING` | `(goal gl-strategy KRUSH)`; `(current-age-time >= 180)`; `(current-age == castle-age)`; `(goal gl-progression-pause -1)`; `(goal gl-current-build-item SCALEBARDING)`; `(can-research-with-escrow ri-scale-barding)` | `(up-research gl-escrow-state c: ri-scale-barding)` | **DIRECT** | No proof command accepted/completed. |
| **1209** | `VERIFYING → RECOVERY` | `(goal gl-strategy KRUSH)`; `(up-research-status c: ri-scale-barding < research-pending)`; `(up-compare-goal gl-build-progress > KrushScaleBardingNumber)` | `(set-goal gl-build-progress KrushScaleBardingNumber)` | **DIRECT** | No runtime proof rewind was required/safe. |
| **1210** | `RECOVERY → RESERVING` | `(goal gl-strategy KRUSH)`; `(up-compare-goal gl-current-build-item != SCALEBARDING)`; `(up-compare-goal gl-build-progress == KrushScaleBardingNumber)` | `(set-goal gl-current-build-item SCALEBARDING)` | **DIRECT** | No proof restored item remained valid. |
| **1211** | `RESERVING → PROTECTED` | `(goal gl-strategy KRUSH)`; `(current-age-time >= 180)`; `(current-age == castle-age)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == SCALEBARDING)` | `(set-escrow-percentage food LOW-ESCROW)`; `(set-escrow-percentage gold 0)`; `(set-escrow-percentage wood 0)`; `(release-escrow gold)`; `(release-escrow wood)` | **DIRECT** | No proof food protection established or releases completed. |
| **1212** | `VERIFYING → REASSESS` | `(goal gl-strategy KRUSH)`; `(goal gl-current-build-item SCALEBARDING)`; `(up-research-status c: ri-scale-barding >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | No completion-grade proof. |

## F10 — Fletching, rules 1236–1240

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1236** | `PROTECTED → EXECUTING` legacy path | `(goal gl-progression-pause -1)`; `(goal gl-current-build-item FLTCH)`; `(can-research-with-escrow ri-fletching)` | `(set-escrow-percentage food 0)`; `(set-escrow-percentage gold 0)`; `(chat-to-player me "Fletching")`; `(release-escrow food)`; `(release-escrow gold)`; `(research ri-fletching)` | **DIRECT** command/release pattern; **INFERRED** Byzantine execution-state semantics | No proof legacy `research` command accepted/completed; no proof release completed. |
| **1237** | `VERIFYING → RECOVERY` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-build-progress > 9)`; `(up-research-status c: ri-fletching < research-pending)` | `(set-goal gl-build-progress 9)` | **DIRECT** | No runtime proof correction was needed. |
| **1238** | `RECOVERY → RESERVING` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-build-progress == 9)`; `(up-compare-goal gl-current-build-item != FLTCH)` | `(set-goal gl-current-build-item FLTCH)` | **DIRECT** | No proof restored item remained valid. |
| **1239** | `RESERVING → PROTECTED` | `(goal gl-strategy FLUSH)`; `(building-type-count blacksmith >= 1)`; `(up-compare-goal gl-current-build-item == FLTCH)` | `(up-modify-escrow food c:max 100)`; `(up-modify-escrow gold c:max 50)` | **DIRECT** mutation; **INFERRED** protection | No proof physical escrow reached intended amounts. |
| **1240** | `VERIFYING → REASSESS` | `(goal gl-current-build-item FLTCH)`; `(up-research-status c: ri-fletching >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | Pending is not completion; no runtime proof. |

## F11 — Leather Archer Armor, rules 1241–1245

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1241** | `PROTECTED → EXECUTING` | `(goal gl-progression-pause -1)`; `(goal gl-current-build-item LAA)`; `(can-research-with-escrow ri-leather-archer-armor)` | `(up-research gl-escrow-state c: ri-leather-archer-armor)` | **DIRECT** | No command acceptance/completion proof. |
| **1242** | `VERIFYING → RECOVERY` | `(goal gl-strategy FLUSH)`; `(up-research-status c: ri-leather-archer-armor < research-pending)`; `(up-compare-goal gl-build-progress > LeatherArcherArmorNumber)` | `(set-goal gl-build-progress LeatherArcherArmorNumber)` | **DIRECT** | No runtime proof rewind needed/safe. |
| **1243** | `RECOVERY → RESERVING` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-current-build-item != LAA)`; `(up-compare-goal gl-build-progress == LeatherArcherArmorNumber)` | `(set-goal gl-current-build-item LAA)` | **DIRECT** | No proof current-item restoration remained valid. |
| **1244** | `RESERVING → PROTECTED` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-progression-pause == -1)`; `(up-compare-goal gl-current-build-item == LAA)` | `(set-escrow-percentage food MID-HIGH-ESCROW)`; `(set-escrow-percentage gold MID-HIGH-ESCROW)`; `(set-escrow-percentage wood 0)`; `(release-escrow wood)` | **DIRECT** | No proof reserve established or wood release completed. |
| **1245** | `VERIFYING → REASSESS` | `(goal gl-current-build-item LAA)`; `(up-research-status c: ri-leather-archer-armor >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | Pending is not completion; no runtime proof. |

## F12 — Padded Archer Armor, rules 1246–1250

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1246** | `PROTECTED → EXECUTING` legacy path | `(goal gl-progression-pause -1)`; `(goal gl-current-build-item PAA)`; `(can-research-with-escrow ri-padded-archer-armor)` | `(set-escrow-percentage food 0)`; `(release-escrow food)`; `(research ri-padded-archer-armor)` | **DIRECT** command/release; **INFERRED** state semantics | No proof command accepted/completed or release completed. |
| **1247** | `VERIFYING → RECOVERY` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-build-progress > PaddedArcherArmorNumber)`; `(up-research-status c: ri-padded-archer-armor < research-pending)` | `(set-goal gl-build-progress PaddedArcherArmorNumber)` | **DIRECT** | No runtime proof rewind was needed/safe. |
| **1248** | `RECOVERY → RESERVING` | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-current-build-item != PAA)`; `(up-compare-goal gl-build-progress == PaddedArcherArmorNumber)` | `(set-goal gl-current-build-item PAA)` | **DIRECT** | No proof current item remained valid. |
| **1249** | `RESERVING → PROTECTED` | `(goal gl-current-build-item PAA)`; `(up-research-status c: ri-fletching >= research-complete)` | `(up-modify-escrow food c:max 100)`; `(set-escrow-percentage wood 0)`; `(set-escrow-percentage gold 0)`; `(release-escrow wood)`; `(release-escrow gold)` | **DIRECT** mutation; **INFERRED** protection | No proof Fletching completion was live/valid; no proof escrow established. |
| **1250** | `VERIFYING → REASSESS` | `(goal gl-current-build-item PAA)`; `(up-research-status c: ri-padded-archer-armor >= research-pending)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** | Pending is not completion; no runtime proof. |

---

# 4. Construction escrow/control transitions

These rules are not part of the twelve research reservation families, but they are essential because the Byzantine state machine also uses escrow to protect construction transactions.

## Farm path — rules 1794–1800

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1794** | bypass / preemption guard before construction | `(or (goal gl-current-build-item MARKET1) (or (up-pending-placement c: blacksmith) (up-compare-goal gl-strategy != FLUSH)))` | `(up-jump-rule 1)` | **DIRECT** control-flow evidence; **INFERRED** as arbitration | No proof jump target/next rule produced intended priority behavior at runtime. |
| **1795** | `IDLE → RESERVING` construction requirement | `(idle-farm-count < 2)`; `(current-age >= feudal-age)`; `(up-compare-goal MILL != YES)`; `(up-pending-objects c: farm < 3)`; `(building-type-count-total farm < 50)`; `(building-type-count-total archery-range >= 2)`; `(or (wood-amount >= 120) (and (wood-amount >= 80) (building-type-count-total farm < 10)))` | `(set-goal SPLIT 1)` | **COMPOSED** | No runtime proof farm requirement was admitted or that another construction requirement did not win. |
| **1796** | reservation/feasibility staging | `(goal SPLIT 1)`; `(or (building-type-count-total blacksmith >= 1) (or (and (up-compare-goal rt >= 2) (building-type-count-total farm < 7)) (and (up-compare-goal rt < 2) (building-type-count-total farm < 10))))` | `(set-goal SPLIT 2)` | **DIRECT** staging; **COMPOSED** transition | No runtime proof SPLIT state was unique or persisted. |
| **1797** | `PROTECTED → EXECUTING` | `(goal SPLIT 2)`; `(or (nand (current-age == castle-age) (up-compare-goal gl-current-build-item == ESKIRMS)) (up-research-status c: ri-elite-skirmisher >= research-pending))` | `(up-build place-normal gl-escrow-state c: farm)` | **DIRECT** command | No proof farm build was accepted/placed; no proof escrow state actually protected farm resources. |
| **1798** | engine escrow mode reset / latch clear | `(true)` | `(set-goal gl-escrow-state with-escrow)`; `(set-goal SPLIT 0)` | **DIRECT** | No proof global accounting mode was safe to reset at this point; no proof another transaction was not using it. |
| **1799** | alternate construction admission | `(can-build farm)`; `(wood-amount >= 90)`; `(idle-farm-count < 2)`; `(up-compare-goal MILL != YES)`; `(up-pending-objects c: farm < 2)`; `(building-type-count-total farm < 50)` | `(set-goal SPLIT 1)` | **DIRECT** | No proof this branch did not race with 1795. |
| **1800** | non-escrow legacy execution path | `(goal SPLIT 1)`; `(or (current-age >= castle-age) (and (goal gl-strategy KRUSH) (up-research-status c: ri-horse-collar >= research-complete)))`; `(or (wood-amount >= 260) (up-compare-goal gl-current-build-item != EXTRA-STABLES))` | `(build farm)` | **DIRECT** command; **INFERRED** transaction semantics | No proof build accepted/placed; this is not equivalent to `up-build ... gl-escrow-state`. |

## Gold Mining Camp / Stone Mining Camp — rules 1890–1896

| Rule | Transition role | Exact predicates | Exact actions | Evidence | Missing runtime proof |
|---|---|---|---|---|---|
| **1890** | disabled historical execution anchor | `(false)`; `(goal gl-progression-pause -1)`; `(can-build-with-escrow mining-camp)`; `(goal gl-current-build-item GOLDMC2)`; `(up-set-target-object search-remote c: 0)` | `(up-get-point position-object point-x)`; `(up-set-target-point point-x)`; `(chat-to-player me "Second Gold Mining Camp")`; `(set-strategic-number sn-placement-zone-size 15)`; `(set-strategic-number sn-placement-fail-delta 2)`; `(set-strategic-number sn-allow-adjacent-dropsites 0)`; `(set-strategic-number sn-dropsite-separation-distance 25)`; `(release-escrow wood)`; `(up-build place-point 0 c: mining-camp)` | **DIRECT** source evidence, but **not active** because `(false)` | No runtime firing proof is possible from this rule as written; it is a disabled source anchor. |
| **1891** | `VERIFYING → RECOVERY` / progression rewind | `(goal gl-strategy FLUSH)`; `(building-type-count-total mining-camp < 3)`; `(up-compare-goal gl-build-progress > GoldMC2Number)` | `(set-goal gl-build-progress GoldMC2Number)` | **DIRECT** reconciliation; **COMPOSED** recovery | No proof building count represented a failed transaction rather than pending construction; no runtime proof rewind was safe. |
| **1892** | `RECOVERY → RESERVING` / restore active item + policy | `(goal gl-strategy FLUSH)`; `(up-compare-goal gl-current-build-item != GOLDMC2)`; `(up-compare-goal gl-build-progress == GoldMC2Number)` | `(set-goal gl-current-build-item GOLDMC2)`; `(set-escrow-percentage wood LOW-ESCROW)` | **DIRECT** | No proof LOW escrow established; no proof restored item was valid. |
| **1893** | `VERIFYING → REASSESS` | `(goal gl-current-build-item GOLDMC2)`; `(building-type-count-total mining-camp >= 3)` | `(up-modify-goal gl-build-progress c:+ 1)` | **DIRECT** world-state observer | No proof a new build-progress value could not be incremented repeatedly; no explicit escrow-release evidence here. |
| **1894** | `PROTECTED → EXECUTING` target-search preparation | `(goal gl-fifth-turn 1)`; `(goal gl-progression-pause -1)`; `(can-build-with-escrow mining-camp)`; `(goal gl-current-build-item STONEMC1)` | `(set-strategic-number sn-focus-player-number 0)`; `(up-full-reset-search)`; `(up-set-target-point home-x)`; `(up-filter-distance c: -1 c: 30)`; `(up-find-remote c: stone-mine c: 40)`; `(up-modify-sn sn-focus-player-number s:= sn-target-player-number)`; `(up-clean-search search-remote object-data-distance search-order-asc)`; `(up-remove-objects search-remote -1 > 0)` | **DIRECT** search/feasibility path; **COMPOSED** execution transition | No proof search returned a valid target; no proof target remained valid until placement. |
| **1895** | `PROTECTED → EXECUTING` placement + release | `(goal gl-fifth-turn 1)`; `(goal gl-progression-pause -1)`; `(can-build-with-escrow mining-camp)`; `(goal gl-current-build-item STONEMC1)`; `(up-set-target-object search-remote c: 0)` | `(up-get-point position-object point-x)`; `(up-set-target-point point-x)`; `(set-strategic-number sn-placement-zone-size 5)`; `(set-strategic-number sn-placement-fail-delta 10)`; `(set-strategic-number sn-allow-adjacent-dropsites 0)`; `(set-strategic-number sn-dropsite-separation-distance 10)`; `(release-escrow wood)`; `(set-escrow-percentage wood 0)`; `(up-build place-point 0 c: mining-camp)` | **DIRECT** | No proof target was valid; no proof wood release reached zero; no proof building was placed; no proof release-before-build ordering produced intended accounting behavior. |
| **1896** | `VERIFYING → RECOVERY` / cursor correction | `(goal gl-strategy FLUSH)`; `(dropsite-min-distance stone >= 5)`; `(up-compare-goal gl-build-progress > StoneMC1Number)` | `(set-goal gl-build-progress StoneMC1Number)` | **DIRECT** reconciliation | No runtime proof this condition means the intended Stone MC was skipped or invalid; no proof rewind was safe. |

---

# 5. Transition-level proof ledger

| Byzantine transition | Shadow rule evidence | Classification | Exact missing proof |
|---|---|---|---|
| `IDLE → RESERVING` | Trigger writers such as 1172, 1175 and construction admission 1795/1799 | **COMPOSED** | Live trigger firing, authority ownership, exclusivity, valid cost vector, no stale objective. |
| `RESERVING → PROTECTED` | Physical writers 1173, 1176, 1181, 1186, 1191, 1196, 1201, 1206, 1211, 1239, 1244, 1249, 1892 | **DIRECT + INFERRED** | Actual escrow amount/percentage after mutation, persistence, ownership, no competing writer, economic-floor preservation. |
| `PROTECTED → EXECUTING` | 1174, 1177, 1178, 1183, 1188, 1193, 1198, 1203, 1208, 1241, 1246, 1797, 1894–95 | **DIRECT / COMPOSED** | Command acceptance, target validity, executor availability, no supersession, actual engine action. |
| `EXECUTING → VERIFYING` | Command rules plus downstream status/build-count observers | **COMPOSED** | Proof observer was armed, command actually issued, expected state delta defined. |
| `VERIFYING → RELEASE` | 1174/1177 release sequences and later reconciliation rules | **COMPOSED** | Completion-grade world state, physical escrow reconciliation, logical commitment closure. |
| `VERIFYING → TIMEOUT` | Shadow temporal/progression guards | **BYZANTINE-GENERALIZATION** | Measured deadline, absent progress, no alternate completion, commitment still active. |
| `VERIFYING → RECOVERY` | 1179, 1184, 1189, 1194, 1199, 1204, 1209, 1237, 1242, 1247, 1891, 1896 | **COMPOSED** | Contradiction must be real; recovery action must not destroy a still-valid transaction. |
| `RELEASE → IDLE` | Resource zero/release actions | **DIRECT physical / BYZANTINE-GENERALIZATION logical** | Actual escrow zero/released, cursor cleared, commitment closed, no stale pending state. |
| `TIMEOUT → RECOVERY` | No literal Shadow timeout state | **BYZANTINE-GENERALIZATION** | Timeout record + last-known-good state + protected resources + retry/substitute/cancel decision. |
| `RECOVERY → RESERVING` | Cursor restoration/re-entry families | **COMPOSED + BYZANTINE-GENERALIZATION** | Old attempt reconciled, new attempt identity, new arbitration, fresh reservation. |
| `PROTECTED → RECOVERY` | Shared escrow namespace + competing writers + reconciliation | **INFERRED + BYZANTINE-GENERALIZATION** | Authorized supersession and safe unwinding. |
| `EXECUTING → RECOVERY` | Reconciliation after contradictory world state | **INFERRED + BYZANTINE-GENERALIZATION** | Demonstrated failed/invalid execution and unsafe blind retry. |
| `RESERVING → RECOVERY` | No literal equivalent | **BYZANTINE-GENERALIZATION** | Partial reservation contradiction and safe unwind. |
| `RECOVERY → IDLE` | Release/reconciliation substrate | **BYZANTINE-GENERALIZATION** | Complete physical and logical cleanup. |

---

# 6. Runtime proof requirements by evidence class

## DIRECT source evidence still requires runtime qualification

A DIRECT classification means only that the source body proves the stated static relationship. It does **not** prove firing, ordering under the live engine, command acceptance, or world-state effect.

For a DIRECT reservation rule, runtime instrumentation must establish:

```text
predicate true
→ rule fires
→ escrow mutation occurs
→ observed escrow state matches requested policy
```

For a DIRECT command rule:

```text
predicate true
→ command fires once
→ engine accepts command
→ expected pending/active state appears
→ completion observer eventually sees expected world state
```

For a DIRECT completion observer:

```text
world-state predicate true
→ observer fires
→ progression changes exactly once
→ subsequent rule path is the intended path
```

## COMPOSED transitions

Every constituent rule must be runtime-qualified **as a chain**, not individually. Static existence of A, B and C does not establish A→B→C at runtime.

## INFERRED transitions

These require a runtime test specifically designed to falsify the inferred semantic interpretation. In particular:

- `PROTECTED` must be tested against actual escrow state.
- `VERIFYING` must distinguish command issuance from world-state completion.
- recovery must demonstrate that cursor correction restores rather than corrupts progression.

## BYZANTINE-GENERALIZATION transitions

These require a Byzantine-specific acceptance test because Shadow cannot prove them. They should not be labeled “Shadow behavior” merely because Shadow contains compatible primitives.

---

# 7. Critical findings

### 7.1 Shadow has a real reservation/execution/reconciliation pattern

Across Scale Mail, Chain Mail, Iron Casting, Forging, Chain Barding, Scale Barding, Fletching, Leather Archer Armor and Padded Archer Armor, the repeated structure is:

```text
requirement
→ progression/cursor state
→ escrow mutation
→ feasibility gate
→ engine command
→ observed status
→ progression reconciliation
→ later resource policy/release
```

That repetition is **COMPOSED evidence for a reusable economic-control idiom**. It is not evidence for a literal eight-state Shadow FSM.

### 7.2 `research-pending` is a hard verification boundary

Many completion observers use `up-research-status ... >= research-pending`. That is exactly what Shadow uses to advance its progression cursor, but it must not be silently relabeled “completed” in the Byzantine state machine. Runtime qualification must determine what the engine reports at that threshold and whether a stronger completion predicate is required.

### 7.3 Legacy research paths must remain separate

Fletching (1236) and Padded Archer Armor (1246) use `research`, not the newer `up-research gl-escrow-state` pattern. They are therefore valid evidence for reservation/release behavior but **not** interchangeable execution templates.

### 7.4 Construction proves the same architecture outside research

Rules 1892–1895 show the same economic-control shape around construction: cursor restoration, escrow policy, `can-build-with-escrow`, target resolution, resource release and engine-facing placement. Rules 1891/1893/1896 provide the world-state/progression reconciliation layer.

### 7.5 `gl-escrow-state` must remain an engine-interface variable

Nothing in these rules proves that `gl-escrow-state` is a logical commitment owner. The Byzantine machine must therefore keep logical commitment identity separate from the engine accounting-mode selector.

### 7.6 The missing runtime proof is not one test

The minimum qualification campaign needs separate tests for:

1. reservation establishment;
2. reservation persistence under competing resource writers;
3. escrow-aware command acceptance;
4. command-to-pending transition;
5. command-to-completion transition;
6. release reconciliation;
7. progression cursor correction;
8. jump/preemption interaction;
9. duplicate-firing prevention;
10. timeout/recovery behavior;
11. supersession of a protected commitment;
12. re-entry after successful release.

---

# 8. Final evidence boundary

The recovered Shadow rules justify the following statement:

> Shadow contains repeated, source-level economic-control chains in which strategic/progression state gates physical escrow manipulation, escrow-aware or legacy execution, observed status/progression reconciliation, and resource release/rebalancing.

They do **not** by themselves justify the stronger statement:

> Shadow implements the Byzantine eight-state escrow machine.

The latter is our reconstruction. The correct engineering posture is therefore:

```text
SHADOW RULE
    ↓
STATIC RELATION
    ↓
COMPOSED CONTROL CHAIN
    ↓
RUNTIME OBSERVATION
    ↓
QUALIFIED SHADOW SUBSTRATE
    ↓
BYZANTINE STATE SEMANTICS
    ↓
BYZANTINE RUNTIME QUALIFICATION
```

Until the missing runtime evidence exists, `PROTECTED`, `VERIFYING`, `TIMEOUT`, and explicit transaction recovery remain **architectural hypotheses/generalizations**, while the underlying Shadow predicates/actions remain directly recoverable source evidence.
