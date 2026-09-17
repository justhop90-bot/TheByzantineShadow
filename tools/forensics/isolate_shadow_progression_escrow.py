#!/usr/bin/env python3
import csv, hashlib, json, re, sys
from pathlib import Path

SRC = Path(sys.argv[1] if len(sys.argv) > 1 else "ShadowSource.per")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else "shadow-progression-escrow-out")
OUT.mkdir(parents=True, exist_ok=True)
EXPECTED_GIT_BLOB_SHA = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
raw = SRC.read_bytes()
text = raw.decode("utf-8")
git_blob_sha = hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()
raw_sha = hashlib.sha1(raw).hexdigest()
if git_blob_sha != EXPECTED_GIT_BLOB_SHA:
    raise SystemExit(f"authenticated Git blob SHA mismatch: {git_blob_sha} != {EXPECTED_GIT_BLOB_SHA}")

TARGETS = [
    "gl-build-progress", "gl-current-build-item", "gl-progression-pause", "gl-strategy",
    "SPLIT", "set-escrow-percentage", "up-modify-escrow", "release-escrow", "disable-self",
    "gl-escrow-state", "gl-food-escrow", "gl-wood-escrow", "gl-gold-escrow", "gl-stone-escrow",
    "building-type-count", "building-type-count-total", "research-completed", "research-status",
    "research-available", "can-research-with-escrow", "can-build-with-escrow", "can-train-with-escrow",
    "can-research", "can-build", "can-train", "research-feasibility", "build-feasibility",
    "train-feasibility", "construction-completed", "building-completed", "research-completion",
    "research-completed", "train-completed", "build-completed"
]
TARGETS = list(dict.fromkeys(TARGETS))


def mask_source(s):
    out = list(s); i = 0; n = len(s); in_str = False; escaped = False
    while i < n:
        c = s[i]
        if in_str:
            if c == "\\" and not escaped:
                out[i] = " "; escaped = True
            elif c == '"' and not escaped:
                out[i] = " "; in_str = False; escaped = False
            else:
                if c not in "\r\n": out[i] = " "
                escaped = False
            i += 1; continue
        if c == '"': out[i] = " "; in_str = True; i += 1; continue
        if c == ';':
            while i < n and s[i] not in "\r\n": out[i] = " "; i += 1
            continue
        i += 1
    return "".join(out)

masked = mask_source(text)
starts = [m.start() for m in re.finditer(r"\(defrule\b", masked)]

def end_of_rule(start):
    depth = 0; i = start
    while i < len(masked):
        c = masked[i]
        if c == '(': depth += 1
        elif c == ')':
            depth -= 1
            if depth == 0: return i + 1
        i += 1
    raise ValueError(f"unbalanced defrule at char {start}")

def line(pos): return text.count("\n", 0, pos) + 1

def byte(pos): return len(text[:pos].encode("utf-8"))

def normalize(body):
    body = re.sub(r"\s+", " ", body).strip()
    m = re.match(r"^\(defrule\s*(.*?)\s*=>\s*(.*?)\)$", body, re.S)
    return (m.group(1).strip(), m.group(2).strip()) if m else (body, "")

rules = []
for ordinal, start in enumerate(starts, 1):
    end = end_of_rule(start)
    body = text[start:end]
    pred, actions = normalize(body)
    hits = [t for t in TARGETS if re.search(r"(?<![A-Za-z0-9_-])" + re.escape(t) + r"(?![A-Za-z0-9_-])", body)]
    jumps = re.findall(r"\(up-jump-rule\s+([^\)]+)\)", body)
    disable = bool(re.search(r"\(disable-self\b", actions))
    writers = [t for t in hits if re.search(r"(?<![A-Za-z0-9_-])" + re.escape(t) + r"(?![A-Za-z0-9_-])", actions)]
    readers = [t for t in hits if re.search(r"(?<![A-Za-z0-9_-])" + re.escape(t) + r"(?![A-Za-z0-9_-])", pred)]
    rules.append({
        "ordinal": ordinal,
        "byte_start": byte(start),
        "byte_end_exclusive": byte(end),
        "source_line_start": line(start),
        "source_line_end": line(end),
        "predicate": pred,
        "actions": actions,
        "jump_targets_raw": jumps,
        "fall_through_ordinal": ordinal + 1 if ordinal < len(starts) else None,
        "target_hits": hits,
        "writers": writers,
        "readers": readers,
        "disable_self": disable,
    })

if len(rules) != 1956:
    raise SystemExit(f"unexpected rule count: {len(rules)} != 1956")
by = {r["ordinal"]: r for r in rules}
edges = []
for r in rules:
    if r["fall_through_ordinal"] is not None:
        edges.append((r["ordinal"], r["fall_through_ordinal"], "fall-through", ""))
    for raw_delta in r["jump_targets_raw"]:
        delta = int(float(raw_delta)); target = r["ordinal"] + delta
        if not 1 <= target <= len(rules):
            raise SystemExit(f"out-of-range jump: {r['ordinal']} {delta} -> {target}")
        edges.append((r["ordinal"], target, "up-jump-rule", str(delta)))

seed = {r["ordinal"] for r in rules if r["target_hits"]}
# Dependency closure over the fixed progression/escrow vocabulary. This captures
# distributed readers/writers without allowing arbitrary symbol propagation.
changed = True
while changed:
    changed = False
    active_targets = set(t for o in seed for t in by[o]["target_hits"])
    for r in rules:
        if r["ordinal"] not in seed and active_targets.intersection(r["target_hits"]):
            seed.add(r["ordinal"]); changed = True

