# History Rewrite Playbook

Read this file before reset, rebase cleanup, force-push, or any full-branch commit reorganization.

## Parallel Agent Preference

Prefer multiple agents when the branch is large enough to split safely.

- Keep the main agent responsible for base selection, backup branch creation, reset/rewrite execution, final staging, and any push.
- Use sub-agents for parallel read-only analysis:
  - inspect separate directories or packages
  - inspect separate commit clusters in the local range
  - infer repository commit style from recent history
  - propose rebuilt commit boundaries
- Consolidate all sub-agent recommendations into one explicit rewrite plan before running `git reset`, creating commits, or force-pushing.
- Do not let sub-agents perform destructive history edits by default.

## Start With A Snapshot

Inspect the current state before touching history:

- `git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 status --short --branch`
- `git log --oneline --decorate -n 10`
- `git branch -vv`
- `git reflog -n 20`

If merge, rebase, cherry-pick, or revert is already in progress, finish or abort it intentionally before doing anything else.

## Default Rewrite Scope

Unless the user asks for a broader change, treat "整理所有 Git 记录" as:

- the current branch only
- the local commit range between `<base>` and `HEAD`
- a rewrite that must preserve the final file content

Do not assume permission to rewrite the entire repository or other branches.

## Standard Non-Interactive Rewrite Method

Use this as the default branch-normalization flow:

1. Choose the base:
   - `git merge-base HEAD @{upstream}` when upstream exists
   - otherwise the merge-base against `origin/develop`, `origin/main`, or another explicit target branch
2. If the scope is broad, run parallel read-only analysis on file groups or commit clusters and turn the results into one final rewrite plan.
3. Create a recovery pointer:
   - `git branch backup/<branch>-<yyyymmdd-hhmm>`
4. Turn the current branch range into a working tree:
   - `git reset --soft <base>`
   - `git reset`
5. Re-stage and commit by module:
   - `git add -- <path> <path>`
   - audit staged changes
   - commit with an explicit message
6. Verify the rebuilt history:
   - `git diff --stat <base>...HEAD`
   - `git log --oneline --decorate --graph <base>..HEAD`

This method is preferred over interactive rebase for this skill because it makes the rewritten scope explicit and keeps the grouping logic aligned with the current file tree.

## Shared History Rules

If commits were already pushed:

- explain collaborator impact before rewriting
- prefer `git revert <commit>` when the real goal is to undo published work
- ask before `git push --force-with-lease`
- never default to plain `git push --force`

## Recovery Rules

Use the least destructive recovery option first:

1. `git restore --staged -- <path>`
2. `git restore -- <path>`
3. `git stash push -u -m "message"`
4. `git revert <commit>`
5. `git reset --soft <target>`
6. `git reset --mixed <target>`
7. `git reset --hard <target>` only after explicit user approval

If commits seem lost, recover from `git reflog` with a non-destructive branch:

- `git switch -c recovery/<name> <sha>`
