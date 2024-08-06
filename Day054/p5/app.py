# Python Decorator Function

def decorator_function(func):
    def wrapper():
        func()

    return wrapper


@decorator_function
def say_hello():
    print("Hello!")


say_hello()
