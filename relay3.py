import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [5, 6, 9, 10, 11]

for pin in pins:
	GPIO.setup(pin, GPIO.OUT, initial= GPIO.LOW)

print("Setup ready")
print("7: steering on. 8 mctrl on. 9 motors on. U steering off. I. mctrl off. O motors off.")

def cleanup():
	for pin in pins:
		GPIO.output(pin, GPIO.LOW)
	GPIO.cleanup()
	print("\ncleanup complete")
	
try:
	motor_controllers_on = False
	while True:
		key = input("Choose action: (7, 8, 9, U, I, O): ")
		#Press 7 for steering control on
		if key == '7':
			print("steering ON")
			GPIO.output(11, GPIO.HIGH)
			time.sleep(2)
		#Press 8 for motor control on
		if key == '8':
			GPIO.output(9, GPIO.HIGH)
			print("Motor controller 1 ON")
			time.sleep(1)
			GPIO.output(10, GPIO.HIGH)
			print("Motor controller 2 ON")
			motor_controllers_on = True
		#Press 9 for motors on
		if key == '9':
			if motor_controllers_on:
				GPIO.output(5, GPIO.HIGH)
				print("Motor 1 ON")
				time.sleep(1)
				GPIO.output(6, GPIO.HIGH)
				print("Motor 2 ON")
			else:
				print("Turn on motor-controllers before turning on motors (press key 8)")
########## TURN OFF SYSTEMS
		#Press u to turn off steering
		if key == 'u':
			GPIO.output(11, GPIO.LOW)
			print("Steering OFF")
		#press i to turn off motor controllers
		if key == 'i':
			GPIO.output(9, GPIO.LOW)
			print("Motor controller 1 OFF")
			GPIO.output(10, GPIO.LOW)
			print("Motor controller 2 OFF")
			motor_controllers_on = False
		#press o to turn off motors
		if key == 'o':
			GPIO.output(5, GPIO.LOW)
			print("Motor 1 OFF")
			GPIO.output(6, GPIO.LOW)
			print("Motor 2 OFF")

except KeyboardInterrupt:
	print("exiting")	
except Exception as e:
	print(f"Error: {e}")
finally:
	cleanup()
	
	

