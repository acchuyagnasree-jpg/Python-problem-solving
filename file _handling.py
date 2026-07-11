with open("student.txt", "w") as file:
    file.write("Name: Alex\n")
    file.write("Course: Python Programming\n")
    file.write("Age: 20\n")

print("File created and data written successfully.\n")

print("Reading file:")
with open("student.txt", "r") as file:
    print(file.read())

with open("student.txt", "a") as file:
    file.write("City: Hyderabad\n")
    file.write("Grade: A\n")

print("New data appended successfully.\n")

print("Updated file content:")
with open("student.txt", "r") as file:
    print(file.read())
