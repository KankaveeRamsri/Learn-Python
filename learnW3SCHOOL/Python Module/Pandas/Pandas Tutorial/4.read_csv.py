#Read CSV File 

#load the CSV into a DataFrame : 

# import pandas as pd 

# df = pd.read_csv('/Users/balast/Downloads/data.csv')

# print(df.to_string()) #print the entire dataframe 

# #If you have a large DataFrame with many rows, Pandas will only return the first 5 rows, and the last 5 rows:

# print(df)

print("------------------------------------")

#Max_rows

#check the number of maximum returned rows :

# import pandas as pd 

# print(pd.options.display.max_rows)


print("------------------------------------")

#increase the maximum number of rows to display the entire DataFrame :

import pandas as pd 

pd.options.display.max_rows = 9999

df = pd.read_csv('/Users/balast/Downloads/data.csv')

print(df)

print("------------------------------------")

