# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# ginger_number

def is_ginger_number(n):
    while n >= 0:
        if n % 2 == 0:
            n /= 2
        elif n % 3 == 0:
            n /= 3
        elif n % 5 == 0:
            n /= 5
        elif n % 7 == 0:
            n /= 7
        elif n ==1:
            return True
        else:
            return False
print(is_ginger_number(98))
