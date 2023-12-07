# def get_number(prompt) :
#     while True : 
#         try : 
#             value = input(prompt)
#             if len(str(value)) == 5 :
#                 return str(value)
#             else :
#                 print("Error, Value must be 5 units.")

#         except ValueError :
#             print("Error, Value must be integer number.")


# arabic_input = get_number("Enter only 5 Arabic number: ")
# arabic_num = '1234567890'
# thai_num = '๑๒๓๔๕๖๗๘๙๐'

# result = ''
# for i in range(5) : 
#     num = arabic_num.index(arabic_input[i])
#     result += thai_num[num]

# print("Thai number is {}".format(result))

print("--------------------------------")

# def change_to_fahrenheit(celcius) :
#     fahrenheit = ((celcius * 9) / 5 ) + 32
#     return fahrenheit

# fahrenheit = change_to_fahrenheit(float(input("Enter a temperature in celcius : ")))
# print("That is {:.1f} degrees fahrenheit.".format(fahrenheit))

print("--------------------------------")

# import string 

# while True : 
#     user_input = input("Enter 5 characters: ").upper()
#     if len(user_input) != 5 :
#         pass
#     else : 
#         break
    
# uppercase = string.ascii_uppercase
# lowercase = string.ascii_lowercase[::-1] 

# alphabet1 = uppercase.index(user_input[0])


# def encoder() :
#     answer = ""
#     for i in range(5) :
#         alphabet = uppercase.index(user_input[i])
#         answer += lowercase[alphabet]
#     return answer

# result = encoder()
# print("Encryption is {}".format(result))

print("--------------------------------")

# data_num = list()

# while True :
#     user_input = int(input("Enter number: "))
#     if user_input >= 0 :
#         data_num.append(user_input)
#     else :
#         break

# data_num.sort()
# print("Minimum number is {}".format(data_num[0]))
# print("Maximum number is {}".format(data_num[-1]))

print("--------------------------------")

# data_num = list()
# for i in range(1,21) :
#     user_input = int(input("Enter number #{}: ".format(i)))
#     if user_input not in data_num :
#         data_num.append(user_input)

# data_num.sort()

# result = ""
# for i in data_num :
#     result += str(i)
#     result += " "

# print("Unique numbers is {}".format(result))

# even_position = list()
# for i in range(0,len(data_num),2) :
#     even_position.append(data_num[i])

# answer = sum(even_position)/len(even_position)
# print("Average number of even position in list is {:.2f}".format(answer))

print("--------------------------------")

# def change_to_celsiuis(fahrenheit) :
#     celcius = ((fahrenheit - 32) / 9) * 5 
#     return celcius 

# fahrenheit_input = change_to_celsiuis(int(input("Type in a temperature in Fahrenheit: ")))
# print("That is {:.1f} degrees Celsius".format(fahrenheit_input))

print("--------------------------------")

# user_input = str(input("Enter text: "))
# hide_text = str(input("Enter filter word: "))

# print("Text after filter is {}".format(user_input.replace(hide_text,'*'*len(hide_text))))

print("--------------------------------")

# text_input = str(input("Enter value in mm, cm and m: " ))
# unit = str(input("Enter unit to convert in mm, cm, m: "))

# if 'mm' in text_input and 'm' in unit :
#     value = float(text_input.replace('mm',"")) * 0.001
#     print("Value after unit conversion is {}m".format(value))

# elif 'mm' in text_input and 'cm' in unit :
#     value = float(text_input.replace('mm',"")) * 0.1
#     print("Value after unit conversion is {}cm".format(value))

# elif 'mm' in text_input and 'mm' in unit :
#     value = float(text_input.replace('mm',''))
#     print("Value after unit conversion is {}mm".format(value))

# elif 'cm' in text_input and 'm' in unit :
#     value = float(text_input.replace('cm',"")) * 0.01
#     print("Value after unit conversion is {}m".format(value))

# elif 'cm' in text_input and 'mm' in unit : 
#     value = float(text_input.replace('cm','')) * 10
#     print("Value after unit conversion is {}mm".format(value))

# elif 'cm' in text_input and 'cm' in unit :
#     value = float(text_input.replace('cm',''))
#     print("Value after unit conversion is {}cm".format(value))

