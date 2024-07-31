# Guess the number

import random

print("Welcome to 'Guess the Number'!")
select_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if select_difficulty == "easy":
    print("You have 10 attempts remaining to guess the number.")
elif select_difficulty == "hard":
    print("You have 5 attempts remaining to guess the number.")
else:
    print("Invalid input. Please enter 'easy' or 'hard'.")
    exit()

guess_count = 0
if select_difficulty == "easy":
    guess_count = 10
else:
    guess_count = 5
secret_number = random.randint(1, 100)
while guess_count > 0:
    guess = int(input("Make a guess: "))
    if guess < secret_number:
        print("Too low.")
    elif guess > secret_number:
        print("Too high.")
    else:
        print(f"You got it! The answer was {secret_number}.")
        break
    guess_count -= 1
    if guess_count > 0:
        print(f"You have {guess_count} attempts remaining to guess the number.")
    else:
        print("You've run out of guesses, you lose.")
