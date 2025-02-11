# lab3.1.7_extra_question.py
# Program created to solve the following question:
# Why does this expression cause an error? How can you fix it? 
# message = 'I have eaten ' + 99 + ' burritos.'
# print (message)

# to fix the error: I used str() function to convert the number into a string
message = 'I have eaten ' + str(99) + ' burritos.' 
print (message)