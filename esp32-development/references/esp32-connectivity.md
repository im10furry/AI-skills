# ESP32 Connectivity Guidance

## 1. Scope

Use this file for:

- Wi-Fi
- ESP-NETIF
- event-loop integration
- reconnect behavior
- BLE and NimBLE/Bluedroid choices
- connectivity state ownership

Fallback rule:

- For chip-specific radio capabilities, enterprise-auth details, or API differences across IDF versions, consult the official docs first.

Official docs:

- Wi-Fi overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi-driver/overview.html
- ESP-NETIF programming guide root context: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/
- Bluetooth architecture overview: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/bt-architecture/overview.html
- NimBLE host APIs: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/nimble/index.html

## 2. Wi-Fi initialization and ownership

Recommended initialization order:

1. `esp_netif_init()`
2. `esp_event_loop_create_default()`
3. create default netif
4. `esp_wifi_init()`
5. `esp_wifi_set_mode()`
6. `esp_wifi_set_config()`
7. `esp_wifi_start()`

Rules:

- one module should own Wi-Fi state transitions
- connection state should be event-driven
- avoid duplicated connection-state flags across modules
- keep cloud or protocol connection state separate from Wi-Fi link state

Official docs:

- Wi-Fi overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi-driver/overview.html

## 3. Reconnect and failure behavior

Rules:

- apply backoff to reconnect loops
- distinguish auth failure from signal loss
- stop blind retries when configuration is clearly invalid
- make retry policy observable in logs

Common failure pattern:

- one task keeps reconnecting Wi-Fi while another task independently keeps reconnecting MQTT or HTTP without using the actual Wi-Fi state machine

Official docs:

- Wi-Fi overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi-driver/overview.html

## 4. Credential handling

Rules:

- do not hard-code SSIDs, passwords, certificates, or enterprise credentials in source control
- if credentials are stored in NVS, define migration and corruption handling
- configuration writes should tolerate power loss and partial failure

Official docs:

- Programming Guide root: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/

## 5. BLE stack choice

Choose stack by requirement:

- Bluedroid when classic Bluetooth and BLE are both required
- NimBLE when BLE-only support is sufficient

Selection should be based on:

- feature requirement
- memory footprint
- existing codebase dependency
- expected connection model

Official docs:

- Bluetooth architecture overview: https://docs.espressif.com/projects/esp-idf/en/latest/api-guides/bt-architecture/overview.html
- NimBLE host APIs: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/nimble/index.html

## 6. BLE design rules

Rules:

- define advertising payload and interval explicitly
- document GATT layout and characteristic ownership
- keep callbacks lightweight
- move persistence, parsing, and networking out of callbacks
- define full shutdown order and confirm it is reachable from failures

Typical NimBLE shutdown:

1. disconnect peers
2. stop advertising and scanning
3. `nimble_port_stop()`
4. `nimble_port_freertos_deinit()`
5. `nimble_port_deinit()`

Official docs:

- NimBLE host APIs: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/nimble/index.html

## 7. Callback and event-loop discipline

Rules:

- do not parse large payloads in Wi-Fi or BLE callbacks
- do not block callbacks with storage or cloud requests
- use queues, notifications, or dispatcher tasks for follow-up work

Official docs:

- Wi-Fi overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/wifi-driver/overview.html
- NimBLE host APIs: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/bluetooth/nimble/index.html
