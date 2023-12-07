# Data of Wrong Format

print("------------------------------------")

# Convert Into a Correct Form 

# convert to date : 

import pandas as pd 

df = pd.read_csv('/Users/balast/Desktop/text.txt')

# df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())