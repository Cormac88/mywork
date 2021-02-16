# This program generates 10 random numbers, prints them out, then prints out the top 3

# I will use a list to stor and manipulate the numbers

import random

# Programming the general case

howMany = 10
topHowMany = 3
rangeFrom = 0
rangeTo = 100

numbers = []

for i in range (0, 10):
    numbers.append (random.randint(rangeFrom, rangeTo))
print ("Here are {} random numbers:\t {}".format(howMany, numbers))

# Now I split and sort the list

topOnes = numbers.copy ()
topOnes.sort (reverse=True)
print ("The top {} are \t\t {}".format(topHowMany, topOnes[0:topHowMany]))