#NumPy GCD Greatest Common Denomination (หารร่วมมาก)

print("-----------------------------------")

#Finding GCD (Greatest Common Denomination)

#find the HCF of the following two numbers :

# import numpy as np

# num1 = 6
# num2 = 9

# x = np.gcd(num1,num2)

# print(x)

print("-----------------------------------")

#Finding GCD in Arrays 

#find the GCD for all of the numbers in the following array :

import numpy as np

arr = np.array([20,8,32,36,16])

x = np.gcd.reduce(arr)

print(x)

print("-----------------------------------")