# This program reads in a string and strips
# any leading or trailing spaces.
# It also converts all the letters to lower case.
# It then outputs the lengths of the original string
# and the normalised one
# Author: Andrew Beatty
# Reproduced by Elaine Cazetta

rawstring = input("please enter a string: ")
normalisedstring = rawstring.strip().lower()

lenghtofrawstring = len(rawstring)
lenghtofnormalised = len(normalisedstring)

print(f"That string normalised is: {normalisedstring}")
print(f"We reduced the input string from {lenghtofrawstring} to {lenghtofnormalised} characters")