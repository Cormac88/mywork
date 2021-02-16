# Asks the user to enter in a number and tells the user if the number is even or odd.

# Author: Cormac Hennigan

number = int(input("Enter an integer: "))

if (number % 2) == 0:
    print("{} is an even number".format(number))

else:
    print("{} is an odd number".format(number))