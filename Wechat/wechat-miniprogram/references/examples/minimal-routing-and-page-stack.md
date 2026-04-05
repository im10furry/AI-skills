# Minimal Routing And Page Stack

```js
Page({
  goDetail() {
    wx.navigateTo({
      url: "/pages/detail/detail?id=42"
    })
  },
  replaceDetail() {
    wx.redirectTo({
      url: "/pages/detail/detail?id=42"
    })
  },
  backHomeTab() {
    wx.switchTab({
      url: "/pages/index/index"
    })
  },
  resetToHome() {
    wx.reLaunch({
      url: "/pages/index/index"
    })
  },
  goBack() {
    wx.navigateBack()
  }
})
```

规则：

- `tabBar` 页面用 `switchTab`
- 要重置路由栈时用 `reLaunch`
- 不要用页面栈绕过清晰的参数传递

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/framework/app-service/route.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.navigateTo.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.redirectTo.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.switchTab.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.reLaunch.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.navigateBack.html
