import pandas as pd

#Read Dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

#Dataset Overview
print('=' * 40)
print('IBM HR Analytics Dataset')
print('=' * 40)

print(f'Rows : {df.shape[0]}')
print(f'Columns : {df.shape[1]}')

print(f'\nMissing Values : {df.isnull().sum().sum()}')
print(f'Duplicated Rows : {df.duplicated().sum()}')

print('\nColumns :')
print(df.columns.tolist())