# APIs And Open Capabilities

这个文件用于把用户需求映射到正确的 `wx.*` API 或开放能力页面。

## Lookup Order

1. 先确认是不是内置组件已经覆盖
2. 再查 `wx.*` API
3. 涉及平台开放能力时，再查对应专题
4. 涉及服务端交互或消息推送时，再转服务端文档

## Common API Categories

- 路由与应用生命周期
- 界面与交互
- 网络请求
- 缓存与文件系统
- 媒体与位置
- 设备能力
- 登录与用户体系
- 支付、分享、订阅消息
- Worker 与后台能力

## Working Rules

- 先看 API 是否受基础库版本限制
- 先用 `wx.canIUse` 判断兼容性，再给降级方案
- 涉及登录、手机号、支付、订阅消息、用户信息时，不要猜合规路径
- 涉及网络、上传、下载、WebSocket 时，记得检查域名和 HTTPS 合法域名要求

## Official Links

- API 总览  
  https://developers.weixin.qq.com/miniprogram/dev/api/
- `wx.request`  
  https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html
- `wx.login`  
  https://developers.weixin.qq.com/miniprogram/dev/api/open-api/login/wx.login.html
- `wx.canIUse`  
  https://developers.weixin.qq.com/miniprogram/dev/api/base/system/wx.canIUse.html
- 路由 API  
  https://developers.weixin.qq.com/miniprogram/dev/api/base/app/app-route/wx.navigateTo.html
- 更新管理  
  https://developers.weixin.qq.com/miniprogram/dev/api/base/update/wx.getUpdateManager.html
- 服务端能力入口  
  https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/backend-api.html
