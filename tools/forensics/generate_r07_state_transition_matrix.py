#!/usr/bin/env python3
"""Generate the authenticated R07 state-transition matrix keyed to the R07 edge matrix.

The edge matrix remains the authoritative CFG key. This generator attaches rule-local
state/effect observations to each edge without promoting them to runtime facts.

Evidence classes:
- DIRECT_DONOR_TEXT: literal predicate/action text extracted from ShadowSource.per.
- MECHANICALLY_DERIVED: values obtained by deterministic parsing/tokenization.
- MECHANICALLY_CLASSIFIED: semantic bucket assignment from parsed tokens.
- MECHANICALLY_DERIVED_SOURCE_ORDER: fall-through edge facts.
- UNCERTAIN: reserved for fields that cannot be established mechanically.
"""
from __future__ import annotations

import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
EDGE = ROOT / "docs" / "forensics" / "SHADOW_R07_EDGE_MATRIX_v0.1.csv"
OUT = ROOT / "docs" / "forensics" / "SHADOW_R07_STATE_TRANSITION_MATRIX_v0.1.csv"
EXPECTED_BLOB_SHA = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
R07_START = 1794
R07_END = 1896


def git_blob_sha(raw: bytes) -> str:
    return hashlib.sha1(f"blob {len(raw)}\0".encode() + raw).hexdigest()


def mask_source(text: str) -> str:
    out = list(text)
    i = 0
    n = len(text)
    in_string = False
    escaped = False
    while i < n:
        c = text[i]
        if in_string:
            if c == "\\" and not escaped:
                out[i] = " "
                escaped = True
            elif c == '"' and not escaped:
                out[i] = " "
                in_string = False
                escaped = False
            else:
                if c not in "\n\r":
                    out[i] = " "
                escaped = False
            i += 1
            continue
        if c == '"':
            out[i] = " "
            in_string = True
            i += 1
            continue
        if c == ';':
            while i < n and text[i] not in "\r\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return ''.join(out)


def parse_rules(text: str):
    masked = mask_source(text)
    starts = [m.start() for m in re.finditer(r'\(defrule\b', masked)]
    rules = []
    for rid, start in enumerate(starts, 1):
        depth = 0
        end = None
        for i in range(start, len(masked)):
            c = masked[i]
            if c == '(':
                depth += 1
            elif c == ')':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise SystemExit(f"unbalanced defrule #{rid}")
        raw = text[start:end]
        masked_raw = masked[start:end]
        line_start = text.count("\n", 0, start) + 1
        line_end = text.count("\n", 0, end) + 1
        rules.append((rid, line_start, line_end, raw, masked_raw))
    return rules


def split_halves(masked_body: str, raw_body: str):
    """Return predicate/action halves using the top-level => separator."""
    pos = masked_body.find("=>")
    if pos < 0:
        raise SystemExit("rule without =>")
    return raw_body[:pos], raw_body[pos + 2:]


def unique(seq):
    return sorted(set(seq))


def paren_forms(text: str, names: set[str] | None = None):
    """Extract balanced parenthesized forms, optionally filtered by first symbol."""
    masked = mask_source(text)
    forms = []
    starts = [m.start() for m in re.finditer(r'\(', masked)]
    for start in starts:
        depth = 0
        end = None
        for i in range(start, len(masked)):
            if masked[i] == '(':
                depth += 1
            elif masked[i] == ')':
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            continue
        form = text[start:end].strip()
        mm = re.match(r'\(\s*([^\s\)]+)', masked[start:end])
        if mm and (names is None or mm.group(1) in names):
            forms.append(form)
    return unique(forms)


