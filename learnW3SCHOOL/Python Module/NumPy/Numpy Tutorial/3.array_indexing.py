#Access array elements

# import numpy as np

# arr = np.array([1,2,3,4])
# print(arr[0])
# print(arr[1])
# print(arr[2] + arr[3])

print("------------------------------")

#Access 2-D Arrays

import numpy as np 

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('2nd element on 1st row : {}'.format(arr[0,1]))
print('5nd element on 2nd row : {}'.format(arr[1,4]))

print("------------------------------")

#Access 3-D Arrays

# import numpy as np 

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr[0,1,2])

print("------------------------------")

#Negative Indexing

import numpy as np

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('Last element from 2nd dim : {}'.format(arr[1,-1]))
