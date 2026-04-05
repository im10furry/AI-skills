# 微信支付产品路由

## 已核验的产品入口

- `JSAPI支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012062524 ，官方更新时间 `2025.07.15`
- `JSAPI支付 / 开发指引`：https://pay.weixin.qq.com/doc/v3/merchant/4012791870 ，官方更新时间 `2026.02.28`
- `付款码支付（V2）/ 场景介绍`：https://pay.weixin.qq.com/doc/v2/merchant/4011936234 ，官方更新时间 `2025.11.14`
- `SDK 总览`：https://pay.weixin.qq.com/doc/v3/merchant/4012076498 ，官方更新时间 `2024.11.25`

## 典型需求到文档的路由矩阵

| 需求场景 | 优先读取的官方文档 | 说明 |
| --- | --- | --- |
| 微信内网页、公众号内拉起支付 | `JSAPI支付 / 产品介绍` `4012062524` + `JSAPI支付 / 开发指引` `4012791870` | 先确认场景、主体准入和整体链路，再进入具体 API 文档。 |
| 小程序支付 | `JSAPI支付 / 开发指引` `4012791870` + `JSAPI/小程序下单` `4012791856` | 小程序前端支付能力在官方 SDK 页也有入口，但后端下单、查单、退款仍回到微信支付文档体系。 |
| 前端拉起支付后的状态确认 | `支付回调和查单实现指引` `4012075249` + `查询订单API` `4012791859` + `支付成功回调通知` `4012791861` | 不要只看前端返回；支付状态由后端查单与异步回调共同确认。 |
| 需要关闭订单、退款、对账 | `关闭订单API` `4012791860` + `申请退款接口` `4012791862` + `查询退款单接口` `4012791863` + `下载交易账单` `4012791866` | 这类问题通常从 JSAPI 开发指引或回调/查单指引继续展开。 |
| 线下扫用户付款码 | `场景介绍` `4011936234` + `验证密码规则` `4011936523` + `协议规则` `4011986581` + `开发指引` `4011936672` | 付款码支付当前主文档在 V2 体系，避免直接套用 v3 字段。 |
| H5 收银台适配、无障碍、大字体 | `商户收银台H5大字号规范` `4011939746` + `支付验收指引` `4011984810` | 这是规则/验收问题，不是单纯 API 问题。 |
| 安全、验签、证书、网络 | `最佳安全实践` `4011941549` + `安全与网络相关注意事项` `4011984638` + `HTTPS服务器配置` `4012197402` | 如果还涉及工具，继续读 `sdk-and-tools.md`。 |

## 还需要继续展开的 v3 产品目录

- 官方 v3 产品文档树中，当前已核验存在但未在本地索引中完全展开子页 URL 的目录包括：
  - `APP支付`
  - `H5支付`
  - `Native支付`
  - `小程序支付`
- 当用户问题明确落在这些产品时，先从 `JSAPI支付 / 产品介绍` 或 `official-doc-index.md` 进入 v3 产品文档树，再继续打开对应产品子页，不要凭记忆写出未核验的文档号。

## 重点官方链接

- `JSAPI支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012062524
- `JSAPI支付 / 开发指引`：https://pay.weixin.qq.com/doc/v3/merchant/4012791870
- `JSAPI/小程序下单`：https://pay.weixin.qq.com/doc/v3/merchant/4012791856
- `JSAPI调起支付 / WeixinJSBridge`：https://pay.weixin.qq.com/doc/v3/merchant/4012791857
- `查询订单API`：https://pay.weixin.qq.com/doc/v3/merchant/4012791859
- `支付成功回调通知`：https://pay.weixin.qq.com/doc/v3/merchant/4012791861
- `支付回调和查单实现指引`：https://pay.weixin.qq.com/doc/v3/merchant/4012075249
- `关闭订单API`：https://pay.weixin.qq.com/doc/v3/merchant/4012791860
- `申请退款接口`：https://pay.weixin.qq.com/doc/v3/merchant/4012791862
- `查询退款单接口`：https://pay.weixin.qq.com/doc/v3/merchant/4012791863
- `下载交易账单`：https://pay.weixin.qq.com/doc/v3/merchant/4012791866
- `付款码支付（V2）/ 场景介绍`：https://pay.weixin.qq.com/doc/v2/merchant/4011936234
- `付款码支付（V2）/ 验证密码规则`：https://pay.weixin.qq.com/doc/v2/merchant/4011936523
- `付款码支付（V2）/ 协议规则`：https://pay.weixin.qq.com/doc/v2/merchant/4011986581
- `通用规则 / 商户收银台H5大字号规范`：https://pay.weixin.qq.com/doc/v2/merchant/4011939746
- `通用规则 / 最佳安全实践`：https://pay.weixin.qq.com/doc/v2/merchant/4011941549
- `通用规则 / 支付回调和查单实现指引（V2）`：https://pay.weixin.qq.com/doc/v2/merchant/4011984682

## 常见误区

- 前端“支付成功”不等于订单最终成功，后端还要查单并处理异步回调。
- 不要把付款码支付（V2）的规则、字段或文档号混到 v3 的 JSAPI / 小程序 / App 接口里。
- 如果问题涉及服务商模式、普通商户模式、公众号、小程序、App、多端收银台，先确认主体与终端，再给实现路径。
- 如果问题只问“微信支付怎么接”，先问清楚是 `微信内网页`、`小程序`、`App`、`外部浏览器 H5` 还是 `线下付款码`，否则文档路由极易出错。
