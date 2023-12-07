# import string

# print("Select 2 options")
# print(" - 1 encrypt with ROT 13")
# print(" - 2 decrypt with ROT 13")

# option = str(input("Choose option: "))
# text_input = str(input("Enter text: "))

# lower_alpha = string.ascii_lowercase
# upper_alpha = string.ascii_uppercase 

# answer = ""
# for i in text_input :
#     if i.isupper() :
#         if option == '1' :
#             answer += upper_alpha[(upper_alpha.index(i) + 13) % 26]
#         elif option == '2' :
#             answer += upper_alpha[(upper_alpha.index(i) - 13) % 26]
    
#     elif i.islower() :
#         if option == '1' :
#             answer += lower_alpha[(lower_alpha.index(i) + 13) % 26]
#         elif option == '2' :
#             answer += lower_alpha[(lower_alpha.index(i) + 13) % 26]
    
#     else :
#         answer += i

# if option == '1' :
#     print('Cyphertext is "{}"'.format(answer))
# elif option == '2' :
#     print('Plaintext is "{}"'.format(answer))
    
print("----------------------------")

# row = int(input("Enter the number of row: "))

# for i in range(1,row + 1) :
#     print(" " * (row - i),end="")
#     print("*" * i)

print("----------------------------")

# row = int(input("Enter the number of rows: "))

# for i in range(row,0,-1) :
#     print("*" * i)

print("----------------------------")

# row = int(input("Enter the number of rows: "))

# for i in range(row,0,-1) :
#     print(" " * (row - i),end="")
#     print("*" * i)

print("----------------------------")

# ls_num = []
# for i in range(1,21) :
#     number = int(input("Enter number #{}: ".format(i)))
#     if number not in ls_num :
#         ls_num.append(number)

# ls_num.sort()

# unique_num = ""
# for i in ls_num :
#     unique_num += str(i)
#     unique_num += " "

# print("Unique numbers is {}".format(unique_num))

# even_position_ls_num =[]
# for i in range(0,len(ls_num) + 1,2):
#     even_position_ls_num.append(ls_num[i])

# average = sum(even_position_ls_num) / len(even_position_ls_num)

# print("Average number of even position in list is {:.2f}".format(average))
    
print("----------------------------")

# import string

# lower_alpha = {}

# while True :
#     text_input = str(input("Enter string: "))
#     if text_input == 'end' :
#         break
#     text_input.lower()
#     for s in text_input :
#         if s in string.ascii_lowercase :
#             if s in lower_alpha.keys() :
#                 lower_alpha[s] += 1
#             else :
#                 lower_alpha[s] = 1 

# lower_alpha_sorted = dict(sorted(lower_alpha.items()))

# for key , value in lower_alpha_sorted.items() :
#     print(key, value)

print("----------------------------")

# row = int(input())
# symbol = str(input())

# for i in range(row) :
#     result = ' ' * (row - i - 1) + symbol * (i * 2 + 1)
#     print(result)

print("----------------------------")

# row = int(input())
# symbol = str(input())

# for i in range(row) :
#     result = ' ' * i + symbol * ((row - i) * 2 - 1)
#     print(result)

print("----------------------------")

# number = int(input("Enter number : "))

# base2 = ""
# base10 = number 

# while base10 > 0 :
#     frac = int(base10 % 2)
#     base2 = str(frac) + base2 
#     base10 = (base10 - frac) / 2

# print(base2)

print("----------------------------")


        