#Generatte Random Number 
#generate a random integer from 0 to 100 :

# from numpy import random

# x = random.randint(100)

# print(x)

print('-------------------------------')

#Generate Random Float
#generate a random float from 0 to 1 :

# from numpy import random

# x = random.rand()

# print(x)

print('-------------------------------')

#Generate Random Array
#generate a 1-D array containing 5 random integers from 0 to 100 :

# from numpy import random

# x = random.randint(100,size=(5))

# print(x)

print('-------------------------------')

#generate a 2-D array with 3 rows , each row containing 5 random integers from 0 to 100 :

# from numpy import random

# x = random.randint(100,size=(3,5))

# print(x)

print('-------------------------------')

#Floats
#generate a 1-D array containing 5 random float :

# from numpy import random

# x = random.rand(5)

# print(x)

print('-------------------------------')

#generate a 2-D array with 3 rows , each rows containing 5 random number :

# from numpy import random

# x = random.rand(3,5)

# print(x)

print('-------------------------------')

#Generate Random Number From Array
#return one of the values in an array :

# from numpy import random

# x = random.choice([3,5,7,9])

# print(x)

print('-------------------------------')

#generate a 2-D array that consists of the values in the array parameter (3,5,7 and 9) :

from numpy import random

x = random.choice([3,5,7,9],size=(3,5))

print(x)

print('-------------------------------')




