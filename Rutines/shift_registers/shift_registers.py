#Author: Carlos Del Cid
#



#lets start by importing the necessary libraries
import numpy as np
import math as ma

#import functions form the main folder
import function_cafe as fc

#create a loop to keep testing the ports
i=0
while i==0:
    address_number = input("Enter the 4 digit address for the light:")
    red_strip = input("% of red  :")
    blue_strip = input("% of blue :")
    # send this data to a function and somehow get something back to program the shift registers
    fc.address_format(address_number)