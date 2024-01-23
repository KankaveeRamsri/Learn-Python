#Copy
# import numpy as np

# arr = np.array([1,2,3,4,5])
# x = arr.copy() 
# arr[0] = 42 #ไม่ส่งผลต่อค่าในตัวแปร x

# print(arr)
# print(x)

print("------------------------------")

#View
# import numpy as np

# arr = np.array([1,2,3,4,5])
# x = arr.view()
# arr[0] = 42 #ส่งผลต่อค่าในตัวแปร x

# print(arr)
# print(x)

print("------------------------------")

#Make Changes in the VIEW 
# import numpy as np

# arr = np.array([1,2,3,4,5])
# x = arr.view()
# x[0] = 31

# print(arr)
# print(x)

print("------------------------------")

#Check if Array Owns its Data

import numpy as np

arr = np.array([1,2,3,4,5])

x = arr.copy() #x is the array owns data will return None
y = arr.view()

print(x.base)
print(y.base)

print("------------------------------")