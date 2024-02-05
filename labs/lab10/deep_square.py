def deep_square(lst):
    if len(lst) == 0:
        return lst
    elif type(lst[0]) is int:
        return [(lst[0]**2)] + deep_square(lst[1:])
    else:
        return [deep_square(lst[0])] + deep_square(lst[1:])
        
print(deep_square([[-1,[2],[3],[[[-4,5]]],[],[]]]))
