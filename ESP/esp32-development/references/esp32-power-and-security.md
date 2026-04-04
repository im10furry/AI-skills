# ESP32 Power and Security Guidance

## 1. Scope

Use this file for:

- sleep modes
- dynamic frequency scaling
- power-management locks
- wake sources
- secure boot
- flash encryption
- eFuse handling
- provisioning constraints

Fallback rule:

- Do not improvise sleep, secure boot, flash encryption, or eFuse behavior from memory. For any target-specific or version-specific question, verify in official docs first.

Official docs:

- sleep modes: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html
- power management: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/power_management.html
- security overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/security.html
- Secure Boot v2: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html
- flash encryption: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html

## 2. Low-power mode selection

Guidance:

- use DFS and power-management locks when the CPU stays active but can slow down
- use Light-sleep when faster wakeup matters
- use Deep-sleep when battery savings dominate the requirement

Rules:

- choose power mode from product behavior, not API convenience
- document wakeup sources and post-wakeup behavior
- measure current on real hardware

Official docs:

- sleep modes: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html
- power management: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/power_management.html

## 3. Sleep entry and wakeup rules

Rules:

- configure at least one valid wake source before entering sleep
- stop or disable radio and nonessential peripherals when required by the target and design
- separate cold boot and wake-from-sleep logic
- log wake reason during validation and issue analysis

Official docs:

- sleep modes: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html

## 4. Board-level power validation

Rules:

- validate leakage on the actual board, not only the chip
- inspect LDO, pull resistors, sensors, and powered peripherals
- validate wake pin levels and external pull interactions

Official docs:

- sleep modes: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/sleep_modes.html

## 5. Secure Boot

Rules:

- explicitly decide whether production uses Secure Boot
- keep signing keys under controlled handling
- understand chip revision and algorithm constraints before enabling
- update manufacturing, OTA, and repair flows together with secure-boot changes

Official docs:

- Secure Boot v2: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/secure-boot-v2.html
- security enablement workflows: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/security/security-features-enablement-workflows.html

## 6. Flash encryption

Rules:

- explicitly decide whether production uses flash encryption
- treat encrypted-device servicing as a process topic, not just a build flag
- keep per-device key strategy documented if used

Official docs:

- flash encryption: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/flash-encryption.html

## 7. eFuse operations

Rules:

- eFuse writes must be isolated from normal dev scripts
- show operators exactly what bits are being written
- log eFuse operations for traceability
- never treat eFuse changes as routine debug actions

Official docs:

- security overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/security.html

## 8. Device identity and provisioning

Rules:

- keys, certs, and credentials must not live in source control
- define provisioning ownership and revocation model
- document repair or reprovisioning policy for secured devices

Official docs:

- security overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/security/security.html
