# Statistical Significance Tests (ผลลัพธ์ที่เกิดขึ้นโดยมีเหตุผลอยู่เบื้องหลัง)

print('---------------------------------')

# T-Test 

# find if the given values v1 and v2 are from same distribution : 

# import numpy as np 
# from scipy.stats import ttest_ind

# v1 = np.random.normal(size=100)
# v2 = np.random.normal(size=100)

# res = ttest_ind(v1,v2)

# print(res)

print('---------------------------------')

# KS-Test 

# find if the given value follows the normal distribution : 

# import numpy as np
# from scipy.stats import kstest

# v = np.random.normal(size=100)

# res = kstest(v,'norm')

# print(res)

print('---------------------------------')

# Statistical Description of Data

# show statistical description of the values in an array : 

# import numpy as np 
# from scipy.stats import describe

# v = np.random.normal(size=100)
# res = describe(v)

# print(res)

print('---------------------------------')

# Normality Tests (Skeness and Kurtosis) (ความเบ้และเคอร์โทซิส)

# find skewness and kurtosis of values in an array : 

# import numpy as np 
# from scipy.stats import skew,kurtosis

# v = np.random.normal(size=100)

# print(skew(v))
# print(kurtosis(v))

print('---------------------------------')

# find if the data comes from a normal distribution : 

import numpy as np 
from scipy.stats import normaltest

v = np.random.normal(size=100)

print(normaltest(v))

print('---------------------------------')









