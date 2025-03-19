# bank.py
# This program should prompt the user and read in two money amounts (in cent)
# Add the two amounts
# Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
# Author Elaine Cazetta

# First attempt, 5th February 2025
# Source: Andrew Beatty lectures
 # amount1 = input("Enter amount1(in cent):")
 # amount2 = input("Enter amount2(in cent):")
 # print('The sum of these is €' + amount1 + amount2)

# Second attempt, 6th February 2025
# Help from source: https://www.w3schools.com/python/python_string_formatting.asp:
 # amount1 = input("Enter amount1(in cent):")
 # amount2 = input("Enter amount2(in cent):")
 # print(f"The sum of these is €" + {amount1+amount2:.2f})

# Third attempt, 7th February 2025:
 # amount1 = input("Enter amount1(in cent):")
 # amount2 = input("Enter amount2(in cent):")
 # total_cents = amount1 + amount2
 # total_euros = total_cents / 100
 # print(f"The sum of these is €" + {total_cents:.2f})

# After several attempts and error messages, I finally succeeded on February 8, 2025
# Help obtained from ChatGPT (I didn’t ask for the answer but for guidance on fixing errors)
# Learned that I should use the 'int' function before 'input' to convert the string into an integer, 
# since the values were being concatenated instead of summed.
# Learned how to use f-strings and that I must include quotes after the 'f' prefix. 
# This was the cause of the errors.

amount1 = int(input("Enter amount1(in cent):")) / 100
amount2 = int(input("Enter amount2(in cent):")) / 100
print(f"The sum of these is €{(amount1 + amount2):.2f}")