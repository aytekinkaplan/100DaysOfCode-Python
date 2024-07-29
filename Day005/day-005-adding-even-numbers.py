# Adding Even Numbers

numbers_user_entered = input("Enter Numbers: \n").split()

for number in range(0, len(numbers_user_entered)):
    numbers_user_entered[number] = int(numbers_user_entered[number])

even_numbers = []
for number in numbers_user_entered:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
print(sum(even_numbers))

total_numbers = 0
for number in range(0, 101):
    if number % 2 == 0:
        total_numbers += number
print(total_numbers)