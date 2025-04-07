def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Sample sorted list
numbers = [3, 7, 12, 18, 23, 31, 42, 57, 63, 75, 88, 95]

print("🔍 Welcome to Binary Search Project!")
print("Sorted list:", numbers)

# User input
try:
    target = int(input("Enter a number to search in the list: "))
    result = binary_search(numbers, target)

    if result != -1:
        print(f"✅ Number {target} found at index {result}.")
    else:
        print(f"❌ Number {target} not found in the list.")
except ValueError:
    print("⚠️ Please enter a valid integer.")
