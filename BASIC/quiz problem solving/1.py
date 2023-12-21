def display_menu():
    print("Kanom Machine")
    print("  1. Khanom Jak        7 Baht")
    print("  2. Khanom Kruy       13 Baht")
    print("  3. Khanom Keemod     9 Baht")
    print("  4. Khanom Co         3 Baht")
    print("  5. Khanom Dokdon     22 Baht")


def get_order():
    kanom_dict = {
        '1': 7,
        '2': 13,
        '3': 9,
        '4': 3,
        '5': 22
    }

    order = input("Enter your order: ")
    quantity = int(input("Enter quantity: "))
    total = kanom_dict[order] * quantity
    print("Total: {} baht".format(total))
    return total


def calculate_change(total):
    money_left = total

    while money_left > 0:
        user_money = int(input("Enter your money: "))
        
        if user_money >= money_left:
            if user_money == money_left:
                change = user_money - money_left
                break
            else:
                change = user_money - money_left
                print(f"Change: {change} Baht")
                break
        
        else:
            money_left -= user_money
            print(f"{money_left} Baht left.")
    return change


def calculate_coins(change):
    coin_dict = {}
    coin_change = change

    while coin_change > 0:
        if coin_change >= 10:
            coin = '10'
        elif coin_change >= 5:
            coin = '5'
        elif coin_change >= 2:
            coin = '2'
        elif coin_change >= 1:
            coin = '1'

        if coin in coin_dict.keys():
            coin_dict[coin] += 1
        else:
            coin_dict[coin] = 1

        coin_change -= int(coin)

    for key, values in coin_dict.items():
        if values > 1:
            print("  ", f"{int(key)}:", '{} coins'.format(values))
        elif values == 1:
            print("  ", f"{int(key)}:", '{} coin'.format(values))


def main():
    display_menu()
    total_cost = get_order()
    change = calculate_change(total_cost)
    calculate_coins(change)
    print("Thank you")


if __name__ == "__main__":
    main()
