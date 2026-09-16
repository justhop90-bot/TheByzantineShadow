#!/usr/bin/env python3
"""Generate the rule-level Shadow -> ShadowByzantine transplantation atlas.

The donor is parsed directly from ShadowSource.per.  No ordinals or offsets are
hard-coded.  The generated section is inserted into the existing
SHADOW_RULE_TRANSPLANTATION_MAP_v0.1.md between explicit markers.
"""
from __future__ import annotations

import pathlib
import re
from collections import Counter, defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[1]
DONOR = ROOT / "ShadowSource.per"
BYZ_ROOT = ROOT / "ShadowByzantine"
MAP = ROOT / "docs/forensics/SHADOW_RULE_TRANSPLANTATION_MAP_v0.1.md"
BEGIN = "<!-- BEGIN GENERATED RULE-LEVEL ATLAS -->"
END = "<!-- END GENERATED RULE-LEVEL ATLAS -->"

# These are source headings, not architectural inventions.  QTABLE/QRULES are
# navigation labels rather than control regions, so they are excluded.
EXCLUDE = {"QLOAD", "QVERSION", "QTEST", "QMISC STUFF", "QTABLE OF CONTENTS(QQ)",
           "QRULES", "QTIMERS", "QCONSTANTS"}


def strip_comment(line: str) -> str:
    out, quoted, esc = [], False, False
    for ch in line:
        if esc:
            out.append(ch); esc = False; continue
        if ch == "\\" and quoted:
            out.append(ch); esc = True; continue
        if ch == '"':
            quoted = not quoted; out.append(ch); continue
        if ch == ";" and not quoted:
            break
        out.append(ch)
    return "".join(out)


def balanced_end(lines, start):
    depth = 0; quoted = False; esc = False; comment = False
    for i in range(start, len(lines)):
        line = lines[i]
        comment = False
        for ch in line:
            if comment:
                continue
            if esc:
                esc = False; continue
            if ch == "\\" and quoted:
                esc = True; continue
            if ch == '"':
                quoted = not quoted; continue
            if ch == ";" and not quoted:
                comment = True; continue
            if quoted:
                continue
            if ch == "(": depth += 1
            elif ch == ")":
                depth -= 1
                if depth == 0:
                    return i
    raise ValueError(f"unbalanced rule at line {start+1}")


def extract_rules(text):
    lines = text.splitlines()
    rules = []
    headings = []
    for i, line in enumerate(lines):
        raw = line.strip()
        if raw.startswith(";"):
            h = re.sub(r"^;+\s*", "", raw)
            h = re.sub(r"^[#@>*-]+\s*", "", h).strip()
            m = re.search(r"\b(Q[A-Z0-9][A-Z0-9 _'()/-]*)\b", h)
            if m:
                name = m.group(1).strip()
                if name not in EXCLUDE:
                    headings.append((i + 1, name))
        if re.match(r"\s*\(defrule\b", line):
            end = balanced_end(lines, i)
            rules.append({"ordinal": len(rules)+1, "start": i+1, "end": end+1,
                          "text": "\n".join(lines[i:end+1])})
    # Associate each rule with the latest Q-heading.
    hp = 0
    for r in rules:
        while hp + 1 < len(headings) and headings[hp+1][0] <= r["start"]:
            hp += 1
        r["region"] = headings[hp][1] if headings and headings[hp][0] <= r["start"] else "UNHEADED"
    return rules, headings


