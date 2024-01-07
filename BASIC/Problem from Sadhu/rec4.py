row = int(input("Enter the number of rows: "))

for i in range(row,0,-1):
    print(" " * (row-i),end="")
    print('*'*i)
    