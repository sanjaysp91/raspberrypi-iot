# 01_blink.py
import RPi.GPIO as GPIO
import time

# Use Broadcom (BCM) pin numbering
GPIO.setmode(GPIO.BCM)

# Set up pin 17 as an output pin
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    print("Blinking... Press Ctrl+C to stop.")
    while True:
        GPIO.output(LED_PIN, True)   # LED ON
        print("LED status: ON")
        time.sleep(1)                # wait 1 second
        GPIO.output(LED_PIN, False)  # LED OFF
        print("LED status: OFF")
        time.sleep(1)                # wait 1 second

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    print("Cleaning up GPIO")
    GPIO.cleanup()  # Reset GPIO settings when exiting
