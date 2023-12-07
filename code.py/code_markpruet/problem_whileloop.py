#1
# i = 1
# while i <=15 :
#     print(i)
#     i += 2

print(" ---------------------------- ")

#2
# i = 2
# while i <=17 :
#     print(i)
#     i += 3

print(" ---------------------------- ")

#3
# i = 30
# while i >= -30 :
#     print(i)
#     i -= 10

print(" ---------------------------- ")

#4
# i = 15
# while i <= 55 :
#     print(i)
#     i += 8

print(" ---------------------------- ")

#5
# i = 0
# while i <= 100 :
#     print(i)
#     i += 1

print(" ---------------------------- ")

#6
# num = int(input())
# i = 0

# while i <= num :
#     print(i)
#     i += 1

print(" ---------------------------- ")

#7

# i = 100
# while i >= 0 :
#     print(i)
#     i -= 1

print(" ---------------------------- ")

#8

# num = int(input())
# i = num 

# while i >= 0 :
#     print(i)
#     i -= 1

print(" ---------------------------- ")

#9

# summ = 0
# while True :
#     num = float(input())
#     if num < 0 :
#         break
#     summ += num
# print(summ)

print(" ---------------------------- ")

#10

# count1 = 0
# count2 = 0

# while True :
#     num = float(input())
#     if num == 0 :
#         break
#     else :
#         if num > 0 : 
#             count1 += 1
#         elif num < 0 :
#             count2 += 1

# print(count1)
# print(count2)

print(" ---------------------------- ")

#11

# summ = 0
# count = 0

# while True :
#     num = float(input())
#     if num < 0 :
#         break
#     else :
#        
#         summ += num

# print(summ)
# print(count)
# print(summ/count)

print(" ---------------------------- ")

#12

# data = []
# while True :
#     num = float(input())
#     if num < 0 :
#         break
#     else :
#         data.append(num)

# print(data)
# print(max(data))

print(" ---------------------------- ")

#13

# data = []
# while True :
#     num = float(input())
#     if num < 0 :
#         break
#     else :
#         data.append(num)

# print(data)
# print(min(data))

print(" ---------------------------- ")

#14

# data = []
# while True :
#     num = float(input())
#     if num < 0 :
#         break
#     else :
#         data.append(num)
#         result = max(data) - min(data)
        
# print(result)

print(" ---------------------------- ")

#15

# summ = 0
# while True :
#     num = int(input())
#     if num == -1 : 
#         break
#     else :
#         summ += num
    
# print(summ)

print(" ---------------------------- ")

#16

# num = int(input())
# if num < 0 :
#     print("Error")
# else :
#     i = num 
#     while i > 0 :
#         a = i % 10
#         print(a)
#         i = i // 10


print(" ---------------------------- ")

#17

# count = 0
# while True :
#     num = int(input())
#     if num < 0 :
#         break
#     else :
#         if num % 2 != 0 :
#             count += 1

# print("Received {} odd numbers ".format(count))

print(" ---------------------------- ")

#18

# num = int(input())
# summ = 0
# i = num
# while i > 0 :
#     a = i % 10
#     summ += a  #ตัดหลักให้เหลือหลักเดียว
#     i //= 10
# # print(summ)
# if summ % 9 == 0 :
#     print("Yes {}".format(summ))
# elif summ % 9 != 0 :
#     print("No {}".format(num % 9))

print(" ---------------------------- ")


#19

# count = 0
# target = 72
# while True :
#     num = int(input("Enter your guess : "))
#     count += 1
#     if num < 0 or num > 100 :
#         print("Sorry,your guess is out of range.")
#     elif num < target :
#         print("Sorry,your guess is too low.")       
#     elif num > target :
#         print("Sorry,your guess is too high.")       
#     elif num == target :
#         print("Congratulations , your guess is correct.") 
#         print(f"Total number of guesses is {count}")
#         break


print(" ---------------------------- ")

#20

# high = 0
# count = 0
# while True :
#     num = int(input())
#     if num == -1 :
#         break
#     else :
#        if num > high :
#            high = num
#            count += 1

# print(count)

print(" ---------------------------- ")

#21

# num = int(input())
# i = num
# summ = 0
# while i > 0 :
#     a = i % 10
#     summ += a
#     i //= 10
# print(summ)

# if summ < 10 :
#     print(summ)
# else :
#     while True :
#         if summ < 10 :
#             break
#         else :
#             i = summ
#             summ = 0
#             while i > 0 :
#                 a = i % 10
#                 summ += a
#                 i //= 10
#     print(summ)

print(" ---------------------------- ")

# i = 1
# sum = 0
# while True :
#     if i > 10 :
#         break
#     else :
#         print("Frame #{}".format(i))
#         num1 = int(input("Number of pins down : "))
#         sum += num1
#         if num1 == 10 :
#             i += 1 
#         else :
#             print("Frame #{}".format(i))
#             num3 = 10 - num1 
#             num2 = int(input("Number of pins down (0 - {}) : ".format(num3)))          
#             i += 1
#             sum += num2
    

# print("Total score is {}".format(sum))

print(" ---------------------------- ")
    





