# Gets the program to generate a random number between 0 and 100 to guess
# Author: Cormac Hennigan

import random

numberToGuess = 30

guess = random.randint(0, 100)
while guess != numberToGuess:
    if guess < numberToGuess:
        print("Too low")
        guess = random.randint(0, 100)
    else: # Can't be equal or too low so it must be too high
        print("Too high")
        guess = random.randint(0, 100)

print("Well done! Yes the number was {}".format(numberToGuess))