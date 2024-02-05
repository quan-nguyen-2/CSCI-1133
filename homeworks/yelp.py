# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# yelp

import os

def load_yelp():
    pathname = os.path.join("hw4_supplements", "yelp.csv")
    with open(pathname, 'r', encoding ='utf-8') as full_dataset:
        with open("mini-yelp.csv", 'w') as new_dataset:
            for line in full_dataset:
                line = line.split(",")
                if line[3] == "Restaurants":
                    new_dataset.write(",".join(line))
def get_state_count(state):
    count = 0
    with open("mini-yelp.csv",'r') as dataset:
        for line in dataset:
            line = line.split(",")
            if line[8] == state:
                count += 1
    return count
print(get_state_count("MN"))
print(get_state_count("AZ"))
