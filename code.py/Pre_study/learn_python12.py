import random 
import time
class  Pokemon :
    def __init__(self , name , type , weight , height) :
        self.name = name
        self.type = type
        self.weight = weight
        self.height = height
        self.hp = 100
     
    def eat(self,food):
        if food == 'electric' :
            self.hp += 10

    def print(self) : 
        print("Name :",self.name)
        print('HP :' , self.hp)
        print('type :',self.type)
        print('weight :',self.weight,
              'height :',self.height)
        
    def attack(self,enemy):
        enemy.hp -= 20

    def support(self,sup):
        sup.hp += 10

pikachu = Pokemon('Pikachu', 'electric', 5, 20)
charizard = Pokemon('Charizard', 'fire', 5, 20)

pikachu.print()
print("*"*20)
charizard.print()
pikachu.eat('electric')
pikachu.print()
pikachu.attack(charizard)
print("*"*20,"Pikachu attack Charizard","*"*20)
charizard.print()
print("*"*20)
tong = Pokemon('tong','ghost',5,20)
tong.print()
tong.support(charizard)
print("*"*20 , "tong support charizard" , "*"*20)
charizard.print()




# class Yaiba(Pokemon) :
#     def __init__(self , name , type , weight , height) :
#         super().__init__(name , type , weight , height  )

#     def attackrand(self ,enemy):
#         power = 100
#         enemy.hp -= power
#         print(power)
        
      

        

# uzui = Yaiba('Uzui' , 'Voice' , '5' , '20')  
# uzui.print()
# print('-'*20)
# gyutaro = Yaiba('Gyutaro' , 'Poison' , '5' , '20')
# gyutaro.print()

# uzui_attack = "Uzui"

# uzui_attack == "Uzui"
# if uzui.attackrand(gyutaro) == :
#     gyutaro.print()
#     print("Gyutaro died")



# if uzui_attack == "Uzui" :
#     uzui.attackrand(gyutaro) 
#     gyutaro.print()
#     if gyutaro.hp == 0 :
#         print("Gyutaro died")

