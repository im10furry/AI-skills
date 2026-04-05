# Minimal App And Page

用于提供最小原生示例。示例保持保守，只覆盖高频结构。

## App Skeleton

```json
{
  "pages": [
    "pages/index/index"
  ],
  "window": {
    "navigationBarTitleText": "Demo"
  }
}
```

```js
App({
  onLaunch() {
    console.log("app launch")
  }
})
```

## Page Skeleton

```js
Page({
  data: {
    count: 0
  },
  onLoad() {
    console.log("page load")
  },
  handleTap() {
    this.setData({
      count: this.data.count + 1
    })
  }
})
```

```xml
<view class="page">
  <text class="value">{{count}}</text>
  <button bindtap="handleTap">+1</button>
</view>
```

```css
.page {
  padding: 32rpx;
}

.value {
  display: block;
  margin-bottom: 24rpx;
}
```

## Notes

- 路径写到 `pages` 时不带扩展名。
- 按钮点击用 `bindtap` 即可覆盖大多数基础交互。
- `setData` 只更新渲染所需字段。

## Key Official Links

- 快速开始代码结构  
  https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/code.html
- 注册页面  
  https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html
- 事件系统  
  https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html

