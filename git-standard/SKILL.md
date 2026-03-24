---
name: git-workflow
description: "Git repository inspection and safe workflow guidance for status checks, commit preparation, commit message validation, branch creation and merging, pre-commit audits, `.gitignore` rules, conflict resolution, and recovery steps. Use when working with Git history, branches, commits, merge targets such as `master` or `develop`, staged file safety checks, or post-implementation cleanup."
---

# Git Workflow

Use this skill inside existing Git repositories with safe defaults, explicit state checks, and minimal surprise. Inspect repository state before proposing or running any write operation.

## Initial Inspection

1. Run `python scripts/git_snapshot.py [repo-path]` from the target repository when available.
2. If the script is unavailable or more detail is needed, inspect:
   - `git status --short --branch`
   - `git branch --show-current`
   - `git remote -v`
   - `git log --oneline --decorate -n 8`
   - `git diff --stat`
3. Call out:
   - current branch or detached HEAD
   - staged, unstaged, and untracked changes
   - upstream tracking and ahead/behind state
   - ongoing merge, rebase, cherry-pick, or revert operations
   - recent commit message language tendency
   - recent commit title style tendency: lightweight, conventional, shared-colon, or mixed

On PowerShell or in repositories with non-ASCII file names, preserve UTF-8 output. Use the snapshot script or run Git with `-c core.quotepath=false -c i18n.logOutputEncoding=utf8`.

## Safety Rules

- Preserve user changes. Treat dirty worktrees as intentional until the user says otherwise.
- Prefer read-only commands before staging, committing, rebasing, merging, resetting, or pushing.
- Avoid `git reset --hard`, `git clean -fd`, `git checkout -- <path>`, and force-push unless the user explicitly requests them or the task clearly requires them.
- Explain safer alternatives before using history-rewriting commands.
- Quote exact branch names, commit hashes, and commands in user-facing summaries.
- Prefer non-interactive commands. Avoid opening editors, interactive rebases, and patch mode unless the user explicitly asks for that workflow.
- Prefer `git push --force-with-lease` over `git push --force` when force-push is truly required.
- Treat `master` as a protected merge target. Require explicit user confirmation before merging into `master`.
- Merge into `develop` only after repository state, target branch, and diff have been inspected.
- Do not bypass hooks with `--no-verify` unless the user explicitly requests it.
- Do not commit likely secrets, local credentials, or generated output silently. Audit and explain those files first.

## Workflow Decision Tree

1. Need to understand repository state?
   - Follow "Inspect Local State" or "Inspect History".
2. Need to prepare commits?
   - Follow "Create A Focused Commit".
3. Need to choose or validate a commit title style?
   - Follow "Commit Title Styles" and use `python scripts/validate_commit_message.py --style <style> "<message>"`.
4. Need to audit staged files before commit?
   - Follow "Pre-Commit Audit" and use `python scripts/pre_commit_audit.py [repo-path] --scope staged`.
5. Need to create a branch or merge a branch?
   - Follow "Create Or Merge Branches" and use `python scripts/branch_policy.py <target-branch>` before the merge if the target branch matters.
6. Need to take over after implementation or testing is done and turn local changes into clean Git operations?
   - Follow "Post-Implementation Git Handoff".
7. Need to check whether the repository usually commits in Chinese or English?
   - Run `python scripts/git_snapshot.py [repo-path] --commits 30` or `python scripts/analyze_commit_language.py [repo-path]`.
8. Need to update a branch from remote or integrate another branch?
   - Follow "Sync Or Integrate Branches".
9. Need to resolve conflicts?
   - Follow "Resolve Conflicts".
10. Need to add or fix `.gitignore` rules?
   - Follow "Manage Ignore Rules" and read [references/gitignore-patterns.md](references/gitignore-patterns.md).
11. Need to recover, undo, or rewrite history?
   - Read [references/recovery-and-history-rewrite.md](references/recovery-and-history-rewrite.md) before changing anything.

## Inspect Local State

- Run the snapshot script first.
- Use `git diff` for unstaged changes and `git diff --cached` for staged changes.
- Use `git branch -vv` to inspect tracking branches.
- Use `git stash list` if the task might involve previously shelved work.
- Summarize scope before acting: what changed, where, and whether the branch is clean or diverged.
- When preparing a commit, compare `git diff` and `git diff --cached` so the staged scope matches the intended title.

## Inspect History

- Use `git log --oneline --decorate --graph -n 20` for recent branch history.
- Use `git show <commit>` for one commit.
- Use `git diff <base>...HEAD` to compare branch content.
- Use `git log --left-right --cherry-pick --oneline <base>...HEAD` to understand branch divergence.
- Use `git blame <file>` only when line-level authorship matters.
- Inspect recent commit subjects before writing a new one. Keep the existing language and style convention unless the user asks to change it.
- If recent history is split between lightweight, conventional, or shared-colon subjects, report it as `mixed-convention` instead of forcing a migration.
- Use `python scripts/analyze_commit_language.py [repo-path]` for a quick Chinese vs English summary over recent commit subjects.

