# Prompts the user to guess a number, keeps prompting the user to guess the number until the user gets the right one

# Auothor: Cormac Hennigan

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    print("Wrong")
    guess = int(input("Please guess again: "))

print("Well done! Yes the number was {}".format(numberToGuess))