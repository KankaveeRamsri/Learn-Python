#5
# score = int(input("Enter score : "))

# if score >= 80 :
#     print("You got A grade.")

# elif score >= 70 :
#     print("You got B grade.")

# elif score >= 60 :
#     print("You got C grade.")

# elif score >= 50 :
#     print("You got D grade.")

# else :
#     print("You got F grade.")

print(" ---------------------------- ")

#6
# num = int(input())

# if num > 31 :
#     print("Great!")

# else :
#     print("none")

print(" ---------------------------- ")

#7
# num = int(input())

# if num < 90 :
#     print("Great!")

# else :
#     print("none")

print(" ---------------------------- ")

#8
# num = int(input())

# if num % 2 == 0 :
#     print(f"{num} is even number.")

# else :
#     print(f"{num} is odd number.")

print(" ---------------------------- ")

#9
# num = int(input())

# if num % 3 == 0 :
#     print("Great!")

# else :
#     print("Good bye!")

print(" ---------------------------- ")
#10
# num = int(input())

# if num % 2 == 0 :
#     # print(num)
#     if num % 3 == 0 :
#         print("Good job!")
#     else :
#         print("Great!")

# else :
#     print("Good bye !")

print(" ---------------------------- ")

#11
# num = str(input())

# if num[0] == num[1] :
#     print("same number")

# else :
#     print("different number")

print(" ---------------------------- ")

#12
# num = str(input())

# if num[1] > num[0] :
#     print("เลขโดดในหลักสิบมากกว่าหลักหน่วย")

# else :
#     print("เลขโดดในหลักสิบน้อยกว่าหลักหน่วย")ห

print(" ---------------------------- ")

#13
# num = str(input())
# import math
# a = int(num[0])
# b = int(num[1])
# if num[0] < num[1] :
#     print(f"หลักหน่วยน้อยกว่าหลักสิบอยู่ {abs(a - b)}")

# elif num[0] > num[1] :
#     print(f"หลักหน่วยมากกว่าหลักสิบอยู่ {abs(a - b)}")

# else :
#     print("เลขหลักหน่วยและหลักสิบมีค่าเท่ากัน")

print(" ---------------------------- ")

#14
# num = str(input())
# a = int(num[0])
# b = int(num[1])
# if a + b == 15 :
#     print("15")
# else : 
#     print("Good bye !")

print(" ---------------------------- ")

#15

# num = int(input())
# num1 = int(input())
# num2 = int(input())

# print(max(num , num1 , num2))

print(" ---------------------------- ")

#16
# a = int(input())
# b = int(input())
# c = int(input())

# A = max(a,b,c)
# B = min(a,b,c)

# print("มากสุดมากกว่าน้อยสุดอยู่ {}".format(A-B))


print(" ---------------------------- ")

#17
# celsius = float(input("Enter temp in celsius : "))
# text = input()

# if text == 'f' or text == "F" :
#     fahrenheit = (9 * celsius)/5  + 32
#     print("Temp in fahremheit : {:.2f} degrees fahrenheit".format(fahrenheit))

# elif text == 'k' or text == "K" :
#     kalvin = 273.15 + celsius
#     print("Temp in kalvin : {:.2f} kalvin".format(kalvin))

# else :
#     print(" -------- Error -------- ")

print(" ---------------------------- ")

# 18
# weight = float(input("Enter your weight(kg) : "))
# height = float(input("Enter your height(m) : "))

# BMI = weight / pow(height,2)
# print("BMI is {:.2f}".format(BMI))

# if BMI < 18.5 :
#     print("Underweight")

# elif BMI < 25 :
#     print("Normal weight")

# elif BMI < 30 :
#     print("overweight")

# else :
#     print("Obisity")

print(" ---------------------------- ")

#19
# price = float(input("Enter buying amount : "))

# if price >= 1000 :
#     if price < 3000 :
#         value = price * 0.9
#         print("Amount due after discount is {:.2f} bath".format(value))
#     else :
#         value = price * 0.85
#         print("Amount due after discount is {:.2f} bath".format(value))

# else :
#     print("You didn't receive discount.")

print(" ---------------------------- ")

#20
# num = int(input("Enter your guess (0-100) : "))
# target = 72

# if num < 0 or num > 100 :
#     print("Sorry , out of range , try again later")

# elif num != target :
#     print("Sorry , your guess is wring , try again later")

# else :
#     print("Congratulations , your guess is correct")

print(" ---------------------------- ")

#21
# user = input("Username : ")
# password = input("Password : ")

# if user == 'admin' and password == 'Ad13n@23t' :
#     print('Welcome , admin!')

# else :
#     print("You are not admin.")

print(" ---------------------------- ")

# food = input("Enter your buffet choice : ")
# day = input("Is today Wednesday(yes/no) : ")

# Japanese = 1000
# Korean = 1500

# if day == "yes" :
#     if food == "Japanese" :
#         value = Japanese * 0.85
#         print("Your payment is {:.2f} bath.".format(value))
#     elif food == "Korean" :
#         value = Korean * 0.85
#         print("Your payment is {:.2f} bath".format(value))
#     else :
#         print(f"We don't have {food} buffet , select choice again")

# elif day == "no" :
#     if food == "Japanese" :
#         print("Your payment is {:.2f} bath.".format(Japanese))
#     elif food == "Korean" :
#         print("Your payment is {:.2f} bath".format(Korean))
#     else :
#         print(f"We don't have {food} buffet , select choice again")

# else :
#     print("Wrong input , try again later")

print(" ---------------------------- ")

#22
# tv = int(input("How many TVs : "))
# dp = int(input("How many DVD players : "))
# As = int(input("How many Audio System : "))

# TV = 6000
# DVD_players = 1500
# Audio_systems = 3000

# a = TV * tv
# b = DVD_players * dp
# c = Audio_systems * As

# value = a + b + c

# if value < 24000 :
#     print("Total price is {:.2f} bath.".format(value))
#     print("Your payment is {:.2f} bath.".format(value))

# elif value >= 24000 :
#     print("Total price is {:.2f} bath.".format(value))
#     print("You've got a discount of {:.2f} bath.".format(value * 0.2))
#     print("Your payment is {:.2f} bath.".format(value * 0.8))

print(" ---------------------------- ")