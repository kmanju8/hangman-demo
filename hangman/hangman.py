# hangman game logic
# answer is the correct answer user is trying to guess
# user_answer contains the progress the player has made in guessing
def hangman(answer):
    lives = 6
    user_answer = ["_"]*len(answer) # creates empty guessboard for user to start guessing letters in
    
    # keep asking user to guess letters till no more gaps
    while "_" in user_answer:
        print("\n\n"," ".join(user_answer))
        print("Lives remaining:", lives)
        user_guess = input("Please enter a letter: ")
        # check user has only entered one letter
        if len(user_guess) != 1:
            print("Please enter only one character.\n")
            continue
        
        # lose a life, as guessed letter not in answer
        if user_guess not in answer:
            lives = lives - 1
            if lives == 0:
                print("man is dead :\(")
                break

        # guess is in answer, so fill user_answer with guess wherever applicable
        for i in range(len(answer)):
            if user_guess==answer[i]:
                user_answer[i]=user_guess

    # if you got here by not dying, get congratulatory message   
    if lives>0:
        print("congratulations, you guessed the correct word:", answer)