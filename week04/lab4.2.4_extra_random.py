# Extra task - lab 4.2: 
# 
# This program prompts the user to guess a number
# 
# and it automatically generates a random number 
# between 0 and 100 to guess
# Author: Elaine Cazetta

import random #source: https://www.programiz.com/python-programming/examples/random-number

numberToGuess = random.randint(0,100)

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
 if guess < numberToGuess:
   print("too low")
 else: # I know it cant be equal or too low, so it must be too high
   print("too high")
 guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)