import random
import time

# Initial Steps to invite in the game:
def Starting_Game ():
    global name
    print("""
        █ █ ███ █  █ ███    █ █ ███ █  █
        █▄█ █▄█ ██▄█ █╬▄    █V█ █▄█ ██▄█
        █ █ █ █ █ ██ █▄█    █ █ █ █ █ ██""")
    time.sleep(2)

    print()
    print()
    print("          You have made a GREAT SIN.")
    print()
    time.sleep(3)
    print("     And for that you shall be punish!!!")
    print()
    time.sleep(3)
    print( "But you have been given a chance to redeem yourself.")
    print()
    time.sleep(3)
    print("  You must play this HANG MAN in order to live!!!")
    print()
    time.sleep(3)
    print("""
The rules are simple. A hidden random word will be given to you.
            All you have to do is guess the word.
            You can only offord to make 5 Mistakes.
                    prepare yourself.
                        cause
                   GUESS WRONG AND""")
    print()
    time.sleep(5)
    print("""\
                █ █ ███ █ █
                █▄█ █ █ █ █
                 █  █▄█ ███""")
    time.sleep(2)
    print()
    print("""\
              ██ █ █ ███ █  █
              █▄ █▄█ █▄█ █  █
              ▄█ █ █ █ █ ██ ██""")
    time.sleep(2)
    print()
    print("""\
                  ██▄ ██
                  █▄█ █▄
                  █▄█ █▄""")
    time.sleep(2)
    print()
    print("""\
              █ █ ███ █  █ ████
              █▄█ █▄█ ██▄█ █ ▄▄
              █ █ █ █ █ ██ █▄▄█""")
    print()
    time.sleep(2)
    print("You only have 1 Life, make it count")
    time.sleep(2)
    new_player()

# The parameters we require to execute the game:

def new_player():
    global name
    name = input("Identify yourself: ")
    print()
    print( " Best of Luck! " + name + "!")
    time.sleep(2)
    print("The game is about to start!")
    print()
    time.sleep(2)
    print("Let's have some HANGING!")
    print()
    time.sleep(3)
    main()

def main():
    
    # global name
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game
    global game_over
    global words
    global word

    words_to_guess = ["republic", "bankrupt","beach","film","promise","keyboard","basket","flying","rhyme","mousepad"
                     ,"plants", "myths"]
    word = random.choice(words_to_guess)
    words = word
    length = len(words)
    count = 0
    display = "_" * length
    already_guessed = []
    play_game = ""
    game_over = word
    hangman()

# A loop to re-execute the game when the first round ends:
def end_game():
    global end_game
    end_game = words
    print("The word was:",game_over)
    play_loop()


def you_died():
    global play_game
    global play_game
    print("Wrong guess!!!")
    print()
    print("The word was:",game_over)
    time.sleep(2)
    print("See you in the other side! " + (name) + "." )
    time.sleep(2)
    print()
    print("You are hanged!!!\n")
    time.sleep(5)
    print("Next Player.")
    while play_game not in ["y", "n" , "q"]:
        play_game = input("Do You want to start right away press 'y' or start a whole new game press 'n' or press 'q' to quit? \n")

        if play_game == "y" :
            new_player()                      #     IMPORTANT

        elif play_game == "n":
            print("Press ENTER to start a New Hanging")
            input()
            time.sleep(1)
            Starting_Game()
        elif play_game == "q":
            exit()

def play_loop():
    global play_game
    global name
    # play_game = input("Do You want to play again? y = yes, n = no \n")
    while play_game not in ["y", "n"]:
        play_game = input("Do You want to play again? y = yes, n = no \n")

    if play_game == "y" :
        main()

    elif play_game == "n":
        print("You are free to go! But I have the a feeling that we will see you again!")
        time.sleep(2)
        print("Until next time!!! " + (name) )
        time.sleep(1)
        print("Press ENTER to start a New Hanging")
        input()
        time.sleep(1)
        Starting_Game()

# Initializing all the conditions required for the game:

def hangman():
    global count
    global display
    global words
    global already_guessed
    global play_game
    global word
    global length
    limit = 5
    print("you are given a", (length), "letter word")
    guess = input("This is the Hangman Word: " + display + " Enter your guess: \n")
    guess = guess.strip()

    # if word == '_' * length:
    #     print("Congrats! You have guessed the word correctly!")
    #     play_loop()
    
    if guess == word:
        print("Congrats! You have guessed the word correctly!")
        time.sleep(2)       
        play_loop()

    if len(guess.strip()) == 0:
        print("Invalid Input, Try a letter\n")
        hangman()
    # elif len(guess.strip()) == word and guess == word:
    #     time.sleep(1)
    #     print("Congrats! You have guessed the word correctly!")        
    #     play_loop()

    elif guess in words:
        already_guessed.extend([guess]) 
        index = words.find(guess)
        words = words[:index] + "_" + words[index + 1:]
        display = display[:index] + guess + display[index + 1:]
        print(display + "\n")
    
    

    elif guess in already_guessed:
        print("Try another letter.\n")
 
    else:
        count += 1

        if count == 1:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |      \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 2:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O\n"
                  "  |    / \ \n"
                  "  |      \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 3:
           time.sleep(1)
           print("   _____ \n"
                 "  |     | \n"
                 "  |     |\n"
                 "  |     O \n"
                 "  |    /|\ \n"
                 "  |      \n"
                 "  |      \n"
                 "__|__\n")
           print("Wrong guess. " + str(limit - count) + " guesses remaining\n")

        elif count == 4:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    /  \n"
                  "  |      \n"
                  "__|__\n")
            print("Wrong guess. " + str(limit - count) + " last guess remaining\n")

        elif count == 5:
            time.sleep(1)
            print("   _____ \n"
                  "  |     | \n"
                  "  |     |\n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |        \n"
                  "__|__\n")
            
            you_died()

    if words == '_' * length:
        print("Congrats! You have guessed the word correctly!")
        play_loop()


    if len(guess.strip()) == word and guess == word:
        time.sleep(1)
        print("Congrats! You have guessed the word correctly!")        
        play_loop()

    if count != limit:
        hangman()

Starting_Game()

hangman()