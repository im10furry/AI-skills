---
name: legal-documents
description: 法律文档与开源合规材料的统一起草、审阅、重写、缺口检查与场景路由。Use when working on a confidentiality agreement/NDA, user agreement/Terms of Service, privacy policy, contributor license agreement (CLA), or open-source license and repository release compliance task, especially when Codex should first classify the document type and then read only the minimum relevant files from the matching subdirectory under references/.
---

# 法律文档

## Overview

- 把这个 skill 当作法律文档任务的总入口，不要一次性加载全部参考资料。
- 先把请求归到单一文档类型，再去对应子目录读取最小必要文件。
- 文档类型固定分为五类：
  - `references/confidentiality-agreement/`
  - `references/user-agreement/`
  - `references/privacy-policy/`
  - `references/contributor-license-agreement/`
  - `references/open-source-license/`
- 如果一个请求同时涉及多份文档，先判断主文档，再按需要交叉读取相邻子目录。
- 把输出写成可执行的起草或审阅建议，不要伪装成正式法律意见。

## Workflow

1. 先判断文档类型。
   - `NDA`、保密协议、保密条款、披露流程：走 `confidentiality-agreement`
   - 用户协议、服务条款、Terms of Service：走 `user-agreement`
   - 隐私政策、App/Web 数据收集说明、SDK/跨境数据披露：走 `privacy-policy`
   - `CLA`、贡献者许可、代码贡献授权、企业贡献确认：走 `contributor-license-agreement`
   - 开源许可证选型、`LICENSE` / `NOTICE`、依赖许可证排查、开源发布清单：走 `open-source-license`

2. 再判断任务类型。
   - 从零起草
   - 重写或精简
   - 红线审阅
   - 缺口检查
   - 场景到条款的映射
   - 仓库或发布物落地

3. 只读取对应子目录里的最小必要文件。
   - 不要把全部参考文件都读进上下文。
   - 如果只是搭框架，优先读取结构/路由类文件。
   - 如果只是审红线，优先读取 review/red-flags 类文件。
   - 只有在需要直接产出初稿时，才读取 `initial-draft-template.md`。

4. 收集最小事实并输出。
   - 主体是谁
   - 服务、产品、仓库或合作事项是什么
   - 用户、贡献者、接收方、处理者或发布方是谁
   - 是否收费、是否跨境、是否含个人信息、是否含知识产权或专利风险
   - 法域、争议解决、通知方式、期限等是否已知
   - 未知信息用 `[待确认: ...]` 保留，不要擅自补齐

## Subdirectory Routing

### `references/confidentiality-agreement/`

- `mutual-unilateral-and-purpose-routing.md`
  - 用于先判断单向或双向、披露目的和允许接收人范围。
- `nda-structure-and-negotiation-points.md`
  - 用于搭保密协议结构或梳理谈判点。
- `nda-redline-review-checklist.md`
  - 用于审对方模板、高风险条款和不对称义务。
- `special-clauses-and-operational-boundaries.md`
  - 用于 `residuals`、非招揽、竞业、知识产权归属、备份例外等特殊条款。
- `disclosure-process-and-operational-checklist.md`
  - 用于把文本义务对齐到真实披露流程。
- `initial-draft-template.md`
  - 只有在需要直接生成初稿时再读取。

### `references/user-agreement/`

- `product-scenario-routing.md`
  - 用于把产品形态映射到条款关注点。
- `terms-structure-and-clause-checklist.md`
  - 用于搭框架、补章节和占位。
- `subscription-refund-and-consumer-flags.md`
  - 用于订阅、自动续费、退款、试用与消费者敏感条款。
- `ai-product-and-ugc-clauses.md`
  - 用于 AI 产品、`UGC`、输入输出、内容授权。
- `review-red-flags.md`
  - 用于审查条款缺口、产品不一致和高风险承诺。
- `initial-draft-template.md`
  - 只有在需要整份草稿时再读取。

### `references/privacy-policy/`

- `privacy-policy-routing-and-data-map.md`
  - 用于先梳理主体、数据流、处理角色和适用产品场景。
- `data-categories-retention-and-rights-checklist.md`
  - 用于盘点收集字段、处理目的、保留期限和数据主体权利。
- `cookies-sdk-and-cross-border-flags.md`
  - 用于 Cookie、分析 SDK、广告追踪、跨境传输和未成年人敏感点。
- `review-red-flags.md`
  - 用于审查政策和真实产品行为是否一致。
- `initial-draft-template.md`
  - 只有在需要完整隐私政策初稿时再读取。

### `references/contributor-license-agreement/`

- `cla-routing-and-model-selection.md`
  - 用于判断个人还是企业 `CLA`、是版权让与还是许可授权、是否应改用 `DCO`。
- `contribution-scope-and-inbound-rights-checklist.md`
  - 用于检查贡献范围、第三方代码、雇佣关系、历史提交和再许可边界。
- `patent-moral-rights-and-review-red-flags.md`
  - 用于专利授权、精神权利、未来贡献覆盖、过宽陈述保证等敏感条款。
- `initial-draft-template.md`
  - 只有在需要 `CLA` 草稿时再读取。

### `references/open-source-license/`

- `license-selection-and-compatibility.md`
  - 用于常见许可证选型和兼容性初筛。
- `copyleft-saas-and-linking-boundaries.md`
  - 用于 copyleft、SaaS、链接、插件和网络边界判断。
- `spdx-license-files-and-notices.md`
  - 用于 `SPDX`、`LICENSE`、`NOTICE`、版权头和包元数据落地。
- `dependency-license-review-checklist.md`
  - 用于依赖、模型、素材和第三方资产许可盘点。
- `repository-release-checklist.md`
  - 用于开源发布前仓库清单与发布物检查。
- `output-templates.md`
  - 用于直接输出建议、审查结论或仓库落地文本。

## Cross-Document Guardrails

- 不要把用户协议和隐私政策混成一份文档。
- 不要把开源许可证任务当成普通商业合同起草。
- 用户问“产品上线需要哪些法律文档”时，通常先从 `user-agreement` 与 `privacy-policy` 开始，再判断是否需要额外规则或开源清单。
- 用户问“开源仓库怎么收贡献”时，通常联动 `contributor-license-agreement` 与 `open-source-license`。
- 用户问“合作前先签什么”时，通常先从 `confidentiality-agreement` 开始，而不是直接写采购或主服务协议。

## Answering Standards

- 先给文档类型判断，再给最短可执行建议。
- 审阅场景优先输出“红线 / 可谈判 / 可接受”或“问题 / 风险 / 建议修改”。
- 起草场景优先保留关键占位，不要编造法域、法院、机构、地址和期限。
- 说明哪些结论是工程或合规初筛，哪些需要目标法域法务复核。
- 遇到消费者权益、自动续费、未成年人、跨境数据、雇佣发明、专利、出口管制、金融医疗教育等强监管因素时，显式提示专项复核。
