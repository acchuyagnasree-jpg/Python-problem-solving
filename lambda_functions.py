students = [
    {"name": "Alice", "marks": 82},
    {"name": "Bob", "marks": 45},
    {"name": "Charlie", "marks": 91},
    {"name": "David", "marks": 67},
    {"name": "Eva", "marks": 55}
]

while True:
    print("\n===== Student Data Analyzer =====")
    print("1. Show All Students")
    print("2. Show Passed Students")
    print("3. Show Failed Students")
    print("4. Sort by Marks")
    print("5. Add 5 Grace Marks")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        for student in students:
            print(student)

    elif choice == "2":
        passed = list(filter(lambda s: s["marks"] >= 50, students))
        print("\nPassed Students:")
        for student in passed:
            print(student)

    elif choice == "3":
        failed = list(filter(lambda s: s["marks"] < 50, students))
        print("\nFailed Students:")
        for student in failed:
            print(student)

    elif choice == "4":
        sorted_students = sorted(students, key=lambda s: s["marks"], reverse=True)
        print("\nStudents Sorted by Marks:")
        for student in sorted_students:
            print(student)

    elif choice == "5":
        updated_marks = list(
            map(lambda s: {"name": s["name"], "marks": s["marks"] + 5}, students)
        )
        print("\nAfter Grace Marks:")
        for student in updated_marks:
            print(student)

    elif choice == "6":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice.")
