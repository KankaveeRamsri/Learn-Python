row = int(input("Enter the number of rows: "))
symbol = str(input("Enter print symbol: "))

for i in range(row):
        print(' ' * (row - i - 1) + symbol * (i * 2 + 1))
        


