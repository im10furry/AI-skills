# Configuration

## Configuration Layers

先区分用户说的“SDK 设置”落在哪一层：

- Kconfig 选项：`idf.py menuconfig`、`sdkconfig`、`sdkconfig.defaults`
- CMake 缓存变量：`idf.py -DNAME=VALUE reconfigure` 或 preset
- 编译期源码宏：头文件、组件配置头、源码常量
- Flash 布局：`partitions.csv`

## `sdkconfig` And `sdkconfig.defaults`

- `sdkconfig` 是当前工程的生成配置。
- `sdkconfig.defaults` 用来保存用户定义的默认值，尤其适合版本控制场景。
- 官方文档明确说明：第一次配置项目且还没有 `sdkconfig` 时，`sdkconfig.defaults` 会覆盖 Kconfig 默认值；之后用户仍然可以通过 `idf.py menuconfig` 修改。
- 团队协作时，优先把应提交的默认配置放进 `sdkconfig.defaults`，而不是依赖本地 `sdkconfig`。

## Target Defaults

- `idf.py set-target <target>` 是最直接的设置方式，但它会重置当前构建目录和 `sdkconfig`。
- 如果项目长期默认某个目标芯片，可在 `sdkconfig.defaults` 里写：

```ini
CONFIG_IDF_TARGET="esp32"
```

- 当用户没有通过环境变量、CMake 变量或 `idf.py set-target` 明确指定目标时，构建系统会使用这里的默认值；如果都没有设置，则默认目标是 `esp32`。

## Recommended Practice

- 优先通过 `idf.py menuconfig` 改 Kconfig 选项。
- 优先提交 `sdkconfig.defaults`，谨慎提交 `sdkconfig`。
- 不要把一次性、本机专用设置误写进团队共享的 defaults 文件。
- 用户说“改 SDK 配置”时，先确认要改的是：
  - 目标芯片
  - 串口/烧录相关
  - 组件配置
  - 分区表
  - 编译优化/调试等级

## Reconfigure Cases

这些情况优先执行：

```sh
idf.py reconfigure
```

- 新增或删除源码文件后，构建系统没看到变化
- 新增 `idf_component.yml`
- 调整 CMake 缓存变量
- 使用 `SRC_DIRS` 自动搜源且新增了源文件

## Related Docs

- 项目配置 / Kconfig  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-guides/kconfig/index.html
- Configuration Options Reference  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-reference/index.html
