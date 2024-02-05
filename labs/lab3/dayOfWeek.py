def main():
    month = int(input("enter month: "))
    day = int(input("enter day: "))
    year = int(input("enter year: "))

    if month == 1:
        zyear = year - 1
        zmonth = month + 12
    elif month == 2:
        zyear = year -1
        zmonth = month +12
    else:
        zyear = year
        zmonth = month

    dayofweek = day
    dayofweek += 5
    dayofweek += (26 *(zmonth +1) ) // 10
    dayofweek += (5* (zyear % 100) ) // 4
    dayofweek += (21 * (zyear // 100) ) //4
    dayofweek %= 7

    if dayofweek == 0:
        print(f"{month}/{day}/{year} is a Monday")
    elif dayofweek == 1:
        print(f"{month}/{day}/{year} is a Tuesday")
    elif dayofweek == 2:
        print(f"{month}/{day}/{year} is a Wednesday")
    elif dayofweek == 3:
        print(f"{month}/{day}/{year} is a Thursday")
    elif dayofweek == 4:
        print(f"{month}/{day}/{year} is a Friday")
    elif dayofweek == 5:
        print(f"{month}/{day}/{year} is a Saturday")
    elif dayofweek == 6:
        print(f"{month}/{day}/{year} is a Sunday")

if __name__== '__main__':
    main()
    
