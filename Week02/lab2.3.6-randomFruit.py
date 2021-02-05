# This program prints out a random fruit
# Author: Cormac Hennigan

import random

# We want a random number between 0 and length-1
fruits = ['Apple', 'Orange', 'Banana', 'Pear']
index = random.randint(0, len(fruits)-1)

fruit = fruits[index]

print ("Here is a random fruit: {} ".format(fruit))