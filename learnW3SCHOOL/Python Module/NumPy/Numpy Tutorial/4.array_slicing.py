#Slicing arrays

# import numpy as np
# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5])
# print(arr[4:])
# print(arr[:4])

print("------------------------------")

#Negative Sliceing

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[-3:-1])

print("------------------------------")

#Step

# import numpy as np

# arr = np.array([1,2,3,4,5,6,7])
# print(arr[1:5:2])
# print(arr[::2])

print("------------------------------")

#Slicing 2-D Arrays

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
print(arr[0:2,2]) #from both elements,return index 2
print(arr[0:2,1:4])

print("------------------------------")


