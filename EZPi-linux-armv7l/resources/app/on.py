import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
x = sys.argv[1]
y = sys.argv[2]
print(x)
print(y)
if int(y) == 1:
	GPIO.setup(int(x), GPIO.IN)

if int(y) == 2:
	GPIO.setup(int(x), GPIO.OUT)
	GPIO.output(int(x), False)

if int(y) == 3:
	GPIO.setup(int(x), GPIO.OUT)
	GPIO.output(int(x), True)


print('Done!')
