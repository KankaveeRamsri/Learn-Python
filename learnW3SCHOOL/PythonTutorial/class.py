class Myclass :
    x = 5 

p1 = Myclass()
print(p1.x)

print('-'*15)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# p1 = Person("John",36)
# print("{} is {} years old.".format(p1.name,p1.age))

print('-'*15)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John",36)
print(p1)

print('-'*15)

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
        
#     def myfunc(self):
#         print("Hello,my name is {} and I'm {} years old.".format(self.name,self.age))

# p1 = Person("John",36)
# p1.myfunc()

print('-'*15)

# class Person :
#     def __init__(Puntawat,name,age):
#         Puntawat.name = name
#         Puntawat.age = age
    
#     def myfunc(Samakkee):
#         print("Hello,My name is {}.I'm {} years old.".format(Samakkee.name,Samakkee.age))

# p1 = Person("Art",19)
# p1.myfunc()
# print('-'*15)