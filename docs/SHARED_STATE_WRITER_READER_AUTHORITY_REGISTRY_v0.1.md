# The Byzantine Shadow — Shared State / Writer-Reader Authority Registry v0.1

**Status:** Control-plane registry / implementation gate

**Scope:** Systems 01–09

**Purpose:** Provide a machine-checkable canonical registry for shared mutable state, its semantic ownership, writers, readers, mutation paths, verification sources, conflict status, and qualification gates.

**Evidence rule:** A registry row distinguishes recovered donor evidence from AEGIS architectural assignment. `UNRECOVERED` means the source occurrence has not been recovered; it does **not** mean “no writer/reader exists.”

---

## 1. Registry contract

Each row is a semantic state object, not merely a symbol inventory entry.

Required fields:

```text
stable_id
system
state_class
symbol_name
physical_channel
owner
writers
readers
mutation_path
verification_source
conflict_status
qualification_gate
evidence_level
status
```

### Stable ID convention

```text
SSAR-SXX-NNN
```

where `XX` is the owning system number and `NNN` is a stable three-digit state identifier. IDs are never reused after deletion; replacement semantics require a new generation/versioned entry.

---

# 2. Machine-readable registry

The following table is the normative registry surface. Fields deliberately contain `UNRECOVERED`, `UNKNOWN`, or `RUNTIME-QUALIFY` where the current forensic evidence does not establish a stronger claim.

