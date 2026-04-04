# Commit Standardization

Use this file when deciding how to split staged changes and how to name each commit.

## Inspect Before Choosing A Title

Always inspect the staged set before writing a subject:

- `git diff --cached --name-only --diff-filter=ACMR`
- `git diff --cached --stat`
- `git diff --cached`
- `git log --oneline --decorate -n 12`

Infer the message from the staged diff, not from the branch name or ticket text.

## Default Lightweight Style

Use this when the repository does not already show a stronger standard:

```text
type: description
```

Allowed types:

- `fix`
- `add`
- `update`
- `style`
- `test`
- `revert`
- `build`

Rules:

- keep `type` lowercase
- keep exactly one colon separator
- use a concrete summary
- prefer staying within about 50 characters when practical
- keep the repository's existing language convention when it is clear

Examples:

- `fix: 修复接口超时问题`
- `add: 新增批量导出功能`
- `update: refresh dashboard copy`

## Conventional Commits

Use this when recent history already follows it, the user explicitly asks for it, or release tooling depends on it:

```text
type(scope)!: description
```

Common types:

- `feat`
- `fix`
- `docs`
- `style`
- `refactor`
- `perf`
- `test`
- `build`
- `ci`
- `chore`
- `revert`

Rules:

- keep `scope` only when it meaningfully narrows the subsystem
- use `!` only for actual breaking changes
- keep the description aligned with the repository's language convention
- do not silently migrate a lightweight-history repository to Conventional Commits

Examples:

- `feat(auth): add passkey login`
- `fix(api)!: remove legacy token format`
- `docs(readme): clarify merge workflow`

## Module Split Checklist

Split staged changes by one logical intent at a time:

- one feature or bug fix
- one package or directory when the change is isolated there
- one docs-only change
- one test-only change
- one build or CI change

Do not mix unrelated source, docs, tests, and generated files unless the diff clearly belongs to one inseparable change.

## Stage Audit Blockers

Treat these as blockers that require direct inspection before commit:

- `.env`
- `*.pem`
- `*.key`
- `credentials.json`
- `service-account*.json`

Treat these as verify-first warnings:

- `dist/`
- `build/`
- `.next/`
- `coverage/`
- `node_modules/`

If generated output is intentionally committed, explain why it belongs in the commit.
