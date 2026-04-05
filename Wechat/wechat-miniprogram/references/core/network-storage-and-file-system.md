# Network Storage And File System

这个文件用于网络请求、本地缓存、文件系统和资源落地。

## Scope

读取本文件的典型场景：

- `wx.request`
- 上传下载
- WebSocket
- 本地缓存
- 临时文件和持久文件
- 离线资源落地
- 合法域名和 HTTPS 检查

## Network Baseline

- 先确认请求侧是前端 `wx.request` 还是服务端 API
- 前端访问受合法域名和 HTTPS 约束
- 弱网、超时、重试和加载态要单独设计，不要只写 happy path
- 需要网络优化时，再去看预拉取和弱网专题

## Storage Baseline

- 小体量本地状态优先用存储 API
- 存储问题要区分“短期缓存”和“长期持久化”
- 存储只是本地副本，不等于服务端真值

## File System Baseline

- 先分清临时文件、用户文件、下载文件
- 文件系统经常和上传下载、图片、音视频、离线包配合使用
- 文件落地后再决定是否要缓存路径、上传或删除

## Common Combination Patterns

- 请求后缓存结果到 storage
- 下载后把资源转成文件路径复用
- 需要离线可用时，用文件系统而不是只留内存状态
- 业务失败先查网络，再查域名白名单，再查文件和权限边界

## Working Rules

- 涉及域名或网络连通性时，优先读域名文档
- 涉及资源持久化时，优先判断 storage 还是 file system 更合适
- 涉及大文件、音视频、离线资源时，不要只靠 storage

## Official Links

- 网络  
  https://developers.weixin.qq.com/miniprogram/dev/framework/ability/network.html
- 存储  
  https://developers.weixin.qq.com/miniprogram/dev/framework/ability/storage.html
- 文件系统  
  https://developers.weixin.qq.com/miniprogram/dev/framework/ability/file-system.html
- 业务域名  
  https://developers.weixin.qq.com/miniprogram/dev/framework/ability/domain.html
- `wx.request`  
  https://developers.weixin.qq.com/miniprogram/dev/api/network/request/wx.request.html
