# IBM HR Analytics Employee Attrition

## Project Overview

This project analyzes employee attrition using the IBM HR Analytics dataset. The dataset contains 1,470 employee recoords and 35 variables. 

Initial data quality assessment shows no missing values and no duplicate records, indicating that dataset is ready for analysis.

## Tech Stack

- SQL
- Python
- Pandas
- Matplotlib
- Seaborn
- Power BI

## Workflow

Business Understanding

↓

Data Understanding

↓

Data Cleaning

↓

Exploratory Data Analysis

↓

Dashboard Development

↓

Business Insights

### Business Understanding

Employee attrition is one of the most important HR metrics because replacing an employee is expensive.

The objective of this project is to identify factors associated with employee attrition and provide insights that may support HR decision-making.

### Business Questions
1. Does overtime increase the likelihood of employee attrition?
2. Is employee attrition associated with monthly income?
3. Which department has the highest attrition rate?
4. Does work-life balance influence attrition?
5. Does distance from home affect employee attrition?
6. Are employees who experience longer promotion delays more likely to leave the company?
7. Which employee characteristics are associated with employee attrition?

#### 1. Does overtime increase employee attrition?
-Finding
Employees who work overtime are substantially more likely to leave the company than employees who do not work overtime.

-Evidence
--Employees working overtime: 30.5% resigned, 69.5% remained with the company
--Employees without overtime: 10.4% resigned, 89.6% remained with the company

-Business Insight
Employees working overtime are nearly three times more likely to leave company than those who do not work overtime. HR should evaluate workload allocation, overtime policies, and employee well-being initiatives to reduce voluntary turnover.

#### 2. Does monthly income affect employee attrition?
-Finding
Employees who leave the company generally have lower monthly incomes than employees who stay.

-Evidence
--The median monthly income of employees who resigned is lower than that of employees who stayed.
--The histogram also shows that employees with lower salaries are more frequently found in the attrition group.

-Business Insight
Monthly income appears to be associated with employee attrition. Employees receiving lower salaries may be more likely to seek better opportunities elsewhere. HR should regulary evaluate compensation policies, especially for employees in lower salary ranges.

### EDA 1 - Attrition Distribution
Most employees remain with the company, while only a smaller proportion leave. This indicates that the dataset is imbalanced, with significantly more employees staying than leaving. This imbalance should be considered in further analysis.

### EDA 2 - Department vs Attrition
The Research & Development (R&D) department has the largest number of employees who stay with the company. It also records the highest number of employees who leave. Sales ranks second, while Human Resources has the smallest number of employees.

### EDA 3 - Overtime vs Attrition
Employees who work overtime appear to have a higher likelihood of leaving the company compared to employees who do not work overtime. This suggests that overtime may be associated with employee attrition.

### EDA 4 - Monthly Income
Employees who left the company tend to have lower monthly incomes than employees who stayed. However, additional statistical analysis would be required to determine whether income is a significant factor influencing attrition.

### EDA 5 - Work Life Balance
Employees with lower work-life balance scores appear slightly more likely to leave the company. However, the relationship is not sufficiently clear from this visualization alone and requires further analysis.