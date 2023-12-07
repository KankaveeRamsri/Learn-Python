data = []
for i in range(1,11) :
    num = int(input("Enter num user #{} : ".format(i)))
    data.append(num)

result_1 = min(data)
result_2 = max(data)
print("Minimum is {}".format(result_1))
print("Maximum is {}".format(result_2))