def linear_search(arr, target):
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1  


arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(arr, target)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")


# RECURSIVE APPROACH

# def linear_search_recursive(arr, target, index=0):
#     if index >= len(arr):
#         return -1 
#     if arr[index] == target:
#         return index 
#     return linear_search_recursive(arr, target, index + 1) 

# arr = [10, 23, 45, 70, 11, 15]
# target = 70
# result = linear_search_recursive(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")
