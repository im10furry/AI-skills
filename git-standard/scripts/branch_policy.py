#!/usr/bin/env python3
"""
Report whether merging into a target branch requires explicit user confirmation.
"""

from __future__ import annotations

import argparse
import json
import sys


def get_policy(target_branch: str) -> dict[str, object]:
    normalized = target_branch.strip()
    lowered = normalized.lower()

    requires_confirmation = lowered == "master"
    if lowered == "master":
        reason = "master is a protected merge target and requires explicit user confirmation."
    elif lowered == "develop":
        reason = "develop does not require extra confirmation after inspection and verification."
    else:
        reason = "No built-in special rule for this branch. State the assumption before merging."

    return {
        "target_branch": normalized,
        "requires_confirmation": requires_confirmation,
        "reason": reason,
    }


def render_text(policy: dict[str, object]) -> str:
    return "\n".join(
        [
            f"Target branch: {policy['target_branch']}",
            f"Requires confirmation: {'yes' if policy['requires_confirmation'] else 'no'}",
            f"Reason: {policy['reason']}",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Check whether a merge target requires explicit user confirmation.")
    parser.add_argument("target_branch", help="Branch name to evaluate.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of text.")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    policy = get_policy(args.target_branch)
    if args.json:
        print(json.dumps(policy, ensure_ascii=False, indent=2))
    else:
        print(render_text(policy))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
