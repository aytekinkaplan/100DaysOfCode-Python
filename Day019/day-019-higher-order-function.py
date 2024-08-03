def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    if num2 == 0:
        return "Can't divide by zero!"
    return num1 / num2


def calculator(num1, num2, operation):
    return operation(num1, num2)


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def get_operation():
    operations = {"+", "-", "*", "/"}
    while True:
        operation = input("Enter the operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")


num1 = get_number("Enter the first number: ")
num2 = get_number("Enter the second number: ")
operation = get_operation()

result = calculator(num1, num2, {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}[operation])

print("Result:", result)
