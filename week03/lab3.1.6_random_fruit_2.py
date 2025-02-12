# lab3.1.6_random_fruit_2.py
# This program prints out a random fruit
# Uses a turple rather than a list
# Author Andrew Beatty
# Reproduced by Elaine Cazetta

import random

fruits = ('Apple', 'Orange', 'Banana', 'Pear')

# we want a random number between 0 and lenght-1
index = random.randint(0,len(fruits)-1)

fruit = fruits[index]
print("A Random Fruit:{}".format(fruit))
