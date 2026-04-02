# ESP32 Core and Architecture Guidance

## 1. Scope

Use this file for:

- project layout
- configuration management
- coding rules
- API design
- lifecycle and cleanup
- FreeRTOS task structure
- logging
- error handling
- memory ownership

Fallback rule:

- If a behavior depends on a specific IDF version, chip family, or repository setup, verify it in the official docs first.

Official docs:

- Programming Guide root: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/
- build system: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
- style guide: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/contribute/style-guide.html

## 2. Project baseline

Each project should clearly record:

- chip target and supported chip matrix
- ESP-IDF version
- toolchain version
- flash and PSRAM configuration
- partition table scheme
- board mapping

Any implementation rule that depends on version or chip should say so explicitly.

Official docs:

- `idf.py` frontend: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-guides/tools/idf-py.html
- reproducible builds: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/reproducible-builds.html

## 3. Project structure

Recommended layout:

```text
.
├─ main/
├─ components/
│  ├─ board/
│  ├─ app_core/
│  ├─ wifi_mgr/
│  ├─ ble_service/
│  └─ ...
├─ docs/
├─ tools/
├─ test/
├─ sdkconfig.defaults
├─ CMakeLists.txt
└─ README.md
```

Rules:

- `main/` should stay as the composition layer
- keep reusable logic in components
- keep hardware mapping and release notes in `docs/`
- keep scripts in `tools/`
- generated artifacts should not be committed unless the repo explicitly requires them

Official docs:

- build system: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/build-system.html
- build system v2: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/build-system-v2.html
- configuration options reference: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/kconfig-reference.html

## 4. Coding conventions

Rules:

- use 4 spaces
- no tabs
- use K&R braces
- always use braces for branch bodies
- keep line length controlled
- use UTF-8 with LF line endings
- end files with a single newline

Naming:

- `snake_case` for files, functions, local variables, and static variables
- uppercase with underscores for macros and compile-time constants
- component prefix for public interfaces
- `static` for file-local functions and variables

Headers:

1. current module header
2. C standard library
3. ESP-IDF and third-party headers
4. project headers

Comments:

- explain constraints and rationale
- do not narrate obvious code
- document sequencing, callback restrictions, and cleanup assumptions

Official docs:

- style guide: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/contribute/style-guide.html
- Arduino coding guidelines when relevant: https://docs.espressif.com/projects/arduino-esp32/en/latest/guides/coding_guidelines.html

## 5. API design and lifecycle

Preferred lifecycle:

1. `init`
2. `start`
3. `stop`
4. `deinit`

Rules:

- `init` allocates resources and initializes dependencies
- `start` begins runtime work
- `stop` stops runtime work
- `deinit` releases resources
- partial init failure must roll back earlier steps
- ownership of every allocated resource must be obvious

Public API guidance:

- return `esp_err_t` or a clearly defined project-specific enum
- define timeout semantics for blocking APIs
- document thread or ISR restrictions
- avoid hidden mutable global state unless the module is explicitly singleton-based

Official docs:

- Programming Guide root: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

## 6. Concurrency and callback discipline

Rules:

- callbacks must stay lightweight
- long work must move to a task or deferred execution path
- shared mutable state must have an explicit synchronization rule
- ISR code must not block, allocate normal heap memory, or use normal logging

Good default pattern:

- ISR or callback captures minimal data
- wake a task via queue, notification, or event group
- task handles parsing, storage, networking, or retries

Official docs:

- fatal errors: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/fatal-errors.html

## 7. FreeRTOS task structure

Rules:

- one clear responsibility per task
- do not use permanent polling loops when an event-driven design is enough
- choose stack sizes from evidence, not habit
- check task high-water marks during validation
- choose priorities with a concrete reason, especially for radio, audio, sampling, and OTA paths

Recommended IPC choices:

- task notification for single-consumer wakeups
- queue for message passing
- event group for state bits

Official docs:

- Programming Guide root: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

## 8. Logging

Rules:

- each source file should have one `TAG`
- use `ESP_LOGE` for real failures
- include stage, object, and error code where useful
- avoid noisy logs in hot paths
- do not use normal log macros in ISRs
- keep production log level at or below `INFO` by default

Official docs:

- logging library: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/log.html

## 9. Error handling

Rules:

- do not ignore return values
- do not swallow recoverable failures without logging or propagation
- prefer cleanup blocks when multiple resources are acquired
- use `ESP_ERROR_CHECK()` carefully in production paths

Preferred macros:

- `ESP_RETURN_ON_ERROR`
- `ESP_GOTO_ON_ERROR`
- `ESP_RETURN_ON_FALSE`
- `ESP_GOTO_ON_FALSE`

Official docs:

- error handling: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/error-handling.html
- error codes: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/error-codes.html

## 10. Memory ownership and debugging

Rules:

- every dynamic allocation must have a clear owner
- task stacks must be validated
- keep large buffers out of small stacks
- use capability-aware allocation when DMA or memory class matters
- validate PSRAM assumptions against actual performance needs

Useful metrics:

- `xPortGetFreeHeapSize()`
- `xPortGetMinimumEverFreeHeapSize()`
- `heap_caps_get_largest_free_block()`
- `heap_caps_print_heap_info()`

Debugging methods:

- heap tracing
- per-task allocation inspection
- soak testing for fragmentation-sensitive paths

Official docs:

- heap memory allocation: https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/mem_alloc.html
- heap debugging: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/system/heap_debug.html
