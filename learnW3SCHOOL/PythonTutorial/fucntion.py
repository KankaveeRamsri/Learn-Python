def my_function():
    print("Hello from a function")

# my_function()
print('-'*15)

def my_function_2(fname):
    print("{}Refsnes".format(fname))

# my_function_2("Email")
# my_function_2("Tobias")
# my_function_2("Linus")
print('-'*15)

def my_function_3(fname,lname):
    print(fname + " "+ lname)

# my_function_3("Emil","Refnses")
print('-'*15)

def my_function_4(*kids): #tuple
    print("The youngest child is " + kids[2])

# my_function_4("Emil","Tobias","Linus")
print('-'*15)

def my_function_5(child3,child2,child1):
    print("The youngest child is " + child1)

# my_function_5(child1="Emil",child2="Tobias",child3="Linus")
print('-'*15)

def my_function_6(**kid):
    print("His last name is " + kid["lname"])

# my_function_6(fname="Tobias",lname="Refsnes")
print('-'*15)

def my_function_7(country = "Norway"):
    print("I am from " + country)

# my_function_7("Sweden")
# my_function_7()
print('-'*15)

def my_function_8(food):
    for x in food:
        print(x)

fruits = ["apple","banana","cherry"]
# my_function_8(fruits)
print('-'*15)

def my_function_9(x):
    return 5 * x

# print(my_function_9(3))
# print(my_function_9(5))
# print(my_function_9(9))
print('-'*15)

def tri_recursion(k):
    if k > 0 :
        result = k + tri_recursion(k-1)
        print(result)
    else :
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)
        



