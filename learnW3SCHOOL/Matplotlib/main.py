# import matplotlib.pyplot as plt  # plotting for 2 dimoensions
# import numpy as np

# ypoints = np.array([3,3.5,4.2,5.6,7.8,10.1,12]) # แกน x กำหนดอัติโนมัติ จากลำดับตำแหน่ง

# plt.plot(ypoints)
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt

# values = [3,3.5,4.2,5.6,7.8,10.1,12]

# plt.title('Basis Graph Plotting 01')
# plt.ylabel('Some Values')
# plt.plot(values)
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt

# xpoints = [1, 1.5, 2.5, 2.8, 3.6]
# ypoints = [10, 20, 15, 25, 21]

# plt.title('Basic Graph Plotting 02: XY')
# plt.ylabel('Y-Values')
# plt.xlabel('X-Values')
# plt.plot(xpoints, ypoints)
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt

# xpoints = [1, 1.5, 2.5, 2.8, 3.6]
# ypoints = [10, 20, 15, 25, 21]

# plt.title('Basic Graph Plotting 03: points')
# plt.ylabel('Y-Values')
# plt.xlabel('X-Values')
# plt.plot(xpoints, ypoints, '+')
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt

# xpoints = [1, 1.5, 2.5, 2.8, 3.6]
# ypoints = [10, 20, 15, 25, 21]

# plt.title('Basic Graph Plotting 03: points')
# plt.ylabel('Y-Values')
# plt.xlabel('X-Values')
# plt.plot(xpoints, ypoints, marker = 'o', ms = 20)
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt 

# X = [0, 1, 2, 3, 4, 5, 6]
# Y1 = [0, 29, 60, 89, 122, 151, 180]
# Y2 = [5, 35, 66, 95, 129, 159, 185]
# Y3 = [0, 20, 50, 80, 110, 130, 160]
# plt.title("Basic Graph Plotting 06: Line Styles and Colors")
# plt.plot(X, Y1, '-b') # solid line , blue
# plt.plot(X, Y2, linestyle=':', color ='r') # dotted line , red
# plt.plot(X, Y3, ls ='--', c = 'g') # dashed line,green
# # *** ทางที่ดีควรใส่ชื่อเต็ม ไม่ต้องย่อ
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt 

# X = [0, 1, 2, 3, 4, 5, 6]
# Y1 = [0, 29, 60, 89, 122, 151, 180]
# Y2 = [5, 35, 66, 95, 129, 159, 185]
# Y3 = [0, 20, 50, 80, 110, 130, 160]
# plt.title("Basic Graph Plotting 07: Label and Legend")
# plt.plot(X, Y1, '-b', label = 'Y1') 
# plt.plot(X, Y2, linestyle=':', color ='r', label = 'Y2') 
# plt.plot(X, Y3, ls ='--', c = 'g', label = 'Y3') 
# plt.legend()
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt 
# import numpy as np

# X = np.arange(-5,5,0.1)
# y = 2*X + 10
# fx = pow(X,2) - 2*X + 1
# gx = pow(-X,2) + 2*X + 5

# plt.plot(X,y, 'k', label='y = 2x + 10')
# plt.legend()
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt
# import numpy as np
# X = np.arange(0, 5, 0.1)
# # Subplot #1
# plt.subplot(3, 1, 1) # 3 rows, 1 col
# A = np.sin(X)
# plt.title('sin(x)')
# plt.plot(X,A)

# # Subplot #2
# plt.subplot(3, 1, 2) # 3 rows, 1 col
# plt.title('cos(x)')
# B = np.cos(X)
# plt.plot(X,B)

# # Subplot #3
# plt.subplot(3, 1, 3) # 3 rows, 1 col
# C = np.cos(X)+np.sin(X)
# plt.title('sin(x)+cos(x)')
# plt.plot(X,C)
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt
# import numpy as np
# X = np.arange(0,5,0.1)
# y = 2*X+10

# plt.plot(X, y,color = 'g', label='y = 2x+10')
# plt.title('Prob 3')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt 
# import numpy as np 

# Day = np.array(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
# Sales = np.array([510,240,405,532,625,655,600])

# plt.subplot(1,2,1)
# plt.title('Weekly Sales')
# plt.xlabel('Day')
# plt.ylabel('Sales')
# plt.bar(Day, Sales, color='r')

# plt.subplot(1,2,2)
# plt.title('Weekly Sales')
# plt.xlabel('Sales')
# plt.ylabel('Day')
# plt.barh(Day, Sales, color='r')
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt 
# import numpy as np 

# data = np.array([19,99,70,35,69,93,63,42,84,43,55,20,95,50,32,38,78,36,32,9])

# plt.hist(data,color='r',bins=5) # แบ่งเป็น 5 ช่วง
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt
# import numpy as np

# N = np.array([10, 35, 20, 12, 25])
# fruits = ['apple', 'banana', 'orange', 'grape', 'papaya']


# y = [0.1,0,0.2,0,0]

# plt.pie(N, labels=fruits, explode=y)
# plt.show()

print("-------------------------------")

# import matplotlib.pyplot as plt 

# X = [1, 1.5, -2.5, -2.8, 3.6, 2.7, 3.3, -1]
# Y = [10, 20, 15, 25, 21, 15, 22, 18]

# plt.title('Basic Graph Plotting 04; Scatter')
# plt.ylabel('Y-Values')
# plt.xlabel('X-Values')
# plt.scatter(X, Y)
# plt.show()

print("-------------------------------")

import matplotlib.pyplot as plt
import numpy as np
X = np.arange(-5,5,0.1)

y = 2*X + 10
fx = pow(X,2) + 2*X + 1 


plt.subplot(2,1,1)
plt.title("Prob 4")
plt.plot(X,y,color = 'g',label = 'y = 2x+10')
plt.legend()
plt.ylabel('y')

plt.subplot(2,1,2)
plt.plot(X,fx,label = 'f(x) = x^2+2x+1')
plt.legend()
plt.ylabel('f(x)')
plt.show()