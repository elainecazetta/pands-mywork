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
#
# Answer:
#
# The input is limited by the first 10 characters, using the slicer function
account = input("Please enter an 10 digit account number: ") [:10]
# Funtion ' "X" * (len(account) - 4) ' was used to count the number 
# of the account's characters, minus 4, and replace it by Xs 
hidden_account = "X" * (len(account) - 4) + account[-4:]
print(hidden_account) # prints a number of Xs + the account's four last digits
#
# Extra Task - Answer:
# To handle any length, I would remove the slicer "[:10]"
# then if the account number has 4 or fewer digits, it'll show as is
# if it’s longer, the program will mask all but the last 4 digits