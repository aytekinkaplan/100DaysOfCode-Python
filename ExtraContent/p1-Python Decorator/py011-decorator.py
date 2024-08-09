import inspect


def enforce_type_checking(func):
    def type_checked_wrapper(*args, **kwargs):
        # Get the function signature and parameter names
        function_signature = inspect.signature(func)
        function_parameters = function_signature.parameters

        # Iterate over the positional arguments
        for i, arg_value in enumerate(args):
            parameter_name = list(function_parameters.keys())[i]
            parameter_type = function_parameters[parameter_name].annotation
            if not isinstance(arg_value, parameter_type):
                raise TypeError(f"Argument '{parameter_name}' must be of type '{parameter_type.__name__}'")

        # Iterate over the keyword arguments
        for keyword_name, arg_value in kwargs.items():
            parameter_type = function_parameters[keyword_name].annotation
            if not isinstance(arg_value, parameter_type):
                raise TypeError(f"Argument '{keyword_name}' must be of type '{parameter_type.__name__}'")

        # Call the original function
        return func(*args, **kwargs)

    return type_checked_wrapper


# Example usage
@enforce_type_checking
def multiply_numbers(factor_1: int, factor_2: int) -> int:
    return factor_1 * factor_2


# Call the decorated function
result = multiply_numbers(5, 7)  # No type errors, returns 35
print("Result:", result)

result = multiply_numbers("5", 7)  # Type error: 'factor_1' must be of type 'int'
