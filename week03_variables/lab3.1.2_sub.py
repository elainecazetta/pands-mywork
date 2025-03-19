# lab3.1.2_sub.py
# This program was created to subtract a number from another
# input reads in a string so we need to convert it into an int
# so we can perform mathematical operations
# Author Andrew Beatty
# Reproduced by Elaine Cazetta

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
answer= x-y
print("{} minus {} is {} ".format(x, y, answer))