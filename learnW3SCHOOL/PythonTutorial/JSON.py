import json 

#Parse JSON - Convert from JSON to Python

#some JSON :
# x = '{"name":"John","age":30,"city":"New York"}'

# #parse x :
# y = json.loads(x)

# #the result is a Python dictionary :
# print(y["age"])

print("------------------------------------------")

#Convert from Python to JSON

# a Pythin object (dict) :
# x = {
#     "name" : "John",
#     "age" : 30,
#     "city" : "New York"
# }

# # convert into JSON :
# y = json.dumps(x)

# # the result is a JSON string :
# print(y)

print("------------------------------------------")

#Convert from Python to JSON

# print(json.dumps({"name":"John","age":30})) #dict
# print(json.dumps(["apple","banana"])) #list
# print(json.dumps(("apple","banana"))) #tuple
# print(json.dumps("hello")) #string
# print(json.dumps(42)) #int
# print(json.dumps(31.76)) #float
# print(json.dumps(True)) #True
# print(json.dumps(False)) #False
# print(json.dumps(None)) #None

print("------------------------------------------")

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# print(json.dumps(x))

#Format the Result

# print(json.dumps(x,indent=4))

# print(json.dumps(x, indent=4, separators=(". ", " = ")))

#Order the Result

# print(json.dumps(x,indent=4,sort_keys=True))