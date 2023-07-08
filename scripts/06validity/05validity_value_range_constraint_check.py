import pandas as pd
from pandasql import sqldf

# 读取CSV文件并转换为DataFrame
df = pd.read_csv('../../data/01singlecolumnmockdata/02validity/05validity_value_range_constraint.csv')

# 创建pandasql对象
pysqldf = lambda q: sqldf(q, globals())

range = ('Sales', 'Support', 'Marketing')

# 执行SQL查询进行数据质量检测
query = f'''SELECT ID FROM df WHERE Contract_Type NOT IN {range}'''
result = pysqldf(query)

# 输出数据质量检测结果
if result.empty:
    print("Data quality check passed for the '值域约束类' script")
else:
    print("Data quality check failed for the '值域约束类' script. Invalid contract types found:")
    print(result)
