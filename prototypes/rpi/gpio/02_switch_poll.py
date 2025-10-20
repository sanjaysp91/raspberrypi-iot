# 02_switch_poll.py
import RPi.GPIO as GPIO
import time

# Use Broadcom (BCM) pin numbering 
GPIO.setmode(GPIO.BCM)

# Setup Pin 23 as an input pin with internal pull-up  
SWITCH_PIN = 23
GPIO.setup(SWITCH_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    print("Reading Switch State... Press Ctrl+C to stop.")
    while True:
        if GPIO.input(SWITCH_PIN) == False:
            print("Button Pressed")
            time.sleep(0.2)

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    print("Cleaning up GPIO")
    GPIO.cleanup() 	# Reset GPIO settings when exiting 
