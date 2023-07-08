import csv
# 针对跨行一致性的层级结构一致约束类，可以采取以下步骤进行数据质量检测：
#
# 检查每个部门的层级关系是否符合总部-分部-子网的三层结构。
#
# 确保每个部门都有一个上级部门，除了总部部门。
# 确保每个部门的上级部门也是表中存在的部门。
# 确保每个部门的上级部门是其直接上一级部门，符合层级关系。
# 检查是否存在重复的层级结构。
#
# 确保每个部门的层级结构是唯一的，即没有相同的部门层级结构重复出现。
# 检查是否存在无效的层级关系。
#
# 确保不存在循环引用的层级关系，例如A部门是B部门的上级部门，而B部门又是A部门的下级部门。
# 检查层级结构的完整性。
#
# 确保所有子网类型的客户都满足总部-分部-子网的三层结构，即每个子网客户都有一个上级分部部门，每个分部部门都有一个上级总部部门。


# 定义表头
fieldnames = ['Department', 'ParentDepartment']
# 定义模拟数据
data = [
    ['Headquarters', None],
    ['Branch1', 'Headquarters'],
    ['Branch2', 'Headquarters'],
    ['Subnet1', 'Branch1'],
    ['Subnet2', 'Branch1'],
    ['Subnet3', 'Branch2']
]

# 将数据写入CSV文件
with open('15data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(data)
