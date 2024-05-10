import random 
import math 

lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))

x = random.randint(lower, upper)
chances = round(math.log(upper - lower + 1,2))

print("\n\tYou've only ",chances,
      " chances to guess the integer!\n")

count = 0 
while count < chances:
    count += 1 
    
    guess = int(input("Guess a number:- "))
    
    if guess == x:
        print("Congratulations you did it in ",count, " try")
        break
    elif guess < x:
        print("You guessed too small!")
    elif guess > x:
        print("You guessed too high!")

if count > chances:
    print("\nThe number is {}".format(x))
    print("\tBetter Luck Next time!")