# Official Docs

优先用微信开放文档的当前页面，不要用记忆代替规则。

## Primary Entry Points

- 开发框架总览  
  https://developers.weixin.qq.com/miniprogram/dev/framework/
- 快速开始  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/
- 组件总览  
  https://developers.weixin.qq.com/miniprogram/dev/component/
- API 总览  
  https://developers.weixin.qq.com/miniprogram/dev/api/
- 开发者工具  
  https://developers.weixin.qq.com/miniprogram/dev/devtools/devtools
- 设计总览  
  https://developers.weixin.qq.com/miniprogram/design/

## Core Lookup Order

1. 项目初始化、目录、示例、协同与发布：
   - `quickstart/`
2. 目录、`app.json`、页面配置：
   - `framework/config.html`
3. 生命周期、路由、运行机制：
   - `framework/app-service/`
   - `framework/runtime/`
4. WXML、WXSS、事件：
   - `framework/view/`
5. 自定义组件：
   - `framework/custom-component/`
6. API 和开放能力：
   - `dev/api/`
7. 调试、CI、上传发布：
   - `dev/devtools/`

## Advanced Lookup Order

- 性能与兼容：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/performance/
  - https://developers.weixin.qq.com/miniprogram/dev/framework/compatibility.html
- 分包：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/subpackages.html
- 体验评分与审计：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/audits/audits.html
- Skyline：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/runtime/skyline/introduction.html
- Glass-Easel：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/glass-easel/introduction.html
- 云开发：
  - https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/basis/getting-started.html
  - https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/basis/capabilities.html
  - https://developers.weixin.qq.com/miniprogram/dev/wxcloudservice/wxcloud/guide/database.html
- 服务端与消息推送：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/backend-api.html
  - https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html
- 平台能力：
  - https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/business-capabilities/
  - https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/industry/
  - https://developers.weixin.qq.com/miniprogram/dev/platform-capabilities/miniapp/intro/intro
- 安全与域名：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/ability/domain.html
  - https://developers.weixin.qq.com/miniprogram/dev/framework/ability/HTTPDNS.html
  - https://developers.weixin.qq.com/miniprogram/security/basic/
- Worker 与 WASM：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/workers.html
  - https://developers.weixin.qq.com/miniprogram/dev/framework/performance/wasm.html
- 插件与功能页：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/plugin/
- 服务端能力：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/backend-api.html
- 隐私：
  - https://developers.weixin.qq.com/miniprogram/dev/framework/user-privacy/miniprogram-intro.html

## Design Entry Points

- 设计指南  
  https://developers.weixin.qq.com/miniprogram/design/
- 无障碍  
  https://developers.weixin.qq.com/miniprogram/design/accessibility.html
- 适配  
  https://developers.weixin.qq.com/miniprogram/design/adapt.html
- 适老化  
  https://developers.weixin.qq.com/miniprogram/design/elderly.html

## Rule

涉及下面主题时，不要只靠 skill 内摘要，必须回到官方页核对：

- 基础库版本与兼容性
- 体验评分细项
- 审核与发布规则
- 隐私弹窗与授权要求
- 插件、功能页、Skyline、Glass-Easel
