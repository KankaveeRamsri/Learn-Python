keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

myDict = dict(zip(keys,values))

print(myDict)

print("---------------------------------")

dic = dict.fromkeys(range(5),True)
print(dic)

print("---------------------------------")

myDict = {x:pow(x,2) for x in [1,2,3,4,5]}
print(myDict)

print("---------------------------------")

sDict = {char.upper():char*3 for char in sorted('coding')}
print(sDict)

print("---------------------------------")

newdict = {x:pow(x,3) for x in range(10) if pow(x,3) % 4 == 0}
print(newdict)

print("---------------------------------")

l = "GFG"

dic = {
    x: {y: x + y for y in l} for x in l
}

print(dic)

print("---------------------------------")







