import pandas as pd


def check_missing_values(data):
    """
    检测数据完整性中的缺失值

    参数:
    - data: 待检测的数据（DataFrame）
    """
    # 统计每列缺失值数量
    missing_values = data.isnull().sum()

    # 获取存在缺失值的列
    columns_with_missing_values = missing_values[missing_values > 0]

    if columns_with_missing_values.empty:
        print("数据中没有缺失值")
    else:
        print("存在缺失值的列:")
        print(columns_with_missing_values.index.tolist())


# 示例数据
data = pd.DataFrame({
    '列1': [1, 2, 3, None, 5],
    '列2': [6, 7, None, 9, 10],
    '列3': [11, None, 13, 14, 15]
})

# 检测完整性中的缺失值
check_missing_values(data)
