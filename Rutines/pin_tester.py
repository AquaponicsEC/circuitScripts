#Author: Carlos Del Cid
#SN#   : A00-PT01-G1
#------------------------------------
#we start by importing the libraies we need
import RPi.GPIO as GPIO
import time     as tm
import numpy    as np

#ask erlin what this line does
GPIO.setmode(GPIO.BCM)#Erlin is making shit up
#Settup warnings if needed
GPIO.setwarnings(False)#True)#<--change to False if you want to hide warnings

#lets create a function to activate the pin needed
def turnon(a):
    GPIO.setup(a, GPIO.OUT)
    GPIO.output(a, GPIO.HIGH)
    #tell the user whats going on
    print("Pin",a,": has been set to high (5V) ")

def turnoff():
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(27, GPIO.LOW)
    GPIO.setup(22, GPIO.OUT)
    GPIO.output(22, GPIO.LOW)

    print("All done mate")
#set a loop for testing
i=0
while i == 0:
    question_about_mode = input("Do you want to run the test manually? (y=1/n=0)")
    #if the user wants to run an auto test
    if question_about_mode == 0:
        j=0
        a=1
        #Tell the user which pin we are using
        while j == 0:
            if a == 1 or a == 17:
                print("Pin",a,": 3.3V output")
            elif a == 2 or a == 4:
                print("Pin 2: 5.0V output")
            elif a == 3:
                print("Pin 3: SDA")
            elif a == 5:
                print("Pin 5: SCL")
            elif a == 6 or a == 14 or a == 20 or a == 25 or a == 30 or a == 34 or a == 39:
                print("Pin",a," : 0V GND")
            elif a == 7:
                print("Pin 7: GPIO 4 (?)")
            elif a == 8:
                print("Pin 8: TXD UART")
            elif a == 9:
                print("Pin 9: 0V GND")
            elif a == 10:
                print("Pin 10: RXD UART")
            elif a == 11:
                #set b equal to the GPIO value
                b = 17
                #send b to the fuction to activate the pin
                turnon(b)
            elif a== 13:
                #set b equal to the GPIO value
                b = 27
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 15:
                #set b equal to the GPIO value
                b = 22
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 16:
                #set b equal to the GPIO value
                b = 23
                #send b to the fuction to activate the pin
            elif a == 18:
                #set b equal to the GPIO value
                b = 24
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 22:
                #set b equal to the GPIO value
                b = 25
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 29:
                #set b equal to the GPIO value
                b = 5
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 31:
                # set b equal to the GPIO value
                b = 6
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 32:
                # set b equal to the GPIO value
                b = 12
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 33:
                #set b equal to the GPIO value
                b = 13
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 36:
                #set b equal to the GPIO value
                b = 16
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 37:
                #set b equal to the GPIO value
                b = 26
                #send b to the fuction to activate the pin
                turnon(b)
            elif a == 12:
                print("Pin 12: CLK PCM")
            elif a == 19:
                print("Pin 19: MOSI SPI")
            elif a == 21:
                print("Pin 21: MISO SPI")
            elif a == 23:
                print("Pin 23: SCLK SPI")
            elif a == 24:
                print("Pin 24: CEO SPI")
            elif a == 26:
                print("Pin 26: CE1 SPI")
            elif a == 27:
                print("Pin 27: ID SD")
            elif a == 28:
                print("Pin 28: ID SC")
            elif a == 35:
                print("Pin 35: FS PCM")
            elif a == 38:
                print("Pin 38: DIN PCM")
            elif a == 40:
                print("Pin 40: DOUT PCM")
	    elif a == 101:
		turnoff()
            else:
                print("Error 001: Pin ", a, " is outside the boundaries.")
                turnoff()
                j = 1
            a = a+1
    else:
        d=0
        while d == 0:
            pin_activation_question = input("Which pin do you want to activate?")
            a = pin_activation_question
            if a == 1 or a == 17:
                print("Pin", a, ": 3.3V output")
            elif a == 2 or a == 4:
                print("Pin 2: 5.0V output")
            elif a == 3:
                print("Pin 3: SDA")
            elif a == 5:
                print("Pin 5: SCL")
            elif a == 6 or a == 14 or a == 20 or a == 25 or a == 30 or a == 34 or a == 39:
                print("Pin", a, " : 0V GND")
            elif a == 7:
                print("Pin 7: GPIO 4 (?)")
            elif a == 8:
                print("Pin 8: TXD UART")
            elif a == 9:
                print("Pin 9: 0V GND")
            elif a == 10:
                print("Pin 10: RXD UART")
            elif a == 11:
                # set b equal to the GPIO value
                b = 17
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 13:
                # set b equal to the GPIO value
                b = 27
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 15:
                # set b equal to the GPIO value
                b = 22
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 16:
                # set b equal to the GPIO value
                b = 23
                # send b to the fuction to activate the pin
            elif a == 18:
                # set b equal to the GPIO value
                b = 24
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 22:
                # set b equal to the GPIO value
                b = 25
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 29:
                # set b equal to the GPIO value
                b = 5
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 31:
                # set b equal to the GPIO value
                b = 6
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 32:
                # set b equal to the GPIO value
                b = 12
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 33:
                # set b equal to the GPIO value
                b = 13
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 36:
                # set b equal to the GPIO value
                b = 16
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 37:
                # set b equal to the GPIO value
                b = 26
                # send b to the fuction to activate the pin
                turnon(b)
            elif a == 12:
                print("Pin 12: CLK PCM")
            elif a == 19:
                print("Pin 19: MOSI SPI")
            elif a == 21:
                print("Pin 21: MISO SPI")
            elif a == 23:
                print("Pin 23: SCLK SPI")
            elif a == 24:
                print("Pin 24: CEO SPI")
            elif a == 26:
                print("Pin 26: CE1 SPI")
            elif a == 27:
                print("Pin 27: ID SD")
            elif a == 28:
                print("Pin 28: ID SC")
            elif a == 35:
                print("Pin 35: FS PCM")
            elif a == 38:
                print("Pin 38: DIN PCM")
            elif a == 40:
                print("Pin 40: DOUT PCM")
            elif a == 101:
		turnoff()
	    else:
                print("Error 001: Pin ", a, " is outside the boundaries.")
                turnoff()
                j = 1
