import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# ==========================
# Boxplot
# ==========================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Attrition',
    y='MonthlyIncome',
    palette='Set1'
)

plt.title('Monthly Income by Employee Attrition')

plt.show()

# ==========================
# Histogram
# ==========================

sns.histplot(
    data=df,
    x='MonthlyIncome',
    hue='Attrition',
    kde=True,
    palette='Set3'
)

plt.title('Distribution of Monthly Income')
plt.show()