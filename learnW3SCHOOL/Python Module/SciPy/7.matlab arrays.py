# Matlab Arrays 

print('---------------------------------')

# Exporting Data in Matlab Format

# export the following array as variable name "vec" to a mat file : 

# from scipy import io 
# import numpy as np 

# arr = np.arange(10)

# io.savemat('arr.mat',{"vec":arr})

print('---------------------------------')

# Import Data from Matlab Format 

# import the array from following mat file : 

from scipy import io 
import numpy as np 

arr = np.array([0,1,2,3,4,5,6,7,8,9])

# Export : 
io.savemat('arr.mat',{"vec":arr})

# Import : 
mydata = io.loadmat('arr.mat', squeeze_me = True)

print(mydata)

# use the variable name "vec" to display only the array from the matlab data :

print(mydata['vec'])

print('---------------------------------')

