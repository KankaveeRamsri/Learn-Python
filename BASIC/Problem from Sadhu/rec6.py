row = int(input("Enter the number of rows: "))
symbol = str(input("Enter print symbol: "))

for i in range(row):
    print(' ' * i + symbol * ((row - i) * 2 - 1))

