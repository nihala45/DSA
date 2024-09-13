lst = [1,15,13,2,4,3]
for i in range(len(lst)-1):
    for j in range(len(lst)-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            
print(lst)