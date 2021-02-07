# Gives the absolute value of a number

# Author: Cormac Hennigan

# In the question, the number is ambiguous but the output implies that we should be dealing
# with floats, so I am caseting the imput to a float.

number = float(input("Enter a number: "))
absoluteValue = abs(number)

print("The absolute value of {} is {}".format(number, absoluteValue))