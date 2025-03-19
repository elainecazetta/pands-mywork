# This program checks if a file exists
#
# Author: Andrew Beatty
#
# Reproduced by: Elaine Cazetta

import os.path
FILENAME = "count.txt"
if not os.path.isfile(FILENAME):
    print ("File does not exist")
    #initialise file here
    


