x = lambda a : a + 10
print(x(5))
print('-'*15)

x = lambda a,b : a*b
print(x(5,6))
print('-'*15)

x = lambda a,b,c : a+b+c
print(x(1,2,3))
print('-'*15)

def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
print(mytripler(11))
print('-'*15)