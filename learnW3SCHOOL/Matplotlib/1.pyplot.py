# Matplotlib Pyplot 

print("---------------------------------------")

# Pyplot 

# draw a line in a diagram from position (0,0) to position (6,250) :

import matplotlib
import matplotlib.pyplot as plt 
import numpy as np 

print('Matplotlib version :', matplotlib.__version__)

xpoints = np.array([0,6])
ypoints = np.array([0,250])

plt.plot(xpoints,ypoints)
plt.show()

print("---------------------------------------")