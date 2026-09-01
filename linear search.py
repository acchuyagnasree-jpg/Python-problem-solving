numbers = [12, 45, 23, 67, 89, 34]

target = int(input("Enter number to search: "))

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index:", i)
        found = True
        break

if not found:
    print("Number not found")
