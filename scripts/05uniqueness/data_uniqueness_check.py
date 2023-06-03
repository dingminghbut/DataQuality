import pandas as pd


def check_data_uniqueness(data, key_columns):
    """
    检测唯一性数据质量中的数据是否唯一

    参数:
    - data: 待检测的数据（DataFrame）
    - key_columns: 用于判断唯一性的列（列表）
    """
    # 根据指定列，检查数据是否存在重复记录
    duplicated_rows = data[data.duplicated(subset=key_columns, keep=False)]

    if duplicated_rows.empty:
        print("数据唯一性校验通过")
    else:
        print("存在重复数据:")
        print(duplicated_rows)


# 示例数据
data = pd.DataFrame({
    '列1': [1, 2, 3, 4, 5],
    '列2': ['A', 'B', 'C', 'B', 'E'],
    '列3': [11, 12, 13, 14, 15]
})

# 说明：这段代码用于检测唯一性数据质量中的数据是否唯一。
# 数据是否唯一是指数据中是否存在重复的记录或重复的数据。

# 指定用于判断唯一性的列
key_columns = ['列2']

# 检测唯一性数据质量中的数据是否唯一
check_data_uniqueness(data, key_columns)