# elif 'm' in text_input and 'mm' in unit :
#     value = float(text_input.replace('m','')) * 1000
#     print("Value after unit conversion is {}mm".format(value))

# elif 'm' in text_input and 'cm' in unit :
#     value = float(text_input.replace('m','')) * 100
#     print("Value after unit conversion is {}cm".format(value))

# elif 'm' in text_input and 'm' in unit : 
#     value = float(text_input.replace('m',''))
#     print("Value after unit conversion is {}m".format(value))
    
print("--------------------------------")

# token = str(input("Enter Token number: "))


# a_number_of_ackara = int(len(token)) #จำนวนอักขระ

# summation_of_1 = 0 #ผลบวกของเลข 1
# for i in token :
#     summation_of_1 += int(i)

# a_number_of_zero = 0 # ผลบวกของจำนวนเลข 0
# for i in token :
#     if int(i) == 0 :
#         a_number_of_zero += 1

# # print(summation_of_1)
# # print(a_number_of_zero)


# if '2' in token or '3' in token or '4' in token or '5' in token or '6' in token or '7' in token or '8' in token or '9' in token :      
#     print("Your token is invalid")

# else :
#     if a_number_of_ackara % summation_of_1 == a_number_of_zero :
#         print("You get jackpot!!")
#     else :
#         print("See you next time, have a nice day.")

print("--------------------------------")

# import string

# def check_len_text(prompt) :
#     while True :
#         try : 
#             value = str(input(prompt))
#             if len(value) == 3 :
#                 return value
#             else :
#                 print("Error!,text must be 3 alphabets")
#         except ValueError :
#             break


# text = check_len_text("Enter 3 charecters: ").upper()

# uppercase = string.ascii_uppercase
# new_value = "BCDEFGHIJKLMNOPQRSTUVWXYZA"

# result = ""
# for i in range(3) :
#     alphabet = uppercase.index(text[i])
#     result += new_value[alphabet]

# print("Ciphertext is {}".format(result))

print("--------------------------------")

# n = int(input('Enter number: '))

# base2 = ''
# base10 = n

# while base10 > 0 :
#     frac = int(base10%2)
#     base2 = str(frac) + base2
#     base10 = (base10 - frac)/2

# print('{} is {} in base 2'.format(n,base2))


print("--------------------------------")

# row = int(input("Enter the number of rows:"))

# for i in range(2,row+1) :
#     print('*'*i)

print("--------------------------------")

# row = int(input("Enter number of rows: "))

# for i in range(1, row + 1):
#     print(" " * (row - i),end="")
#     print("*" * i)

print("--------------------------------")

# row = int(input("Enter the number of rows: "))

# for i in range(row,0,-1):
#     print('*'*i)

print("--------------------------------")
    
# row = int(input("Enter the number of rows: "))

# for i in range(row,0,-1):
#     print(" " * (row-i),end="")
#     print('*'*i)
    
print("--------------------------------")

# row = int(input("Enter the number of rows: "))
# symbol = str(input("Enter print symbol: "))

# for i in range(row):
#         print(' ' * (row - i - 1) + symbol * (i * 2 + 1))
        
print("--------------------------------")

row = int(input("Enter the number of rows: "))
symbol = str(input("Enter print symbol: "))

for i in range(row):
    print(' ' * i + symbol * ((row - i) * 2 - 1))

print("--------------------------------")

# import string

# print("Select 2 options")
# print("- 1 encrypt with ROT 13")
# print("- 2 decrypt with ROT 13")


# option = str(input("Choose option: "))
# text = str(input("Enter text: "))

# lower_alpha = string.ascii_lowercase
# upper_alpha = string.ascii_uppercase

# answer = ""

# for i in text :
#     if i.isupper() :
#         if option == '1' :
#             answer += upper_alpha[(upper_alpha.index(i) + 13) % 26]
#         elif option == '2' :
#             answer += upper_alpha[(upper_alpha.index(i) - 13) % 26]
    
#     elif i.islower() :
#         if option == '1' :
#             answer += lower_alpha[(lower_alpha.index(i) + 13) % 26]
#         elif option == '2' :
#             answer += lower_alpha[(lower_alpha.index(i) - 13) % 26]
    
#     else :
#         answer += i
    
# if option == '1' :
#     print('Ciphertext is "{}"'.format(answer))
# elif option == '2' :
#     print('Plaintext is "{}"'.format(answer))


