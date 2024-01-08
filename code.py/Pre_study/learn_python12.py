import random
import time

class Pokemon:
    def __init__(self, name, type, weight, height):
        self.name = name
        self.type = type
        self.weight = weight
        self.height = height
        self.hp = 100

    def eat(self, food):
        if food == 'electric':
            self.hp += 10

    def print(self):
        print("Name:", self.name)
        print('HP:', self.hp)
        print('Type:', self.type)
        print('Weight:', self.weight, 'Height:', self.height)

    def attack(self, enemy):
        enemy.hp -= 20

    def potion(self, sup):
        sup.hp += 10

# สร้าง Pokemon
pikachu = Pokemon('Pikachu', 'electric', 5, 20)
charizard = Pokemon('Charizard', 'fire', 5, 20)

# ฟังก์ชันสำหรับการต่อสู้
def battle(pokemon1, pokemon2):
    while pokemon1.hp > 0 and pokemon2.hp > 0:
        attacking_pokemon = random.choice([pokemon1, pokemon2])
        
        if random.randint(1, 100) <= 10:
            attacking_pokemon.potion(attacking_pokemon)
            print(f"<<< {attacking_pokemon.name} uses a potion! >>>")
            
        if attacking_pokemon == pokemon1:
            pokemon1.attack(pokemon2)
            print(f">>> {pokemon1.name} attacks {pokemon2.name} <<<")
        else:
            pokemon2.attack(pokemon1)
            print(f">>> {pokemon2.name} attacks {pokemon1.name} <<<")

        # พิมพ์สถานะปัจจุบัน
        pokemon1.print()
        pokemon2.print()
        print("------------------------")

        # หน่วงเวลาเพื่อให้ผู้เล่นเห็นผลของการโจมตี
        time.sleep(3)

    # ตรวจสอบว่าใครชนะ
    if pokemon1.hp <= 0:
        print(f"{pokemon2.name} wins!")
    else:
        print(f"{pokemon1.name} wins!")

# เริ่มต่อสู้
battle(pikachu, charizard)

    

# pikachu = Pokemon('Pikachu', 'electric', 5, 20)
# charizard = Pokemon('Charizard', 'fire', 5, 20)

# pikachu.print()
# print("*"*20)
# charizard.print()
# pikachu.eat('electric')
# pikachu.print()
# pikachu.attack(charizard)
# print("*"*20,"Pikachu attack Charizard","*"*20)
# charizard.print()
# print("*"*20)
# tong = Pokemon('tong','ghost',5,20)
# tong.print()
# tong.support(charizard)
# print("*"*20 , "tong support charizard" , "*"*20)
# charizard.print()




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

