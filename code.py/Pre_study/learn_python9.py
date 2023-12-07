'''
a = 1,2,3
b = 4,5,6
c = a + b
print(c)
x , y , z = a
print("x={} , y={} , z={}".format(x,y,z))

'''

# a , b = input("Enter Name of Movie : ").split()
# print(a)

print("----------------")

# t = ( 1,2,3,4)
# print (t)
# l = list(t)
# l.append('Hello')
# print(l)

# t=tuple(l)
# print(t)

print("----------------")

s0 = {1,2,3}
s1 = set([3,4,5])
s2 = set([4,4,5])

print(s0)
print(s1)
print(s2)

s0.add(4)
s0.add(1)
print(s0)

s0.update(s1)
s0.update(range(0,10,2))
print(s0)

s0.discard(9)