thislist = ["apple","banana","cherry"]
print(thislist)
print(len(thislist))

print("------------------------------")

list1 = [True,True,False]
print(type(list1))

print("------------------------------")

thislist = list(("apple","banana","cherry"))
print(thislist)
print(thislist[1])
print(thislist[-1])

print("------------------------------")

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

print("------------------------------")

thislist = ["apple","banana","cherry"]
if "apple" in thislist:
    print("Yes,'apple' is in the fruits list")
    
print("------------------------------")

thislist = ["apple","banana","cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"watermelon")
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# del thislist
# print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
print("------------------------------")

for i in range(len(thislist)):
    print(thislist[i])

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
i = 0 
while i < len(thislist):
    print(thislist[i])
    i += 1

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

print("------------------------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

print("------------------------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

newlist = [x for x in fruits if x != "apple"]
print(newlist)

print("------------------------------")

newlist = [x for x in range(10)]
print(newlist)

print("------------------------------")

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

print("------------------------------")

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

print("------------------------------")

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist.sort(reverse=True) # เรียงลำดับจากมากไปน้อย
print(thislist)

thislist.sort(reverse=False) # เรียงลำดับจากน้อยไปมาก
print(thislist)

print("------------------------------")

def myfunc(n):
    return abs(n-50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

thislist.sort(key=myfunc,reverse=True)
print(thislist)

print("------------------------------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print(thislist)

print("------------------------------")

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

print("------------------------------")

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

print("------------------------------")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

for x in list2:
    list1.append(x)
print(list1)

print("------------------------------")

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

print("------------------------------")



