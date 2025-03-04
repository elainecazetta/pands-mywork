# This program outputs whether or not today is a weekday.
#
# Author: Elaine Cazetta
#
# Sources: https://www.w3schools.com/python/python_datetime.asp ; chatgpt

import datetime # Imports the datetime module

today = datetime.datetime.today() # this bit assigns the current timestamp as 'today'
weekday = today.strftime("%A") # the 'strftime' formats date objects into strings, and "%A" transforms today's date into a weekday
weekend = ("Saturday", "Sunday") # I used a tupple to assign Saturday and Sunday as weekend

if weekday not in weekend: # I learned the 'not in' function from chatgpt. I was wrongly using "if weekday != weekend:" instead
    print("Yes, unfortunately today is a weekday.")
else:
    print("It is the weekend, yay!")


