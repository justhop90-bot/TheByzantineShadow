# Consolidated Module Qualification Pipeline v0.1

Status: **ACTIVE STATIC QUALIFICATION INFRASTRUCTURE**

## Purpose

`tools/forensics/module_qualification.py` is the consolidated static qualification entrypoint for the ShadowByzantine reconstruction. It authenticates `ShadowSource.per`, parses every Byzantine implementation module, inventories repository constants, checks local jump topology, performs configured donor parity, compares principal state-touch counts, and emits machine-readable plus human-readable reports.

## Evidence boundary

The pipeline is intentionally conservative. It can establish source identity, syntactic balance, structural equivalence, static symbol/state relationships, and donor parity where a donor interval is explicitly established. It does **not** establish live AoE2DE command acceptance, pending-object validity, construction/research completion, progression advancement, runtime escrow release, recovery behavior, replay equivalence, or competitive performance.

## Invocation

```text
python tools/forensics/module_qualification.py \
  --config tools/forensics/module_qualification.json \
  --out artifacts/module-qualification
```

## Current authoritative donor

- `ShadowSource.per`
- Git blob SHA-1: `70a18a3b69e8ea46bd5132673fe9fcf8a36595ee`
- expected donor rule count: `1956`

## Per-module processing

For every `.per` file under `ShadowByzantine/`, the pipeline records:

1. implementation SHA-256;
2. rule count and parser balance;
3. local `up-jump-rule` edges and out-of-module targets;
4. repository-wide `defconst` inventory and duplicate-definition count;
5. unresolved state-symbol references for the conservative `gl-*`/principal-state audit;
6. donor interval and exact normalized rule-body parity when configured;
7. donor versus implementation jump topology;
8. donor versus implementation principal state-touch counts;
9. explicit static status;
10. runtime status fixed at `NOT_PROVEN` unless future runtime evidence is separately integrated.

## Donor mapping policy

A donor range must be established from canonical source/forensic evidence before being marked authoritative. The manifest currently contains the authenticated construction interval `1794-1949`. Other modules are still statically inventoried but are **not** automatically assigned historical donor ranges merely because their names appear architectural. This prevents the qualification system from converting current file boundaries into false donor evidence.

## Generated artifacts

```text
artifacts/module-qualification/
  MODULE_QUALIFICATION_REPORT.md
  donor_rule_index.json
  repository_symbol_index.json
  <module>.json
```

The artifacts are generated in CI rather than committed to the source tree. GitHub Actions uploads them as a workflow artifact and places the aggregate Markdown report in the Actions job summary.

## CI gate

`.github/workflows/module-qualification.yml` runs on pushes to `main`, pull requests affecting donor/implementation/forensic files, and manual dispatch. A static failure causes the job to fail; reports are uploaded with `if: always()` so failures remain inspectable.

## Promotion model

```text
STATIC FORENSIC EXTRACTION
        ↓
STATIC DONOR EQUIVALENCE (where directly mapped)
        ↓
RUNTIME CANDIDATE
        ↓
RUNTIME QUALIFICATION
```

The pipeline deliberately does not collapse these evidence classes. Runtime promotion remains governed by the construction and escrow runtime/replay qualification matrices.

## Relationship to existing forensic tools

This pipeline consolidates recurring qualification concerns; it does not invalidate the existing specialized forensic scripts. Specialized scripts remain authoritative when they implement a stricter or historically specific proof. In particular, the authenticated construction interval qualifier remains the stronger construction-specific equivalence check until the consolidated pipeline reaches feature parity with it.