| stable_id | system | state_class | symbol_name | physical_channel | owner | writers | readers | mutation_path | verification_source | conflict_status | qualification_gate | evidence_level | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SSAR-S01-001 | S01 | FACT | game-time | engine query / alias | S01 config boundary | engine | S01-S09 | engine observation → classified config state | engine time observation | SINGLE_OWNER_SEMANTIC | Q1,Q4,Q14 | DIRECT | ENGINE-SPECIFIC |
| SSAR-S01-002 | S01 | FACT | population-cap | engine query / alias | S01 config boundary | engine | S06,S08,Production | engine observation → consumer read | engine population-cap state | SINGLE_OWNER_SEMANTIC | Q1,Q4,Q14 | DIRECT | ENGINE-SPECIFIC |
| SSAR-S01-003 | S01 | MODE | current-age | engine query / alias | S01 configuration interface | engine | S06,S07,S08,Production | engine observation → age classification | engine age state | SHARED_READ_SINGLE_WRITE | Q1,Q2,Q4,Q14 | DIRECT | ENGINE-SPECIFIC |
| SSAR-S01-004 | S01 | FACT | resource-stock | food/wood/gold/stone queries | S01 engine-state boundary | engine | S05,S06,S09,Production,S07,S08 | engine observation → economic classification | engine resource state | SHARED_READ_SINGLE_WRITE | Q1,Q4,Q14 | DIRECT | ENGINE-SPECIFIC |
| SSAR-S01-005 | S01 | CONFIG | escrow policy constants | constants | S01 | S01 initialization | S02,S05-S09 | initialize policy → governed consumers | configuration/load qualification | SINGLE_OWNER_SEMANTIC | Q1,Q2,Q4,Q14 | DIRECT | DONOR-FACT/POLICY-CANDIDATE |
| SSAR-S02-001 | S02 | AUTHORITY | state registry | registry metadata | S02 | registry build/implementation | S01-S09 | declaration → ownership validation → mutation authorization | static registry audit | SINGLE_OWNER | Q1-Q5 | AEGIS-GENERALIZATION | ARCHITECTURAL |
| SSAR-S02-002 | S02 | AUTHORITY | owner | goal/SN or equivalent | S02 authority contract | domain owner through authorized path | S02 + domain consumers | request → owner check → authorized mutation | owner/generation audit | SINGLE_OWNER | Q4,Q5,Q7 | AEGIS-GENERALIZATION | ARCHITECTURAL |
| SSAR-S02-003 | S02 | AUTHORITY | generation | goal/SN/timer composite | domain-specific owner under S02 contract | domain-specific owner | dependent transaction/commitment readers | create generation → compare → accept/reject | generation comparison | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q7,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S02-004 | S02 | AUTHORITY | validity | goal/SN/timer composite | domain-specific owner under S02 contract | domain-specific owner | all dependent readers | establish → invalidate/expire → verify | domain postcondition | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q8,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S02-005 | S02 | EVIDENCE | evidence-level | state field / encoded state | S02 contract; domain result owner supplies value | verifier/result owner | downstream authority | observation → classification → evidence promotion | source-specific verifier | SINGLE_OWNER_SEMANTIC | Q4,Q11,Q14 | AEGIS-GENERALIZATION | ARCHITECTURAL |
| SSAR-S02-006 | S02 | TIMER | epoch/time | timer/SN | domain-specific owner | domain-specific owner | all lifetime-dependent states | initialize → advance → expiry check | engine time + domain event | RUNTIME_QUALIFICATION_REQUIRED | Q7,Q8,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S02-007 | S02 | CURSOR | gl-build-progress | goal/SN; donor candidate | S02 registry; progression owner is Shadow progression layer | UNRECOVERED | construction/research/production progression consumers | work-item verified → cursor advance | verified completion | MULTIPLE_WRITERS_UNRESOLVED | Q2,Q4,Q5,Q10,Q11,Q14 | DIRECT symbol / AEGIS ownership | CRITICAL_AUDIT |
| SSAR-S02-008 | S02 | IDENTITY | gl-current-build-item | goal/SN; donor candidate | Shadow progression | UNRECOVERED | S07,S08,production/progression consumers | work-item creation → identity write → retire/reset | work-item completion/invalidation | MULTIPLE_WRITERS_UNRESOLVED | Q2,Q4,Q5,Q8,Q10,Q14 | DIRECT symbol / AEGIS ownership | CRITICAL_AUDIT |
| SSAR-S02-009 | S02 | LATCH/MODE | gl-progression-pause | goal/SN; donor candidate | Shadow progression | UNRECOVERED | progression/executor gates | pause request → authority mutation → resume/retire | progression state + verified recovery | MULTIPLE_WRITERS_UNRESOLVED | Q2,Q4,Q5,Q8,Q10,Q14 | DIRECT symbol / AEGIS ownership | CRITICAL_AUDIT |
| SSAR-S02-010 | S02 | MODE | gl-escrow-state | goal/SN; donor carrier | Shadow transaction layer | UNRECOVERED | S07,S08,production transaction paths | transaction mode set → preflight → execute → clear | transaction/resource reconciliation | MULTIPLE_WRITERS_UNRESOLVED | Q2,Q4,Q5,Q9,Q14 | DIRECT symbol / AEGIS ownership | CRITICAL_AUDIT |
| SSAR-S03-001 | S03 | IDENTITY | target-identity | goal/SN composite | S03 | target acquisition writer | S03,S04,tactical consumers | observation → classification → target arbitration → identity mutation | target observation validity | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S03-002 | S03 | ENUMERATION | target-kind | goal/SN | S03 | target classifier | S03 tactical consumers | observation → classify → write kind | observed entity/class | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S03-003 | S03 | COORDINATE | target-position | goal/SN pair | S03 | target acquisition writer | S03 tactical systems | valid observation → coordinate write | fresh observation | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q8,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S03-004 | S03 | AUTHORITY | target-generation/validity | goal/SN composite | S03 | S03 only | target consumers | target replacement → generation/validity update | target freshness/observation | SINGLE_OWNER_SEMANTIC | Q4,Q7,Q8,Q11 | AEGIS-GENERALIZATION | ARCHITECTURAL |
| SSAR-S04-001 | S04 | IDENTITY | observation-id | goal/SN/composite | S04 | scouting/observation writer | S03,S04,belief layer | observation event → record identity | observation event | RUNTIME_QUALIFICATION_REQUIRED | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S04-002 | S04 | FACT | observation-state | state carrier | S04 | S04 | S03,target/belief consumers | scout mission → observe → record | observed world state | SINGLE_OWNER_SEMANTIC | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S04-003 | S04 | COORDINATE | observation-position | goal/SN pair | S04 | S04 | S03 | observation → coordinate write | observed location | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S04-004 | S04 | TIMER | observation-freshness | timer/SN | S04 | S04 | S03,S04 | observation epoch → refresh → stale/expire | engine time + observation | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q7,Q8,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S04-005 | S04 | ENUMERATION | scout-mission-state | state carrier | S04 | S04 | S04 | request → authorize → assign → move → observe → complete/fail | movement + observation | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S05-001 | S05 | ENUMERATION | food-source-state | state carrier | S05 | S05 | S06,S05 | source observation → classify → operational state | resource flow/source observation | RUNTIME_QUALIFICATION_REQUIRED | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S05-002 | S05 | FACT | food-continuity-state | state carrier | S05 | S05 | S06,AEGIS/economic requirement consumers | supply observation → continuity assessment | observed food flow | SINGLE_OWNER_SEMANTIC | Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S05-003 | S05 | REQUIREMENT | food-resource-requirement | state carrier | S05 within authorized economic demand | S05 | S06,S07,Shadow | continuity deficit → requirement | continuity/resource observation | STRATEGIC_AUTHORITY_BOUNDARY | Q4,Q5,Q11 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S05-004 | S05 | TELEMETRY | food-starvation-age | timer/SN | S05 | S05 | S06,arbitration | starvation detected → age/update | resource flow/worker state | SINGLE_OWNER_SEMANTIC | Q4,Q8,Q14 | AEGIS-GENERALIZATION | TELEMETRY |
| SSAR-S06-001 | S06 | FACT | villager-population-state | engine query | S06 economic boundary | engine | S06 | engine observation → labor accounting | engine villager count | SHARED_READ_SINGLE_WRITE | Q1,Q4,Q14 | DIRECT | ENGINE-SPECIFIC |
| SSAR-S06-002 | S06 | ENUMERATION | worker-state | state carrier | S06 | S06 | S05,S07,other economic consumers | observation → classify → assignment state | worker assignment/productivity observation | RUNTIME_QUALIFICATION_REQUIRED | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S06-003 | S06 | ENUMERATION | worker-allocation | state carrier | S06 | S06 | S05,S07,Shadow | requirement → allocation → assignment | observed assignment/productivity | MULTIPLE_WRITERS_UNRESOLVED | Q2,Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | CRITICAL_AUDIT |
| SSAR-S06-004 | S06 | FACT | resource-income-flow | state carrier | S06 | S06 | S05,S09,requirements | worker assignment → productivity → flow | observed resource delta | SINGLE_OWNER_SEMANTIC | Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S06-005 | S06 | REQUIREMENT | labor-requirement | state carrier | S06 | S06 + authorized request consumers | S06,S07,S05 | authorized requirement → labor demand | productive worker observation | SHARED_REQUEST_SINGLE_OWNER | Q4,Q5,Q11 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S06-006 | S06 | TELEMETRY | labor-starvation-age | timer/SN | S06 | S06 | arbitration/diagnostics | blocked demand → age/update | allocation/productivity observation | SINGLE_OWNER_SEMANTIC | Q4,Q8,Q14 | AEGIS-GENERALIZATION | TELEMETRY |
| SSAR-S07-001 | S07 | REQUIREMENT | infrastructure-requirement | state carrier | S07 | S07 from authorized requests | S06,S08,Shadow | need → requirement → deficit | verified building/capability | SINGLE_OWNER | Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S07-002 | S07 | IDENTITY | construction-commitment-id | commitment state | Shadow commitment layer / S07 interface | commitment writer | S07,S02,Shadow | requirement → commitment creation | commitment registry | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q7,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S07-003 | S07 | ENUMERATION | construction-transaction-state | transaction state | S07 | transaction executor | S07,Shadow | request → reserve → preflight → authorize → issue → observe | pending/building state | DUPLICATE_EXECUTOR_RISK | Q4,Q5,Q11,Q13,Q14 | AEGIS-GENERALIZATION | CRITICAL_AUDIT |
| SSAR-S07-004 | S07 | ENUMERATION | building-verification-state | state carrier | S07 | S07 verifier | downstream systems | pending → placed → building → complete → operational | building/pending/world observation | SINGLE_OWNER | Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S07-005 | S07 | COORDINATE | construction-site-state | goal/SN/composite | S07 | placement authority | S07 | site candidate → validate → placement | spatial/world observation | RUNTIME_QUALIFICATION_REQUIRED | Q2,Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S07-006 | S07 | IDENTITY | builder-assignment | state carrier | S06 owns worker assignment; S07 consumes | S06 | S07 | construction requirement → builder request → assignment | worker assignment observation | CROSS_SYSTEM_SINGLE_OWNER | Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S08-001 | S08 | REQUIREMENT | technology-requirement | state carrier | S08 | S08 from authorized strategic requests | S08,Shadow | capability deficit → technology candidate | capability/research state | SINGLE_OWNER | Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S08-002 | S08 | ENUMERATION | research-state | state carrier / engine query | S08 | engine + research executor interface | S08,AEGIS capability layer | preflight → issue → observe → verify | research/technology state | RUNTIME_QUALIFICATION_REQUIRED | Q2,Q4,Q11,Q14 | DIRECT/GENERALIZATION | ENGINE-QUALIFY |
| SSAR-S08-003 | S08 | IDENTITY | research-transaction-id | transaction state | Shadow transaction layer / S08 interface | transaction writer | S08,Shadow | requirement → transaction creation | transaction registry | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q7,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S08-004 | S08 | ENUMERATION | research-verification-state | state carrier | S08 | S08 verifier | AEGIS capability layer | research observation → verification | technology/research observation | SINGLE_OWNER | Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S08-005 | S08 | REQUIREMENT | prerequisite-state | dependency state | prerequisite owner; S08 consumes | prerequisite owner | S08 | prerequisite state observation | prerequisite owner's verifier | CROSS_SYSTEM_READ_ONLY | Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-001 | S09 | REQUIREMENT | liquidity-requirement | state carrier | S09 within authorized resource need | S09 from authorized request | S09,Shadow,requesting system | need → liquidity deficit → candidate | resource observation | STRATEGIC_AUTHORITY_BOUNDARY | Q4,Q5,Q11 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-002 | S09 | ENUMERATION | market-transaction-state | transaction state | S09 | S09 transaction executor | S09,Shadow | request → reserve → preflight → authorize → issue → observe | economic delta | SINGLE_OWNER | Q4,Q5,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-003 | S09 | FACT | liquid-resource-state | derived economic state | S09 | S09 accounting layer | S06,S07,S08,Production | gross → protection/commitments → liquid | resource observation + reconciliation | MULTIPLE_WRITERS_UNRESOLVED | Q2,Q4,Q9,Q11,Q14 | AEGIS-GENERALIZATION | CRITICAL_AUDIT |
| SSAR-S09-004 | S09 | ENUMERATION | market-verification-state | state carrier | S09 | S09 verifier | requesting subsystem | market command → resource deltas → verify | observed source/target resource state | SINGLE_OWNER | Q4,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-005 | S09 | THRESHOLD | market-threshold-policy | constants | S09 policy consumer; source constants governed by S01 config | UNRECOVERED | S09 | threshold evaluation only; no direct strategic objective mutation | static rule evidence + runtime behavior | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q14 | DIRECT constants / interpretation AEGIS | POLICY-CANDIDATE |
| SSAR-S09-006 | S09 | TELEMETRY | transaction-starvation-age | timer/SN | S09 | S09 | arbitration/diagnostics | blocked transaction → age/update | transaction state | SINGLE_OWNER_SEMANTIC | Q4,Q8,Q14 | AEGIS-GENERALIZATION | TELEMETRY |
| SSAR-S09-007 | S09 | RESERVATION | transaction-escrow | resource state | Shadow transaction layer | transaction authority | executor | reserve → authorize → consume/return | resource delta + transaction verification | RESERVATION_RACE_RISK | Q4,Q9,Q11,Q14 | AEGIS-GENERALIZATION | CRITICAL_AUDIT |
| SSAR-S09-008 | S09 | THRESHOLD | LOW-ESCROW | constant | S01 configuration / Shadow economic policy | initialization | S05-S09 consumers | configure → read | static definition/config qualification | SINGLE_OWNER_SEMANTIC | Q1,Q2,Q14 | DIRECT | POLICY-CONSTANT |
| SSAR-S09-009 | S09 | THRESHOLD | MID-ESCROW | constant | S01 configuration / Shadow economic policy | initialization | S05-S09 consumers | configure → read | static definition/config qualification | SINGLE_OWNER_SEMANTIC | Q1,Q2,Q14 | DIRECT | POLICY-CONSTANT |
| SSAR-S09-010 | S09 | THRESHOLD | MID-HIGH-ESCROW | constant | S01 configuration / Shadow economic policy | initialization | S05-S09 consumers | configure → read | static definition/config qualification | SINGLE_OWNER_SEMANTIC | Q1,Q2,Q14 | DIRECT | POLICY-CONSTANT |
| SSAR-S09-011 | S09 | THRESHOLD | HIGH-ESCROW | constant | S01 configuration / Shadow economic policy | initialization | S05-S09 consumers | configure → read | static definition/config qualification | SINGLE_OWNER_SEMANTIC | Q1,Q2,Q14 | DIRECT | POLICY-CONSTANT |
| SSAR-S09-012 | S09 | THRESHOLD | CA-WOOD-TRADING-THRESHOLD | constant | S09 policy layer | initialization | market rules | read → compare | market/resource observation | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q14 | DIRECT | POLICY-CANDIDATE |
| SSAR-S09-013 | S09 | THRESHOLD | CA-EXCESS-WOOD-THRESHOLD | constant | S09 policy layer | initialization | market rules | read → compare | resource observation | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q14 | DIRECT | POLICY-CANDIDATE |
| SSAR-S09-014 | S09 | THRESHOLD | CA-NEED-WOOD-THRESHOLD | constant | S09 policy layer | initialization | market rules | read → compare | resource observation | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q14 | DIRECT | POLICY-CANDIDATE |
| SSAR-S09-015 | S09 | THRESHOLD | CA-NEED-STONE-THRESHOLD | constant | S09 policy layer | initialization | market rules | read → compare | resource observation | WRITER_EVIDENCE_UNRECOVERED | Q2,Q4,Q14 | DIRECT | POLICY-CANDIDATE |
| SSAR-S09-016 | S09 | IDENTITY | commitment-id | goal/SN/composite | Shadow commitment layer | commitment authority | S05-S09 transactions | requirement → commitment | commitment lifecycle verification | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q7,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-017 | S09 | ENUMERATION | commitment-state | goal/SN/composite | Shadow commitment layer | commitment authority | all economic executors | candidate → committed → funded → executing → verified | commitment/result verification | RUNTIME_QUALIFICATION_REQUIRED | Q4,Q7,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-018 | S09 | RESERVATION | commitment-escrow | resource state | Shadow commitment layer | commitment authority | S06-S09 economic systems | commitment → reserve → consume/release | transaction/resource reconciliation | RESERVATION_RACE_RISK | Q4,Q9,Q11,Q14 | AEGIS-GENERALIZATION | IMPLEMENTATION_REQUIRED |
| SSAR-S09-019 | S09 | RESERVATION | policy-escrow | percentage policy | Shadow economic policy | policy writer | transaction/commitment preflight | policy initialization → protected envelope | resource state qualification | SEMANTIC_COLLISION_RISK | Q2,Q4,Q9,Q14 | DIRECT constants; semantics generalized | CRITICAL_AUDIT |

