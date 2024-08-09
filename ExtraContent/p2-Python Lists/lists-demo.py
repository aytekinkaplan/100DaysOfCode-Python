# 1- Create a list containing the elements "Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8".
phones = ["Samsung S5", "Samsung S6", "Samsung S7", "Samsung S8"]

# 2- How many elements are in the list?
result = len(phones)

# 3- What is the first and last element of the list?
result = phones[0]
result = phones[-1]

# 4- Replace "Samsung S5" with "Samsung S9".
# phones[0] = "Samsung S9"
result = phones

# 5- Is "Samsung S6" an element of the list?
if "Samsung S6" in phones:
    print("Samsung S6 is in the list.")

# 6- What is the value at the -3 index of the list?
result = phones[-3]

# 7- Get the first 2 elements of the list.
result = phones[:2]

# 8- Replace the last 2 elements of the list with "Samsung S9" and "Samsung S10".
# phones[-2:] = ["Samsung S9", "Samsung S10"]
result = phones

# 9- Add "iPhone X" and "iPhone XR" to the list.
result = phones + ["iPhone X", "iPhone XR"]

# 10- Delete the last element of the list.
# del phones[-1]
result = phones

# 11- Print the list elements in reverse order.
result = phones[::-1]

# 12- Store the following data in a list:

# userA: Yiğit Bilgi 2010, (70, 60, 70)
# userB: Sena Turan 1999, (80, 80, 70)
# userC: Ahmet Turan 1998, (80, 70, 90)

studentA = ["Yiğit", "Bilgi", 2010, [70, 60, 70]]
studentB = ["Sena", "Turan", 1999, [80, 80, 70]]
studentC = ["Ahmet", "Turan", 1998, [80, 70, 90]]

students = [studentA, studentB, studentC]

for student in students:
    first_name = student[0]
    last_name = student[1]
    age = 2021 - student[2]
    average = (student[3][0] + student[3][1] + student[3][2]) / 3
    print(f"{first_name} {last_name} {age} {average:.2f}")

# 13- Print the list elements to the screen.

# for phone in phones:
#     print(phone)

# print(result)
