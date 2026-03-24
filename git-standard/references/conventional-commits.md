# Conventional Commits

Use this format when the repository already uses Conventional Commits, the user explicitly asks for semantic commit titles, or release tooling depends on commit types.

## Format

```text
type(scope)!: description
```

Scope and `!` are optional. The minimal valid form is:

```text
type: description
```

## Common Types

- `feat`: new user-visible capability
- `fix`: bug fix
- `docs`: documentation-only change
- `style`: formatting-only change
- `refactor`: code change without intended behavior change
- `perf`: performance improvement
- `test`: test-only change
- `build`: build tooling or dependency pipeline change
- `ci`: CI configuration or workflow change
- `chore`: maintenance work that does not fit a better type
- `revert`: revert a previous commit

## Scope Guidance

- Use a scope only when it meaningfully narrows the subsystem, package, page, or service.
- Prefer short scopes such as `auth`, `api`, `readme`, or `build`.
- Skip the scope when the change is already obvious without it.

## Breaking Changes

- Add `!` when the change is intentionally breaking.
- Add a `BREAKING CHANGE:` footer when the change needs reviewer or release-tool context.
- Do not mark a change as breaking unless downstream users really need to act.

## Examples

- `feat(auth): add passkey login`
- `fix(api)!: remove legacy token format`
- `docs(readme): clarify merge workflow`
- `ci(actions): cache pnpm store`

## Validator

```bash
python scripts/validate_commit_message.py --style conventional "feat(auth): add passkey login"
```

## Notes

- Keep the description aligned with the repository's existing language convention.
- Infer the type from the actual staged diff, not just the branch name or issue title.
- If the repository clearly uses a lighter `type: description` convention, preserve it unless the user asks to migrate.
