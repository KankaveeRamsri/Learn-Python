user = input("Enter arabic 5 units  : ")
num = "1234567890"
num_thai = "๑๒๓๔๕๖๗๘๙0"

num1 = num.index(user[0])
num2 = num.index(user[1])
print(num1)
num3 = num.index(user[2])
num4 = num.index(user[3])
num5 = num.index(user[4])
print(num_thai[num1])

print(num_thai[num1]+num_thai[num2]+num_thai[num3]+num_thai[num4]+num_thai[num5])


print(" <------------------------> ")

# user = input("Enter num Thai 5 units :")
# num = "1234567890"
# num_thai = "๑๒๓๔๕๖๗๘๙๐"

# if user.isalpha() :
#     print("Cannot find the result")

# elif user in num :
#     print("a result is",user)

# elif len(user) != 5 :
#     print("Cannot find the result(1)")


# else :
#     numt1 = num_thai.index(user[0])
#     numt2 = num_thai.index(user[1])
#     numt3 = num_thai.index(user[2])
#     numt4 = num_thai.index(user[3])
#     numt5 = num_thai.index(user[4])

#     print(num[numt1] + num[numt2] + num[numt3] + num[numt4] + num[numt5])

    