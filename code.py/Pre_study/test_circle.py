r = float(input('Radius is :'))
import math
d = 2 * math.pi * r
a1 = 'a value of d is {:.4f}'.format(d) 
print(a1)

Area = math.pi * (r**r)
print('a value of Area is {:.2f}'.format(Area))

y = float(input('y is :'))
c = r**2
e = y**2
f = c-e
x = math.sqrt(abs(f))
print('x = {:.4f} and -x = {:.4f}'.format(x,-x))