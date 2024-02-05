from random import randint
def open_csv(filename):
    f = open(filename, "a")
    for i in range (100):
        f.write(f"{randint(-1000,1000)},{randint(-1000,1000)},\n")
    f.close()
    
open_csv("open2.csv")

