import pandas as pd
from pandasql import sqldf

# 读取CSV文件并转换为DataFrame
df = pd.read_csv('../../data/01singlecolumnmockdata/02validity/04validity_length_constraint.csv')

# 创建pandasql对象
pysqldf = lambda q: sqldf(q, globals())

# 执行SQL查询进行数据质量检测
query = "SELECT ID, Password FROM df WHERE LENGTH(Password) < 8 OR LENGTH(Password) > 16"
result = pysqldf(query)

# 输出数据质量检测结果
if result.empty:
    print("Data quality check passed for the '长度约束类' script")
else:
    print("Data quality check failed for the '长度约束类' script. Invalid passwords found:")
    print(result)
