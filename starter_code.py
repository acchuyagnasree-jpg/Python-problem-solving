students = [
    ["Anu", 85, 78, 92],
    ["Ravi", 65, 72, 68],
    ["Priya", 95, 91, 89],
    ["Kiran", 45, 52, 48],
    ["Sneha", 82, 88, 79]
]

for student in students:

    name = student[0]
    marks = student[1:]

    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("-------------------------")
    print("Name:", name)
    print("Total:", total)
    print("Average:", round(average, 2))
    print("Grade:", grade)
