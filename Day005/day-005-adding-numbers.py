# Adding Numbers

# Adding Random Numbers

number_user_entered = input("Enter Numbers: \n").split()

for number in range(0, len(number_user_entered)):
    number_user_entered[number] = int(number_user_entered[number])

sum = 0
for number in number_user_entered:
    sum += number
print(sum)
