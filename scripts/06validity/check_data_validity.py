import pandas as pd


def check_data_validity(data):
    """
    检测有效性数据质量中的数据有效性校验

    参数:
    - data: 待检测的数据（DataFrame）
    """
    # 在此处编写数据有效性校验的代码
    # 检查数据中是否符合特定的规则或约束条件

    # 示例：检查列1是否为正数
    invalid_values = data['列1'][data['列1'] <= 0]

    if invalid_values.empty:
        print("数据有效性校验通过")
    else:
        print("存在数据无效的情况:")
        print(invalid_values)


# 示例数据
data = pd.DataFrame({
    '列1': [1, 2, 3, -4, 5],
    '列2': [6, 7, 8, 9, 10],
    '列3': [11, 12, 13, 14, 15]
})

# 说明：这段代码用于检测有效性数据质量中的数据有效性校验。
# 数据有效性校验是指对数据进行特定的规则或约束条件的验证，以确保数据的合法性和准确性。

# 检测有效性数据质量中的数据有效性校验
check_data_validity(data)
