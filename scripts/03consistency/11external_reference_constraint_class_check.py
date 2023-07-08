import pandas as pd
from pandasql import sqldf

#跨表	一致性	外关联约束类	引用其他业务对象属性时，所维护的属性值必须在其他业务对象中存在的约束	合同的签约客户必须为客户主数据中定义的法人客户

# 读取 Contract 数据和 Customer 数据
df_contract = pd.read_csv('../../data/03crosstablemockdata/01consistency/11contracts.csv')
df_customer = pd.read_csv('../../data/03crosstablemockdata/01consistency/11customers.csv')

# 定义 PandasSQL 查询函数
pysqldf = lambda q: sqldf(q, globals())

# 执行数据质量检测的 SQL 查询
query = '''
    SELECT c.ContractID
    FROM df_contract c
    LEFT JOIN df_customer cust ON c.SigningCustomer = cust.CustomerID
    WHERE cust.CustomerType != 'Corporate'
'''
result = pysqldf(query)

# 输出不符合外关联约束类的合同ID
if not result.empty:
    print("以下合同违反了'外关联约束类'的数据质量规则:")
    print(result)
else:
    print("数据质量检测通过，所有合同符合'外关联约束类'的要求。")
