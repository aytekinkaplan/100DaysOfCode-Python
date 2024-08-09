numbers = [1, 5, 8, 9, 3, 45, 77, 5]
letters = ['a', 'b', 'e', 's', 'a', 'y']

result = min(numbers)
result = max(numbers)
result = min(letters)
result = max(letters)

# Adding elements
numbers.append(10)
numbers.insert(3, 5)
numbers.insert(-1, 50)
numbers.insert(len(numbers), 150)

# Removing elements
numbers.pop()
numbers.pop(0)
numbers.remove(45)
letters.remove('y')

# Sorting
numbers.sort()
letters.sort()
numbers.reverse()

# Counting elements
# print(numbers.count(5))
# print(letters.count('a'))

print(numbers.index(3))
numbers.clear()

result = numbers
# result = letters

print(result)
