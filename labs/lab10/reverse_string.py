def reverse_string(str):
    if str == "":
        return str
    else:
        return reverse_string(str[1: ]) + str[0]
    

print(reverse_string("olleh"))
