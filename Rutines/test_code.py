import RPi.GPIO as GPIO
import time     as tm
import numpy    as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)

h=0
while h == 0:
     #turn on the pins for testing
     GPIO.output(17, GPIO.HIGH)
     GPIO.output(27, GPIO.HIGH)
     GPIO.output(22, GPIO.HIGH)
     
     question_ok = input("is everything ok")
     print(question_ok)
     if question_ok == 1:     
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        h=1
     else:
        print("crap, something is worng")
        h=0

w=0
while w==0:
    input_data = int(input("data in:"))
    clock_out =  int(input("clock out data:"))
    
    if input_data == 1:
        GPIO.output(17, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        print("11 was set to one")

    elif input_data == 0:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.HIGH)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        print("11 was set to zero")
    else: print("error errorooororororooror ")

    if clock_out == 1:
        GPIO.output(22, GPIO.HIGH)
        GPIO.output(22, GPIO.LOW)
        print("Clockout was set to one")
    else:
        GPIO.output(22, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        print("Clockout was set to zero")