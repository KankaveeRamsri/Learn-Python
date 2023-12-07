number = [int(i) for i in input("Enter 10 numbers: ").split()]

def check_even_number(list) : 
    even_num_set = set()
    for i in list :
        if i % 2 == 0 :
            even_num_set.add(i)
    return even_num_set

answer = check_even_number(number)
print("Result is {}".format(answer))


