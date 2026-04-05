---
name: wechat-miniprogram
description: 微信小程序原生开发、调试、组件与 API 选型、性能优化、发布审核、隐私合规与设计规范导航。Use when working on WeChat Mini Program files such as app.json, project.config.json, Page(), Component(), wx.*, WXML/WXSS, DevTools/CI, release, privacy, accessibility, elderly-mode, or when mapping a request to the correct official doc page.
---

# 微信小程序开发

## Overview

- 优先以微信开放文档为准，不要猜基础库版本、审核规则、隐私要求、插件限制、Skyline 兼容性。
- 先判断任务属于 `core`、`design`、`extended` 还是 `examples`，只读相关文件，不要把整套资料一次性读完。
- 如果仓库是 `Taro`、`uni-app`、`Remax` 等跨端框架输出到微信小程序，用这个 skill 只处理底层平台约束；构建链和框架语法回到对应框架文档。
- 对“必须精确”的内容保持保守：配置字段、API 参数、审核要求、隐私接入、域名规则、体验评分细则都应回到官方页核对。

## Workflow

1. 先判断项目类型和任务类型。
   - 项目是原生小程序，还是跨端框架产物。
   - 当前任务是实现、调试、代码评审、发布排查、设计检查，还是隐私合规。

2. 再判断改动触及哪一层。
   - `app` 与全局配置：`app.js`、`app.json`、`app.wxss`、`project.config.json`
   - 页面与视图层：`Page()`、WXML、WXSS、事件、动画、模板
   - 组件层：`Component()`、组件通信、插槽、生命周期
   - 能力层：`wx.*` API、登录、请求、缓存、文件系统、开放能力
   - 运行与发布层：路由、页面栈、更新机制、开发者工具、CI、上传审核

3. 按问题类型读取最小必要参考。
   - 项目起步、目录、配置、发布主线：读取 `references/core/overview-and-quickstart.md`
   - `app.json`、页面配置、目录结构：读取 `references/core/project-structure-and-config.md`
   - 生命周期、路由、页面栈、场景值：读取 `references/core/runtime-routing-and-lifecycle.md`
   - 冷热启动、运行环境、更新管理：读取 `references/core/runtime-environment-and-update-mechanism.md`
   - WXML、WXSS、事件：读取 `references/core/view-layer-and-events.md`
   - `template`、`include`、`wxs`、动画：读取 `references/core/view-templates-wxs-and-animation.md`
   - 内置组件、自定义组件、组合方式：读取 `references/core/components.md` 和 `references/core/components-and-composition.md`
   - `wx.*` API、开放能力：读取 `references/core/apis-and-open-capabilities.md`
   - 请求、缓存、文件系统：读取 `references/core/network-storage-and-file-system.md`
   - `data`、`setData`、页面与组件数据流：读取 `references/core/data-flow-and-state-updates.md`
   - 开发者工具、上传发布、合规入口：读取 `references/core/devtools-release-and-compliance.md`
   - 工具设置、调试面板、`project.config.json`：读取 `references/core/devtools-project-config-and-settings.md`

4. 高频问题优先走场景路由。
   - 登录、鉴权、网络请求、域名白名单、分包、审核、隐私、适配这类高频问题，先读 `references/common-task-routing.md`
   - 需要最小可复制骨架时，再读 `references/examples/` 下对应示例

5. 输出时保持最短可执行路径。
   - 先给任务归类、应打开的文档和最小改法
   - 再补约束、兼容性、审核或隐私风险
   - 如果结论是基于文档结构推断，而不是官方页面明说，要明确标注为推断

## Reference Files

### Core

- `references/core/overview-and-quickstart.md`
  - 项目起步、目录概览、工具链、协同与发布入口。
- `references/core/project-structure-and-config.md`
  - `app.json`、页面配置、目录结构和注册入口。
- `references/core/runtime-routing-and-lifecycle.md`
  - `App()`、`Page()` 生命周期，路由与页面栈。
- `references/core/runtime-environment-and-update-mechanism.md`
  - 运行环境、冷热启动、场景值、更新管理。
- `references/core/view-layer-and-events.md`
  - WXML、WXSS、事件绑定与视图层规则。
- `references/core/view-templates-wxs-and-animation.md`
  - `template`、`include`、`wxs`、动画与双向绑定。
- `references/core/components.md`
  - 内置组件、自定义组件和常用能力入口。
- `references/core/components-and-composition.md`
  - 组件通信、组合模式和复用约束。
- `references/core/apis-and-open-capabilities.md`
  - `wx.*` API 和开放能力主入口。
