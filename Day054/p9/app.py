def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result

    return wrapper


@my_decorator
def say_hello(name):
    print(f"Hello {name}")


say_hello("John")


@my_decorator
def say_bye(name):
    print(f"Bye {name}")


say_bye("John")


@my_decorator
def add_numbers(num1, num2, num3):
    return num1 + num2 + num3


# Kullanıcıdan girdi al
numb1 = int(input("Enter first number: "))
numb2 = int(input("Enter second number: "))
numb3 = int(input("Enter third number: "))

# Fonksiyonu çağır ve sonucu yazdır
result = add_numbers(numb1, numb2, numb3)
print(result)
