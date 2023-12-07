# Interpolation (สร้างจุดระหว่างจุดที่กำหนดให้)

print('---------------------------------')

# 1D Interpolation 

# for given xs and ys interpolate values from 2.1,2.2,... to 2.9 : 

# from scipy.interpolate import interp1d
# import numpy as np 

# xs = np.arange(10)
# ys = 2*xs + 1

# interp_func = interp1d(xs,ys)

# newarr = interp_func(np.arange(2.1,3,0.1))

# print(newarr)

print('---------------------------------')

# Spline Interpolation 

# find univariate spline interpolation for 2.1,2.2,...,2.9 for the following non linear points : 

# from scipy.interpolate import UnivariateSpline
# import numpy as np

# xs = np.arange(10)
# ys = xs**2 + np.sin(xs) + 1

# interp_func = UnivariateSpline(xs,ys)

# newarr = interp_func(np.arange(2.1,3,0.1))

# print(newarr)

print('---------------------------------')

# Interpolation with Radial Basis Function 

# interpolate following xs and ys uisng rbf and find values for 2.1,2.2,...,2.9 : 

from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1

interp_func = Rbf(xs, ys)

newarr = interp_func(np.arange(2.1, 3, 0.1))

print(newarr)
