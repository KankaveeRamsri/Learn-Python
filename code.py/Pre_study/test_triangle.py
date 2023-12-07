import math
 
a_CB = int(input("a value of a : "))
b_AC = int(input("a value of b : "))

x = a_CB**2
y = b_AC**2
z = x + y
c_AB = math.sqrt(z)
print("a value of c : " ,c_AB)
print(" A value of degree : {:.4f} ".format(math.degrees(math.atan(a_CB/b_AC))))
print(" A value of degree : {:.4f} ".format(math.degrees(math.atan(b_AC/a_CB))))