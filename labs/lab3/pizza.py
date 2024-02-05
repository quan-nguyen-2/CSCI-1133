userinput = str(input("please type what kind of size pizza do you want large or small? "))
crust = str(input("please type what kind of crust do you want thin or thick? "))

if userinput == "small":
    areapizza = 3.14 * 6 ** 2


if userinput == "large":
    areapizza = 3.14 * 10 ** 2

if crust == "thin":
    price = 1.25 * (0.25 * areapizza)            

if crust == "thick":

    price = 1.25 * (0.50 * areapizza)
            

print("Price of the pizza is: ", price)
