print("Welcome to the Python Calculator!")
type_of_calc = input(
    "Choose type of calculation: 'a' for addition, 's' for subtraction, 'm' for multiplication, 'd' for division: ")

try:
    n1 = float(input("Enter first number: "))
    n2 = float(input("Enter second number: "))
except ValueError:
    print("Invalid input. Please enter numeric values.")
    exit()

operations = {
    "a": lambda x, y: x + y,
    "s": lambda x, y: x - y,
    "m": lambda x, y: x * y,
    "d": lambda x, y: "Can't divide by zero!" if y == 0 else x / y
}

if type_of_calc in operations:
    result = operations[type_of_calc](n1, n2)
    print(f"The result is: {result}")
else:
    print("Invalid input!")
