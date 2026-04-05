# Components

这个文件用于内置组件选型和自定义组件开发。

## Built-In Components

先从官方组件库选型，再决定是否自定义。高频分类包括：

- 视图容器
- 基础内容
- 表单
- 导航
- 媒体
- 地图与画布
- 开放能力

## Custom Component Baseline

高频结构：

- `properties`
- `data`
- `methods`
- `lifetimes`
- `observers`

常见专题：

- 插槽 `slot`
- 样式隔离
- 组件事件 `triggerEvent`
- `behaviors`
- `relations`
- `pureDataPattern`
- `componentGenerics`

## Working Rules

- 能用官方组件时，不要先造自定义组件
- 组件通信优先“属性下传 + 事件上抛”
- 样式问题先检查样式隔离和宿主样式边界
- 复用横切逻辑时优先看 `behaviors`

## Official Links

- 组件总览  
  https://developers.weixin.qq.com/miniprogram/dev/component/
- 自定义组件总览  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/
- Component 构造器  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html
- 生命周期  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html
- 组件事件  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html
- 组件模板与样式  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html
- behaviors  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/behaviors.html
- relations  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/relations.html
