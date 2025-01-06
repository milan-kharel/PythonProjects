import random
from words import word_list

def get_word():
    word = random.choice(word_list)
    return word.upper()

def play(word):

    word_completion = "_"*len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:

        guess = input("please guess a lettr:").upper()

        if len(guess) == 1 and guess.isalpha(): #check if input is a single letter
            if guess in guessed_letters:
                print("U already guessed the letter",guess)
            elif guess not in word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("good job", guess, "is correct word")
                guessed_letters.append(guess)

                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print ("U already guessed it",guess)
            elif guess != word:
                print(guess, "is not in the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("congrats, u guessed the word, U Win!")
    else:
        print("Boooo! U ran out of tries. The word was " +word+"Maybe Next Time!")
                    



def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                  # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                     --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


