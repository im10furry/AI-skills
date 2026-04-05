# Minimal Custom Component

```js
// components/user-card/index.js
Component({
  properties: {
    name: {
      type: String,
      value: ""
    }
  },
  methods: {
    onTap() {
      this.triggerEvent("select", {
        name: this.properties.name
      })
    }
  }
})
```

```xml
<!-- components/user-card/index.wxml -->
<view bindtap="onTap">{{name}}</view>
```

```json
{
  "usingComponents": {
    "user-card": "/components/user-card/index"
  }
}
```

```xml
<user-card name="{{userName}}" bind:select="onSelectUser" />
```

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/component.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/events.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/lifetimes.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/custom-component/wxml-wxss.html
