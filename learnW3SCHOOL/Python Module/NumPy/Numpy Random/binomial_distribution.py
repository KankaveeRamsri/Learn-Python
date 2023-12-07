#Binomial Distribution

#given 10 trials for coin toss generate 10 data points :

# from numpy import random

# x = random.binomial(n=10,p=0.5,size=10)

# print(x)

print("------------------------------")

#Visualization of Binomial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.binomial(n=10,p=0.5,size=1000),hist=True,kde=False)

plt.show()

print("------------------------------")

#Difference Between Normal and Binomial Distribution

# from numpy import random
# import matplotlib.pyplot as plt
# import seaborn as sns

# sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='normal')
# sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='binomial')

# plt.show() # ส้ม(binomial) , น้ำเงิน(normal)

print("------------------------------")
