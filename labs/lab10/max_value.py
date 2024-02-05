def max_value(lst):
    if len(lst) == 1:
        return lst[0] 
    else:
        if max_value(lst[1: ]) > lst[0]:
            return max_value(lst[1:])
        else:
            return lst[0]
    

print(max_value([10,50,40,30,100]))
