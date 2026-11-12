import random

randomNumber = random.randint(1, 20)


def numberGuess():
    guessedNumber = int(input('Guess the number 1 through 20 '))
    while guessedNumber != 20:
        guessedNumber = int(input("Try again "))
        if guessedNumber < 5:
            print('Cold as ice')
            guessedNumber = int(input("One more time "))
        elif guessedNumber > 10:
            print('Getting warmer')
        break


numberGuess()
