# Recovery And History Rewrite

Read this file before reset, revert, stash recovery, reflog recovery, amend, rebase cleanup, or force-push work.

## Start With A Snapshot

1. Run `python scripts/git_snapshot.py [repo-path]`.
2. Inspect `git status --short --branch`.
3. Inspect `git log --oneline --decorate -n 10`.
4. Inspect `git reflog -n 20` when commits may have moved or disappeared.

## Prefer The Least Destructive Tool

Use the first command that solves the request:

1. `git restore --staged -- <path>`
2. `git restore -- <path>`
3. `git stash push -u -m "message"`
4. `git revert <commit>`
5. `git reset --soft <target>`
6. `git reset --mixed <target>`
7. `git reset --hard <target>` only after explicit user approval

## Intent To Command Map

### Unstage A File

Run `git restore --staged -- <path>`.

### Discard Local Edits To One File

Inspect with `git diff -- <path>` first. Run `git restore -- <path>` only if the user clearly wants to discard that work.

### Undo The Last Commit But Keep Changes Staged

Run `git reset --soft HEAD~1`.

### Undo The Last Commit And Leave Changes Unstaged

Run `git reset --mixed HEAD~1`.

### Reverse A Commit On Shared History

Run `git revert <commit>`.

### Shelve Work Temporarily

- save: `git stash push -u -m "message"`
- inspect: `git stash list`
- restore: `git stash pop` or `git stash apply stash@{n}`

### Recover Lost Commits Or Branch Tips

1. Run `git reflog`.
2. Identify the commit or branch tip to recover.
3. Recover safely with `git switch -c recovery/<name> <sha>` or another non-destructive branch move.
4. Use `git reset --hard <sha>` only if the user explicitly wants the current branch moved there.

## Rebase And Cherry-Pick Recovery

1. Inspect `git status`.
2. Resolve conflicted files intentionally.
3. Stage resolved files with `git add -- <path>`.
4. Continue with `git rebase --continue` or `git cherry-pick --continue`.
5. Abort with the matching `--abort` command only when the user wants to abandon the operation.

## Force-Push Checklist

Before force-pushing:

1. Verify the exact branch and upstream.
2. Verify that rewritten commits are the expected commits.
3. Warn about collaborator impact.
4. Prefer `git push --force-with-lease`.

## High-Risk Commands

Treat these as opt-in operations:

- `git reset --hard`
- `git clean -fd`
- `git push --force`
- `git branch -D`

Before using any of them, capture the current state and explain the safer alternative.
