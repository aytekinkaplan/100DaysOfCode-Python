import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")

# Kullanıcıdan şifre için kaç adet harf, sembol ve rakam istediğini alır
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Kolay Seviye - Karakterlerin sırası rastgele değil
# Örneğin, 4 harf, 2 sembol, 2 rakam = JduE&!91
password_easy = ""

for _ in range(nr_letters):
    password_easy += random.choice(letters)

for _ in range(nr_symbols):
    password_easy += random.choice(symbols)

for _ in range(nr_numbers):
    password_easy += random.choice(numbers)

print(f"Easy level password: {password_easy}")

# Zor Seviye - Karakterlerin sırası rastgele
# Örneğin, 4 harf, 2 sembol, 2 rakam = g^2jk8&P
password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))

for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))

for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password_hard = ""
for char in password_list:
    password_hard += char

print(f"Hard level password: {password_hard}")