---

# 3. Mutation-path registry

Every authoritative mutation must map to one of these canonical paths.

| path_id | mutation path | permitted state classes | authority requirement | verification requirement |
|---|---|---|---|---|
| MP-01 | `OBSERVE → CLASSIFY → WRITE → VERIFY` | FACT/BELIEF | observation owner | observed source state |
| MP-02 | `REQUEST → AUTHORITY CHECK → WRITE → VERIFY` | REQUIREMENT/MODE | domain owner | resulting valid state |
| MP-03 | `REQUIREMENT → COMMITMENT → RESERVE → VERIFY` | COMMITMENT/RESERVATION | Shadow commitment owner | attributable reservation |
| MP-04 | `REQUEST → PREFLIGHT → AUTHORIZE → COMMAND → OBSERVE → VERIFY` | TRANSACTION | transaction owner | physical/economic postcondition |
| MP-05 | `WORK ITEM → EXECUTE → POSTCONDITION → PROGRESS++` | CURSOR | progression owner | sufficient completion evidence |
| MP-06 | `ACTIVE → SUSPEND → RECONCILE → PREEMPT → VERIFY → RESUME/RETIRE` | AUTHORITY/COMMITMENT | higher-priority authority | emergency result + reconciliation |
| MP-07 | `OBSERVED FAILURE → INVALIDATE/EXPIRE → RELEASE/RECONCILE` | VALIDITY/LIFETIME | state owner | failure/expiry evidence |
| MP-08 | `OBSERVATION → FRESHNESS UPDATE → STALE/INVALID` | EVIDENCE/TIMER | observation owner | time + observation provenance |

