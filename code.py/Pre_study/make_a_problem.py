# lang = str(input("Select languages :"))
# list_lang  = lang.split() #แยกคำไปอยู่ใน lists
# # print(list_lang)

# if len(list_lang) < 3 :
#     print("Wrong input")
# else :
#     print(list_lang)
#     name = input('Enter your name : ')
#     lan = int(input('Enter lang you like :'))
#     print(f"{name} love {list_lang[lan-1]}.") #ตำแหน่งลบไป 1


print("-----------------------------")

# def area(width , length): #รับ parameter
#     return width*length

# w = float(input("Select width : "))
# h = float(input("Select length : "))
# result = area(w,h)
# print("A value is " , result)

print("-----------------------------")

# def area() : #ไม่รับ parameter
#     w = float(input("Select width : "))
#     h = float(input("Select length : "))
#     return w * h

# print('A value is ',area())


print("-----------------------------")

# def area(width , length):
#     print(width*length)

# w = float(input("Select width : "))
# l = float(input("Select length : "))
# area(w,l)  #ไม่ต้อง return ค่า แต่จะเอาค่าไปใช้ใน func อื่นไม่ได้

print("-----------------------------")

# class Sqare :
#     def __init__(self,width) :
#         self.width = width
    
#     def area(self) :
#         return self.width * self.width

#     def perimeter(self) :
#         return 4 * self.width


# w = Sqare(int(input("Enter num : ")))
# print("A value is",w.area())
# print("A value is",w.perimeter())

print("-----------------------------")

# data = []
# while True :
#     num = int(input("Enter num :"))
#     if num < 0 :
#         break
#     else :
#         data.append(num)
#         data.sort()

# print(data)
# print(len(data))
# print(f"Minimum is {min(data)}")
# print(f"Maximum is {max(data)}")

# avg = sum(data)/len(data)
# print("A result of avg is",avg)

print("-----------------------------")

# data = input("Enter data :")
# width = int(input("Enter width :"))

# stop = 0
# ans = ""
# for i in range(len(data)) :
#     # print(data[i]) #ตำแหน่ง i ใน data
#     if stop == width :
#         stop = 0
#         ans = ans + "\n"
#     ans += data[i]
#     stop += 1
    
# print(ans)

print("-----------------------------")

# dis1 = float(input("Select distance cat_1: "))
# dis2 = float(input("Select distance cat_2: "))
# dis3 = float(input("Select distance mouse: "))

# a = abs(dis3 - dis1)
# b = abs(dis3 - dis2)

# if dis1 == dis2 :
#     print("Mouse")

# elif a < b :
#     print("cat_1")

# elif a > b :
#     print("cat_2")

print("-----------------------------")

# def distance(dis1 ,dis2 ,dis3):
#     if dis1 == dis2 :
#         print("Mouse")
#     elif abs(dis3-dis1) < abs(dis3-dis2) :
#         print("cat_1")
#     else :

#         print("cat_2")

# d1 = float(input("Select distance cat_1 : "))
# d2 = float(input("Select distance cat_2 : "))
# d3 = float(input("Select distance mouse : "))
# distance(d1,d2,d3)

print("-----------------------------")

# def distance(dis1 ,dis2 ,dis3):
#     if dis1 == dis2 :
#         return "Mouse"
#     elif abs(dis3-dis1) < abs(dis3-dis2) :
#         return "cat_1"
#     else :
#         return "cat_2"
        

# d1 = float(input("Select distance cat_1 : "))
# d2 = float(input("Select distance cat_2 : "))
# d3 = float(input("Select distance mouse : "))
# print(distance(d1,d2,d3))

print("-----------------------------")

change = int(input("Your change : "))
data = []
coin = 0
while change > 0 :
    if change == 6 :
        change -= 6 # 3 bath 2 coins
        data.extend([3,3])
        coin += 2
    elif change > 4:
        change -= 4
        data.append(4)
        coin +=1
    elif change > 3 :
        change -= 3
        data.append(3)
        coin += 1
    elif change >= 1 :
        change -= 1
        data.append(1)
        coin += 1

print(data)
print(coin)

print("-----------------------------")

# import string
# select = input("Select Encrypt or Decrypt :").lower()

# a = string.ascii_lowercase + string.ascii_lowercase[:13]

# if select == 'a' :
#     user = input("Enter your word :")
#     for i in user :
#         # print(i)   #มีตัวไรบ้างที่อยู่ใน user ให้มาเก็บไว้ในตัวแปร i
#         # print(a.find(i))  #หาตำแหน่งของ i ในตัวแปร a
#         print(a[a.find(i)+13]) #บวกตำแหน่งจากตัวแรก ไปอีก 13
#         if i.isdigit() :
#             print(i)

