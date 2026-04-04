---
name: esp32-development
description: ESP32 and ESP-IDF firmware development, review, debugging, architecture, OTA, partition table, Wi-Fi, BLE, peripherals, low-power, memory, security, packaging, and release workflow guidance. Use when working on ESP32-family projects, drafting standards, reviewing firmware, debugging boot/runtime failures, or preparing OTA and production releases.
---

# ESP32 Development

Use this skill for ESP32-family firmware work. Keep the skill body lean and use the references for detail.

## Default rule

If this skill or its references do not cover a topic, are not detailed enough for the current target, or conflict with the repository or ESP-IDF version in use, consult Espressif official documentation and follow the official documentation first.

Do not guess on:

- chip-specific pin limits
- sleep behavior
- eFuse/security operations
- OTA partition behavior
- API behavior that changed across ESP-IDF versions

## Entry points

Read only the reference file that matches the task first:

- For topic selection and overall navigation:
  - Read [references/esp32-development-spec.md](references/esp32-development-spec.md)
- For core architecture, project layout, coding rules, lifecycle, FreeRTOS, logging, error handling, and memory:
  - Read [references/esp32-core-and-architecture.md](references/esp32-core-and-architecture.md)
- For Wi-Fi, BLE, event handling, and reconnect behavior:
  - Read [references/esp32-connectivity.md](references/esp32-connectivity.md)
- For GPIO, UART, ADC, I2S, LEDC, and board-level peripheral work:
  - Read [references/esp32-peripherals.md](references/esp32-peripherals.md)
- For low-power, secure boot, flash encryption, and eFuse-sensitive changes:
  - Read [references/esp32-power-and-security.md](references/esp32-power-and-security.md)
- For partition design, OTA, HTTPS OTA, rollback, and package layout:
  - Read [references/esp32-ota-and-partitions.md](references/esp32-ota-and-partitions.md)
- For code review, test planning, CI/CD, packaging, release, manufacturing, and merge gates:
  - Read [references/esp32-review-release-checklist.md](references/esp32-review-release-checklist.md)

Do not load all references by default.

## What to confirm before acting

Before making code or review decisions, confirm:

- target chip: `ESP32`, `ESP32-S2`, `ESP32-S3`, `ESP32-C3`, `ESP32-C6`, `ESP32-H2`, or another variant
- framework: `ESP-IDF` or `Arduino ESP32`
- ESP-IDF version and toolchain
- board resources: flash, PSRAM, key GPIOs, power model, external peripherals
- task type: implementation, debugging, review, standards/doc, release
- risk areas: OTA, secure boot, flash encryption, eFuse, low-power, battery operation, audio, multi-task concurrency

If the repository already contains those answers, extract them from code and config first instead of asking.

## Working defaults

### Implementation

1. Confirm lifecycle and thread model first.
2. Make state transitions, failure paths, cleanup paths, and logging boundaries explicit.
3. Prefer ESP-IDF abstractions over direct register work unless there is a clear reason not to.
4. After changes, check buildability and likely regressions.

### Review

Prioritize:

- init/deinit order
- callback and ISR safety
- error propagation and cleanup
- logging quality and logging volume
- stack, heap, handle, and peripheral resource closure
- OTA, partition, security, and low-power release risk

### Debugging

Collect facts before proposing fixes:

- panic log, backtrace, error code, reproduction path, chip, config
- whether failure is boot-time or runtime
- whether it is deterministic or long-run
- whether it correlates with Wi-Fi, BLE, OTA, sleep/wakeup, PSRAM, audio, or interrupts

Present debugging output as:

- symptom
- narrowed scope
- most likely root cause
- validation steps

## Output rules

### When writing code

- Keep lifecycle, failure path, and cleanup strategy explicit.
- Call out behavior changes and regression risk.
- State chip applicability when a change is target-specific.

### When writing standards/docs

- State scope and requirement level first.
- Use `must`, `should`, and `may`.
- For risky topics, include review or release checks, not only principles.
- Include official Espressif documentation links per major section.

### When writing reviews

- Findings first, summary second.
- Sort by severity.
- Include file/function context, consequence, and fix direction when possible.

## Official documentation baseline

Use official Espressif docs as the primary source. Start from:

- ESP-IDF Programming Guide: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/
- ESP-IDF Build System: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
- ESP-IDF Style Guide: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/contribute/style-guide.html
- ESP32 security overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/security.html

If the target is not `esp32`, switch the chip path in the official docs to the correct target before making a chip-specific claim.

## Common failure patterns

- blocking work inside BLE or Wi-Fi callbacks
- normal logging or heap allocation inside ISRs
- stack sizes chosen by guesswork
- `ESP_ERROR_CHECK()` used in production recovery paths
- OTA that downloads successfully but never confirms boot or rollback behavior
- low-power logic validated only through API calls, not board-level current measurement
- security and eFuse operations mixed into normal dev flows
- chip differences scattered across business logic instead of isolated in an adaptation layer
