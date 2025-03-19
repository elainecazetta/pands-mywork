# This program prompts the user to guess a number.
# It should keep prompting the user to guess the number 
# until the user gets the right on
# The program tells the user if their guess is too high or too low
# Author: Andrew Beatty
# Reproduced by: Elaine Cazetta

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
 if guess < numberToGuess:
   print("too low")
 else: # I know it cant be equal or too low, so it must be too high
   print("too high")
 guess = int(input("Please guess again:"))

print("Well done! Yes the number was ", numberToGuess)
