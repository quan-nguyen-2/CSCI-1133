# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# word_enconder


from operator import le
def short_encode(list_of_words):
    string = ""
    for word in list_of_words:
        if len(word) != 1:
            new_string = word[0]+word[len(word)-1]
            string = string + new_string + " "
        else:
            new_string = word[0]
            string = string + new_string + " "

    return string


print(short_encode(['Hello','World']))
