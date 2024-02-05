# <Quan Nguyen>
# <nguy4658@umn.edu>
# CSCI 1133 Section <070>
# rod

userinput = int(input("please type the size of the rod in feets between from 1-99: "))
twentyfivefeet = userinput//25
tenfeet = (userinput - (twentyfivefeet * 25))//10
fivefeet = (userinput-((twentyfivefeet * 25)+(tenfeet * 10)))//5
onefoot = (userinput-(((twentyfivefeet * 25)+(tenfeet * 10))+fivefeet*5))
print(twentyfivefeet, "rods each of 25 feet")
print(tenfeet, "rods each of 10 feet")
print(fivefeet, "rods each of 5 feet")
print(onefoot, "rods each of 1 foot")
