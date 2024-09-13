lst = [1,5,2,4,3]
n = len(lst)
for i in range(1,n):
    pos = i
    current_element = lst[i]
    while current_element < lst[pos-1] and pos>0:
        lst[pos] = lst[pos - 1]
        pos = pos - 1
    lst[pos] = current_element
print(lst)
        
        
    
        