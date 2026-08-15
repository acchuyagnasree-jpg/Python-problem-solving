numbers = [1, 2, 3, 4, 5, 6]
k = 2

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print("Original:", numbers)
print("Rotated:", rotated)
