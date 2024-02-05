print("pounds ,ounces , miles, inches, kilos, grams, kilometers, centimeters")
print(" ")
unit = str(input("^ please type what a specific unit you want to use from the list above ^: "))
value = float(input("please type in a value for the unit too: "))

if unit == "pounds":
    total = value * .453
    print(format(total, ".4f")," kilos")


if unit == "ounces":
    total = value * 28.3495
    print(format(total, ".4f")," grams")

if unit == "miles":
    total = value * 1.609
    print(format(total, ".4f")," kilometers")

if unit == "inches":
    total = value * 2.54
    print(format(total, ".4f")," centimeters")

if unit == "kilos":
    total = value * 2.205
    print(format(total, ".4f")," pounds")

if unit == "grams":
    total = value * .0353
    print(format(total, ".4f")," ounces")

if unit == "kilometers":
    total = value * .621371
    print(format(total, ".4f")," miles")

if unit == "centimeters":
    total = value * .393701
    print(format(total, ".4f")," inches")



