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

# import pandas as pd
# import numpy as np

# student_dict = {
#     "name": ["Joe", "Sam", "Harry"], 
#     "age": [20, 21, 19],
#     "marks": [85.10, np.nan, 91.54]}

# df = pd.DataFrame(student_dict)
# print(df)
# print("--------")
# print(df.notnull())
# print("--------")
# print(df.isnull())
# print("--------")
# print(df['name'].isnull())
# print("--------")
# print(df['name'].isnull().sum())
# print("--------")
# print(df.info())
# print("--------")
# print(df.isna())

print("---------------------------------")

# import pandas as pd
# import numpy as np

# student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}
# df = pd.DataFrame(student_dict)
# # print(df)

# # print("---------------")

# # df1 = df.fillna(0)
# # print(df1)
# # print("---------------")
# # print(df)
# # print("---------------")

# # df.fillna(0,inplace=True) # เปลี่ยนค่าบน original dataframe
# # print(df)
# # print("---------------")
# # print(df["marks"].mean())
# # print("\nReplace NaN with means:")
# # df1 = df.fillna(df["marks"].mean())
# # print(df1)

# # print("---------------")

# # change_dict = {'name': 'John Doe', 'marks': -100, 'total mark': 0} # หา column ใน df ที่มีค่า null
# # df1 = df.fillna(value=change_dict)
# # print(df1)

# print("---------------")

# # student_dict = {"name": ["Joe", "Sam", "Harry"], "age": [20, 21, 19], "marks": [85.10, np.nan, 91.54]}
# # df = pd.DataFrame(student_dict)
# # print(df)

# print("---------------")

# # df1 = df.reindex([0, 1, 2, 3]) # เพิ่มแถวสาม
# # print(df1)
# # print("---------------")
# # change_dict = {'name': 'John Doe', 'marks': -100, 'total mark': 0}
# # df1 = df1.fillna(value=change_dict)
# # print(df1)

# print("---------------")

# temp_dict = {'one':[1,2,3,4,5,2000],
#             'two':[1000,np.nan,3,4,5,6]}
# print(temp_dict)
# print("---------------")
# df = pd.DataFrame(temp_dict)
# print(df)
# print("---------------")
# # print(df.replace({1000:-10,2000:5,np.nan:20}))
# print("---------------")
# # print(df.replace({1000:df['two'].mean()}))
# print("---------------")
# # print(df.replace({1000:df['one'].mean()}))
# print("---------------")
# print(df.dropna(axis=0))
# print("------------------------------")
# print(df.dropna(axis=1))

print("---------------------------------")

# import pandas as pd
 
# student_dict = {"name": ["Joe", "Nat", "Harry", "Joe", "Nat"], "age": [20, 21, 19, 20, 21],
#                 "marks": [70, 77.80, 91.54, 85.10, 77.80]}
 
# student_df = pd.DataFrame(student_dict)
# print(student_df)
# print("---------------")
# print(student_df.duplicated('name'))
# print("---------------")
# print(student_df.duplicated('age'))
# print("---------------")
# print(student_df.duplicated('marks'))

print("---------------------------------")

# import pandas as pd

# student_dict = {"name": ["Joe", "Nat", "Harry", "Nat"], "age": [20, 21, 19, 21],
#                 "marks": [70, 77.80, 91.54, 77.80]}

# # Create DataFrame from dict
# # print('Before')
# # student_df = pd.DataFrame(student_dict)
# # print(student_df)

# # print('\nAfter')
# # # drop duplicate rows
# # student_df = student_df.drop_duplicates()

# # print(student_df)

# # print('Before')
# # student_df = pd.DataFrame(student_dict)
# # print(student_df)

# # print('\nAfter')
# # # drop duplicate rows
# # student_df = student_df.drop_duplicates(keep='last') # เก็บแถวสุดท้ายไว้
# # print(student_df)

# print("---------------------------------")

# print('Before')
# student_df = pd.DataFrame(student_dict)
# print(student_df)

# print('\nAfter')
# student_df = student_df.drop_duplicates(keep=False) # ตัดแถวที่ซ้ำออกให้หมด
# print(student_df)

print("---------------------------------")

# import pandas as pd
 
# student_dict = {"name":["Joe","Nat","Harry","Sam" ], "age":[20,21,19,21], "marks":[85.10, 77.80, 91.54, 77.80]}
 
# # Create DataFrame from dict
# print('Before')
# student_df = pd.DataFrame(student_dict)
# print(student_df)
 
# print('\nAfter')
# # drop duplicate rows
# student_df = student_df.drop_duplicates(subset=['age','marks'],keep='last')
 
# print(student_df)


print("---------------------------------")

# import pandas as pd 
# import matplotlib.pyplot as plt

# df = pd.read_csv('/Users/balast/Downloads/mystudents.csv')

# print(df)

# print("-----------")

# print(df.dropna())

# print("-----------")

# temp = df [df['Age'] < 0]
# print(temp)

# print("-----------")

