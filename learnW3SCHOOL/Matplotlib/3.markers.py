# Matplotlib Markers 

print("---------------------------------------")

# Markers 

# mark each point with a circle : 

import matplotlib.pyplot as plt 
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker = 'o')
plt.show()

print("---------------------------------------")

# mark each point with a star : 

# import matplotlib.pyplot as plt 
# import numpy as np

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints,marker = '*')
# plt.show()

print("---------------------------------------")

# Format Strings (fmt) (syntax : marker|line|color) 

# mark each point with a circle : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints,'o:r')
# plt.show()

print("---------------------------------------")

# Maker Size 

# set the size of the markers to 20 : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints,marker = 'o' , ms = 20)
# plt.show()

print("---------------------------------------")

# Marker Color 

# set the EDGE color to red : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints,marker = 'o',ms = 20,mec = 'r')
# plt.show()

print("---------------------------------------")

# set the FACE color to red : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints,marker = 'o',ms = 20 , mfc = 'r')
# plt.show()

print("---------------------------------------")

# set the color of both the edge and the face to red :

# import matplotlib.pyplot as plt 
# import numpy as np 

# ypoints = np.array([3,8,1,10])

# plt.plot(ypoints,marker = 'o',ms=20,mec ='r',mfc = 'r')
# plt.show()

print("---------------------------------------")



