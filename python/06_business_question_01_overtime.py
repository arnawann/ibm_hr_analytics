import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset

df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# Countplot

plt.figure(figsize=(6,5))

sns.countplot(
    data=df,
    x='OverTime',
    hue='Attrition'

)

plt.title('Employee Attrition by Overtime')

plt.show()

#percentage

overtime_attrition = pd.crosstab(
    df['OverTime'],
    df['Attrition'],
    normalize='index'
) * 100

print(overtime_attrition)