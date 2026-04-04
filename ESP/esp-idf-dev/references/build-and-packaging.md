# Build And Packaging

## Core Build Commands

```sh
idf.py build
idf.py app
idf.py bootloader
idf.py partition-table
idf.py clean
idf.py fullclean
idf.py reconfigure
```

- `build` 是增量构建；若源码和配置没变化，通常不会重复构建。
- `app`、`bootloader`、`partition-table` 可只构建对应目标。
- `clean` 删除构建输出，但保留 CMake 配置。
- `fullclean` 删除整个 `build` 目录内容，副作用更强，只在需要彻底重配时使用。
- 新增或删除源文件、增加新的 `idf_component.yml`、修改 CMake 缓存变量时，优先运行 `reconfigure`。

## Flash And Monitor

```sh
idf.py -p COM3 flash
idf.py -p COM3 monitor
idf.py -p COM3 flash monitor
```

- `flash` 底层调用 `esptool write-flash`。
- `-p` 指定串口，`-b` 指定波特率。
- `ESPPORT` 和 `ESPBAUD` 环境变量可作为默认值。
- 需要透传 `esptool` 参数时，用 `flash --extra-args="..."`。

## Size Analysis

```sh
idf.py size
idf.py size-components
idf.py size-files
```

- `size` 看整体 RAM/flash 占用。
- `size-components` 看每个组件的体积。
- `size-files` 看每个源文件的体积。

## Packaging Deliverables

生成可分发的单文件固件时，不要只停留在 `build/` 目录里的多个二进制文件，优先考虑以下命令：

```sh
idf.py merge-bin -o dist/merged.bin -f raw
idf.py merge-bin -o dist/merged.hex -f hex
idf.py merge-bin -o dist/firmware.uf2 -f uf2
idf.py uf2
idf.py uf2-app
```

- `merge-bin` 会根据当前项目配置，把 bootloader、partition table、app 以及其他相关分区合并成单个文件。
- `merge-bin` 适合“传给另一台机器烧录”或“作为工厂固件产物”。
- `uf2` 会生成包含 bootloader、partition table 和 app 的 `uf2.bin`。
- `uf2-app` 只生成应用程序的 UF2。
- `merge-bin -f uf2` 与 `idf.py uf2` 在目的上等价，但 `merge-bin` 的格式和选项更灵活。

## Build Variants

当项目需要多个构建变体（例如 `debug`、`release`、`production`）时，优先使用 CMake preset，而不是手工维护一堆命令：

```sh
idf.py --preset production build
```

- 在项目根目录维护 `CMakePresets.json` 或 `CMakeUserPresets.json`。
- 把构建目录、`SDKCONFIG` 路径、`SDKCONFIG_DEFAULTS` 和其他缓存变量写进 preset，避免不同构建变体互相污染。
