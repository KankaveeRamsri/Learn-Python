# data_num = []
# while True :
#     user_input = int(input("Enter number: "))
#     if user_input >= 0 :
#         data_num.append(user_input)
#     else :
#         break

# data_num.sort()
# print("Minimum number is {}".format(data_num[0]))
# print("Maximum number is {}".format(data_num[-1]))


number = sorted([int(i) for i in input().split()])
print(number)