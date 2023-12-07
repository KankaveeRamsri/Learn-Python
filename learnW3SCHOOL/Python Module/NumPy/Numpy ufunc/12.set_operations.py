#NumPy Set Operations 

print("-----------------------------------")

#Create Sets in NumPy

#convert following array with repeated elements to a set :

# import numpy as np 

# arr = np.array([1,1,1,2,3,4,5,5,6,7])

# x = np.unique(arr) #the set arrays should only be 1-D arrays.

# print(x)

print("-----------------------------------")

#Finding Union 

#find union of the following two set arrays :

# import numpy as np 

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])

# newarr = np.union1d(arr1,arr2)

# print(newarr)

print("-----------------------------------")

#Finding Intersection 

#find intersection of the following two set arrays :

# import numpy as np 

# arr1 = np.array([1,2,3,4])
# arr2 = np.array([3,4,5,6])

# newarr = np.intersect1d(arr1,arr2,assume_unique=True) #อากิวเม้นตัวสุดท้ายทำให้การคำนวนทางเซ็ตเร็วขึ้น

# print(newarr)

print("-----------------------------------")

#Finding Difference 

#find the difference of the set1 from set2 :

# import numpy as np 

# set1 = np.array([1,2,3,4])
# set2 = np.array([3,4,5,6])

# newarr = np.setdiff1d(set1,set2,assume_unique=True)

# print(newarr) #A-B

print("-----------------------------------")


#Finding Symmetric Difference 

#find the symmetric difference of the set1 and set2 :

# import numpy as np

# set1 = np.array([1,2,3,4])
# set2 = np.array([3,4,5,6])

# newarr = np.setxor1d(set1,set2,assume_unique=True)

# print(newarr) #(A-B) u (B-A)

print("-----------------------------------")


