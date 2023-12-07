#Viewing the Data

#get a quick overview by printing the first 10 rows of the DataFrame : 

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# print(df.head(10))

print("------------------------------------")

#print the first 5 rows of the DataFrame :

import pandas as pd

df = pd.read_csv('/Users/balast/Downloads/data.csv')

print(df.head())

print("------------------------------------")

#Print the last 5 rows of the DataFrame :

print(df.tail())

print("------------------------------------")

#Info About the Data

#Print information about the data :

print(df.info())

#Non-Null มีค่าที่ไม่ใช่ค่าว่างจำนวนเท่าใด Ex.ในคอลัมน์ calories มีค่าที่ไม่ใช่ค่าว่าง 164 ค่า แสดงว่ามี 5 แถวในคอลัมน์ calories ที่ไม่มีค่า

print("------------------------------------")




