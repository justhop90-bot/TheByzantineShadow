# Shadow Escrow Progression Control Graph v0.1

## Authentication

Canonical donor: `ShadowSource.per`

Authenticated blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`

## Control-machine result

Shadow does not implement escrow as a centralized reserve manager. Escrow is distributed through the progression machine. The principal state variables are:

- `gl-strategy` — KRUSH / FLUSH / SIEGE strategy context.
- `gl-build-progress` — ordered progression cursor.
- `gl-current-build-item` — current objective represented by a symbolic build/research item.
- `gl-progression-pause` — interrupt/hold state for special research/build objectives.
- `SPLIT` — transient arbitration/preemption latch.
- `gl-escrow-state` — execution mode passed to escrow-aware build/train/research commands.

The recurring path is:

```text
strategy + build-progress
        |
        v
current-build-item
        |
        +--> escrow policy mutation
        |       set-escrow-percentage
        |       up-modify-escrow
        |       release-escrow
        |
        +--> executor
        |       up-build / up-research / up-train
        |
        +--> observed completion
                building/research status
                |
                v
        gl-build-progress += 1
                |
                v
        next current-build-item
```

`SPLIT` is not the persistent state machine. It is a transient arbitration latch that selects a special action, mutates `gl-progression-pause` or executes a search/training action, then is normally reset to `0`.

## 1. Progression state establishment

For both KRUSH and FLUSH, progression is driven by a repeated three-stage pattern:

```text
if build-progress == ItemNumber
    -> set gl-current-build-item ITEM

if current-build-item == ITEM
   and progression-pause == -1
    -> mutate escrow policy
    -> execute research/build/train path

if completion is observed
    -> increment gl-build-progress
```

There are explicit recovery rules for skipped objectives. If the observed building/research state is behind the progression cursor, Shadow resets `gl-build-progress` backward to the required item number. This prevents the cursor from permanently outrunning world state.

Examples in the authenticated source include Stable1/Stable2, Market1, Monastery, Iron Casting, Forging, Chain Barding, Scale Barding, Fletching, Leather Archer Armor, Padded Archer Armor, Bodkin Arrow and Castle Age.

## 2. Stable topology

### FLUSH Stable1

`gl-build-progress == Stable1Number` establishes `STABLE1`.

When `STABLE1` is active and `gl-progression-pause == -1`:

```text
wood = LOW-ESCROW
food = 0
 gold = 0
release gold
release food
```

The stable build command uses `up-build place-control gl-escrow-state c: stable`.

Completion is observed through `building-type-count-total stable >= 1`, then `gl-build-progress += 1`.

### KRUSH Stable2

`KrushStable2Number -> STABLE2 -> LOW-ESCROW wood / release food+gold -> build -> stable count >= 2 -> progress++`.

### FLUSH Stable2

`SecondStableNumber -> STABLE2 -> MID-ESCROW wood / release food+gold -> build -> stable count >= 2 -> progress++`.

If the building count shows the objective was skipped, the `gl-build-progress` cursor is reset to the corresponding Stable number.

## 3. Research topology

The same state machine is used for technologies.

### Iron Casting

KRUSH and FLUSH each have:

```text
progress cursor -> IRONCASTING
progression-pause == -1
    -> escrow policy
    -> up-research gl-escrow-state
research status >= pending
    -> progress++
```

KRUSH escrow:

```text
food LOW-ESCROW
 gold LOW-ESCROW
wood 0 + release
```

FLUSH escrow:

```text
food max 220
 gold max 120
wood 0 + release
```

### Forging

FLUSH: `food MID-ESCROW`, wood/gold zero and released.

KRUSH: `food LOW-ESCROW`, wood/gold zero and released.

Completion is observed through `ri-forging >= research-pending`, then `gl-build-progress += 1`.

### Chain Barding

KRUSH has an age gate (`current-age-time >= 460`) before applying:

```text
food LOW-ESCROW
 gold LOW-ESCROW
wood 0 + release
```

FLUSH applies:

```text
food MID-HIGH-ESCROW
 gold MID-HIGH-ESCROW
