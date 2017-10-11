#PiBot

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#Motor A 
MotorAin1 = 11
MotorAin2 = 12
MotorAen1 = 13
MotorAen2 = 15

#Motor B
MotorBin1 = 35
MotorBin2 = 36
MotorBen1 = 37
MotorBen2 = 38

#Set Output
GPIO.setup(MotorAin1,GPIO.OUT)
GPIO.setup(MotorAin2,GPIO.OUT)
GPIO.setup(MotorAen1,GPIO.OUT)
GPIO.setup(MotorAen2,GPIO.OUT)
GPIO.setup(MotorBin1,GPIO.OUT)
GPIO.setup(MotorBin2,GPIO.OUT)
GPIO.setup(MotorBen1,GPIO.OUT)
GPIO.setup(MotorBen2,GPIO.OUT)

def front():
		GPIO.output(MotorAin1,GPIO.HIGH)
		GPIO.output(MotorAin2,GPIO.LOW)
		GPIO.output(MotorAen1,GPIO.HIGH)
		GPIO.output(MotorAen2,GPIO.HIGH)
		sleep(3)
		
def back():
		GPIO.output(MotorAin1,GPIO.LOW)
		GPIO.output(MotorAin2,GPIO.HIGH)
		GPIO.output(MotorAen1,GPIO.HIGH)
		GPIO.output(MotorAen2,GPIO.HIGH)
		sleep(3)
		
def right():
		GPIO.output(MotorBin1,GPIO.LOW)
		GPIO.output(MotorBin2,GPIO.HIGH)
		GPIO.output(MotorBen1,GPIO.HIGH)
		GPIO.output(MotorBen2,GPIO.HIGH)
		sleep(3)
		
def left():
		GPIO.output(MotorBin1,GPIO.HIGH)
		GPIO.output(MotorBin2,GPIO.LOW)
		GPIO.output(MotorBen1,GPIO.HIGH)
		GPIO.output(MotorBen2,GPIO.HIGH)
		sleep(3)
		
def stop():
		GPIO.output(MotorAin1,GPIO.LOW)
		GPIO.output(MotorAin2,GPIO.LOW)
		GPIO.output(MotorAen1,GPIO.LOW)
		GPIO.output(MotorAen2,GPIO.LOW)
		
