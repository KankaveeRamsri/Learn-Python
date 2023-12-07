# s1 = 'Hello world!'
# print(s1)

# s2 = 'Hello\n world!'
# print(s2)

# s3 = 'doesn\'t Hello, world!'
# print(s3)


print("------------------------")

# hello = 'Hello'
# world = 'World'
# lucky_number = 13.1313
# s1 = 'Hello,{}!'.format(world)
# s2 = '{hello},{world}'.format(world=world,hello='Hellooooo')
# s3 = '{2} => {1} , {0}'.format(hello,world,lucky_number)
# s4 = '{} , {}! The lucky number is {} and {:.2f}'.format(hello,world,lucky_number,lucky_number)
# print(s1)
# print(s2)
# print(s3)
# print(s4)


print("------------------------")

# s = 'Hello, World!'
# print(s[4])
# print(s[::-1])
# print(s[:4])
# print(s[4:])
# print(s[:4] + s[4:])
# print(s[0:-9])

# print('He' in s)
# print('Heool' in s)
# print('Heool' not in s)
# print('kankavee' in s)


print("------------------------")

# s = 'Hello, World!'
# ss = s.split() #แยก str ไปอยู่ใน list
# print(ss)
# print(ss[0].strip(',') + ss[1])
# print(ss[-1].upper() , ss[0].lower())
# print(s.index('l'))
# print(s.count('l'))
# print(s.replace('World','Kankavee'))
# print(s.capitalize())


print("------------------------")

import math

# print("PI is {:.4f}".format(math.pi))
# print('Floor PI is {}'.format(math.floor(math.pi)))
# print('Ceil PI is {}'.format(math.ceil(math.pi)))
# print('Log 2 = {}'.format(math.log(2,10)))
# print('Sqrt 2 = {}'.format(math.sqrt(2)))


print("------------------------")

# raduis_user = float(input('Enter radius : '))
# print('raduis of circle is {}'.format(raduis_user))
# circumference = 2 * math.pi * raduis_user
# print('Circumference of circle is {:.4f}'.format(circumference))
# area = math.pi * pow(raduis_user,2)
# print('Area of circle is {:.2f}'.format(area))

# y_user = float(input('Enter value of y : '))
# y = pow(y_user,2)
# r = pow(raduis_user,2)
# xx = r - y
# x = math.sqrt(abs(xx))

# print('Value of x is {:.4f} and {:.4f}'.format(x,-x))


print("------------------------")

# while True :
#     user_arabic = input("Enter your number in arabic : ")
#     if len(str(user_arabic)) == 5 :
#         break
#     else :
#         print("Error! , try it again")

# num_arabic = '1234567890'
# num_thai = '๑๒๓๔๕๖๗๘๙๐'

# result = ""
# for i in range(0,len(str(user_arabic))) :
#     num = num_arabic.index(user_arabic[i])
#     value = num_thai[num]
#     result += value

# print(result)

print("------------------------")

# import string

# while True : 
#     user_alphabet = input("Enter your alphabet 5 units : ")
#     if len(user_alphabet) == 5 :
#         break
#     else :
#         print("Error! , try it again")

# new_user_alphabet = user_alphabet.lower()
# lowercase = string.ascii_lowercase
# reverse_lowercase = string.ascii_lowercase[::-1]

# value = ""
# for i in range(0,len(user_alphabet)):
#     alphabet = lowercase.index(new_user_alphabet[i])
#     result = reverse_lowercase[alphabet]
#     value += result

# print(value)

print("------------------------")

#A = 65
#a = 97

# import string
# while True :
#     user_text = input("Enter your text in lowercase : ")
#     if  user_text.islower() :
#         break
#     else :
#         print("Error! , try it again")

# result = ""
# for i in user_text :
#     value = chr(ord(i) - 32)
#     result += value

# print(result)

print(ord('A'))
print(chr(65))