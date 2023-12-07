# Matplotlib Adding Grid Lines 

print("---------------------------------------")

# Add Grid Lines to a Plot 

# add grid lines to the plot : 

# import numpy as np 
# import matplotlib.pyplot as plt 

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calories Burnage")

# plt.plot(x,y)

# plt.grid()

# plt.show()

print("---------------------------------------")

# Specify Which Grid Lines to Display 

# display only grid lines for the x-axis : 

# import numpy as np 
# import matplotlib.pyplot as plt 

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calories Burnage")

# plt.plot(x,y)

# plt.grid(axis = 'x')

# plt.show()

print("---------------------------------------")

# display only grid lines for the y-axis : 

# import numpy as np 
# import matplotlib.pyplot as plt 

# x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
# y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calories Burnage")

# plt.plot(x,y)

# plt.grid(axis = 'y')

# plt.show()

print("---------------------------------------")

# Set Line Properties for the Grid 

# set the line properties of the grid :

import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calories Burnage")

plt.plot(x,y)

plt.grid(color = 'green',linestyle = '--' ,linewidth = 0.5)

plt.show()

print("---------------------------------------")