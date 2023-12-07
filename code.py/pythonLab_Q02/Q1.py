data = "".split()
while True :
    num = int(input("Please enter a number (6 digits) : "))
    if len(str(num)) > 6 :
        print("Error , try it again !")
    
    else :     
        break
        
data += str(num)
position = int(input("please select the position (1-6) : "))
ans = data[len(str(num)) - position]
print("The digit is {}".format(ans))


