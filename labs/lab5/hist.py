import random
number = 0
listone = []
listtwo = []
listthree = []
listfour = []
listfive = []
listsix = []
listseven = []
listeight = []
listnine = []
listten = []
listeleven = []
listtwelve = []
while number <= 10000:
    number = number + 1
    n = random.randint(1,6)
    n2 = random.randint(1,6)
    n3 = n2 + n
    if n3 == 1:
        listone.append('1')
    elif n3 == 2:
        listtwo.append('1')
    elif n3 == 3:
        listthree.append('1')
    elif n3 == 4:
        listfour.append('1')
    elif n3 == 5:
        listfive.append('1')
    elif n3 == 6:
        listsix.append('1')
    elif n3 == 7:
        listseven.append('1')
    elif n3 == 8:
        listeight.append('1')
    elif n3 == 9:
        listnine.append('1')
    elif n3 == 10:
        listten.append('1')
    elif n3 == 11:
        listeleven.append('1')
    elif n3 == 12:
        listtwelve.append('1')

one = len(listone)
two = len(listtwo)
three = len(listthree)
four = len(listfour)
five = len(listfive)
six = len(listsix)
seven = len(listseven)
eight = len(listeight)
nine = len(listnine)
ten = len(listten)
eleven = len(listeleven)
twelve = len(listtwelve)
print(format(1,"2d"),end="")
print(format(one, "5d"))
print(format(2,"2d"),end="")
print(format(two, "5d"))
print(format(3,"2d"),end="")
print(format(three, "5d"))
print(format(4,"2d"),end="")
print(format(four, "5d"))
print(format(5,"2d"),end="")
print(format(five, "5d"))
print(format(6,"2d"),end="")
print(format(six, "5d"))
print(format(7,"2d"),end="")
print(format(seven, "5d"))
print(format(8,"2d"),end="")
print(format(eight, "5d"))
print(format(9,"2d"),end="")
print(format(nine, "5d"))
print(format(10,"2d"),end="")
print(format(ten, "5d"))
print(format(11,"2d"),end="")
print(format(eleven, "5d"))
print(format(12,"2d"),end="")
print(format(twelve, "5d"))


   
