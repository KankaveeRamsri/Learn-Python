date = input("Enter date : ")

year = int(date) // 10000
day = int(date) % 100
month = int(date[4:6])


if len(date) != 8 :
    print("Error")

elif day <= 9 and month <= 9 :
    print("0{}-0{}-{:4d}".format(day,month,year))

elif day >= 1 and day <= 9 :
    print("0{}-{:2d}-{:4d}".format(day,month,year))

elif month >= 1 and month <= 9 :
    print("{:2d}-0{}-{:4d}".format(day,month,year))

else :
    print("{:2d}-{:2d}-{:4d}".format(day,month,year))