def extract_state_reads(predicates: str):
    forms = paren_forms(predicates)
    out = []
    # Explicit goal predicates and comparisons.
    for f in forms:
        m = re.match(r'\(\s*goal\s+([^\s\)]+)', f)
        if m:
            out.append("goal:" + m.group(1))
            continue
        m = re.match(r'\(\s*up-compare-goal\s+([^\s\)]+)', f)
        if m:
            out.append("goal:" + m.group(1))
            continue
        m = re.match(r'\(\s*up-can-build\s+([^\s\)]+)', f)
        if m:
            out.append("goal:" + m.group(1))
    # Engine/state predicates that directly read persistent or world state.
    for token in re.findall(r'\b(?:current-age|game-time|wood-amount|housing-headroom|population-headroom|idle-farm-count|civilian-population|building-type-count(?:-total)?|up-pending-objects|up-pending-placement|up-research-status|can-build-with-escrow|can-build)\b[^\n\r\)]*', predicates):
        out.append(token.strip())
    # Strategic-number reads are represented as explicit function forms.
    for m in re.finditer(r'\((?:up-)?(?:compare-)?(?:strategic-number|sn-[^\s\)]*)[^\)]*\)', predicates):
        out.append(m.group(0).strip())
    return unique(out)


def extract_state_writes(actions: str):
    out = []
    patterns = [
        r'\(set-goal\s+([^\s\)]+)(?:\s+([^\)]*))?\)',
        r'\(up-modify-goal\s+([^\s\)]+)(?:\s+([^\)]*))?\)',
        r'\(set-strategic-number\s+([^\s\)]+)(?:\s+([^\)]*))?\)',
        r'\(disable-self\)',
    ]
    for p in patterns:
        for m in re.finditer(p, actions):
            out.append(m.group(0).strip())
    return unique(out)


def extract_escrow(actions: str):
    forms = paren_forms(actions, {"set-goal", "up-modify-escrow", "set-escrow-percentage", "release-escrow"})
    out = []
    for f in forms:
        if "gl-escrow-state" in f or f.startswith("(up-modify-escrow") or f.startswith("(set-escrow-percentage") or f.startswith("(release-escrow"):
            out.append(f)
    return unique(out)


def extract_commands(actions: str):
    names = {"up-build", "build", "up-assign-builders", "up-set-placement-data", "up-full-reset-search", "up-find-remote", "up-find-local", "up-get-point", "up-set-target-point"}
    return paren_forms(actions, names)


def extract_pending(predicates: str):
    return unique(paren_forms(predicates, {"up-pending-objects", "up-pending-placement"}))


def extract_milestones(predicates: str):
    forms = paren_forms(predicates)
    out = []
    for f in forms:
        if re.search(r'\bbuilding-type-count(?:-total)?\b', f):
            out.append(f)
        elif re.search(r'\b(?:housing-headroom|population-headroom|civilian-population|idle-farm-count)\b', f):
            # These are world/economy observations, but not construction completion milestones.
            if re.search(r'>=|<=|==|>|<|!=', f):
                out.append(f)
    return unique(out)


def evidence_list(values, classification=False):
    if not values:
        return "NONE"
    return "MECHANICALLY_CLASSIFIED" if classification else "DIRECT_DONOR_TEXT"


def load_edges():
    with EDGE.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 107:
        raise SystemExit(f"EDGE MATRIX CARDINALITY FAILURE: expected 107 rows, got {len(rows)}")
    return rows


