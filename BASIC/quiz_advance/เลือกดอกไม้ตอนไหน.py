if __name__ == '__main__':
    a = [int(i) for i in input().split()]
    number_flowers = a[0]
    money = a[1]
    price = sorted([int(i) for i in input().split()[:number_flowers]])
    print(price)
    
    total_price = 0
    
    flowers = []
    count_flower = 0

    for x in range(number_flowers):
        flowers.append(False)
    
    for i in range(number_flowers):
        if total_price + price[i] <= money:
            count_flower += 1
            total_price += price[i]
            flowers[i] = True
    
    print(count_flower)
    
    
    
        
        
        
        
    
    
    
    
    
        