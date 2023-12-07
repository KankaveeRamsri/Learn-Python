#1.A+B Problem

# a = int(input())
# b = int(input())
# summation = a + b
# print(summation)

print("-------------------------------")

#2.Grading

# sum1 = 0
# for i in range(0,2) :
#     while True :
#         score = float(input())
#         if score >= 0 and score <= 30 :
#             sum1 += score
#             break
#         else :
#             print("Error!,try it again")

# sum2 = 0
# while True :
#     score = float(input())
#     if score >= 0 and score <= 40 :
#         sum2 += score
#         break
#     else :
#         print("Error!,try it again")

# summation = sum1 + sum2

# def Grade():
#     if summation >= 80 :
#         return "A"
#     elif summation >= 75 and summation <= 79 :
#         return "B+"
#     elif summation >= 70 and summation <= 74 :
#         return "B"
#     elif summation >= 65 and summation <= 69 :
#         return "C+"
#     elif summation >= 60 and summation <= 64 :
#         return "C"
#     elif summation >= 55 and summation <= 59 :
#         return "D+"
#     elif summation >= 50 and summation <= 54 :
#         return "D"
#     else :
#         return "F"


# result = Grade()
# print(result)

print("-------------------------------")

#3.Min Max

# while True :
#     a = int(input())
#     if a >= 1 and a <= 1000 :
#         break
# data_num = list()
# for i in range(0,a) :
#     num = int(input())
#     data_num.append(num)

# print(min(data_num))
# print(max(data_num))

print("-------------------------------")

#4.Matrix Addition

# def matrix(m,n) :
#     mat = [list(map(int,input().split())) for i in range(m)]
#     return mat

# m,n = list(map(int,input().split()))
# mat1 = matrix(m,n)
# mat2 = matrix(m,n)
# result = []

# for i in range(m) :
#     temp = []
#     for j in range(n) :
#         temp.append(mat1[i][j] + mat2[i][j])
#     result.append(temp)

# for i in result :
#     for j in i :
#         print(j,end="")
#     print()

print("-------------------------------")

#5.Character Checker 

# user_input = str(input())

# def check_alphabet():
#     if user_input == user_input.upper():
#         return "All Capital Letter"
#     elif user_input == user_input.lower():
#         return "All Small Letter"
#     else :
#         return "Mix"

# result = check_alphabet()
# print(result)    

print("-------------------------------")

#6.Pythagorus (มีปัญหาอยู่)

# import math

# def Pythaorus(x,y) :
#     c = pow((pow(x,2) + pow(y,2)),1/2)
#     return c

# a,b = input().split()
# a = float(a)
# b = float(b)
# result = Pythaorus(a,b)
# print(result)

print("-------------------------------")

#7.Herman (อ่านโจทย์กูยังงง)

print("-------------------------------")

#8.X2

# while True :
#     X1 , S = input().split()
#     X1 = int(X1)
#     S = int(S)
#     if X1 >= 0 and X1 <= 1000 and S >= 0 and S <= 1000 :
#         break
#     else :
#         print("Error! , try it again.")

# def value_X2() :
#     X2 = (S*2) - X1
#     return X2

# result = value_X2()
# print(result)

print("-------------------------------")

#9.ABC

# x = [int(i) for i in input().split()]
# x.sort()
# y = str(input()) # A < B < C
# tol = ""
# for i in y :
#     if i == "C" :
#         tol += str(x[2]) + " "
#     elif i == "A" :
#         tol += str(x[0]) + " "
#     elif i == "B" :
#         tol += str(x[1]) + " "

# print(x)
# print(tol)

print("-------------------------------")

#10.Trick

# วิธีที่ 1

# process = str(input())
# ans = ["o","x","x"]

# def A() :
#     x = ans.pop(0)
#     if x == "o" :
#         ans.insert(1,"o")
#     elif x == "x" :
#         ans.insert(1,"x")

# def B() :
#     x = ans.pop(1)
#     if x == "o" :
#         ans.insert(2,"o")
#     elif x == "x" :
#         ans.insert(2,"x")

# def C() :
#     x = ans.pop(0)
#     y = ans.pop(0)
#     if y == "o" :
#         ans.insert(1,"o")
#     elif y == "x" :
#         ans.insert(1,"x")
#     if x == "o" :
#         ans.insert(2,"o")
#     elif x == "x" :
#         ans.insert(2,"x")

# for i in process :
#     if i == "A" :
#         A()
#     elif i == "B" :
#         B()
#     elif i == "C" :
#         C()

# print(ans.index("o")+1)

print("-------------------------------")

# วิธีที่ 2

# alphabet = str(input())
# initial = [True,False,False]

# for x in alphabet :
#     if x == 'A' :
#         initial[0],initial[1] = initial[1],initial[0]
#     elif x == 'B' :
#         initial[1],initial[2] = initial[2],initial[1]
#     elif x == 'C' :
#         initial[0],initial[2] = initial[2],initial[0]

# for y in range(len(initial)) :
#     if initial[y] == True :
#         print(y+1)

print("-------------------------------")

# วิธีที่ 3

# alphabet = str(input())
# result = 1

# for text in alphabet :
#     if text == 'A':
#         if result == 1 :
#             result += 1 
#         elif result == 2 :
#             result -= 1
#     elif text == 'B' :
#         if result == 2 :
#             result += 1
#         elif result == 3 :
#             result -= 1 
#     elif text == 'C' :
#         if result == 3 :
#             result -= 2
#         elif result == 1 :
#             result += 2

# print(result)

print("-------------------------------")