Forbidden shortcuts:

```text
COMMAND → COMPLETION
COMMAND → PROGRESS++
READER → AUTHORITATIVE WRITE
FAILURE → GLOBAL RESET
RESOURCE SHORTAGE → UNAUTHORIZED TRADE
EXECUTOR → STRATEGIC OBJECTIVE
TELEMETRY → CONTROL MUTATION
```

---

# 4. Conflict-status vocabulary

The registry uses the following machine-checkable values:

```text
SINGLE_OWNER
SINGLE_OWNER_SEMANTIC
SHARED_READ_SINGLE_WRITE
SHARED_REQUEST_SINGLE_OWNER
CROSS_SYSTEM_SINGLE_OWNER
CROSS_SYSTEM_READ_ONLY
MULTIPLE_WRITERS_UNRESOLVED
DUPLICATE_EXECUTOR_RISK
RESERVATION_RACE_RISK
STRATEGIC_AUTHORITY_BOUNDARY
WRITER_EVIDENCE_UNRECOVERED
RUNTIME_QUALIFICATION_REQUIRED
SEMANTIC_COLLISION_RISK
```

`UNRECOVERED` is an evidence state, not a conflict status.

---

# 5. Qualification-gate registry

| gate | name | pass condition | blocking failure |
|---|---|---|---|
| Q1 | Symbol identity | Physical symbol/channel is identified | ambiguous channel/alias |
| Q2 | Writer inventory | Every actual writer is recovered or explicitly marked UNRECOVERED | fabricated/unknown writer treated as none |
| Q3 | Reader inventory | Material readers/dependencies are enumerated | hidden dependency |
| Q4 | Ownership | Exactly one semantic owner is assigned | competing owners |
| Q5 | Mutation path | Every write has authorized transition path | direct arbitrary write |
| Q6 | Precedence | Competing authorities have explicit resolution | source-order-only arbitration |
| Q7 | Generation | Stale generation cannot mutate current state | stale write accepted |
| Q8 | Lifetime | creation/reset/expiry/invalidation defined | immortal or ambiguous state |
| Q9 | Resource attribution | reserve/consume/release attributable | double-spend/global reset |
| Q10 | Progression | cursor advances only after verified postcondition | command advances progress |
| Q11 | Verification | sufficient postcondition defined | acknowledgement used as completion |
| Q12 | Failure handling | reject/fail/partial/unverified/expired/preempted paths explicit | infinite retry/false success |
| Q13 | Bypass audit | all legacy/direct executor paths classified | hidden executor/bypass |
| Q14 | Runtime ABI | target-build engine semantics qualified | untested engine assumption |
| Q15 | Vertical slice | integrated requirement→result loop verified | isolated rule only |
| Q16 | Adversarial review | duplicate authority/resource/progression/verification failures tested | critical invariant failure |

