# Shadow Rule Atlas v0.1

## Status

**Role:** forensic reconstruction artifact specification and operating contract.

**Authority:** `ShadowSource.per` remains the canonical source candidate. This atlas is derived evidence; it never replaces the source.

**Attitude:** A rule index is not a bot. A pretty graph is not a bot. If an assertion cannot be traced to a rule, source offset, or runtime observation, it is not yet an engineering fact.

---

## 1. Purpose

The atlas exists to turn Shadow's 22k-line `.per` monolith into a machine-addressable corpus without prematurely imposing conventional software architecture.

For every `defrule`, record:

- ordinal in source order;
- exact source line range;
- exact byte range;
- raw source hash;
- predicate text;
- action text;
- goals read/written;
- strategic-number writes and, where later parsers permit, reads;
- jumps;
- commands;
- escrow operations;
- search/placement operations;
- temporal predicates/actions;
- provisional semantic tags.

The atlas is deliberately lexical first. Semantic interpretation is a later layer.

## 2. Non-negotiable forensic rules

1. **Do not reorder rules.** Source order is evidence.
2. **Do not normalize away comments before preserving the raw rule.** Comments can identify author intent and historical seams.
3. **Do not infer completion from command issuance.**
4. **Do not infer commitment from `can-build-with-escrow`.**
5. **Do not infer completion from pending-object or pending-placement state.**
6. **Do not treat a jump as a normal function call.** Its positional semantics must remain explicit.
7. **Do not invent module ownership from symbol names.** Build the data-flow map first.
8. **Do not call static reachability runtime reachability.**
9. **Do not silently repair malformed source.** Record the defect.
10. **Do not copy Shadow into ShadowByzantine until the machine being copied is understood.**

## 3. Evidence levels

| Level | Meaning |
|---|---|
| DIRECT | Explicitly present in source or measured runtime evidence. |
| COMPOSED | Deterministically derived from multiple direct observations. |
| INFERRED | A defensible interpretation requiring assumptions. |
| UNCERTAIN | Competing explanations remain. |

The atlas itself should primarily contain DIRECT and COMPOSED facts.

## 4. Required derived views

The raw atlas is only the beginning. The reconstruction pipeline must derive these views without changing source evidence.

### 4.1 Control-flow view

```text
rule N
  -> fall-through successor
  -> jump successor(s)
  -> conditional dispatch context
  -> possible re-entry region
```

Track forward skips, negative jumps, loops, disabled rules, and source-order dependencies separately.

### 4.2 State/data-flow view

For each goal, strategic number, and timer of interest:

```text
writer(s)
   |
   v
stored state
   |
   +--> reader(s)
   |
   +--> command/action
   |
   +--> reset/release path
```

A symbol with many writers is not automatically a bug. It is a candidate arbitration point and must be studied in source order.

### 4.3 Escrow view

Every occurrence must be indexed by:

```text
rule
resource
operation
predicate context
associated state
associated command
preceding rule region
following rule region
release/reallocation candidates
```

The interesting question is not the count of escrow calls. It is whether repeated escrow patterns form a resource-protection and commitment mechanism.

### 4.4 Progression view

For construction/progression, correlate:

```text
objective selector
 -> feasibility
 -> escrow/resource protection
 -> target resolution
 -> build command
 -> pending observation
 -> world observation
 -> progression write
 -> release/re-entry
```

The chain must be demonstrated, not assumed.

## 5. Shadow-specific hypotheses to test

These are research hypotheses, not axioms:

- `gl-current-build-item` behaves like an active milestone/cursor.
- `gl-build-progress` behaves like an ordered progression register.
- `gl-progression-pause` gates or arbitrates progression.
- `gl-escrow-state` selects an engine/accounting mode used by construction paths.
- escrow is repeatedly used to protect an objective against competing resource consumers.
- progression is recognized through observations of the world, not merely by command issuance.
- source order plus jumps creates a practical state machine without a conventional dispatcher.

Each hypothesis must eventually be linked to multiple source regions and, where possible, replay evidence.

## 6. Minimum acceptance criteria

The atlas generator is acceptable only if it can report:

- source byte length and cryptographic hashes;
- rule count;
- every rule's source offset;
- every rule's stable ordinal;
- parse failures explicitly;
- unbalanced block detection;
- escrow-bearing rules;
- jump-bearing rules;
- goal-writing rules;
- construction-bearing rules;
- search/placement-bearing rules;
- deterministic output.

The expected historical Shadow rule count is approximately 1,956; any different count is a **finding requiring reconciliation**, not a number to be silently adjusted.

## 7. Artifact contract

The generator in `tools/forensics_shadow_rule_atlas.py` emits:

- `shadow_rule_atlas.json` — primary machine-readable inventory;
- `shadow_rule_atlas.csv` — analyst-friendly flat view;
- `shadow_rule_atlas_summary.md` — provenance and validation summary.

Generated artifacts belong under `artifacts/forensics/` and must never overwrite the source corpus.

## 8. What comes after the atlas

The correct order is:

1. validate the atlas against source hashes;
2. reconcile `ShadowSource.per` with `Shadow DC7.zip`;
3. build jump/control topology;
4. build goal/SN/timer data-flow;
5. build escrow interaction graph;
6. build progression/construction traces;
7. identify recurring control mechanisms;
8. only then define reconstruction code boundaries.

That is how we avoid the oldest AI-scripting mistake: writing a beautiful architecture around behavior that was never actually understood.
