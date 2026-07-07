
rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n=== Sum of Numbers from 1 to 10 ===")

total = 0

for i in range(1, 11):
    total += i

print("Sum =", total)

print("\n=== Multiplication Table of 5 ===")

for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")
