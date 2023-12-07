# l = ['Kankavee','Peerada' , 'Puntawut' , 'Ronnakrit','Thanchanok','Nathan']
# # print(l[0])
# # print(l)

# # l_1 = l[::-1]
# # print(l_1)

# # x = l[1:]
# # print(x)

# # print(l[: len(l)-1])

# print(l[:-1])

print('---------------------')

# l = [0,1,2,3,4,5,6]
# print(l)
# l[2:4]=[24,46]
# print(l)
# l[2:4]=[2,3,4]
# print(l)
# l[0] =[2.4,4.8]
# print(l)

print('---------------------')

# l = [0,1,2,3]
# print(l)
# l.append(4)
# print(l)
# l.extend([5,6,7,8])
# print(l)
# l.insert(4,3.75)
# print(l)

print('---------------------')

# l = [0,1,2,3,2,1,0]
# print(l)
# l.remove(2) #ทิ้งไปไหนไม่รู้สักที่ช่างแม่ง
# print(l)
# del(l[2])
# print(l)

# val = l.pop(2)
# print(l)
# print("pop val:",val) #หยิบออกแบบไม่ทิ้ง

print('---------------------')

# l1 = [0,1,2]
# l2 = [3,4,5]
# l = l1 + l2
# print(l)

# print("l1 * 3 = ",l1*3)

print('---------------------')

# primes = [2,3,5,7,11,13,17,19,23,29]

# num = int(input("Enter integer  : "))
# if 0 <= num <= 30 :
#     if num in primes :
#         print(num,"is prime number")
#     else :
#         print("is not prime number")
# else :
#     print(num,"out of test range")

# print("Good bye")

print('---------------------')

# name = ["Bas" , "Prince" , "Pin" , "Game" , "Moo"]

# while "Bas" in name :
#     user_input = input("remove name :")
#     index = name.index(user_input)
#     name.remove(name[index])
#     print(name)
# print("Bas isn't in name ")

print('---------------------')


numbers = []
for i in range(0,10) :
    numbers.append(int(input(f'Enter numbser # {i+1}.')))
print(numbers)


# user_input = ""
# count = 0
# while True :
#     user_input = input(f"Enter name or Enter 'end' for exits #{count} ")
#     count = count + 1
#     if user_input == "end" :
#         break
#     numbers.append(int(user_input))

total = 0
for i in numbers :
    total = total + i 
# print(numbers)
print('Average of input numbers is {}'.format(sum(numbers)/len(numbers)))

print('---------------------')

# height = [100,165,95,170,175,85]
# copy_height = height[:]
# print(height)
# height.sort()
# print(height)
# height.reverse()
# print(height)

# print(" ---------------- ")

# print(copy_height)
# height.sort(reverse=True) #merge sort and reverse in 1 line.
# print(height)

print('---------------------')

# height = [100,165,95,170,175,85]
# print(height)

# sorted(height)
# print(height)

# sorted_height = sorted(height) #create new datas in this variable.
# print(height)
# print(sorted_height)

# r_height = sorted(height,reverse=True)
# print(r_height)

print('---------------------')