# # print(df.hist())

# # print(df.boxplot(column=['Student ID']))

# print(df['Age'].value_counts())

print("---------------------------------")

# import pandas as pd
# df1 = pd.read_csv('https://raw.githubusercontent.com/TrainingByPackt/Data-Science-with-Python/master/Chapter01/Data/mark.csv',header = 0)
# df2 = pd.read_csv('https://raw.githubusercontent.com/TrainingByPackt/Data-Science-with-Python/master/Chapter01/Data/student.csv',header = 0)

# print(df1)
# print(df2)
# print(pd.merge(df1,df2, on='Student_id'))

print("---------------------------------")

# import pandas as pd
 
# # create dataframe from dict
# print('student_df')
# student_dict = {'Name': ['Joe', 'Nat'], 'Age': [20, 21]}
# student_df = pd.DataFrame(student_dict)
# print(student_df)
 
# print('\nmarks_df')
# # create dataframe from dict
# marks_dict = {'Marks': [85.10, 77.80]}
# marks_df = pd.DataFrame(marks_dict)
# print(marks_df)
 
# print('\njoined _df')
# # join dfs
# joined_df = student_df.join(marks_df)
# print(joined_df)

print("---------------------------------")

# import pandas as pd
 
# student_dict1 = {"name": ["Joe", "Nat"], "age": [20, 21, ], "marks": [85.10, 77.80, ]}
# student_dict2 = {"name": [ "Harry", "Nat"], "age": [19, 21], "marks": [91.54, 77.80]}
# print('student_df1')
# # Create DataFrame from dict
# student_df1 = pd.DataFrame(student_dict1)
# print(student_df1)
 
# print('\nstudent_df2')
# # Create DataFrame from dict
# student_df2 = pd.DataFrame(student_dict2)
# print(student_df2)
 
# print('\ncombined')
# combined_df = pd.concat([student_df1, student_df2], axis=1)  # (axis = 0 for row, axis = 1 for columns)
# print(combined_df)

print("---------------------------------")

# import pandas as pd

# # Create DataFrame from dict
# student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Class': ['A', 'B', 'A'], 'Marks': [85.10, 77.80, 91.54]}
# student_df = pd.DataFrame(student_dict)
# print(student_df)

# print('\nGroupby mean')
# # apply group by
# student_df = student_df.groupby('Class').mean()
# student_df = student_df.reset_index()
# print(student_df)

print("---------------------------------")

# import pandas as pd

# # Create DataFrame from dict
# student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Class': ['A', 'B', 'A'], 'Marks': [85.10, 77.80, 91.54]}
# student_df = pd.DataFrame(student_dict)
# print(student_df)

# print("-----")

# print('\naggregate')
# student_stat = student_df['Marks']
# print("-----")
# print(student_stat)
# print("-----")
# student_stat = student_stat.agg(['sum', 'max','mean'])
# print(student_stat)
# print("-----")

print("---------------------------------")

# import pandas as pd
 
# # Create DataFrame from dict
# student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Class': ['A', 'B', 'A'], 'Marks': [85.10, 77.80, 91.54]}
# student_df = pd.DataFrame(student_dict)
# print(student_df)
 
# print('\nTranspose View')
# print(student_df.T)

print("---------------------------------")

# import pandas as pd
# import numpy as np
# df = pd.read_csv("https://raw.githubusercontent.com/TrainingByPackt/Data-Science-with-Python/master/Chapter01/Data/student.csv")
# # print(df.head())

# print("---------------")

# df_categorical = df.select_dtypes(exclude=np.number)
# print(df_categorical.head())

# print("---------------")


# df_categorical['Gender'].unique()

# df_categorical = df_categorical.replace({'Male': 1, 'Female': 2})

# print(df_categorical)

# print("---------------")


# from sklearn.preprocessing import LabelEncoder
# label_encoder = LabelEncoder()

# # df['Gender'] = label_encoder.fit_transform(df['Gender'])
# df['Grade'] = label_encoder.fit_transform(df['Grade'])
# print(df.head(10))

print("---------------------------------")

# import pandas as pd
 
# # Create DataFrame from dict
# student_dict = {'Name': ['Joe', 'Nat', 'Harry'], 'Class': ['A', 'B', 'A'], 'Marks': [65.10, 55.80, 71.54]}
# student_df = pd.DataFrame(student_dict)
# print(student_df)


# student_df = pd.DataFrame(student_dict)
# student_df['Marks'] = student_df['Marks'] + 10
# print(student_df)

# student_df = pd.DataFrame(student_dict)
# student_df['Marks'] = 0
# print(student_df)

import pandas as pd

# สร้าง DataFrame ตัวอย่าง
data = {'A': [1, 2, None, 4],
        'B': [5, None, 7, 8],
        'C': [9, 10, 11, 12]}

df = pd.DataFrame(data)
print(df)
nan = df.isna().sum()
df = df.drop(columns = nan[nan > 0.5 * len(df)].index)

print(nan)
print(len(df))

