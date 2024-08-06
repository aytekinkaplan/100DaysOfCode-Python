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


@my_decorator
def say_bye(name):
    print(f"Bye {name}")


say_hello("John")
say_bye("John")
