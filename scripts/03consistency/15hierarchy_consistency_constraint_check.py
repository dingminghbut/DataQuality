import pandas as pd
from pandasql import sqldf

# Read the CSV file and convert it to a DataFrame
df = pd.read_csv('../../data/04crossrowmockdata/02consistency/15data.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# Execute SQL queries for data quality check
query = """
SELECT Subnet.*
FROM df AS Subnet
LEFT JOIN df AS Branch ON Subnet.ParentDepartment = Branch.Department
LEFT JOIN df AS Headquarters ON Branch.ParentDepartment = Headquarters.Department
WHERE Subnet.Department <> ''
  AND Subnet.ParentDepartment <> ''
  AND (Branch.Department IS NULL OR Headquarters.Department IS NULL)
"""

query = '''

select Subnet from 
(
select
Subnet,
CASE
    WHEN Category = 'Subnet' and Level = 'Level 3' THEN 'True'
    WHEN Category = 'Branch' and Level = 'Level 2' THEN 'True' 
    WHEN Category = 'Headquarters'  and Level = 'Level 1' THEN 'True' 
    ELSE 'False'
    END AS Detected_Level
from
(
SELECT 
    Subnet.Department AS Subnet, 
    Branch.Department AS Branch, 
    Headquarters.Department AS Headquarters,
    CASE 
        WHEN Subnet.Department IS NOT NULL AND Branch.Department IS NOT NULL AND Headquarters.Department IS NOT NULL THEN 'Level 3'
        WHEN Subnet.Department IS NOT NULL AND Branch.Department IS NOT NULL AND Headquarters.Department IS NULL THEN 'Level 2'
        WHEN Subnet.Department IS NOT NULL AND Branch.Department IS NULL AND Headquarters.Department IS NULL THEN 'Level 1'
        ELSE 'Unknown Level'
    END AS Level,
    CASE 
        WHEN Subnet.Department LIKE '%Headquarters%' THEN 'Headquarters'
        WHEN Subnet.Department LIKE '%Branch%' THEN 'Branch'
        WHEN Subnet.Department LIKE '%Subnet%' THEN 'Subnet'
        ELSE 'Unknown Category'
    END AS category  
FROM df AS Subnet
LEFT JOIN df AS Branch ON Subnet.ParentDepartment = Branch.Department
LEFT JOIN df AS Headquarters ON Branch.ParentDepartment = Headquarters.Department
) t
) t where Detected_Level = 'False'
'''

print(query)
result = pysqldf(query)

print(result)
# Check if the result is empty
if result.empty:
    print("Data quality check passed for the '层级结构一致约束类' script")
else:
    print("Data quality check failed for the '层级结构一致约束类' script. Inconsistent data found.")

