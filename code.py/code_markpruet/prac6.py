# i = 0
# while i <= 10 :
#     if i == 5 :
#         i += 1
#         continue
#     print(i)
#     i += 1

print(" ---------------------------- ")

# while True :
#     n = int(input())
#     if n == -1 :
#         break

print(" ---------------------------- ")

# n = int(input())
# i = n
# sum = 1
# while i >= 1 :
#     sum *= i
#     i -= 1

# print(sum)

print(" ---------------------------- ")

# i = 1
# summ = 0

# while i <= 5 :
#     n = int(input())
#     summ += n
#     i += 1

# print(summ)

print(" ---------------------------- ")

# i = 1
# while i <= 5 :
#     print("Round : {}".format(i))
#     j = 1
#     while j <= 3 :
#         print(j)
#         j += 1
#     i += 1

print(" ---------------------------- ")

import random

i = 1
bot = random.randint(1,100)

while i <= 10 :
    num = int(input("Select your number #{} : ".format(i)))
    if num == bot :
        print("You win.")
        print(bot)
        break
    i += 1
    
else :
    print(bot) 
    print("You loose , try it later.")

print(" ---------------------------- ")

    
    




