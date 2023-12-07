user = (input(" Select number :"))

num = "1234567890"
num_thai ="๑๒๓๔๕๖๗๘๙0"

num1 = num.index(user[0])
print(num1)
num2 = num.index(user[1])
num3 = num.index(user[2])
num4 = num.index(user[3])
num5 = num.index(user[4])

print(" a result is",num_thai[num1] + num_thai[num2] + num_thai[num3] + num_thai[num4] + num_thai[num5] )

print("--------------------")

# import string

# user = input( "Select your 5 alphabets : ")
# user = user.lower()

# # num = "1234567890"
# import string
# lowercase = string.ascii_lowercase
# reverse_lowercase = string.ascii_lowercase[::-1]

# if len(user) != 5 :
#     print("----- alphabet error -----")
# elif user.isdigit() :
#     print("----- alphabet error -----")

# else :
#     alphabet1 = lowercase.index(user[0])
#     alphabet2 = lowercase.index(user[1])
#     alphabet3 = lowercase.index(user[2])
#     alphabet4 = lowercase.index(user[3])
#     alphabet5 = lowercase.index(user[4])
#     print(" a result is",reverse_lowercase[alphabet1] + reverse_lowercase[alphabet2] + 
#           reverse_lowercase[alphabet3] + reverse_lowercase[alphabet4] + reverse_lowercase[alphabet5])

# import random
# import time
# # mul = int(input("Select multiplier : "))
# # for count in range(0,13) :
# #     print(count , "times" , mul , "=" , count*mul)

# mul = int(input(" Select multiplier :"))
# for count in range(12 , 0 , -1):
#     print(count , "times" , mul , "=" , count*mul)
#     if count > 0 : 
#         time.sleep(0.5)


print("--------------------")

# import random
# import time
# # for count in range(0,12) :
# #     print(count)
# #     time.sleep(0.5)

# count = 0
# while count < 6 :
#     count += 1
#     print(count)
#     time.sleep(1)
# else :
#     print("While loop is done")


print("--------------------")

# name = ["Kankavee" , "Peerada" , "Puntawut"]
# import time

# for i in name :
#     print(i)
#     if i is "Kankavee" :
#         for ii in "Kankavee" :
#             print(ii)
#             time.sleep(0.5)

#     if i is "Peerada" :
#         for ii in "Peerada" :
#             print(ii)
#             time.sleep(0.5)

#     if i is "Puntawut" :
#         for ii in "Puntawut" :
#             print(ii)
#             time.sleep(0.5)

# else :
#     print("For loop is done!!!")

print("--------------------")

# import random
# mul = int(input("Enter multiplier :"))

# for i in range(1,13) :
#     print(mul , 'times', i , '=', mul*i)

print("--------------------")

# mul = int(input("Enter multiplier :"))
# count = 0
# while count < 12 :
#     # print(count)
#     count += 1
#     print(mul , 'times', count , '=', mul*count)

print("--------------------")

# import random

# bot = random.randint(0,100)

# for i in range(1,11) :
#     user = int(input("Select your number : "))
#     print(f"{i}.Ans = {user}")
#     if user == bot :
#         print("You win")
#         break
#     else :
#         print("You fail")

# print(bot)

print("--------------------")

# num = int(input())
# i = num

# if num < 0 :
#     print("Error")
# else :
#     while i > 0 :
#         a = i % 10
#         print(a)
#         i = i // 10

print("--------------------")

# count = 0
# while True :
#     num = int(input())
#     if num < 0 :
#         break
#     else :
#         if num %2 != 0 :
#             count += 1

# print(f"Recieved {count} odd numbers")

print("--------------------")

# num = int(input())
# summ = 0  
# i = num
# while i > 0 :
#     a = i % 10
#     summ += a
#     i //= 10
# # print(summ)

# if summ % 9 == 0 :
#     print("Yes {}".format(summ))
# elif summ % 9 != 0 :
#     print("No {}".format(summ % 9))

print("--------------------")

# count = 0
# high = 0
# while True :
#     num = int(input())
#     if num <= 0 :
#         break
#     else :
#         while num > high :
#             high = num
#             count += 1
# print(count)

print("--------------------")

# num = int(input())
# i = num 
# sum = 0
# while i > 0 :
#     a = i % 10
#     sum += a
#     i //= 10

# if sum < 10 :
#     print(sum)
# else :
#     while True :
#         if sum < 10 :
#             break
#         else :
#             i = sum
#             sum = 0 
#             while i > 0 :
#                 b = i % 10
#                 sum += a
#                 i //= 10
#     print(sum)

print("--------------------")

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
#             num3 = 10 - num1
#             num2 = int(input("Number of pins down(0 - {}) :".format(num3)))
#             i += 1
#             sum += num2