# Preserve control topology at the boundary: include immediate predecessors,
# successors, jump targets, and incoming jump sources for every semantic node.
node_set = set(seed)
for s, t, typ, delta in edges:
    if s in seed or t in seed:
        node_set.add(s); node_set.add(t)

# One additional boundary pass catches a jump/return edge introduced by the
# first context layer without turning the entire fall-through chain into the graph.
for s, t, typ, delta in edges:
    if s in node_set or t in node_set:
        if typ == "up-jump-rule":
            node_set.add(s); node_set.add(t)

sub_edges = [e for e in edges if e[0] in node_set or e[1] in node_set]

node_fields = ["ordinal", "byte_start", "byte_end_exclusive", "source_line_start", "source_line_end", "target_hits", "writers", "readers", "disable_self", "predicate", "actions"]
with (OUT / "ShadowSource_progression_escrow_nodes.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=node_fields); w.writeheader()
    for o in sorted(node_set):
        r = by[o].copy()
        r["target_hits"] = ";".join(r["target_hits"])
        r["writers"] = ";".join(r["writers"])
        r["readers"] = ";".join(r["readers"])
        w.writerow({k: r[k] for k in node_fields})

edge_fields = ["edge_id", "source_ordinal", "source_line_start", "source_line_end", "source_writers", "source_readers", "source_disable_self", "edge_type", "jump_delta", "target_ordinal", "target_line_start", "target_line_end", "target_hits"]
with (OUT / "ShadowSource_progression_escrow_graph.csv").open("w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=edge_fields); w.writeheader()
    for i, (s, t, typ, delta) in enumerate(sub_edges, 1):
        a, b = by[s], by[t]
        w.writerow({
            "edge_id": i, "source_ordinal": s, "source_line_start": a["source_line_start"], "source_line_end": a["source_line_end"],
            "source_writers": ";".join(a["writers"]), "source_readers": ";".join(a["readers"]), "source_disable_self": a["disable_self"],
            "edge_type": typ, "jump_delta": delta, "target_ordinal": t, "target_line_start": b["source_line_start"], "target_line_end": b["source_line_end"], "target_hits": ";".join(b["target_hits"])
        })

# State-centric index: each canonical target gets every reader/writer rule.
with (OUT / "ShadowSource_progression_escrow_state_index.csv").open("w", newline="", encoding="utf-8") as f:
    fields = ["state", "rule_ordinal", "role", "source_line_start", "source_line_end", "disable_self"]
    w = csv.DictWriter(f, fieldnames=fields); w.writeheader()
    for state in TARGETS:
        for r in rules:
            if state in r["writers"]:
                w.writerow({"state": state, "rule_ordinal": r["ordinal"], "role": "writer", "source_line_start": r["source_line_start"], "source_line_end": r["source_line_end"], "disable_self": r["disable_self"]})
            if state in r["readers"]:
                w.writerow({"state": state, "rule_ordinal": r["ordinal"], "role": "reader", "source_line_start": r["source_line_start"], "source_line_end": r["source_line_end"], "disable_self": r["disable_self"]})


def q(s): return '"' + str(s).replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n").replace("\r", "") + '"'
with (OUT / "ShadowSource_progression_escrow_graph.dot").open("w", encoding="utf-8") as f:
    f.write('digraph ShadowProgressionEscrow {\n  rankdir=LR;\n  graph [label="ShadowSource progression-escrow control/data graph", labelloc=t, fontsize=18];\n  node [shape=box, fontsize=8];\n')
    for o in sorted(node_set):
        r = by[o]
        label = f"R{o}\\nL{r['source_line_start']}-{r['source_line_end']}\\nB{r['byte_start']}-{r['byte_end_exclusive']}"
        if r["target_hits"]: label += "\\nSTATE: " + ",".join(r["target_hits"])
        if r["disable_self"]: label += "\\nDISABLE-SELF"
        f.write(f"  r{o} [label={q(label)}{',penwidth=2' if o in seed else ''}];\n")
    seen = set()
    for s, t, typ, delta in sub_edges:
        key = (s, t, typ)
        if key in seen: continue
        seen.add(key)
        attrs = ('style=bold,label=' + q('jump ' + delta)) if typ == 'up-jump-rule' else 'label="fall-through"'
        f.write(f"  r{s} -> r{t} [{attrs}];\n")
    f.write("}\n")

meta = {
    "expected_git_blob_sha1": EXPECTED_GIT_BLOB_SHA,
    "actual_git_blob_sha1": git_blob_sha,
    "raw_content_sha1": raw_sha,
    "byte_length": len(raw),
    "source_lines": text.count("\n") + 1,
    "rule_count": len(rules),
    "semantic_seed_rule_count": len([r for r in rules if r["target_hits"]]),
    "dependency_closure_rule_count": len(seed),
    "graph_node_count": len(node_set),
    "graph_edge_count": len(sub_edges),
    "jump_edges_in_graph": len([e for e in sub_edges if e[2] == "up-jump-rule"]),
    "fallthrough_edges_in_graph": len([e for e in sub_edges if e[2] == "fall-through"]),
    "disable_self_nodes": len([r for r in rules if r["ordinal"] in node_set and r["disable_self"]]),
    "target_vocabulary": TARGETS,
    "closure_definition": "all rules mentioning the fixed progression/escrow vocabulary, plus every control-flow endpoint touching that semantic closure; no arbitrary symbol expansion",
    "writer_reader_definition": "writer=state token appears in normalized action body; reader=state token appears in normalized predicate",
    "qualification": "DIRECT / STATIC / AUTHENTICATED; semantic role classification is heuristic and requires source-window review before implementation"
}
(OUT / "ShadowSource_progression_escrow_metadata.json").write_text(json.dumps(meta, indent=2), encoding="utf-8")
print(json.dumps(meta, indent=2))
