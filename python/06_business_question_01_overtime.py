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

#Stacked Bar Chart for percentage of Attrition by OverTime

overtime_attrition.plot(
    kind='bar',
    stacked=True,
    figsize=(6,5)
)

plt.title('Attrition Percentage by Overtime')

plt.ylabel('Percentage')

plt.xticks(rotation=0)

plt.show()