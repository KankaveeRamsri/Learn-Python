s1 = 'Hello , world!'
# s2 = "Hello , world!"
# s3 = "Hello ,\n world!"
# s4 = 'doesn\'t  Hello , world '
# s5 = ' "Hello ," world !'
# s6 = "Hello , 'world!'"
# s7 = ''' Hello
#  World!
#  1
#  Good bye , World '''
# s8 = 'สวัสดีชาวโลก' 

print('<-------------------->')

# print(s1)
# print(s2)
# print(s3)
# print(s4)
# print(s5)
# print(s6)
# print(s7)
# print(s8)

print('<-------------------->')

# a = 'Hello'
# b = 'Ready'
# c = 'Python'

# print(f"{a} World!.I'm {b} to learn {c}")  #ใส่ format
# print("{} World!.I'm {} to learn {}".format(a,b,c)) #ใส่ format
print('<-------------------->')

# print('Pi is {:.4f}'.format(3.1415926589)) #กำหนดจุดทศนิยมใน วงเล็บ

print('<-------------------->')

print('{:20}'.format('Hello')) #*รวมกับHello = 20 ตัว
# print('{:-^30}'.format(' I LOVE YOU ')) #-รวมกับI LOVE YOU = 30 ตัว

print('<-------------------->')

# hello = 'Hello'
# world = 'World'
# lucky_number = 13.1313
# s1 = 'Hello , {}!'.format(world)
# s2 = '{hello} , {world}!'.format(world = world , hello ='Hellooooo')
# s3 = '{2} => {1} , {0}!'.format(hello , world , lucky_number)
# s4 = '{} , {} ! The lucky number is {} and {:.2f}'.format(hello , world , lucky_number , lucky_number)
# print(s1)
# print(s2)
# print(s3)
# print(s4)

print('<-------------------->')

# s = 'Hello,World!'
# print(s[8])     #r
# print(s[0:7])   #Hello,W
# print(s[8:])    #rld
# print(s[::-1])  #สลับด้าน

# s = "Kankavee!"
# print(s[3])
# print(s[0:5]) #start 0 stop 5
# print(s[3:]) #start 3 จนจบ
# print(s[4:7]) #start 4 stop 7

print('<-------------------->')

# s = ' Hello'
# print(s + 'o'*3)
# print('He' in s)
# print('He' not in 'Hello,World!')

print('<-------------------->')

# print('man' == 'men') #false
# print('man'[:1] == 'men'[:1]) #true
# print('man' < 'men'[:1] + 'an') #false
# print('gentleman'[-3:] < 'men') #true #startท ที่ตำแหน่ง -3
# print('man' in 'gentleman') #true
# print('man' not in 'gentleman'[:-3]) #true
# print('man' not in 'gentleman'[::-1]) #true
# print('man' in 'gentle{}'.format('man')) #true
# print('man' in 'man'*5) #true

print('<-------------------->')


s = 'Hello, World!'
ss = s.split()
print(ss)
print(ss[0].strip(' , ') + ss[1])
print(ss[0].upper() , ss[1].lower())
print(s.index('o'))
print(s.count('l'))
print(s.replace('World','School'))
print(s.capitalize()) #ตัวแรกตัวพิมใหญ่ ที่เหลือพิมเล็ก

print('<-------------------->')



