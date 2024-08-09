import time


def measure_execution_time(func):
    def timed_execution(*args, **kwargs):
        start_timestamp = time.time()
        result = func(*args, **kwargs)
        end_timestamp = time.time()
        execution_duration = end_timestamp - start_timestamp
        print(f"Function {func.__name__} took {execution_duration:.2f} seconds to execute")
        return result

    return timed_execution


# Example usage
@measure_execution_time
def multiply_numbers(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


# Call the decorated function
result = multiply_numbers([i for i in range(1, 10)])
print(f"Result: {result}")
