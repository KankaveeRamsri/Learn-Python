#Reshape From 1-D to 2-D

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3) #ต้องคูนกันได้เท่าจำนวน elements ของ arr

print(newarr)

print("------------------------------")

#Reshape From 1-D to 3-D

import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(2,3,2)

print(newarr)

print("------------------------------")

#Returns Copy or View ?

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7,8])

# print(arr.reshape(2,4).base)

print("------------------------------")

#Unknown Dimension

# import numpy as np 

# arr = np.array([1,2,3,4,5,6,7,8])

# newarr = arr.reshape(2,2,-1) #ใส่ -1 แล้ว numpy จะคำนวนค่าที่ถูกต้องให้

# print(newarr)

print("------------------------------")

#Flattening the arrays

#Flattening array means converting a multidimensional array into a 1D array.

# import numpy as np 

# arr = np.array([[1,2,3],[4,5,6]])
# newarr = arr.reshape(-1)

# print(newarr)

print("------------------------------")
