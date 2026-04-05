# Minimal App And Config

```js
// app.js
App({
  globalData: {
    userInfo: null
  },
  onLaunch() {},
  onShow() {}
})
```

```json
{
  "pages": [
    "pages/index/index"
  ],
  "window": {
    "navigationBarTitleText": "Demo"
  },
  "tabBar": {
    "list": [
      {
        "pagePath": "pages/index/index",
        "text": "首页"
      }
    ]
  }
}
```

```json
{
  "navigationBarTitleText": "首页"
}
```

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/framework/quickstart/code.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/config.html
- https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/app.html
