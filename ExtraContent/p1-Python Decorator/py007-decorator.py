def check_condition_positive(value):
    def argument_validator(func):
        def validate_and_calculate(*args, **kwargs):
            if value(*args, **kwargs):
                return func(*args, **kwargs)
            else:
                raise ValueError("Invalid arguments passed to the function")
        return validate_and_calculate
    return argument_validator

@check_condition_positive(lambda x: x > 0)
def compute_cubed_result(number):
    return number ** 3

print(compute_cubed_result(5))  # Output: 125
print(compute_cubed_result(-2))  # Raises ValueError: Invalid arguments passed to the function
