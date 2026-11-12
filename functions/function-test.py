import random

randomNumber = random.randint(1, 20)


def numberGuess():
    guessedNumber = int(input('Guess the number 1 through 20 '))
    while guessedNumber != 20:
        if guessedNumber < 5:
            print('Cold as ice', "Give another guess: Second ")
        elif guessedNumber in range(5, 15):
            print('Getting warmer! Try another number: Third')
        elif guessedNumber in range(15, 20):
            print('HOT, One more time!: Fourth')
        else: 
            print('Too high, pick 1-20 ')
        guessedNumber = int(input('Guess the number 1 through 20 '))
    print("YOU DID IT")
numberGuess()

