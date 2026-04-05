# Minimal Update Manager

```js
App({
  onLaunch() {
    const updateManager = wx.getUpdateManager()

    updateManager.onCheckForUpdate(() => {})

    updateManager.onUpdateReady(() => {
      wx.showModal({
        title: "更新提示",
        content: "新版本已经准备好，是否重启应用？",
        success(res) {
          if (res.confirm) {
            updateManager.applyUpdate()
          }
        }
      })
    })

    updateManager.onUpdateFailed(() => {
      wx.showToast({
        title: "更新失败",
        icon: "none"
      })
    })
  }
})
```

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.getUpdateManager.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onCheckForUpdate.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onUpdateReady.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.applyUpdate.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/update/UpdateManager.onUpdateFailed.html
