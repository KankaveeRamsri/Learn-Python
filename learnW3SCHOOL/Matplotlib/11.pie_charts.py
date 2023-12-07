# Matplotlib Pie Charts

print("---------------------------------------")

# Creating Pie Charts 

# a simple pie chart : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# y = np.array([35,25,25,15])

# plt.pie(y)
# plt.show()

print("---------------------------------------")

# Labels 

# a simple pie chart : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# y = np.array([35,25,25,15])
# mylabels = ["Apples","Bananas","Cherries","Dates"]

# plt.pie(y,labels=mylabels)
# plt.show()

print("---------------------------------------")

# Start Angle 

# start the first wedge at 90 degrees : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# y = np.array([35,25,25,15])
# mylabels = ["Apples","Bananas","Cherries","Dates"]

# plt.pie(y,labels = mylabels,startangle=90)
# plt.show()

print("---------------------------------------")

# Explode 

# pull the "Apples" wedge 0.2 from the center of the pie : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# y = np.array([35,25,25,15])
# mylabels = ["Apples","Bananas","Cherries","Dates"]
# myexplode = [0.5,0.2,0.3,0]

# plt.pie(y,labels = mylabels , explode = myexplode)
# plt.show()

print("---------------------------------------")

# Shadow 

# add a shadow :

# import matplotlib.pyplot as plt 
# import numpy as np 

# y = np.array([35,25,25,15])
# mylabels = ["Apples","Bananas","Cherries","Dates"]
# myexplode = [0.5,0.2,0.3,0]

# plt.pie(y,labels = mylabels , explode = myexplode , shadow = True)
# plt.show()

print("---------------------------------------")

# Colors 

# specify a new color for each wedge : 

# import matplotlib.pyplot as plt 
# import numpy as np 

# y = np.array([35,25,25,15])
# mylabels = ["Apples","Bananas","Cherries","Dates"]
# mycolors = ["black","hotpink","b","#4CAF50"]

# plt.pie(y,labels = mylabels,colors = mycolors)
# plt.show()

print("---------------------------------------")

# Legend 

# add a legend : 

import matplotlib.pyplot as plt 
import numpy as np 

y = np.array([35,25,25,15])
mylabels = ["Apples","Bananas","Cherries","Dates"]

plt.pie(y,labels = mylabels)
plt.legend(title = "Four Fruits :")
plt.show()

print("---------------------------------------")




