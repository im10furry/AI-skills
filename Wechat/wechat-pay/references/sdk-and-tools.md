# SDK 与开发工具参考

## 已核验的官方入口

- `SDK 总览`：https://pay.weixin.qq.com/doc/v3/merchant/4012076498 ，官方更新时间 `2024.11.25`
- `使用 Java SDK`：https://pay.weixin.qq.com/doc/v3/merchant/4012076506
- `使用 PHP SDK`：https://pay.weixin.qq.com/doc/v3/merchant/4012076511
- `使用 Go SDK`：https://pay.weixin.qq.com/doc/v3/merchant/4012076515
- `验签工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076525
- `平台证书下载工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076524
- `Postman调试工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076519
- `示例代码 / Go`：https://pay.weixin.qq.com/doc/v3/merchant/4015119334
- `示例代码 / Java`：https://pay.weixin.qq.com/doc/v3/merchant/4014931831

## 官方服务端 SDK

- `Java`：
  - 文档页：https://pay.weixin.qq.com/doc/v3/merchant/4012076506
  - GitHub：https://github.com/wechatpay-apiv3/wechatpay-java
  - Maven Central：https://central.sonatype.com/artifact/com.github.wechatpay-apiv3/wechatpay-java/
- `PHP`：
  - 文档页：https://pay.weixin.qq.com/doc/v3/merchant/4012076511
  - GitHub：https://github.com/wechatpay-apiv3/wechatpay-php
  - Packagist：https://packagist.org/packages/wechatpay/wechatpay
- `Go`：
  - 文档页：https://pay.weixin.qq.com/doc/v3/merchant/4012076515
  - GitHub：https://github.com/wechatpay-apiv3/wechatpay-go
  - pkg.go.dev：https://pkg.go.dev/github.com/wechatpay-apiv3/wechatpay-go
- 官方 SDK 页明确说明：当前官方服务端 SDK 基于 API v3 构建，提供自动签名验签、敏感信息加解密与回调验签/解密能力；如果问题落在这些基础能力，优先使用官方 SDK。
- 如果某个语言没有出现在官方 SDK 页中，就不要默认它存在“官方服务端 SDK”；此时应回到官方接口文档或明确标注为社区方案。

## 官方客户端与前端入口

- `JS-SDK`：https://developers.weixin.qq.com/doc/offiaccount/OA_Web_Apps/JS-SDK.html
- `小程序支付 API / wx.requestPayment`：https://developers.weixin.qq.com/miniprogram/dev/api/payment/wx.requestPayment.html
- `iOS OpenSDK`：https://developers.weixin.qq.com/doc/oplatform/Downloads/iOS_Resource.html
- `Android OpenSDK`：https://developers.weixin.qq.com/doc/oplatform/Downloads/Android_Resource.html
- `JSAPI/小程序下单`：https://pay.weixin.qq.com/doc/v3/merchant/4012791856
- `JSAPI调起支付`：https://pay.weixin.qq.com/doc/v3/merchant/4012791857

## 官方开发工具

- `验签工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076525
  - 用于验证回调签名与排查验签失败问题。
- `平台证书下载工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076524
  - 用于获取和更新平台证书，配合回调验签和敏感报文处理。
- `Postman调试工具`：https://pay.weixin.qq.com/doc/v3/merchant/4012076519
  - 用于快速验证请求头、签名、报文格式与接口返回。
- `网络云排查 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012076542
- `网络云排查 / 网络问题排查指南`：https://pay.weixin.qq.com/doc/v3/merchant/4012076543
- `网络云排查 / 常见问题`：https://pay.weixin.qq.com/doc/v3/merchant/4012076544

## 官方示例与仓库

- `示例代码 / Go`：https://pay.weixin.qq.com/doc/v3/merchant/4015119334
- `示例代码 / Java`：https://pay.weixin.qq.com/doc/v3/merchant/4014931831
- `wechatpay-java 业务接口目录`：https://github.com/wechatpay-apiv3/wechatpay-java/tree/main/service
- `wechatpay-go 业务接口目录`：https://github.com/wechatpay-apiv3/wechatpay-go/tree/main/services
- `微信支付开发者社区`：https://developers.weixin.qq.com/community/pay/doc/00022e47830e90adbd2c507c951801
- 官方 SDK 页同时提示：社区 SDK 只适合参考，不应默认直接复制到生产环境。

## 何时优先使用官方 SDK 或官方工具

- 需要下单、查单、退款、账单下载、回调验签、回调解密时，优先官方服务端 SDK。
- 需要排查签名失败、平台证书不匹配、回调验签失败、HTTP 报文格式错误时，优先官方验签工具、平台证书下载工具与 Postman 调试工具。
- 需要原生 App 拉起微信支付时，优先官方 OpenSDK；不要把网页 JSAPI 方案硬套到 App 端。
- 需要小程序支付时，前端能力看 `wx.requestPayment`，但后端创建订单、回调、查单仍回到微信支付官方接口与 SDK。
- 如果必须手写 HTTP 请求，只把官方 SDK 当“参考实现”和“签名/回调处理样例”；不要凭社区博客或旧代码猜测当前字段。
