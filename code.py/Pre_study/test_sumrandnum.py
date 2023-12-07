import random

random_time = int(input("Enter random time : "))

list_number = []
for i in range(0,random_time) :
    random_number = random.randrange(1,100)
    list_number.append (random_number)
print(list_number)

sumation_of_number = sum(list_number)
average_of_number = sumation_of_number/len(list_number)

print("Sumation of {} and Average is {:.4f}".format(sumation_of_number,average_of_number))