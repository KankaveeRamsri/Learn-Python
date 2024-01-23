#Filtering Arrays 

#create an array from the elements on index 0 and 2 :

# import numpy as np 

# arr = np.array([41,42,43,44])
# x = [True,False,True,False]

# newarr = arr[x]

# print(newarr)

print("------------------------------")

#Creating the Filter Arrays

#create a filter array will return only values higher than 42 :

# import numpy as np

# arr = np.array([41,42,43,44])

# filter_arr = list()

# for element in arr :
#     if element > 42 :
#         filter_arr.append(True)
#     else :
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

print("------------------------------")

#create a filter array that will return only even elements from original array :

# import numpy as np 

# arr = np.array([1,2,3,4,5,6,7])

# filter_arr = list()

# for element in arr :
#     if element % 2 == 0 :
#         filter_arr.append(True)
#     else :
#         filter_arr.append(False)

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

print("------------------------------")

#Creating Filter Directly From Array

#create a filter array that will return only values higher than 42 :

# import numpy as np

# arr = np.array([41,42,43,44])

# filter_arr = arr > 42

# newarr = arr[filter_arr]

# print(filter_arr)
# print(newarr)

print("------------------------------")

#create a filter array that will return only even elements from the original array :

import numpy as np 

arr = np.array([1,2,3,4,5,6,7])

filter_arr = arr % 2 == 0

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

print("------------------------------")






