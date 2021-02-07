# Takes in a float amount of dollars, and returns that absolute amount in cent.

# Author: Cormac Hennigan

# We need to get the absolute value of the float, then multiply by 100 and then round it to a whole number

numberInDollars = float(input("Please enter an amount: "))
numberInCents = round(abs(numberInDollars)*100)

print("That amount in cent is {}".format(numberInCents))