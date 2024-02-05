# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# cooking

def createOrder(food_item):
    food_item = food_item.lower()
    if food_item == "burger":
        return ['buns', 'patty', 'lettuce', 'pickles', 'tomato', 'cheese']
    elif food_item == "fries":
        return ["potato", "salt"]
    elif food_item == "panini":
        return ["bread", "ham", "cheese"]
    elif food_item == "salad":
        return["green mix", "ranch", "tomato"]
    else:
        return "Invalid Order"

def gatherIngredients(order_lst):
#check if list is empty
    if not order_lst:
        return "No orders to complete at this time"
    ingredients_list = []
    ingredients_dict = {}
    output_str = ""

    for food_item in order_lst:
        ingredients_list.append(createOrder(food_item))
#converting ingredients to a dict
    for food in ingredients_list:
        for ingredient in food:
            if ingredient in ingredients_dict:
                ingredients_dict[ingredient] = ingredients_dict[ingredient] + 1
            else:
                ingredients_dict[ingredient] = 1
#printing items
    output_str = "you need "
    for item in ingredients_dict:
        output_str += str(ingredients_dict[item]) + ' ' + item + ', '
    return output_str
    
print(gatherIngredients(["burger", "burger", "panini"]))
print(gatherIngredients([]))
