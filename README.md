#  `AI-skills` 技能仓库

> 把常用工作流整理成可复用的 skill，让重复问题不再重复解释。

`AI-skills` 是一个偏实战向的技能仓库，我自己会反复用到、也希望以后能持续扩展的 AI skill。
目前内容集中在三条主线：

- `Git` 工作流整理
- `ESP32 / ESP-IDF` 开发支持
- `Wechat` 平台开发支持

---

## 关于这个仓库

| 属性 | 内容 |
| --- | --- |
| `仓库名` | `AI-skills` |
| `定位` | 面向 AI Agent / Coding Agent 的技能仓库 |
| `当前状态` | 持续补全中，先把高频、能落地的部分做好 |


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

### `Wechat` 分支

| Skill | 作用 |
| --- | --- |
| `wechat-miniprogram` | 处理微信小程序原生开发、调试、组件/API 选型、性能优化、发布审核、隐私合规与设计规范问题 |
| `wechat-pay` | 处理微信支付接入、模式选择、签名验签、回调、退款、对账、官方 SDK 与文档路由问题 |

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
├─ Wechat/
│  ├─ wechat-miniprogram/
│  │  ├─ SKILL.md
│  │  ├─ agents/
│  │  └─ references/
│  └─ wechat-pay/
│     ├─ SKILL.md
│     ├─ agents/
│     └─ references/
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

npx skills add https://github.com/im10furry/AI-skills
