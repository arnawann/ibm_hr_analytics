import pandas as pd
import matplotlib.pyplot as plt

summary = pd.DataFrame({
    'Factor':[
        'Overtime',
        'Monthly Income',
        'Department',
        'Work-Life Balance',
        'Distance From Home',
        'Years Since Last Promotion'
    ],

    'Impact Score':[
        5,
        4,
        3,
        2,
        2,
        1
    ]
})

summary = summary.sort_values(
    by='Impact Score',
    ascending=True
)

plt.figure(figsize=(8,5))

plt.barh(
    summary['Factor'],
    summary['Impact Score'],
    color='steelblue'
)

plt.title('Factors Associated with Employee Attrition')

plt.xlabel('Relative Impact')

plt.show()