# Minimal Page Data Binding

```js
Page({
  data: {
    loading: false,
    count: 0,
    items: ["A", "B"]
  },
  onLoad() {},
  onShow() {},
  onTapAdd() {
    this.setData({
      count: this.data.count + 1
    })
  }
})
```

```xml
<view wx:if="{{!loading}}">
  <text>{{count}}</text>
  <button bindtap="onTapAdd">+1</button>
  <view wx:for="{{items}}" wx:key="*this">{{item}}</view>
</view>
```

```css
.counter {
  padding: 24rpx;
}
```

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/page-life-cycle.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/
- https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxml/event.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/view/wxss.html
