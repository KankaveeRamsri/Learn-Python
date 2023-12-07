class Person : 
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname,self.lastname)

p1 = Person("John","Doe")
p1.printname()

class Student(Person):
    pass #ถ้าไม่ต้องการเพิ่มอะไรให้ใช้ pass

x = Student("Mike","Olsen")
x.printname()

print("------------------------------------------")

class Person : 
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear,'.')

p1 = Student("Kankavee","Ramsri",2007)
p1.welcome()

