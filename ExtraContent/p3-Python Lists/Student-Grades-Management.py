students = []


def add_student():
    try:
        name = input("Enter student name: ")
        surname = input("Enter student surname: ")
        birth_year = int(input("Enter student birth year: "))
        grades = {
            "math": int(input("Enter student math grade: ")),
            "physics": int(input("Enter student physics grade: ")),
            "chemistry": int(input("Enter student chemistry grade: ")),
            "history": int(input("Enter student history grade: ")),
            "geography": int(input("Enter student geography grade: ")),
            "computer science": int(input("Enter student computer science grade: ")),
            "literature": int(input("Enter student literature grade: ")),
            "politics": int(input("Enter student politics grade: ")),
        }
        new_grades = list(grades.values())
        student = (name, surname, birth_year, new_grades)
        students.append(student)
        print("Student added successfully!")
        print(
            f"Student name: {name} | Student surname: {surname} | Student birth year: {birth_year} | Student grades: {new_grades}")
    except ValueError:
        print("Invalid input. Please enter numeric values for grades and birth year.")


def average_grade():
    name = input("Enter student name: ")
    surname = input("Enter student surname: ")
    for student in students:
        if student[0] == name and student[1] == surname:
            grades = student[3]
            average = sum(grades) / len(grades)
            print(f"Average grade: {average:.2f}")
            break
    else:
        print("Student not found.")


def list_students_by_birth_year():
    birth_year = int(input("Enter the birth year to list students: "))
    found = False
    for student in students:
        if student[2] == birth_year:
            print(
                f"Student name: {student[0]} | Student surname: {student[1]} | Student birth year: {student[2]} | Student grades: {student[3]}")
            found = True
    if not found:
        print("No students found for the given birth year.")


while True:
    print("\nStudent Grades Management")
    print("1. Add Student")
    print("2. Calculate Average Grade")
    print("3. List Students by Birth Year")
    print("4. Exit")
    choice = input("Make your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        average_grade()
    elif choice == "3":
        list_students_by_birth_year()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

print("Thank you for using the Student Grades Management System!")
