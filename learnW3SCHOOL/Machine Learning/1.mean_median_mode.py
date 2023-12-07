# Mean 

# use the NumPy mean() method to find the average speed : 

# import numpy as np 

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = np.mean(speed)

# print(x)

print("---------------------------------------")

# Median 

# use the NumPy median() method to find the middle value : 

# import numpy as np 

# speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# x = np.median(speed)

# print(x)

print("---------------------------------------")

# Mode 

# use the SciPy mode() method to find the number that appears the most : 

from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

x = stats.mode(speed)

print(x)

print("---------------------------------------")
