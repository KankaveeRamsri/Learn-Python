import random
import math
import string

# rand_num = random.randint(0,20)
# user_number = int(input("Enter a number : "))

# if user_number < 0 or user_number > 20 :
#     print("----- Out of range -----")
# elif abs(user_number - rand_num) <= 10 :
#     print("----- Close -----")
# elif abs(user_number - rand_num) > 10 :
#     print("----- Far -----")
# elif abs(user_number == rand_num) :
#     print("Good job,it's equal")

# print(rand_num)

print('---------------------------------')

# user_num = float(input("Enter a number : "))

# if user_num % 15 == 0 :
#     print("----- FizzBuzz -----")
# elif user_num % 3 == 0 :
#     print("----- Fizz -----")
# elif user_num % 5 == 0 :
#     print("----- Buzz -----")

print('---------------------------------')

# user_measure = input("Enter measure in cm , mm , m : ")
# wanted_measure = input("Enter measure to convert in cm , mm , m : ")

# if 'cm' in user_measure and wanted_measure == 'mm' :
#     result = float(user_measure.replace('cm','')) * 10
#     print("A result after converting is {} mm. ".format(result))
# elif 'cm' in user_measure and wanted_measure == 'm' :
#     result = float(user_measure.replace('cm','')) / 100
#     print("A result after converting is {} m. ".format(result))
# elif 'mm' in user_measure and wanted_measure == 'cm' :
#     result = float(user_measure.replace('mm','')) / 10
#     print("A result after converting is {} cm.".format(result))
# elif 'mm' in user_measure and wanted_measure == 'm' :
#     result = float(user_measure.replace('mm','')) / 1000
#     print("A result after converting is {} m.".format(result))
# elif 'm' in user_measure and wanted_measure == 'cm' :
#     result = float(user_measure.replace('m','')) * 100 
#     print("A result after converting is {} cm.".format(result))
# elif 'm' in user_measure and wanted_measure == 'mm' :
#     result = float(user_measure.replace('m','')) * 1000
#     print("A result after converting is {} mm.".format(result))

print('---------------------------------')

# user_text = input("Enter your text : ")
# hidden_text = input("Enter hidden text : ")

# result = user_text.replace(hidden_text,'*'*len(hidden_text))
# print(result)

print('---------------------------------')

user_text = str(input("Enter your text : "))
user_text = user_text.upper()

if len(user_text) != 3 :
    print("----- Word length is mismatched -----")
else :
    result = ""
    for i in range(0,len(user_text)) :
        if user_text[i] == 'Z' :
            value = 'A'
            result += value
        else :
            value = chr(ord(user_text[i]) + 1)
            result += value

    print(result)

print('---------------------------------')





