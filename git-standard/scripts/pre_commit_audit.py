#!/usr/bin/env python3
"""
Audit changed Git paths for common pre-commit risks.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path, PurePosixPath


GIT_BASE_COMMAND = [
    "git",
    "-c",
    "core.quotepath=false",
    "-c",
    "i18n.logOutputEncoding=utf8",
]

GENERATED_DIRS = {
    "node_modules",
    "dist",
    "build",
    "coverage",
    ".next",
    ".nuxt",
    ".svelte-kit",
    ".parcel-cache",
    ".cache",
    ".turbo",
    "target",
    "out",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    "obj",
}

SECRET_TEXT_PATTERNS = [
    (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "Private key material detected in file content."),
    (re.compile(r"\bAKIA[0-9A-Z]{16}\b"), "AWS access key pattern detected in file content."),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"), "GitHub token pattern detected in file content."),
    (re.compile(r"\bgithub_pat_[A-Za-z0-9_]{20,}\b"), "GitHub fine-grained token pattern detected in file content."),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b"), "Slack token pattern detected in file content."),
    (re.compile(r"\bAIza[0-9A-Za-z\-_]{35}\b"), "Google API key pattern detected in file content."),
    (re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b"), "Stripe live secret key pattern detected in file content."),
]


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
    return completed.stdout


def get_repo_root(repo: Path) -> Path:
    return Path(run_git(repo, "rev-parse", "--show-toplevel").strip()).resolve()


def list_paths(repo: Path, scope: str) -> list[str]:
    paths: set[str] = set()

    if scope in {"staged", "all"}:
        staged = run_git(repo, "diff", "--cached", "--name-only", "--diff-filter=ACMR", "-z")
        paths.update(path for path in staged.split("\0") if path)

    if scope == "all":
        unstaged = run_git(repo, "diff", "--name-only", "--diff-filter=ACMR", "-z")
        untracked = run_git(repo, "ls-files", "--others", "--exclude-standard", "-z")
        paths.update(path for path in unstaged.split("\0") if path)
        paths.update(path for path in untracked.split("\0") if path)

    return sorted(paths)


def is_secret_like_name(path: PurePosixPath) -> str:
    name = path.name.lower()
    full_path = path.as_posix().lower()

    safe_env_names = {
        ".env.example",
        ".env.sample",
        ".env.template",
        ".env.defaults",
    }
    if name.startswith(".env") and name not in safe_env_names:
        return "Environment file is likely to contain machine-local or secret values."

    if name in {"id_rsa", "id_dsa", "id_ed25519"}:
        return "Private SSH key file should not be committed."

    if name.endswith((".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".ovpn")):
        return "Key or certificate file looks secret-bearing."

    if name == "credentials.json" or name.startswith(("service-account", "service_account")) and name.endswith(".json"):
        return "Credentials or service-account JSON file looks secret-bearing."

    if "secret" in name or "secrets" in name:
        return "Filename suggests the file may store secrets."

    if full_path.endswith("/.npmrc") or full_path.endswith("/.pypirc"):
        return "Package registry credential file may contain tokens."

    return ""


def is_generated_path(path: PurePosixPath) -> str:
    for part in path.parts[:-1]:
        if part.lower() in GENERATED_DIRS:
            return "Path lives inside a common generated-output directory."

    lowered_name = path.name.lower()
    if lowered_name.endswith((".min.js", ".bundle.js", ".map", ".pyc", ".class", ".o", ".so", ".dll", ".exe", ".jar")):
        return "Filename looks like generated or compiled output."

    return ""


def staged_text(repo: Path, path: str, scope: str) -> str:
    if scope == "staged":
        completed = subprocess.run(
            [*GIT_BASE_COMMAND, "-C", str(repo), "show", f":{path}"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        if completed.returncode == 0:
            return completed.stdout[:200000]

    candidate = repo / Path(path)
    if not candidate.exists() or not candidate.is_file():
        return ""

    try:
        return candidate.read_text(encoding="utf-8", errors="replace")[:200000]
    except OSError:
        return ""


def inspect_path(repo: Path, path_text: str, scope: str, max_bytes: int) -> list[dict[str, str]]:
    path = PurePosixPath(path_text.replace("\\", "/"))
    findings: list[dict[str, str]] = []

    secret_reason = is_secret_like_name(path)
    if secret_reason:
        findings.append(
            {
                "severity": "high",
                "category": "secret-name",
                "path": path.as_posix(),
                "reason": secret_reason,
            }
        )

    generated_reason = is_generated_path(path)
    if generated_reason:
        findings.append(
            {
                "severity": "warning",
                "category": "generated-output",
                "path": path.as_posix(),
                "reason": generated_reason,
            }
        )

    candidate = repo / Path(path.as_posix())
    if candidate.exists() and candidate.is_file():
        try:
            size = candidate.stat().st_size
        except OSError:
            size = 0
        if size > max_bytes:
            findings.append(
                {
                    "severity": "warning",
                    "category": "large-file",
                    "path": path.as_posix(),
                    "reason": f"File is larger than {max_bytes} bytes and may be accidental commit material.",
                }
            )

    content = staged_text(repo, path.as_posix(), scope)
    if content:
        for pattern, reason in SECRET_TEXT_PATTERNS:
            if pattern.search(content):
                findings.append(
                    {
                        "severity": "high",
                        "category": "secret-content",
                        "path": path.as_posix(),
                        "reason": reason,
                    }
                )

    deduped: list[dict[str, str]] = []
    seen: set[tuple[str, str, str]] = set()
    for finding in findings:
        key = (finding["severity"], finding["category"], finding["path"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(finding)
    return deduped


def audit_repo(repo: Path, scope: str, max_bytes: int) -> dict[str, object]:
    repo_root = get_repo_root(repo)
    paths = list_paths(repo_root, scope=scope)
    findings: list[dict[str, str]] = []
    for path in paths:
        findings.extend(inspect_path(repo_root, path, scope=scope, max_bytes=max_bytes))

    blockers = [item for item in findings if item["severity"] == "high"]
    warnings = [item for item in findings if item["severity"] != "high"]
    status = "clean"
    if blockers:
        status = "high-risk"
    elif warnings:
        status = "warnings"

    return {
        "repo_root": str(repo_root),
        "scope": scope,
        "status": status,
        "files_scanned": len(paths),
        "paths": paths,
        "blockers": blockers,
        "warnings": warnings,
    }


def render_findings(title: str, items: list[dict[str, str]]) -> list[str]:
    if not items:
        return [f"{title}: none"]
    lines = [f"{title}:"]
    for item in items:
        lines.append(f"  - {item['path']} [{item['category']}] {item['reason']}")
    return lines


def render_text(result: dict[str, object]) -> str:
    lines = [
        f"Repository: {result['repo_root']}",
        f"Scope: {result['scope']}",
        f"Status: {result['status']}",
        f"Files scanned: {result['files_scanned']}",
    ]
    lines.extend(render_findings("Blockers", result["blockers"]))
    lines.extend(render_findings("Warnings", result["warnings"]))
    if result["status"] == "clean":
        lines.append("Advice: No obvious pre-commit risks were detected in the scanned paths.")
    elif result["status"] == "warnings":
        lines.append("Advice: Review the warnings and confirm the files are intentional before committing.")
    else:
        lines.append("Advice: Stop and confirm the risky files before creating or pushing a commit.")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit changed Git paths for common pre-commit risks.")
    parser.add_argument("repo", nargs="?", default=".", help="Path to a Git repository. Defaults to the current directory.")
    parser.add_argument(
        "--scope",
        choices=("staged", "all"),
        default="staged",
        help="Audit staged files only or all changed/untracked files.",
    )
    parser.add_argument(
        "--max-bytes",
        type=int,
        default=1_000_000,
        help="Warn when a tracked file is larger than this many bytes.",
    )
    parser.add_argument("--json", action="store_true", help="Emit machine-readable JSON instead of text.")
    args = parser.parse_args()

    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    if hasattr(sys.stderr, "reconfigure"):
        sys.stderr.reconfigure(encoding="utf-8")

    repo = Path(args.repo).resolve()
    try:
        result = audit_repo(repo, scope=args.scope, max_bytes=max(args.max_bytes, 1))
    except RuntimeError as exc:
        print(f"pre_commit_audit.py: {exc}", file=sys.stderr)
        return 1

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_text(result))
    return 2 if result["blockers"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
