# Gitignore Patterns

Use this file when the task involves creating, reviewing, or cleaning up `.gitignore`.

## Rules Of Thumb

- Ignore generated output, caches, logs, temp files, and machine-local secrets.
- Do not ignore source code, migration files, lockfiles, or other inputs required for reproducible builds unless the repository already treats them as generated.
- Prefer repository `.gitignore` for team-wide rules.
- Prefer `.git/info/exclude` or global ignores for personal editor noise that the team does not share.
- If a file is already tracked, adding it to `.gitignore` does not remove it from version control.

## Useful Inspection Commands

- show ignored files: `git status --ignored=matching --short`
- explain why a path is ignored: `git check-ignore -v -- <path>`
- stop tracking a file that should now be ignored: `git rm --cached -- <path>`

## Common Baseline

```gitignore
# OS and editor noise
.DS_Store
Thumbs.db
*.swp
*.swo
*~

# Logs and temp files
*.log
logs/
tmp/
temp/
.cache/

# Local environment files
.env
.env.local
.env.*.local
!.env.example
```

## Node.js And Frontend

Use these when the repo is a Node.js or frontend project and the files are generated locally:

```gitignore
# Dependencies
node_modules/

# Package manager caches
.pnpm-store/
.npm/
.yarn/cache/
.yarn/unplugged/

# Build output
dist/
build/
coverage/
.next/
.nuxt/
.svelte-kit/
.parcel-cache/
*.tsbuildinfo
```

Usually commit these unless the project has a specific reason not to:

- `package-lock.json`
- `yarn.lock`
- `pnpm-lock.yaml`

## Python

```gitignore
__pycache__/
*.py[cod]
.pytest_cache/
.mypy_cache/
.ruff_cache/
.venv/
venv/
dist/
build/
*.egg-info/
```

## Java And JVM

```gitignore
target/
build/
.gradle/
out/
*.class
```

## Go

```gitignore
bin/
coverage.out
*.test
```

## Rust

```gitignore
target/
```

Commit `Cargo.lock` for applications unless the repository intentionally treats it as a library-only file.

## .NET

```gitignore
bin/
obj/
.vs/
```

## Tracked File Cleanup

If `node_modules/`, `dist/`, or another generated directory is already tracked:

1. Add the ignore rule.
2. Remove it from the index without deleting the working copy:
   - `git rm -r --cached -- node_modules`
   - `git rm -r --cached -- dist`
3. Verify with `git status`.
4. Commit the cleanup separately from unrelated code changes.

## Decision Guidance

- Ignore `node_modules/`: yes, in normal Node.js repositories.
- Ignore `dist/` or `build/`: usually yes, unless the repo intentionally commits built artifacts.
- Ignore `.env`: yes.
- Ignore `.env.example`: no, if it documents required variables.
- Ignore `.vscode/`: only if the repository does not intentionally share workspace settings.
