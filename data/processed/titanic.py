import pandas as pd

#original
dataFrame = pd.read_csv(r'C:\Users\dagak\OneDrive\Pulpit\titanic\titanic.csv')

#############################PART1#############################

#copy for our project
df = dataFrame.copy()
'''
print(df)
'''

#light preprocessing before ETL 
'''
print(df.info())
print(df.columns)
print(df.head())
print(df.describe())
'''
