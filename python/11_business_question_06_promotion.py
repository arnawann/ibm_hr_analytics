import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv('dataset/WA_Fn-UseC_-HR-Employee-Attrition.csv')

# =====================================
# Boxplot
# =====================================

plt.figure(figsize=(8,5))

sns.boxplot(
    data=df,
    x='Attrition',
    y='YearsSinceLastPromotion',
    palette='Set2'
)

plt.title('Years Since Last Promotion by Employee Attrition')

plt.show()

# =====================================
# Histogram
# =====================================

sns.histplot(
    data=df,
    x='YearsSinceLastPromotion',
    hue='Attrition',
    palette='Set3'
)

plt.title('Distribution of Years Since Last Promotion')

plt.show()

# =====================================
# Mean
# =====================================
print('='*40)
print('Average Years Since Last Promotion')
print('='*40)

print(
    df.groupby('Attrition')['YearsSinceLastPromotion'].mean().round(2)
)