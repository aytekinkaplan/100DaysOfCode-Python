import time


def cached_function_with_expiry(expiry_time):
    def decorator(original_function):
        cache = {}

        def wrapper(*args, **kwargs):
            key = (*args, *kwargs.items())

            if key in cache:
                cached_value, cached_timestamp = cache[key]

                if time.time() - cached_timestamp < expiry_time:
                    return f"[CACHED] - {cached_value}"

            result = original_function(*args, **kwargs)
            cache[key] = (result, time.time())

            return result

        return wrapper

    return decorator


# Example usage

@cached_function_with_expiry(expiry_time=5)  # Cache expiry time set to 5 seconds
def calculate_product(x, y):
    return f"PRODUCT - {x * y}"


# Call the decorated function multiple times
print(calculate_product(23, 5))  # Calculation is performed
print(calculate_product(23, 5))  # Result is retrieved from cache
time.sleep(5)
print(calculate_product(23, 5))  # Calculation is performed (cache expired)
