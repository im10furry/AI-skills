# git-standard

`git-standard` 是一个面向 AI 代理和开发者的 Git 工作流技能包，用来统一仓库检查、提交准备、分支合并、安全审计和 Git 恢复操作。它把一套可执行脚本、规则说明和代理入口放在同一个目录里，适合在真正动 Git 之前先做一次安全、可解释的检查。

## 适用场景

- 进入一个已有 Git 仓库，先快速看清当前状态
- 准备提交代码，需要判断仓库偏好的提交语言和标题风格
- 提交前排查 `.env`、密钥、构建产物、大文件等高风险内容
- 创建分支、合并分支，且对 `develop` / `master` 有明确策略
- 清理 `.gitignore` 规则或检查忽略行为
- 处理冲突、回滚、stash、reflog 恢复、历史改写前的风险评估

## 核心能力

### 1. 仓库状态快照

优先通过 `scripts/git_snapshot.py` 输出仓库摘要，补足下面这些判断：

- 当前分支或 detached HEAD 状态
- staged / unstaged / untracked 变更数量
- upstream 跟踪关系与 ahead / behind 状态
- merge、rebase、cherry-pick、revert 等进行中的 Git 操作
- 最近提交的语言倾向
- 最近提交标题的风格倾向

### 2. 提交规范判断与校验

该技能支持两套提交标题约定：

- 轻量规范：`type: description`
- Conventional Commits：`type(scope)!: description`

默认策略不是强推迁移，而是先读仓库历史，优先沿用已有习惯。只有在仓库已经使用 Conventional Commits、用户明确要求、或发布工具依赖语义化提交时，才切换到 Conventional Commits。

### 3. 提交前风险审计

`scripts/pre_commit_audit.py` 用来检查 staged 或全部变更，重点发现：

- `.env`、私钥、凭据 JSON 等敏感文件
- token / secret 模式
- `dist/`、`build/`、`coverage/`、`node_modules/` 等构建产物
- 过大的可疑文件

### 4. 分支与合并策略

内置的分支策略很直接：

- 合并到 `develop`：检查完成后可继续
- 合并到 `master`：必须先获得用户明确确认

### 5. 恢复与高风险操作前置说明

在执行 `reset`、`revert`、`stash` 恢复、`reflog` 恢复、`amend`、`force-push` 之前，先看快照，再优先选择破坏性更小的命令。

## 目录结构

```text
git-standard/
├─ SKILL.md
├─ README.md
├─ agents/
│  └─ openai.yaml
├─ references/
│  ├─ commit-message-convention.md
│  ├─ conventional-commits.md
│  ├─ gitignore-patterns.md
│  └─ recovery-and-history-rewrite.md
└─ scripts/
   ├─ analyze_commit_language.py
   ├─ branch_policy.py
   ├─ git_snapshot.py
   ├─ pre_commit_audit.py
   └─ validate_commit_message.py
```

## 快速开始

### 作为技能使用

该目录的技能名是 `git-workflow`。代理入口定义在 `agents/openai.yaml`，默认提示词是：

```text
Use $git-workflow to inspect this repository, audit staged files, and prepare a safe Git commit or merge.
```

适合的触发词包括：

- 提交、提交规范、commit message、commitlint
- 分支、创建分支、合并分支、master、develop
- push 前检查、整理改动、测试完成后提交代码
- secrets、.env、冲突、回滚、stash、reflog、cherry-pick、.gitignore

### 作为命令行工具使用

依赖：

- Git
- Python 3
- 标准库即可，无第三方 Python 依赖

常用命令：

```bash
python scripts/git_snapshot.py [repo-path]
python scripts/analyze_commit_language.py [repo-path]
python scripts/branch_policy.py develop
python scripts/validate_commit_message.py --style lightweight "fix: 修复登录页空白问题"
python scripts/pre_commit_audit.py [repo-path] --scope staged
```

所有脚本都支持 `--help`，其中多数支持 `--json`，便于被代理或自动化流程调用。

## 推荐工作流

### 1. 先看仓库状态

```bash
python scripts/git_snapshot.py .
```

如果需要额外核对，再补这些 Git 命令：

