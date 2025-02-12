# Weekly Task 03
#
# Task: Write a python program called accounts.py that reads in 
# a 10 character account number and outputs the account number 
# with only the last 4 digits showing (and the first 6 digits replaced with Xs)
#
# Extra:
# Modify the program to deal with account numbers of any length 
# (yes that is a vague requirement, comment your assumptions)
#
# Author Elaine Cazetta
# Source: https://www.w3schools.com/python/python_strings_slicing.asp and ChatGPT (function 'len')

# Answer:

# The input is limited by 10 characters, using the slicer function
account = input("Please enter an 10 digit account number: ")[:10]
# Funtion len() and "-4" were used to count the number of the account's characters
# and subtract it by 4 = the four last digits 
# the result, 6, is the number of characters that are going to be replaced by Xs 
hidden_account = "X" * (len(account) - 4) + account[6:]
print(hidden_account) # prints 6 times the character "X" + the account's four last digits

# Extra: 
