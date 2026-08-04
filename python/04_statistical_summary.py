import pandas as pd

# Load Dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

print('='*40)
print('STATISTICAL SUMMARY')
print('='*40)

print(df.describe())

print('\nCategorical Summary')
print(df.describe(include=['object', 'string']))

attrition_percentage = df['Attrition'].value_counts(normalize=True)*100
print(attrition_percentage)

#feature understanding

print('\n' + '='*50)
print('UNIQUE VALUES PER COLUMN')
print('='*50)

print(df.nunique().sort_values())

df = df.drop(columns=['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'])
print(f'Jumlah kolom SETELAH dibuang : {df.shape[1]}')