def features(rule_text):
    code = strip_comments(rule_text).lower()
    toks = set(re.findall(r"[a-z][a-z0-9_-]*", code))
    states = set(re.findall(r"(?:goal|sn|timer|g:)\s+([a-z0-9_-]+)", code))
    writes = set()
    for m in re.finditer(r"\((set-goal|up-modify-goal|set-strategic-number|up-modify-sn)\s+([a-z0-9_-]+)", code):
        writes.add(m.group(2))
    ops = set()
    for op in ("up-jump-rule", "up-modify-escrow", "set-escrow-percentage", "release-escrow",
               "can-train-with-escrow", "can-research-with-escrow", "can-build-with-escrow",
               "up-train", "up-research", "up-build", "build", "research", "train",
               "up-full-reset-search", "up-find-local", "up-find-remote", "up-find-status-remote",
               "up-set-target-object", "up-set-target-point", "up-get-search-state",
               "up-clean-search", "up-remove-objects", "up-target-point", "up-target-objects",
               "up-assign-builders", "building-type-count-total", "unit-type-count-total",
               "research-completed", "research-pending", "enable-timer", "disable-timer",
               "disable-self"):
        if op in code: ops.add(op)
    commands = set(re.findall(r"\((up-(?:train|research|build|target-[a-z-]+)|build|train|research)\b", code))
    jumps = re.findall(r"\(up-jump-rule\s+(-?\d+)", code)
    timers = set(re.findall(r"(?:timer-triggered|up-timer-status|enable-timer|disable-timer)\s+([a-z0-9_-]+)", code))
    escrow = {x for x in ("up-modify-escrow", "set-escrow-percentage", "release-escrow",
                          "can-train-with-escrow", "can-research-with-escrow", "can-build-with-escrow") if x in code}
    search = {x for x in ("up-full-reset-search", "up-find-local", "up-find-remote", "up-find-status-remote",
                          "up-set-target-object", "up-set-target-point", "up-get-search-state",
                          "up-clean-search", "up-remove-objects") if x in code}
    observers = set()
    for x in ("building-type-count-total", "unit-type-count-total", "research-completed", "research-pending",
              "up-pending-objects", "up-pending-placement", "up-get-fact", "up-get-object-data", "up-get-search-state"):
        if x in code: observers.add(x)
    return {"tokens": toks, "states": states, "writes": writes, "ops": ops, "commands": commands,
            "jumps": jumps, "timers": timers, "escrow": escrow, "search": search, "observers": observers}


def normalized(text):
    return re.sub(r"\s+", " ", strip_comment(text)).strip().lower()


def load_byz():
    files = sorted(BYZ_ROOT.rglob("*.per"))
    all_rules = []
    for p in files:
        rs, _ = extract_rules(p.read_text(encoding="utf-8"))
        for r in rs:
            r["file"] = p.relative_to(ROOT).as_posix()
            r["features"] = features(r["text"])
            r["normalized"] = normalized(r["text"])
            all_rules.append(r)
    return all_rules


def score(a, b):
    # Mechanism-first similarity. State names are intentionally weighted more
    # heavily than generic tokens, while exact text gets a separate fast path.
    f1, f2 = a["features"], b["features"]
    score = 0.0
    for key, weight in (("ops", 5), ("writes", 4), ("escrow", 7), ("search", 4),
                        ("commands", 6), ("observers", 4), ("timers", 3), ("states", 2)):
        u = f1[key] | f2[key]
        if u: score += weight * len(f1[key] & f2[key]) / len(u)
    return score


def classify(donor, candidates):
    exact = [c for c in candidates if c["normalized"] == donor["normalized"]]
    if exact:
        # Exact source rule retained but moved into a module/file.
        return "PRESERVED" if any(c["file"] == "ShadowByzantine/ShadowByzantine.per" for c in exact) else "MOVED", exact[:3]
    ranked = sorted(((score(donor, c), c) for c in candidates), reverse=True, key=lambda x: x[0])
    strong = [c for s, c in ranked[:3] if s >= 8]
    if strong:
        # If the mechanism overlaps but object/state predicates differ, this is
        # adaptation/change rather than a claimed exact transplant.
        cls = "ADAPTED" if donor["features"]["commands"] & strong[0]["features"]["commands"] else "CHANGED"
        return cls, strong
    return "LOST", []


def fmtset(xs):
    return ", ".join(sorted(xs)) if xs else "—"


