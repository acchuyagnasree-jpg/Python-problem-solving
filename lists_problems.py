# Creating a list
numbers = [10, 20, 30, 40, 50]

# Printing the list
print(numbers)

# Accessing elements
print(numbers[0])      # First element
print(numbers[-1])     # Last element

# Length of the list
print(len(numbers))

# Adding elements
numbers.append(60)
print(numbers)

# Inserting an element
numbers.insert(2, 25)
print(numbers)

# Removing an element
numbers.remove(30)
print(numbers)

# Removing the last element
numbers.pop()
print(numbers)

# Checking if an element exists
if 20 in numbers:
    print("20 is present")

# Finding the largest element
print(max(numbers))

# Finding the smallest element
print(min(numbers))

# Finding the sum
print(sum(numbers))

# Finding the average
average = sum(numbers) / len(numbers)
print(average)

# Sorting
numbers.sort()
print(numbers)

# Reverse sorting
numbers.sort(reverse=True)
print(numbers)

# Reversing the list
numbers.reverse()
print(numbers)

# Copying a list
copy_list = numbers.copy()
print(copy_list)

# Counting occurrences
print(numbers.count(20))

# Finding the index
print(numbers.index(20))

# Removing duplicates
unique = list(set(numbers))
print(unique)

# List slicing
print(numbers[1:4])

# Looping through a list
for item in numbers:
    print(item)

# List comprehension
squares = [x * x for x in range(1, 6)]
print(squares)
