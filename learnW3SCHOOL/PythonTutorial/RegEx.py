import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$",txt)

if x :
    print("YES! We have a match!")
else :
    print("No match")

print("------------------------------------------")

#The findall() Function

# txt = "The rain in Spain"
# x = re.findall("ai",txt)
# print(x)

# y = re.findall("Portugal",txt)
# print(y)

print("------------------------------------------")

#The search() Function

# txt = "The rain in Spain"
# x = re.search("\s",txt)

# print("The first white-space character is located in position :",x.start())

# y = re.search("Portugal",txt)
# print(y)

print("------------------------------------------")

#The split() Function

# txt = "The rain in Spain"
# x = re.split("\s",txt)
# print(x)

# y = re.split("\s",txt,2)
# print(y)

print("------------------------------------------")

#The sub() Function

# txt = "The rain in Spain"
# x = re.sub("\s","9",txt)
# print(x)

# y = re.sub("\s","9",txt,2)
# print(y)

print("------------------------------------------")

#Match Objects

# txt = "The rain in Spain"
# x = re.search(r"\bS\w+",txt)
# print(x.span())
# print(x.string)
# print(x.group())

