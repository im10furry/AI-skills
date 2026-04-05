# SPDX、许可证文件与 Notice 落地

## SPDX 标识

- 优先使用标准 SPDX 标识，如：
  - `MIT`
  - `Apache-2.0`
  - `GPL-3.0-only`
  - `GPL-3.0-or-later`
  - `MPL-2.0`
- 组合场景中，表达式要明确，例如：
  - `MIT OR Apache-2.0`
  - `GPL-2.0-only WITH Classpath-exception-2.0`

## 仓库根目录常见文件

- `LICENSE`
  - 当前项目主许可证文本。
- `NOTICE`
  - 当许可证或第三方依赖要求保留通知时使用。
- `COPYING`
  - 某些项目沿用该命名，尤其在 GNU 生态里常见。
- `THIRD_PARTY_NOTICES.md`
  - 当第三方声明较多时，集中列出来源、版本和许可证。

## 源码文件头

- 若项目需要文件级标识，优先用简洁 SPDX 头，不要手工粘贴整份许可证全文到每个文件。
- 常见最小形式：

```text
SPDX-FileCopyrightText: 2026 Example Corp
SPDX-License-Identifier: Apache-2.0
```

## 包管理器元数据

- `package.json`
  - `license`
- `Cargo.toml`
  - `license` 或 `license-file`
- `pyproject.toml`
  - 检查元数据与根目录许可证是否一致
- 镜像、压缩包、安装包
  - 确认许可证文本与 notice 是否随分发物一起提供

## 易错点

- 仓库写 `Apache-2.0`，包元数据却还停留在 `MIT`
- 引入第三方源码后，把原版权头删掉
- 多许可证目录没有边界说明
- `NOTICE` 应保留但被遗漏
