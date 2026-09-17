# Closed Slice 01 — Spearman Production Qualification v0.1

## Status

Experimental modular/forensic slice. It is **not** the authenticated 1,956-rule Shadow runtime and must not replace or modify that runtime.

## Objective

Qualify one complete production lifecycle:

```text
BARRACKS OBSERVED
    -> SPEARMAN OBJECTIVE ADMITTED
    -> REQUIREMENT MATERIALIZED
    -> CAPITAL FEASIBILITY
    -> ESCROW COMMIT REQUEST
    -> ENGINE ESCROW COMMIT OBSERVED
    -> AUTHORITY GRANTED
    -> PRE-EXECUTION COUNT BASELINE
    -> UP-CAN-TRAIN
    -> UP-TRAIN
    -> EXECUTING
    -> WORLD-STATE COUNT DELTA
    -> VERIFIED
    -> ESCROW RELEASE REQUEST
    -> ENGINE ESCROW RELEASE
    -> ZERO ESCROW OBSERVED
    -> RELEASED
    -> REASSESSMENT
    -> IDLE
```

## Module ownership

| Stage | Owner |
|---|---|
| Barracks world-state observation | `02_state.per` |
| Objective/transaction demonstrator admission | `16_pass1_transaction.per` |
| Requirement/cost authority | `08_requirements.per` / Pass-1 demonstrator contract |
| Capital feasibility | `09_capital.per` / Pass-1 demonstrator gate |
| Physical escrow mutation and observation | `10_escrow.per` |
| Execution authority | `11_authority.per` |
| Training command | `12_execution.per` |
| World-state completion verification | `13_verification.per` |
| Failure recovery | `14_recovery.per` |
| Terminal lifecycle closure | `15_reassessment.per` |

`16_pass1_transaction.per` is retained as a vertical transaction demonstrator/ABI experiment. It is not an architectural orchestrator and must not become the production control plane.

## Required positive path

1. `building-type-count-total barracks > 0`.
2. `unit-type-count spearman-line < 1`.
3. Pass 1 enters `AEGIS-TRANSACTION-RESERVING`.
4. Requirement contract establishes `60 food + 40 wood` for this demonstrator.
5. Capital feasibility becomes `1` only when both resources are available.
6. Pass 1 leaves physical escrow mutation to Module 10.
7. Module 10 issues `up-modify-escrow` and does not declare commitment from command issuance.
8. Module 10 observes the four escrow balances and writes `AEGIS-ESCROW-COMMITTED`.
9. Module 11 grants authority only for READY + COMMITTED.
10. Module 12 captures a pre-execution trained Spearman baseline and issues `up-train` only under its documented guards.
11. Module 13 verifies completion from `unit-type-count`, not queued `unit-type-count-total`.
12. Module 13 requests escrow release only after world-state verification.
13. Module 10 issues release and independently observes all four escrow balances at zero.
14. Successful reassessment returns the transaction to IDLE.

## Required negative path

At minimum test:

- insufficient food;
- insufficient wood;
- no barracks;
- existing Spearman already satisfies the demonstrator objective;
- escrow commit command issued but commitment observation not yet satisfied;
- authority denied before training;
- training command issued but trained-unit count does not increase;
- release requested but escrow remains non-zero;
- failed transaction enters recovery;
- recovery does not clear until Module 10 reports RELEASED;
- reassessment does not close a failed transaction before `RECOVERY-CLEARED`.

## Qualification states

Do not collapse these into one pass/fail value:

```text
STATIC-PARSE
STATIC-SYMBOL-CLOSURE
STATIC-ORDER-CHECK
STATIC-JUMP-CHECK
STATIC-DEPENDENCY-CLOSURE
RUNTIME-LOAD
RUNTIME-RULE-FIRE
ENGINE-COMMAND-ISSUED
WORLD-STATE-COMPLETION
ESCROW-COMMIT-OBSERVED
ESCROW-RELEASE-OBSERVED
TRANSACTION-REASSESSMENT
```

## Hard evidence rule

A command is never completion evidence.

`up-modify-escrow` does not prove COMMITTED.
`up-train` does not prove a trained unit exists.
`up-release-escrow` does not prove RELEASED.

Each transition requires the corresponding engine/world-state observation.

## Runtime boundary

This qualification artifact does not authorize changing the authenticated Shadow runtime. The modular slice remains an experimental/forensic implementation until it passes static qualification and a separately controlled runtime test.
