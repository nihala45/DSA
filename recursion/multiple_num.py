def multiple_num(n,i):
    if i == 10:
        return []
    return [n*i]+multiple_num(n,i+1)
print(multiple_num(5,1))