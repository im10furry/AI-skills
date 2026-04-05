# Minimal Api Request Login

```js
function request(url, data = {}) {
  return new Promise((resolve, reject) => {
    wx.request({
      url,
      method: "GET",
      data,
      success: resolve,
      fail: reject
    })
  })
}

Page({
  data: {
    loading: false,
    code: ""
  },
  async onLoad() {
    if (!wx.canIUse("login")) return
    this.setData({ loading: true })
    try {
      const loginRes = await wx.login()
      this.setData({ code: loginRes.code })
    } finally {
      this.setData({ loading: false })
    }
  }
})
```

官方链接：

- https://developers.weixin.qq.com/miniprogram/dev/api/
- https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html
- https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html
- https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.canIUse.html
