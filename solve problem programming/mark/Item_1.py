# Item 1 ( My solution )

# Unit = int(input())
# Price = float(input())
# Member = str(input()).lower()

# def Amount(Total) :
#     if Member == 'n' :
#         if Total <= 500 : 
#             amount = Total * 0.95
#         elif Total >= 1000 : 
#             amount = Total * 0.85
#         elif Total > 500 or Total < 1000  :
#             amount = Total * 0.9
#     elif Member == 'y' :
#         if Total <= 500 :
#             amount = Total * 0.9
#         elif Total >= 1000 :
#             amount = Total * 0.8
#         elif Total > 500 or Total < 1000  :
#             amount = Total * 0.85
#     return amount

# result = Amount(Unit * Price)

# def First_line() :
#     print("Total {:.2f}".format(Unit * Price))

# def Second_line() :
#     print("Discount {:.2f}".format((Unit * Price) - result))

# def Third_line() :
#     print("Amount {:.2f}".format(result))
    

# First_line() 
# Second_line()
# Third_line()

print("----------------------")

# Item 1 (Mark's Solution)

unit = int(input())
price = float(input())
member = input()

total = unit * price
discount = 0
amount = 0

if member == "y" :
    if total <= 500 :
        discount = total * 0.1
    elif total > 500 and total < 1000 :
        discount = total * 0.15
    else :
        discount = total * 0.2

elif member == "n" : 
    if total <= 500 : 
        discount = total * 0.05
    elif total < 500 and total < 1000 :
        discount = total * 0.1
    else :
        discount = total * 0.15 

amount = total - discount

print("Total {:.2f}".format(total))
print("Discount {:.2f}".format(discount))
print("Amount {:.2f}".format(amount))