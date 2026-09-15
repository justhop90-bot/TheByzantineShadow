# The Byzantine Shadow — System 09 Donor Reconstruction Matrix v0.1

**Source:** `SourceShaRef` (`main`)  
**Purpose:** Separate donor facts, AEGIS interpretations, and implementation requirements before market/resource-exchange transplantation.  
**Status:** Implementation-gating forensic artifact  
**Evidence:** DIRECT / COMPOSED / INFERRED / AEGIS-GENERALIZATION / UNCERTAIN

## 0. Forensic rule

`SourceShaRef` is a historical, heterogeneous Shadow corpus. It explicitly identifies Shadow as FireBall37's AI and warns that unused experimental code may remain. It also exposes a shared namespace containing military, scouting, economic, positional, timer, identity, and progression channels. The recovered source directly declares escrow-level constants and resource thresholds including `LOW-ESCROW`, `MID-ESCROW`, `MID-HIGH-ESCROW`, `HIGH-ESCROW`, `CA-WOOD-TRADING-THRESHOLD`, `CA-EXCESS-WOOD-THRESHOLD`, `CA-NEED-WOOD-THRESHOLD`, and `CA-NEED-STONE-THRESHOLD`. fileciteturn55file0L2-L2

> **Symbol presence is donor-existence evidence. It is not proof of semantic role, active reachability, authority, transaction lifecycle, or strategic correctness.**

Every row below deliberately separates:

1. **DONOR FACT** — what the source directly establishes.
2. **AEGIS INTERPRETATION** — the semantic/architectural meaning AEGIS may derive.
3. **IMPLEMENTATION REQUIREMENT** — what Muse should preserve, formalize, adapt, replace, quarantine, or qualify.

---

# 1. Primary reconstruction matrix

