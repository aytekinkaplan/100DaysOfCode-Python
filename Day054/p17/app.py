import random


def generate_random_number():
    return random.randint(1, 100)


def guess_number():
    number = generate_random_number()
    guess = int(input("Guess the number: "))
    guess_count = 0
    while guess_count < 5 and guess != number:
        guess_count += 1
        if guess < number:
            print("Too low")
        else:
            print("Too high")
        guess = int(input("Guess again: "))
    print("Correct!")


def main():
    guess_number()


if __name__ == "__main__":
    main()
