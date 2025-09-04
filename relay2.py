import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
relay_pins = [9, 10, 11, 5, 6]

for pin in relay_pins:
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)

for pin in relay_pins:
	GPIO.output(pin, GPIO.HIGH)
	print(f"pin {pin} ON")
	time.sleep(2)
	
for pin in relay_pins:
	GPIO.output(pin, GPIO.LOW)
	print(f"pin {pin} OFF")
	time.sleep(1)

GPIO.cleanup()

