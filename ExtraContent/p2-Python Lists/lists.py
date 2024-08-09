msg = "Welcome to our Python Course. I am Sadık Turan".split()

numbers = [1, 3, 5, 7, 9]

result = numbers
result = numbers[0]
result = numbers[4]
# result = numbers[5] # IndexError: list index out of range

names = ['ahmet', 'ali', 'can', 'ada']

result = names[0]

# print(type(names[0]))
# print(type(numbers[0]))

listAli = ['ali', 20]
listAhmet = ['ahmet', 22]

result = listAli[0]
result = listAli[1]

# students = [["ali", 20], ["ahmet", 22]]
students = [listAli, listAhmet]

result = students[0][0]
# result = students[1][0]

print(result)
