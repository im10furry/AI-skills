# ESP32 OTA and Partition Guidance

## 1. Scope

Use this file for:

- partition tables
- OTA-capable layouts
- app update flow
- HTTPS OTA
- boot confirmation
- rollback behavior
- package contents and traceability

Fallback rule:

- If OTA behavior, app-update APIs, or partition details are unclear for the target or IDF version, use the official Espressif documentation as the authority.

Official docs:

- partition tables: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html
- OTA API: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html
- ESP HTTPS OTA: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/esp_https_ota.html

## 2. Partition-table rules

Rules:

- OTA-capable designs must include `otadata` and at least two app partitions
- partition sizes must be selected from actual artifact size and expected growth
- partition changes must be reviewed together with flashing, packaging, and migration impact
- data partitions should be sized from real use, not copied from examples without thought

Example:

```csv
# Name,     Type, SubType, Offset,  Size,   Flags
nvs,        data, nvs,     0x9000,  0x4000,
otadata,    data, ota,     0xd000,  0x2000,
phy_init,   data, phy,     0xf000,  0x1000,
ota_0,      app,  ota_0,   0x10000, 1600K,
ota_1,      app,  ota_1,            1600K,
```

Official docs:

- partition tables: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html

## 3. OTA flow requirements

Minimum acceptable OTA flow:

1. download
2. integrity validation
3. write to inactive app slot
4. select boot target
5. reboot
6. run application health check
7. confirm or roll back

Rules:

- do not call OTA done just because the download succeeded
- define application self-test and boot confirmation conditions
- design rollback behavior before release

Official docs:

- OTA API: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/ota.html

## 4. HTTPS OTA guidance

Rules:

- use HTTPS OTA when the product architecture fits it
- define certificate source and update policy
- treat redirect and CA-bundle behavior explicitly
- if more control is needed than the single-call API provides, use the staged OTA APIs

Official docs:

- ESP HTTPS OTA: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/esp_https_ota.html

## 5. Security interaction

Rules:

- when secure boot is enabled, OTA images must meet the signing requirements of the target
- do not plan first-time secure feature enablement through OTA unless the official workflow explicitly supports it for the exact target and process
- confirm packaging, signing, and rollback assumptions together

Official docs:

- Secure Boot v2: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html
- flash encryption: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html

## 6. Release artifact requirements

Recommended release outputs:

- full flash package
- OTA package
- checksum file
- release metadata

Rules:

- package names should be versioned and traceable
- flashing offsets and chip mode parameters must come from the build configuration
- full package and OTA package should not be conflated

Example merge command:

```bash
esptool.py --chip esp32 merge_bin -o build/full_package.bin \
  --flash_mode dio --flash_size 4MB --flash_freq 40m \
  0x1000 build/bootloader/bootloader.bin \
  0x8000 build/partition_table/partition-table.bin \
  0x10000 build/<project_name>.bin
```

Official docs:

- partition tables: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html
- firmware update and flashing FAQ: https://docs.espressif.com/projects/esp-faq/en/latest/development-environment/firmware-update.html
