list_of_strings = input().split(',')
# 🚨 Do  not change the code above

# TODO: Use list comprehension to convert the strings to integers 👇:

result = [int(string) for string in list_of_strings if int(string) % 2 == 0]


# TODO: Use list comprehension to filter out the odd numbers
# and store the even numbers in a list called "result"



# Write your code 👆 above:
print(result)