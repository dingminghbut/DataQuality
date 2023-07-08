import pandas as pd
from pandasql import sqldf

# 读取CSV文件并转换为DataFrame
df = pd.read_csv('../../data/01singlecolumnmockdata/02validity/03validity_format_constraint.csv',encoding='gbk')

# 创建pandasql对象
pysqldf = lambda q: sqldf(q, globals())

# 定义SQL查询
query = "SELECT ID, Date FROM df WHERE NOT Date LIKE '____-__-__'"

# 执行SQL查询
result = pysqldf(query)

# 检查结果
if result.empty:
    print("数据满足格式规范类要求")
else:
    print("数据不满足格式规范类要求")
    print(result)
