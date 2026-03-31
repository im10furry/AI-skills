---
name: git-init
description: Check whether the current working directory or target path already belongs to a Git repository before coding or file edits. Use at the start of programming tasks, project bootstrap work, or requests such as "git init", "初始化 git", "先检查有没有 Git 仓库", or "before coding, make sure this folder has Git". If no repository exists, initialize an empty one and stop. Use this skill only for the one-time preflight check, not for staging, commits, history inspection, or later Git operations.
---

# Git Init

Run this skill once at the start of a coding task when repository presence is unknown. Its only job is to detect an existing Git repository or create a new empty repository, then hand off later Git work to `git-workflow` or another commit-focused skill.

## Workflow

1. Resolve the target directory.
   - Default to the user's current working directory unless the user names another path.
   - The target path must already exist.
2. Check whether the directory is already inside a repository.
   - Run `git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 rev-parse --show-toplevel` in the target directory.
3. Interpret the result.
   - If the command succeeds, report the repository root and continue with the coding task.
   - If the command fails because the directory is not inside a repository, run `git init` in the target directory.
   - If another error occurs, stop and show the exact failure.
4. After the repository exists, stop using this skill for the rest of the task.
   - Later staging, diff, branch, or commit work belongs to `git-workflow` or another commit-focused skill.

## Rules

- Detect repositories from the target directory upward. Never run `git init` inside a subdirectory that is already inside a repository.
- Initialize only a normal empty repository with `git init`.
- Do not stage files, write commits, add remotes, or edit `.gitignore`.
- This skill must stay text-only. Do not rely on Python helpers or other bundled scripts.
- When reporting paths or Git output, preserve UTF-8 and avoid quoted escape sequences.

## Command Pattern

Use this exact decision flow:

1. `git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 rev-parse --show-toplevel`
2. If that succeeds, stop and report the existing repository root.
3. If that fails with a "not a git repository" style message, run `git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 init`
4. Report whether the repository was found or newly created.

## Examples

- `开始写这个项目之前先看有没有 Git 仓库`
- `先帮我做 git init 检查`
- `Before coding, make sure this folder has Git`
- `If this folder is not a repo, initialize one`

## Resources

- No scripts. This skill is intentionally text-only and uses direct Git commands.
