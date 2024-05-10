import random

name = input("What is your name? ")
print("Good Luck, {}!".format(name))

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the characters")

guesses = ''
turns = 20

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed += 1

    if failed == 0:
        print("\nYou Win")
        print("The word is :",word)
        break

    print()
    guess = input("Guess a character: ")
    turns -= 1
    print("You have", turns, 'more guesses')

    guesses += guess

    if guess not in word:
        print("Wrong")

    if turns == 0:
        print("You Loose")
