# Server Side Backend Api And Message Push

这个文件用于服务端后端 API、消息推送和服务端职责边界。

## Scope

- 后端 API 调用
- 消息推送
- 服务端通知链路
- 服务端与前端职责划分

## Working Rules

- 先区分这是前端 `wx.*` 还是服务端接口
- 服务端能力通常依赖服务端凭证、鉴权和回调链路
- 消息推送和开放能力经常有关联，但不要把它们混成一层
- 当前 skill 只做路由和边界提示，具体参数仍应回到官方页

## Official Links

- 后端 API  
  https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/backend-api.html
- 消息推送  
  https://developers.weixin.qq.com/miniprogram/dev/framework/server-ability/message-push.html
- 服务端接口凭证入口  
  https://developers.weixin.qq.com/miniprogram/dev/server/API/
