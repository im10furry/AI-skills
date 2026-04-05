# 微信支付产品扩展区（V3）

## 场景分流总表

| 场景 | 优先产品 | 官方入口 | 关键分流点 |
| --- | --- | --- | --- |
| 微信内公众号网页、微信内 H5 | JSAPI 支付 | `产品介绍` https://pay.weixin.qq.com/doc/v3/merchant/4012062524 | 运行环境是微信内置浏览器，前端调起支付走 `WeixinJSBridge`。 |
| 小程序内支付 | 小程序支付 | `产品介绍` https://pay.weixin.qq.com/doc/v3/merchant/4012791894 | 前端走 `wx.requestPayment`，不要和公众号网页混用。 |
| 商户自有原生 App | APP 支付 | `产品介绍` https://pay.weixin.qq.com/doc/v3/merchant/4013070158 | 官方文档明确这是商户自有 App 场景，不适合拿网页或小程序方案替代。 |
| 手机外部浏览器网页 | H5 支付 | `产品介绍` https://pay.weixin.qq.com/doc/v3/merchant/4012791832 | 官方文档明确这是“手机浏览器网页、非微信内置浏览器”场景。 |
| PC 扫码或商户展示二维码让用户扫 | Native 支付 | `产品介绍` https://pay.weixin.qq.com/doc/v3/merchant/4012791874 | 这是扫码支付产品，不是线下扫用户付款码。 |
| 扫码枪扫用户付款码 | 付款码支付（V2） | `场景介绍` https://pay.weixin.qq.com/doc/v2/merchant/4011936234 | 属于 V2 体系，文档路径和字段规则不同。 |

## 已核验的产品入口

- `JSAPI支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012062524
- `JSAPI支付 / 开发指引`：https://pay.weixin.qq.com/doc/v3/merchant/4012791870
- `JSAPI/小程序下单`：https://pay.weixin.qq.com/doc/v3/merchant/4012791856
- `JSAPI调起支付`：https://pay.weixin.qq.com/doc/v3/merchant/4012791857

- `小程序支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012791894
- `小程序支付 / 快速开始`：https://pay.weixin.qq.com/doc/v3/merchant/4015459512

- `APP支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4013070158
- `APP支付 / 快速开始`：https://pay.weixin.qq.com/doc/v3/merchant/4015478291

- `H5支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012791832
- `Native支付 / 产品介绍`：https://pay.weixin.qq.com/doc/v3/merchant/4012791874

## 产品级重点提醒

- `JSAPI` 与 `小程序支付`
  - 两者在后端下单链路上高度相关，官方文档明确 `JSAPI/小程序下单` 是共同入口。
  - 但前端调起方式不同：公众号网页看 `WeixinJSBridge`，小程序看 `wx.requestPayment`。

- `APP支付`
  - 官方产品介绍强调这是商户自有 App 场景，通常要结合开放平台账号、移动应用 `APPID`、商户号绑定和 OpenSDK 一起看。
  - 如果用户只是做移动网页，不要误路由到 APP 支付。

- `H5支付`
  - 官方产品介绍用于“手机浏览器网页，非微信内置浏览器”场景。
  - 如果用户明确说“微信里打开网页”，那通常应先看 JSAPI，而不是 H5 支付。

- `Native支付`
  - 官方产品介绍用于二维码被用户扫描的场景。
  - 这和“扫码枪扫用户付款码”的付款码支付（V2）是两套不同产品，不要混答。

## 继续深挖时的打开顺序

1. 先打开对应产品的 `产品介绍`
2. 再打开该产品的 `快速开始`
3. 需要参数或接口时，再进入 `official-doc-index.md` 对应页面的目录树与关键链接
4. 需要签名、证书、公钥、回调闭环时，切到 `security-materials.md` 和 `funds-refund-and-billings.md`
