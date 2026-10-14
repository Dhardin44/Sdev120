import random

words = ["python", "java", "kotlin", "javascript"]
word = random.choice(words)
letters_guessed = []
attempts_remaining = 6
first_guess = True

print("Let's play Hangman!\n")

while attempts_remaining > 0:
    print("Guess a letter: ")
    word_display = ""

    for letter in word:
        if letter in letters_guessed:
            word_display += letter + " "

        else:
            word_display += "_ "

    print("Word:", word_display)
    print("Attempts remaining:", attempts_remaining)

    if "_" not in word_display:
        print("You guessed the word correctly :) Congratulations!")
        break

    if first_guess:
        guess = input("Guess a letter: ").lower()
        first_guess = False

    else:
        guess = input("Guess again: ").lower()

    if guess in letters_guessed:
        print("You already guessed that letter, try again!\n")

    else:
        letters_guessed.append(guess)

        if guess in word:
            print("Correct! That letter is in the word :)\n")
        else:
            attempts_remaining -= 1
            print("Sorry, that letter is not in the word :(\n")

if attempts_remaining == 0:
    print("Oh no, you ran out of attempts :(")
    print("The word was:", word)