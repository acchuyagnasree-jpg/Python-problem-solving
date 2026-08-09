numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) < 2:
    print("Second largest number does not exist")
else:
    print("Second largest:", unique_numbers[-2])
