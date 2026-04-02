# ESP32 Peripheral Guidance

## 1. Scope

Use this file for:

- GPIO
- LEDC/PWM
- UART
- I2C
- SPI
- ADC
- I2S and audio
- board-level peripheral ownership

Fallback rule:

- Any claim about pin capability, electrical behavior, ADC ranges, or target-specific peripheral limits must be verified against the official docs and the actual chip datasheet.

Official docs:

- peripherals index: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/index.html
- GPIO: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html
- UART: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html
- ADC: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc/index.html
- I2S: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/i2s.html

## 2. Board mapping rules

Rules:

- document all application-used pins in one place
- mark strapping pins and restricted pins explicitly
- define safe boot state and safe shutdown state for outputs
- do not assume a pin capability from another chip family

Official docs:

- GPIO: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html

## 3. GPIO

Rules:

- configure through `gpio_config_t`
- document direction, pull mode, interrupt mode, and safe default state
- keep ISR handlers minimal and deferred

Official docs:

- GPIO: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/gpio.html

## 4. LEDC / PWM

Rules:

- define frequency, resolution, timer binding, and channel ownership
- verify multi-channel frequency and resolution constraints
- restore or release the pin to a safe state on stop

Official docs:

- LEDC: https://docs.espressif.com/projects/esp-idf/en/latest/api-reference/peripherals/ledc.html

## 5. UART

Rules:

- separate debug console use from business protocol use where possible
- define framing, timeout, and resync behavior
- use direct IO_MUX routing only when baud-rate or signal requirements justify it
- do not bury protocol parsing in ISR-like contexts

Official docs:

- UART: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/uart.html

## 6. I2C and SPI

Rules:

- define bus ownership and locking
- define recovery strategy for bus faults
- do not let multiple modules silently reconfigure the same bus
- verify DMA and alignment constraints where relevant

Official docs:

- peripherals index: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/index.html

## 7. ADC

Rules:

- define attenuation and calibration strategy
- do not rely on raw ADC values for product decisions without calibration or scaling logic
- validate noise behavior on real hardware
- watch for target-specific ADC differences

Official docs:

- ADC overview: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc/index.html
- ADC continuous mode: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/adc/adc_continuous.html

## 8. I2S and audio

Rules:

- define sample rate, bit width, channels, DMA depth, and task ownership
- validate CPU and RAM impact under realistic load
- verify that networking and audio timing do not starve each other
- use APLL only when the accuracy requirement justifies it

Official docs:

- I2S: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/i2s.html

## 9. Validation guidance

Hardware validation is required for:

- signal integrity
- startup states
- ADC accuracy
- audio continuity
- wake-up pin behavior

Official docs:

- peripherals index: https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/index.html
