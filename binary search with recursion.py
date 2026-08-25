def binary_search(arr, target, left, right):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    if target < arr[mid]:
        return binary_search(arr, target, left, mid - 1)

    return binary_search(arr, target, mid + 1, right)


arr = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

index = binary_search(arr, target, 0, len(arr) - 1)

if index != -1:
    print("Element found at index:", index)
else:
    print("Element not found")
