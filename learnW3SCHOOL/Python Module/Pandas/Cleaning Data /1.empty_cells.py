# Empty Cells 

print("------------------------------------")

# Remove Rows

# return a new Data Frame with no empty cells : 

# import pandas as pd

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# new_df = df.dropna()

# print(new_df.to_string())

# Note: By default, the dropna() method returns a new DataFrame, and will not change the original.

print("------------------------------------")

# If you want to change the original DataFrame, use the inplace = True argument:

# remove all roes with NULL values : 

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# new_df = df.dropna(inplace = True)

# print(df.to_string())

print("------------------------------------")

# Replace Empty Values

# replace NULL values with the number 130 : 

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# df.fillna(130 , inplace = True)

# print(df.to_string())

print("------------------------------------")

# Replace Only For Specified Columns 

# replace NULL values in the "Calories" columns with the number 130 : 

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# df["Calories"].fillna(130 , inplace = True )

# print(df.to_string())

print("------------------------------------")

# Replace Using Mean, Median, or Mode

# calculate the MEAN, and replace any empty values with it :

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# x = df["Calories"].mean()

# df["Calories"].fillna(x,inplace = True)

# print(df)

print("------------------------------------")

# calculate the MEDIAN, and replace any empty values with it :

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# x = df["Calories"].median()

# df["Calories"].fillna(x, inplace = True)

# print(df)

print("------------------------------------")

# calculate the MODE, and replace any empty values with it :

import pandas as pd 

df = pd.read_csv("/Users/balast/Downloads/data.csv")

x = df["Calories"].mode()[0]

df["Calories"].fillna(x,inplace = True)

print(df)

print("------------------------------------")

