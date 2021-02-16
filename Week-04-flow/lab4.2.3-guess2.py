# Prompts the user to guess a number, keeps prompting the user to guess the number until the user gets the right one 
# and also tells the user whether their guess is too high or too low

# Author: Cormac Hennigan

import random

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
        guess = int(input("Please guess again: "))
    else: # Can't be equal or too low so it must be too high
        print("Too high")
        guess = int(input("Please guess again: "))

print("Well done! Yes the number was {}".format(numberToGuess))