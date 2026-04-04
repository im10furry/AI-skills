# 欢迎来到 `AI-skills` 的技能仓库

> 把常用工作流整理成可复用的 skill，让重复问题不再重复解释。

`AI-skills` 是一个偏实战向的技能仓库，主要收录我自己会反复用到、也希望以后能持续扩展的 AI skill。
目前内容集中在两条主线：

- `Git` 工作流整理
- `ESP32 / ESP-IDF` 开发支持

---

## 关于这个仓库

| 属性 | 内容 |
| --- | --- |
| `仓库名` | `AI-skills` |
| `定位` | 面向 AI Agent / Coding Agent 的技能仓库 |
| `当前状态` | 持续补全中，先把高频、能落地的部分做好 |
| `内容风格` | 不是堆资料，而是把任务拆成能直接执行的工作流 |
| `关注方向` | `Git` / `ESP32` / `ESP-IDF` / `Automation` |
| `附带内容` | `references` / `agents` / `scripts` |

## 当前任务栏

- 正在整理：`Git` 提交规范、历史整理、仓库初始化这类高频动作
- 正在补全：`ESP32` 固件开发、构建、OTA、分区、发布相关流程
- 想做成的样子：每个 skill 都能直接告诉 agent “先看哪里，再怎么做”
- 特殊设定：比起大而全，我更在意“看完就能用”

## 技能树

### `Git` 分支

| Skill | 作用 |
| --- | --- |
| `git-init` | 开始编码前先确认目标目录是否已经在 Git 仓库中 |
| `git commit` | 检查仓库状态、整理提交、处理安全的 Git 操作 |
| `git-rganize-commit` | 重组脏工作区或本地提交历史，让提交更聚焦 |

注：目录名 `Git/git-standard/` 当前对外暴露的 skill 名是 `git commit`。

### `ESP` 分支

| Skill | 作用 |
| --- | --- |
| `esp-idf-dev` | 处理 ESP-IDF 项目的配置、编译、烧录、组件与 OTA 工作流 |
| `esp32-development` | 处理 ESP32 系列固件开发、评审、架构、外设、低功耗与发布问题 |

## 仓库结构

```text
AI-skills/
├─ ESP/
│  ├─ esp-idf-dev/
│  │  ├─ SKILL.md
│  │  ├─ agents/
│  │  └─ references/
│  └─ esp32-development/
│     ├─ SKILL.md
│     ├─ references/
│     └─ scripts/
└─ Git/
   ├─ git-init/
   │  └─ SKILL.md
   ├─ git-standard/
   │  ├─ SKILL.md
   │  ├─ agents/
   │  └─ references/
   └─ git-rganize-commit/
      ├─ SKILL.md
      ├─ agents/
      └─ references/
```

## 使用方式

1. 先按主题进入对应目录。
2. 从 `SKILL.md` 开始读，它是这个 skill 的主入口。
3. 需要细节时，再按说明读取 `references/` 里的专题文档。
4. 如果你的平台支持技能元信息，可以继续使用 `agents/openai.yaml`。
5. 有辅助脚本的 skill，再按需执行 `scripts/` 中的内容。

## 这个仓库适合谁

- 想把常见开发动作整理成稳定 prompt / workflow 的人
- 经常处理 `Git` 状态、提交规范、历史整理的人
- 在做 `ESP32 / ESP-IDF` 项目，需要工程化知识沉淀的人
- 不想每次都从零解释上下文，而是希望 agent 先读规范再动手的人

## Fun Fact

- 我不太喜欢只放一句“这是一个仓库”式 README。
- 对我来说，skill 不只是资料收纳，它更像是给 agent 准备好的行动脚本。
- 如果一个目录只有信息堆砌、没有执行路径，那它还不算合格。

---

Made for reusable workflows, cleaner context, and less repeated explanation.
