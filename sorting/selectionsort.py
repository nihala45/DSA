lst = [1,5,2,4,3]
for i in range(len(lst)):
    min_index = i
    for j in range(i+1,len(lst)):
        if lst[min_index]>lst[j]:
            min_index = j
    lst[min_index],lst[i] = lst[i],lst[min_index]
    
print(lst)
        