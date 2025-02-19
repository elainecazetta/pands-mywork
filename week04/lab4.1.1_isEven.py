# This program asks the user to enter in a number, and it
# tell the user if the number is even or odd
# Author Andrew Beatty
#
# Reproduced by Elaine Cazetta

number = int(input("enter an integer: "))
if(number % 2) == 0:
 print(f"{number} is an even number")
else:
 print(f"{number} is an odd number")