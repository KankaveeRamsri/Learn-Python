# mytuple = ("apple","banana","cherry")
# myit = iter(mytuple)

# print(next(myit)) # bluit in function 
# print(next(myit))
# print(next(myit))

print("------------------------------------------")

import datetime 

mystr = "banana"
myit = iter(mystr)

start_time = datetime.datetime.now()
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
stop_time = datetime.datetime.now()
print("Time : {}".format(stop_time - start_time))

print("--------")

start_time = datetime.datetime.now()
for i in mystr :
    print(i)
stop_time = datetime.datetime.now()
print("Time : {}".format(stop_time - start_time))

print("------------------------------------------")

# mytuple = ("apple","banana","cherry")

# for i in mytuple : # ทำงาน 4 ครั้ง ครั้งสุดท้าย return None 
#     print(i)

print("------------------------------------------")

# mystr = "banana"

# for i in mystr :
#     print(i)

print("------------------------------------------")

class MyNumbers :
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1 
        return x

myclass = MyNumbers()
myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

print("------------------------------------------")

# class MyNumbers :
#     def __iter__(self):
#         self.a = 1
#         return self
    
#     def __next__(self):
#         if self.a <= 20 :
#             x = self.a
#             self.a += 1
#             return x
#         else :
#             raise StopIteration # Stop execution

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter :
#     print(x)

print("------------------------------------------")