def main():
    donor_rules, headings = extract_rules(DONOR.read_text(encoding="utf-8"))
    byz_rules = load_byz()
    for r in donor_rules:
        r["features"] = features(r["text"])
        r["normalized"] = normalized(r["text"])
    generated = [BEGIN, "", "## Generated executable-mechanism atlas", "",
                 f"Generated directly from `ShadowSource.per` ({len(donor_rules)} rules) and "
                 f"the current `ShadowByzantine/**/*.per` tree ({len(byz_rules)} rules).",
                 "No donor ordinal or source offset is hard-coded in this artifact.", ""]
    generated += ["### A. Exact donor region boundaries", "",
                  "| Region | Donor ordinals | Donor source offsets |", "|---|---:|---|"]
    grouped = defaultdict(list)
    for r in donor_rules: grouped[r["region"]].append(r)
    for region, rs in grouped.items():
        generated.append(f"| {region} | {rs[0]['ordinal']}–{rs[-1]['ordinal']} | L{rs[0]['start']}–L{rs[-1]['end']} |")
    generated += ["", "### B. Region control inventory", "",
                  "| Region | Writers | Readers / state carriers | Timers | Jumps | Escrow | Search / placement | Commands | Observers | Re-entry topology |", "|---|---|---|---|---|---|---|---|---|---|"]
    for region, rs in grouped.items():
        fs = [r["features"] for r in rs]
        writers = set().union(*(x["writes"] for x in fs))
        states = set().union(*(x["states"] for x in fs))
        timers = set().union(*(x["timers"] for x in fs))
        jumps = []
        for r in rs:
            for j in r["features"]["jumps"]: jumps.append(f"{r['ordinal']}:{j}")
        esc = set().union(*(x["escrow"] for x in fs))
        search = set().union(*(x["search"] for x in fs))
        cmds = set().union(*(x["commands"] for x in fs))
        obs = set().union(*(x["observers"] for x in fs))
        reentry = []
        for r in rs:
            if r["features"]["jumps"]:
                reentry.append(f"R{r['ordinal']}→" + ",".join(r["features"]["jumps"]))
        generated.append(f"| {region} | {fmtset(writers)} | {fmtset(states)} | {fmtset(timers)} | {fmtset(jumps)} | {fmtset(esc)} | {fmtset(search)} | {fmtset(cmds)} | {fmtset(obs)} | {fmtset(reentry)} |")
    generated += ["", "### C. Donor-rule transplantation ledger", "",
                  "Each row is an executable donor rule. Current-rule references are only emitted where the current tree has a mechanism-level candidate; otherwise the rule is explicitly LOST. `UNKNOWN` is reserved for cases where static evidence is insufficient to distinguish two plausible mechanisms.", "",
                  "| Donor # | Source | Region | Predicate/state mechanism | Writers | Timers | Escrow | Search/placement | Commands/observers | Jump | Current candidate(s) | Classification |", "|---:|---|---|---|---|---|---|---|---|---|---|---|"]
    for d in donor_rules:
        cand = byz_rules
        cls, matches = classify(d, cand)
        f = d["features"]
        pred = strip_comment(d["text"]).split("=>", 1)[0].replace("\n", " ").strip()
        if len(pred) > 180: pred = pred[:177] + "..."
        mtxt = "; ".join(f"{c['file']}#{c['ordinal']}" for c in matches) or "—"
        generated.append(f"| {d['ordinal']} | L{d['start']}–L{d['end']} | {d['region']} | `{pred}` | {fmtset(f['writes'])} | {fmtset(f['timers'])} | {fmtset(f['escrow'])} | {fmtset(f['search'])} | {fmtset(f['commands'] | f['observers'])} | {fmtset(f['jumps'])} | {mtxt} | **{cls}** |")
    generated += ["", "### D. Current ShadowByzantine inventory", "",
                  "| File | Current rule | Mechanism | Candidate donor region(s) | Classification basis |", "|---|---:|---|---|---|"]
    donor_by_region = {k: v for k, v in grouped.items()}
    for c in byz_rules:
        ranked = sorted(((score(d, c), d) for d in donor_rules), reverse=True, key=lambda x: x[0])[:3]
        if c["normalized"] in {d["normalized"] for d in donor_rules}:
            cls = "PRESERVED/MOVED"
        elif ranked and ranked[0][0] >= 8:
            cls = "ADAPTED/CHANGED"
        else:
            cls = "ADDED/UNKNOWN"
        regs = ", ".join(sorted({d["region"] for s, d in ranked if s >= 8})) or "—"
        mech = fmtset(c["features"]["ops"] | c["features"]["commands"] | c["features"]["escrow"])
        generated.append(f"| `{c['file']}` | {c['ordinal']} | {mech} | {regs} | {cls} |")
    generated += ["", "### E. Generator invariants", "",
                  "1. Donor ordinals are assigned solely by source-order `defrule` extraction.",
                  "2. Donor offsets are the actual source line intervals in `ShadowSource.per`.",
                  "3. No conceptual subsystem name is used as a donor ordinal.",
                  "4. Exact rule text is required for PRESERVED/MOVED; mechanism overlap alone cannot promote to exact transplantation.",
                  "5. A candidate match is not runtime qualification and does not establish firing reachability.",
                  "6. Command issuance remains distinct from world-state completion.",
                  "", END]
    text = MAP.read_text(encoding="utf-8")
    block = "\n".join(generated)
    if BEGIN in text and END in text:
        pre = text.split(BEGIN, 1)[0].rstrip()
        post = text.split(END, 1)[1].lstrip()
        text = pre + "\n\n" + block + "\n" + post
    else:
        text = text.rstrip() + "\n\n" + block + "\n"
    MAP.write_text(text, encoding="utf-8")
    print(f"generated {len(donor_rules)} donor-rule rows and {len(byz_rules)} current-rule rows")


if __name__ == "__main__":
    main()
