# Shadow jump/fall-through graph resolution v0.1

## Authority
- Source: authenticated `ShadowSource.per` Git blob `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`.
- Raw-content SHA-1: `319c7769a08a6045ee09528da2bf4a47318010fc`.
- Authenticated source size: 615,773 bytes; 1,956 `defrule` records.

## Mechanical resolution
The AoE scripting reference defines `up-jump-rule` as a signed delta within the current rule set. Therefore the forensic ordinal mapping is:

`jump_target_ordinal = source_ordinal + signed_operand`

Fall-through is the next rule ordinal:

`fall_through_ordinal = source_ordinal + 1`

The terminal rule (1956) has no fall-through edge. All 188 jump operands resolve inside ordinals 1–1956; no out-of-range edge exists.

## Outputs
- Full graph: every rule's fall-through edge plus all 188 explicit jump edges.
- Targeted subgraph: every rule touching the donor control set (`gl-build-progress`, `gl-current-build-item`, `gl-progression-pause`, `gl-strategy`, `SPLIT`, escrow mutation/release, `disable-self`, and completion/feasibility observers), plus one-hop jump/fall-through context endpoints.

No ABI, runtime implementation, or donor semantics were changed by this extraction.
