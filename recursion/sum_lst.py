def sum_lst(lst):
    if lst == []:
        return 0
    return lst[-1] + sum_lst(lst[:-1])
lst = [1,2,3,4,5]
print(sum_lst(lst))