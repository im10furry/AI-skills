#!/usr/bin/env python3
"""
Summarize the state of a Git repository in a deterministic, UTF-8-safe format.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


GIT_BASE_COMMAND = [
    "git",
    "-c",
    "core.quotepath=false",
    "-c",
    "i18n.logOutputEncoding=utf8",
]

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

CONVENTIONAL_PATTERN = re.compile(
    r"(?P<type>[a-z]+)(?:\((?P<scope>[a-z0-9][a-z0-9._/-]*)\))?(?P<breaking>!)?:\s+(?P<description>.+)"
)
LIGHTWEIGHT_PATTERN = re.compile(r"(?P<type>[a-z]+):\s+(?P<description>.+)")


def run_git(repo: Path, *args: str, check: bool = True) -> str:
    completed = subprocess.run(
        [*GIT_BASE_COMMAND, "-C", str(repo), *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if check and completed.returncode != 0:
        message = completed.stderr.strip() or completed.stdout.strip() or "git command failed"
        raise RuntimeError(message)
    return completed.stdout.strip()


def optional_git(repo: Path, *args: str) -> str:
    try:
        return run_git(repo, *args)
    except RuntimeError:
        return ""


def parse_status_porcelain(output: str) -> tuple[dict[str, object], dict[str, int]]:
    branch = {
        "head": "",
        "upstream": "",
        "ahead": 0,
        "behind": 0,
    }
    counts = {
        "staged": 0,
        "unstaged": 0,
        "untracked": 0,
        "conflicted": 0,
    }

    for line in output.splitlines():
        if line.startswith("# branch.head "):
            branch["head"] = line.removeprefix("# branch.head ")
            continue
        if line.startswith("# branch.upstream "):
            branch["upstream"] = line.removeprefix("# branch.upstream ")
            continue
        if line.startswith("# branch.ab "):
            parts = line.split()
            if len(parts) >= 4:
                branch["ahead"] = int(parts[2].removeprefix("+"))
                branch["behind"] = int(parts[3].removeprefix("-"))
            continue
        if line.startswith("? "):
            counts["untracked"] += 1
            continue
        if line.startswith("u "):
            counts["conflicted"] += 1
            continue
        if line.startswith(("1 ", "2 ")):
            fields = line.split(" ", 4)
            if len(fields) >= 2:
                xy = fields[1]
                if len(xy) == 2:
                    if xy[0] != ".":
                        counts["staged"] += 1
                    if xy[1] != ".":
                        counts["unstaged"] += 1

    return branch, counts


def detect_in_progress_operations(repo: Path) -> list[str]:
    git_dir_text = run_git(repo, "rev-parse", "--git-dir")
    git_dir = Path(git_dir_text)
    if not git_dir.is_absolute():
        git_dir = (repo / git_dir).resolve()

    operations = []
    if (git_dir / "MERGE_HEAD").exists():
        operations.append("merge")
    if (git_dir / "rebase-merge").exists() or (git_dir / "rebase-apply").exists():
        operations.append("rebase")
    if (git_dir / "CHERRY_PICK_HEAD").exists():
        operations.append("cherry-pick")
    if (git_dir / "REVERT_HEAD").exists():
        operations.append("revert")
    if (git_dir / "BISECT_LOG").exists():
        operations.append("bisect")
    return operations


def get_recent_commits(repo: Path, limit: int) -> list[dict[str, str]]:
    output = optional_git(
        repo,
        "log",
        f"--max-count={limit}",
        "--date=short",
        "--pretty=format:%H%x09%h%x09%ad%x09%d%x09%s",
    )
    commits = []
    for line in output.splitlines():
        full_sha, short_sha, date, decorations, subject = (line.split("\t", 4) + ["", "", "", "", ""])[:5]
        commits.append(
            {
                "sha": full_sha,
                "short_sha": short_sha,
                "date": date,
                "decorations": decorations.strip(),
                "subject": subject,
            }
        )
    return commits


def classify_subject_language(subject: str) -> str:
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


def classify_subject_format(subject: str) -> str:
    conventional_match = CONVENTIONAL_PATTERN.fullmatch(subject)
    if conventional_match:
        commit_type = conventional_match.group("type")
        scope = conventional_match.group("scope")
        breaking_change = conventional_match.group("breaking")
        if commit_type in CONVENTIONAL_TYPES:
            if scope or breaking_change or commit_type in (CONVENTIONAL_TYPES - LIGHTWEIGHT_TYPES):
                return "conventional"
            if commit_type in (CONVENTIONAL_TYPES & LIGHTWEIGHT_TYPES):
                return "shared-colon"

    lightweight_match = LIGHTWEIGHT_PATTERN.fullmatch(subject)
    if lightweight_match and lightweight_match.group("type") in LIGHTWEIGHT_TYPES:
        if lightweight_match.group("type") in (LIGHTWEIGHT_TYPES & CONVENTIONAL_TYPES):
            return "shared-colon"
        return "lightweight"

    return "other"


def summarize_commit_languages(commits: list[dict[str, str]]) -> dict[str, object]:
    counts = {
        "chinese": 0,
        "english": 0,
        "mixed": 0,
        "other": 0,
    }
    for commit in commits:
        language = classify_subject_language(commit["subject"])
        commit["language"] = language
        counts[language] += 1

    total = len(commits)
    dominant_language = "unknown"
    confidence = 0.0
    if total:
        highest = max(counts.values())
        tied = [language for language, count in counts.items() if count == highest and count > 0]
        dominant_language = tied[0] if len(tied) == 1 else "mixed-convention"
        confidence = round(highest / total, 2)

    return {
        "counts": counts,
        "dominant_language": dominant_language,
        "confidence": confidence,
        "sample_size": total,
    }


def summarize_commit_formats(commits: list[dict[str, str]]) -> dict[str, object]:
    counts = {
        "lightweight": 0,
        "conventional": 0,
        "shared-colon": 0,
        "other": 0,
    }
    for commit in commits:
        commit_format = classify_subject_format(commit["subject"])
        commit["format"] = commit_format
        counts[commit_format] += 1

    total = len(commits)
    dominant_format = "unknown"
    confidence = 0.0
    if total:
        highest = max(counts.values())
        tied = [item for item, count in counts.items() if count == highest and count > 0]
        dominant_format = tied[0] if len(tied) == 1 else "mixed-convention"
        confidence = round(highest / total, 2)

    return {
        "counts": counts,
        "dominant_format": dominant_format,
        "confidence": confidence,
        "sample_size": total,
    }


def get_remotes(repo: Path) -> list[dict[str, str]]:
    output = optional_git(repo, "remote", "-v")
    remotes = []
    seen = set()
    for line in output.splitlines():
        match = re.match(r"^(\S+)\s+(.+)\s+\((fetch|push)\)$", line)
        if not match:
            continue
        name, url, direction = match.groups()
        key = (name, url, direction)
        if key in seen:
            continue
        seen.add(key)
        remotes.append(
            {
                "name": name,
                "url": url,
                "direction": direction,
            }
        )
    return remotes


def get_stashes(repo: Path, limit: int) -> list[str]:
    output = optional_git(repo, "stash", "list")
    return output.splitlines()[:limit] if output else []


def build_snapshot(repo: Path, commit_limit: int) -> dict[str, object]:
    repo_root = Path(run_git(repo, "rev-parse", "--show-toplevel")).resolve()
    branch_name = optional_git(repo_root, "branch", "--show-current")
    head_short = optional_git(repo_root, "rev-parse", "--short", "HEAD")
    upstream = optional_git(repo_root, "rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}")
    divergence = optional_git(repo_root, "rev-list", "--left-right", "--count", "@{upstream}...HEAD") if upstream else ""
    status_porcelain = run_git(repo_root, "status", "--porcelain=2", "--branch")
    status_short = optional_git(repo_root, "status", "--short")
    branch_info, change_counts = parse_status_porcelain(status_porcelain)
    operations = detect_in_progress_operations(repo_root)

    ahead = 0
    behind = 0
    if divergence:
        parts = divergence.split()
        if len(parts) == 2:
            behind = int(parts[0])
            ahead = int(parts[1])

    branch_display = branch_name or f"detached at {head_short or 'unknown'}"
    upstream_display = upstream or branch_info["upstream"] or ""
    snapshot = {
        "repo_root": str(repo_root),
        "branch": branch_display,
        "head": branch_info["head"] or branch_display,
        "upstream": upstream_display,
        "ahead": ahead or int(branch_info["ahead"]),
        "behind": behind or int(branch_info["behind"]),
        "operations": operations,
        "dirty": bool(status_short),
        "change_counts": change_counts,
        "status_lines": status_short.splitlines() if status_short else [],
        "remotes": get_remotes(repo_root),
        "recent_commits": get_recent_commits(repo_root, commit_limit),
        "stashes": get_stashes(repo_root, min(commit_limit, 5)),
    }
    snapshot["commit_language"] = summarize_commit_languages(snapshot["recent_commits"])
    snapshot["commit_format"] = summarize_commit_formats(snapshot["recent_commits"])
    return snapshot


def render_text(snapshot: dict[str, object]) -> str:
    change_counts = snapshot["change_counts"]
    lines = [
        f"Repository: {snapshot['repo_root']}",
        f"Branch: {snapshot['branch']}",
        f"Upstream: {snapshot['upstream'] or '(none)'}",
        f"Ahead/Behind: {snapshot['ahead']}/{snapshot['behind']}",
        f"Dirty: {'yes' if snapshot['dirty'] else 'no'}",
        (
            "Changes: "
            f"staged={change_counts['staged']} "
            f"unstaged={change_counts['unstaged']} "
            f"untracked={change_counts['untracked']} "
            f"conflicted={change_counts['conflicted']}"
        ),
        f"Operations: {', '.join(snapshot['operations']) if snapshot['operations'] else 'none'}",
    ]
    commit_language = snapshot["commit_language"]
    lines.append(
        "Commit language: "
        f"{commit_language['dominant_language']} "
        f"(confidence={commit_language['confidence']}, sample={commit_language['sample_size']})"
    )
    lines.append(
        "Commit language counts: "
        f"chinese={commit_language['counts']['chinese']} "
        f"english={commit_language['counts']['english']} "
        f"mixed={commit_language['counts']['mixed']} "
        f"other={commit_language['counts']['other']}"
    )
    commit_format = snapshot["commit_format"]
    lines.append(
        "Commit format: "
        f"{commit_format['dominant_format']} "
        f"(confidence={commit_format['confidence']}, sample={commit_format['sample_size']})"
    )
    lines.append(
        "Commit format counts: "
        f"lightweight={commit_format['counts']['lightweight']} "
        f"conventional={commit_format['counts']['conventional']} "
        f"shared-colon={commit_format['counts']['shared-colon']} "
        f"other={commit_format['counts']['other']}"
    )

    status_lines = snapshot["status_lines"]
    lines.append("Status:")
    if status_lines:
        lines.extend(f"  {line}" for line in status_lines)
    else:
        lines.append("  (clean)")

    remotes = snapshot["remotes"]
    lines.append("Remotes:")
    if remotes:
        for remote in remotes:
            lines.append(f"  {remote['name']} [{remote['direction']}]: {remote['url']}")
    else:
        lines.append("  (none)")

    recent_commits = snapshot["recent_commits"]
    lines.append("Recent commits:")
    if recent_commits:
        for commit in recent_commits:
            decorations = f" {commit['decorations']}" if commit["decorations"] else ""
            language = f" [{commit['language']}]" if commit.get("language") else ""
            commit_format_label = f" [{commit['format']}]" if commit.get("format") else ""
            lines.append(
                f"  {commit['short_sha']}{language}{commit_format_label} {commit['date']}{decorations} {commit['subject']}".rstrip()
            )
    else:
        lines.append("  (no commits)")

    stashes = snapshot["stashes"]
    lines.append("Stashes:")
    if stashes:
        lines.extend(f"  {line}" for line in stashes)
    else:
        lines.append("  (none)")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Print a concise snapshot of a Git repository.")
    parser.add_argument("repo", nargs="?", default=".", help="Path to a Git repository. Defaults to the current directory.")
    parser.add_argument("--commits", type=int, default=8, help="Number of recent commits to include.")
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of text.")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    repo = Path(args.repo).resolve()

    try:
        snapshot = build_snapshot(repo, max(args.commits, 1))
    except RuntimeError as exc:
        print(f"git_snapshot.py: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(snapshot, ensure_ascii=False, indent=2))
    else:
        print(render_text(snapshot))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
