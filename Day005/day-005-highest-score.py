# Highest Score

student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

newestScore = sorted(student_scores, reverse=True)
print(f"The highest score in the class is: {newestScore[0]}")


