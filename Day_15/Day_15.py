students = {}

def add_student():
    name = input("Enter student name: ")

    if name in students:
        print("Student already exists!")
        return

    mark = int(input("Enter mark: "))
    students[name] = mark

    print("Student added successfully!")


def view_students():
    if not students:
        print("No students found.")
        return

    print("\nStudent Records:")
    for name, mark in students.items():
        print(f"{name}: {mark}")


def search_student():
    name = input("Enter student name: ")

    if name in students:
        print(f"{name}'s mark: {students[name]}")
    else:
        print("Student not found.")


def update_mark():
    name = input("Enter student name: ")

    if name in students:
        new_mark = int(input("Enter new mark: "))
        students[name] = new_mark
        print("Mark updated successfully!")
    else:
        print("Student not found.")


def delete_student():
    name = input("Enter student name: ")

    if name in students:
        del students[name]
        print("Student deleted successfully!")
    else:
        print("Student not found.")


def highest_mark():
    if not students:
        print("No students found.")
        return

    top_student = max(students, key=students.get)

    print("\nHighest Scorer")
    print(f"Name: {top_student}")
    print(f"Mark: {students[top_student]}")


def average_mark():
    if not students:
        print("No students found.")
        return

    avg = sum(students.values()) / len(students)

    print(f"Average Mark: {avg:.2f}")


while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Mark")
    print("5. Delete Student")
    print("6. Highest Mark")
    print("7. Average Mark")
    print("8. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_mark()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        highest_mark()

    elif choice == "7":
        average_mark()

    elif choice == "8":
        print("Goodbye!")
        break

    else:
        print("Please enter a valid choice.")