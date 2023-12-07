number = [int(i) for i in input("Enter numbers: ").split()]

even_number = []
for i in number :
    if i % 2 == 0 :
        even_number.append(i)

result = 0
for i in even_number :
    result += i
     
print("Total: {}".format(result))

