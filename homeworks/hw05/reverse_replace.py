# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# reverse_replace

def reverse_replace(txt, dict):
    if len(txt) == 0:
        return ""
    temp = txt[0]
    if temp in dict:
        temp = dict[temp]

    return reverse_replace(txt[1:], dict) + temp

print(reverse_replace('glue', {'l':'t', 't':'l'}))
