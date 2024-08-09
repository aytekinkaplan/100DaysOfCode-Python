names = ['Ada', 'Yiğit', 'Hasan', 'Beril']
ages = [1998, 2000, 1998, 1987]

# 1- Add "Cenk" to the end of the list.
names.append('Cenk')

# 2- Add "Sena" to the beginning of the list.
names.insert(0, "Sena")
names.insert(-1, "Sena")
names.insert(len(names), "Sena")

# 3- Remove "Yiğit" from the list.
# names.remove("Yiğit")
names.pop()
names.pop(0)

# 4- What is the index of "Yiğit"?
index = names.index('Yiğit')
names.pop(index)
print(index)

# 5- Is "Beril" an element of the list?
result = "Beril" in names
print(result)

# 6- Reverse the elements of the list.
names.reverse()
ages.reverse()

# 7- Sort the list alphabetically.
names.sort()

# 8- Sort the ages list numerically.
ages.sort()

# 9- Convert the string "IPhone X,IPhone XR" into a list.
s = "IPhone X,IPhone XR"
result = s.split(',')
print(result)

# 10- What is the largest and smallest element in the ages list?
print(min(ages))
print(max(ages))

# 11- How many times does 1998 appear in the ages list?
print(ages.count(1998))

# 12- Clear all elements from the ages list.
ages.clear()

# 13- Store 3 brand names provided by the user in a list.
brands = []

brand = input("Brand: ")
brands.append(brand)

brand = input("Brand: ")
brands.append(brand)

brand = input("Brand: ")
brands.append(brand)

print(brands)

print(names)
print(ages)
