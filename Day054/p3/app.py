# Python Decorator Function

def decorator_function(say_my_name):
    def wrapper_function(name):
        print("Hello, there!")
        say_my_name(name)
        print("Bye, bye!")

    return wrapper_function


@decorator_function
def say_my_name(name):
    print(f"My name is {name}")


say_my_name("John")
