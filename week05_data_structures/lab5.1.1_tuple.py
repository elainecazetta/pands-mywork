# This program creates a tuple that stores the months of the year.
# From this tuple, a second tuple is created 
# with just the summer months (May, June, July),
# and it print out the summer months one at a time.
# Author: Andrew Beatty
# Reproduced by: Elaine Cazetta

months =("January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December"
)
summer = months[4:7]
for month in summer:
 print(month)