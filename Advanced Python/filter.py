def fun(variable):
    letters = ['a','e','i','o','u']
    return True if variable in letters else False 

sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

filtered = list(filter(fun,sequence))

print("The filtered letters are : {}".format(filtered))

print("---------------------------------")

seq = [0, 1, 2, 3, 5, 8, 13]

result = list(filter(lambda x : x % 2 != 0, seq))
print(result)

result = [x for x in seq if x % 2 == 0]
print(result)

print("---------------------------------")

def is_multiple_of_3(num):
    return num % 3 == 0

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = list(filter(lambda x: is_multiple_of_3(x),numbers))
result = [x for x in numbers if is_multiple_of_3(x)]
print(result)

print("---------------------------------")
