#Exception Handling

# try :
#     print(x)
# except :
#     print("An exception occurred")

print("------------------------------------------") 

#Many Exceptions

# try :
#     print(x)
# except NameError :
#     print("Variable x is not defined")
# except :
#     print("Something else went wrong")

print("------------------------------------------") 

#Else

# try :
#     print("Hello")
# except :
#     print("Something went wrong")
# else :
#     print("Nothing went wrong")

print("------------------------------------------") 

#Finally

# try :
#     print(x)
# except :
#     print("Something went wrong")
# finally :
#     print("The 'try except' is finished ")

print("------------------------------------------") 

# try :
#     f = open("demofile.txt")
#     try :
#         f.write("Lorum Ipsum")
#     except :
#         print("Something went wrong when writing to the file")
#     finally :
#         f.close()
# except :
#     print("Something went wrong when opening the file")

print("------------------------------------------") 

#Raise an exception

# x = -1 
# if x < 0 :
#     raise Exception("Sorry,no numbers below zero")

print("------------------------------------------") 

# y = "hello"
# if not type(y) is int :
#     raise TypeError("Only integers are allowed")