| ID | Donor symbol / fact | Donor fact | AEGIS interpretation | Implementation requirement | Evidence | Disposition |
|---|---|---|---|---|---|---|
| RM-001 | Shadow source identity | Source identifies Shadow as an AoE2 AI by FireBall37 and says unused code may remain. fileciteturn55file0L2-L2 | Historical donor contains active, legacy, and experimental material. | Never treat source presence as active architecture; require reachability evidence. | DIRECT | QUALIFY |
| RM-002 | Environment | Source comments specify Vikings-only, AoC UP 1.6+, Tiny Arabia, 1v1. fileciteturn55file0L2-L2 | Donor behavior is environment-specific historical evidence. | Do not transplant donor settings or coefficients as AoE2DE/Byzantine facts. | DIRECT | ADAPT |
| RM-003 | Goal namespace | Source states goals `1-317, 392, 478-479` are used. fileciteturn55file0L2-L2 | Numeric goal channels are donor ABI, not semantic identity. | Build a fresh AEGIS semantic registry; no blind numeric reuse. | DIRECT | REPLACE |
| RM-004 | `gl-need-stone = 144` | A named goal channel exists for stone need. fileciteturn55file0L2-L2 | A donor economic state carrier exists. | Recover all writers/readers before assigning market ownership. | DIRECT | QUALIFY |
| RM-005 | `gl-build-progress = 186` | A named progression channel exists. fileciteturn55file0L2-L2 | Economic/construction progression shares the donor namespace. | Do not reuse the channel for market state merely because it exists. | DIRECT | REPLACE |
| RM-006 | `LOW-ESCROW = 25` | Named escrow-level constant exists. fileciteturn55file0L2-L2 | Candidate low escrow policy level. Exact unit/scope unknown from declaration. | Recover readers/writers before calling it a percentage or policy state. | DIRECT / UNCERTAIN | QUALIFY |
| RM-007 | `MID-ESCROW = 35` | Named escrow-level constant exists. fileciteturn55file0L2-L2 | Candidate intermediate escrow level. | Preserve as donor parameter; do not hard-code as AEGIS doctrine. | DIRECT / UNCERTAIN | QUALIFY |
| RM-008 | `MID-HIGH-ESCROW = 40` | Named escrow-level constant exists. fileciteturn55file0L2-L2 | Candidate higher intermediate escrow level. | Do not infer `40%` without use-site evidence. | DIRECT / UNCERTAIN | QUALIFY |
| RM-009 | `HIGH-ESCROW = 60` | Named escrow-level constant exists. fileciteturn55file0L2-L2 | Candidate high escrow level. | Recover exact unit, resource scope, lifetime, and release semantics. | DIRECT / UNCERTAIN | QUALIFY |
| RM-010 | Four escrow levels | Four named levels coexist. fileciteturn55file0L2-L2 | Donor has a multi-level escrow vocabulary. | AEGIS may formalize policy states, but must label that as redesign rather than donor fact. | COMPOSED / AEGIS-GENERALIZATION | FORMALIZE |
| RM-011 | `CA-WOOD-TRADING-THRESHOLD = 300` | Wood trading threshold exists. fileciteturn55file0L2-L2 | Strong evidence of donor wood-trading policy. Exact trigger semantics unknown. | Extract every reader, operator, precondition, branch, command, and side effect. | DIRECT / UNCERTAIN role | QUALIFY |
| RM-012 | `CA-EXCESS-WOOD-THRESHOLD = 450` | Excess-wood threshold exists. fileciteturn55file0L2-L2 | Candidate surplus boundary. | Never equate `excess` with freely sellable resource without protection/commitment analysis. | DIRECT / INFERRED | QUALIFY |
| RM-013 | `CA-NEED-WOOD-THRESHOLD = 250` | Wood-need threshold exists. fileciteturn55file0L2-L2 | Candidate shortage/need boundary. | Determine whether it drives trade, labor, construction, or another subsystem. | DIRECT / INFERRED | QUALIFY |
| RM-014 | `CA-NEED-STONE-THRESHOLD = 200` | Stone-need threshold exists. fileciteturn55file0L2-L2 | Candidate stone shortage boundary. | Determine whether market-owned or general economic state. | DIRECT / INFERRED | QUALIFY |
| RM-015 | Domestic economic constants | Source groups wood/stone/economic constants under domestic configuration. fileciteturn55file0L2-L2 | Supports an economic-policy cluster, not automatically a standalone market module. | Separate market predicates from non-market resource predicates by rule graph. | DIRECT / COMPOSED | FORMALIZE |
| RM-016 | Map-conditioned constants | Source uses `#load-if-defined` for map-specific constants. fileciteturn55file0L2-L2 | Donor behavior contains compile/load-time environment specialization. | Check every market/resource threshold for conditional definitions before generalization. | DIRECT | QUALIFY |
| RM-017 | Time/age state | Source contains age-checking and temporal/economic constants such as `p2-current-age`, `p2-age-checking`, `LATE-GAME-TIME`, `STONE-DELAY`, `SkipMillTime`. fileciteturn55file0L2-L2 | Donor economic behavior can be temporally/age conditioned. | Prove the causal rule path; do not infer age-sensitive market behavior from variable existence alone. | DIRECT / INFERRED | QUALIFY |
| RM-018 | Heterogeneous namespace | Military, scouting, targeting, coordinates, timers, economy and progression all occupy the same goal/timer namespace. fileciteturn55file0L2-L2 | Market extraction is a graph-extraction problem, not a file-copy problem. | Map physical channel → semantic state → writers → readers → commands. | DIRECT | REPLACE / FORMALIZE |

---

# 2. What the donor facts do NOT prove

| AEGIS concept | Source support | Classification | Rule |
|---|---|---|---|
| `LIQUIDITY_REQUIREMENT` | Resource need/excess/trading thresholds | AEGIS-GENERALIZATION | May be introduced as AEGIS architecture; do not describe as donor-native. |
| `LIQUID_RESOURCE` | Constrained resource thresholds | AEGIS-GENERALIZATION | Compute from explicit AEGIS accounting, not hidden engine semantics. |
| `COMMITMENT_ID` | No direct declaration recovered | AEGIS-GENERALIZATION | Introduce only as an AEGIS state contract. |
| `TRANSACTION_ID` | No direct declaration recovered | AEGIS-GENERALIZATION | Needed for retry/reconciliation; must remain `.per`-feasible. |
| `OWNER/GENERATION/VALID` | No direct market declaration recovered | AEGIS-GENERALIZATION | Formalize for AEGIS authority; do not back-project into donor history. |
| Partial trade state | Trade thresholds exist | UNCERTAIN / AEGIS-GENERALIZATION | Runtime qualification required before implementation. |
| Opportunity-cost equation | Economic tradeoffs exist | AEGIS-GENERALIZATION | Design improvement, not donor fact. |
| Market-as-actuator boundary | Trading thresholds exist | AEGIS-GENERALIZATION | Strategic authority must be externalized in AEGIS. |
| Command ≠ completion | Not established by declarations | AEGIS verification rule | Must be runtime-qualified at the command/postcondition boundary. |
| Threshold = sellable surplus | Excess threshold exists | NOT PROVEN | Require resource protection and commitment analysis. |
| Escrow values = percentages | Values 25/35/40/60 exist | UNCERTAIN | Do not infer units from magnitude. |

