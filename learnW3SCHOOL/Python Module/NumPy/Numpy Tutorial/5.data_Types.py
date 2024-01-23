#Checking the Data Type of an array

# import numpy as np

# arr = np.array([1,2,3,4])
# print(arr.dtype)

# arr1 = np.array(['apple','banana','cherry'])
# print(arr1.dtype)

print("------------------------------")

#Creating Arrays With a Defined Data Type

import numpy as np

arr = np.array([1,2,3,4],dtype='S')
print(arr)
print(arr.dtype)

arr1 = np.array([1,2,3,4],dtype='i4')
print(arr1)
print(arr1.dtype)

print("------------------------------")

#Converting Data Type on Existing Arrays

# import numpy as np

# arr = np.array([1.1,2.1,3.1])
# newarr = arr.astype('i')

# print(newarr)
# print(newarr.dtype)

# #change data type from float to integer by using int as parameter value :

# arr1 = np.array([1.1,2.1,3.1])
# newarr1 = arr1.astype(int)

# print(newarr1)
# print(newarr1.dtype)

# #change data type from integer to boolean :

# arr2 = np.array([1,0,3])
# newarr2 = arr2.astype(bool)

# print(newarr2)
# print(newarr2.dtype)

print("------------------------------")


