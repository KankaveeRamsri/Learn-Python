#Local variable

# def myfunc():
#     x = 300 
#     print(x)

# myfunc()

print("------------------------------------------")

# def myfunc():
#     x = 300
#     def myinnerfunc():
#         print(x)
#     myinnerfunc()

# myfunc()

print("------------------------------------------")

#Global variable

# x = 300
# def myfunc():
#     print(x)

# myfunc()
# print(x)


print("------------------------------------------")

#Naming Variables

# x = 300
# def myfunc():
#     x = 200
#     print(x)

# myfunc()
# print(x)

print("------------------------------------------")

#Global Keyword

# def myfunc():
#     global x
#     x = 300

# myfunc()
# print(x)

print("------------------------------------------")

x = 300
def myfunc():
    global x
    x = 200

myfunc()
print(x)

print("------------------------------------------")

