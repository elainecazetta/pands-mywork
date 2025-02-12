# This program takes in a float amount of dollars and returns that absolute amount in cent
# Author Elaine Cazetta

# Task:
# I am writing an application, at the moment, in it I take an input of an amount
# in the form -9.44 (9 dollars and 44 cent), the issue there may or may not be a
# minus sign, and the bank takes in the amount in cent, (944). Write a program
# called convert.py that takes in a float amount of dollars and returns that
# absolute amount in cent.

# Solution:

import math

# the input will accept a float number
num_float = float(input("Please enter an amount: ")) 
# here the float number is converted in an absolute integer and it's multiplied by 100
num_abs = abs(int((num_float) * 100))
# output
print(f"That amount in cent is: {num_abs}")