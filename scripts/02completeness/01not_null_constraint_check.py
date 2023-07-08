import pandas as pd
from pandasql import sqldf

# 单列	完整性	不可为空类	属性不允许或在满足某种条件下不允许出现空值	员工工号不可为空

# Read the CSV data into a DataFrame
df = pd.read_csv('../../data/01singlecolumnmockdata/01completeness/01mock_data.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# 检测字段
check_col = 'Employee_ID'

# Execute SQL queries for data quality check
query = f'''SELECT {check_col} FROM df WHERE {check_col} IS NULL'''
result = pysqldf(query)

# Output the data quality check result
if result.empty:
    print("Data quality check passed for the '不可为空类' constraint")
else:
    print("Data quality check failed for the '不可为空类' constraint. Null values found in Employee_ID column.")
