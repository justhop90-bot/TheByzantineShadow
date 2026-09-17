# Shadow Escrow Jump Graph / Adversarial Review v0.1

## Authority

Behavioral authority: `ShadowSource.per`.
Authenticated donor blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`.

This artifact deliberately does not promote the current Byzantine modules into donor evidence.

## Qualification note

The authenticated source is available through the repository connector, but the connector's full-blob response is transport-truncated. Therefore exact donor byte offsets and a complete numeric rule-ordinal table are **not qualified in this pass**. Where source-order/rule-local bodies were recoverable from authenticated source windows, they are recorded below. No fabricated ordinals or offsets are supplied.

## Donor control topology

```text
strategy (KRUSH / FLUSH / SIEGE)
        |
        v
rollback / establish gl-build-progress
        |
        v
establish gl-current-build-item
        |
        +---- if gl-progression-pause != -1 ----> blocked/interrupted
        |
        v
objective-specific escrow mutation
        |
        +---- set-escrow-percentage
        +---- up-modify-escrow
        +---- release-escrow
        |
        v
executor
  build / research / train
        |
        v
world-state observation
  building count / research-completed /
  research-status / unit state
        |
        v
up-modify-goal gl-build-progress c:+ 1
        |
        v
next build item / next progression state
```

`gl-progression-pause` is an actual distributed interruption latch. It is not equivalent to transaction-idle state in the Byzantine demonstrator.

## Rule-local control families recovered

### Establish / repair cursor

Shadow repeatedly uses the pattern:

```text
if actual world state is behind gl-build-progress
    gl-build-progress := prerequisite cursor

if gl-build-progress == ITEM_NUMBER
    gl-current-build-item := ITEM
```

This is explicit recovery of skipped or invalidated progression. It occurs before escrow mutation.

Authenticated source window around the SW sequence demonstrates this directly: a failed/absent second siege workshop condition can reset progress to `33`; the following rule establishes `SW2` as current item.

### Escrow gate

A representative recovered sequence is:

```text
(goal gl-strategy FLUSH)
(gl-progression-pause == -1)
(gl-current-build-item == SW1)
    -> wood MID-ESCROW
    -> food 0
    -> gold 0
    -> release gold
    -> release food
```

The subsequent SW1 executor requires `can-build-with-escrow siege-workshop`, and completion is observed with `building-type-count-total siege-workshop >= 1` before incrementing `gl-build-progress`.

### SW2 interruption / recovery

Recovered source ordering:

```text
pause == -1 && current == SW2 && can-build-with-escrow
    -> wood escrow 0
    -> release wood
    -> placement
    -> build

if FLUSH && progress > 33 && siege-workshop < 2
    -> progress := 33

if FLUSH && progress == 33 && current != SW2
    -> wood LOW-ESCROW
    -> current := SW2

if current == SW2 && siege-workshop >= 2
    -> progress++
```

This is a distributed recovery loop, not a one-shot transaction.

### RAX2 interruption

The recovered source has two enemy-condition rules. One disables itself without setting RAX2; the other sets `gl-progression-pause := RAX2` and disables itself. A following rule applies bounded wood escrow while paused. The executor builds a second barracks and clears the pause immediately after issuing the build command.

That distinction matters: Shadow's pause can be a tactical interruption state, and not every branch that tests the same condition takes the same transition.

## Completion semantics

Shadow increments `gl-build-progress` from observed world state, not from command issuance.

Examples recovered:

- siege workshop: building count >= required count -> progress++
- research: research status/completed -> progress++
- elite skirmisher: research pending/completion state -> progress++

This preserves the donor rule:

```text
command accepted != progression completed
```

## SPLIT / pause topology

`SPLIT` is an arbitration/interruption latch. The emergency pike path sets high escrow, advances `gl-progression-pause` to `PIKES`, performs the research, releases the relevant escrow, and only then permits progression to continue.

The economic NET gate can also establish `SPLIT`. Thus NET liquidity is upstream of escrow mutation in some paths.

## Adversarial comparison: current Byzantine modules

### 1. Centralization

Current Module 10 owns one generic four-resource escrow transaction. Shadow does not have this topology. Shadow mutates only the resources required by the current progression objective and often releases other resource escrow in the same rule family.

**Delta: HIGH.**

### 2. Progress cursor

Current Modules 08-16 use `AEGIS-TRANSACTION-*` state. They do not reproduce Shadow's `gl-build-progress` / `gl-current-build-item` cursor and item-specific rollback topology.

**Delta: HIGH.**

### 3. Pause/interruption

Current transaction lifecycle uses `AEGIS-TRANSACTION` and `AEGIS-RECOVERY-STATE`. Shadow uses distributed `gl-progression-pause`, with tactical pause states such as `RAX2`, `PIKES`, and `MARKET` interleaved with normal progression.

**Delta: HIGH.**

### 4. Escrow policy

Current Module 10 commits one engine-derived transaction vector. Shadow uses percentage policy selected locally by progression objective, including release of competing escrow.

**Delta: HIGH.**

### 5. Completion

Current Module 10 correctly distinguishes escrow command from observed escrow state, but the overall demonstrator remains a single Spearman transaction. Shadow's completion is distributed among each build/research objective and feeds directly into `gl-build-progress`.

**Delta: MEDIUM/HIGH.**

### 6. Recovery / re-entry

Current Module 15 returns a terminal transaction to IDLE. Shadow generally re-enters the progression cursor: rollback -> current item -> escrow -> executor -> observed completion. It does not simply terminate the control episode.

**Delta: HIGH.**

## ABI consequence

No reserve ABI replacement is justified by this graph.

The current four-resource reserve inputs remain a Byzantine adaptation boundary. They must not be used as a claim that Shadow itself owns a centralized reserve vector.

The next donor-faithful ABI requirement is instead a progression-control boundary capable of representing:

- current progression cursor;
- current build item;
- pause/interruption state;
- objective-specific escrow policy;
- escrow release/reacquisition;
- observed completion;
- rollback/re-entry.

Those are control-state concepts, not reserve amounts.

## Drift check

- Donor remains sole behavioral authority: PASS.
- No fabricated exact ordinal/byte offsets: PASS.
- Source-order topology preserved where authenticated windows were available: PASS.
- Command/completion distinction preserved: PASS.
- Distributed pause/re-entry preserved: PASS.
- Current Byzantine central transaction model identified as non-donor architecture: PASS.
- New implementation code introduced: NONE.

## Evidence classes

- Donor escrow/progression rule bodies: DIRECT.
- Byzantine comparison: DIRECT from current repository files.
- Full numeric donor ordinal/byte map: UNKNOWN / transport-unqualified.
- Proposed progression ABI boundary: COMPOSED.
