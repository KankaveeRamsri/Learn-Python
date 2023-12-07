# Matplotlib Subplot 

print("---------------------------------------")

# Display Multiple Plots 

# draw 2 plots : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# # plot 1 : 
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])

# plt.subplot(1,2,1)
# # the figure has 1 row , 2 columns ,and this plot is the first plot.
# plt.plot(x,y)

# # plot 2 : 
# x = np.array([0,1,2,3])
# y = np.array([10,20,30,40])

# plt.subplot(1,2,2)
# # the figure has 1 row , 2 columns ,and this plot is the second plot.
# plt.plot(x,y)

# plt.show()

print("---------------------------------------")

# draw 2 plots on top of each other : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# # plot 1 : 
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])

# plt.subplot(2,1,1)
# plt.plot(x,y)

# # plot 2 : 
# x = np.array([0,1,2,3])
# y = np.array([10,20,30,40])

# plt.subplot(2,1,2)
# plt.plot(x,y)

# plt.show()

print("---------------------------------------")

# draw 6 plots :

# import matplotlib.pyplot as plt
# import numpy as np

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 1)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 2)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 3)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 4)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# plt.subplot(2, 3, 5)
# plt.plot(x,y)

# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# plt.subplot(2, 3, 6)
# plt.plot(x,y)

# plt.show()

print("---------------------------------------")

# Title 

# 2 plots,with titles : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# # plot 1 : 
# x = np.array([0,1,2,3])
# y = np.array([3,8,1,10])

# plt.subplot(1,2,1)
# plt.plot(x,y)
# plt.title("SALES")

# # plot 2 : 
# x = np.array([0,1,2,3])
# y = np.array([10,20,30,40])

# plt.subplot(1,2,2)
# plt.plot(x,y)
# plt.title("INCOME")

# plt.show()

print("---------------------------------------")

import matplotlib.pyplot as plt 
import numpy as np 

# plot 1 : 
x = np.array([0,1,2,3])
y = np.array([3,8,1,10])

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("SALES")

# plot 2 : 
x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.title("INCOME")

plt.suptitle("MY SHOP")
plt.show()

print("---------------------------------------")



