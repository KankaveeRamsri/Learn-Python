#Uniform Distribution (กระจายสม่ำเสมอ)

#create a 2x3 uniform distribution sample :

# from numpy import random

# x = random.uniform(size=(2,3))

# print(x)


print("------------------------------")

#Visualiztion of Uniform Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000),hist=False)

plt.show()

print("------------------------------")