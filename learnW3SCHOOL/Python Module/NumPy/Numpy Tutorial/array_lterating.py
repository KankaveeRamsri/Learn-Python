#Iterating Arrays

# import numpy as np 

# arr = np.array([1,2,3])

# for x in arr :
#     print(x)

print("------------------------------")

#Irerating 2-D Arrays

# import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])

# for x in arr :
#     print(x)

print("------------------------------")

#To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# import numpy as np

# arr = np.array([[1,2,3],[4,5,6]])

# for x in arr :
#     print(x)
#     for y in x :
#         print(y)

print("------------------------------")

#Iterating 3-D Arrays

# import numpy as np

# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# for x in arr :
#     print(x)

print("------------------------------")

#To return the actual values, the scalars, we have to iterate the arrays in each dimension.

# import numpy as np

# arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])

# for x in arr :
#     # print(x)
#     for y in x :
#         # print(y)
#         for z in y :
#             print(z)

print("------------------------------")

#Iterating on Each Scalar Element

# import numpy as np

# arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# for x in np.nditer(arr):
#     print(x)

print("------------------------------")

#Iterating Array With Different Data Types
#Iterate through the array as a string

# import numpy as np

# arr = np.array([1,2,3])

# for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']): #มี flags เพราะ numpy ไม่สามารถเปลี่ยนประเภทของข้อมูลได้จึงจำเป็นต้องมีพื้นที่อื่นในการดำเนินการ
#     print(x)

print("------------------------------")

#Iterating With Different Step Size 
#Iterate through every scalar element of the 2D array skipping 1 element:

# import numpy as np 

# arr = np.array([[1,2,3,4],[5,6,7,8]])

# for x in np.nditer(arr[:,::2]):
#     print(x)

print("------------------------------")

#Enumerated Iteration Using ndenumerate() #แจกแจงการวนซ้ำ

# import numpy as np

# arr = np.array([1,2,3])

# for idx , x in np.ndenumerate(arr):
#     print(idx,x)

print("------------------------------")

#Enumerate on following 2D array's elements :

# import numpy as np

# arr = np.array([[1,2,3,4],[5,6,7,8]])

# for idx,x in np.ndenumerate(arr):
#     print(idx,x)

print("------------------------------")