# ยังไม่เสดดดดดดด

print("-----------------------------")

# import string

# choices = input('yes 1 or no 2 : ')
# text = input('Enter your text : ')

# lower = string.ascii_lowercase
# uppper = string.ascii_uppercase
# answer = '' #เก็บไว้ใน form 

# for i in text : 
#     if i.isupper() :
#         if choices == '1' :
#             answer += uppper[(uppper.index(i)+13) % 26]
#         elif choices == '2' :
#             answer += uppper[(uppper.index(i)-13) % 26]
    
#     elif i.islower() :
#         if choices == '1' :
#             answer += lower[(lower.index(i)+13) % 26]
#         elif choices == '2' :
#             answer += lower[(lower.index(i)-13) % 26]
    
#     else :
#         answer += i
    
# print(answer)

print("-----------------------------")

import string

choices = input('yes 1 or no 2 : ')
text = input('Enter your text : ')

lower = string.ascii_lowercase
uppper = string.ascii_uppercase
answer = []  #เก็บไว้ใน form list

for i in text : 
    if i.isupper() :
        if choices == '1' :
            answer.append(uppper[(uppper.index(i)+13) % 26])
        elif choices == '2' :
            answer.append(uppper[(uppper.index(i)-13) % 26])
    
    elif i.islower() :
        if choices == '1' :
            answer.append(lower[(lower.index(i)+13) % 26])
        elif choices == '2' :
            answer.append(lower[(lower.index(i)-13) % 26])
   
    else :
        answer.append(i)
    
print(answer)

print("-----------------------------")


# data = []
# new_data = []
# new_data_even = []

# count = 1
# while True :
#     num = float(input("Enter num 20 unit #{}:".format(count)))
#     data.append(num)
#     if count == 20 :
#         break
#     count += 1
# print(num)
# print(data)
# data.sort()
# print(data)

# for i in range(len(data)) :
#     if data[i] not in new_data : 
#         new_data.append(data[i])
# print(new_data)

# for x in range(len(new_data)):
#     if x % 2 == 0 :
#         new_data_even.append(new_data[x])
# print(new_data_even)

# result = sum(new_data_even) / len(new_data_even)
# print("A value is {:.3f}".format(result))

print("-----------------------------")

# import random

# def count(good,price) :
#     if good == 'food' :
#         return price * 0.97
#     elif good == 'medicine' : 
#         return price * 0.99
#     elif good == 'shoes' :
#         return price * 0.8
#     else :
#         return price
    
# merchandise = input("Select goods :")
# a = random.randint(100,1000)
# print("Price are",a)
# result = count(merchandise,a)
# print(f"a result is {result}")


print("-----------------------------")


# def increase(a):
#     for i in range(10) :
#         a = a + 1
        
#     return a

# a = 10
# b = increase(a)
# print(b)

print("-----------------------------")

# sum_num1 = []
# for i in range(1,10):
#     sum_num1.append(i)
# print(sum_num1)
# print(sum(sum_num1))

print("-----------------------------")

# data = []
# i = 0
# sum = 0

# while i <= 9 :
#     i += 1
#     data.append(i)
#     sum = sum + i 

# print(data)
# print(sum)

print("-----------------------------")

# a = float(input("Select number : "))
# b = float(input("Select number : "))

# if a < 0 :
#     print("กรุณากรอกเป็นจำนวนเต็มบวก")

# elif b < 0 :
#     print("กรุณากรอกเป็นจำนวนเต็มบวก")

# else :
#     result = a * b
#     print("A value of area is {:.2f}".format(result))

print("-----------------------------")

# data = []
# i = 0
# while i < 20 :
#     i += 1
#     # print(i)
#     data.append(i)
   
   

# print(data)

print("-----------------------------")

# data = []
# for i in range(1,21) :
#     data.append(i)

# print(data)

print("-----------------------------")

# data = []
# result = 1
# for i in range(0,10) :
#     i += 1
#     # print(i)
#     data.append(i)
#     result *= i


# print(data)
# print(result)

print("-----------------------------")

# usd = float(input("Enter your money : "))

# if usd < 0 :
#     print("You don't have money.")
# else :
#     result = usd * 32.5

#     print(result)

print("-----------------------------")

# hour = int(input("Enter hour(s) : "))
# minute = int(input("Enter minute(s) : "))

# if hour < 0 or minute < 0 :
#         print("--- โปรดใส่ข้อมูลที่ไม่ติดลบ ---")

# else :
#     if minute > 0 :
#         hour = hour + 1
    
#     pay = (hour - 1) * 30
#     print(pay)

print("-----------------------------")

