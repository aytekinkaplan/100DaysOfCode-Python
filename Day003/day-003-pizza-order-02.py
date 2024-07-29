print("Welcome to Python Pizza Deliveries!")
print("Our menu is:")
print("Sizes: \nS - Small: $15\nM - Medium: $20\nL - Large: $25")
print("Toppings:")
print("P - Pepperoni: $2\nV - Vegetarian: $3\nE - Extra cheese: $1\n"
      "T - Tomato sauce: $1\nH - Ham: $1\nO - Onions: $1\n"
      "C - Capsicum: $1\nM - Mushrooms: $1\nG - Green peppers: $1\n"
      "B - Black olives: $1\nN - Pineapple: $1\nA - Anchovies: $1")

size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

# Set base price according to the size
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
else:
    print("Invalid size selected.")
    bill = 0

# Add pepperoni price if selected
if add_pepperoni == "Y":
    bill += 2

# Add extra cheese price if selected
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}")
