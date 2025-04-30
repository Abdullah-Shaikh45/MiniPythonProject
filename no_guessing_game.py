import random


def guess_the_number_game():
    random_number = random.randint(1, 10)
    attempts = 7

    while attempts > 0:
        user_input = input(
            f"Guess the number (1-10) or press 'q' to quit. Attempts left: {attempts}: ")

        if user_input.lower() == 'q':
            print("Game over. Thanks for playing!")
            break

        if not user_input.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        user_guess = int(user_input)

        if user_guess == random_number:
            print("Correct! You guessed the number.")
            break
        elif user_guess < random_number:
            print("Too low!")
        else:
            print("Too high!")

        attempts -= 1

    else:
        print(f"Out of attempts! The correct number was {random_number}.")


guess_the_number_game()
