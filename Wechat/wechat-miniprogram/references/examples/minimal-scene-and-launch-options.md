# Minimal Scene And Launch Options

```js
App({
  onLaunch() {
    const launchOptions = wx.getLaunchOptionsSync()
    console.log("launch scene", launchOptions.scene)
  },
  onShow() {
    const enterOptions = wx.getEnterOptionsSync()
    console.log("enter scene", enterOptions.scene)
  }
})
```

规则：

- 场景值只用于分流和埋点，不要把复杂业务硬编码到单个场景分支
- 进入来源判断优先集中在 `App` 或入口页

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/scene.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getLaunchOptionsSync.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/life-cycle/wx.getEnterOptionsSync.html
