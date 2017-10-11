#PiBot test1

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Motor A 
MotorAin1 = 
MotorAin2 =
MotorAen1 =
MotorAen2 =

#Set Output
GPIO.setup(MotorAin1,GPIO.OUT)
GPIO.setup(MotorAin2,GPIO.OUT)
GPIO.setup(MotorAen1,GPIO.OUT)
GPIO.setup(MotorAen2,GPIO.OUT)

GPIO.output(MotorAin1,GPIO.HIGH)
GPIO.output(MotorAin2,GPIO.LOW)
GPIO.output(MotorAen1,GPIO.HIGH)
GPIO.output(MotorAen2,GPIO.HIGH)
sleep(3)