# print("Total score is {}".format(sum))

print("--------------------")

# a = "I'm good programming"
# result = ""
# for i in range(len(a)-1 , -1 ,-1):
#     result += a[i]

# print(result)

print("--------------------")

# text = input()
# count = 0
# for i in text :
#     if i in "aeiouAEIOU" :
#         count += 1

# print(count)

print("--------------------")

# text = input()
# count_a = 0
# count_e = 0
# count_i = 0
# count_o = 0
# count_u = 0

# for i in text :
#     if "a" in i :
#         count_a += 1
#     elif "e" in i :
#         count_e += 1
#     elif "i" in i :
#         count_i += 1
#     elif "o" in i :
#         count_o += 1
#     elif "u" in i :
#         count_u += 1


# print(f"a = {count_a}")
# print(f"e = {count_e}")
# print(f"i = {count_i}")
# print(f"o = {count_o}")
# print(f"u = {count_u}")
# total = count_a + count_e + count_i + count_o + count_u
# print(f"Total is {total}")


print("--------------------")

# import random
# name = ['บาส','นาย','ตอง','เดียร์','นัท','เก้า','มิว','เพื่อนตอง']

# for i in range(1,9) :
#     random_name = random.choice(name)
#     if i < 5 :
#         print("Group 1 / {} : {}".format(i,random_name))
#         name.remove(random_name)
#     else :
#         print("Group 2 / {} : {}".format(i,random_name))
#         name.remove(random_name)

print("--------------------")


# print("Enter grade ( A -E ) for each course")

# print("Physics I")
# grade_1 = input("grade : ")
# section_1 = int(input("Section : "))

# print("Math I")
# grade_2 = input("grade : ")
# section_2 = int(input("Section : "))

# print("Chemistry")
# grade_3 = input("grade : ")
# section_3 = int(input("Section : "))

# print("Intro to Computer : ")
# grade_4 = input("grade : ")
# section_4 = int(input("Section : "))

# print("Table tennis")
# grade_5 = input("grade : ")
# section_5 = int(input("Section : "))


# print("\n   GRADE REPORT")
# print("--------------------------------------------------------------------")
# print("#      Course               Section        Credit        Grade ")
# print("--------------------------------------------------------------------")


# if section_1 < 10 :
#     print("{:6}{:24}{:16}{:13}{}".format("1","Physics I",f"0{section_1}","3",grade_1))
# else :
#     print("{:6}{:24}{:16}{:13}{}".format("1","Physics I",f"{section_1}","3",grade_1))

# if section_2 < 10 :
#     print("{:6}{:24}{:16}{:13}{}".format("2","Math I",f"0{section_2}","3",grade_2))
# else :
#     print("{:6}{:24}{:16}{:13}{}".format("2","Math I",f"{section_2}","3",grade_2))

# if section_3 < 10 :
#     print("{:6}{:24}{:16}{:13}{}".format("3","Chemistry",f"0{section_3}","3",grade_3))
# else :
#     print("{:6}{:24}{:16}{:13}{}".format("3","Chemistry",f"{section_3}","3",grade_3))

# if section_4 < 10 :
#     print("{:6}{:24}{:16}{:13}{}".format("4","Intro to Computer",f"0{section_4}","3",grade_4))
# else :
#     print("{:6}{:24}{:16}{:13}{}".format("4","Intro to Computer",f"{section_4}","3",grade_4))

# if section_5 < 10 :
#     print("{:6}{:24}{:16}{:13}{}".format("5","Table tennis",f"0{section_5}","1",grade_5))
# else :
#     print("{:6}{:24}{:16}{:13}{}".format("5","Table tennis",f"{section_5}","1",grade_5))

print("--------------------------------------------------------------------")

# data = "".split()
# while True :
#     num = int(input("Please enter a number (6 digits) : "))
#     if len(str(num)) > 6 :
#         print("Error , try it again !")
    
#     else :     
#         break
        
# data += str(num)
# position = int(input("please select the position (1-6) : "))
# ans = data[len(str(num)) - position]
# print("The digit is {}".format(ans))

print("--------------------------------------------------------------------")

# def rfac(n) :
#     sum = 1
#     for i in range(1,n+1) :
#         sum *= i
    
#     return sum
# print(rfac(5))

print("--------------------------------------------------------------------")

# def rfac(n) :
#     if n < 2 :
#         return 1
    
#     return n * rfac(n-1)


# print(rfac(5))

print("--------------------------------------------------------------------")

# import platform
# x = platform.system()
# print(x)

print("--------------------------------------------------------------------")

# thisdict = {"brand" : "Ford" ,
#             "model" : "Mustang" ,
#             "year" : 1964 }

