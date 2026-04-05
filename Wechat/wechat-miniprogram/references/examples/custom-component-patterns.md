# Custom Component Patterns

用于提供高频自定义组件示例。

## Minimal Component

```js
Component({
  properties: {
    title: {
      type: String,
      value: ""
    }
  },
  data: {
    expanded: false
  },
  methods: {
    toggle() {
      const expanded = !this.data.expanded
      this.setData({ expanded })
      this.triggerEvent("toggle", { expanded })
    }
  }
})
```

```xml
<view class="card">
  <view class="header" bindtap="toggle">{{title}}</view>
  <view wx:if="{{expanded}}" class="body">
    <slot />
  </view>
</view>
```

```json
{
  "component": true
}
```

## Parent Usage

```json
{
  "usingComponents": {
    "expand-card": "/components/expand-card/index"
  }
}
```

```xml
<expand-card title="详情" bind:toggle="handleToggle">
  <text>content</text>
</expand-card>
```

## Notes

- 对外输入优先放 `properties`。
- 对外输出优先用自定义事件。
- 组件是否渲染内容，优先用自身 `data` 控制。

## Key Official Links

- 自定义组件总览  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/
- `Component()`  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html
- 组件事件  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html
- 模板和样式  
  https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html
