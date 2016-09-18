import RPi.GPIO as GPIO
import time

input_port = 8
output_port = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(input_port, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(output_port, GPIO.OUT)

while True:
	time.sleep(.1)
	if (GPIO.input(input_port) == False):
		GPIO.output(output_port, True)
		print("Button down.")
	else:
		GPIO.output(output_port, False)