#What is a DataFrame ? (ตารางที่มีแถวและคอมลัมน์)

#create a simple Pandas DataFrame 

# import pandas as pd 

# data = {
#     "calories" : [420,380,390],
#     "duration" : [50,40,45]
# }

# #load data into a DataFrame object : 

# df = pd.DataFrame(data)

# print(df)

print("------------------------------------")

#Locate Row 

#return row 0 :

import pandas as pd 

data = {
    "calories" : [420,380,390],
    "duration" : [50,40,45]
}

df = pd.DataFrame(data)

print(df.loc[0]) #series
print(df.loc[[0,1]]) #dataframe

print("------------------------------------")

#Named Indexes 

#add a list of names to give each row a name : 

# import pandas as pd 

# data = {
#     "calories" : [420,380,390],
#     "duration" : [50,40,45]
# }

# df  = pd.DataFrame(data,index=["day1","day2","day3"])

# print(df)

print("------------------------------------")

#Locate Named Indexes 

#return "day2" : 

# import pandas as pd 

# data = {
#     "calories" : [420,380,390],
#     "duration" : [50,40,45]
# }

# df  = pd.DataFrame(data,index=["day1","day2","day3"])

# print(df.loc["day2"])

print("------------------------------------")

#Load Files Into a DataFrame

#load a comam separated file (CSV file) into a DataFrame :

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/datatest.csv')

# print(df)

print("------------------------------------")