---

# 6. Machine-checking rules

A registry validator should fail the build if any of the following is true for an authoritative row:

```text
owner == EMPTY
writers == EMPTY AND evidence != UNRECOVERED
mutation_path == EMPTY
verification_source == EMPTY
qualification_gate == EMPTY
```

It should additionally fail if:

```text
conflict_status == MULTIPLE_WRITERS_UNRESOLVED
AND status == IMPLEMENTATION_READY
```

or:

```text
state_class in {CURSOR, RESERVATION, TRANSACTION, COMMITMENT, AUTHORITY}
AND qualification_gate does not include Q4
```

or:

```text
state_class == CURSOR
AND mutation_path does not require Q10
```

or:

```text
state_class in {RESERVATION, TRANSACTION}
AND mutation_path does not require Q9
```

or:

```text
status == RUNTIME_CONFIRMED
AND qualification_gate does not include Q14
```

These checks are architectural lint rules; they do not themselves establish engine behavior.

---

# 7. Donor-evidence discipline

The registry deliberately does not claim that every AEGIS state object exists in the donor.

The following distinctions are mandatory:

### DIRECT

A symbol, command, definition, or rule relationship is directly recovered from donor source.

### COMPOSED

Multiple direct donor facts establish a relationship without a single donor rule expressing the complete relationship.

