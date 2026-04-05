# Common Task Routing

这个文件用于把高频微信小程序问题快速路由到对应参考文件和官方入口。

## 使用方式

先按问题类型定位，再补读最小必要文件，不要一次把全部参考资料读完。

## 高频场景

### 1. 项目初始化、目录和配置

适用问题：

- `app.json` 怎么写
- 页面为什么没注册成功
- `project.config.json` 该不该改
- 默认首页、`tabBar`、全局样式放哪里

优先读取：

- `references/core/overview-and-quickstart.md`
- `references/core/project-structure-and-config.md`
- `references/examples/minimal-app-and-config.md`
- `references/examples/minimal-tabbar-and-subpackage-config.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/
- https://developers.weixin.qq.com/miniprogram/dev/framework/config.html

### 2. 生命周期、路由和页面栈

适用问题：

- `onLoad`、`onShow`、`onReady` 触发顺序
- `navigateTo` / `redirectTo` / `switchTab` 怎么选
- 页面返回后为什么状态变了
- 场景值、启动参数、更新管理怎么接

优先读取：

- `references/core/runtime-routing-and-lifecycle.md`
- `references/core/runtime-environment-and-update-mechanism.md`
- `references/examples/minimal-routing-and-page-stack.md`
- `references/examples/minimal-scene-and-launch-options.md`
- `references/examples/minimal-update-manager.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/
- https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/

### 3. 页面渲染、事件和数据更新

适用问题：

- WXML 条件渲染和列表渲染
- 事件绑定不生效
- `setData` 太慢或更新不对
- 模板、动画、`wxs` 怎么接

优先读取：

- `references/core/view-layer-and-events.md`
- `references/core/view-templates-wxs-and-animation.md`
- `references/core/data-flow-and-state-updates.md`
- `references/examples/minimal-page-data-binding.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/view/
- https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips/runtime_setData.html

### 4. 组件封装和通信

适用问题：

- 自定义组件怎么拆
- 父子组件怎么传值
- 插槽、生命周期、复用边界怎么定

优先读取：

- `references/core/components.md`
- `references/core/components-and-composition.md`
- `references/examples/minimal-custom-component.md`
- `references/examples/custom-component-patterns.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/
- https://developers.weixin.qq.com/miniprogram/dev/component/

### 5. 登录、请求、缓存和文件系统

适用问题：

- `wx.login` 怎么配合后端鉴权
- `wx.request` 失败或返回异常
- 缓存、下载、上传、文件读写怎么做

优先读取：

- `references/core/apis-and-open-capabilities.md`
- `references/core/network-storage-and-file-system.md`
- `references/examples/minimal-api-request-login.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/api/
- https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html
- https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html

### 6. 域名、HTTPS、安全和内容安全

适用问题：

- 请求域名不合法
- 真机可复现、开发者工具不可复现
- 内容安全、风控、安全通知怎么处理

优先读取：

- `references/extended/security-domain-and-gateway.md`
- `references/core/devtools-release-and-compliance.md`
- `references/official-docs.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/ability/domain.html
- https://developers.weixin.qq.com/miniprogram/security/basic/
- https://developers.weixin.qq.com/miniprogram/security/content/

### 7. 性能、兼容性和分包

适用问题：

- 首屏慢、切页卡、弱网体验差
- 主包过大
- 基础库兼容怎么做
- 是否需要普通分包、独立分包或预下载

优先读取：

- `references/extended/performance-compatibility-and-subpackages.md`
- `references/extended/quality-audits-and-experience-score.md`
- `references/core/data-flow-and-state-updates.md`
- `references/examples/minimal-tabbar-and-subpackage-config.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/performance/
- https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html

### 8. 开发者工具、调试、CI 和发布

适用问题：

- 编译、预览、调试面板怎么用
- `project.config.json` 某项配置的意义
- CLI / CI 上传发布怎么走
- 审核前要先看什么

优先读取：

- `references/core/devtools-release-and-compliance.md`
- `references/core/devtools-project-config-and-settings.md`
- `references/extended/quality-audits-and-experience-score.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools
- https://developers.weixin.qq.com/miniprogram/dev/devtools/ci.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/release.html

### 9. 隐私合规、运营规范和审核风险

适用问题：

- 隐私弹窗和授权接入
- 个人信息收集说明
- 插件隐私要求
- 上线前合规检查

优先读取：

- `references/extended/operation-and-privacy.md`
- `references/core/devtools-release-and-compliance.md`
- `references/design/accessibility-and-adapt.md`
- `references/design/elderly-mode.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/
- https://developers.weixin.qq.com/miniprogram/dev/framework/operation.html
- https://developers.weixin.qq.com/miniprogram/design/

### 10. Skyline、Glass-Easel、云开发、插件和高级能力

适用问题：

- Skyline 是否可用、如何迁移
- Glass-Easel 和高级组件能力
- 云函数、数据库、存储
- 插件、功能页、服务端消息推送

优先读取：

- `references/extended/skyline-runtime.md`
- `references/extended/glass-easel-and-advanced-components.md`
- `references/extended/skyline-glass-easel-and-advanced-rendering.md`
- `references/extended/cloud-development-and-wxcloud.md`
- `references/extended/plugins-functional-pages-and-server-side.md`
- `references/extended/server-side-backend-api-and-message-push.md`

官方入口：

- https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/introduction.html
- https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/basis/getting-started.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/

## 输出提醒

- 先给当前问题应该读哪几个文件，再给结论。
- 如果问题涉及基础库、审核、隐私、插件、Skyline 或安全，必须提醒以当前官方文档为准。
- 如果仓库明显不是原生小程序，而是跨端框架生成结果，要先标注这是“平台约束层”问题还是“框架层”问题。
