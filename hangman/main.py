import random
from hangman import *            #import everything (*) from hangman.py, so we can call hangman(answer) here

# selection of possible answers. Feel free to change
words = ("python", "jumble", "easy", "difficult", "answer",  "xylophone")

# main retry loop. Will keep repeating.
while True:
    print("Starting new game of hangman")

    # calling the function to start a game of hangman.
    # We choose what the correct answer will be here, and pas it into the hangman function
    hangman(random.choice(words))
    
    again = input("Would you like to play again (Y/n)?: ")
    if again == "n" :
        # if user selects no, breaks from infinite loop, quitting game 
        break