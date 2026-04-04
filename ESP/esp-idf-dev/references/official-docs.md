# Official Docs

优先使用与项目实际目标芯片和 ESP-IDF 版本匹配的官方文档。若项目版本未知，可先从 stable ESP32 文档开始，再在回答中说明这是基于 stable 页面的默认判断。

## Primary Entry Points

- 快速入门首页  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/get-started/index.html
- Windows 安装与 EIM  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/get-started/windows-setup.html
- 从示例到编译、烧录、监视  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/get-started/start-project.html
- `idf.py` 命令总览  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-guides/tools/idf-py.html
- 项目配置 / `menuconfig` / `sdkconfig.defaults`  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-guides/kconfig/index.html
- 构建系统 / 组件 CMake / 预建库  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-guides/build-system.html
- IDF 组件管理器  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-guides/tools/idf-component-manager.html
- 分区表  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-guides/partition-tables.html
- OTA 基础 API  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-reference/system/ota.html
- HTTPS OTA  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-reference/system/esp_https_ota.html
- API 参考首页  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/api-reference/index.html
- 库与框架入口  
  https://docs.espressif.com/projects/esp-idf/zh_CN/stable/esp32/libraries-and-frameworks/index.html

## Preferred Lookup Order

1. 用户要命令或构建行为：先看 `idf.py`
2. 用户要配置项：先看 Kconfig / Configuration Options Reference
3. 用户要组件组织方式：先看 Build System
4. 用户要第三方或官方库：先看 Component Manager 和 Libraries and Frameworks
5. 用户要联网升级：先分清 `merge-bin`/`uf2` 和运行时 OTA API

## Useful Shortcut

在项目根目录执行：

```sh
idf.py docs
```

这个命令会在浏览器里打开与当前目标芯片和 ESP-IDF 版本匹配的官方文档。
