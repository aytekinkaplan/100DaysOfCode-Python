import random


def random_number():
    return random.randint(1, 10)


def guess_number(function):
    def wrapper():
        number = random_number()
        guess_count = 0
        while guess_count < 5:
            guess = int(input("Guess the number: "))
            if guess == number:
                print("Correct!")
                break
            elif guess < number:
                print("Too low")
            else:
                print("Too high")
            guess_count += 1
        else:
            print(f"Sorry, you've used all attempts. The number was {number}.")
        return function()  # Süslenecek fonksiyonu çağırmak

    return wrapper


@guess_number
def guessNumber():
    pass  # Fonksiyonun içeriği boş


guessNumber()
