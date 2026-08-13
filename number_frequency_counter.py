numbers = list(map(int, input("Enter numbers: ").split()))

frequency = {}

for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

print("Frequency:")

for num, count in frequency.items():
    print(num, "->", count)
