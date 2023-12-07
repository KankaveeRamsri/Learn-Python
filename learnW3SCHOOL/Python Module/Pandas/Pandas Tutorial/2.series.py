#What is a Series ? (คอลัมน์ในตาราง)

#create a simple Pandas Series from a list :

# import pandas as pd 

# a = [1,7,2]

# myvar = pd.Series(a)

# print(myvar)

print("------------------------------------")

#Labels

#return the first value of the Series :

# import pandas as pd 

# a = [1,7,2]

# myvar = pd.Series(a)

# print(myvar[0])

print("------------------------------------")

#Create Labels

#create your own labels :

# import pandas as pd 

# a = [1,7,2]

# myvar = pd.Series(a,index=['x','y','z'])

# print(myvar)

# #when you have created labels, you can access an item by referring to the label :

# print(myvar['y'])

print("------------------------------------")

#Key/Value Objects as Series 

#create a simple Pandas Series from a dictonary  : 

# import pandas as pd 

# calories = {"day1" : 420,"day2" : 380 ,"day3" : 390}

# myvar = pd.Series(calories)

# print(myvar)

print("------------------------------------")

#create a Series using only data from "day1" and 'day2' :

# import pandas as pd 

# calories = {"day1" : 420,"day2" : 380 ,"day3" : 390}

# myvar = pd.Series(calories,index = ["day1","day2"])

# print(myvar)

print("------------------------------------")

#DataFrames

#create a DataFrame from two Series :

import pandas as pd 

data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}

myvar = pd.DataFrame(data)

print(myvar)


print("------------------------------------")
