# x = "you are my destiny"

# #1
# print(x.capitalize())

# #2
# print(x.replace("are","ARE"))

#3
# result = "Y" + x[1:9] + "Y" + x[10:18]
# print(result)

# #4
# print(x.title())

# #5
# print(x.find("r"))

# #6
# print(x.endswith("d"))

# #7
# print(x.islower())

#8
# print(x[0].isupper())

#9
# print(x[0].islower())

print(" ---------------------------- ")

#10

# text = input()
# count = 0 
# for i in range(len(text)-1,-1,-1) :
#     if text[i] == " " :
#         break
#     else :
#         count += 1

# print(count) #เริ่มนับจากตัวหลัง
    
print(" ---------------------------- ")

#11

username = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
u_score = "_"
num = "0123456789"
status = 1

if len(username) >= 4 and len(username) <= 25 :
    if username[0].isalpha() :
        for i in username :
            if i not in alpha and i not in u_score and i not in num :
              status = 0
        if status == 0 :
            print("NO")
        elif status == 1 :
            if not(username.endswith("_")):
                print("Yes")
            else :
                print("NO")    
    else :
        print("NO")
else :
    print("NO")


