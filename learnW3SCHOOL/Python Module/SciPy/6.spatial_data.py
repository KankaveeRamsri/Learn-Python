# Spatial Data (ข้อมูลเชิงพื้นที่)

print('---------------------------------')

# Triangulation

# create a triangulation from following points : 

# import numpy as np 
# from scipy.spatial import Delaunay #สร้างสามเหลี่ยมจากจุดต่างๆในรูปหลายเหลี่ยม
# import matplotlib.pyplot as plt 

# points = np.array([
#     [2,4],
#     [3,4],
#     [3,0],
#     [2,2],
#     [4,1]
# ])

# simplices = Delaunay(points).simplices

# plt.triplot(points[:,0],points[:,1],simplices)
# plt.scatter(points[:, 0], points[:, 1], color='r')

# plt.show()

print('---------------------------------')

# Convex Hull 

# create a convex hull for following point : 

# import numpy as np 
# from scipy.spatial import ConvexHull
# import matplotlib.pyplot as plt 

# points = np.array([
#   [2, 4],
#   [3, 4],
#   [3, 0],
#   [2, 2],
#   [4, 1],
#   [1, 2],
#   [5, 0],
#   [3, 1],
#   [1, 2],
#   [0, 2]
# ])

# hull = ConvexHull(points)
# hull_points = hull.simplices

# plt.scatter(points[:,0],points[:,1])
# for simplex in hull_points : 
#     plt.plot(points[simplex,0],points[simplex,1],'k-')

# plt.show()

print('---------------------------------')

# KDTrees

# find the nearest neighbor to point(1,1) :

# from scipy.spatial import KDTree

# points = [(1,-1),(2,3),(-2,3),(2,-3)] 

# kdtree = KDTree(points)

# res = kdtree.query((1,1))

# print(res)

print('---------------------------------')

# Distance Matrix 

print('---------------------------------')

# Euclidean Distance (ระยะทางแบบยุคลิด)

# find the euclidean distance between given points : 

# from scipy.spatial.distance import euclidean

# p1 = (1,0)
# p2 = (10,2)

# res = euclidean(p1,p2)

# print(res)

print('---------------------------------')

# Cityblock Distance (Manhattan Distance) (4 ทิดทาง บน ล่าง ซ้่าย ขวา )

# find the cityblock distance between given points : 

# from scipy.spatial.distance import cityblock

# p1 = (1,0)
# p2 = (10,2)

# res = cityblock(p1,p2)

# print(res)

print('---------------------------------')

# Cosine Distance (ค่า cosine ระหว่างจุด 2 จุด)

# find the cosine distance between given points : 

# from scipy.spatial.distance import cosine

# p1 = (1,0)
# p2 = (10,2)

# res = cosine(p1,p2)


# print(res)

print('---------------------------------')

# Hamming Distance 

# find the hamming distance between given points : 

from scipy.spatial.distance import hamming

p1 = (True,False,True)
p2 = (False,True,True)

res = hamming(p1,p2)

print(res)

print('---------------------------------')














