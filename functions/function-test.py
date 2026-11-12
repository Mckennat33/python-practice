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


# ---- SOLUTION: handles 0 / negatives and letters ----
# To try it, comment out numberGuess() above and uncomment numberGuessSolution() at the bottom.

def getGuess():
    while True:
        try:
            return int(input('Guess the number 1 through 20 '))
        except ValueError:
            print('That is not a number, try again')


def numberGuessSolution():
    guessedNumber = getGuess()
    while guessedNumber != 20:
        if guessedNumber < 1:
            print('Too low, pick 1-20 ')
        elif guessedNumber < 5:
            print('Cold as ice')
        elif guessedNumber in range(5, 15):
            print('Getting warmer!')
        elif guessedNumber in range(15, 20):
            print('HOT, one more time!')
        else:
            print('Too high, pick 1-20 ')
        guessedNumber = getGuess()
    print("YOU DID IT")


# numberGuessSolution()
