# def hello() :
#     print("Hello Function")
#     print("Hello Python")
#     print("Hello World")
#     print("Hello Bas")


# hello()

print(" ---------------------------- ")

# def birthday_song(my_friend) :
#     print("Happy birthday to you")
#     print("Happy birthday to you")
#     print("Happy birthday dear " + my_friend)
#     print("Happy birthday to you")

# birthday_song("ploy")

# name = input()
# birthday_song(name)

print(" ---------------------------- ")

# def find_average(n1 , n2 , n3) :
#     avg = (n1 + n2 + n3) / 3
#     return avg

# result = find_average(1,5,3)
# print(result + 3) #ประโยชน์ของการรีเทิน นำค่ามาใช้ต่อได้

print(" ---------------------------- ")

# def find_circum(r , pi = 3.14) :
#     result = 2 * pi * r
#     print(result)

# find_circum(2)

print(" ---------------------------- ")

# def find_sum(ls) :
#     summ = 0
#     for i in ls :
#         summ += i
#     return summ

# result = find_sum([1,2,3])
# print(result)

print(" ---------------------------- ")

# def show_greeting():
#     return "Hello , how are you"

# greeting = show_greeting()
# name = input()
# print(greeting + " " + name)

print(" ---------------------------- ")

# def test_local() :  #global
#     print(var)

# var = 10
# test_local()

print(" ---------------------------- ")

# def test_local() :    #local
#     var = 3
#     print(var)

# var = 10
# test_local()

print(" ---------------------------- ")

# def test_local() : 
#     global var
#     print(var)

# var = 10
# test_local()

print(" ---------------------------- ")

def test_local() : # มอง local ก่อนเสมอ
    global var
    var = 5
    print(var)

var = 10
test_local()