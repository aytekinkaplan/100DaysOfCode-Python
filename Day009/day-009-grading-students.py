student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student, score in student_scores.items():
    if score > 90:
        new_score = "Outstanding"
    elif score > 80:
        new_score = "Exceeds Expectations"
    elif score > 70:
        new_score = "Acceptable"
    else:
        new_score = "Fail"
    student_grades[student] = new_score

# 🚨 Don't change the code below 👇
print(student_grades)
