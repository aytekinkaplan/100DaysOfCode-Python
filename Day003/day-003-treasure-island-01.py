import random
# Random number generator

import random

# Random number between 1 and 10
random_number = random.randint(1, 10)
print(random_number)

# Random number between 0 and 1
random_number = random.random()
print(random_number)

# Random number between 0 and 100
random_number = random.randint(0, 100)
print(random_number)

# Random number between 1 and 100
random_number = random.randint(1, 100)
print(random_number)

# Random number between 1 and 1000
random_number = random.randint(1, 1000)
print(random_number)

# Random string
random_string = random.choice(["rock", "paper", "scissors"])
print(random_string)