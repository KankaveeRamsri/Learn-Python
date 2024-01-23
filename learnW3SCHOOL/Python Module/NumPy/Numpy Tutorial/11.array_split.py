#Splitting Numpy Arrays

#split the array in 3 parts :

# import numpy as np

# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,2)

# print(newarr)

print("------------------------------")

#split the array in 4 parts :

# import numpy as np

# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,4)

# print(newarr)

print("------------------------------")

#Split Into Arrays

#access the splitted arrays :

# import numpy as np

# arr = np.array([1,2,3,4,5,6])
# newarr = np.array_split(arr,3)

# print(newarr[0])
# print(newarr[1])
# print(newarr[2])

print("------------------------------")

#Splitting 2-D Arrays 

#split the 2-D array into three 2-D arrays :

# import numpy as np

# arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
# newarr = np.array_split(arr,3)

# print(newarr)

print("------------------------------")

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr,3)

# print(newarr)

print("------------------------------")

#split the 2-D array into three 2-D arrays along rows :

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.array_split(arr,3,axis=1)

# print(newarr)

print("------------------------------")

#use the hsplit() method to split 2-D array into three 2-D arrays along rows :

# import numpy as np

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
# newarr = np.hsplit(arr,3)

# print(newarr)

print("------------------------------")