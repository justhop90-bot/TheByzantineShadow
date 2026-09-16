# ShadowSource Military–Production Boundary Atlas v0.1

**Audit revision:** 2026-09-16  
**Canonical source:** `ShadowSource.per`  
**Canonical source SHA-1:** `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`  
**Purpose:** compact forensic map of the Military–Production interface. This document is an audit/correction of v0.1, not a new architecture proposal.

## 0. Audit status

The previous atlas was directionally correct but overstated several points. This revision is the authoritative correction.

- Military–Production is a **shared-state/control-flow interface**, not an API boundary.
- `QUNITS` and `QBUILDINGS` are a **contiguous unit/building production closure**, but **not the entirety of Shadow's production/progression machinery**.
- `up-jump-rule` is **positional control flow**, not a priority declaration and not a call/return operation.
- Connector-generated rule IDs are **not canonical source labels**. Canonical rule identity is source-order position + physical source range + predicate/action signature.
- Command issuance is not completion.
- Research-pending/progression state is not equivalent to research completion.
- Runtime firing remains unqualified by this static audit.

## 1. Canonical production closure

The principal contiguous production block is:

```text
QUNITS       L15201–L15683
QBUILDINGS   L15684–L16477
```

The source-order transition is:

```text
QUNITS
  QMONKS
  QMANGOS
  QSCORPS
  QRAMS
  QSCOUTS
  QKNIGHTS
  QARCHERS
  QSKIRMS
  QMILITIAMAN
  QSPEARS
      |
      | normal successor / positional jumps
      v
QBUILDINGS
  QTOWERS
  QSTABLE
  QMONASTERY
  QMARKET
      |
      v
QANALYZING ENEMY ATTACK
```

These ranges are the **contiguous production closure**, not a claim that all production authority lives here. Research, economy, progression, escrow policy, construction, and military state also participate in production decisions elsewhere in the source.

## 2. Positional jump semantics

For this audit, `up-jump-rule Δ` is represented as:

```text
current rule
   |
   | Δ
   v
rule pointer = current + 1 + Δ
```

Thus a positive jump skips `Δ` subsequent rules and resumes at the next rule. A negative jump can re-enter an earlier rule and form a loop. There is **no return stack**.

Jump destinations below are therefore **source-order destinations**, not "return paths".

## 3. QUNITS jump closure

| Source region | Jump | Skipped rules | Destination |
|---|---:|---|---|
| QMANGOS anti-knight/eagle bypass | `+1` | one SIEGE-3 emergency Mangonel rule | following SIEGE-1 Mangonel escalation rule |
| QARCHERS resource bypass | `+1` | GeneralArcher production rule | first QSKIRMS rule |
| QSKIRMS fewer-if-ahead | `+2` | fewer-if-enemy-castled; ALL | SPLIT-1 stage |
| QSKIRMS fewer-if-enemy-castled | `+1` | ALL | SPLIT-1 stage |
| QSPEARS KRUSH bypass | `+4` | MESO bypass; EmergencySpear; Spear2; Spear3 | first QTOWERS rule |
| QSPEARS MESO bypass | `+2` | EmergencySpear; Spear2 | Spear3 |

### Critical cross-region edge

```text
QSPEARS / KRUSH bypass
    +4
    ├─ skip MESO bypass
    ├─ skip EmergencySpear
    ├─ skip Spear2
    ├─ skip Spear3
    └──────────────► QTOWERS / first rule
```

This is a **direct positional QUNITS → QBUILDINGS edge**. It must not be rewritten as a generic `return-to-buildings` abstraction.

### QSKIRMS arbitration

The two Skirmisher jumps bypass deliberation stages and land on the SPLIT-1 stage. They do not directly execute a training command. This is source-order preemption, not an abstract scheduler priority.

## 4. QBUILDINGS jump closure

| Source region | Jump | Skipped rules | Destination |
|---|---:|---|---|
| QTOWERS entry | `+6` | builder=1; unsafe-town builder=5; tower-control -1; tower-control 0; tower-control 1; tower-control 2 | tower-control 3 placement rule |
| QMARKET OTHER | `+9` | nine intervening Market trigger/setup/arbitration rules | Market `can-build-with-escrow` execution rule |

### QTOWERS

```text
QTOWERS entry
   +6
   ├─ builder setup
   ├─ unsafe-town builder override
   ├─ tower-control -1
   ├─ tower-control 0
   ├─ tower-control 1
   ├─ tower-control 2
   └──────────────► tower-control 3
```

The destination issues the Tower placement command and advances the tower-control cycle. The `up-build` command is **not** itself evidence that a Tower exists.

### QMARKET

```text
QMARKET OTHER
   +9
   ├─ resource trigger
   ├─ SPLIT stage
   ├─ progression-pause setup
   ├─ Feudal/Cup trigger
   ├─ failsafe
   ├─ escrow mutation
   ├─ generic goal setup
   ├─ KRUSH modifier
   ├─ town-safety modifier
   └──────────────► can-build-with-escrow MARKET
```

