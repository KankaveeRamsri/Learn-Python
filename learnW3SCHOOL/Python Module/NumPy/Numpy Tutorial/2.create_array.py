#Create a NumPy ndarray Object
import numpy as np

arr = np.array([1,2,3,4,5]) #List
print(arr)
print(type(arr))

print("------------------------------")

# arr = np.array((1,2,3,4,5)) #Tuple
# print(arr)

print("------------------------------")

#Dimensions in Arrays
# import numpy as np

# #0-D Arrays
# arr = np.array(42)
# print(arr)

# #1-D Array
# arr1 = np.array([1,2,3,4,5])
# print(arr1)

#2-D Arrays
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2)

# #3-D Arrays
# arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
# print(arr3)

print("------------------------------")

#Check Number of Dimensions

import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


print("------------------------------")

#Higher Dimensional Arrays

import numpy as np
arr = np.array([1,2,3,4],ndmin=5)

print(arr)
print('Number of dimensions : {}'.format(arr.ndim))

print("------------------------------")