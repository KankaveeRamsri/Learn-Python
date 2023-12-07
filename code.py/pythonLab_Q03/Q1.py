data = []
for i in range(1,11) :
    score = int(input("Enter score student #{} : ".format(i)))
    data.append(score)

result_1 = sum(data)
result_2 = result_1 / len(data)
print("Sum of scores is {}".format(result_1))
print("Average score is {:.2f}".format(result_2))

