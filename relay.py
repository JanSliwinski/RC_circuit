
import RPi.GPIO as GPIO
import time

#set_up
GPIO.setmode(GPIO.BCM)
relay_pins = [10, 9, 11, 25, 8]

try:
	for pin in relay_pins:
		GPIO.setup(pin, GPIO.OUT)
		GPIO.output(pin, GPIO.HIGH)
	
	for pin in relay_pins:
		print(f"Setting high pin {pin}.")
		GPIO.output(pin, GPIO.LOW)
	while True:
		time.sleep(0.5)
except KeyboardInterrupt:
	print("Turning off relays")
finally:
	print("Exiting program")
	GPIO.cleanup()
	
