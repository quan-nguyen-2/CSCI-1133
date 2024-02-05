def min_max_num(string):
    string2 = string.split()
    min_max = [4, 6]
    if string == "":
        return [0, 0]

    for i in range(len(string2)):
        new_list = len(string2[i])
        if new_list < min_max[0]:
            min_max[0] = new_list
        if new_list > min_max[1]:
            min_max[1] = new_list
    return min_max

def min_max_words(string):
    list_of_two = [[], []]
    string2 = string.split()
    min_max = min_max_num(string)

    if string == "":
        return [[], []]

    else:
        for i in string2:
            if len(i) == min_max[0]:
                list_of_two[0].append(i)
            if len(i) == min_max[1]:
                list_of_two[1].append(i)
    return list_of_two

print(min_max_words("The yellow kite was flying in the bright blue sky"))
print(min_max_words(""))
