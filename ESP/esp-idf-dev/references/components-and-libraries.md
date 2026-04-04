# Components And Libraries

## Local Components

创建新组件：

```sh
idf.py create-component my_component
```

常见结构：

```text
components/
  my_component/
    CMakeLists.txt
    include/
      my_component.h
    my_component.c
```

## Register A Component

在组件的 `CMakeLists.txt` 中使用 `idf_component_register()`：

```cmake
idf_component_register(
    SRCS "my_component.c"
    INCLUDE_DIRS "include"
    REQUIRES esp_wifi
    PRIV_REQUIRES nvs_flash
)
```

依赖声明规则：

- `REQUIRES`：当前组件的公共头文件里直接依赖到的组件
- `PRIV_REQUIRES`：只在实现文件里使用，或只为链接所需的组件
- `main` 组件会自动依赖其他组件，因此很多情况下无需显式写 `REQUIRES`

## Source File Strategy

- 团队项目优先用显式 `SRCS`，便于增量构建稳定工作。
- `SRC_DIRS` 也可以用，但新增源文件后通常要运行：

```sh
idf.py reconfigure
```

## Managed Dependencies

IDF 组件管理器使用 `idf_component.yml` 管理清单和依赖。

创建清单：

```sh
idf.py create-manifest
idf.py create-manifest --component=my_component
idf.py create-manifest --path="../../my_component"
```

添加依赖：

```sh
idf.py add-dependency example/cmp
idf.py add-dependency --component=my_component example/cmp<=3.3.3
idf.py add-dependency --path="../../my_component" example/cmp^3.3.3
```

更新依赖：

```sh
idf.py update-dependencies
```

重要约束：

- 新增某个组件的 `idf_component.yml` 后，先执行 `idf.py reconfigure`
- 组件管理器会自动创建 `dependencies.lock`
- 组件下载内容位于 `managed_components`
- 不要手动修改 `dependencies.lock` 和 `managed_components`

## Dependency Sources

`idf_component.yml` 中的依赖可以来自：

- 乐鑫组件注册表
- Git 仓库
- 本地路径

因此，用户说“引入一个库”时，优先判断它是本地组件、注册表依赖，还是 Git 依赖。

## BSP, Libraries, And Frameworks

- BSP（板级支持包）通过 IDF 组件管理器发布。
- 例如把 ESP-WROVER-KIT BSP 加入项目：

```sh
idf.py add-dependency esp_wrover_kit
```

- 用户说“框架”时，先查看官方的 Libraries and Frameworks 入口，再判断是否应通过组件注册表引入，还是在项目内封装成本地组件。

## Prebuilt Static Libraries

如果已有外部构建过程生成的 `.a` 静态库，可以在组件中用：

```cmake
add_prebuilt_library(target_name lib_path [REQUIRES req1 ...] [PRIV_REQUIRES req2 ...])
```

注意：

- 预建库必须与当前项目目标芯片一致
- 预建库的编译选项、ABI、工具链参数也要与当前项目匹配
- 否则很容易出现隐蔽 bug 或链接问题

## API Lookup Strategy

用户说“找 API”时，优先按功能把问题映射到 API 参考目录：

- 连网：Wi-Fi、ESP-NETIF、HTTP、MQTT、TLS
- 外设：GPIO、UART、SPI、I2C、ADC、RMT
- 系统：FreeRTOS、事件循环、日志、OTA、定时器、电源管理
- 存储：NVS、SPIFFS、分区 API、FATFS
