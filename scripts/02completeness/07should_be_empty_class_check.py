import pandas as pd
from pandasql import sqldf

# 跨列	完整性	应为空值类	属性满足某种条件下不能维护值	敏感站点不允许维护经纬度信息

# 读取 CSV 文件并转换为 DataFrame
df = pd.read_csv('../../data/02crosscolumnmockdata/01completeness/07mock_data.csv')

# 定义 PandasSQL 查询函数
pysqldf = lambda q: sqldf(q, globals())

# 检测字段
check_col = ['Longitude', 'Latitude']

# 执行数据质量检测的 SQL 查询
query = f'''
    SELECT Site_Name
    FROM df
    WHERE ({check_col[0]} IS NOT NULL AND {check_col[1]} IS NOT NULL)
'''
result = pysqldf(query)

# 输出不符合应为空值类的站点
if not result.empty:
    print("以下站点违反了'应为空值类'的数据质量规则:")
    print(result)
else:
    print("数据质量检测通过，所有站点符合'应为空值类'的要求。")
