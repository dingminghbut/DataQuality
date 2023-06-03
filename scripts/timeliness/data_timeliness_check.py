import pandas as pd
from datetime import datetime, timedelta


def check_data_timeliness(data, max_delay_hours):
    """
    检测及时性数据质量中的数据更新延迟

    参数:
    - data: 待检测的数据（DataFrame）
    - max_delay_hours: 允许的最大数据更新延迟时间（以小时为单位）
    """
    # 获取数据的最新时间戳
    latest_timestamp = data.index.max()

    # 计算当前时间与最新时间戳之间的时间差
    current_time = datetime.now()
    time_diff = current_time - latest_timestamp

    if time_diff <= timedelta(hours=max_delay_hours):
        print("数据更新及时")
    else:
        print(f"数据更新延迟超过 {max_delay_hours} 小时")


# 示例数据
data = pd.DataFrame({
    '列1': [1, 2, 3, 4, 5],
    '列2': [6, 7, 8, 9, 10],
    '列3': [11, 12, 13, 14, 15]
}, index=pd.date_range(start='2023-01-01', periods=5, freq='D'))

# 说明：这段代码用于检测及时性数据质量中的数据更新延迟。
# 数据更新延迟是指数据更新的时间与当前时间之间的差异，用于评估数据是否及时更新。

# 设置允许的最大数据更新延迟时间（以小时为单位）
max_delay_hours = 24

# 检测及时性数据质量中的数据更新延迟
check_data_timeliness(data, max_delay_hours)
