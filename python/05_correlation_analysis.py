import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Drop identifier columns
df = df.drop(columns=['EmployeeCount', 'EmployeeNumber', 'Over18', 'StandardHours'])

# Encode target variable

df['Attrition'] = df['Attrition'].map({'Yes': 1, 'No': 0})

# Correlation matrix

corr = df.corr(numeric_only=True)

# Heatmap

sns.heatmap(
    corr,
    cmap='coolwarm',
    center=0
)

plt.title('Correlation Matrix')
plt.show()

# Correlation with Attrition
print('\nCorrelation with Attrition')
print('='*40)

corr_attrition = corr['Attrition'].sort_values()

print(corr_attrition)

# Horizontal Bar Chart
plt.figure(figsize=(8,8))

corr_attrition.drop('Attrition').plot(kind='barh')

plt.title('Correlation with Employee Attrition')
plt.xlabel('Correlation')

plt.show()