---

# 3. Required reader/writer reconstruction

The matrix above is the **declaration-level pass**. The next pass must turn every market/escrow symbol into this exact graph:

```text
SOURCE SYMBOL
    ↓
PHYSICAL CHANNEL
    ↓
WRITERS
    ↓
READERS
    ↓
COMPARISON OPERATOR
    ↓
PRECONDITIONS
    ↓
BRANCH / PRECEDENCE
    ↓
JUMP / SUPPRESSION
    ↓
COMMAND
    ↓
STATE MUTATIONS
    ↓
RESOURCE CONSEQUENCE
    ↓
RESET / EXPIRY
    ↓
CROSS-SYSTEM DEPENDENCIES
```

For each edge, record:

```text
symbol
physical goal/SN/timer channel
definition location
writer rule(s)
reader rule(s)
operator
preconditions
source order
jump/suppression
commands
state mutations
resource affected
lifetime
reset/expiry
competing writer
owner
EVIDENCE LEVEL
AEGIS DISPOSITION
```

**No field may be filled from architectural expectation. Unknown is a valid result.**

---

# 4. Mandatory market symbol search set

The complete next-pass extraction must enumerate every source symbol or rule containing/semantically matching:

```text
trade
trading
market
buy
sell
exchange
need
excess
surplus
shortage
resource
food
wood
gold
stone
escrow
release
reserve
save
```

Then classify each match as:

```text
MARKET
ECONOMIC BUT NON-MARKET
ESCROW
PROGRESSION
MILITARY
SCOUTING
CONSTRUCTION
RESEARCH
LEGACY / EXPERIMENTAL
UNKNOWN
```

This prevents a symbol such as `need` or `excess` from being incorrectly promoted to market authority merely because its name sounds economic.

---

# 5. AEGIS implementation disposition

| Donor mechanism | Required treatment |
|---|---|
| Resource trading thresholds | PRESERVE AS EVIDENCE; FORMALIZE after reader/writer extraction. |
| Need/excess thresholds | PRESERVE + CLASSIFY; never equate excess with sellable. |
| Escrow constants | PRESERVE AS DONOR PARAMETERS; do not assume units. |
| Market commands | KEEP AS EXECUTION INTERFACE only after exact command path is recovered. |
| Donor numeric goal assignments | REPLACE with AEGIS semantic namespace. |
| Experimental/unused material | QUARANTINE until reachability is demonstrated. |
| Donor coefficients | ADAPT; qualify/tune rather than worship values. |
| Strategic market selection | REPLACE / AEGIS-OWNED. |
| Commitment lifecycle | FORMALIZE as AEGIS architecture if representable in `.per`. |
| Transaction lifecycle | FORMALIZE with immutable retry identity if representable. |
| Verification | IMPROVE; economic postcondition required. |
| Partial transaction semantics | QUALIFY before implementation. |
| Opportunity-cost accounting | AEGIS-GENERALIZATION. |
| Global escrow reset | REJECT unless ownership and scope are proven. |

---

# 6. Cross-system authority audit

Every recovered market rule must be checked against Systems 02, 05, 06, 07, and 08 for:

- duplicate writers;
- conflicting economic state;
- market logic writing strategic state;
- resource allocation bypassing commitments;
- non-owner escrow release;
- construction/research/production consuming protected resources;
- circular `requirement → market → requirement` loops;
- hidden priority caused solely by rule order;
- `up-jump-rule` suppression that bypasses commitment ownership.

The final authority graph should be:

