import RPi.GPIO as GPIO
import time

#set up
GPIO.setmode(GPIO.BCM)
PUL_pin = 22
DIR_pin = 27
relay = 11
enable = 4

GPIO.setup(relay, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PUL_pin, GPIO.OUT)
GPIO.setup(DIR_pin, GPIO.OUT)
GPIO.setup(enable, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(PUL_pin, GPIO.OUT, initial= GPIO.LOW)
GPIO.setup(DIR_pin, GPIO.OUT, initial= GPIO.LOW)


#open steering relay
GPIO.output(11, GPIO.HIGH)
print("sterring relay ON")
#open enable
GPIO.output(4, GPIO.HIGH)
print("enable ON")


#function to move the motor
def move_motor(direction, steps, delay_us):
	GPIO.output(DIR_pin, direction)
	for _ in range(steps):
		GPIO.output(PUL_pin, GPIO.HIGH)
		time.sleep(delay_us / 1_000_000.0)
		GPIO.output(PUL_pin, GPIO.LOW)
		time.sleep(delay_us / 1_000_000.0)
try:
	while True:
		print("moving forward")
		move_motor(GPIO.HIGH, 1000, 100)
		print("pause 1s")
		time.sleep(2)
		print("moving backward")
		move_motor(GPIO.LOW, 1000, 100)
		print("pause 2s")
		time.sleep(2)
		
except KeyboardInterrupt:
	GPIO.cleanup()

