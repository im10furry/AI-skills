# Components And Composition

用于处理自定义组件、组件通信、复用和复杂组件组织方式。

## Core Points

- 自定义组件统一从 `Component()` 开始。
- 组件基础关注项：
  - `properties`
  - `data`
  - `methods`
  - 生命周期
  - 事件
  - 插槽
- 需要复用横切逻辑时，优先看 `behaviors`。
- 需要组件关系和父子协同时，优先看 `relations`。
- 需要细粒度数据监听时，优先看 `observers`。
- 需要大对象但不参与渲染时，优先看纯数据字段。
- 高级泛化和进阶能力，再看 `generics`、`glass-easel` 和高级组件文档。

## Working Defaults

- 页面能完成的简单结构，不要过早抽成复杂组件系统。
- 组件对外接口先收敛到 `properties` 和自定义事件。
- 样式问题先确认 `styleIsolation` 和组件模板结构。

## Key Official Links

- 自定义组件总览  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/
- `Component()`  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html
- 生命周期  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html
- 事件  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html
- 模板和样式  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html
- `behaviors`  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html
- `relations`  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/relations.html
- `observers`  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/observer.html

