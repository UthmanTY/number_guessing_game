import random
from utils import get_valid_number, score_calculator

EASY_MAX = 50
MEDIUM_MAX = 100
HARD_MAX = 200

EASY_ATTEMPTS = 10
MEDIUM_ATTEMPTS = 7
HARD_ATTEMPTS = 5

EASY_MULTIPLIER = 1
MEDIUM_MULTIPLIER = 2
HARD_MULTIPLIER = 3

def difficulty_selector():
    while True:
        try:
            option = int(input("Select difficulty:\n[1]Easy\n[2]Medium\n[3]Hard\n"))
            if option == 1:
                return EASY_MAX, EASY_ATTEMPTS, EASY_MULTIPLIER
            elif option == 2:
                return MEDIUM_MAX, MEDIUM_ATTEMPTS, MEDIUM_MULTIPLIER
            elif option == 3:
                return HARD_MAX, HARD_ATTEMPTS, HARD_MULTIPLIER
            else:
                print("Input must be between 1-3")
        except ValueError:
            print("Input must be an int")

while True:
    max_number, max_attempts, difficulty_multiplier = difficulty_selector()

    secret_number = random.randint(1, max_number)

    attempts_used = 0
    won = False

    while attempts_used < max_attempts and won is not True:
        attempts_used += 1
        print(f"Attempt {attempts_used}/{max_attempts} - Enter your guess: ")
        guess = get_valid_number(max_number)

        if guess == secret_number:
            won = True
            print("Correct")
        elif guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
    if won:
        print(f"🎉 Correct! You got it in {attempts_used} attempts!")
        score = score_calculator(max_attempts, attempts_used, difficulty_multiplier)
        print(f"Your score: {score} points.")
    else:
        print(f"You ran out of attempts! The secret number is {secret_number}")

    while True:
        play_again = input("Play again? (y/n): ").lower()

        if play_again not in ("y", "n"):
            print("Invalid input! Please enter (y/n).")
            continue
        else:
            break
           
    if play_again == "n":
        break
