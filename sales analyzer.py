sales = []

n = int(input("Enter number of sales: "))

for i in range(n):
    amount = float(input(f"Sale {i + 1}: "))
    sales.append(amount)

total = sum(sales)
average = total / len(sales)
highest = max(sales)
lowest = min(sales)

print("\n--- Sales Report ---")
print("Total Sales:", total)
print("Average Sale:", round(average, 2))
print("Highest Sale:", highest)
print("Lowest Sale:", lowest)
