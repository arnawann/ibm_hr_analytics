import pandas as pd

# Load Dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

print('='*40)
print('STATISTICAL SUMMARY')
print('='*40)

print(df.describe())

print('\nCategorical Summary')
print(df.describe(include='object'))

attrition_percentage = df['Attrition'].value_counts(normalize=True)*100
print(attrition_percentage)