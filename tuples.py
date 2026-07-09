
# Create a  tuple
numbers = (10, 20, 30, 40, 50, 20)

print("Tuple:", numbers)

# Length 
print("Length:", len(numbers))

# First and last elements
print("First Element:", numbers[0])
print("Last Element:", numbers[-1])

# Maximum and minimum values
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Sum of all elements
print("Sum:", sum(numbers))

# Count occurrences of an element
print("Count of 20:", numbers.count(20))

# Find the index of an element
print("Index of 40:", numbers.index(40))

# Check if an element exists
search = 30

if search in numbers:
    print(search, "is present in the tuple.")
else:
    print(search, "is not present in the tuple.")

# Convert tuple to list
numbers_list = list(numbers)
print("Converted to List:", numbers_list)

# Convert list back to tuple
numbers_tuple = tuple(numbers_list)
print("Converted Back to Tuple:", numbers_tuple)
