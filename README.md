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
Employees working overtime are nearly three times more likely to leave the company than those who do not work overtime. HR should evaluate workload allocation, overtime policies, and employee well-being initiatives to reduce voluntary turnover.

#### 2. Does monthly income affect employee attrition?
-Finding
Employees who leave the company generally have lower monthly incomes than employees who stay.

-Evidence
--The median monthly income of employees who resigned is lower than that of employees who stayed.
--The histogram also shows that employees with lower salaries are more frequently found in the attrition group.

-Business Insight
Monthly income appears to be associated with employee attrition. Employees with lower salaries tend to leave the company more frequently than employees with higher salaries. HR should regularly review compensation policies, particularly for employees in lower salary ranges.

### 3. Which department has the highest attrition rate?
-Finding
The Sales department has the highest employee attrition rate(20.6%), followed by Human Resources (19.0%). Although the Research & Development (R&D) department has the largest workforce, it records the lowest attrition rate among three departments (13.8%).

-Evidence
-- Sales: **20.6%**
-- Human Resources: **19.0%**
-- Research & Development: **13.8%**

-Business Insight
The Sales department should become a priority for HR intervention because it experiences the highest employee attrition rate. HR should evaluate workload distribution, compensation, career development opportunities, and managerial support within the Sales department to reduce voluntary turnover.

### 4. Does work-life balance influence employee attrition?

-Finding
Employees with the lowest work-life balance score (Level 1) experience the highest attrition rate. Attrition decreases considerably among employees with better work-life balance (Levels 2-4).

Attrition decreases considerably among employees with better work-life balance.

-Evidence
Work Life Balance Level 1 : **31.25%**
Work Life Balance Level 2 : **16.86%**
Work Life Balance Level 3 : **14.22%**
Work Life Balance Level 4 : **17.65%**

-Business Insight
Poor work-life balance appears to be associated with higher employee attrition. HR should prioritize initiatives that improve work-life balance, such as workload management, flexible working arrangements, and employee wellness programs.

### 5. Does distance from home affect employee attrition?

-Finding
Employees who leave the company generally live farther from the workplace than employees who stay. The average distance from home for employees who resigned is **10.63**, compared with **8.92** for employees who remained with company.

-Evidence
Average Distance from Home
--Stayed: **8.92km**
--Resigned: **10.63 km**

-Business Insight
Distance from home appears to be associated with employee attrition. Employees who live farther from workplace tend to leave the company more frequently. HR may consider flexible work arrangements, transportation support, or location-based hiring strategies to improve employee retention.

### 6. Are employees who experience longer promotion delays more likely to leave the company?

-Finding
Contrary to the initial expectation, employees who remained with company have, on average, waited slightly longer since their last promotion than employees who resigned.

-Evidence

Average Years Since Last Promotion

--Stayed: **2.23 years**
--Resigned:  **1.95 years**

-Business Insight
Years since last promotion does not appear to be a major factor associated with employee attrition in this dataset. Employees who stayed with the company actually waited slightly longer for promotion than employees who resigned. This suggests that other factors, such as overtime, salary, or work-life balance, may play a more important role in employee turnover.

### 7. Which employee characteristics are associated with employee attrition?
-Finding
Among the variables analyzed, overtime appears to be the strongest factor associated with employee attrition. Monthly income, department, work-life balance, and commuting distance also show meaningful relationships with attrition. In contrast, years since the last promotion does not appear to have a strong association with employee attrition.

-Evidence
Key findings from previous analyses:
-- Employees working overtime show nearly three times higher attrition.
-- Employees who resigned generally have lower monthly incomes.
-- Sales records the hiighest department attrition rate.
-- Poor work-life balance is associated with higher attrition.
-- Employees who resigned live slightly farther from the workplace.
-- Years since last promotion shows little evidence of influencing attrition.

-Business Insight
⭐⭐⭐⭐⭐ Overtime
⭐⭐⭐⭐ Monthly Income
⭐⭐⭐ Department
⭐⭐⭐ Work-Life Balance
⭐⭐ Distance From Home
⭐ Years Since Last Promotion

### Final HR Recommendations
Based on this analysis, HR should prioritize:

1. Reducing excessive overtime.
2. Reviewing compensation for lower-income employees.
3. Improving retention strategies within the Sales department.
4. Supporting employees with poor work-life balance.
5. Considering commuting distance when designing flexible work policies.
6. Continue monitoring promotion practices, although promotion delay does not appear to be a major driver of employee attrition in this dataset.