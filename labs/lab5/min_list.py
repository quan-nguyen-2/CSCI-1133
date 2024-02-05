def minimum_index(lst, index):
    min_index = index
    for i in range(len(lst)-(index+1), len(lst), 1):
        if lst[i] < lst[min_index]:
            min_index = i
    return min_index

print(minimum_index([9, 1, 7, 6, 8,], 2))
print(minimum_index([1, 3, 7, 6, 2,], 1))
