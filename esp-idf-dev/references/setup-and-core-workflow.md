# Setup And Core Workflow

## Environment Setup

- 在 Windows 上，ESP-IDF v6.0 及以上版本的默认和推荐安装方式是 EIM（ESP-IDF 安装管理器）。
- EIM 会自动检查依赖；官方文档明确提到 Git 和 Python，且 Python 3.10 是最低支持版本。
- 典型安装命令：

```sh
eim install
eim wizard
```

- 日常开发应在已激活的 ESP-IDF 环境中运行 `idf.py`。如果环境未激活，先让用户进入 EIM 提供的终端或已配置好的 ESP-IDF shell。

## Optional AI Integration

如果当前 IDE 或智能体支持 MCP，可直接使用 ESP-IDF 官方 MCP server：

```sh
eim run "idf.py mcp-server"
idf.py mcp-server
```

- `eim run "idf.py mcp-server"` 是官方推荐方式，要求 EIM 0.8.1+ 且 ESP-IDF 通过 EIM 安装。
- 若已在激活好的 ESP-IDF shell 中，也可直接运行 `idf.py mcp-server`。
- 这个服务器会暴露针对 ESP-IDF 的工具和资源，例如设置 target、构建项目、烧录项目、查询项目配置和设备列表。

## Core Build Loop

```sh
idf.py --list-targets
idf.py set-target esp32
idf.py menuconfig
idf.py build
idf.py -p COM3 flash
idf.py -p COM3 monitor
idf.py -p COM3 flash monitor
```

## Notes To Apply

- `idf.py` 必须在包含 `CMakeLists.txt` 的工程根目录运行。
- `idf.py set-target` 会清空 `build`，重建 `sdkconfig`，并把旧配置保存到 `sdkconfig.old`。
- `flash` 会在需要时自动构建，因此通常不需要先单独执行 `build`。
- 多个命令可以组合执行，顺序不重要，例如：

```sh
idf.py -p COM4 clean flash monitor
```

- 要擦除整片 flash：

```sh
idf.py -p COM3 erase-flash
```

- 只擦 OTA 选择数据：

```sh
idf.py -p COM3 erase-otadata
```

## Common Troubleshooting

- 串口日志乱码或烧录后很快报错时，检查开发板主晶振频率，必要时在 `menuconfig` 里调整 `CONFIG_XTAL_FREQ`。
- 需要快速跳到当前版本文档时，直接运行：

```sh
idf.py docs
```