- `references/core/network-storage-and-file-system.md`
  - 请求、下载、缓存、存储和文件系统。
- `references/core/data-flow-and-state-updates.md`
  - 页面和组件的数据流，`setData` 使用边界。
- `references/core/devtools-release-and-compliance.md`
  - 开发者工具、CI、上传发布、体验评分与基础合规入口。
- `references/core/devtools-project-config-and-settings.md`
  - `project.config.json`、调试面板、编译设置和日常排障入口。

### Design

- `references/design/accessibility-and-adapt.md`
  - 无障碍与适配主线。
- `references/design/guidelines-and-accessibility.md`
  - 更精简的设计评审基线。
- `references/design/elderly-mode.md`
  - 适老化要求和入口。

### Extended

- `references/extended/performance-compatibility-and-subpackages.md`
  - 性能、兼容性、分包与降级策略。
- `references/extended/quality-audits-and-experience-score.md`
  - 体验评分、质量审计和排查方向。
- `references/extended/security-domain-and-gateway.md`
  - 域名、HTTPS、安全、内容安全和网关能力。
- `references/extended/operation-and-privacy.md`
  - 健康运营、隐私接入和隐私合规。
- `references/extended/cloud-development-and-wxcloud.md`
  - 云开发、数据库、存储、HTTP API。
- `references/extended/plugins-functional-pages-and-server-side.md`
  - 插件、功能页、服务端能力。
- `references/extended/server-side-backend-api-and-message-push.md`
  - 后端 API 与消息推送。
- `references/extended/open-abilities-and-growth-capabilities.md`
  - 开放能力、运营增长与业务能力入口。
- `references/extended/platform-capabilities-business-and-industry.md`
  - 商业、行业、多端平台能力。
- `references/extended/worker-wasm-and-runtime-env.md`
  - Worker、WASM 和特殊运行环境。
- `references/extended/advanced-view-rendering-and-interaction.md`
  - 高级动画、渲染与交互缓存。
- `references/extended/glass-easel-and-advanced-components.md`
  - Glass-Easel 和高级组件能力。
- `references/extended/skyline-runtime.md`
  - Skyline 运行时。
- `references/extended/skyline-glass-easel-and-advanced-rendering.md`
  - Skyline / Glass-Easel / 高级渲染的合并综述。
- `references/extended/testing-automation-and-quality.md`
  - 自动化测试、Automator、MiniTest 和质量平台。

### Routing

- `references/common-task-routing.md`
  - 高频问题到参考文件和官方入口的快速路由。

### Examples
- `references/examples/minimal-app-and-config.md`
  - `app` 与全局配置骨架。
- `references/examples/minimal-app-and-page.md`
  - 最小 `app/page` 骨架。
- `references/examples/minimal-page-data-binding.md`
  - 页面数据绑定骨架。
- `references/examples/minimal-routing-and-page-stack.md`
  - 路由与页面栈骨架。
- `references/examples/minimal-custom-component.md`
  - 自定义组件骨架。
- `references/examples/custom-component-patterns.md`
  - 组件复用与组合模式。
- `references/examples/minimal-api-request-login.md`
  - 登录与请求最小示例。
- `references/examples/minimal-update-manager.md`
  - 更新管理骨架。
- `references/examples/minimal-scene-and-launch-options.md`
  - 场景值和启动参数骨架。
- `references/examples/minimal-tabbar-and-subpackage-config.md`
  - `tabBar` 和分包配置骨架。

### Official Entry

- `references/official-docs.md`
  - 微信开放文档主入口与高频查阅顺序。

## What To Confirm Before Acting

- 是原生微信小程序，还是跨端框架输出到微信小程序
- 目标任务是实现、调试、评审、发布、设计还是合规
- 当前改动触及 `app`、页面、组件、插件、分包、服务端能力中的哪一层
- 是否涉及登录、支付、用户信息、手机号、订阅消息、隐私弹窗、域名白名单、审核发布
- 是否存在基础库版本、机型兼容、Skyline、插件、功能页等限制

如果仓库里已经能读出这些信息，优先从代码和配置中提取，不要先问用户。

## Answering Standards

- 先把任务归类，再给最短可执行路径，不要先铺长篇背景。
- 写代码时优先给最小原生骨架，不要先堆抽象层。
- 做 review 时优先指出行为风险、兼容性风险、审核风险、隐私风险和缺少的测试点。
- 给规则时尽量附上对应官方文档页；遇到基础库、审核、隐私、插件、Skyline 等易变主题时，明确说明“以下结论应以当前官方文档为准”。
- 输出中明确区分“官方页面已验证的信息”和“基于文档结构的推断”。
