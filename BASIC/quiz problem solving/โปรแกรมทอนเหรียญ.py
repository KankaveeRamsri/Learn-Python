# print("Kanom Machine")
# print("  1. Khanom Jak        7 Baht")
# print("  2. Khanom Kruy      13 ฺBaht")
# print("  3. Khanom Keemod     9 Baht")
# print("  4. Khanom Co         3 Baht")
# print("  5. Khanom Dokdon    22 Baht")

# kanom_dict = {
#     '1': 7 ,    # Khanom Jak
#     '2': 13 ,   # Khanom Kruy
#     '3': 9 ,    # Khanom Keemod
#     '4': 3 ,    # Khanom Co
#     '5': 22     # Khanom Dokdon
# }

# order = str(input("Enter your order: "))
# quality = int(input("Enter quality: "))
# total = kanom_dict[order] * quality
# print("Total: {} baht".format(total))

# money_left = total

# while money_left > 0:
#     user_money = int(input("Enter your money: "))
    
#     if user_money >= money_left:
#         if user_money == money_left :
#             change = user_money - money_left
#             break
        
#         else :
#             change = user_money - money_left
#             print(f"Change: {change} Baht")
#             break
    
#     else:
#         money_left -= user_money
#         print(f"{money_left} Baht left.")

# coin_dict = {}
# coin_change = change

# while coin_change > 0 :
#     if coin_change >= 10 :
#         coin = '10'
#         if coin in coin_dict.keys():
#             coin_dict[coin] += 1
#         else :
#             coin_dict[coin] = 1
#         coin_change -= 10

#     elif coin_change >= 5 :
#         coin = '5'
#         if coin in coin_dict.keys():
#             coin_dict[coin] += 1
#         else :
#             coin_dict[coin] = 1
#         coin_change -= 5 

#     elif coin_change >= 2 :
#         coin = '2' 
#         if coin in coin_dict.keys():
#             coin_dict[coin] += 1
#         else :
#             coin_dict[coin] = 1
#         coin_change -= 2 

#     elif coin_change == 1 :
#         coin = '1'
#         if coin in coin_dict.keys():
#             coin_dict[coin] += 1
#         else :
#             coin_dict[coin] = 1
#         coin_change -= 1
    
#     elif coin_change == 0 :
#         break

# for key, values in coin_dict.items():
#     if values > 1:
#         print("  ",f"{int(key)}:",'{} coins'.format(values)) 
#     elif values == 1:
#         print("  ",f"{int(key)}:",'{} coin'.format(values)) 
       
# print("Thank you")
        
print("------------------------------------")

# Method (P'Boat)

if __name__ == "__main__":
    coins = [7,13,9,3,22]
    kanoms = ["Jak", "Kruy", "Keemod", "Co", "Dokdon"]
    
    print('Kanom Machine')
    for i, name in enumerate(kanoms): # list มาพร้อมกับ index 
        print(f" {i+1}. Khanom {name:10} {coins[i]:>20} Bath")
    
    order_item = int(input("Enter your order: "))
    order_quantity = int(input("Enter Quantity: "))
    
    total = coins[order_item-1] * order_quantity
    print(f"Total: {total} Baht")
    
    money = 0
    diff = 0
    while money <= total:
        money += int(input("Enter your money: "))
        diff = money - total 
        if diff < 0:
            print(f" {-1*diff} Baht left ")
            
    change = dict()
    if diff > 0:
        change_coins = [10,5,2,1]
        sub_diff = diff
        for i in change_coins:
            num = sub_diff // i
            if num == 0:
                continue
            
            change[i] = num
            sub_diff = sub_diff % i 
            if sub_diff <= 0:
                break
        
        print(f'Change: {diff} baht')
        for k, v in change.items():
            coin_text = "coins" if v > 1 else "coin"
            print(f'   {k}: {v} {coin_text}')
        
            
    
    print("Thank you")