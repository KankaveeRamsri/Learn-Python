#NumPy LCM Lowest Common Multiple (ตัวคูณร่วมต่ำสุด/ค.ร.น)

print("-----------------------------------")

#Finding LCM (Lowest Common Multiple)

#find the LCM of the following two numbers :

# import numpy as np 

# num1 = 4
# num2 = 6

# x = np.lcm(num1,num2)

# print(x)

print("-----------------------------------")

#Finding LCM in Arrays 

#find the LCM of the values of the following array :

import numpy as np 

arr = np.array([3,6,9])

x = np.lcm.reduce(arr)

print(x)

print("-----------------------------------")


