# temp = float(input('Enter current temperature :'))
# print('Temperature is' , temp , 'Celsius.' , 'It make me feel good')

# if temp > 35 :
#     print('Current temperature is so damn hot' )

# if temp < 23 :
#     print('Current temperature make me freeze')

# if temp >=23 and temp <=35 :
#     print('I am fine')

print('-----------------------------------')

# sid = int(input(' Enter your student id : '))
# if sid % 2 != 0 :
#     print("your number is odd number")

# else: 
#     print("ัYour number is even number")

# num = int(input('Enter number :'))

# print('-----------------------------------')

# if num%3 == 0 and num%5 == 0  :
#     print('FizzBuzz')
# elif num%3 == 0 :
#     print('Fizz')
# else :
#     print('Buzz')

print('---------------------------------')

# num = float(input('Enter number : '))
# measure = input('Enter measure : ')
# wanted_measure = input('Enter measure you want : ')

# if measure == 'm' :
#     if wanted_measure == 'cm' :
#         print("a result is " , num*100 , "cm")
#     elif wanted_measure == 'mm' :
#         print("a result is " , num*1000 , "mm")

# elif measure == 'cm' :
#     if wanted_measure == 'm' : 
#         print("a result is " , num/100 , "m")
#     elif wanted_measure == 'mm':
#         print("a result is " , num*10 , "mm")

# elif measure == 'mm' :
#     if wanted_measure == 'm' :
#        print("a result is " , num/1000 , "m")
#     elif wanted_measure == 'cm' :
#         print("a result is " , num/10 , "cm")

print('---------------------------------')

# value = input("Enter value in mm , cm , m : ")        #*****************************************
# unit = input("Enter unit to convert in mm , cm , m : ")


# if "cm" in value and unit == "mm":
#     result = float(value.replace("cm","")) * 10
#     print(f"Value after unit conversion is {result} mm")
# elif "cm" in value and unit == "m":
#     result = float(value.replace("cm","")) / 100
#     print(f"Value after unit conversion is {result} m")
# elif "mm" in value and unit == "cm":
#     result = float(value.replace("mm","")) / 10
#     print(f"Value after unit conversion is {result} cm")
# elif "mm" in value and unit == "m":
#     result = float(value.replace("mm","")) / 1000
#     print(f"Value after unit conversion is {result} m")
# elif "m" in value and unit == "cm":
#     result = float(value.replace("m","")) * 100
#     print(f"Value after unit conversion is {result} cm")
# elif "m" in value and unit == "mm":
#     result = float(value.replace("m","")) * 1000
#     print(f"Value after unit conversion is {result} mm")
# elif "m" in value and unit == "m" :
#     print(f"a result is same value : {value}")
# elif "cm" in value and unit == "cm" :
#     print(value)
# elif "mm" in value and unit == "mm" :
#     print(value)



print('---------------------------------')

# text = input("Enter text :")
# forbidden_text = input("Enter forbidden text :")

# print(text.replace(forbidden_text , '*' * len(forbidden_text)))

print('---------------------------------')

# text = input("Select your word :")
# hide_word = input("type word you want to hide :")

# print(text.replace(hide_word , '*' * len(hide_word)))




print('---------------------------------')

import string
text = input("Enter text 3 units : ")
text = text.upper()

uppercase = string.ascii_uppercase
new = "BCDEFGHIJKLMNOPQRSTUVWXYZA"

if len(text) != 3 :
    print("a result is word length is mismatched")
else :
    text1 = uppercase.index(text[0])
    print(text1)
    text2 = uppercase.index(text[1])
    text3 = uppercase.index(text[2])
    print(new[text1]+new[text2]+new[text3])
    








    
   