#11.Modulo

# list_num = list()
# counter = 0
# while counter < 10 :
#     num = int(input())
#     if num < 1000 :
#         list_num.append(num)
#         counter += 1
#     else :
#         print("Error! , try it again")

# list_mod = list()
# for i in list_num :
#     val = i % 42 
#     if val in list_mod :
#         pass
#     else :
#         list_mod.append(val)

# print(len(list_mod))


print("-------------------------------")

# 12.Okviri

n = input()
length = len(n)
def first_Line() :
    for i in range(length):
        if i == 0 :
            print(".",end="")
        if (i+1) % 3 == 0 :
            print(".*..",end="")
        else :
            print(".#..",end="")
    print()

def second_Line() :
    for i in range(length):
        if i == 0 :
            print(".",end="")
        if (i+1) % 3 == 0 :
            print("*.*.",end="")
        else :
            print("#.#.",end="")
    print()

def third_Line() :
    for i in range(length):
        if i == 0 :
            print("#." + n[i] + ".#",end="")
        if (i+1) % 3 == 0 :
            print("*." + n[i] + ".*",end="")
        # elif i != 0 and i % 3 == 0 :
        #     print("." + n[i] + ".#",end="")
        elif i != 0 and i % 3 == 1 :
            print("." + n[i] + ".",end="")
        if length % 3 == 2 and i == length - 1 and i % 3 == 1 :
            print("#",end="")
    print()

first_Line()
second_Line()
third_Line()
second_Line()
first_Line()

print("-------------------------------")

# 13.Seven Dwarves

# data_num = [int(input()) for i in range(1,10)]
# summation = sum(data_num)
# result = summation - 100 

# for i in data_num :
#     discard = list()
#     for j in data_num[data_num.index(i) + 1 : 9] :
#         if i + j == result :
#             discard.extend([i,j])
#     if discard :
#         break

# for i in discard :
#     data_num.remove(i)

# for i in range(len(data_num)) :
#     print(data_num[i])

print("-------------------------------")

# import random

# data_num = [int(input()) for i in range(1,10)]
# summation_100 = list()
# while True :
#     rand_num = random.sample(data_num,7)
#     if sum(rand_num) == 100 :
#         summation_100.append(rand_num)
#         break

# sum_100 = list()
# for i in range(0,7) :
#     sum_100.append(summation_100[0][i])

# new = list()
# for i in data_num :
#     if i in sum_100 :
#         new.append(i)

# for result in new :
#     print(result)

print("-------------------------------")

#14.Great Common Divisor

# import math

# a , b = input().split()
# a = int(a)
# b = int(b)

# result = math.gcd(a,b)

# print(result)

print("-------------------------------")

#15.Skocimis 

# num = [int(i) for i in input().split()]
# num.sort()

# result = max(num[1] - num[0] , num[2] - num[1]) - 1 
# print(result)

print("-------------------------------")

# num = [int(i) for i in input().split()]
# num.sort()

# count1 = -1
# count2 = -1

# for i in range(num[0],num[1]) :
#     count1 += 1

# for i in range(num[1],num[2]) :
#     count2 += 1

# maximum_round = max(count1,count2)
# print(maximum_round)

print("-------------------------------")

#16.Ptice 

# วิธีนี้ผิด 3 จาก 10 (ยังไม่สมบูรณ์)

# while True :
#     score = int(input())
#     if score < 0 or score > 100 :
#         pass
#     else :
#         break

# while True :
#     answer = [str(i) for i in input().upper()]
#     if len(answer) != score :
#         pass
#     else :
#         break

# mydict = dict(
#     Adrian = ['A','B','C'] * score ,
#     Bruno = ['B','A','B','C'] * score ,
#     Goran = ['C','C','A','A','B','B'] * score 
# )

# score_Adrian = score_Bruno = score_Goran = 0 

# for i in range(score) : 
#     if mydict['Adrian'][i] == answer[i] :
#         score_Adrian += 1
#     if mydict['Bruno'][i] == answer[i] :
#         score_Bruno += 1 
#     if mydict['Goran'][i] == answer[i] :
#         score_Goran += 1 

# maximum = max(score_Adrian,score_Bruno,score_Goran)

# if maximum == score_Adrian and maximum == score_Bruno and maximum == score_Goran :
#     print(maximum , '\n{}'.format(list(mydict.keys())[0]) , '\n{}'.format(list(mydict.keys())[1]) , '\n{}'.format(list(mydict.keys())[2]))
# elif maximum == score_Adrian  :
#     print(maximum , '\n{}'.format(list(mydict.keys())[0]))
# elif maximum == score_Bruno  :
#     print(maximum , '\n{}'.format(list(mydict.keys())[1]))
# elif maximum == score_Goran  :
#     print(maximum , '\n{}'.format(list(mydict.keys())[2]))

print("-------------------------------")

#17.Kornislav 

# length = [int(i) for i in input().split()]
# length.sort()
# print(length[0] * length[2])

print("-------------------------------")

#18.Reseto

print("-------------------------------")

#19.Perket (งงแดก)

import math 

while True : 
    N = int(input())
    if N < 1 or N > 10 :
        pass
    else : 
        break

SList = list()
BList = list()
for i in range(N) : 
    S , B = input().split()
    S = int(S)
    B = int(B)
    SList.append(S)
    BList.append(B)

Value_S = 1
for i in SList :
     Value_S *= i

Value_B = 0
for i in BList :
    Value_B += i

result = min(1000000000,abs(Value_B - Value_S))
print(result)
   






















    


   
    