## Create A Focused Commit

1. Inspect the working tree first.
2. Group changed files by intent.
3. Stage only the relevant files with explicit paths.
4. Inspect recent commit subjects and determine:
   - repository language tendency
   - repository commit title style tendency
5. Run `python scripts/pre_commit_audit.py [repo-path] --scope staged` when staged files include env files, credentials, build output, binary artifacts, or when the user wants to commit "everything".
6. Verify the staged diff with `git diff --cached` or `git diff --cached --stat`.
7. Infer the title from the actual staged diff, not just the branch name or ticket title.
8. Preserve the repository's existing commit style when it is clear.
9. If the repository has no stronger convention, default to the lightweight `type: description` format described in [references/commit-message-convention.md](references/commit-message-convention.md).
10. If the repository already uses Conventional Commits, the user asks for semantic titles, or release tooling depends on it, use [references/conventional-commits.md](references/conventional-commits.md).
11. Validate the final title with `python scripts/validate_commit_message.py --style <style> "<message>"`.
12. Re-run the snapshot script or `git status --short --branch` after committing.

Prefer separate commits for unrelated concerns. Keep generated files separate from hand-edited source when they do not belong to the same logical change.

## Commit Title Styles

### Lightweight Default

Use this when the repository has no stronger standard or already uses simple `type: description` subjects.

- Reference: [references/commit-message-convention.md](references/commit-message-convention.md)
- Validate with: `python scripts/validate_commit_message.py --style lightweight "fix: 修复登录页空白问题"`
- Allowed types: `fix`, `add`, `update`, `style`, `test`, `revert`, `build`
- Prefer a concrete summary such as verb plus object.
- Keep the title within about 50 characters when practical.

Examples:

- `fix: 修复登录页空白问题`
- `add: 新增用户筛选功能`
- `update: refresh dashboard copy`

### Conventional Commits

Use this when recent history already uses `feat:` / `fix(scope):` style, the user explicitly requests it, or the repository uses release automation, changelog tooling, or commitlint.

