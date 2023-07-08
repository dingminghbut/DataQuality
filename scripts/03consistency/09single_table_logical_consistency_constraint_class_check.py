import pandas as pd
from pandasql import sqldf

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv('../../data/02crosscolumnmockdata/02consistency/09single_table_logical_consistency_constraint_data.csv')

# 定义 PandasSQL 查询函数
pysqldf = lambda q: sqldf(q, globals())


# 执行数据质量检测的 SQL 查询
query = '''
    SELECT Contract_ID
    FROM df
    WHERE Closure_Date < Registration_Date
'''
result = pysqldf(query)

# 输出不符合单表逻辑一致约束类的合同ID
if not result.empty:
    print("以下合同违反了'单表逻辑一致约束类'的数据质量规则:")
    print(result)
else:
    print("数据质量检测通过，所有合同符合'单表逻辑一致约束类'的要求。")