The destination is the Market execution rule. Static analysis establishes the positional edge; it does not establish runtime firing frequency.

## 5. Production completion semantics

Shadow distinguishes at least four relevant observations:

### Unit/world-state completion

Observed unit/group counts such as `unit-type-count-total` and group-size state establish that produced military capability exists in the world.

### Building/world-state completion

`building-type-count-total` establishes actual building presence. Shadow then uses that observation to reconcile `gl-build-progress`.

### Research completion

`research-completed` is a true completion predicate and can directly mutate Military capability state. Fletching, Bodkin Arrow, and Elite Skirmisher are explicit examples.

### Progression state

`gl-build-progress`, `gl-current-build-item`, and `gl-progression-pause` are Shadow's logical control state. They are not engine completion signals. Rules exist that roll progression back when the observed world state does not support the logical cursor.

Therefore:

```text
command issued       != completed
pending              != completed
progression advanced != completed
escrow released      != completed
```

## 6. Escrow finding

Escrow is embedded in production/progression control rather than owned by one central transaction module.

Confirmed production-side operations include:

- `up-modify-escrow`
- `set-escrow-percentage`
- `release-escrow`
- `can-train-with-escrow`
- `can-build-with-escrow`
- `up-train gl-escrow-state ...`
- `up-build ... gl-escrow-state ...`

The machine commonly follows:

```text
trigger
→ progression/current-item mutation
→ resource protection
→ feasibility gate
→ engine command
→ world-state observation
→ progression reconciliation
→ release/rebalancing
→ re-entry
```

This is a **forensic control pattern**, not a claim that Shadow contains a named transaction FSM.

## 7. Military ↔ Production interface

The interface is bidirectional and observation-driven.

```text
MILITARY
  enemy composition / group state / tactical evaluation
             |
             v
     persistent Shadow state
             |
             v
PRODUCTION / TECHNOLOGY
  unit / building / research actions
             |
             v
     actual world state
             |
             v
MILITARY
  group size / capability / range / damage evaluation
             |
             +──────────────► re-evaluation
```

### Production → Military

Hard evidence includes:

- completed Fletching/Bodkin/Elite Skirmisher changing tactical range/tracking state;
- produced unit/group counts contributing to military capability evaluation;
- enemy/own composition observations being consumed by tactical scoring.

### Military → Production

The production closure directly reads military-relevant observations such as enemy Stable/Knight/Camel presence for Spear decisions and enemy composition for other unit branches. The exact outer writer matrix is broader than this document and must not be invented from the boundary alone.

## 8. Military control-flow correction

The military region has a richer jump topology than QUNITS/QBUILDINGS. Confirmed examples include:

```text
QADVANTAGE
   +44
   → bypass detailed ranged evaluation

enemy-player search
   -2 / related negative offsets
   → increment focus player
   → re-enter search
```

These are control-flow edges. They are not priority labels and do not imply procedure calls.

## 9. Evidence grades

| Claim | Grade |
|---|---|
| QUNITS L15201–L15683 | DIRECT / STATIC |
| QBUILDINGS L15684–L16477 | DIRECT / STATIC |
| QSPEARS `+4` crosses into QTOWERS | DIRECT / STATIC |
| QTOWERS `+6` destination | DIRECT / STATIC |
| QMARKET `+9` execution destination | DIRECT / STATIC |
| Unit/building count as world-state observation | DIRECT / STATIC |
| `research-completed` → Military capability mutation | DIRECT / STATIC |
| Military ↔ Production bidirectional coupling | COMPOSED from direct edges |
| Semantic meaning of a jump beyond its positional effect | INFERRED unless directly established by surrounding predicates |
| Runtime firing / completion | UNQUALIFIED by this static atlas |

## 10. Reconstruction rule

Do **not** turn this closure into:

```text
Military API → Production API → trainer
```

and do not manufacture a centralized `RECOVERY` or `ESCROW` subsystem because the analysis is easier that way.

Preserve the donor's actual machinery:

```text
source order
+ positional jumps
+ persistent goals
+ strategic numbers
+ timers
+ escrow mutations
+ engine commands
+ world-state observations
+ progression reconciliation
+ re-entry
```

The useful reconstruction unit is the **coherent control closure**, while the analytical labels remain just that: labels.

## 11. Audit conclusion

The previous atlas is corrected here without expanding the paperwork footprint. The durable finding is simple:

> **Shadow's Military–Production interface is a persistent sequential control machine whose production closure is coupled to Military through shared state, positional control flow, escrow, actual-world observations, and capability feedback.**

That is the donor behavior worth transplanting. The individual `train`/`build` commands are the easy part. The annoying source-order machinery is the part that actually matters.
