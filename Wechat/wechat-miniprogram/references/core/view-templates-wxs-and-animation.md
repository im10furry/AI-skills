# View Templates Wxs And Animation

这个文件用于视图层模板复用、WXS 和常见动画能力。

## Scope

- `template`
- `include`
- `wxs`
- selector
- 动画
- 交互动画
- 双向绑定
- 初始渲染缓存

## Working Rules

- 基础页面渲染优先用普通 WXML 绑定
- 模板复用先用 `template` 或 `include`，不要过早上复杂组件系统
- `wxs` 只用于明确需要的视图层辅助逻辑
- 双向绑定是进阶能力，不应成为默认答案
- 动画问题先分清普通动画、交互动画和 Skyline 级别问题

## Official Links

- 动画  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html
- 交互动画  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/interactive-animation.html
- 双向绑定  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/two-way-bindings.html
- 初始渲染缓存  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/initial-rendering-cache.html
- WXML 入口  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/
- WXS 入口  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxs/
