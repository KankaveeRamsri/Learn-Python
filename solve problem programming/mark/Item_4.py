# Item 4 ( My Solution )

# user = [int(_) for _ in input().split()]
# number = int(input())
# x = user[0]
# y = user[1]

# def solution() :
#     if number == 1 :
#         print('{:.5f}'.format(x + y))
#     elif number == 2 :
#         print('{:.5f}'.format(x - y))
#     elif number == 3 :
#         print('{:.5f}'.format(x * y))
#     elif number == 4 :
#         print('{:.5f}'.format(x / y))
#     elif number == 5 : 
#         print(x % y)
#     elif number == 6 :
#         print('{:.5f}'.format(x ** y))
#     elif number == 7 :
#         print('{:.5f}'.format(sum(user)/len(user)))
#     else :
#         print('Error')

# solution()

print("----------------------")

# Item 4 ( Mark's Solution )

n1 , n2 = [int(_) for _ in input().split()]
option = int(input())
result = 0

if option == 1 :
    result = n1 + n2 

elif option == 2 :
    result = n1 - n2 

elif option == 3 :
    result = n1 * n2 

elif option == 4 :
    result = n1 / n2 

elif option == 5 :
    result = n1 % n2 

elif option == 6 :
    result = n1 ** n2 

elif option == 7 :
    result = (n1 + n2) / 2

else :
    print("Error")

if option != 5 :
    print("{:.5f}".format(result))

else : 
    print(result)
