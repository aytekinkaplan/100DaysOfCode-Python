import tkinter as tk
from tkinter import messagebox


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


def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        result = calculator(num1, num2, {
            "+": add,
            "-": subtract,
            "*": multiply,
            "/": divide
        }[operation])
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")


def calculator(num1, num2, operation):
    return operation(num1, num2)


# GUI Setup
root = tk.Tk()
root.title("Simple Calculator")

# Number Entry Fields
tk.Label(root, text="Enter the first number:").grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

tk.Label(root, text="Enter the second number:").grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Operation Selection
operation_var = tk.StringVar(value="+")
tk.Label(root, text="Select operation:").grid(row=2, column=0)
operations = ["+", "-", "*", "/"]
for i, op in enumerate(operations):
    tk.Radiobutton(root, text=op, variable=operation_var, value=op).grid(row=2, column=i + 1)

# Calculate Button
calc_button = tk.Button(root, text="Calculate", command=calculate)
calc_button.grid(row=3, column=0, columnspan=4)

# Result Label
result_label = tk.Label(root, text="Result: ")
result_label.grid(row=4, column=0, columnspan=4)

root.mainloop()
