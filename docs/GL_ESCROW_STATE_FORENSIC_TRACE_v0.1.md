# gl-escrow-state Static Forensic Trace v0.1

**Source:** `SourceShaRef` on `main`
**Source line count:** 22603

## Verdict

Direct goal writes were recovered:
- line 15477: `(set-goal gl-escrow-state without-escrow)`
- line 15538: `(set-goal gl-escrow-state with-escrow)`
- line 15545: `(set-goal gl-escrow-state with-escrow)`
- line 17855: `(set-goal gl-escrow-state with-escrow)`
- line 20301: `(set-goal gl-escrow-state with-escrow)`
- line 20897: `(set-goal gl-escrow-state with-escrow)`

This is distinct from the escrow resource mutations performed by `set-escrow-percentage`, `up-modify-escrow`, and `release-escrow`: those mutate escrow accounting, not the `gl-escrow-state` goal itself.

## All literal occurrences
| line | classification | source |
|---:|---|---|
| 1571 | SYMBOL_REFERENCE | `(defconst gl-escrow-state 205)` |
| 4698 | SYMBOL_REFERENCE | `(not(up-can-build-line gl-escrow-state point-x c: palisade-wall))` |
| 4744 | SYMBOL_REFERENCE | `(not(up-can-build-line gl-escrow-state point-x c: house))` |
| 4751 | SYMBOL_REFERENCE | `(not(up-can-build-line gl-escrow-state point-x c: house))` |
| 4760 | SYMBOL_REFERENCE | `(up-can-build-line gl-escrow-state point-x c: house)` |
| 14319 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-scale-mail)` |
| 14353 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-chain-mail)` |
| 14370 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-iron-casting)` |
| 14418 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-iron-casting)` |
| 14467 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-forging)` |
| 14517 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-forging)` |
| 14567 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-chain-barding)` |
| 14617 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-chain-barding)` |
| 14668 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-scale-barding)` |
| 14720 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-scale-barding)` |
| 14776 | EXECUTOR_PARAMETER | `(up-can-research gl-escrow-state c: ri-crossbow)` |
| 14778 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-crossbow)` |
| 15030 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-leather-archer-armor)` |
| 15127 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-bodkin-arrow)` |
| 15248 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: mangonel-line)` |
| 15267 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: mangonel-line)` |
| 15441 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: knight-line)` |
| 15460 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: archer-line)` |
| 15468 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: archer-line)` |
| 15477 | DIRECT_WRITE;GOAL_MUTATION_CANDIDATE;READ | `(set-goal gl-escrow-state without-escrow)` |
| 15513 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: skirmisher-line)` |
| 15537 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: skirmisher-line)` |
| 15538 | DIRECT_WRITE;GOAL_MUTATION_CANDIDATE;READ | `(set-goal gl-escrow-state with-escrow)` |
| 15545 | DIRECT_WRITE;GOAL_MUTATION_CANDIDATE;READ | `(set-goal gl-escrow-state with-escrow)` |
| 15587 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: spearman-line)` |
| 15592 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: spearman-line)` |
| 15646 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: spearman-line)` |
| 15653 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: spearman-line)` |
| 15798 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: stable)` |
| 15860 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: stable)` |
| 15946 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: stable)` |
| 16000 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: stable)` |
| 16075 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: stable)` |
| 16127 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: stable)` |
| 16191 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: monastery)` |
| 16262 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: market)` |
| 16333 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: market)` |
| 16473 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: market)` |
| 17855 | DIRECT_WRITE;GOAL_MUTATION_CANDIDATE;READ | `(set-goal gl-escrow-state with-escrow)` |
| 19558 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-bow-saw)` |
| 19608 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-bow-saw)` |
| 19742 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-gold-shaft-mining)` |
| 19877 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-heavy-plow)` |
| 19957 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: villager)` |
| 19963 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: villager)` |
| 19975 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: villager)` |
| 19977 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: villager)` |
| 19985 | EXECUTOR_PARAMETER | `(up-can-train gl-escrow-state c: villager)` |
| 19991 | EXECUTOR_PARAMETER | `(up-train gl-escrow-state c: villager)` |
| 20297 | EXECUTOR_PARAMETER | `(up-can-research gl-escrow-state c: ri-elite-skirmisher)))` |
| 20299 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-elite-skirmisher)` |
| 20301 | DIRECT_WRITE;GOAL_MUTATION_CANDIDATE;READ | `(set-goal gl-escrow-state with-escrow)` |
| 20369 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: siege-workshop)` |
| 20536 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: barracks)` |
| 20846 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: farm)` |
| 20890 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: farm)` |
| 20897 | DIRECT_WRITE;GOAL_MUTATION_CANDIDATE;READ | `(set-goal gl-escrow-state with-escrow)` |
| 20935 | EXECUTOR_PARAMETER | `(up-can-build gl-escrow-state c: farm)` |
| 20941 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: farm)` |
| 21096 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: house)` |
| 21108 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: house)` |
| 21515 | EXECUTOR_PARAMETER | `(up-can-build gl-escrow-state c: lumber-camp)` |
| 21518 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: lumber-camp)` |
| 21778 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: mining-camp)` |
| 21869 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: mining-camp)` |
| 22087 | EXECUTOR_PARAMETER | `(up-can-build gl-escrow-state c: mining-camp)` |
| 22094 | SYMBOL_REFERENCE | `(up-build place-normal gl-escrow-state c: mining-camp)` |
| 22106 | SYMBOL_REFERENCE | `(up-build place-control gl-escrow-state c: university)` |
| 22152 | EXECUTOR_PARAMETER | `(up-research gl-escrow-state c: ri-ballistics)` |

## Indirect-mutation audit

- `gl-escrow-state` is passed as the `EscrowState` goal parameter to escrow-aware feasibility/execution commands.
- Those commands **read** the goal value to select escrow-included versus escrow-deducted behavior; they do not write the goal.
- `set-escrow-percentage`, `release-escrow`, and `up-modify-escrow` mutate the engine escrow amounts/policy, not `gl-escrow-state`.
- Therefore the donor source establishes `gl-escrow-state` as a stable mode carrier whose value is supplied by goal state, while the resource escrow subsystem is mutated separately.

## Evidence rule

Absence of a direct write is a static-source finding, not proof that the engine can never mutate the goal. Engine initialization/default semantics remain runtime/ABI evidence territory.
