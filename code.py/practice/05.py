# lst = [0,1,2,3,4,5]
# print(lst)
# print(lst[3])
# print(lst[-1])
# lst[3] = 3.3
# print(lst)

# lst[::-1]
# print(lst)
# lst = lst[::-1]
# print(lst)

print('---------------------------------')

# lst = [0,1,2,3,4,5,6,7]
# print(lst)
# x = lst[0:4]
# print(x)
# x[0] = 20
# print(lst)
# print(x)

# print(lst[:4])
# print(lst[4:])
# print(lst[:len(lst)-1])
# print(lst[:-1])

print('---------------------------------')

# lst = [0,1,2]
# print(lst)
# lst.append(3)
# print(lst)
# lst.extend([4,5,6])
# print(lst)
# lst.insert(1,0.5)
# print(lst)

print('---------------------------------')

# lst = [0,1,2,3,2,1,0]
# print(lst)
# lst.remove(1)
# print(lst)
# del(lst[2])
# print(lst)
# val = lst.pop(2)
# print(lst)

print('---------------------------------')

# primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]
# num = int(input("Enter integer 1 - 100 : ")) 
# if 1 <= num <= 100 :
#     if num in primes :
#         print("{} is prime number".format(num))
#     else :
#         print("{} isn't prime number".format(num))
# else :
#     print("{} out of test range")

# print("Good bye !")

print('---------------------------------')

# numbers = list()
# for i in range(1,11) :
#     user_input = int(input("Enter number #{} : ".format(i)))
#     numbers.append(user_input)

# total = 0
# for i in numbers :
#     total += i

# print("Average of input numbers is {}".format(total / len(numbers)))

print('---------------------------------')

height = [100,165,95,170,175,85]
copy_height = height[:]
print(height)
height.sort()
print(height)
height.reverse()
print(height)

print(copy_height)
height.sort(reverse=True)
print(height)