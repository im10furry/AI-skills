# Data Flow And State Updates

这个文件用于页面和组件的数据流、`setData` 边界和状态更新。

## Core Model

- 页面和组件各自维护自己的 `data`
- 视图通过 WXML 绑定读取 `data`
- 状态变化最终通过 `setData` 进入渲染层
- 组件之间默认走“属性下传 + 事件上抛”

## High-Frequency Topics

- `Page().data` 与页面渲染
- `Component().data` 与 `properties`
- `setData` 粒度和性能
- `wx:if`、`wx:for` 与状态更新配合
- `observers` 在组件数据流中的角色
- 双向绑定属于进阶能力，不是默认方案

## Working Rules

- 只把渲染需要的数据放进 `data`
- 大对象、临时上下文、非渲染状态不要无脑塞进 `data`
- `setData` 优先做小粒度更新
- 组件数据流先求清晰，再谈抽象
- 排查渲染问题时，先看数据源，再看 WXML 绑定，再看 `setData`

## Common Mistakes

- 直接改 `this.data.xxx` 却不调用 `setData`
- 把复杂业务对象全量写入 `data`
- 页面和组件同时维护同一份状态却没有单一事实来源
- 为了省事用双向绑定掩盖数据流设计问题

## Official Links

- 页面  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html
- WXML  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/
- 事件  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html
- 自定义组件  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html
- `observers`  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/observer.html
- 双向绑定  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/two-way-bindings.html
- `setData` 优化  
  https://developers.weixin.qq.com/miniprogram/dev/framework/performance/tips/runtime_setData.html
