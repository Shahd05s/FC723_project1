#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:18:54 2025

@author: shahdalharthy
"""




def find_GCD(a, b):
    #a function to find the greatest common divisor of 2 numbers using the Euclidean Algorithm.
    while b != 0 : # while loop Continue until the remainder (b) becomes  zero as the algrothim says .
        rem = a % b # Find the remainder equation 
        a=b # set a equal to the value of b 
        b= rem # set b equal to the remainder
    return a # Return the last non-zero value of (a) as the GCD
      


try: # using try-except to deal with error if the user inputed somthing that is not a positive integer 
# Get integer input from the user 
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Check if inputs are valid, positive
    if num1 >= 0 and num2 >= 0:
    # Calculate the GCD
        print(f"The GCD of {num1} and {num2} is: {find_GCD(num1, num2)}")
        
    else: # if the entered number was negative then asks user to a positive number 
        print(" Please enter positive integers only.")
        
except ValueError: #print an error message if the user input is invalid 
        print(" Invalid input. Please enter integers only.")
            


def lcm(a,b):
    return (a // find_GCD(a,b))* b





