# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2  

#         if arr[mid] == target:
#             return mid 
#         elif arr[mid] < target:
#             low = mid + 1 
#         else:
#             high = mid - 1  

#     return -1  


# arr = [1, 3, 5, 7, 9, 11, 13, 15]
# target = 7
# result = binary_search(arr, target)

# if result != -1:
#     print(f"Element found at index {result}")
# else:
#     print("Element not found")



# USING RECURSION

def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1 

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid  
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)  
    else:
        return binary_search_recursive(arr, target, low, mid - 1) 

arr = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7
result = binary_search_recursive(arr, target, 0, len(arr) - 1)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")