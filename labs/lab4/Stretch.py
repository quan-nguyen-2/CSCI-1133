import random
userinput = str(input("Would you like to go first (y/n)? "))
objects = 21

if userinput == "y":
    while objects > 0:
        
        userinput2 = float(input("type how many objects you want to take 1,2,3: "))
        Num = userinput2
        objects = objects - Num
        if objects <= 0:
            print("you win")
            break
            
        Num2 = random.randint(1,3)
        print(objects, "objects remain, I'll take", Num2)
        objects = objects - Num2
        if objects <= 0:
            print("your opponent won")
            break
        print(objects, "objects remain")
        
if userinput == "n":
    while objects > 0:
        Num2 = random.randint(1,3)
        print(objects, "objects remain, I'll take", Num2)
        objects = objects - Num2
        if objects <= 0:
            print("your opponent win")
            break
        print(objects, "objects remain")

        userinput2 = float(input("type how many objects you want to take 1,2,3: "))
        Num = userinput2
        objects = objects - Num
        if objects <= 0:
            print("you win")
            break
