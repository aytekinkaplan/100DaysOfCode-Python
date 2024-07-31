def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "Can't divide by zero!"
    return n1 / n2


print("Welcome to the Python Calculator!")
type_of_calc = input(
    "Choose type of calculation: 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division: ")

operations = {
    "a": add,
    "s": subtract,
    "m": multiply,
    "d": divide,
}

if type_of_calc in operations:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
    result = operations[type_of_calc](n1, n2)
    print(f"The result is: {result}")
else:
    print("Invalid input!")
