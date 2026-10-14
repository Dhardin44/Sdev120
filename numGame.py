import random
number = random.randint(1, 100)
attempts = 0

print("Guess the number\n"
      "*Hint* It's between 1 and 100\n")

# Computer picks a random number
while True:
    try:
        user_input = int(input("Enter a number: "))

        if user_input == number:
            print("You guessed correctly :) Congratulations!!")
            break

        elif user_input > number:
            print("Sorry, your guess is too high :( try again!")
        else:
            print("Oh no, your guess is too low :( try again!")


    except ValueError:
        print("Hmm, that's not a number, please enter a digit")
