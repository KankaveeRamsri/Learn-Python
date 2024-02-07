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

import matplotlib.pyplot as plt
import numpy as np
X = np.arange(-5,5,0.1)
y = 2*X+5
fx = X**2+2*X+1
plt.plot(X, y,color = 'g', label='y = 2x+10')
plt.plot(X, fx, label='f(x)=x^2+2x+1')
plt.xlabel("x")
plt.ylabel("f(x) or y")
plt.title('Prob 1')
plt.legend()
plt.grid()
plt.show()

