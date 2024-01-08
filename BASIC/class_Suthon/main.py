# class Counter:
#     def __init__(self):
#         self.v = 0 # v ของ self = 0
    
#     def tick(self):
#         self.v += 1

# c = Counter()
# # c.v = -10 # สมมุติ (ทำให้ค่าเปลี่ยน)
# for i in range(5):
#     c.tick()
# print(c.v)

print("--------------------------------------")

# Encapsulation (ปกป้องตัวแปรไม่ให้ค่าเปลี่ยน)

# class Counter:
#     def __init__(self):
#         self.__v = 0
    
#     def tick(self):
#         self.__v += 1
    
#     @property # ทำให้ v เปลี่ยนแปลงค่าไม่ได้
#     def v(self):
#         return self.__v 

# c = Counter()
# for i in range(5):
#     c.tick()

# print(c.v)

print("--------------------------------------")

# Polymorphism

# class Cat:
#     def greet(self):
#         print("Meow")
    
# class Dog:
#     def greet(self):
#         print("Bark")

# cat1 = Cat()
# dog1 = Dog()
# for animal in (cat1, dog1):
#     animal.greet()

# class Animal: # เกิดจากวัตถุแม่ชนิดเดียวกันแต่การทำงานต่างกัน # Object จาก class เดียวกันมีผลลัพธ์ของ method ต่างกัน
#     def __init__(self):
#         pass
    
#     def greet(self):
#         print("Meow")

# class Cat(Animal):
#     pass

# class Dog(Animal):
#     def greet(self):
#         print("Bark")

# cat1 = Cat()
# dog1 = Dog()
# for animal in (cat1, dog1):
#     animal.greet()

print("--------------------------------------")

# Inheritance

class Counter:
    def __init__(self):
        self.v = 0
    
    def tick(self):
        self.v += 1
    

class ResetableCounter(Counter):
    def reset(self):
        self.v = 0

c1 = Counter()
c2 = ResetableCounter()

for i in range(5):
    c1.tick()
print(c1.v)

for i in range(5):
    c2.tick()
print(c2.v)
c2.reset()
print(c2.v)




    