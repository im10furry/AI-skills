# 微信支付规则与核对清单

## 已核验的官方页面快照

- `JSAPI支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012062524 ，官方更新时间 `2025.07.15`
- `JSAPI支付 / 开发指引`：https://pay.weixin.qq.com/doc/v3/merchant/4012791870 ，官方更新时间 `2026.02.28`
- `SDK`：https://pay.weixin.qq.com/doc/v3/merchant/4012076498 ，官方更新时间 `2024.11.25`
- `付款码支付（V2）/ 场景介绍`：https://pay.weixin.qq.com/doc/v2/merchant/4011936234 ，官方更新时间 `2025.11.14`
- `商户收银台H5大字号规范`：https://pay.weixin.qq.com/doc/v2/merchant/4011939746 ，官方更新时间 `2025.03.21`

## 支付结果确认

- 默认采用“后端下单 -> 前端拉起支付 -> 用户返回 -> 后端查单 / 接收异步回调 -> 幂等更新订单”的闭环。
- 不要把前端页面上的“支付成功”、`WeixinJSBridge` 回调，或小程序前端返回结果直接当成最终入账依据。
- 未收到回调时，优先查单补偿；收到重复回调时，按幂等处理。
- 相关官方文档：
  - `JSAPI支付 / 开发指引`：https://pay.weixin.qq.com/doc/v3/merchant/4012791870
  - `支付回调和查单实现指引（v3）`：https://pay.weixin.qq.com/doc/v3/merchant/4012075249
  - `支付回调和查单实现指引（v2）`：https://pay.weixin.qq.com/doc/v2/merchant/4011984682

## 安全、签名与网络

- 优先选用官方服务端 SDK，避免自行拼签名、验签、解密回调报文和处理平台证书轮换。
- 如果用户坚持手写 HTTP 或手写签名逻辑，必须回到官方安全文档，不要凭记忆给出字段或签名串。
- 平台证书、微信支付公钥、验签工具、证书下载工具要和当前文档体系配套使用。
- 排查异常时，优先核对 HTTPS 配置、网络连通性、时钟偏差、代理层和证书材料。
- 相关官方文档：
  - `最佳安全实践`：https://pay.weixin.qq.com/doc/v2/merchant/4011941549
  - `安全与网络相关注意事项`：https://pay.weixin.qq.com/doc/v2/merchant/4011984638
  - `HTTPS服务器配置`：https://pay.weixin.qq.com/doc/v2/merchant/4012197402
  - `验签工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076525
  - `平台证书下载工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076524

## H5 页面规范与验收

- 微信内 H5 收银页面需要适配大字体场景，不允许出现信息溢出、遮挡、重叠等问题。
- 适配时优先避免固定高度；允许换行、滚动，必要时按官方指引处理字号缩放事件。
- 上线前要在 iOS 与 Android 真机上验收，建议覆盖小屏设备；当字体调到第 6 档时，页面主要文字信息最小不低于 `18dp/pt`。
- 相关官方文档：
  - `商户收银台H5大字号规范`：https://pay.weixin.qq.com/doc/v2/merchant/4011939746
  - `支付验收指引`：https://pay.weixin.qq.com/doc/v2/merchant/4011984810

## 产品与版本边界

- 微信内网页 / 公众号场景默认先看 JSAPI 支付。
- 公众号网页拉起支付默认看 `JSAPI调起支付 / WeixinJSBridge`，不要把小程序的 `wx.requestPayment` 用到公众号网页场景。
- 小程序场景通常同时涉及后端下单接口与前端 `wx.requestPayment`。
- 原生 App 场景通常涉及 APP 支付与 OpenSDK。
- 付款码支付当前官方主文档仍主要在 V2 体系内；回答这类问题时，不要把 V3 的接口字段直接套进去。
- 如果用户同时提到服务商模式、普通商户模式、V2、V3，要先确认是哪一套主体与文档。

## 付款码支付（V2）提示

- 付款码支付是线下被扫 / 主扫场景，优先从 `场景介绍`、`验证密码规则`、`协议规则`、`开发指引` 进入。
- 官方场景介绍中明确说明：用户付款码是 `18 位纯数字`，前缀 `10-14` 为中国大陆用户，前缀 `15` 为中国香港用户。
- 相关官方文档：
  - `场景介绍`：https://pay.weixin.qq.com/doc/v2/merchant/4011936234
  - `验证密码规则`：https://pay.weixin.qq.com/doc/v2/merchant/4011936523
  - `协议规则`：https://pay.weixin.qq.com/doc/v2/merchant/4011986581
  - `开发指引`：https://pay.weixin.qq.com/doc/v2/merchant/4011936672

## 回答时的底线

- 如果问题需要精确的请求字段、响应字段、状态枚举、签名串、回调 JSON、SDK 方法名或错误码，先打开对应官方页面。
- 如果只是说明集成路径，优先回答“应该看哪组官方文档”和“为什么”，再给实现建议。
- 如果需要最新目录、页面标题、更新时间或侧边栏子文档，先读取 `official-doc-index.md`；索引不够时，运行 `python scripts/build_official_index.py` 重新抓取。
