# key - value

# 41 => Van
# 34 => Istanbul

cities = ['van', 'istanbul']
plate_numbers = [65, 34]

# print(plate_numbers[0], cities[0])
# print(plate_numbers[1], cities[1])

# print(plate_numbers[cities.index('istanbul')])
# print(plate_numbers[cities.index('van')])

plate_numbers = {'kocaeli': 41, 'istanbul': 34}

# print(plate_numbers['van'])
# print(plate_numbers['istanbul'])

plate_numbers['izmir'] = 35
# plate_numbers['rize'] = 36

# plate_numbers['izmir'] = 35 # Changing 36 to 35
# print(plate_numbers)

students = {
    100: {
        "first_name": "Ahmed",
        "last_name": "Kaplan",
        "age": 4,
        "grades": [70, 80, 70]
    },
    101: {
        "first_name": "Yusuf",
        "last_name": "Yıldırım",
        "age": 10
    }
}

result = students[100]
result = students[101]["first_name"]
result = students[101]["last_name"]

result = (students[100]["grades"][0] + students[100]["grades"][1] + students[100]["grades"][2]) / 3

print(result)