### INFERRED

The interpretation follows from evidence but is not directly stated by source.

### AEGIS-GENERALIZATION

The state/authority model is an AEGIS architectural improvement rather than donor reconstruction.

### UNCERTAIN

Evidence is insufficient to establish the claim.

In particular:

- `gl-escrow-state` existence is donor evidence; its canonical AEGIS ownership contract is architectural.
- `gl-current-build-item`, `gl-build-progress`, and `gl-progression-pause` are donor candidates with semantic roles established by the forensic corpus, but exact writer graphs still require occurrence-level extraction.
- `LOW-ESCROW`, `MID-ESCROW`, `MID-HIGH-ESCROW`, and `HIGH-ESCROW` are direct constants; their precise runtime policy semantics remain separate from their existence.
- Market thresholds are direct constants; their full causal rule paths require source-body recovery.

---

# 8. Immediate audit priorities

The registry identifies four critical unresolved classes that must be resolved before broad `.per` implementation:

1. **Progression writers:** `gl-build-progress`, `gl-current-build-item`, `gl-progression-pause`.
2. **Escrow writers:** `gl-escrow-state`, policy/commitment/transaction reservation paths.
3. **Worker allocation writers:** any competing assignment paths crossing S05/S06/S07.
4. **Transaction/resource writers:** market, production, research, and construction paths that can reserve/consume/release shared resources.

