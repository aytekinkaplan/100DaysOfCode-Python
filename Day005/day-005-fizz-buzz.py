# The FizzBuzz Job Interview Question
array_list = []
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        array_list.append("FizzBuzz")
    elif number % 3 == 0:
        array_list.append("Fizz")
    elif number % 5 == 0:
        array_list.append("Buzz")
    else:
        array_list.append(number)

for number in array_list:
    print(number)
