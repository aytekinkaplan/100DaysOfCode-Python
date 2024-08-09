import tracemalloc


def measure_memory_usage(target_function):
    def wrapper(*args, **kwargs):
        tracemalloc.start()

        # Call the original function
        result = target_function(*args, **kwargs)

        snapshot = tracemalloc.take_snapshot()
        top_stats = snapshot.statistics("lineno")

        # Print the top memory-consuming lines
        print(f"Memory usage of {target_function.__name__}:")
        for stat in top_stats[:5]:
            print(stat)

        # Return the result
        return result

    return wrapper


# Example usage
@measure_memory_usage
def calculate_factorial_recursive(number):
    if number == 0:
        return 1
    else:
        return number * calculate_factorial_recursive(number - 1)


# Call the decorated function
result_factorial = calculate_factorial_recursive(3)
print("Factorial:", result_factorial)
