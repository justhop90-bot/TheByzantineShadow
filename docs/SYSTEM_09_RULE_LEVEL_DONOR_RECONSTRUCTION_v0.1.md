# The Byzantine Shadow — System 09 Rule-Level Donor Reconstruction v0.1

**Source:** `SourceShaRef` on `main`  
**Purpose:** Rule-level reconstruction of the recovered market/resource-exchange and escrow symbols, separating verified donor evidence from unresolved edges and AEGIS implementation requirements.  
**Status:** Evidence-gated forensic artifact; **not implementation authorization**.  
**Evidence taxonomy:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN.

---

## 0. Critical evidence boundary

`SourceShaRef` directly establishes the existence of the following recovered symbols:

- `LOW-ESCROW = 25`
- `MID-ESCROW = 35`
- `MID-HIGH-ESCROW = 40`
- `HIGH-ESCROW = 60`
- `CA-WOOD-TRADING-THRESHOLD = 300`
- `CA-EXCESS-WOOD-THRESHOLD = 450`
- `CA-NEED-WOOD-THRESHOLD = 250`
- `CA-NEED-STONE-THRESHOLD = 200`
- `gl-need-stone = 144`

The source also explicitly warns that unused code from earlier experiments may remain, and it declares a heterogeneous shared goal/timer namespace rather than a clean market module. fileciteturn55file0L2-L2

**Important limitation:** the currently retrievable `SourceShaRef` payload exposed to this analysis contains the declaration region but does not expose the complete rule bodies that consume these symbols. Therefore this document records **writer/reader/predicate/command/jump/mutation/resource-consequence edges as UNRECOVERED where the rule body is not actually available**. It does not invent them.

That distinction is itself a forensic result:

> **A symbol declaration is not a rule-level dependency graph.**

---

# 1. Rule-level reconstruction schema

Every recovered symbol must ultimately resolve to:

```text
SYMBOL
  ↓
PHYSICAL CHANNEL
  ↓
DEFINITION
  ↓
WRITERS
  ↓
READERS
  ↓
PREDICATES / OPERATORS
  ↓
PRECEDENCE
  ↓
JUMP / SUPPRESSION
  ↓
COMMANDS
  ↓
STATE MUTATIONS
  ↓
RESOURCE CONSEQUENCE
  ↓
RESET / EXPIRY
  ↓
CROSS-SYSTEM OWNER
  ↓
AEGIS DISPOSITION
```

A missing edge is recorded as `UNRECOVERED`, not `NONE`.

`NONE` means the complete rule graph was inspected and no edge exists.  
`UNRECOVERED` means the source evidence currently available is insufficient to decide.

---

# 2. Escrow symbol reconstruction

## S09-RL-001 — `LOW-ESCROW`

| Field | Reconstruction |
|---|---|
| Donor declaration | `LOW-ESCROW = 25` |
| Physical channel | Constant; no goal/timer channel established by declaration |
| Writers | **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate low escrow policy parameter; exact unit/semantics not proven |
| Evidence | DIRECT existence; UNCERTAIN semantics |
| Disposition | QUALIFY before transplant |

**Requirement:** recover every use site before interpreting `25` as 25%, a resource amount, a transaction parameter, or a policy level.

## S09-RL-002 — `MID-ESCROW`

| Field | Reconstruction |
|---|---|
| Donor declaration | `MID-ESCROW = 35` |
| Physical channel | Constant |
| Writers | **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate intermediate escrow policy parameter |
| Evidence | DIRECT existence; UNCERTAIN semantics |
| Disposition | QUALIFY before transplant |

## S09-RL-003 — `MID-HIGH-ESCROW`

| Field | Reconstruction |
|---|---|
| Donor declaration | `MID-HIGH-ESCROW = 40` |
| Physical channel | Constant |
| Writers | **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate high-intermediate escrow policy parameter |
| Evidence | DIRECT existence; UNCERTAIN semantics |
| Disposition | QUALIFY before transplant |

## S09-RL-004 — `HIGH-ESCROW`

| Field | Reconstruction |
|---|---|
| Donor declaration | `HIGH-ESCROW = 60` |
| Physical channel | Constant |
| Writers | **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate high escrow policy parameter |
| Evidence | DIRECT existence; UNCERTAIN semantics |
| Disposition | QUALIFY before transplant |

## Escrow aggregate finding — S09-RL-005

The four constants establish a **multi-level escrow vocabulary**, but do not by themselves establish:

- percentage units;
- resource scope;
- whether escrow is global or transaction-specific;
- who selects a level;
- whether levels are persistent or temporary;
- whether levels alter affordability, reservation, production, construction, research, or market behavior;
- release conditions;
- priority/preemption behavior.

