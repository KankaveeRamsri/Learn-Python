# Matplotlib Histogram 

print("---------------------------------------")

# Create Histogram 

# a normal data distribution by NumPy :

# import numpy  as np 

# x = np.random.normal(170,10,250) # ความสูงรอบๆ 170 ส่วนเบี่ยงเบนเท่ากับ 10

# print(x)

print("---------------------------------------")

# a simple histogram : 

import numpy as np
import matplotlib.pyplot as plt 

x = np.random.normal(170,10,250)

plt.hist(x)
plt.show()

print("---------------------------------------")

