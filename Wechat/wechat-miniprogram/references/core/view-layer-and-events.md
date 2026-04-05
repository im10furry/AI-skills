# View Layer And Events

这个文件用于 WXML、WXSS、事件系统和模板层规则。

## WXML Basics

高频点：

- 插值：`{{}}`
- 条件渲染：`wx:if`
- 列表渲染：`wx:for`
- 模板复用：`template`、`include`
- 事件绑定：`bind*`、`catch*`

## WXSS Basics

- 优先使用 `rpx` 做相对尺寸
- 常规布局优先 `flex`
- 样式问题先确认是页面样式、组件样式还是样式隔离导致

## Event Rules

- `bind*` 让事件继续冒泡
- `catch*` 截断冒泡
- 复杂交互先确认事件源、事件类型和数据绑定是否对齐

## Working Defaults

- 模板层做展示和轻逻辑，复杂业务逻辑放回 JS
- 列表渲染优先保证数据结构稳定，减少无意义重绘
- 表单和交互组件优先选内置能力，再补自定义组件

## Official Links

- 视图层入口  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/
- WXML  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/
- 事件系统  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html
- WXSS  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxss.html
- 动画  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/animation.html
