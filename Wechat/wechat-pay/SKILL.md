---
name: wechat-pay
description: 微信支付开发参考与官方文档路由 skill。用于回答微信支付接入、普通商户与服务商模式、JSAPI/小程序支付/APP 支付/H5 支付/Native 支付/付款码支付（V2）、API v2/v3 区分、签名验签、商户 API 证书、APIv3 密钥、平台证书与微信支付公钥、支付回调与查单、退款、对账、收银台 H5 规范、支付验收、SDK、开发工具、示例代码和更新日志等问题；当任务需要依据微信支付官方文档、规则、示例或链接给出实现路径时使用。
---

# 微信支付开发

## Overview

- 优先使用微信支付官方文档、官方 SDK、官方开发工具和官方示例入口。
- 对参数名、签名串、回调字段、证书处理、状态枚举、请求路径这类“必须精确”的内容，不要凭记忆补全；先进入对应官方页面。

## Workflow

1. 先判断支付产品与终端场景。
   - 微信内 H5 / 公众号：优先看 JSAPI 支付。
   - 小程序：优先看小程序支付与 `wx.requestPayment`，后端下单仍回到微信支付官方接口。
   - iOS / Android 原生 App：优先看 APP 支付与 OpenSDK。
   - 扫码枪扫用户付款码：优先看付款码支付（V2）。
   - 外部浏览器手机 H5：优先看 H5 支付。
   - PC 扫码或二维码收款页：优先看 Native 支付。

2. 再判断问题类型，并按需加载参考文件。
   - 产品选型、接入流程、官方入口：读取 `references/product-routing.md`
   - APP / H5 / Native / 小程序 / JSAPI 的产品扩展区：读取 `references/payment-products-v3.md`
   - 普通商户、服务商、合作伙伴文档、接入模式与必要参数：读取 `references/service-provider-and-modes.md`
   - SDK、官方工具、客户端能力、示例代码：读取 `references/sdk-and-tools.md`
   - 安全、签名、证书、公钥、回调验签、回调解密：读取 `references/security-materials.md`
   - 回调、查单、关单、退款、账单、对账：读取 `references/funds-refund-and-billings.md`
   - 安全、回调闭环、H5 规范、验收与常见易错点：读取 `references/rules-and-checklists.md`
   - 更新日志、监控与索引刷新策略：读取 `references/maintenance-and-updates.md`
   - 需要看已抓取的官方目录、页面标题、更新时间或重新刷新索引：读取 `references/official-doc-index.md`，必要时运行 `scripts/build_official_index.py`

3. 明确当前依据的是哪套文档。
   - 如果问题落在新接入、官方 SDK、JSAPI / APP / H5 / Native / 小程序等主线能力，优先看 v3 文档。
   - 如果问题明确是付款码支付或通用规则中的老文档，保留在 V2 文档体系内回答。
   - 如果这是基于当前官方文档组织方式得出的判断，而非官方显式迁移结论，要明确标注为推断。

4. 输出时保持保守。
   - 明确区分“官方页面已验证的信息”和“基于文档结构的推断”。
   - 不要把前端“支付成功”或浏览器回调直接当成最终成功依据；后端需要结合异步回调与查单确认。
   - 不要混写 v2 与 v3 的参数、签名规则、字段名或 SDK 方法。

## Reference Files

- `references/product-routing.md`
  - 用于产品路由、文档入口、常见场景到产品的映射，以及容易混淆的 V2/V3 与产品边界。
- `references/sdk-and-tools.md`
  - 用于官方服务端 SDK、OpenSDK、JS-SDK、小程序支付 API、Postman、验签工具、平台证书工具与示例入口。
- `references/payment-products-v3.md`
  - 用于 JSAPI、APP、H5、Native、小程序支付的产品扩展区、场景分流和主入口对照。
- `references/service-provider-and-modes.md`
  - 用于普通商户与服务商模式分流、`/merchant/` 与 `/partner/` 文档树切换、开发必要参数总表。
- `references/security-materials.md`
  - 用于 APIv3 概述、签名验签、商户 API 证书、APIv3 密钥、平台证书、微信支付公钥、回调解密。
- `references/funds-refund-and-billings.md`
  - 用于查单、关单、退款、退款状态确认、账单下载、T+1 对账。
- `references/rules-and-checklists.md`
  - 用于回调与查单、安全、H5 大字号规范、支付验收、退款与对账相关规则清单。
- `references/maintenance-and-updates.md`
  - 用于跟踪 v2/v3 更新日志、页面更新时间与本地索引刷新策略。
- `references/official-doc-index.md`
  - 用于查看脚本抓取到的官方种子页标题、更新时间、目录大纲与侧边栏子文档。
- `references/official-doc-seeds.md`
  - 用于查看索引脚本为什么默认抓取这些页面，以及后续扩种时的分类依据。

## Refresh Official Index

- 运行 `python scripts/build_official_index.py`
- 如果需要补抓某个未覆盖的官方页面，追加 `--url <official-doc-url>`
- 该脚本会重建：
  - `references/official-doc-index.md`
  - `references/official-doc-index.json`
- 默认抓取范围已经覆盖普通商户主产品线、服务商入口、安全材料、退款/账单和更新日志；新增范围时先同步更新 `scripts/build_official_index.py`

## Answering Standards

- 优先给出“应该打开哪一组官方页面”和“为什么”，再给实现建议。
- 如果用户提到服务商、合作伙伴、子商户、`sp_mchid`、`sub_mchid`、`sub_appid` 等关键词，优先切到 `references/service-provider-and-modes.md` 和 partner 文档。
- 输出链接时，优先归一到 `https://pay.weixin.qq.com/doc/...` 官方文档域名；如果遇到其他官方镜像域名，尽量换回该主域名再回答。
- 如果用户要求精确链接、最新标题或更新时间，先使用本地索引；索引不足时，直接抓取官方页面补充。
- 如果用户要求代码示例，优先引用官方 SDK、官方示例页或官方 GitHub 仓库，而不是社区 SDK。
