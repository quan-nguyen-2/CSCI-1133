# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# name_generator

def name_generator(adjective, name):
    if adjective == [] or name == []:
        print('No name to print')
    else:
        output_lst = []
        for current_adj in adjective:
            for current_name in name:
                output_lst.append(current_adj + " " + current_name)
        return output_lst

print(name_generator(['Fluffy', 'Sour', 'Grumpy'], ['Bob', 'Tim', 'Eren']))
print(name_generator([], []))
