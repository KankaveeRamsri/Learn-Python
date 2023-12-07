#Joining NumPy Arrays
#Join two arrays

# import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.concatenate((arr1,arr2)) #เช่ื่อมต่อกัน

# print(arr)

print("------------------------------")

#Join two 2-D arrays along rows (axis = 1):

# import numpy as np

# arr1 = np.array([[1,2],[3,4,]])
# arr2 = np.array([[5,6],[7,8]])

# arr = np.concatenate((arr1,arr2),axis=1)

# print(arr)

print("------------------------------")

#Joining Arrays Using Stack Function

# import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6]) #(1คู่4 , 2คู่5 , 3คู่6)

# arr = np.stack((arr1,arr2),axis=1)

# print(arr)


print("------------------------------")

#Stacking Along Rows

# import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.hstack((arr1,arr2))

# print(arr)

print("------------------------------")

#Stacking Along Columns

# import numpy as np

# arr1 = np.array([1,2,3])
# arr2 = np.array([4,5,6])

# arr = np.vstack((arr1,arr2))

# print(arr)

print("------------------------------")

#Stacking Along Height(depth)

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

arr = np.dstack((arr1,arr2))

print(arr)

print("------------------------------")