def cached_result_decorator(func):
    result_cache = {}

    def wrapper(*args, **kwargs):
        cache_key = (*args, *kwargs.items())

        if cache_key in result_cache:
            return f"[FROM CACHE] {result_cache[cache_key]}"

        result = func(*args, **kwargs)
        result_cache[cache_key] = result

        return result

    return wrapper


# Example usage

@cached_result_decorator
def multiply_numbers(a, b):
    return f"Product = {a * b}"


# Call the decorated function multiple times
print(multiply_numbers(4, 5))  # Calculation is performed
print(multiply_numbers(4, 5))  # Result is retrieved from cache
print(multiply_numbers(5, 7))  # Calculation is performed
print(multiply_numbers(5, 7))  # Result is retrieved from cache
print(multiply_numbers(-3, 7))  # Calculation is performed
print(multiply_numbers(-3, 7))  # Result is retrieved from cache