The required extraction is occurrence-level, not symbol-level:

```text
FILE
LINE
RULE CONTEXT
SYMBOL
READ/WRITE
OPERATOR
PRECEDING PREDICATES
SOURCE ORDER
JUMP/SUPPRESSION
COMMAND
MUTATION
DOWNSTREAM READER
RESOURCE CONSEQUENCE
RESET/CLEAR
EXPIRY
EVIDENCE
```

Until that extraction exists, unresolved writer fields remain `UNRECOVERED`.

---

# 9. Implementation promotion states

Each row should eventually move through:

```text
REGISTERED
  ↓
SOURCE-AUDITED
  ↓
OWNER-RESOLVED
  ↓
MUTATION-RESOLVED
  ↓
VERIFICATION-DEFINED
  ↓
STATIC-QUALIFIED
  ↓
RUNTIME-QUALIFIED
  ↓
IMPLEMENTATION-READY
```

No row may skip directly from `REGISTERED` to `IMPLEMENTATION-READY`.

---

# 10. Definition of done

The registry is complete only when every shared state object across Systems 01–09 has:

- stable ID;
- semantic type;
- physical channel;
- owner;
- complete writer inventory or explicit UNRECOVERED status;
- complete reader inventory;
- authorized mutation path;
- verification source;
- conflict classification;
- qualification gates;
- evidence classification;
- implementation status;
- lifetime/reset/expiry semantics;
- generation semantics where stale state is possible;
- resource attribution where resources are involved;
- explicit downstream dependencies;
- explicit legacy/bypass disposition.

The registry must be treated as a control-plane source of truth. Implementation changes that alter ownership, writers, readers, mutation paths, or verification contracts require a registry update in the same change set.

---

# 11. Engineering directive

Muse is not authorized to resolve registry gaps by guessing.

Where source evidence is incomplete, preserve `UNRECOVERED` and perform the missing occurrence-level extraction. Where donor behavior is insufficient, make the AEGIS improvement explicit as `AEGIS-GENERALIZATION`. Where runtime semantics are unqualified, retain `RUNTIME-QUALIFICATION-REQUIRED`.

The purpose of this registry is not documentation for its own sake. It is the **machine-checkable authority boundary that prevents the `.per` implementation from recreating the donor's hidden multi-writer control plane under a new set of names.**

The next implementation gate is therefore not “write more rules.” It is:

```text
REGISTRY
 → STATIC OCCURRENCE EXTRACTION
 → CONFLICT RESOLUTION
 → ABI / GENERATION ALLOCATION
 → ONE VERIFIED CROSS-SYSTEM VERTICAL SLICE
 → ONLY THEN BROAD IMPLEMENTATION
```
