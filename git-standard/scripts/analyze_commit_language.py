#!/usr/bin/env python3
"""
Analyze recent Git commit subjects and infer the dominant message language convention.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path


GIT_BASE_COMMAND = [
    "git",
    "-c",
    "core.quotepath=false",
    "-c",
    "i18n.logOutputEncoding=utf8",
]


def run_git(repo: Path, *args: str) -> str:
    completed = subprocess.run(
        [*GIT_BASE_COMMAND, "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip() or "git command failed"
        raise RuntimeError(message)
    return completed.stdout.strip()


def classify_subject(subject: str) -> str:
    han_count = sum(1 for char in subject if "\u4e00" <= char <= "\u9fff")
    latin_words = re.findall(r"[A-Za-z]+", subject)
    latin_word_count = len(latin_words)
    if han_count and not latin_word_count:
        return "chinese"
    if latin_word_count and not han_count:
        return "english"
    if han_count and latin_word_count:
        if han_count >= 2 and latin_word_count <= 1:
            return "chinese"
        if latin_word_count >= 2 and han_count <= 1:
            return "english"
        return "mixed"
    return "other"


def get_commits(repo: Path, limit: int) -> list[dict[str, str]]:
    output = run_git(
        repo,
        "log",
        f"--max-count={limit}",
        "--no-merges",
        "--date=short",
        "--pretty=format:%H%x09%h%x09%ad%x09%s",
    )
    commits = []
    for line in output.splitlines():
        full_sha, short_sha, date, subject = (line.split("\t", 3) + ["", "", "", ""])[:4]
        commits.append(
            {
                "sha": full_sha,
                "short_sha": short_sha,
                "date": date,
                "subject": subject,
                "language": classify_subject(subject),
            }
        )
    return commits


def summarize(commits: list[dict[str, str]]) -> dict[str, object]:
    counts = Counter(commit["language"] for commit in commits)
    ranked = counts.most_common()
    dominant = ranked[0][0] if ranked else "unknown"
    total = len(commits)
    confidence = 0.0
    if total and ranked:
        top_count = ranked[0][1]
        tied = [language for language, count in ranked if count == top_count]
        if len(tied) > 1:
            dominant = "mixed-convention"
        confidence = round(top_count / total, 2)
    return {
        "total_commits": total,
        "counts": dict(counts),
        "dominant_language": dominant,
        "confidence": confidence,
        "commits": commits,
    }


def render_text(summary: dict[str, object]) -> str:
    counts = summary["counts"]
    lines = [
        f"Analyzed commits: {summary['total_commits']}",
        (
            "Language counts: "
            f"chinese={counts.get('chinese', 0)} "
            f"english={counts.get('english', 0)} "
            f"mixed={counts.get('mixed', 0)} "
            f"other={counts.get('other', 0)}"
        ),
        f"Dominant language: {summary['dominant_language']}",
        f"Confidence: {summary['confidence']}",
        "Recent subjects:",
    ]
    for commit in summary["commits"]:
        lines.append(f"  {commit['short_sha']} [{commit['language']}] {commit['subject']}")
    if not summary["commits"]:
        lines.append("  (no commits)")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Infer whether recent Git commit messages are mostly Chinese or English.")
    parser.add_argument("repo", nargs="?", default=".", help="Path to a Git repository. Defaults to the current directory.")
    parser.add_argument("--commits", type=int, default=30, help="Number of recent non-merge commits to inspect.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of text.")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    repo = Path(args.repo).resolve()

    try:
        repo_root = Path(run_git(repo, "rev-parse", "--show-toplevel")).resolve()
        commits = get_commits(repo_root, max(args.commits, 1))
        summary = summarize(commits)
        summary["repo_root"] = str(repo_root)
    except RuntimeError as exc:
        print(f"analyze_commit_language.py: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(summary, ensure_ascii=False, indent=2))
    else:
        print(render_text(summary))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
