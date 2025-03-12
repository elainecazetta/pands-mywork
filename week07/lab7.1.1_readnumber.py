# This program has a function that reads in a number 
# from a file that already exists (count.txt), and 
# tests it by calling the function and outputting the number.
# Author: Andrew Beatty
#
# Reproduced by: Elaine Cazetta

FILENAME = "count.txt"
def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number
# test it
num = readNumber()
print (num)