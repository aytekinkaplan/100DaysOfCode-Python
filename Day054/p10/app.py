import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {func.__name__} took {end_time - start_time} seconds to complete")
        return result
    return wrapper

@timer
def some_function():
    time.sleep(2)
    print("Function is done!")

some_function()
