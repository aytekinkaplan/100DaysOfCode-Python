import time


def delay_decorator(func):
    def wrapper(*args, **kwargs):
        time.sleep(2)
        result = func(*args, **kwargs)
        return result

    return wrapper


@delay_decorator
def hello():
    print("Hello")


@delay_decorator
def what_is_up():
    print("What's up?")


@delay_decorator
def what_is_your_name():
    name = input("Plase enter your name:\n")
    print(f"Hello {name}")


def main():
    hello()
    what_is_up()
    what_is_your_name()


if __name__ == "__main__":
    main()
