# row = int(input("Enter the number of rows: "))

# for i in range(1,row+1) :
#     print('*'*i)


# numbers = [int(i) for i in input("Input: ").split(',')]

# counter = 0
# for i in numbers :
#     check = i
#     while check % 2 == 0:
#         counter += 1
#         check = check // 2

# print(counter)

numbers = [int(i) for i in input("Input: ").split(',')]

counter = 0 
for i in numbers:
    if i % 2 == 0:
        counter += i//2
        
print("output = ", counter)
        