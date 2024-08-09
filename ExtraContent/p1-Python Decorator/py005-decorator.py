def convert_to_data_type(target_type):
    def type_converter_decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return target_type(result)

        return wrapper

    return type_converter_decorator


@convert_to_data_type(int)
def add_values(a, b):
    return a + b


int_result = add_values(10, 20)
print("Result:", int_result, type(int_result))


@convert_to_data_type(str)
def concatenate_strings(str1, str2):
    return str1 + str2


str_result = concatenate_strings("Python", " Decorator")
print("Result:", str_result, type(str_result))
