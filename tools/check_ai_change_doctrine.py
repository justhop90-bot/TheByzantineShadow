#!/usr/bin/env python3
"""Fail CI when an AI-facing PR lacks the mandatory doctrine record."""
from __future__ import annotations

import json
import os
import subprocess
import sys

DOCTRINE = "docs/AI_SCRIPTER_OPERATING_DOCTRINE.md"
AI_PATHS = (
    "ShadowByzantine/",
    "ShadowByzantine.per",
    "ShadowSource.per",
    "docs/forensics/",
    "docs/architecture/",
    "docs/abi/",
    "tools/",
)
REQUIRED_HEADINGS = ("## Evidence", "## Verification", "## Uncertainty")


def run(*args: str) -> str:
    return subprocess.check_output(args, text=True).strip()


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path:
        print("AI doctrine gate: GITHUB_EVENT_PATH is required.", file=sys.stderr)
        return 2

    with open(event_path, encoding="utf-8") as fh:
        event = json.load(fh)

    pr = event.get("pull_request")
    if not pr:
        print("AI doctrine gate: not a pull-request event; nothing to enforce.")
        return 0

    base = pr["base"]["sha"]
    head = pr["head"]["sha"]
    changed = run("git", "diff", "--name-only", f"{base}...{head}").splitlines()
    ai_changed = [p for p in changed if p != DOCTRINE and any(p.startswith(x) or p.endswith(x) for x in AI_PATHS)]

    if not ai_changed:
        print("AI doctrine gate: no AI-facing files changed.")
        return 0

    body = pr.get("body") or ""
    failures = []

    if DOCTRINE not in body:
        failures.append(f"PR description must reference `{DOCTRINE}`.")

    missing = [h for h in REQUIRED_HEADINGS if h.lower() not in body.lower()]
    if missing:
        failures.append("PR description is missing required sections: " + ", ".join(missing))

    print("AI-facing changes detected:")
    for path in ai_changed:
        print(f"  - {path}")

    if failures:
        print("\nAI doctrine gate FAILED:", file=sys.stderr)
        for failure in failures:
            print(f"  - {failure}", file=sys.stderr)
        print("\nRequired PR record:\n", file=sys.stderr)
        print(f"Reference: `{DOCTRINE}`", file=sys.stderr)
        print("## Evidence\n## Verification\n## Uncertainty", file=sys.stderr)
        return 1

    print("AI doctrine gate PASSED: doctrine reference + Evidence + Verification + Uncertainty present.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
