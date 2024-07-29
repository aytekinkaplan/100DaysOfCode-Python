# Data Types

# 1. Integers
# 2. Floats
# 3. Strings
# 4. Booleans
# 5. Lists
# 6. Tuples
# 7. Sets
# 8. Dictionaries
# 9. None

# 1. Integers Examples

a = 10
b = 5
c = a + b
print(c)  # 15

c = a - b
print(c)  # 5

c = a * b
print(c)  # 50

c = a / b
print(c)  # 2.0

c = a % b
print(c)  # 0

c = a // b
print(c)  # 2

c = a ** b
print(c)  # 100000

# 2. Floats Examples

a = 10.0
b = 5.0
c = a + b
print(c)  # 15.0

c = a - b
print(c)  # 5.0

c = a * b
print(c)  # 50.0

c = a / b
print(c)  # 2.0

c = a % b
print(c)  # 0.0

c = a // b
print(c)  # 2.0

c = a ** b
print(c)  # 100000.0

# 3. Strings Examples

a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Hello World

# 4. Booleans Examples

a = True
b = False
c = a and b
print(c)  # False

c = a or b
print(c)  # True

c = not a
print(c)  # False

# 5. Lists Examples

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

c = a * 3
print(c)  # [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

c = 3 in a
print(c)  # True

c = 3 not in a
print(c)  # False

# 6. Tuples Examples

a = (1, 2, 3, 4, 5)
b = (6, 7, 8, 9, 10)
c = a + b
print(c)  # (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

c = a * 3
print(c)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

c = 3 in a
print(c)  # True

c = 3 not in a
print(c)  # False

# 7. Sets Examples

a = {1, 2, 3, 4, 5}
b = {6, 7, 8, 9, 10}
c = a | b
print(c)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

c = a & b
print(c)  # set()

c = a - b
print(c)  # {1, 2, 3, 4, 5}

c = a ^ b
print(c)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# 8. Dictionaries Examples

a = {"name": "John", "age": 30, "city": "New York"}
b = {"name": "Jane", "age": 25, "city": "Paris"}

# Dictionaries do not support bitwise operations
c = {**a, **b}  # Merges two dictionaries, the value of common keys will be from the second dictionary
print(c)  # {'name': 'Jane', 'age': 25, 'city': 'Paris'}

# 9. None Examples

a = None
b = None

# NoneType does not support arithmetic or bitwise operations
print(a)  # None
print(b)  # None

c = a is None
print(c)  # True

c = b is None
print(c)  # True
