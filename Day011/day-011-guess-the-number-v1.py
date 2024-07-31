import random

def guess_the_number():
    print("Welcome to 'Guess the Number'!")
    select_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if select_difficulty == "easy":
        guess_count = 10
        print("You have 10 attempts remaining to guess the number.")
    elif select_difficulty == "hard":
        guess_count = 5
        print("You have 5 attempts remaining to guess the number.")
    else:
        print("Invalid input. Please enter 'easy' or 'hard'.")
        return

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
            print(f"Sorry, you ran out of guesses. The answer was {secret_number}.")

    while True:
        play_again = input("Enter 'E' to exit or 'C' to play again: ").upper()
        if play_again == 'C':
            guess_the_number()
            break
        elif play_again == 'E':
            exit()
        else:
            print("Invalid input. Please enter 'E' to exit or 'C' to play again.")

guess_the_number()
