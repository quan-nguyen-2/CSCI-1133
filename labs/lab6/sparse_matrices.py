import random
def populate(mtrx,n,value):
    matrix = mtrx[0][1]
    mtrx[0][1] = 0

    
    for i in range(len(mtrx)):
        for j in range(len(mtrx[1])):
            mtrx[i][j] = 0
    while n > 0:
        colm = random.randint(0, len(mtrx[i]) -1)
        row = random.randint(0, len(mtrx) - 1)
        mtrx[row][colm] = value
        n = n- 1

    return mtrx
print(populate([[1, 2, 3], [2, 3, 4], [1, 6, 8]],4, 7))
    
    
