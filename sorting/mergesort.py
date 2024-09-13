def mergesort(arr):
    if len(arr)<=1:
        return arr
    mid = len(arr)//2
    lefthalf = arr[:mid]
    righthalf = arr[mid:]
    leftsort = mergesort(lefthalf)
    rightsort = mergesort(righthalf)
    
    return merge(leftsort,rightsort)
def merge(left,right):
    i = j = 0
    result = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result
lst = [1,5,2,4,3]
print(mergesort(lst))