```bash
git status --short --branch
git branch --show-current
git remote -v
git log --oneline --decorate -n 8
git diff --stat
```

### 2. 判断仓库使用哪种提交风格

```bash
python scripts/analyze_commit_language.py .
python scripts/validate_commit_message.py --style auto "fix: 修复接口超时问题"
```

建议：

- 仓库历史清晰时，延续现有语言和风格
- 没有强规范时，默认使用轻量 `type: description`
- 有 commitlint、semantic-release 或明确语义化要求时，使用 Conventional Commits

### 3. 提交前做审计

```bash
python scripts/pre_commit_audit.py . --scope staged
```

如果 staged 集合很大，或者包含环境文件、构建产物、二进制文件，这一步应视为必做。

### 4. 合并前先跑分支策略

```bash
python scripts/branch_policy.py develop
python scripts/branch_policy.py master
```

对于 `master`，应把“需要显式确认”当成硬规则，而不是建议。

## 脚本说明

### `git_snapshot.py`

输出仓库摘要，适合作为所有 Git 写操作前的第一步。

- 用法：`python scripts/git_snapshot.py [repo]`
- 关键参数：
  - `--commits`：最近提交数量
  - `--json`：输出 JSON

### `analyze_commit_language.py`

统计最近非 merge 提交的标题，判断仓库更偏中文、英文还是混合风格。

- 用法：`python scripts/analyze_commit_language.py [repo]`
- 关键参数：
  - `--commits`
  - `--json`

### `branch_policy.py`

检查目标分支是否需要显式确认后才能合并。

- 用法：`python scripts/branch_policy.py <target-branch>`
- 当前内置规则：
  - `develop`：无需额外确认
  - `master`：必须额外确认

### `validate_commit_message.py`

校验提交标题是否符合轻量规范或 Conventional Commits。

- 用法：`python scripts/validate_commit_message.py [--style auto|lightweight|conventional] "<message>"`
- 关键参数：
  - `--style auto`
  - `--style lightweight`
  - `--style conventional`
  - `--json`

### `pre_commit_audit.py`

审计 staged 或全部变更中的常见风险。

- 用法：`python scripts/pre_commit_audit.py [repo] --scope staged`
- 关键参数：
  - `--scope staged|all`
  - `--max-bytes`
  - `--json`

## 提交标题规范

### 轻量规范

格式：

```text
type: description
```

允许的 `type`：

- `fix`
- `add`
- `update`
- `style`
- `test`
- `revert`
- `build`

示例：

```text
fix: 修复接口超时问题
add: 新增活动页埋点
update: refresh docs landing copy
```

### Conventional Commits

格式：

```text
type(scope)!: description
```

常见 `type`：

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

示例：

```text
feat(auth): add passkey login
fix(api)!: remove legacy token format
docs(readme): clarify merge workflow
```

## 安全原则

- 先检查，再执行写操作
- 保留用户已有改动，不擅自清理工作区
- 默认避免 `git reset --hard`、`git clean -fd`、`git checkout -- <path>`、`git push --force`
- 真的需要强推时，优先 `git push --force-with-lease`
- 不绕过 hooks，除非用户明确要求
- 不静默提交 secrets、本地凭据和构建产物

## PowerShell 与 UTF-8

在 PowerShell 或包含中文路径、非 ASCII 文件名的仓库中，建议显式保留 UTF-8 输出，避免路径和日志乱码。

可以优先使用技能内脚本，或者运行 Git 时附带：

```bash
git -c core.quotepath=false -c i18n.logOutputEncoding=utf8 status --short --branch
```

## 参考文档

- `references/commit-message-convention.md`：轻量提交标题约定
- `references/conventional-commits.md`：Conventional Commits 说明
- `references/gitignore-patterns.md`：`.gitignore` 规则与示例
- `references/recovery-and-history-rewrite.md`：恢复与历史改写前的风险说明

## 适合接入的场景

- AI 代理接管“功能已完成，准备提交”的最后一段流程
- 统一团队对提交标题、分支合并和高风险命令的执行口径
- 给 Git 自动化、IDE 助手或 CLI 工具提供一个可复用的规则层
