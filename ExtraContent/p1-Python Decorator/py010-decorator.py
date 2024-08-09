def handle_exceptions(default_response_msg):
    def exception_handler_decorator(func):
        def decorated_function(*args, **kwargs):
            try:
                # Call the original function
                return func(*args, **kwargs)
            except Exception as error:
                # Handle the exception and provide the default response
                print(f"Exception occurred: {error}")
                return default_response_msg

        return decorated_function

    return exception_handler_decorator


# Example usage
@handle_exceptions(default_response_msg="An error occurred!")
def divide_numbers_safely(dividend, divisor):
    return dividend / divisor


# Call the decorated function
result = divide_numbers_safely(7, 0)  # This will raise a ZeroDivisionError
print("Result:", result)
