def get_greatDay(date,great_number):
    great_day = 0
    for day in range(date[0],date[1] + 1):
        if (day - int((str(day))[::-1])) % great_number == 0:
            great_day += 1
    return great_day

if __name__ == "__main__":
    date = [int(i) for i in input("Date: ").split()]
    great_number = int(input("Great Number: "))
    
    print("Great Days:",get_greatDay(date,great_number))
    