wood 0 + release
```

Research completion increments the progression cursor.

### Scale Barding

KRUSH requires Castle Age and `current-age-time >= 180`, then uses food LOW-ESCROW and releases wood/gold.

FLUSH uses food MID-ESCROW and releases wood/gold.

### Fletching

The active execution rule releases food/gold before research. A separate FLUSH rule uses bounded `up-modify-escrow` amounts while the item is active. Completion is observed from research status and advances the cursor.

### Leather Archer Armor

FLUSH sets:

```text
food MID-HIGH-ESCROW
gold MID-HIGH-ESCROW
wood 0 + release
```

Completion advances the cursor.

### Padded Archer Armor

On the prerequisite research state, Shadow applies bounded food escrow and releases wood/gold. Completion of PAA advances the cursor.

### Bodkin

FLUSH applies HIGH-ESCROW to food, wood and gold. Completion is observed through research status and advances the cursor.

## 4. Castle Age / CUP topology

Castle Age is represented as the `CUP` progression item.

For FLUSH, the donor has distinct CUP establishment paths:

- enemy FC: food 95 / gold 95 / wood 0 + release;
- enemy FLUSH: food 65 / gold 65 / wood 0 + release.

The research execution path releases food and gold, sets `gl-age-loading = CA-loading`, enables the economic timer, restores villager production intent, and researches Castle Age.

Completion is observed through Castle Age research status, then `gl-build-progress += 1`.

The donor also contains explicit skipped-state recovery rules that reset the cursor to `CupNumber` / `KrushCupNumber` if Castle Age is not actually pending despite the cursor having advanced.

## 5. Pause/interruption topology

`gl-progression-pause` is a second progression axis, distinct from `gl-build-progress`.

Examples:

```text
SCALEMAIL
    -> up-modify-escrow food max 100
    -> research when escrow-feasible
    -> pause = -1
    -> food escrow zero/released

CHAINMAIL
    -> food max 200 + gold max 100
    -> research when escrow-feasible
    -> pause = -1
    -> food/gold zero/released

PIKES
    -> entered by SPLIT
    -> food HIGH + gold HIGH
    -> research when escrow-feasible
    -> pause = -1
    -> food/gold zero/released
```

Thus a paused research objective can temporarily override normal build progression without destroying the progression cursor.

## 6. SPLIT topology

`SPLIT` is used as a transient preemption latch in multiple subsystems. Within the progression/economic machine, the important case is Pike preemption:

```text
FLUSH + Castle+ + enemy cavalry evidence
    -> SPLIT = 1
    -> food/gold HIGH-ESCROW
    -> gl-progression-pause = PIKES
    -> SPLIT = 0
    -> escrow-aware Pike research
    -> release food/gold
    -> progression resumes
```

`SPLIT` is also used for market admission and emergency training. It should therefore not be treated as an exclusive escrow-state variable.

## 7. Market topology

Market admission is another explicit interrupt path:

```text
market need
    -> gl-progression-pause = MARKET
    -> up-modify-escrow wood max 175
    -> escrow-aware market build
    -> gl-progression-pause = -1
```

A separate `SPLIT=1` rule can request the Market pause. This demonstrates that `SPLIT` is an arbitration trigger while `gl-progression-pause` carries the persistent interrupted objective.

## 8. Economic NET gate

Shadow also uses dynamic NET liquidity in the progression machine. A Market-related rule requires:

```text
wood < 60 OR food < 60 OR gold < 60
AND
NET-WOOD > 600 OR NET-FOOD > 600 OR NET-GOLD > 600
AND
build-progress >= LC3Number
AND
current-build-item != CUP
```

It then sets `SPLIT = 1`.

This is important: NET liquidity is not merely a reporting variable. It participates in progression arbitration.

## 9. Completion and recalculation semantics

Shadow generally does **not** treat the escrow-setting command as completion. The machine observes:

- building counts for construction;
- research status for technology;
- pending/placement state for build admission;
- `can-*-with-escrow` for feasibility before escrow-aware execution.

After observed completion, `gl-build-progress` advances. The next item-selection rule then establishes a new `gl-current-build-item`, and the corresponding escrow rule recalculates policy.

If the world state falls behind the cursor, a recovery rule moves `gl-build-progress` backward to the missing objective. This is the donor's local rollback mechanism.

## 10. Byzantine ABI consequence

Do **not** create a centralized `reserve-manager` abstraction.

The correct recovered interface is distributed:

```text
PROGRESSION CURSOR
    gl-build-progress
        |
        v
CURRENT OBJECTIVE
    gl-current-build-item
        |
        +---------------------+
        |                     |
        v                     v
ESCROW POLICY            EXECUTOR
set/release               build/research/train
        |                     |
        +----------+----------+
                   v
             WORLD OBSERVATION
                   |
                   v
              progress++

INTERRUPT PATH
SPLIT -> gl-progression-pause -> special escrow -> executor -> release -> resume

LIQUIDITY PATH
engine resources - escrow -> NET -> arbitration/SPLIT
```

The existing four-resource reserve inputs remain a Byzantine-specific policy boundary. They must not replace this donor topology.

## Qualification

DIRECT: donor state variables, escrow mutations, progression cursor changes, completion predicates, rollback predicates, pause transitions and SPLIT transitions.

COMPOSED: control graph reconstructed from distributed donor rules.

BYZANTINE-GENERALIZATION: any replacement policy that supplies Byzantine-specific reserve values.

UNKNOWN: exact runtime firing order between every adjacent donor rule without a qualified runtime trace. Static rule order and explicit jumps are preserved as source evidence; runtime completion remains separately unqualified.
