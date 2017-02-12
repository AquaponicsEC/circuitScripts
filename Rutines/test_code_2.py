import RPi.GPIO as GPIO
import time     as tm
import numpy    as np

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
'''
h = 0
while h == 0:
    # turn on the pins for testing
    GPIO.output(17, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)
    GPIO.output(22, GPIO.HIGH)

    question_ok = input("is everything ok")
    print(question_ok)
    if question_ok == 1:
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        GPIO.output(22, GPIO.LOW)
        h = 1
    else:
        print("crap, something is worng")
        h = 0
'''
w = 0
while w == 0:
    input_data = int(input("data in:"))
    #clock_out = int(input("clock out data:"))
    data0=[0,0,0,0,0,0,0,0]
    data25 = [0,1,0,0,0,0,0,0]
    data50 = [0,0,1,0,0,0,0,0]
    data75 = [0,0,0,1,0,0,0,0]
    data100 = [0,0,0,0,1,0,0,0]
    if input_data == 0:
        a = 0
        while a < 8:
            v = data0[a]
            if v==0:
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                a=a+1
                print("11 was set to one")
            elif v==1:
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                a=a+1
                print("11 was set to zero")
    elif input_data == 25:
        a = 0
        while a < 8:
            v = data25[a]
            if v==0:
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                a=a+1
                print("11 was set to one")
            elif v==1:
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                a=a+1
                print("11 was set to zero")
    elif input_data == 50:
        b = 0
        while b < 8:
            v2 = data50[b]
            if v2 == 0:
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                b=b+1
                print("11 was set to one")
            elif v2 == 1:
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                b = b + 1
                print("11 was set to zero")
    elif input_data == 75:
        c = 0
        while c < 8:
            v3 = data75[c]
            if v3 == 0:
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                c = c + 1
                print("11 was set to one")
            elif v3 == 1:
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                c = c + 1
                print("11 was set to zero")
    elif input_data == 100:
        d = 0
        while d < 8:
            v4 = data100[d]
            if v4 == 0:
                GPIO.output(17, GPIO.LOW)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                d = d + 1
                print("11 was set to one")
            elif v4 == 1:
                GPIO.output(17, GPIO.HIGH)
                GPIO.output(27, GPIO.HIGH)
                GPIO.output(27, GPIO.LOW)
                GPIO.output(17, GPIO.LOW)
                GPIO.output(22, GPIO.HIGH)
                GPIO.output(22, GPIO.LOW)
                d = d + 1
                print("11 was set to zero")



