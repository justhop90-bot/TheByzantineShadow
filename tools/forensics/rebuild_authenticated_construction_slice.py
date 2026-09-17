#!/usr/bin/env python3
from __future__ import annotations
import csv
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
IMPLEMENTATION = ROOT / "ShadowByzantine" / "04_construction.per"
INVENTORY = ROOT / "docs" / "forensics" / "SHADOW_BYZANTINE_CONSTRUCTION_TRANSPLANT_INVENTORY_v0.1.csv"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
EXPECTED_RULES = 1956
FIRST = 1794
LAST = 1949


def git_blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask(text: str) -> str:
    out = list(text)
    i = 0
    n = len(text)
    quoted = False
    escaped = False
    while i < n:
        c = text[i]
        if quoted:
            if c == "\\" and not escaped:
                out[i] = " "
                escaped = True
            elif c == '"' and not escaped:
                out[i] = " "
                quoted = False
                escaped = False
            else:
                if c not in "\r\n":
                    out[i] = " "
                escaped = False
            i += 1
            continue
        if c == '"':
            out[i] = " "
            quoted = True
            i += 1
            continue
        if c == ';':
            while i < n and text[i] not in "\r\n":
                out[i] = " "
                i += 1
            continue
        i += 1
    return "".join(out)


def extract_rules(text: str) -> list[str]:
    masked = mask(text)
    starts = [m.start() for m in re.finditer(r"\(defrule\b", masked)]
    rules = []
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
            raise RuntimeError(f"unbalanced defrule at byte offset {start}")
        rules.append(text[start:end])
    return rules


def normalized(rule: str) -> str:
    return re.sub(r"\s+", " ", mask(rule)).strip()


def rule_sha(rule: str) -> str:
    return hashlib.sha256(normalized(rule).encode()).hexdigest()


def jump_deltas(rule: str) -> list[int]:
    return [int(x) for x in re.findall(r"\(up-jump-rule\s+(-?\d+)\)", normalized(rule))]


def region(rule_id: int) -> str:
    if rule_id <= 1896:
        return "R07"
    if rule_id <= 1902:
        return "POST_R07_ADDITIONAL_MINING_CONSTRUCTION"
    if rule_id <= 1907:
        return "QUNIVERSITY"
    if rule_id <= 1912:
        return "QBALLISTICS"
    if rule_id == 1913:
        return "QEND"
    if rule_id <= 1915:
        return "QVERSION"
    if rule_id <= 1917:
        return "QMISC"
    if rule_id <= 1924:
        return "QENEMY_STRATEGY"
    if rule_id <= 1946:
        return "QEAGOL"
    return "QSPECIAL_TIMERS"


def main() -> None:
    source_bytes = SOURCE.read_bytes()
    donor_sha = git_blob_sha(source_bytes)
    if donor_sha != EXPECTED_BLOB:
        raise SystemExit(f"DONOR SHA MISMATCH: {donor_sha}")
    source_text = source_bytes.decode("utf-8")
    donor_rules = extract_rules(source_text)
    if len(donor_rules) != EXPECTED_RULES:
        raise SystemExit(f"DONOR RULE COUNT MISMATCH: {len(donor_rules)}")

    implementation_text = IMPLEMENTATION.read_text(encoding="utf-8")
    current_rules = extract_rules(implementation_text)
    if not current_rules:
        raise SystemExit("IMPLEMENTATION CONTAINS NO DEFRULE BLOCKS")

    donor_slice = donor_rules[FIRST - 1:LAST]
    expected_count = LAST - FIRST + 1
    if len(donor_slice) != expected_count:
        raise SystemExit("INTERNAL DONOR SLICE COUNT ERROR")

    first_rule_offset = mask(implementation_text).find("(defrule")
    if first_rule_offset < 0:
        raise SystemExit("IMPLEMENTATION FIRST DEFRULE NOT FOUND")
    prefix = implementation_text[:first_rule_offset]
    prefix = re.sub(r"; Implemented authenticated donor slices:.*\n", "; Authenticated donor interval: 1794-1949 (R07 1794-1896; post-R07 continuation 1897-1949)\n", prefix, count=1)
    prefix = re.sub(r"; Gap intentionally preserved:.*\n", "; No donor-rule gap inside the authenticated interval; 1806-1814 are QHOUSE donor rules and are restored at their actual IDs.\n", prefix, count=1)
    prefix = re.sub(r";   1794-1805 = farm progression\.\n;   1815-1827 = QHOUSE construction/control region\.\n;   1828-1849 = QLC lumber-camp construction/progression region\.\n", ";   1794-1805 = R07 farm progression.\n;   1806-1823 = R07 QHOUSE construction/control.\n;   1824-1858 = R07 QLC and construction/progression continuation.\n;   1859-1896 = R07 placement/search/construction continuation.\n;   1897-1949 = authenticated donor continuation beyond the R07 boundary.\n", prefix, count=1)
    generated = [prefix.rstrip(), "", "; ============================================================", "; AUTHENTICATED DONOR TRANSPLANT 1794-1949", "; Canonical donor blob SHA: 70a18a3b69e8ea46bd5132673fe9fcf8a36595ee", "; Rule bodies below are copied from the authenticated donor interval in", "; exact source order. Comments identify evidence only; they do not alter", "; donor semantics. Runtime qualification remains pending.", "; ============================================================", ""]
    for rid, rule in zip(range(FIRST, LAST + 1), donor_slice):
        generated.append(f"; AUTHENTICATED DONOR RULE {rid} | REGION={region(rid)} | BODY_SHA256={rule_sha(rule)}")
        generated.append(rule.rstrip())
        generated.append("")
    IMPLEMENTATION.write_text("\n".join(generated).rstrip() + "\n", encoding="utf-8")

    rebuilt = extract_rules(IMPLEMENTATION.read_text(encoding="utf-8"))
    if len(rebuilt) != expected_count:
        raise SystemExit(f"REBUILT RULE COUNT MISMATCH: {len(rebuilt)}")
    mismatches = [rid for rid, donor, impl in zip(range(FIRST, LAST + 1), donor_slice, rebuilt) if normalized(donor) != normalized(impl)]
    if mismatches:
        raise SystemExit(f"REBUILT RULE BODY MISMATCHES: {mismatches}")

    INVENTORY.parent.mkdir(parents=True, exist_ok=True)
    with INVENTORY.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh)
        writer.writerow(["rule_id", "region", "donor_blob_sha", "donor_rule_ordinal", "rule_body_sha256", "jump_deltas", "source_order", "evidence_class", "runtime_qualification"])
        for rid, rule in zip(range(FIRST, LAST + 1), donor_slice):
            writer.writerow([rid, region(rid), donor_sha, rid, rule_sha(rule), ";".join(map(str, jump_deltas(rule))) or "NONE", "DIRECT_DONOR_SOURCE_ORDER", "DIRECT_DONOR_TEXT", "PENDING"])

    print(f"AUTHENTICATED_DONOR_SHA={donor_sha}")
    print(f"DONOR_RULE_COUNT={len(donor_rules)}")
    print(f"IMPLEMENTED_RULE_INTERVAL={FIRST}-{LAST}")
    print(f"IMPLEMENTED_RULE_COUNT={len(rebuilt)}")
    print("RULE_BODY_EQUIVALENCE=PASS")
    print("NO_MISSING_RULES=PASS")
    print("NO_UNEXPECTED_RULES=PASS")
    print("SOURCE_ORDER=PASS")
    print("RUNTIME_QUALIFICATION=PENDING")


if __name__ == "__main__":
    main()

# Trigger authenticated rebuild workflow after workflow installation.
