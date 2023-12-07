import random
import time

# same_number = list()
# rand_number = list()
# number = list()
# for i in range(0,10) :
#     rand_num = random.randint(0,20)
#     rand_number.append(rand_num)
#     if rand_num in number :
#         same_number.append(rand_num)
#         continue
#     else :
#         number.append(rand_num)

# print(rand_number)
# print(number)
# print(same_number)

print('---------------------------------')


# mul = int(input("Enter multiplier : "))
# counter = 1
# while counter < 13 :
#     result = counter * mul
#     print("{} x {} = {}".format(mul,counter,result))
#     counter += 1

print('---------------------------------')

# mul = int(input("Enter multiplier : "))
# counter = 1
# while True :
#     result = mul * counter
#     print("{} x {} = {}".format(mul,counter,result))
#     if counter < 12 :
#         counter += 1
#     else :
#         break

print('---------------------------------')

# rand_num = random.randint(1,100)
# counter = 1
# while counter <= 10 :
#     user = int(input("Enter a number #{} : ".format(counter)))
#     counter += 1
#     if user == rand_num :
#         print("----- You win -----")
#     else :
#         print("False")

# print("The correct answer is {}".format(rand_num))

print('---------------------------------')

# mul = int(input("Enter multiplier : "))
# for i in range(1,13) :
#     result = mul * i
#     print("{} x {} = {}".format(mul,i,result))
#     time.sleep(0.5)

print('---------------------------------')

# num = int(input("Enter number : "))

# fac = 1
# for i in range(num,0,-1) :
#     fac *= i

# print("{}! = {}".format(num,fac))

print('---------------------------------')

# import string

# choice = input("Choose between Encrypt or Decrypt : ")
# user_text = input("Enter your text : ")
# answer = ''

# uppper = string.ascii_uppercase
# lower = string.ascii_lowercase

# for i in user_text :
#     if i.isupper() :
#         if choice == 'Encrypt' :
#             answer += uppper[(uppper.index(i)+13) % 26]
#         elif choice == 'Decrypt' :
#             answer += uppper[(uppper.index(i)-13) % 26]

#     elif i.islower() :
#         if choice == 'Encrypt' :
#             answer += lower[(lower.index(i)+13) % 26]
#         elif choice == 'Decrypt' :
#             answer += lower[(lower.index(i)-13) % 26]

#     else :
#         answer += i

# print(answer)

print('---------------------------------')

rand_num = random.randint(1,50)

for i in range(1,11):
    user = int(input("Enter your number#{} : ".format(i)))
    if user == rand_num :
        print("You win , congratulation!")
        break
    else :
        print("Sorry , try it again")

print("The correct answer is {}".format(rand_num))
    
