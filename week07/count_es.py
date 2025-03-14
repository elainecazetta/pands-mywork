# Author: Elaine Cazetta
# Source: w3 Schools, AI models
# Assuming that the required txt file is in the same directory:

# import sys module to access the Command Line arguments
import sys

FILENAME = sys.argv[1]  # Get the filename from the command line 

# Leaned from an AI model about the "try" and "except" functions.
# Try and Except are similar to "IFERROR" in MS Excel
# and are used to handle errors, rather than crashing the
# program and throwing an error in case something goes wrong.

try:
# Open the file and read the content
    with open(FILENAME, "r") as f:
        content = f.read()

# Count lowercase and uppercase 'e'
    count_e = content.lower().count("e")

# Except was used here to handle FileNotFoundError and Exception errors   
except FileNotFoundError:
    print(f"Error: The file '{FILENAME}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")

print(count_e)








