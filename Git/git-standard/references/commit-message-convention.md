# Lightweight Commit Message Convention

Use this convention when the repository does not already have a stronger standard and the team wants a simple, readable title format.

If the repository already uses `feat:` / `fix(scope):` style, commitlint, semantic-release, or another automated release flow, use [conventional-commits.md](conventional-commits.md) instead.

## Format

```text
type: description
```

## Allowed Types

- `fix`: bug fix
- `add`: new feature or capability
- `update`: update to existing logic, content, or behavior
- `style`: formatting or style-only change
- `test`: add or adjust tests
- `revert`: revert a previous change
- `build`: build tooling or build-process change

## Rules

- Keep the title explicit and short.
- Prefer a concrete summary of the change, usually verb plus object.
- Avoid vague titles such as `修改`, `更新`, `fix bug`, or `update code`.
- Prefer staying within 50 characters when practical.
- Use the repository's existing language convention when possible.
- Keep `type` lowercase.
- Keep exactly one colon separator after `type`.

## Examples

- `fix: 修复接口超时问题`
- `add: 新增活动页埋点`
- `update: refresh docs landing copy`
- `build: 升级 webpack 配置`

## Manual Check

- `type` 使用小写。
- 只保留一个冒号分隔符。
- 描述直接对应本次 staged diff。
- 语言和最近提交历史保持一致。

## Notes

- This format is intentionally lighter than full Conventional Commits.
- Preserve an existing repository convention instead of migrating styles silently.