# print(thisdict)
# print(thisdict.keys())
# print(thisdict.values())

# print(thisdict["brand"])

print("--------------------------------------------------------------------")

# thisdict = {"brand" : "Ford" ,
#             "model" : "Mustang" ,
#             "year" : 1964 ,
#             "year" : 2020 }

# print(thisdict)

print("--------------------------------------------------------------------")

# dict = {}
# for i in range(0,2) :
#     subject = input("Subject : ")
#     grade = input("Grade : ")
#     section = int(input("Section : "))
#     credit = int(input("Credit : "))
#     dict.update({subject : [grade , section , credit]})
#     print("-" * 5)

# print(dict)
# print(dict.keys())

print("--------------------------------------------------------------------")

# num_dict = {"num1" : [1,2,3] , "num2" : [4,5,6] , "num3" : [7,8,9]}

# print(num_dict.values(["num1"]))

print("--------------------------------------------------------------------")


# data = []
# m = int(input("Enter num m : "))
# n = int(input("Enter num n : "))

# if m > n :
#     print("Error")

# elif m < n :
#     for i in range(m , n + 1) :
#     # print(i)
#         data.append(i)

# print(sum(data))

print("--------------------------------------------------------------------")


# m = int(input("Enter num m : "))
# n = int(input("Enter num n : "))
# sum = 0
# i = m
# if m > n :
#     print("Error")

# elif m < n :
#     while i <= n :
#         # print(i)
#         sum += i
#         i += 1
        

# print(sum)


print("--------------------------------------------------------------------")

# import random

# data = {}
# name = ["Bas" , "Dear"]

# for i in range(0,2) :
#     rand_name = random.choice(name)
#     if i < 1 :
#         data.update({'Outline' : rand_name}) 
#         name.remove(rand_name)
    
#     else :
#         data.update({'Essay' : rand_name})

# print(data)

print("--------------------------------------------------------------------")

# class BST : 
#     def __init__(self,key) :
#         self.key = key
#         self.lchild = None
#         self.rchild = None

#     def insert(self,data) :
#         if self.key is None :
#             self.key == data
#             return
#         if self.key == data :
#             return
#         if self.key > data :
#             if self.lchild :  #ถ้ามีข้อมูลอยู่แล้วทำเงื่อนไขนี้
#                 self.lchild.insert(data)
#             else :
#                 self.lchild = BST(data)
#         else :
#              if self.rchild :  #ถ้ามีข้อมูลอยู๋แล้วทำเงื่อนไขนี้
#                 self.rchild.insert(data)
#              else :
#                 self.rchild = BST(data)
    
#     def search(self,data) :
#         if self.key == data :
#             print("Node is found!")
#             return
#         if data < self.key :
#             if self.lchild:
#                 self.lchild.search(data)
#             else :
#                 print("Node is not present in tree!")
#         else :
#             if self.rchild:
#                 self.rchild.search(data)
#             else :
#                 print("Node is not present in tree!")
    
#     def preorder(self) :
#         print(self.key,end = ' ')      #เช็คซ้ายลงเรื่อยๆจากนั้นค่อยขวาขึ้นมา
#         if self.lchild:
#             self.lchild.preorder()
#         if self.rchild:
#             self.rchild.preorder()
    
#     def inorder(self) :
#         if self.lchild:
#             self.lchild.inorder()
#         print(self.key,end= ' ')
#         if self.rchild:
#             self.rchild.inorder()
    
#     def postorder(self) :
#         if self.lchild:
#             self.lchild.postorder()
#         if self.rchild:
#             self.rchild.postorder()
#         print(self.key,end = ' ')
    
#     def delete(self,data) :
#         if self.key is None :
#             print("Tree is empty!")
#             return
#         if data < self.key :
#             if self.lchild:
#                 self.lchild = self.lchild.delete(data)
#             else :
#                 print("Given Node is Not present in the tree!")
#         elif data > self.key :
#             if self.rchild:
#                 self.rchild = self.rchild.delete(data)
#             else :
#                 print("Given Node is Not present in the tree!")
#         else : #delete root node
#             if self.lchild is None :
#                 temp = self.rchild #if lchild is None then return rchild
#                 self = None   
#                 return temp  
#             if self.rchild is None :
#                 temp = self.lchild #if rchild is None then return lchild
#                 self = None
#                 return temp
#             node = self.rchild
#             while node.lchild:
#                 node = node.lchild
#             self.key = node.key
#             self.rchild = self.rchild.delete(node.key)
#         return self
    
#     def min_node(self):
#         current = self
#         while current.lchild:
#             current = current.lchild
#         print("node with smallest key is : {}".format(current.key))
    
