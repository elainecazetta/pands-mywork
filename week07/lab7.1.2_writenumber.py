# This program has a function that takes in a number and 
# overwrites a file with that number (count.txt)
#
# Author: Andrew Beatty
#
# Reproduced by: Elaine Cazetta

FILENAME = "count.txt"
def writeNumber(number):
 with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
    f.write(str(number))

# test it
writeNumber(3)
