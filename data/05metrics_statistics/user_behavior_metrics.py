import pandas as pd
import random

# 创建日期范围
date_range = pd.date_range(start='2023-12-01', end='2023-12-31', freq='D')

# 创建IMEI号列表（假设有100个不重复的IMEI号）
imei_list = ['IMEI' + str(i) for i in range(100)]

# 创建一个空的DataFrame
df = pd.DataFrame(columns=['Date', 'IMEI', 'Login', 'Browse', 'AppInstall', 'AppActive'])

# 循环遍历日期范围和IMEI号，并生成随机的指标值
for date in date_range:
    for imei in imei_list:
        login_count = random.randint(0, 10)
        browse_count = random.randint(0, 20)
        app_install_count = random.randint(0, 5)
        app_active_count = random.randint(0, 8)

        # 将数据添加到DataFrame中
        df = df.append(
            {'Date': date, 'IMEI': imei, 'Login': login_count, 'Browse': browse_count, 'AppInstall': app_install_count,
             'AppActive': app_active_count}, ignore_index=True)

# 保存DataFrame到CSV文件
df.to_csv('user_behavior_metrics.csv', index=False)
