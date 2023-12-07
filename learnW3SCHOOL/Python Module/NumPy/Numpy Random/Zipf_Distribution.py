#Zipf Distribution

#draw out a sample for zipf distribution with distribution parameter 2 with size 2x3:

# from numpy import random

# x = random.zipf(a=2, size=(2, 3))

# print(x)

print("------------------------------")

#Visualization of Zipf Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

x = random.zipf(a=2, size=1000)
sns.distplot(x[x<10], kde=False) #plot แค่จุดที่มีค่าน้อยกว่า 10 จาก 1000 จุด

plt.show()

print("------------------------------")