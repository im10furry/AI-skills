# Project Structure And Config

这个文件用于原生小程序目录结构、配置文件和注册入口。

## Common Structure

```text
.
├── app.js
├── app.json
├── app.wxss
├── project.config.json
├── sitemap.json
└── pages/
    └── index/
        ├── index.js
        ├── index.json
        ├── index.wxml
        └── index.wxss
```

## Configuration Layers

### Global

`app.json` 常见入口：

- `pages`
- `window`
- `tabBar`
- `usingComponents`
- `subpackages`
- `lazyCodeLoading`
- `sitemapLocation`

### Page

页面级 `*.json` 只覆盖当前页配置，常见用于：

- 导航栏样式
- 页面级组件注册
- 下拉刷新等页面行为

## Registration Layers

- `App({ ... })` 注册小程序实例
- `Page({ ... })` 注册页面实例
- 组件用 `Component({ ... })`

## Project Files

- `project.config.json` 主要属于开发者工具配置，不是运行时业务逻辑
- `app.json` 的首个 `pages` 项通常是默认入口页面
- 页面路径写逻辑路径，不带扩展名

## Common Pitfalls

- 把页面级配置误写进 `app.json`
- 页面路径和真实目录不一致
- 用构建工具改了生成结果，却没有回到真实小程序目录核对最终配置

## Official Links

- 配置  
  https://developers.weixin.qq.com/miniprogram/dev/framework/config.html
- 注册小程序  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/app.html
- 注册页面  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html
- 快速开始代码结构  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/code.html
