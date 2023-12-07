# Matplotlib Plotting 

print("---------------------------------------")

# Plotting x and y points 

# draw a line in a diagram from position (1,3) to position (8,10) :

# import matplotlib.pyplot as plt 
# import numpy as np 

# xpoints = np.array([1,8])
# ypoints = np.array([3,10])

# plt.plot(xpoints,ypoints)
# plt.show()

print("---------------------------------------")

# Plotting Without Line 

# draw two points in the diagram , one at position (1,3) and one in position (8,10) :

# import matplotlib.pyplot as plt
# import numpy as np 

# xpoints = np.array([1,8])
# ypoints = np.array([3,10])

# plt.plot(xpoints,ypoints,'o')
# plt.show()

print("---------------------------------------")

# Multiple Points 

# draw a line in a diagram from position (1,3) to (2,8) then to (6,1) and finally to position (8,10) : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# xpoints = np.array([1,2,6,8])
# ypoints = np.array([3,8,1,10])

# plt.plot(xpoints,ypoints)
# plt.show()

print("---------------------------------------")

# Default X-Points 

# plotting without x-points : 

import matplotlib.pyplot as plt 
import numpy as np 

ypoints = np.array([3,8,1,10,5,7])

plt.plot(ypoints)
plt.show()

print("---------------------------------------")