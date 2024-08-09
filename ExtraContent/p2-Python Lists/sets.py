# list
# tuple
# dictionary
# sets => unindexed, unordered

fruits = {"apple", "cherry", "melon", "grape"}
vegetables = {"peas", "onion"}

# result = fruits[0]  # Cannot be indexed
result = "apple" in fruits
fruits.add("watermelon")
fruits.update(["sour cherry", "melon"])

result = len(fruits)
# fruits.remove("watermelonn")  # KeyError
# fruits.discard("watermelon")

# result = fruits.pop()
# fruits.clear()

result = fruits.union(vegetables)

# for x in fruits:
#     print(x)

print(result)