#     def max_node(self):
#         current = self
#         while current.rchild:
#             current = current.rchild
#         print("node with maximum key is : {} ".format(current.key))



      
# root = BST(10)
# list1 = [6,3,1,6,98,3,7,100]
# for i in list1 : 
#     root.insert(i)
# # root.search(6)
# print("Pre-order")
# root.preorder()
# print()
# # print("In-order") 
# # root.inorder()
# # print()
# # print("Post-order")

# # root.delete(10)
# # print("after deleting")
# # root.preorder()

# root.min_node()
# root.max_node()

# import time
# val = 97
# startTime = time.perf_counter_ns()
# result = root.search(val)
# endTime = time.perf_counter_ns()
# print("Find {} = {}".format(val,result))
# print("Process time : {}".format(endTime - startTime))

print("--------------------------------------------------------------------")

# import calendar

# yy = 2023
# mm = 7
# print(calendar.month(yy,mm))

print("--------------------------------------------------------------------")

# STcode = int(input('Student Code : '))
# scode = STcode % 1000
# print("Scode =" ,scode)
# a = scode % 4
# print("a =" ,a)

print("--------------------------------------------------------------------")

# class Player():
#     def __init__(self) :
#         self.fname = ""
#         self.lname = ""
#         self.number = ""
    
#     def print(self) :
#         print("Firstname : {}".format(self.fname))
#         print("Lastname : {}".format(self.lname))
#         print("Number : {}".format(self.number))


# class Player2():
#     def __init__(self , fname , lname , number) :
#         self.fname = fname
#         self.lname = lname
#         self.number = number

#     def print(self) :
#         print("Firstname : {}".format(self.fname))
#         print("Lastname : {}".format(self.lname))
#         print("Number : {}".format(self.number))

# p1 = Player()
# p1.fname = "Kankavee"
# p1.lname = "Ramsri"
# p1.number = "6610110408"

# p1.print()

# print("-" * 30)

# p2 = Player2("Ronnakrit" , "Rattamanee" , "6610110656")
# p2.print()


print("--------------------------------------------------------------------")

# class Yaiba :
#     def __init__(self , name , type , weight , height) :
#         self.name = name
#         self.type = type
#         self.weight = weight
#         self.height = height
#         self.hp = 100
    
#     def print(self) :
#         print("Name : {}".format(self.name))
#         print("Type : {}".format(self.type))
#         print("Weight : {}".format(self.weight))
#         print("Height : {}".format(self.height))
#         print("HP : {}".format(self.hp))
    
#     def attack(self , enemy) :
#         enemy.hp -= 20

#     def overattack(self , enemy) :
#         enemy.hp -= 60
    
#     def headshot(self , enemy) :
#         enemy.hp -= 100
    
#     def support(self , sup) :
#         sup.hp += 30
    

# uzui = Yaiba("Uzui" , "Voice hashira" , "80 kg", "200 cm")
# gyutaro = Yaiba("Gyutaro" , "Demon","40 kg" , "175 cm")
# uzui.print()
# print("-" * 30)
# gyutaro.print()
# print("-" * 30)
# gyutaro.attack(uzui)
# print(" ( Gyutaro attack Uzui ) ")
# print("-" * 30)
# uzui.print()
# print("-" * 30)
# gyutaro.overattack(uzui)
# print(" ( Gyutaro overattack Uzui ) ")
# print("-" * 30)
# uzui.print()
# print("-" * 30)

# tanjiro = Yaiba("Tanjiro" , "Breath of sun" , "60 kg" , "180 cm")
# tanjiro.print()
# print("-" * 30)
# tanjiro.support(uzui)
# print(" ( Tanjiro support Uzui ) ")
# print("-" * 30)
# uzui.print()
# print("-" * 30)
# uzui.overattack(gyutaro)
# print(" ( Uzui overattack Gyutaro ) ")
# print("-" * 30)
# gyutaro.print()

# daki = Yaiba("Daki" , "Demon" , "55 kg" , "175 cm")
# daki.support(gyutaro)
# print("-" * 30)
# print(" ( Daki support Gyutaro ) ")
# print("-" * 30)
# gyutaro.print()
# print("-" * 30)
# tanjiro.attack(gyutaro)
# print( " ( Tanjiro attack Gyutaro ) ")
# print("-" * 30)
# gyutaro.print()


print("--------------------------------------------------------------------")

# while True :
#     num = int(input("Enter num : "))
#     if len(str(num)) > 10 :
#         print("Error , try it again.")
#         print('-' * 20)
#     else :
#         break

# i = num
# sum_num = 0
# while i > 0 :
#     a = i % 10
#     sum_num += a
#     i //= 10

# print("Sum of digits is {}".format(sum_num))

print("--------------------------------------------------------------------")


















