#How to create your own ufunc

#create your own ufunc for addition :

# import numpy as np 

# def myadd(x,y) :
#     return x + y

# myadd = np.frompyfunc(myadd,2,1) # input = 2 , output = 1

# print(myadd([1,2,3,4],[5,6,7,8]))

print("-----------------------------------")

#Check if a Function is a ufunc

import numpy as np

#check if a function is a ufunc :
print(type(np.add))

#check the type of another fucntion : concatenate() :
print(type(np.concatenate))

#check the type of something that does not exist.This will produce an error :
# print(type(np.blahblah))

#use an if statement to check if the function is a ufunc or not :
if type(np.add) == np.ufunc :
    print("add is ufunc")
else :
    print("add is not ufunc")

print("-----------------------------------")

