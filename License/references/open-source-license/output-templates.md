# 开源许可证输出模板

## 模板 1: 许可证推荐意见

```text
结论
- 建议优先选择: [Apache-2.0 / MIT / MPL-2.0 / 其他]
- 备选方案: [备选许可证]

理由
- 商业友好度: [说明]
- copyleft 要求: [说明]
- 专利授权: [说明]
- 与现有依赖或分发方式的匹配度: [说明]

仍需确认
- [待确认: 是否存在 GPL / AGPL 依赖]
- [待确认: 是否需要 SaaS 场景保护]
- [待确认: 是否存在多主体版权]

建议动作
1. 在仓库根目录新增 `LICENSE`
2. 检查包元数据中的 `license` / `license-file`
3. 对第三方代码和素材补 `NOTICE` 或第三方声明
```

## 模板 2: 开源发布审查结论

```text
可直接发布项
- [已确认项]

待复核项
- [依赖或资产]
- [许可证边界问题]

阻塞项
- [缺失 LICENSE / NOTICE / 第三方声明]
- [版权归属不清]
- [无法识别许可证的第三方资源]

建议落地顺序
1. 补仓库根目录许可证文本
2. 盘点第三方依赖与素材
3. 统一 SPDX 和包元数据
4. 再做对外发布
```

## 模板 3: README 里的许可证段落

```md
## License

This project is licensed under the [Apache License 2.0](./LICENSE).

Third-party code, assets, or dependencies may be subject to their own licenses.
See `[THIRD_PARTY_NOTICES.md]` or `[NOTICE]` if applicable.
```

## 模板 4: 第三方声明文件骨架

```text
# Third-Party Notices

This project includes third-party components:

1. [组件名称]
   - Source: [来源链接]
   - Version: [版本]
   - License: [SPDX 标识]
   - Notes: [是否修改过 / 是否复制进仓库]

2. [字体 / 图片 / 模型 / 数据]
   - Source: [来源链接]
   - License: [许可证]
   - Notes: [限制说明]
```

## 模板 5: 源码 SPDX 头

```text
SPDX-FileCopyrightText: [年份] [主体名称]
SPDX-License-Identifier: [SPDX 标识]
```

## 使用提醒

- `LICENSE` 正文优先使用标准官方版本文本，不要自己改写核心条款。
- 模板适合生成“建议稿”和“仓库落地草稿”，不替代正式法律审查。
