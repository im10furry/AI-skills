---
name: git-rganize-commit
description: "Reorganize existing Git history and turn dirty worktrees into focused, standardized commits. Use when the user asks to 整理 Git 记录, 规范化提交, 拆分提交, 重写本地提交历史, 或 when a Git repository has staged, unstaged, or untracked files that should be grouped by module and committed safely. Prefer multi-agent or parallel agent work during organization: let sub-agents inspect file groups, commit clusters, and repository conventions in parallel, while the main agent keeps ownership of final staging, commit creation, and history-rewrite commands. On manual invocation, inspect the current branch history and rebuild the local commit range into clean commits; with uncommitted files, follow the standard focused-commit workflow from git-commit."
---

# Git Rganize Commit

## Overview

Use this skill inside an existing Git repository when commits or local changes need cleanup. Treat the work as one of two modes:

1. `dirty-worktree cleanup`: staged, unstaged, or untracked files should become focused commits by module.
2. `history cleanup`: existing local commits on the current branch should be reorganized into a cleaner sequence.

Keep the workflow text-first and non-interactive. Preserve user changes, preserve the repository's existing commit language/style, and keep UTF-8 output on PowerShell.

## Agent Strategy

Prefer multiple agents when the repository scope is broad enough to parallelize safely.

- Keep the main agent responsible for repository-state decisions, final staging, commit creation, reset/rewrite commands, and any force-push decision.
- Use sub-agents for read-heavy parallel work such as:
  - grouping changed files by module or intent
  - inspecting recent commit language and style
  - reviewing one package or directory each
  - proposing commit boundaries for a local history rewrite
- Give each sub-agent a disjoint analysis scope. Avoid duplicate review of the same files or commit range.
- Do not let sub-agents run destructive Git commands by default. They should inspect, summarize, and recommend; the main agent executes the final Git operations.
- If the task is small, keep it single-agent rather than forcing parallelism.

## Initial Inspection

Start every run with UTF-8-safe inspection:

- `git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 status --short --branch`
- `git branch --show-current`
- `git branch -vv`
- `git remote -v`
- `git log --oneline --decorate -n 12`
- `git diff --stat`
- `git diff --cached --stat`

On PowerShell or non-ASCII paths, also keep UTF-8 console output:

- `$OutputEncoding = [Console]::OutputEncoding = [System.Text.UTF8Encoding]::new()`

Summarize before acting:

- current branch and upstream state
- staged, unstaged, and untracked files
- whether merge, rebase, cherry-pick, or revert is in progress
- recent commit language and title style tendency
- whether the request targets dirty changes, existing commits, or both
- whether the scope is large enough to benefit from parallel sub-agent analysis

## Decision Tree

1. If this is not a Git repository, stop.
2. If merge, rebase, cherry-pick, or revert is in progress, resolve or abort that operation first.
3. If the branch contains already-pushed commits and the user did not explicitly approve history rewriting, stop after explaining the risk. Prefer a new cleanup commit when rewriting shared history is unnecessary.
4. If the file set or commit range is broad enough to partition safely, spawn multiple sub-agents for parallel analysis before making final Git changes.
5. If the worktree is dirty and the user wants focused commits, follow `Split Uncommitted Changes`.
6. If the user explicitly asks to reorganize existing commits, or manually invokes this skill without a narrower scope, follow `Rewrite Local History Safely`.
7. Interpret "整理所有 Git 记录" as the current branch's local commit range relative to its base branch, not the entire repository history, unless the user explicitly asks for the broader rewrite.

## Split Uncommitted Changes

Use this flow when the repo has staged, unstaged, or untracked files and the task is "按模块提交", "拆分提交", or "规范化本次改动".

1. Inspect both unstaged and staged changes:
   - `git diff`
   - `git diff --cached`
2. If the repository has several distinct directories or subsystems, prefer parallel sub-agents to inspect one slice each and propose commit grouping.
3. Group files by intent. Prefer module, package, feature, test, docs, or build boundaries. Do not mix unrelated work in one commit.
4. Merge sub-agent suggestions into one final commit plan before staging anything.
5. Stage one logical change at a time with explicit paths:
   - `git add -- <path> <path>`
6. Audit the staged set before every commit:
   - `git diff --cached --name-only --diff-filter=ACMR`
   - `git diff --cached --stat`
   - `git diff --cached`
7. Choose the commit subject from the staged diff, not from the branch name alone. Use [references/commit-standardization.md](references/commit-standardization.md) when the repo style is unclear.
8. Commit one module and re-run status:
   - `git commit -m "fix: 修复订单列表分页错乱"`
   - `git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 status --short --branch`
9. Repeat until the worktree is clean or only intentionally uncommitted files remain.

## Rewrite Local History Safely

Use this flow only when existing commits on the current branch need normalization. Prefer unpublished local commits or branches where the user explicitly accepts a force-push workflow.

1. Inspect the rewrite scope:
   - `git log --oneline --decorate --graph -n 20`
   - `git log --left-right --cherry-pick --oneline @{upstream}...HEAD` when an upstream exists
2. Prefer parallel sub-agents to inspect different commit clusters, modules, or directories and propose how the rebuilt commit sequence should be split.
3. Choose the rewrite base:
   - prefer `git merge-base HEAD @{upstream}` when the branch tracks a remote
   - otherwise use the merge-base against the target branch such as `origin/develop`, `origin/main`, or the user-provided base
4. Consolidate the sub-agent recommendations into one final rewrite plan owned by the main agent.
5. Capture a safety snapshot before moving `HEAD`:
   - `git branch backup/<branch>-<yyyymmdd-hhmm>`
   - `git reflog -n 20`
6. Convert the local commit range back into a dirty worktree with the non-interactive standard method:
   - `git reset --soft <base>`
   - `git reset`
7. Rebuild commits module by module using `Split Uncommitted Changes`.
8. Verify that the rebuilt branch still matches the intended content:
   - `git diff --stat <base>...HEAD`
   - `git log --oneline --decorate --graph <base>..HEAD`
9. If the old commits were already pushed, explain the collaborator impact and ask before:
   - `git push --force-with-lease`

Avoid interactive rebase by default. The reset-and-recommit flow is the standard method for this skill because it works well for full local branch normalization and keeps the operation explicit.

## Commit Rules

- Preserve the repository's recent language tendency.
- Preserve the repository's recent title style tendency.
- If the repo has no stronger standard, default to lightweight `type: description`.
- If recent history clearly uses Conventional Commits or release tooling depends on it, keep that format.
- Infer the type from the actual staged diff.
- Keep generated artifacts separate from source edits unless they are part of the same logical change.
- Audit suspicious staged files before committing:
  - `.env`
  - `*.pem`
  - `*.key`
  - `service-account*.json`
  - large build output such as `dist/`, `build/`, `.next/`, or `coverage/`

## Safety Boundaries

- Preserve user changes by default.
- Prefer parallel read-only sub-agent analysis before broad cleanup work.
- Prefer `git revert` on shared history when the goal is to undo published work.
- Do not use `git reset --hard`, `git clean -fd`, `git push --force`, or `git branch -D` unless the user explicitly approves the risk.
- Treat `master` as protected. Require explicit confirmation before rewriting work that will land there.
- Do not open interactive editors unless the user explicitly asks for interactive Git operations.

## Resources

- [references/commit-standardization.md](references/commit-standardization.md): Commit title and staged-audit rules derived from the `git-commit` workflow.
- [references/history-rewrite-playbook.md](references/history-rewrite-playbook.md): Recovery, reflog, reset, and force-push guidance for history cleanup.
