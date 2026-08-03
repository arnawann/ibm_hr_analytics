import pandas as pd

#Load Dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

print('=' * 50)
print('Data Cleaning')
print('=' * 50)

#Missing Values
print('\nMissing Values :')
print(df.isnull().sum())

#Duplicate Rows
print('\nDuplicate Rows :')
print(df.duplicated().sum())

#Data Types
print('\nData Types :')
print(df.dtypes)

#Unique Values
print('\nUnique Values in categorical columns :')

categorical = df.select_dtypes(include='object')

for col in categorical.columns:
    print(f'\n{col}')
    print(df[col].unique())