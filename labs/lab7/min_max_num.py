def min_max_nums(string):
    lst = string.split()
    element = 0
    min = len(lst[0])
    max = len(lst[0])
    for i in lst:
        (len(lst[element]))
        element += 1
        if min > len(i):
            min = len(i)
        if max < len(i):
            max = len(i)
    return [min,max]
print(min_max_nums("The yellow kite was flying in the bright blue sky"))
