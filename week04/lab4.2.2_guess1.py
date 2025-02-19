# This program prompts the user to guess a number.
# It should keep prompting the user to guess the number 
# until the user gets the right on
# Author: Andrew Beatty
# Reproduced by: Elaine Cazetta

numberToGuess = 30

guess = int(input("Please guess the number:"))
while guess != numberToGuess:
 print ("Wrong")
 guess = int(input("Please guess again:"))

print ("Well done! Yes the number was ", numberToGuess)