import pandas as pd
import numpy as np

def check_consistency(df, column_name):
    """
    检查指定列的数据是否一致，并返回不一致记录。
    """
    unique_values = df[column_name].dropna().unique()
    print(unique_values)
    if len(unique_values) > 1:
        inconsistent_rows = df[df[column_name].notnull() &
                               ~df[column_name].isin(unique_values)].index.tolist()
        return inconsistent_rows
    else:
        return []

# 生成示例数据
data = {'Name': ['Alice', 'Bob', 'Charlie', np.nan, 'Alice'],
        'Age': [23, 30, 25, np.nan, 23],
        'Gender': ['F', 'M', 'F', np.nan, 'F']}
df = pd.DataFrame(data)

# 检查 Name 列数据一致性问题
inconsistent_rows = check_consistency(df, 'Gender')
if inconsistent_rows:
    print(f"发现 Name 列数据不一致的记录：{inconsistent_rows}")
else:
    print("Name 列数据一致。")