**AEGIS requirement:** treat these as donor parameters until their readers, selectors, and downstream effects are recovered.

---

# 3. Market / resource threshold reconstruction

## S09-RL-010 — `CA-WOOD-TRADING-THRESHOLD`

| Field | Reconstruction |
|---|---|
| Donor declaration | `CA-WOOD-TRADING-THRESHOLD = 300` |
| Physical channel | Constant |
| Writers | N/A for immutable constant; selector/wrapper writers **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | Constant itself has no established expiry; use-site lifecycle **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate wood-trading decision boundary |
| Evidence | DIRECT existence; role UNCERTAIN |
| Disposition | PRESERVE AS EVIDENCE; QUALIFY |

**Do not classify `300` as a floor, ceiling, trigger, maintain threshold, or release threshold until its actual comparison and branch are recovered.**

## S09-RL-011 — `CA-EXCESS-WOOD-THRESHOLD`

| Field | Reconstruction |
|---|---|
| Donor declaration | `CA-EXCESS-WOOD-THRESHOLD = 450` |
| Physical channel | Constant |
| Writers | N/A for immutable constant; use-site state writers **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate wood surplus boundary |
| Evidence | DIRECT existence; role INFERRED |
| Disposition | PRESERVE + QUALIFY |

**Critical constraint:** `EXCESS-WOOD` does not imply `SELLABLE-WOOD`. Protected, committed, or otherwise reserved wood may remain economically unavailable.

## S09-RL-012 — `CA-NEED-WOOD-THRESHOLD`

| Field | Reconstruction |
|---|---|
| Donor declaration | `CA-NEED-WOOD-THRESHOLD = 250` |
| Physical channel | Constant |
| Writers | N/A for immutable constant; use-site writers **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate wood need/floor boundary |
| Evidence | DIRECT existence; role INFERRED |
| Disposition | PRESERVE + QUALIFY |

The threshold may belong to general economic allocation rather than market authority. That distinction must be recovered from readers and successor commands.

## S09-RL-013 — `CA-NEED-STONE-THRESHOLD`

| Field | Reconstruction |
|---|---|
| Donor declaration | `CA-NEED-STONE-THRESHOLD = 200` |
| Physical channel | Constant |
| Writers | N/A for immutable constant; use-site writers **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Operator | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate stone need boundary |
| Evidence | DIRECT existence; role INFERRED |
| Disposition | PRESERVE + QUALIFY |

Stone need is especially dangerous to classify as market-owned: it may be an infrastructure/technology/production prerequisite instead.

---

# 4. Related economic state carrier

## S09-RL-020 — `gl-need-stone = 144`

This is a **goal-channel mapping**, not a threshold.

| Field | Reconstruction |
|---|---|
| Donor declaration | `gl-need-stone` mapped to goal `144` |
| Physical channel | Goal 144 |
| Writers | **UNRECOVERED** |
| Readers | **UNRECOVERED** |
| Predicates | **UNRECOVERED** |
| Precedence | **UNRECOVERED** |
| Jumps / suppression | **UNRECOVERED** |
| Commands | **UNRECOVERED** |
| State mutations | **UNRECOVERED** |
| Resource consequence | Potential stone-demand state; exact effect **UNRECOVERED** |
| Reset / expiry | **UNRECOVERED** |
| Cross-system owner | **UNRECOVERED** |
| AEGIS interpretation | Candidate economic demand state carrier |
| Evidence | DIRECT mapping; semantics UNCERTAIN |
| Disposition | RECONSTRUCT before reuse |

**Do not reuse goal 144 simply because it is available.** Numeric identity is donor ABI, not semantic identity.

---

# 5. Precedence and jump reconstruction

For every symbol above, the following fields remain unresolved from the declaration evidence:

| Required edge | Current status | Prohibited inference |
|---|---|---|
| Rule ordering | UNRECOVERED | Source declaration order ≠ runtime authority |
| Competing writers | UNRECOVERED | One symbolic owner cannot be assumed |
| `up-jump-rule` use | UNRECOVERED | Do not assume market preemption |
| Suppression / cancellation | UNRECOVERED | Do not infer from threshold crossings |
| Timer gating | UNRECOVERED | Do not infer age/time hysteresis |
| Emergency bypass | UNRECOVERED | Do not invent emergency market authority |
| Reset / expiry | UNRECOVERED | Do not infer persistence from constant lifetime |

The rule-level pass must search specifically for `up-jump-rule`, rule-order conflicts, goal writes, timer gates, and state-clearing operations around each market/escrow reader.

---

# 6. Cross-system ownership reconstruction

