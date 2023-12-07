# def print_odd_or_even(value) :
#     if value %2 == 0:
#         print('even number') 
    
#     print('odd number' ) 

# name = input('Enter your name : ')
# print_odd_or_even(len(name))

# number = int(input("Enter student id : "))
# print(f'Your student id is {print_odd_or_even(number)}')

# zipcode = int(input("Enter zip code : "))
# print(f'Zip code is {print_odd_or_even(zipcode)}')


print("---------------------")

# def get_area(width , height ):
#     print(width * height) 

# width1 = float(input("Enter your width : "))
# height2 = float(input("Enter your height : "))
# result = get_area(width1,height2) #เรียกใช้ function
# # print(result) 



print("---------------------")

'''
def get_area() : #ไม่รับ parameter 
    width = float(input("Enter your width :"))
    height = float(input("Enter your height :"))
    return width * height
print(" A result is ",get_area())
print(" A result is ",get_area())

'''

print("---------------------")

# def user_input(num) :
#     data = []
#     for i in range(num) :
#         value = int(input(f'Enter number #{i}.'))
#         data.append(value)
#     return data

# data = user_input(3)
# print(f"before : {data}")
# new_data = data * 5
# print(f"after : {new_data}")

print("---------------------")


# import random
# def average_random_number(num) :
#     data = []
#     for i in range(num) :
#         data.append(random.random())
#     return sum(data)/len(data) , data

# times = int(input("Enter random times : "))
# num_rand , average_num = (average_random_number(times))
# # print(num_rand)
# print("A result is {:.4f}".format(num_rand))
# print("Random numbers : {}" . format(average_num)) 
# # print("a result is {:.4f}".format(average_random_number(4))) #ใส่จำนวนข้อมูล


print("---------------------")

# import random
# def average_random_number(num) :
#     total = 0
#     for i in range(0,num) :
#         total = total + random.random()

#     average = total/num
#     return average

# print(average_random_number(2))

print("---------------------")

# num = int(input("Enter number : "))

# def do_with_num():
#     global num
#     print('num in function : ' , num)
#     num += 20
#     print('num in function after modufy : ' , num)

print("---------------------")

# def rfac(num):
#     data = []
#     if num < 2:
#         return 1
#     data.append(num)
#     print(data)
#     return num * rfac(num-1)

# user = int(input("Select number : "))
# result = rfac(user)
# print("a result is " , result)

print("---------------------")

#นับจำนวนคำ

# def word_count(user) :
#     text = user.split()
#     word = 0 
#     for i in text :
#         if i.isalpha():
#             word = word + 1
#     return word

# while True : 
    
#     user = input(" Select word : ")
#     if user == "end" :
#         break
   
#     word = word_count(user)
#     print("Word in text are {}".format(word))

print("---------------------")

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(5)

print("---------------------")

sum = 0 
for i in range(1,6) :
  sum += i 

print(sum)
  









    
