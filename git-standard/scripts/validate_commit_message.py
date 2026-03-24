#!/usr/bin/env python3
"""
Validate Git commit messages in lightweight or Conventional Commit styles.
"""

from __future__ import annotations

import argparse
import json
import re
import sys


LIGHTWEIGHT_TYPES = {
    "fix",
    "add",
    "update",
    "style",
    "test",
    "revert",
    "build",
}

CONVENTIONAL_TYPES = {
    "feat",
    "fix",
    "docs",
    "style",
    "refactor",
    "perf",
    "test",
    "build",
    "ci",
    "chore",
    "revert",
}

LIGHTWEIGHT_PATTERN = re.compile(r"(?P<type>[a-z]+):\s+(?P<description>.+)")
CONVENTIONAL_PATTERN = re.compile(
    r"(?P<type>[a-z]+)(?:\((?P<scope>[a-z0-9][a-z0-9._/-]*)\))?(?P<breaking>!)?:\s+(?P<description>.+)"
)

AMBIGUOUS_DESCRIPTIONS = {
    "fix bug",
    "update code",
    "update",
    "modify",
    "changes",
    "修复",
    "修改",
    "更新",
    "调整",
    "优化",
}


def build_result(message: str, requested_style: str) -> dict[str, object]:
    return {
        "message": message,
        "requested_style": requested_style,
        "style": "",
        "valid": False,
        "type": "",
        "scope": "",
        "description": "",
        "breaking_change": False,
        "errors": [],
        "warnings": [],
    }


def add_description_warnings(result: dict[str, object], description: str, max_title_length: int) -> None:
    normalized_description = re.sub(r"\s+", " ", description.strip()).lower()
    if normalized_description in AMBIGUOUS_DESCRIPTIONS:
        result["warnings"].append("Description is too vague. Make the title more specific.")

    if len(description.strip()) < 4:
        result["warnings"].append("Description may be too short to be clear.")

    if len(result["message"]) > max_title_length:
        result["warnings"].append(
            f"Message is longer than {max_title_length} characters and may be too long for a clear title."
        )


def validate_lightweight(message: str, requested_style: str) -> dict[str, object]:
    result = build_result(message, requested_style)
    result["style"] = "lightweight"

    match = LIGHTWEIGHT_PATTERN.fullmatch(message)
    if not match:
        result["errors"].append("Message must match `type: description`.")
        return result

    commit_type = match.group("type")
    description = match.group("description")
    result["type"] = commit_type
    result["description"] = description

    if commit_type not in LIGHTWEIGHT_TYPES:
        result["errors"].append(
            "Unsupported lightweight type. Allowed types: " + ", ".join(sorted(LIGHTWEIGHT_TYPES))
        )

    if len(description.strip()) == 0:
        result["errors"].append("Description cannot be empty.")

    add_description_warnings(result, description, max_title_length=50)
    result["valid"] = len(result["errors"]) == 0
    return result


def validate_conventional(message: str, requested_style: str) -> dict[str, object]:
    result = build_result(message, requested_style)
    result["style"] = "conventional"

    match = CONVENTIONAL_PATTERN.fullmatch(message)
    if not match:
        result["errors"].append("Message must match `type(scope): description` or `type: description`.")
        return result

    commit_type = match.group("type")
    scope = match.group("scope") or ""
    description = match.group("description")
    breaking_change = bool(match.group("breaking"))

    result["type"] = commit_type
    result["scope"] = scope
    result["description"] = description
    result["breaking_change"] = breaking_change

    if commit_type not in CONVENTIONAL_TYPES:
        result["errors"].append(
            "Unsupported Conventional Commit type. Allowed types: "
            + ", ".join(sorted(CONVENTIONAL_TYPES))
        )

    if len(description.strip()) == 0:
        result["errors"].append("Description cannot be empty.")

    add_description_warnings(result, description, max_title_length=72)
    result["valid"] = len(result["errors"]) == 0
    return result


def choose_auto_style(message: str) -> str:
    conventional_match = CONVENTIONAL_PATTERN.fullmatch(message)
    if conventional_match:
        commit_type = conventional_match.group("type")
        scope = conventional_match.group("scope")
        breaking_change = conventional_match.group("breaking")
        if scope or breaking_change or commit_type in (CONVENTIONAL_TYPES - LIGHTWEIGHT_TYPES):
            return "conventional"

    lightweight_match = LIGHTWEIGHT_PATTERN.fullmatch(message)
    if lightweight_match and lightweight_match.group("type") in LIGHTWEIGHT_TYPES:
        return "lightweight"

    if conventional_match and conventional_match.group("type") in CONVENTIONAL_TYPES:
        return "conventional"

    return "lightweight"


def validate_message(message: str, style: str) -> dict[str, object]:
    trimmed = message.strip()
    if style == "auto":
        chosen_style = choose_auto_style(trimmed)
    else:
        chosen_style = style

    if "\n" in trimmed or "\r" in trimmed:
        result = build_result(trimmed, style)
        result["style"] = chosen_style
        result["errors"].append("Message title must be a single line.")
        return result

    if chosen_style == "conventional":
        return validate_conventional(trimmed, requested_style=style)
    return validate_lightweight(trimmed, requested_style=style)


def render_text(result: dict[str, object]) -> str:
    lines = [
        f"Message: {result['message']}",
        f"Requested style: {result['requested_style']}",
        f"Validated style: {result['style'] or '(none)'}",
        f"Valid: {'yes' if result['valid'] else 'no'}",
        f"Type: {result['type'] or '(none)'}",
        f"Scope: {result['scope'] or '(none)'}",
        f"Breaking change: {'yes' if result['breaking_change'] else 'no'}",
        f"Description: {result['description'] or '(none)'}",
    ]
    if result["errors"]:
        lines.append("Errors:")
        lines.extend(f"  - {item}" for item in result["errors"])
    if result["warnings"]:
        lines.append("Warnings:")
        lines.extend(f"  - {item}" for item in result["warnings"])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a Git commit message.")
    parser.add_argument("message", help="Commit message to validate.")
    parser.add_argument(
        "--style",
        choices=("auto", "lightweight", "conventional"),
        default="auto",
        help="Validation mode. `auto` prefers lightweight unless Conventional Commit-only syntax is present.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of text.")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    result = validate_message(args.message, style=args.style)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
    return 0 if result["valid"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
