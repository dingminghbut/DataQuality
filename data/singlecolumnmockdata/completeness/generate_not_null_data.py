import csv
import random

csv_file = "mock_data.csv"
num_rows = 10

# 定义表头和字段
header = ["Employee_ID", "Employee_Name", "Hire_Date", "Department", "Position"]

# 生成模拟数据并写入CSV文件
with open(csv_file, "w", newline="") as file:
    writer = csv.writer(file)

    # 写入表头
    writer.writerow(header)

    # 生成模拟数据
    for _ in range(num_rows):
        row = [
            str(random.randint(10000, 99999)),  # Employee_ID
            "Employee_" + str(random.randint(1, 100)),  # Employee_Name
            "2021-01-" + str(random.randint(1, 31)),  # Hire_Date
            "Department_" + str(random.randint(1, 5)),  # Department
            "Position_" + str(random.randint(1, 3))  # Position
        ]
        writer.writerow(row)

print("Mock data generation completed.")
