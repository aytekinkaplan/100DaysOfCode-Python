# 🚨 Don't change the code below 👇
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

for student, score in student_scores.items():
    if score > 90:
        student_scores[student] = "Outstanding"
    elif score > 80:
        student_scores[student] = "Exceeds Expectations"
    elif score > 70:
        student_scores[student] = "Acceptable"
    else:
        student_scores[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_scores)
