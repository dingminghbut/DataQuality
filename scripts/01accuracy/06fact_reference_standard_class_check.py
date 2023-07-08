import pandas as pd
from pandasql import sqldf

# 单列	准确性	事实参照标准类	存在事实数据或者事实参考标准数据该事实或事实参照标准对比一致的约束	中国电信通信有限公司的信息必须与国家法人数据库中的信息保持一致

# Read the CSV file and convert it to a DataFrame
df = pd.read_csv('../../data/01singlecolumnmockdata/03accuracy/06fact_reference_standard_data.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# 此处也可以关联数据库查出对应的标准
standard_data = ['China Telecom', 'ABC Corporation', 'XYZ Corporation']


# 检测字段
check_col = 'Company'

# Execute SQL queries for data quality check
# query = '''SELECT {check_col} FROM df WHERE {check_col} NOT IN tuple({standard_data})'''.format(check_col=check_col,standard_data=standard_data)
query = f'''SELECT {check_col} FROM df WHERE {check_col} NOT IN {tuple(standard_data)}'''

result = pysqldf(query)

# Check if the result is in standard_data
if result.empty:
    print("Data quality check passed for the '事实参照标准类' script")
else:
    non_standard_data = result[check_col].values.tolist()
    print(f"Data quality check failed for the '事实参照标准类' script. Non-standard data found: {non_standard_data}")
