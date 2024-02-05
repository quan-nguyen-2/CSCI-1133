def identity(n):
    lst = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        lst.append(row)
    
    return lst
print(identity(5))  
    
    
