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
    return a # Return the last non-zero value of (a)) as the GCD
      
a=18
b=9

#apply a, b to the function and print the result (gcd) 
gcd = find_GCD(a, b)
print(f"The GCD of {a} and {b} is {gcd}.")


