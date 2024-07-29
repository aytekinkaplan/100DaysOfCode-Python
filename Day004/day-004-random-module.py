import random

random_number = random.randint(1, 10)
print(random_number)

random_names = random.choice(["Alice", "Bob", "Charlie"])
print(random_names)

random_float = random.random()
print(random_float)

random_color = random.choice(["red", "green", "blue"])
print(random_color)

random_decimal = random.uniform(1, 5)
print(random_decimal)

random_numbers = random.sample(range(1, 11), 9)
print(random_numbers)

rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
print(rgb)