def main():
    raw = SOURCE.read_bytes()
    actual = git_blob_sha(raw)
    if actual != EXPECTED_BLOB_SHA:
        raise SystemExit(f"AUTHENTICATION FAILURE: got {actual}, expected {EXPECTED_BLOB_SHA}")
    text = raw.decode("utf-8")
    rules = parse_rules(text)
    if len(rules) != 1956:
        raise SystemExit(f"DONOR RULE COUNT FAILURE: expected 1956, got {len(rules)}")
    by_id = {r[0]: r for r in rules}
    edges = load_edges()

    cache = {}
    for rid, line_start, line_end, raw_rule, masked_rule in rules:
        predicates, actions = split_halves(masked_rule, raw_rule)
        # Use masked halves only for token location-independent parsing; forms are extracted from raw halves.
        mp, ma = split_halves(masked_rule, masked_rule)
        cache[rid] = {
            "source_lines": f"{line_start}-{line_end}",
            "state_reads": extract_state_reads(predicates),
            "state_writes": extract_state_writes(actions),
            "escrow": extract_escrow(actions),
            "commands": extract_commands(actions),
            "pending": extract_pending(predicates),
            "milestones": extract_milestones(predicates),
        }

    fields = [
        "direction", "source_rule", "target_rule", "edge_kind", "jump_delta", "source_line",
        "source_region", "target_region", "cross_boundary",
        "source_fact_evidence", "target_resolution_evidence", "boundary_classification_evidence",
        "raw_jump_or_successor",
        "source_source_lines", "source_state_reads", "source_state_reads_evidence_class",
        "source_state_writes", "source_state_writes_evidence_class",
        "source_escrow_mutations", "source_escrow_mutations_evidence_class",
        "source_command_issuance", "source_command_issuance_evidence_class",
        "source_pending_object_guards", "source_pending_object_guards_evidence_class",
        "source_world_state_milestones", "source_world_state_milestones_evidence_class",
        "target_source_lines", "target_state_reads", "target_state_reads_evidence_class",
        "target_state_writes", "target_state_writes_evidence_class",
        "target_escrow_mutations", "target_escrow_mutations_evidence_class",
        "target_command_issuance", "target_command_issuance_evidence_class",
        "target_pending_object_guards", "target_pending_object_guards_evidence_class",
        "target_world_state_milestones", "target_world_state_milestones_evidence_class",
        "transition_state_effect", "transition_state_effect_evidence_class",
    ]

    out_rows = []
    for e in edges:
        sid = int(e["source_rule"])
        tid = int(e["target_rule"])
        s = cache[sid]
        t = cache[tid]
        def pack(key):
            return "; ".join(s[key]) if s[key] else "NONE"
        def pack_t(key):
            return "; ".join(t[key]) if t[key] else "NONE"
        source_effects = []
        if s["state_writes"]: source_effects.append("writes=" + "; ".join(s["state_writes"]))
        if s["escrow"]: source_effects.append("escrow=" + "; ".join(s["escrow"]))
        if s["commands"]: source_effects.append("commands=" + "; ".join(s["commands"]))
        effect = " | ".join(source_effects) if source_effects else "NONE"
        out_rows.append({
            **{k: e[k] for k in ["direction", "source_rule", "target_rule", "edge_kind", "jump_delta", "source_line", "source_region", "target_region", "cross_boundary", "source_fact_evidence", "target_resolution_evidence", "boundary_classification_evidence", "raw_jump_or_successor"]},
            "source_source_lines": s["source_lines"],
            "source_state_reads": pack("state_reads"),
            "source_state_reads_evidence_class": evidence_list(s["state_reads"]),
            "source_state_writes": pack("state_writes"),
            "source_state_writes_evidence_class": evidence_list(s["state_writes"]),
            "source_escrow_mutations": pack("escrow"),
            "source_escrow_mutations_evidence_class": evidence_list(s["escrow"]),
            "source_command_issuance": pack("commands"),
            "source_command_issuance_evidence_class": evidence_list(s["commands"]),
            "source_pending_object_guards": pack("pending"),
            "source_pending_object_guards_evidence_class": evidence_list(s["pending"]),
            "source_world_state_milestones": pack("milestones"),
            "source_world_state_milestones_evidence_class": evidence_list(s["milestones"]),
            "target_source_lines": t["source_lines"],
            "target_state_reads": pack_t("state_reads"),
            "target_state_reads_evidence_class": evidence_list(t["state_reads"]),
            "target_state_writes": pack_t("state_writes"),
            "target_state_writes_evidence_class": evidence_list(t["state_writes"]),
            "target_escrow_mutations": pack_t("escrow"),
            "target_escrow_mutations_evidence_class": evidence_list(t["escrow"]),
            "target_command_issuance": pack_t("commands"),
            "target_command_issuance_evidence_class": evidence_list(t["commands"]),
            "target_pending_object_guards": pack_t("pending"),
            "target_pending_object_guards_evidence_class": evidence_list(t["pending"]),
            "target_world_state_milestones": pack_t("milestones"),
            "target_world_state_milestones_evidence_class": evidence_list(t["milestones"]),
            "transition_state_effect": effect,
            "transition_state_effect_evidence_class": "MECHANICALLY_DERIVED" if effect != "NONE" else "NONE",
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(out_rows)

    print(f"authenticated_blob_sha={actual}")
    print(f"donor_rule_count={len(rules)}")
    print(f"edge_rows={len(edges)}")
    print(f"output={OUT}")


if __name__ == "__main__":
    main()
