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
    x='WorkLifeBalance',
    hue='Attrition',
    palette='Set2'
)

plt.title('Employee Attrition by Work-Life Balance')

plt.show()

# ==========================
# Attrition Rate
# ==========================

wlb_rate = pd.crosstab(
    df['WorkLifeBalance'],
    df['Attrition'],
    normalize='index'
) * 100

print(wlb_rate.round(2))

# ==========================
# Percentage Chart
# ==========================

wlb_rate['Yes'].plot(
    kind='bar',
    figsize=(8,5),
    color='steelblue'
)

plt.ylabel('Attrition Rate (%)')

plt.xticks(rotation=0)

plt.title('Employee Attrition Rate by Work-Life Balance')

plt.show()