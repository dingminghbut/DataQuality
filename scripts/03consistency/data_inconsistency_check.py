import pandas as pd


def check_data_inconsistency(data):
    """
    检测一致性数据质量中的数据值不一致

    参数:
    - data: 待检测的数据（DataFrame）
    """
    # 检查每行数据是否存在值不一致的情况
    inconsistent_rows = data.apply(lambda row: row.nunique(), axis=1) > 1

    # 获取存在数据值不一致的行
    rows_with_data_inconsistency = data[inconsistent_rows]

    if rows_with_data_inconsistency.empty:
        print("数据中没有数据值不一致的行")
    else:
        print("存在数据值不一致的行:")
        print(rows_with_data_inconsistency)


# 示例数据
data = pd.DataFrame({
    '列1': [1, 2, 3, 4, 5],
    '列2': [6, 7, 8, 9, 10],
    '列3': [11, 12, 13, 14, 15]
})

# 说明：这段代码用于检测一致性数据质量中的数据值不一致。
# 数据值不一致是指数据中某些行的值在同一列中存在差异。

# 检测一致性数据质量中的数据值不一致
check_data_inconsistency(data)
