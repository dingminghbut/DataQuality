import pandas as pd


def check_data_bias(data):
    """
    检测准确性数据质量中的数据偏差

    参数:
    - data: 待检测的数据（DataFrame）
    """
    # 计算每列的均值
    column_means = data.mean()

    # 计算每列与均值的差值的绝对值
    column_biases = (data - column_means).abs()

    # 获取存在数据偏差的列
    columns_with_data_bias = column_biases[column_biases > 0]

    if columns_with_data_bias.empty:
        print("数据中没有数据偏差")
    else:
        print("存在数据偏差的列:")
        print(columns_with_data_bias.index.tolist())


# 示例数据
data = pd.DataFrame({
    '列1': [1, 2, 3, 4, 5],
    '列2': [6, 7, 8, 9, 10],
    '列3': [11, 12, 13, 14, 15]
})

# 说明：这段代码用于检测准确性数据质量中的数据偏差。
# 数据偏差是指数据中某些列的值与整体均值之间的差异。

# 检测准确性数据质量中的数据偏差
check_data_bias(data)
