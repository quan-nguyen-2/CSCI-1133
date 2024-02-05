def matrix(n,init):
    lst = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(init)
        lst.append(row)
    return lst
print(matrix(5,3))        
    

def order(m):
    rows = len(m) * len(m)
    return rows
print(order(matrix(5,3)))
