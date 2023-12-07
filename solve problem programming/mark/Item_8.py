# Item 8 ( My solution )

year = int(input())

if year < 1582 :
    if year % 4 == 0 :
        print("{} is a leap year".format(year))
    else :
        print("{} is not a leap year".format(year))

else :
    if year % 100 == 0 :
        if year % 400 == 0 :
            print("{} is a leap year".format(year))
        else :
            print("{} is not a leap year".format(year))
    
    
    elif year % 4 == 0 :
        print("{} is a leap year".format(year))
    
    else :
        print("{} is not a leap year".format(year))