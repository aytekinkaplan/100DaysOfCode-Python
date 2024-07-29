# BMI Calculation

height = input("What is your height in m? ")
weight = input("What is your weight in kg? ")

weight_as_int = int(weight)
height_as_float = float(height)

bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)

print(bmi_as_int)

name = input("What is your name? ")
print(f"Hello, {name}! You have a BMI of {bmi_as_int}.")