Until rule bodies are recovered, ownership must remain unresolved. The following candidate ownership tests are mandatory:

| Candidate interaction | Question that must be answered |
|---|---|
| System 05 Food → Market | Does food need/excess cause or merely permit exchange? |
| System 06 Labor → Market | Does labor allocation establish the resource surplus/deficit? |
| System 07 Construction → Market | Does infrastructure create the demand that market logic services? |
| System 08 Research → Market | Does research create a gold/food/wood requirement? |
| Production Authority → Market | Does production authorize liquidity demand, or does market logic choose production? |
| Market → Strategic state | Does market logic write a strategic objective? If yes, flag as authority violation candidate. |
| Escrow → Market | Can market logic consume protected resources? Who owns release authority? |
| Market → Escrow | Does a trade create a reservation? What is its lifetime and owner? |

**Default AEGIS ownership rule:** market/resource exchange is an executor-side economic transaction boundary. It may expose feasibility, liquidity state, and verified economic consequences; it does not originate strategic objectives.

That rule is **AEGIS-GENERALIZATION**, not a claim about historical Shadow semantics.

---

# 7. What is actually reconstructed now

### DIRECT donor facts

1. The escrow constants exist with values 25/35/40/60.
2. Wood trading/excess/need thresholds exist with values 300/450/250.
3. Stone need threshold exists with value 200.
4. `gl-need-stone` occupies goal 144.
5. The source uses a heterogeneous shared namespace and explicitly warns that unused experimental material may remain. fileciteturn55file0L2-L2

### COMPOSED / INFERRED findings

1. The source contains a recognizable economic-policy cluster.
2. The thresholds probably participate in resource-state decision logic.
3. The escrow constants probably represent selectable escrow levels.
4. The market symbols may interact with other economic systems.

None of those claims establishes a complete donor-native market transaction state machine.

### AEGIS-GENERALIZATION

The following remain AEGIS architecture rather than donor reconstruction:

- `LIQUIDITY_REQUIREMENT`
- `LIQUID_RESOURCE`
- `COMMITMENT_ID`
- `TRANSACTION_ID`
- owner/generation/validity envelopes
- explicit partial transaction state
- opportunity-cost accounting
- explicit verification lifecycle
- strategic authority separation

---

# 8. Mandatory next extraction pass

The next pass must obtain the **complete SourceShaRef rule bodies** and generate one row per actual use site, not merely one row per constant.

For every occurrence of each recovered symbol, record:

```text
SOURCE LINE
RULE ID / CONTEXT
SYMBOL
READ / WRITE
COMPARISON OPERATOR
OTHER PREDICATES
PRECEDING STATE
SOURCE ORDER
COMPETING RULES
UP-JUMP / SUPPRESSION
COMMANDS
GOAL / SN / TIMER MUTATIONS
RESOURCE DELTA EXPECTED
RESOURCE DELTA OBSERVED
RESET / CLEAR / EXPIRY
DOWNSTREAM READER
CROSS-SYSTEM OWNER
EVIDENCE CLASS
AEGIS DISPOSITION
```

Then collapse the occurrence-level rows into a true dependency graph:

```text
RESOURCE OBSERVATION
       ↓
NEED / EXCESS CLASSIFICATION
       ↓
MARKET CANDIDATE?
       ↓
AUTHORITY / PRECEDENCE
       ↓
ESCROW / PROTECTION
       ↓
MARKET COMMAND
       ↓
ENGINE STATE CHANGE
       ↓
RESOURCE DELTA
       ↓
VERIFICATION
       ↓
RECONCILIATION
       ↓
REASSESSMENT
```

Any missing edge must be reported as a **gap**, not supplied by AEGIS architecture.

---

# 9. Implementation gate

**System 09 remains forensic-only at this point.**

Muse must not implement market `.per` behavior from the constants in isolation.

The implementation gate is:

```text
COMPLETE SOURCE
    ↓
RULE-LEVEL OCCURRENCE EXTRACTION
    ↓
WRITER / READER GRAPH
    ↓
PRECEDENCE / JUMP GRAPH
    ↓
RESOURCE CONSEQUENCE GRAPH
    ↓
CROSS-SYSTEM AUTHORITY AUDIT
    ↓
DONOR FACT / AEGIS GENERALIZATION SEPARATION
    ↓
AEGIS DESIGN IMPROVEMENT
    ↓
`.per` IMPLEMENTATION
    ↓
RUNTIME QUALIFICATION
```

**Final forensic rule:**

> Recover the actual rule path before assigning meaning to the constant. Recover the authority path before assigning ownership. Recover the resource consequence before calling a transaction successful.
