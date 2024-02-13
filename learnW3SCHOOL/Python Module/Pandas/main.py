# import pandas as pd

# mydataset = {
#     'cars':['BMW','Volvo','Ford'], # key ใน dictionary คือ column ใน dataframe
#     'passing':[3,7,2]
# }

# myvar = pd.DataFrame(mydataset)
# print(myvar)

print("---------------------------------")

# import pandas as pd 

# fruits_list = ['Apple',10,'Orange','55.50']
# fruits_df = pd.DataFrame(fruits_list)
# print(fruits_df)

print("---------------------------------")

# import pandas as pd

# fruits_list = {
#     'Name':['Apple', 'Banana', 'Orange','Mango']
# }
# fruits_df = pd.DataFrame(fruits_list, index=['Fruit1', 'Fruit2', 'Fruit3', 'Fruit4'])
# print(fruits_df)

print("---------------------------------")

# import pandas as pd


# student_dict = {"name": ["Joe", "Nat", "Harry"], "age": [20, 21, 19], "marks": [85.10, 77.80, 91.54]}

# student_df = pd.DataFrame(student_dict ,  index=['R1', 'R2', 'R3'])
# print(student_df)

print("---------------------------------")

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')
# print(df.head())
# print('--------------')
# print(df.tail())
# print('--------------')
# print(df.head(-2))
# print('--------------')
# print(df.tail(-3))
# print('--------------')
# print(df.sample())
# print('--------------')

print("---------------------------------")

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')
# print(df.info()) # แสดงข้อมูลของ dataframe โดยละเอียด

print("---------------------------------")

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')
# print(df.describe()) # แสดงข้อมูลทางสถิติเชิงลึกเฉพาะข้อมูลที่เป็นตัวเลข

print("---------------------------------")

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')
# print(df.columns)
# print(df.index)
# print("--------")
# print(df.dtypes)
# print("--------")
# print(df.shape)
# print(df.size)
# print("--------")
# print(df.values)
# print("--------")
# print(df.empty)
# print("--------")
# print(df.get('Name')) # print(df.Name) , print(df['Name'])
# print("--------")
# print(df[['Name', 'Age']])
# print("--------")
# print(df[0::2])
# print("--------")


print("---------------------------------")

# import pandas as pd 


# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')

# new_index = ['R' + str(i) for i in range(20)]

# newdf = df.set_index(pd.Index(new_index))

# print(newdf)

print("---------------------------------")

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')

# new_index = ['R' + str(i) for i in range(20)]

# df = df.set_index(pd.Index(new_index))


# print(df)
# print("----------")
# print(df.at['R0','Name'])
# print("----------")
# print(df.iat[0,1])
# print("----------")
# print(df.loc[['R0', 'R1']])
# print("----------")
# print(df.loc[['R4','R11'],['Student ID','Score']]) # เอาชื่อ
# print("----------")
# print(df.iloc[:2:1, ::]) # เอา index
# print("----------")
# print(df.iloc[7:14:2 , 1:4])

print("---------------------------------")

# import pandas as pd

# student_dict = {
#     'Name':['Joe', 'Nat', 'Harry','Jack','Jose','Jill','Rose'],
#     'Age':[20, 21, 19,17,18,19,17],
#     'Marks':[85.10, 77.80, 91.54,72,87.9,90,72]
# }

# new_index = ['R' + str(i) for i in range(7)]

# df = pd.DataFrame(student_dict,new_index)
# df = df.rename({"Marks":"Scores"},axis='columns')

# # print(df.iloc[1:6:4,::2])
# # print("------------")
# # print(df[(df["Scores"] > 80)])

# print(df.loc[['R0','R2','R5'],['Name','Scores']])
# print("---------")
# print(df[(df["Age"] > 18) & (df["Scores"] > 80)])

print("---------------------------------")

import pandas as pd
import numpy as np

student_dict = {
    "name": ["Joe", "Sam", "Harry"], 
    "age": [20, 21, 19],
    "marks": [85.10, np.nan, 91.54]}

df = pd.DataFrame(student_dict)
print(df)
print("--------")
print(df.notnull())
print("--------")
print(df.isnull())
print("--------")
print(df['name'].isnull())
print("--------")
print(df['name'].isnull().sum())
print("--------")
print(df.info())
print("--------")
print(df.isna())
