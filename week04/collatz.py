# Weekly Task 4
#
# Task: Write a program that asks the user to input any positive
# integer and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, 
# if it is even, divide it by two, but if it is odd, 
# multiply it by three and add one. 
# Have the program end if the current value is one.
# 
# Author: Elaine Cazetta

num = int(input("Please enter a positive integer: "))
while num != 1:
    print(num, end=" ")  # Print sequence number with space (on the same line)
    if num % 2 == 0: # If even, divide by 2
        num = num // 2
    else:
        num = (num * 3) + 1 # If odd, multiply by 3 and add 1
print(num)  # Print the final number (1)    
    