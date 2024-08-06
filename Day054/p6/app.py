# Python Decorator Function

def m_decorator(func):
    def wrapper():
        print("Hello")
        func()
        print("Bye")
    return wrapper

@m_decorator
def say_hello():
    print("Hello!")

say_hello()