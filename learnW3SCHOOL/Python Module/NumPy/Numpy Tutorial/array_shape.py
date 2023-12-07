#Get the Shape of an Array 
# import numpy as np 

# arr = np.array([[1,2,3,4],[5,6,7,8]])

# print(arr.shape) #อาร์เรย์มี 2 มิติ มิติแรกมีสององค์ประกอบ มิติที่สองมี 4 องค์ประกอบ

print("------------------------------")

import numpy as np

arr = np.array([1,2,3,4],ndmin=5)

print(arr)
print('shape of array : {}'.format(arr.shape))

print("------------------------------")