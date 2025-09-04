import RPi.GPIO as GPIO
import time

pin = 27

GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT, initial = GPIO.LOW)
print("OFF")
time.sleep(5)
GPIO.output(pin, GPIO.HIGH)
print("ON")
time.sleep(5)
"""
GPIO.output(4, GPIO.HIGH)
print("pin 4 ON")
time.sleep(5)
GPIO.output(pin, GPIO.LOW)
print("pin 4 OFF")
time.sleep(5)
"""



GPIO.cleanup()



