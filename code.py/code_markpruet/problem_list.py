# x = ["dog" , "cat" , "hamster"]
# y = ["bird" , "crocodile"]

#1
# x.append("snake")
# print(x)

print('-------------------')

#2
# x.insert(2,"bird")
# print(x)

print('-------------------')

#3
# x.pop(-1)
# print(x)

print('-------------------')

#4
# x.remove("dog")
# print(x)

print('-------------------')

#5
# x.sort()
# print(x)

print('-------------------')

#6
# x.reverse()
# print(x)

print('-------------------')

#7
# y = x.copy()
# print(y)

print('-------------------')

#8
# x.extend(y)
# print(x)

print('-------------------')

#9
# y.clear()
# print(y)

print('-------------------')

#10
# print(x)
# print(y)

print('-------------------')

#11

# data = []
# while True :
#     num = int(input())
#     if num == -1 :
#         break
#     else :
#         data.append(num)

# print(data)

print('-------------------')

#12

data = []
text = input()
count = 0

for i in text :
    data.append(i)
    count += 1

print(data)
print(count)

print('-------------------')

#13

# data = []

# while True :
#     num = int(input())
#     if num == -1 :
#         break
#     else :
#         data.append(num)

# # print(data)
# data.reverse()
# print(data)

print('-------------------')

#14

# data = []
# for i in range(1,6) :
#     num = int(input())
#     data.append(num)

# summ = sum(data)
# avgg = sum(data)/len(data)
# print(f"sum = {summ} and avg = {avgg}")

print('-------------------')

#15

# data = []
# for i in range(1,11) :
#     score = int(input("Enter score #{} :".format(i)))
#     data.append(score)

# top = max(data)
# kak = min(data)
# avg = sum(data) / len(data)

# print(f"Max = {top}")
# print(f"Min = {kak}")
# print(f"Average = {avg}")

print('-------------------')

#16

# data = []
# counter = 1
# while counter < 11 :
#     score = int(input("Enter score #{} :".format(counter)))
#     if score < 0 or score > 10 :
#         print("score out of range")
#     else :
#         counter += 1
#         data.append(score)

# top = max(data)
# kak = min(data)
# avg = sum(data) / len(data)

# print(f"Max = {top}")
# print(f"Min = {kak}")
# print(f"Average = {avg}")

print('-------------------')

#17

# text = input()
# new_text = []
# if len(text) > 30 :
#     print("Your text out of range")
# else :
#     for i in text :
#         if i in "aeiouAEIOU" :
#             new_text.append(i)

#     print(new_text)

print('-------------------')







