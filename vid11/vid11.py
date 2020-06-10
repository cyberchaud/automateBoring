#  Number Guessing game

import random

playername = input('Hello, what is your name?')
print('Well {}, I am thinking of a number between 1 and 20.'.format(playername))
randnum = random.randint(1, 20)
guessnum = 0

for i in range(0, 7):
    guessnum = int(input('Take a guess'))

    if guessnum < randnum:
        print("Your guess was too low.")
    elif guessnum > randnum:
        print("Your guess was too high.")
    else:
        break
    i =+ 1

if guessnum == randnum:
    print('Good job {}! You guessed the correct number.'.format(playername))
else:
    print('Nope.  My number was {}.'.format(randnum))

