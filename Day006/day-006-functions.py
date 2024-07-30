import random

# 1. Temel Fonksiyon Tanımı
def greet():
    return "Hello, World!"

print(greet())

# 2. Parametre Alan Fonksiyon
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# 3. Çoklu Parametre Alan Fonksiyon
def add(a, b):
    return a + b

print(add(5, 3))

# 4. Varsayılan Parametreli Fonksiyon
def greet(name="World"):
    return f"Hello, {name}!"

print(greet())
print(greet("Bob"))

# 5. Anahtar Kelime Argümanları ile Fonksiyon
def describe_pet(animal_type, pet_name):
    return f"I have a {animal_type} named {pet_name}."

print(describe_pet(animal_type="dog", pet_name="Rex"))

# 6. Değer Döndürmeyen Fonksiyon
def print_greeting():
    print("Hello, World!")

print_greeting()

# 7. Listeyi Parametre Olarak Alan Fonksiyon
def list_sum(numbers):
    return sum(numbers)

print(list_sum([1, 2, 3, 4, 5]))

# 8. İç İçe Fonksiyonlar
def outer_function(text):
    def inner_function():
        return text.upper()
    return inner_function()

print(outer_function("hello"))

# 9. Lambda Fonksiyonu
add = lambda x, y: x + y
print(add(3, 5))

# 10. Fonksiyonun Fonksiyon Döndürmesi
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(5))

# 11. Keyfi Sayıda Argüman Alan Fonksiyon
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4, 5))

# 12. Keyfi Sayıda Anahtar Kelime Argümanı Alan Fonksiyon
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# 13. Global Değişken Kullanımı
counter = 0

def increment_counter():
    global counter
    counter += 1

increment_counter()
print(counter)

# 14. Recursive Fonksiyon
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))

# 15. Docstring Kullanımı
def greet(name):
    """Bu fonksiyon bir ismi alır ve selam verir."""
    return f"Hello, {name}!"

print(greet("Alice"))
print(greet.__doc__)

# 16. Fonksiyonların Fonksiyon Parametresi Olarak Kullanılması
def apply_function(f, x):
    return f(x)

def square(n):
    return n * n

print(apply_function(square, 4))

# 17. Harfleri Büyükten Küçüğe Çeviren Fonksiyon
def to_uppercase(text):
    return text.upper()

print(to_uppercase("hello"))

# 18. Liste İçinde Listeyi Döndüren Fonksiyon
def nested_list(n):
    return [[i for i in range(n)] for _ in range(n)]

print(nested_list(3))

# 19. Fibonacci Serisini Döndüren Fonksiyon
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(10))

# 20. En Büyük Sayıyı Bulan Fonksiyon
def find_max(numbers):
    return max(numbers)

print(find_max([3, 5, 7, 2, 8]))
