# 03_led_and_switch_poll.py
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# Pin setup
LED_PIN = 17
BUTTON_PIN = 23

# LED as output
GPIO.setup(LED_PIN, GPIO.OUT)

# Button as input with internal pull-up resistor
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Press the button (GPIO 23) to toggle the LED (GPIO 17). Press Ctrl+C to quit.")
    while True:
        button_state = GPIO.input(BUTTON_PIN)
        if button_state == GPIO.LOW:  # Button pressed
            print("Button status: ON or Button Pressed")
            GPIO.output(LED_PIN, True)   # Turn LED ON
        else:                           # Button not pressed
            print("Button status: OFF or Button Not Pressed")
            GPIO.output(LED_PIN, False)  # Turn LED OFF
        time.sleep(0.2)  # small delay to avoid high CPU usage

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()
