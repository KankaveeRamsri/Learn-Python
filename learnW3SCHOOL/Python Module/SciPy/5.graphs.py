# Graphs 

print('---------------------------------')

# Connected Components 

# find all of the connected components with the connected_components() method :

# import numpy as np 
# from scipy.sparse.csgraph import connected_components
# from scipy.sparse import csc_matrix

# arr = np.array([
#     [0,1,2],
#     [1,0,0],
#     [2,0,0]
# ])

# newarr = csc_matrix(arr)

# print(connected_components(newarr))

print('---------------------------------')

# Dijkstra (หาเส้นทางที่สั้นที่สุดในกราฟจากองค์กระกอบหนึ่งไปอีกองค์ประกอบหนึ่ง)

# find the shortest path from element 1 to 2 : 

# import numpy as np 
# from scipy.sparse.csgraph import dijkstra
# from scipy.sparse import csr_matrix

# arr = np.array([
#     [0,1,2],
#     [1,0,0],
#     [2,0,0]
# ])

# newarr = csr_matrix(arr)

# print(dijkstra(newarr,return_predecessors=True,indices=0))

print('---------------------------------')

# Floyd Warshall (หาเส้นทางที่สั้นที่สุดจากคู่องค์ประกอบ)

# find the shortest path between all pairs of elements : 

# import numpy as np 
# from scipy.sparse.csgraph import floyd_warshall
# from scipy.sparse import csr_matrix

# arr = np.array([
#     [0,1,2],
#     [1,0,0],
#     [2,0,0]
# ])

# newarr = csr_matrix(arr)

# print(floyd_warshall(newarr,return_predecessors=True))

print('---------------------------------')

# Bellman Ford (เหมือน Floyd Warshall แต่สามารถจัดการกับค่า weight ที่ติดลบได้)

# find shortest path from element 1 to 2 with given graph with negative weight : 

# import numpy as np 
# from scipy.sparse.csgraph import bellman_ford
# from scipy.sparse import csr_matrix

# arr = np.array([
#     [0,-1,2],
#     [1,0,0],
#     [2,0,0]
# ])

# newarr = csr_matrix(arr)

# print(bellman_ford(newarr,return_predecessors=True,indices=0))

print('---------------------------------')

# Depth First Order 

# traverse the graph depth first for given adjacency matrix : 

# import numpy as np 
# from scipy.sparse.csgraph import depth_first_order
# from scipy.sparse import csr_matrix 

# arr = np.array([
#     [0,1,0,1],
#     [1,1,1,1],
#     [2,1,1,0],
#     [0,1,0,1]
# ])

# newarr = csr_matrix(arr)

# print(depth_first_order(newarr,1))

print('---------------------------------')

# Breadth First Order 

# traverse the graph breadth first for given adjacency : 

# import numpy as np 
# from scipy.sparse.csgraph import breadth_first_order
# from scipy.sparse import csr_matrix

# arr = np.array([
#     [0,1,0,1],
#     [1,1,1,1],
#     [2,1,1,0],
#     [0,1,0,1]
# ])

# newarr = csr_matrix(arr)

# print(breadth_first_order(newarr,1))

print('---------------------------------')




