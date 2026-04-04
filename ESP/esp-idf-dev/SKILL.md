---
name: esp-idf-dev
description: ESP32/ESP-IDF 项目的环境安装、目标芯片设置、编译、烧录、串口监视、menuconfig/sdkconfig.defaults 配置、组件与依赖管理、CMake 构建、分区表、OTA 打包与 HTTPS OTA 接入指南。Use when working on an ESP-IDF project, creating or modifying components, packaging firmware, troubleshooting build or flash issues, or mapping a request to the correct official ESP-IDF API/docs page.
---

# ESP-IDF Dev

使用这个 skill 处理 ESP32 系列芯片上的 ESP-IDF 项目开发任务。优先把用户请求映射到正确的 `idf.py` 工作流、Kconfig/CMake 配置层、组件依赖层，或 OTA/分区层，而不是把所有问题都当成“重新编译一次”。

## Quick Start

1. 在包含 `CMakeLists.txt` 的 ESP-IDF 项目根目录工作。
2. 先确认目标芯片，再决定是否要改配置或直接构建。
3. 需要环境安装或开发闭环时，读 [references/setup-and-core-workflow.md](references/setup-and-core-workflow.md)。
4. 需要编译、烧录、监视、打包单文件固件、看体积时，读 [references/build-and-packaging.md](references/build-and-packaging.md)。
5. 需要 `menuconfig`、`sdkconfig`、`sdkconfig.defaults`、目标芯片默认值、配置预设时，读 [references/configuration.md](references/configuration.md)。
6. 需要组件、库、BSP、组件注册表、`idf_component.yml`、`idf_component_register()`、预建 `.a` 库时，读 [references/components-and-libraries.md](references/components-and-libraries.md)。
7. 需要分区表、OTA 槽位、`merge-bin`、`uf2`、`esp_https_ota`、`partitions.csv` 时，读 [references/ota-and-partitions.md](references/ota-and-partitions.md)。
8. 需要官方入口或查具体 API 时，读 [references/official-docs.md](references/official-docs.md)。

## Core Rules

- 只在 ESP-IDF 工程根目录执行 `idf.py`。
- 优先使用项目实际 ESP-IDF 版本对应的官方文档；如果只能先参考 stable 文档，要明确说明这一点。
- 不要默认手改生成文件 `sdkconfig`；优先使用 `idf.py menuconfig` 和可提交的 `sdkconfig.defaults`。
- `idf.py set-target` 会清空 `build` 并重建 `sdkconfig`，不要在没提醒用户的情况下随意执行。
- 新增或删除源文件、组件清单、CMake 变量不生效时，优先尝试 `idf.py reconfigure`。
- 用 `SRC_DIRS` 自动搜源时，新增文件后经常需要 `reconfigure`；团队项目更推荐显式 `SRCS`。
- 使用组件管理器时，不要手动修改 `managed_components` 和 `dependencies.lock`。
- 如果会话环境已经接入 ESP-IDF MCP server，优先用它查询项目状态、设备列表、配置和构建动作；如果没有，再回退到 shell 里的 `idf.py`。
- 把 “生成可分发固件” 与 “实现运行时 OTA 升级” 区分开：
  - 打包交付物：`idf.py merge-bin`、`idf.py uf2`
  - 在线升级逻辑：`esp_https_ota` 或更底层 OTA API
  - 启用 OTA 槽位：分区表与 `otadata`
- 串口日志乱码时，检查 `CONFIG_XTAL_FREQ` 是否与开发板主晶振匹配。
- 用户说“框架”或“库”时，先判断是：
  - ESP-IDF 组件/组件注册表依赖
  - BSP 或官方库与框架页面里的外部框架
  - 项目内部要抽成组件的可复用模块

## Common Commands

```sh
idf.py create-project my_app
idf.py create-component my_component
idf.py --list-targets
idf.py set-target esp32
idf.py menuconfig
idf.py build
idf.py app
idf.py bootloader
idf.py partition-table
idf.py -p COM3 flash
idf.py -p COM3 monitor
idf.py -p COM3 flash monitor
idf.py size
idf.py size-components
idf.py size-files
idf.py reconfigure
idf.py merge-bin -o dist/merged.bin -f raw
idf.py uf2
idf.py uf2-app
idf.py read-otadata
idf.py add-dependency namespace/name^1.2.3
idf.py update-dependencies
```

## Files To Inspect First

- `CMakeLists.txt`
- `main/CMakeLists.txt`
- `components/*/CMakeLists.txt`
- `idf_component.yml`
- `sdkconfig`
- `sdkconfig.defaults`
- `partitions.csv`
- `CMakePresets.json`
- `CMakeUserPresets.json`
- `dependencies.lock`

## Response Pattern

- 先判断任务属于“环境/构建/配置/组件/OTA/API 查询”中的哪一类。
- 给出最短可执行命令，再补充为什么这么做。
- 涉及版本、副作用或 OTA 风险时，明确指出会改哪些文件、会不会清空 `build`、会不会影响启动分区。
- 涉及 API 用法时，先指出组件名、头文件、依赖声明，再给最小调用骨架。
