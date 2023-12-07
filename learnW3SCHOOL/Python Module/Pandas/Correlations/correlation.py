# Finding Relationships

# show the relationship between the columns : 

import pandas as pd 

df = pd.read_csv('https://www.w3schools.com/python/pandas/data.csv.txt')

print(df.corr())

print('-----------------------------------')

