import RPi.GPIO as GPIO
import time
import sys
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
x=sys.argv[1]
temp=3
usage=3
try:
	temp=GPIO.gpio_function(int(x))
except:
	temp=3
finally:
	usage=temp
	print usage
	