#Differences

#compute discrete difference of the following array : 

import numpy as np 

arr = np.array([10,15,25,5])

newarr = np.diff(arr)

print(newarr)

print("-----------------------------------")

#compute discrete difference of the following array twice :

import numpy as np 

arr = np.array([10,15,25,5])

newarr = np.diff(arr,n=2)

print(newarr)

print("-----------------------------------")


