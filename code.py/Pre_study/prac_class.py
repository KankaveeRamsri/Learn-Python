class Player : 
    def __init__(self) : 
        self.fname = ""
        self.lname = ""
        self.number = ""

class Player2 :
    def __init__(self,fname , lname , number) :
        self.fname = fname
        self.lname = lname
        self.number = number
        
p1 = Player()
p1.fname = "Loris"
p1.lname = "Karius"
p1.number = 1

p2 = Player()
p2.fname = "Alex"
p2.lname = "Manninger"
p2.number = 13

p1a = Player2("Loris" , "Karius" , 1)
p2a = Player2("Alex" , "Manninger" , 13)

print(p1a.fname)
print(p1.lname)

print('---------------------')

# def demo_tuple() :
#     p12 = "Joe" , "Gomez" , 12
#     print(p12)
#     print(p12[1])

# def demo_dict() :
#     p12 = {"fname" : "Joe" , "lname" : "Gomez" , "number" : 12}
#     print(p12)
#     print(p12["lname"])

# class Player() :
#     pass

# class Player2() :
#     def __init__(self) :
#         self.fname = ""
#         self.lname = ""
#         self.number = 0

# class Player3() :
#     def __init__(self , fname , lname , number) :
#         self.fname = fname
#         self.lname = lname
#         self.number = number 
        

# def demo_simple_player_class():
#     p12 = Player()
#     p12.fname = "Joe"
#     p12.lname = "Gomez"
#     p12.number = 12
#     print(p12.lname)

# def demo_simple_player2_class() :
#     p12 = Player2()
#     p12.fname = "Joe"
#     p12.lname = "Gomez"
#     p12.number = 12
#     print(p12.lname)

# def demo_simple_player3_class() :
#     p12 = Player3("Joe" , "Gomez", 12)
#     print(p12.lname)


# demo_simple_player_class()
# demo_simple_player2_class()
# demo_simple_player3_class()

print('---------------------')

# class Person() :
#     def __init__(self) :
#         self.fname = ""
#         self.lname = ""
#         self.country = "Thailand"
    
    # def __init__(self , fname , lname , country) :
    #     self.fname = fname
    #     self.lname = lname 
    #     self.country = country

# class Person2() :
#     def __init__(self , fname = None , lname = None , country = "Thailand") :
#         self.fname = fname
#         self.lname = lname 
#         self.country = country
    
#     def __str__(self):
#         return "fname : {} lname : {} country : {}".format(self.fname ,self.lname , self.country)
    


# p1 = Person()
# print(p1.country)

# p2 = Person("Prasert" , "Kana" , "Thailand")
# print(p2)

# p1 = Person2() 
# print(p1.fname)
# print(p1.country)

# p2 = Person2(fname="Peter")
# print(p2.fname , p2.country)

# p3 = Person2("Peter" , "Parker")
# print(p3)

# p4 = Person2(lname = "Swift" , fname = "Taylor" , country = "USA")
# print(p4)

print('---------------------')

class Medal : 
    def __init__(self , country , gold , silver , bronze) :
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze
    
    def total(self) :
        return self.gold + self.silver + self.bronze

    def print(self) :
        print("Country : {}".format(self.country))
        print("Gold : {}".format(self.gold))
        print("Silver : {}".format(self.silver))
        print("Bronze : {}".format(self.bronze))

th = Medal("Thailand" , 5 , 3 , 2)
th.print()
print(th.total())

