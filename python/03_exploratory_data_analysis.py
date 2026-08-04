import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Style
sns.set_style('whitegrid')

# EDA 1 - Attrition Distribution
print(df['Attrition'].value_counts())

plt.figure(figsize=(6,5))
sns.countplot(data=df, x='Attrition', palette='Set1')

plt.title('Employee Attrition Distribution')
plt.xlabel('Attrition')
plt.ylabel('Number of Employees')

plt.show()

# EDA 2 - Department vs Attrition
print(df['Department'].value_counts())

plt.figure(figsize=(8,6))
sns.countplot(data=df, x='Department', hue='Attrition')

plt.title('Department vs Attrition')
plt.xticks(rotation=15)

plt.show()

# EDA 3 - Overtime vs Attrition
print(df['OverTime'].value_counts())

plt.figure(figsize=(6,5))
sns.countplot(data=df, x='OverTime', hue='Attrition')
plt.title('Overtime vs Attrition')

plt.show()

# EDA 4 - Monthly Income
plt.figure(figsize=(8,5))

sns.boxplot(data=df, x='Attrition', y='MonthlyIncome', palette='Set2')
plt.title('Monthly Income by Attrition')

plt.show()

# EDA 5 - Work Life Balance

plt.figure(figsize=(8,5))
sns.countplot(data=df, x='WorkLifeBalance', hue='Attrition', palette='Set3')
plt.title('Work Life Balance vs Attrition')

plt.show()
