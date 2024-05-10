# numbers = [12, 13, 14]
# doubled = [x*2 for x in numbers]
# print(doubled)

# print("---------------------------------")

# numbers = [1, 2, 3, 4, 5]
# squared = [pow(x,2) for x in numbers]
# print(squared)

# print("---------------------------------")

# List = [char for char in [1,2,3]]
# print(List)

# print("---------------------------------")

# List = [i for i in range(11) if i % 2 == 0]
# print(List)

# print("---------------------------------")

# matrix = [[j for j in range(5)] for i in range(3)]
# print(matrix)

# print("---------------------------------")

# List = [char for char in 'Geeks 4 Geeks!']
# print(List)

print("---------------------------------")

# Time Analysis in List Comprehensions and Loop 

import time 

def for_loop(n):
    result = []
    for i in range(n):
        result.append(pow(n,2))
    return result 

def list_comprehension(n):
    return [pow(i,2) for i in range(n)]

# Calculate time taken by for_loop()
start = time.time()
for_loop(10**6)
end = time.time()

print('Time taken for_loop : {}'.format(round(end-start,2)))

# Calculate time taken by list_comprehension()
start = time.time()
list_comprehension(10**6)
end = time.time()

print('Time taken for list_comprehension : {}'.format(round(end-start,2)))

print("---------------------------------")

lis = ["Even number" if i % 2 == 0 else "Odd number" for i in range(8)]
print(lis)

print("---------------------------------")

twoDMatrix = [[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]]

trans = [[i[j] for i in twoDMatrix] for j in range(len(twoDMatrix[0]))]

transpose = []
for i in range(len(twoDMatrix[0])):
    transpose.append([])
    for j in twoDMatrix:
        transpose[i].append(j[i])
    

print(trans)
print(transpose)
    

