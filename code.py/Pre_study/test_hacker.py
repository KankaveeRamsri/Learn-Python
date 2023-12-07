import string
user = input("Enter your alphabet 5 units : ")
user = user.lower()
lowercase_1 = string.ascii_lowercase
lowercase_2 = string.ascii_lowercase[::-1]


alphabet1 = lowercase_1.index(user[0])
alphabet2 = lowercase_1.index(user[1])
alphabet3 = lowercase_1.index(user[2])
alphabet4 = lowercase_1.index(user[3])
alphabet5 = lowercase_1.index(user[4])

print(lowercase_2[alphabet1]+lowercase_2[alphabet2]+lowercase_2[alphabet3]+lowercase_2[alphabet4]+lowercase_2[alphabet5])
