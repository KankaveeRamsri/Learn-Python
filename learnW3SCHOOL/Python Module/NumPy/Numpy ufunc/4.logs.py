#Logs

print("-----------------------------------")

#Log at Base 2

#find log at base 2 of all elements of following array :

# import numpy as np 

# arr = np.arange(1,10)

# print(np.log2(arr)) #log2 ฐาน 1-9

print("-----------------------------------")

#Log at Base 10

#find log at base 10 of all elements of following array :

# import numpy as np 

# arr = np.arange(1,10)

# print(np.log10(arr))

print("-----------------------------------")

#Natural Log , or Log at Base e 

#find log at base e of all elements of following array :

# import numpy as np 

# arr = np.arange(1,10)

# print(np.log(arr))

print("-----------------------------------")

#Log at Any Base 

from math import log
import numpy as np

nplog = np.frompyfunc(log,2,1)

print(nplog(100,15))

print("-----------------------------------")


