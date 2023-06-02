import pandas as pd
import numpy as np

def check_accuracy(df, column_name, expected_values):
    """
    检查指定列的数据准确性，并返回准确率。
    """
    actual_values = df[column_name].tolist()
    correct_count = sum([1 for i in range(len(expected_values))
                        if actual_values[i] == expected_values[i]])
    return correct_count / len(expected_values)

# 生成随机数据
df = pd.DataFrame({'A': np.random.randint(0, 10, size=100),
                   'B': np.random.choice(['X', 'Y', 'Z'], size=100)})

# 检查 B 列数据准确性：期望值应为 'X'
accuracy = check_accuracy(df, 'B', ['X'] * 100)
print('准确率为：', accuracy)
