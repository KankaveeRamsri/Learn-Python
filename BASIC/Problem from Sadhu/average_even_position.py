data_num = list()
for i in range(1,21) :
    user_input = int(input("Enter number #{}: ".format(i)))
    if user_input not in data_num :
        data_num.append(user_input)

data_num.sort()

result = ""
for i in data_num :
    result += str(i)
    result += " "

print("Unique numbers is {}".format(result))

even_position = list()
for i in range(len(data_num)) :
    if i % 2 == 0 :
        even_position.append(data_num[i])

average = sum(even_position)/len(even_position)
print("Average number of even position in list is {:.2f}".format(average))


    