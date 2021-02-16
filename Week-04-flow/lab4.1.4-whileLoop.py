# Asks the user to enter in a number, and the program will tell the user if the number is even or odd. It also will keep prompting the user to guess the number until the user guesses -1
# It also will keep prompting the user to guess the number until the user guesses -1

# Author: Cormac Hennigan

number = int(input("Please guess an integer: "))
numberToGuess = -1

while number != -1:
    if (number % 2) == 0:
        print("{} is an even number".format(number))
    else:
        print("{} is an odd number".format(number))
    number = int(input("Please guess again: "))

print("Well done! Yes the number was {}".format(numberToGuess))