```text
AEGIS OBJECTIVE
      ↓
CAPABILITY / ECONOMIC REQUIREMENT
      ↓
MARKET CANDIDATE
      ↓
AEGIS / ECONOMIC AUTHORIZATION
      ↓
COMMITMENT
      ↓
RESOURCE PROTECTION / PREFLIGHT
      ↓
MARKET EXECUTOR INTERFACE
      ↓
ENGINE COMMAND
      ↓
OBSERVED ECONOMIC DELTA
      ↓
VERIFICATION
      ↓
RECONCILIATION
      ↓
REASSESSMENT
```

If the donor has a different edge, record it as **donor behavior** first. Do not silently rewrite it into this graph during archaeology.

---

# 7. Qualification register

Every unresolved claim must have:

```text
CLAIM
STATIC EVIDENCE
REQUIRED OBSERVATION
EXPECTED POSTCONDITION
FAILURE SIGNATURE
PROMOTION CRITERION
```

Priority qualifications:

1. exact meaning/unit of `LOW/MID/MID-HIGH/HIGH-ESCROW`;
2. exact readers/writers of every `CA-*` threshold;
3. whether thresholds actually invoke market commands;
4. whether excess resources are protected/committed before trading;
5. exact market command lifecycle;
6. observable source/target resource deltas;
7. partial/failed transaction semantics;
8. retry behavior;
9. release behavior after trade;
10. `up-jump-rule`/rule-order effects on market authority.

---

# 8. Hard forensic invariants

**MK-RM-01** — Source presence is not active reachability.

**MK-RM-02** — A threshold declaration is not semantic classification.

**MK-RM-03** — A trading threshold is not proof of a market transaction.

**MK-RM-04** — Excess resource is not automatically sellable resource.

**MK-RM-05** — Gross resource is not automatically liquid resource.

**MK-RM-06** — Escrow magnitude does not prove unit or policy semantics.

**MK-RM-07** — Numeric goal identity does not equal semantic identity.

**MK-RM-08** — Source order alone does not establish authority when competing predicates exist.

**MK-RM-09** — Market command is not proof of economic completion.

**MK-RM-10** — Partial economic effect is not full requirement satisfaction.

**MK-RM-11** — Affordability is not strategic correctness.

**MK-RM-12** — AEGIS abstractions must not be back-projected into donor history.

**MK-RM-13** — Donor coefficients are evidence, not canonical AEGIS values.

**MK-RM-14** — Every resource reservation must have an identifiable owner before implementation.

**MK-RM-15** — Market logic may report economic infeasibility but may not silently manufacture strategic objectives.

**MK-RM-16** — Every retry must preserve transaction history and reconcile actual resource deltas.

**MK-RM-17** — Global escrow reset is prohibited unless exact ownership scope is proven.

**MK-RM-18** — No System 09 implementation may proceed from constants alone; rule-path reconstruction is mandatory.

---

# 9. Current verdict

`SourceShaRef` directly establishes escrow-level constants, resource-specific threshold constants, a heterogeneous shared control namespace, environment-specific configuration, and acknowledged historical/experimental material. fileciteturn55file0L2-L2

It does **not**, from the recovered declarations alone, establish a donor-native `LIQUIDITY` abstraction, explicit market commitment IDs, explicit transaction IDs, formal opportunity-cost accounting, partial-market-transaction semantics, exact escrow units, or market ownership of every resource threshold.

Those are AEGIS design targets and qualification questions.

## Engineering directive

**Do not implement System 09 from architectural prose alone.** The next forensic artifact must be the rule-level graph for every market/economic threshold and escrow mechanism:

```text
SOURCE SYMBOL
→ PHYSICAL CHANNEL
→ DEFINITION
→ WRITERS
→ READERS
→ PREDICATES
→ PRECEDENCE
→ JUMP / SUPPRESSION
→ COMMANDS
→ STATE MUTATIONS
→ RESOURCE CONSEQUENCE
→ RESET / EXPIRY
→ CROSS-SYSTEM DEPENDENCIES
→ EVIDENCE CLASS
→ AEGIS DISPOSITION
```

> **Recover first. Interpret second. Improve third. Implement fourth. Qualify fifth. Never reverse that order.**
