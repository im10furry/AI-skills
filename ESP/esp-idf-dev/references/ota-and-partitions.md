# OTA And Partitions

## Split The Problem First

先把“OTA”拆成三类任务：

- 生成一个可交付的固件包：`merge-bin`、`uf2`
- 让设备具备 OTA 槽位和启动选择：分区表
- 在代码里实现联网升级：`esp_https_ota` 或其他 OTA API

不要把这三件事混在一起回答。

## Partition Table Basics

- ESP32 默认在 flash 偏移 `0x8000` 处写分区表。
- 直接查看当前分区摘要：

```sh
idf.py partition-table
```

- 在 `menuconfig` 的 `CONFIG_PARTITION_TABLE_TYPE` 下，可选常见内置方案：
  - 单 factory app，无 OTA
  - factory app + 两个 OTA 定义

- 双槽 OTA 至少需要：
  - `otadata`
  - `ota_0`
  - `ota_1`

官方文档说明，bootloader 会读取 `otadata` 来决定从哪个 OTA 应用分区启动；若 `otadata` 为空，则会启动 `factory`。

## Minimal Dual-Slot Example

```csv
# Name, Type, SubType, Offset, Size
nvs, data, nvs, 0x9000, 0x4000
otadata, data, ota, 0xd000, 0x2000
phy_init, data, phy, 0xf000, 0x1000
factory, app, factory, 0x10000, 1M
ota_0, app, ota_0, , 1M
ota_1, app, ota_1, , 1M
```

- 需要自定义分区表时，在 `menuconfig` 里选择自定义 CSV，并指向项目中的 `partitions.csv`。
- 除非必须固定地址，否则优先把 OTA app 分区的 `Offset` 留空，让工具按当前分区表偏移和对齐规则自动计算。

## Useful OTA Maintenance Commands

```sh
idf.py read-otadata
idf.py -p COM3 erase-otadata
```

- `read-otadata` 可查看当前 OTA 启动选择信息。
- `erase-otadata` 适合在测试 OTA 回切、启动异常或恢复 factory 流程时使用。

## Runtime HTTPS OTA

要在代码里实现通过 HTTPS 下载并更新固件，优先使用 `esp_https_ota`。

组件依赖：

```cmake
idf_component_register(
    SRCS "ota_task.c"
    INCLUDE_DIRS "."
    REQUIRES esp_https_ota
)
```

最小调用骨架：

```c
esp_http_client_config_t http_cfg = {
    .url = CONFIG_FIRMWARE_UPGRADE_URL,
    .cert_pem = (char *)server_cert_pem_start,
};

esp_https_ota_config_t ota_cfg = {
    .http_config = &http_cfg,
};

ESP_ERROR_CHECK(esp_https_ota(&ota_cfg));
esp_restart();
```

## HTTPS OTA Notes

- 必须配置服务端证书校验；优先使用根证书，或使用 x509 证书包。
- 内存紧张时，可启用 partial download。
- 需要中断恢复时，可结合 NVS 记录已写入字节数并启用 OTA resume。
- 安全要求更高时，再看签名校验和预加密固件方案。

## Recommended Examples

- `system/ota/simple_ota_example`
- `system/ota/advanced_https_ota`
- `system/ota/partitions_ota`

## Packaging Is Not Runtime OTA

下面这些命令是“打包交付物”，不是“设备在线升级逻辑”：

```sh
idf.py merge-bin -o dist/merged.bin -f raw
idf.py uf2
```

- `merge-bin` 适合工厂烧录、发给其他机器烧录、归档单文件产物。
- `uf2` 适合 USB 拖放烧录场景。
- 如果用户说“生成 OTA 包”，先追问或判断他要的是：
  - 工厂/发布用单文件固件
  - 可由 bootloader 切换的 OTA 分区布局
  - 运行中的设备下载并安装新固件
