# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# cat_count

def cat_count(n):
    if n == 1 or n == 2 or n == 3:
        return 1
    else:
        return cat_count(n - 1) + cat_count(n - 3)

def custom_cat_count(n, init, prod_year, num_cats):
    if n < prod_year:
        return init
    else:
        return custom_cat_count(n-1,init,prod_year, num_cats) + (custom_cat_count(n-prod_year +1,init,prod_year, num_cats)*num_cats)

print(custom_cat_count(23, 1, 3, 1))
print(cat_count(25))