- Reference: [references/conventional-commits.md](references/conventional-commits.md)
- Validate with: `python scripts/validate_commit_message.py --style conventional "feat(auth): add passkey login"`
- Common types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`
- Use a scope only when it meaningfully narrows the subsystem.
- Use `!` only for actual breaking changes.
- Keep the subject line within about 72 characters when practical.
- If a full Conventional Commit body or footer is needed, write it after the validated title. Explain why or document `BREAKING CHANGE:` only when it materially helps reviewers or tooling.

Examples:

- `feat(auth): add passkey login`
- `fix(api)!: remove legacy token format`
- `docs(readme): clarify branch policy`

## Pre-Commit Audit

Run `python scripts/pre_commit_audit.py [repo-path] --scope staged` before committing when the staged set looks broad or risky.

- Treat high-risk findings as blockers:
  - `.env` files
  - private keys such as `id_rsa`, `*.pem`, `*.key`
  - credential JSON files such as `credentials.json` or `service-account*.json`
  - token or private key patterns detected in staged file content
- Treat generated-output findings as verify-first warnings:
  - `dist/`, `build/`, `coverage/`, `node_modules/`, `.next/`, `target/`, and similar directories
  - large generated bundles or compiled artifacts
- If generated files are intentionally committed, explain that intention before proceeding.
- Re-run the audit after changing the staged file set.

## Post-Implementation Git Handoff

Use this flow when coding work is already done and the next step is to turn the resulting changes into clean Git operations.

1. Start with `python scripts/git_snapshot.py [repo-path]`.
2. Inspect the changed files and diff shape:
   - `git status --short --branch`
   - `git diff --stat`
   - `git diff`
   - `git diff --cached`
3. Confirm what just happened:
   - feature implementation finished
   - bug fix finished
   - tests were added or fixed
   - verification already passed or still needs to run
4. Split unrelated changes before committing.
5. Check the repository's commit language and title style convention.
6. Stage only the files for one logical change.
7. Audit the staged file set with `python scripts/pre_commit_audit.py [repo-path] --scope staged` when needed.
8. Validate the commit title, then commit.
9. If the next step is integration, apply the branch policy:
   - merge to `develop` after inspection
   - stop for explicit confirmation before merging to `master`

Use this flow after requests like "功能做完了", "测试通过了", "开始整理改动", or similar.

## Create Or Merge Branches

1. Inspect available branches first:
   - `git branch --all --verbose`
   - `git status --short --branch`
2. Choose a starting point intentionally:
   - prefer `develop` when the repository uses `master` plus `develop`
   - otherwise use the user-specified base branch
3. Create the branch with an explicit name:
   - preserve the repository's existing naming scheme when it is clear
   - otherwise prefer `feature/<name>`, `fix/<name>`, `chore/<name>`, or `hotfix/<name>`
   - keep names lowercase and hyphenated unless the repository uses ticket prefixes or another established pattern
4. Before merging, inspect both the target branch and the feature branch:
   - `git log --oneline --decorate --graph <target>..HEAD`
   - `git diff --stat <target>...HEAD`
5. Check the target branch policy:
   - `python scripts/branch_policy.py develop` means no extra confirmation is required
   - `python scripts/branch_policy.py master` means stop and ask the user before merging
6. Merge into `develop` after inspection and verification:
   - switch to `develop`
   - merge with an explicit command such as `git merge --no-ff <feature-branch>` when merge commits are preferred
7. Do not merge into `master` until the user explicitly confirms that target.
8. After any merge, inspect `git status`, inspect the new history, and run relevant tests if the repository has them.

When the target branch is not `master` or `develop`, state the assumption you are making before merging.

## Sync Or Integrate Branches

1. Fetch first: `git fetch --all --prune`.
2. Inspect divergence with `git status --short --branch` and `git branch -vv`.
3. Choose the integration strategy deliberately:
   - rebase local-only work for a linear history
   - merge when the repository intentionally preserves merge commits
4. Before push, confirm the destination branch, whether history was rewritten, and whether the branch name matches repository conventions.
5. Push with an explicit remote and branch name when possible.
6. Summarize verification state before opening or updating a pull request.

Avoid relying on ambiguous defaults such as a bare `git pull` when the strategy matters. Prefer `fetch` plus an explicit `merge` or `rebase` decision.

## Manage Ignore Rules

1. Inspect the current rules before editing:
   - `.gitignore`
   - `.git/info/exclude`
   - global ignore config if the task depends on developer-local behavior
2. Inspect what Git currently ignores or still reports:
   - `git status --ignored=matching --short`
   - `git check-ignore -v -- <path>` for one specific file or directory
3. Add ignore rules only for files that should not be versioned:
   - dependency directories such as `node_modules/`
   - build output such as `dist/`, `build/`, `.next/`
   - logs, caches, and temporary files
   - local-only secrets such as `.env`
4. Do not ignore files that are usually intentional repository inputs:
   - lockfiles such as `package-lock.json`, `yarn.lock`, `pnpm-lock.yaml`
   - shared examples such as `.env.example`
   - source files, migrations, or generated files that the repository intentionally commits
5. If a file is already tracked, explain that `.gitignore` will not untrack it by itself. Use `git rm --cached -- <path>` only when the user wants to stop tracking it.

Prefer the narrowest rule that matches the user intent. Repository-level `.gitignore` should contain team-shared rules; developer-specific noise belongs in `.git/info/exclude` or global Git ignore.

## Resolve Conflicts

1. Identify the operation in progress: merge, rebase, cherry-pick, revert, or stash pop.
2. List conflicted files with `git diff --name-only --diff-filter=U`.
3. Inspect each file and resolve the final content intentionally instead of choosing sides mechanically.
4. Stage resolved files with `git add -- <path>`.
5. Continue with the matching command:
   - `git merge --continue`
   - `git rebase --continue`
   - `git cherry-pick --continue`
6. Abort only when the user wants to discard the in-progress operation.

Run targeted tests or at least a build or lint step after conflict resolution when the repository has an existing verification workflow.

## Resources

- `scripts/git_snapshot.py`: Capture branch, upstream, status counts, remotes, recent commits, stashes, in-progress Git operations, and commit format tendencies.
- `scripts/analyze_commit_language.py`: Classify recent commit subjects as Chinese, English, mixed, or other, then report the dominant language convention.
- `scripts/branch_policy.py`: Report whether a target branch requires explicit user confirmation before merge. `master` requires confirmation; `develop` does not.
- `scripts/validate_commit_message.py`: Validate lightweight or Conventional Commit titles with explicit style selection.
- `scripts/pre_commit_audit.py`: Audit staged or changed paths for likely secrets, generated output, and large accidental artifacts.
- [references/commit-message-convention.md](references/commit-message-convention.md): Lightweight commit title convention for repositories without a stronger standard.
- [references/conventional-commits.md](references/conventional-commits.md): Conventional Commit format, type guidance, and breaking-change examples.
- [references/gitignore-patterns.md](references/gitignore-patterns.md): Common `.gitignore` patterns and guidance for Node.js, build output, temp files, logs, editors, and tracked-file cleanup.
- [references/recovery-and-history-rewrite.md](references/recovery-and-history-rewrite.md): Read before reset, revert, stash recovery, reflog recovery, or force-push work.
