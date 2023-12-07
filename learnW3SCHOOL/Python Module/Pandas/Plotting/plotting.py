# Plotting 

# import pyplot from Matplotlib and visualize our DataFrame :

# import pandas as pd 
# import matplotlib.pyplot as plt 

# df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

# df.plot()

# plt.show()

print('-------------------------------------')

# Scatter Plot (กระจาย)

# import pandas as pd 
# import matplotlib.pyplot as plt 

# df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

# df.plot(kind = 'scatter' , x = 'Duration' , y = 'Calories') # good relationship

# plt.show()


print('-------------------------------------')

# a scatterplot where there are no relationship between the columns : 

# import pandas as pd 
# import matplotlib.pyplot as plt 

# df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

# df.plot(kind = 'scatter' , x = 'Duration' , y = 'Maxpulse')

# plt.show()

print('-------------------------------------')

# Histogram 

import pandas as pd 
import matplotlib.pyplot as plt 

df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

df["Duration"].plot(kind = 'hist')

plt.show()

print('-------------------------------------')






