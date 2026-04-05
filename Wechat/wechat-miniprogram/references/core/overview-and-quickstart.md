# Overview And Quickstart

这个文件用于把一个微信小程序任务快速映射到原生开发闭环。

## Native Mini Program Baseline

一个典型原生项目至少包含：

- `app.js`
- `app.json`
- `app.wxss`
- `pages/**`
- `project.config.json`
- 可选：`sitemap.json`

## Default Workflow

1. 确认是不是原生微信小程序任务
2. 在开发者工具中打开项目
3. 先确认 `app.json`、入口页面、页面路径、组件注册方式
4. 本地编译和预览
5. 真机验证
6. 需要交付时再进入上传、审核、发布流程

## When To Read Next

- 要看目录和配置：读 [project-structure-and-config.md](project-structure-and-config.md)
- 要看生命周期和路由：读 [runtime-routing-and-lifecycle.md](runtime-routing-and-lifecycle.md)
- 要找组件或 API：分别读 [components.md](components.md) 和 [apis-and-open-capabilities.md](apis-and-open-capabilities.md)
- 要找工具、CI、发布、合规：读 [devtools-release-and-compliance.md](devtools-release-and-compliance.md)

## Official Links

- 快速开始  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/
- 快速开始里的代码结构  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/code.html
- 快速开始里的框架说明  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/framework.html
- 协同工作与发布  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/release.html

## Working Defaults

- 默认给最小可运行骨架，不先引入复杂状态管理
- 默认用官方框架能力解释问题，不先引入第三方包装层
- 遇到发布或审核问题时，先把问题拆成“工具流程”和“平台规则”两部分
