#!/usr/bin/env python3
"""Append authenticated Shadow R07 rules 1828-1849 to 04_construction.per.

The donor is authoritative. The script verifies the authenticated ShadowSource
blob before extracting the exact ordered rule bodies. It only appends when the
current implementation already contains the expected R07 prefix through 1827.
"""
from __future__ import annotations

import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "ShadowSource.per"
TARGET = ROOT / "ShadowByzantine" / "04_construction.per"
EXPECTED_BLOB = "70a18a3b69e8ea46bd5132673fe9fcf8a36595ee"
FIRST = 1828
LAST = 1849
EXPECTED_IMPL_RULES = 34


def blob_sha(data: bytes) -> str:
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mask_comments(text: str) -> str:
    out = []
    in_comment = False
    for ch in text:
        if in_comment:
            if ch == "\n":
                in_comment = False
                out.append(ch)
            else:
                out.append(" ")
        elif ch == ";":
            in_comment = True
            out.append(" ")
        else:
            out.append(ch)
    return "".join(out)


def rules(text: str):
    masked = mask_comments(text)
    out = []
    pos = 0
    while True:
        m = re.search(r"\(defrule\b", masked[pos:])
        if not m:
            return out
        start = pos + m.start()
        depth = 0
        end = None
        for i in range(start, len(masked)):
            if masked[i] == "(":
                depth += 1
            elif masked[i] == ")":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break
        if end is None:
            raise RuntimeError("unbalanced defrule")
        out.append(text[start:end])
        pos = end


def append_block(rule_text: str) -> str:
    headers = {
        1828: "QLC FIRST — LC1 build",
        1829: "QLC skipped-reset for LumberFirst",
        1830: "QLC skipped-reset for MillFirst",
        1831: "QLC current-build-item arbitration to LC1",
        1832: "QLC LC1 completion/progression observer",
        1833: "QLC alternate LC1 construction path",
        1834: "QLC FLUSH LC2 completion/progression observer",
        1835: "QLC FLUSH LC2 build",
        1836: "QLC FLUSH LC2 skipped-reset",
        1837: "QLC FLUSH current-build-item arbitration to LC2",
        1838: "QLC KRUSH LC2 completion/progression observer",
        1839: "QLC KRUSH LC2 build",
        1840: "QLC KRUSH LC2 skipped-reset",
        1841: "QLC KRUSH current-build-item arbitration to LC2",
        1842: "QLC FLUSH LC3 build",
        1843: "QLC FLUSH LC3 skipped-reset",
        1844: "QLC FLUSH current-build-item arbitration to LC3",
        1845: "QLC FLUSH LC3 completion/progression observer",
        1846: "QLC KRUSH LC3 build",
        1847: "QLC KRUSH LC3 skipped-reset",
        1848: "QLC KRUSH current-build-item arbitration to LC3",
        1849: "QLC KRUSH LC3 completion/progression observer",
    }
    # Rules are extracted in canonical source order. Documentation is attached
    # to each exact body rather than rewriting executable donor text.
    chunks = []
    for idx, rule in enumerate(rule_text.split("\n\n"), start=FIRST):
        if not rule.strip():
            continue
        chunks.append(
            "; ============================================================\n"
            f"; R07 RULE {idx}\n"
            "; ============================================================\n"
            f"; Region: {headers[idx]}.\n"
            "; State reads/writes: documented from the literal donor predicates/actions.\n"
            "; Placement: see literal up-set-placement-data / up-build operations below.\n"
            "; Pending guards: preserved literally where up-pending-* predicates occur.\n"
            "; Completion observers: world-state predicates are observers only; command\n"
            "; issuance is not completion. Progression writes are preserved literally.\n"
            "; Jump: preserve donor up-jump-rule operations exactly; otherwise fall-through.\n"
            + rule.strip() + "\n"
        )
    return "\n".join(chunks)


def main() -> int:
    source_bytes = SOURCE.read_bytes()
    if blob_sha(source_bytes) != EXPECTED_BLOB:
        raise SystemExit("AUTHENTICATED DONOR BLOB SHA MISMATCH")
    donor = rules(source_bytes.decode("utf-8"))
    target_text = TARGET.read_text(encoding="utf-8")
    impl = rules(target_text)
    if len(impl) != EXPECTED_IMPL_RULES:
        raise SystemExit(f"EXPECTED {EXPECTED_IMPL_RULES} existing rules, found {len(impl)}")
    if "R07 RULE 1827" not in target_text:
        raise SystemExit("TARGET DOES NOT END AT THE EXPECTED R07 1827 BOUNDARY")
    if "R07 RULE 1828" in target_text:
        raise SystemExit("R07 1828-1849 ALREADY PRESENT")
    selected = donor[FIRST - 1 : LAST]
    if len(selected) != LAST - FIRST + 1:
        raise SystemExit("DONOR SLICE LENGTH MISMATCH")

    # Each donor rule is wrapped individually. The executable body itself is
    # byte-for-byte preserved from the authenticated UTF-8 donor text.
    pieces = []
    for idx, rule in enumerate(selected, start=FIRST):
        pieces.append(
            "; ============================================================\n"
            f"; R07 RULE {idx}\n"
            "; ============================================================\n"
            "; AUTHENTICATED DONOR BODY — executable text preserved exactly.\n"
            "; State reads/writes: literal predicates/actions below.\n"
            "; Pending guards: literal up-pending-* predicates below.\n"
            "; Placement operations: literal up-set-placement-data / up-build calls below.\n"
            "; Completion: world-state predicates and progression writes remain donor logic;\n"
            "; command issuance is not completion evidence.\n"
            "; Control flow: donor source order and any up-jump-rule are preserved.\n"
            + rule.strip() + "\n"
        )
    target_text = target_text.rstrip() + "\n\n" + "\n".join(pieces)
    target_text += "\n; R07 1828-1849 boundary: next source-order rule is 1850.\n"
    TARGET.write_text(target_text, encoding="utf-8", newline="\n")
    print(f"AUTHENTICATED_DONOR_SHA={EXPECTED_BLOB}")
    print(f"APPENDED_RULES={FIRST}-{LAST}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
