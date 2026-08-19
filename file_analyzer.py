filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    lines = content.splitlines()
    words = content.split()

    print("Number of lines:", len(lines))
    print("Number of words:", len(words))
    print("Number of characters:", len(content))

except FileNotFoundError:
    print("File not found.")
