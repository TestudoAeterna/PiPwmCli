import sys
import RPi.GPIO as GPIO

pin = int(sys.argv[1])
duty = int(sys.argv[2])
freq = int(sys.argv[3])

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT)
pipwm = GPIO.PWM(pin,freq)
pipwm.start(duty)