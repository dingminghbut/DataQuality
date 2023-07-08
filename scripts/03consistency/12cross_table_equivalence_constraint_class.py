import pandas as pd
from pandasql import sqldf

# 读取 Contract 数据和 Product_Split 数据
df_contract = pd.read_csv('../../data/03crosstablemockdata/01consistency/12contracts_data.csv')
df_product_split = pd.read_csv('../../data/03crosstablemockdata/01consistency/12product_split_data.csv')

# 定义 PandasSQL 查询函数
pysqldf = lambda q: sqldf(q, globals())

# 执行数据质量检测的 SQL 查询
query = '''
    SELECT c.Contract_ID
    FROM df_contract c
    LEFT JOIN (
        SELECT Contract_ID, SUM(Product_Split_Amount) AS Total_Product_Split_Amount
        FROM df_product_split
        GROUP BY Contract_ID
    ) p ON c.Contract_ID = p.Contract_ID
    WHERE c.Total_Amount != p.Total_Product_Split_Amount
'''
result = pysqldf(query)

# 输出不符合跨表等值一致约束类的合同ID
if not result.empty:
    print("以下合同违反了'跨表等值一致约束类'的数据质量规则:")
    print(result)
else:
    print("数据质量检测通过，所有合同符合'跨表等值一致约束类'的要求。")
