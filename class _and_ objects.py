class Student:
    def __init__(self, roll_no, name, branch, marks):
        self.roll_no = roll_no
        self.name = name
        self.branch = branch
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Branch  : {self.branch}")
        print(f"Marks   : {self.marks}")

    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        else:
            return "Fail"


student1 = Student(101, "Rahul", "AIML", 92)
student2 = Student(102, "Priya", "CSE", 78)
student3 = Student(103, "Arjun", "ECE", 65)

students = [student1, student2, student3]

for student in students:
    student.display()
    print("Grade   :", student.grade())
