# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# seven_stories

import os

def clean():
    return_list = []
    pathname = os.path.join("hw4_supplements", "short_stroies.txt")
    with open(pathname, 'r', encoding='utf-8') as original_file:
        for line in original_file:
            if line == "":
                pass
            elif len(line) < 4:
                pass
            else:
                new_str =""
                for chat in line:
                    if char.isalpha() or char =="":
                        new_str += char.lower()
                return_list.append(new_str)
    return return_list
def count_sevens(story):
    count = 0
    for i in range(len(story)):
        words = story[i].split("")
        for word in words:
            if word == "seven":
                count += 1
    return count

print(count_sevens(clean()))
