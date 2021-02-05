# Program to subtract one number from another.

# Input reads in a string so we need to convert in into an int so that we can perform mathematical operations.

x = int (input ("Enter first number: "))
y = int (input ("Enter second number: "))
answer = x - y

print ("{} minus {} is {} ".format(x, y, answer))