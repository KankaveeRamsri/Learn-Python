while True :
    num = int(input("Enter number ( 8 digits ) : "))
    if len(str(num)) != 8 :
        print("Error , try it again")

    else :
        break

i = num 
sum = 0
while i > 0 :
    a = i % 10
    sum += a
    i //= 10

print("ผลรวมของเลขโดด = ",sum)

