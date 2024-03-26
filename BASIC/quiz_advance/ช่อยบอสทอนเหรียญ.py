if __name__ == "__main__":
    coin = {
        '1':0,
        '3':0,
        '4':0
    }
    
    change = int(input("Enter change: "))
    
    while change != 0:
        if change == 6:
            coin['3'] += 2
            change = change - 6
        elif change >= 4:
            coin['4'] += 1
            change = change - 4 
        
        elif change >= 3:
            coin['3'] += 1
            change = change - 3
        
        elif change >= 1:
            coin['1'] += 1
            change = change - 1 
    
    minimum_coin = 0
    for key, value in coin.items():
        minimum_coin += value 
    
    print("The minimum coin is {}".format(minimum_coin))
    