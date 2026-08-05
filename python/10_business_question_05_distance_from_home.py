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
    y='DistanceFromHome',
    palette='Set2'
)

plt.title('Distance from Home by Employee Attrition')

plt.show()

# =====================================
# Histogram
# =====================================

plt.figure(figsize=(8,5))

sns.histplot(
    data=df,
    x='DistanceFromHome',
    hue='Attrition',
    kde=True,
    palette='Set3'
)

plt.title('Distribution of Distance from Home')

# =====================================
# Mean Distance
# =====================================

print('='*40)
print('Average Distance from Home')
print('='*40)

print(
    df.groupby('Attrition')['DistanceFromHome'].mean().round(2)
)