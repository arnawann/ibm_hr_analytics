import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# ==========================
# Countplot
# ==========================

plt.figure(figsize=(8,5))

sns.countplot(
    data=df,
    x='Department',
    hue='Attrition',
    palette='Set2'
)

plt.title('Employee Attrition by Department')

plt.xticks(rotation=10)

plt.show()

# ==========================
# Attrition Rate
# ==========================

department_rate = pd.crosstab(
    df['Department'],
    df['Attrition'],
    normalize = 'index'
) * 100
print(department_rate)

# ==========================
# Percentage Rate
# ==========================

department_rate['Yes'].sort_values().plot(
    kind='barh',
    figsize=(8,5),
    color='tomato'
)

plt.xlabel('Attrition Rate (%)')
plt.ylabel('Employee Attrition Rate by Department')

plt.show()