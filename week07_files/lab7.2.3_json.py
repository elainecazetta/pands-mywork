# This function stores a simple Dict to a file 
# as JSON and tests it.
# Author: Andrew Beatty
#
# Reproduced by: Elaine Cazetta

import json
FILENAME="testdict.json"
sample= dict(name='andrew', age=99, grades=[1,34,55])

def writeDict(obj):
    with open(FILENAME, 'wt') as f:
        json.dump(obj,f)

#test the function
writeDict(sample)