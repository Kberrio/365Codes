import RPi.GPIO as GPIO
import time

# Pin Definitions
led_pin = 18  # BCM pin 18, Physical pin 12

# GPIO setup
GPIO.setmode(GPIO.BCM)  # Use BCM pin numbering
GPIO.setup(led_pin, GPIO.OUT)  # Set pin as an output pin

try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  # Turn LED on
        time.sleep(1)  # Sleep for 1 second
        GPIO.output(led_pin, GPIO.LOW)   # Turn LED off
        time.sleep(1)  # Sleep for 1 second

except KeyboardInterrupt:
    # Gracefully handle the Ctrl+C interruption
    pass

finally:
    GPIO.cleanup()  # Cleanup GPIO settings
