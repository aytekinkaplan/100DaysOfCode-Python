import math


def prime_checker(number):
    if number <= 1:
        print("It's not a prime number.")
    elif number <= 3:
        print("It's a prime number.")
    elif number % 2 == 0 or number % 3 == 0:
        print("It's not a prime number.")
    else:
        i = 5
        while i * i <= number:
            if number % i == 0 or number % (i + 2) == 0:
                print("It's not a prime number.")
                return
            i += 6
        print("It's a prime number.")


# Do NOT change any of the code below👇
n = int(input())  # Check this number
prime_checker(number=n)
