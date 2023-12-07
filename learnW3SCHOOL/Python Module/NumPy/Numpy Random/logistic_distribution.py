#Logistic Distribution

#draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0 :

# from numpy import random

# x = random.logistic(loc=1,scale=2,size=(2,3))

# print(x)

print("------------------------------")

#Visualize of Logistic Distribution

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.logistic(size=1000),hist=False)

# plt.show()

print("------------------------------")

#Difference Between Logistic and Normal Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(scale=2, size=1000), hist=False, label='normal')
sns.distplot(random.logistic(size=1000), hist=False, label='logistic')

plt.show() # ส้ม(logistic) , น้ำเงิน(normal)

print("------------------------------")

