# ESP32 Development Specification Index

## Purpose

This file is the entry index for implementation-facing ESP32 guidance in this skill.

Use it to choose the right detailed reference first instead of loading everything.

Global rule:

- If a topic is missing here, not detailed enough, or differs from the ESP-IDF version, chip target, board design, or repository architecture in use, consult the official Espressif documentation first.

Official docs:

- ESP-IDF Programming Guide root: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/
- ESP-IDF build system: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
- ESP-IDF style guide: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/contribute/style-guide.html

## Read order

Choose by task:

- Core project structure, coding rules, API design, lifecycle, FreeRTOS, logging, error handling, memory:
  - Read [esp32-core-and-architecture.md](esp32-core-and-architecture.md)
- Wi-Fi, ESP-NETIF, BLE, reconnect logic, event handling, connectivity state:
  - Read [esp32-connectivity.md](esp32-connectivity.md)
- GPIO, LEDC, UART, I2C, SPI, ADC, I2S, audio, board-level pin limits:
  - Read [esp32-peripherals.md](esp32-peripherals.md)
- sleep modes, DFS, power-management locks, secure boot, flash encryption, eFuse, provisioning constraints:
  - Read [esp32-power-and-security.md](esp32-power-and-security.md)
- partition tables, OTA flows, HTTPS OTA, boot confirmation, rollback, package layout:
  - Read [esp32-ota-and-partitions.md](esp32-ota-and-partitions.md)
- review, tests, CI/CD, packaging checks, release gates, manufacturing:
  - Read [esp32-review-release-checklist.md](esp32-review-release-checklist.md)

## Minimum baseline for any ESP32 task

Before making design or code decisions, confirm:

- chip target and supported chip matrix
- ESP-IDF version
- framework mode: ESP-IDF or Arduino ESP32
- flash and PSRAM layout
- power model and wakeup expectations
- board pin mapping and restricted pins
- partition scheme
- whether the path touches OTA, secure boot, flash encryption, or eFuse

## Requirement levels

Use these terms consistently in implementation-facing docs:

- `must`: required
- `should`: recommended unless there is a documented reason not to
- `may`: optional

## Decision guardrails

Default engineering posture:

- prefer explicit lifecycle and cleanup over implicit global state
- prefer official ESP-IDF APIs over custom low-level reimplementation
- keep callbacks and ISRs lightweight
- isolate chip-specific behavior in an adaptation layer when possible
- treat OTA, low-power, and security as release-critical topics

## Official documentation reminder

For chip-specific claims, switch the `esp32` path in official docs to the actual target, such as `esp32s3`, `esp32c3`, or `esp32h2`, before using the document as the authority.
