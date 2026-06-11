#interactive word game
# we get a word that is not shown to user just the blank space in each letters of the word. and user gueses letters for specific number of times (attempts) . every right guess updates the black word with the position of the guessed letter in the word and every wrong guess reduces no of attempts until 0
#firstly, lets create a function to get the word from the list of words randomly. since we willbe using random module we import random

import random

def chosen_word():
    word_list = ['python', 'programming', 'language',
                 'visual', 'studio', 'great']
    return random.choice(word_list)

def word_status(word, guessed_letters):
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    return display

def word_guessing_game():

    attempts = 7
    word = chosen_word()
    guessed_letters = []

    print("Secret word:", word_status(word, guessed_letters))

    while attempts > 0:

        guessed_letter = input("Enter your guessed letter: ").lower()

        if len(guessed_letter) != 1 or not guessed_letter.isalpha():
            print("Please enter a single alphabet letter.")
            continue

        if guessed_letter in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guessed_letter)

        if guessed_letter not in word:
            attempts -= 1
            print(f"'{guessed_letter}' is not in the word.")
            print(f"Attempts remaining: {attempts}")

        current_status = word_status(word, guessed_letters)

        print("Secret word:", current_status)

        if "_" not in current_status:
            print("Congratulations! You won!")
            return

    print(f"You lost! The word was '{word}'")

word_guessing_game()