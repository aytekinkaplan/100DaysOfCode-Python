def log_decorator(original_function):
    def wrapper(*args, **kwargs):
        print(f"Calling {original_function.__name__} with args: {args}, kwargs: {kwargs}")

        # Call the original function
        result = original_function(*args, **kwargs)

        # Log the return value
        print(f"{original_function.__name__} returned: {result}")

        # Return the result
        return result
    return wrapper

# Example usage
@log_decorator
def calculate_product(x, y):
    return x * y

# Call the decorated function
result = calculate_product(10, 20)
print("Result:", result)