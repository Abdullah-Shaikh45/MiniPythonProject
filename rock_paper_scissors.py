import random

option_list = ["rock", "paper", "scissors"]

while True:
    user = input(
        "Choose one option (rock, paper, scissors) or press 'q' to quit ").lower().strip()
    computer = random.choice(option_list)

    print(f"User chose: {user}")
    print(f"Computer chose: {computer}")

    if user == "q":
        break

    elif user == computer:
        print("It's a tie!")

    elif user == "rock" and computer == "scissors":
        print("user wins!")

    elif user == "scissors" and computer == "paper":
        print("user wins")

    elif user == "paper" and computer == "rock":
        print("user wins!")

    else:
        print("computer wins!")
