import numpy as np
import matplotlib.pyplot as plt
fname = 'scores240.txt'
with open(fname) as fr:
    ls = fr.read()

ldt = [float(e) for e in ls.split()]
data = np.array(ldt)

plt.hist(data,color='g',bins=5)
plt.xlabel("score")
plt.ylabel("number of students")
plt.grid(linestyle=":",color = 'b')
plt.show()