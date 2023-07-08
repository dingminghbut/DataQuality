import pandas as pd
from pandasql import sqldf

# 跨表	一致性	跨表逻辑一致约束类	某一属性值满足其他实体的一个或多个属性值的函数关系的约束(大于或小于)	员工的任命日期早于员工的到岗日期

# Read the CSV files and convert them to DataFrames
df1 = pd.read_csv('../../data/03crosstablemockdata/01consistency/13employees_data.csv')
df2 = pd.read_csv('../../data/03crosstablemockdata/01consistency/13employee_onboarding_data.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# Execute SQL queries for data quality check
query = """
SELECT Employee_ID
FROM df2
WHERE Onboarding_Date > (
    SELECT Appointment_Date
    FROM df1
    WHERE df1.Employee_ID = df2.Employee_ID
)
"""
result = pysqldf(query)

# Check if the result is empty
if result.empty:
    print("Data quality check passed for the '跨表逻辑一致约束类' script")
else:
    print("Data quality check failed for the '跨表逻辑一致约束类' script. Inconsistent data found.")
    print(result)

