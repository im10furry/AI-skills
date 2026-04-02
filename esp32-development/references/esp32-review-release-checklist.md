# ESP32 Review, Test, and Release Checklist

## 1. Default rule

Use this file for review, test planning, packaging, release, and manufacturing readiness checks.

If the checklist does not cover a case, is not detailed enough, or the repository uses a different ESP-IDF version or chip target, consult the official Espressif documentation first.

Official docs:

- ESP-IDF Programming Guide root: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

## 2. Code review checklist

### 2.1 Architecture and module boundaries

Check:

- does each module have one clear responsibility
- is board adaptation separated from business logic
- are lifecycle boundaries clear
- is state ownership duplicated across modules

Official docs:

- build system: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
- style guide: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/contribute/style-guide.html

### 2.2 Concurrency, callbacks, and ISR safety

Check:

- blocking work in callbacks
- ISR-unsafe operations
- deadlock and lock-order risk
- misuse of queues, event groups, or task notifications

Official docs:

- fatal errors: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/fatal-errors.html

### 2.3 Error handling

Check:

- are return values checked
- are cleanup paths complete
- is `ESP_ERROR_CHECK()` used where recovery is required
- do logs preserve error code and stage

Official docs:

- error handling: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/error-handling.html
- error code reference: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/error-codes.html

### 2.4 Logging and observability

Check:

- unique module `TAG`s
- logs at key state transitions
- excessive logging in hot paths
- production log level too high

Official docs:

- logging library: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/log.html

### 2.5 Memory and resource handling

Check:

- realistic task stack sizes
- memory, handle, and peripheral leaks
- repeated allocation of long-lived objects
- unsafe PSRAM assumptions

Official docs:

- heap memory allocation: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/mem_alloc.html
- heap debugging: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/heap_debug.html

### 2.6 Wi-Fi, BLE, low-power, OTA, and security

Check:

- Wi-Fi init order and reconnect logic
- BLE callback weight and full shutdown path
- low-power entry and wakeup assumptions
- OTA validation, boot confirmation, and rollback
- secure boot, flash encryption, and credential handling

Official docs:

- Wi-Fi overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi-driver/overview.html
- Bluetooth architecture: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/bt-architecture/overview.html
- sleep modes: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html
- partition tables: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html
- Secure Boot v2: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html
- flash encryption: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html

## 3. Test expectations

### 3.1 Unit tests

Unit-test component logic when behavior can be isolated.

Example:

```c
TEST_CASE("wifi manager returns timeout when connect waits too long", "[wifi_mgr]") {
    // test body
}
```

Rules:

- tests should describe behavior, not just function names
- place component tests where the project structure expects them
- do not treat lack of tests as acceptable for failure-prone logic without explanation

Official docs:

- unit testing in ESP32: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/unit-tests.html

### 3.2 Integration tests

Cover at least:

- Wi-Fi connect, disconnect, reconnect
- BLE advertise, connect, disconnect, data path
- OTA upgrade, reboot, health-check, rollback
- low-power entry and wakeup
- NVS/config migration
- peripheral init and error recovery

Official docs:

- unit testing guide and related test guidance: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/unit-tests.html

### 3.3 Hardware validation

Require real hardware for:

- GPIO
- UART, I2C, SPI
- ADC
- I2S/audio
- battery and sleep-current measurement
- wakeup behavior
- radio behavior

Official docs:

- peripherals index: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/index.html
- GPIO: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html
- UART: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html
- ADC: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc/index.html
- I2S: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/i2s.html

## 4. CI/CD checklist

Minimum expectations:

- build runs with a pinned ESP-IDF version
- format/lint/build gates exist as appropriate for the repository
- important test stages run before release
- artifacts and checksums are archived
- secrets are injected through CI secrets, not stored in the repo

Official docs:

- build system: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
- `idf.py` frontend: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-py.html

## 5. Packaging and flashing checklist

Release output should include:

- full flash package
- OTA package
- checksum file
- release metadata

Example merge command:

```bash
esptool.py --chip esp32 merge_bin -o build/full_package.bin \
  --flash_mode dio --flash_size 4MB --flash_freq 40m \
  0x1000 build/bootloader/bootloader.bin \
  0x8000 build/partition_table/partition-table.bin \
  0x10000 build/<project_name>.bin
```

Checks:

- flash mode/size/frequency match the build configuration
- chip-specific offsets are parameterized
- OTA package naming is versioned and traceable
- packaging logs clearly show artifact paths and checksums

Official docs:

- partition tables: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html
- firmware update and flashing FAQ: https://docs.espressif.com/projects/esp-faq/en/latest/development-environment/firmware-update.html

## 6. Git workflow checklist

Recommendations:

- `feature/*` for new work
- `fix/*` for bug fixes
- `release/*` for release preparation
- `hotfix/*` for urgent production fixes
- use clear commit messages, preferably a consistent convention such as Conventional Commits

Merge gate:

- build passes
- key self-test is done
- docs and config are updated with the code
- no generated artifacts are committed by mistake
- OTA/security/low-power changes have specific validation evidence

Official docs:

- build system and project configuration docs above are the baseline when a workflow change affects packaging, partitions, or configuration

## 7. Release checklist

Before release, confirm:

- branch, tag, version, and build metadata are aligned
- partition table and packaging scripts are aligned
- full package and OTA package were both generated
- checksums were generated and verified
- rollback path is defined and, where possible, tested
- security materials came from the correct source and were not substituted ad hoc
- release log level is appropriate

Official docs:

- partition tables: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html
- Secure Boot v2: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html
- flash encryption: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html

## 8. Manufacturing and repair notes

Checks:

- manufacturing scripts record result, time, and device identity
- repair flows distinguish development repair from production repair
- devices with security features enabled have a documented reflash policy
- eFuse writes are logged and traceable

Official docs:

- security overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/security.html
- firmware update and flashing FAQ: https://docs.espressif.com/projects/esp-faq/en/latest/development-environment/firmware-update.html
