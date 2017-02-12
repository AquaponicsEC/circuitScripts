#lets start by importing the necessary libraries
import numpy as np

def address_format(address):
    #we start by checking the length of the address
    address_length = len(address)
    #now we create an array capable of handling the length
    length_array  = np.zeros(address_length)
    values_array  = np.zeros(address_length)
    sum_of_values = 0
    #create a loop to calculate the value in decimal
    i = 0
    while i < address_length:
        values_array[i] = int(address[i])
        length_array[i] = ((values_array[i])*(2**i))
        i=i+1

    #create a new loop to add the results into a single number
    i=0
    while i < address_length:
        sum_of_values = sum_of_values + length_array[i]
        i=i+1
    print(sum_of_values)
    #create a new loop to create the encoded number needed
    i = 0
    size_total = address_length**2
    shift_register_array = np.zeros(size_total)
    shift_register_array[sum_of_values] = 1

    print("whole size", shift_register_array)
    return 0
