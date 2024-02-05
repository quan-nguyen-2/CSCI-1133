def flat_deep_square(lst):
    if len(lst) == 0:
        return lst
    elif type(lst[0]) is int:
        return [(lst[0]**2)] + flat_deep_square(lst[1:])
    else:
        return flat_deep_square(lst[0]) + flat_deep_square(lst[1:])
        
print(flat_deep_square([[-1,[2],[3],[[[-4,5]]],[],[]]]))
