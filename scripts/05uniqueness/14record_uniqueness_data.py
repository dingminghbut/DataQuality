import pandas as pd
from pandasql import sqldf

# Read the CSV file and convert it to a DataFrame
df = pd.read_csv('../../data/04crossrowmockdata/01uniqueness/14record_uniqueness_data.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# Execute SQL query for data quality check
check_col = "Company_Name"

query = f"""
SELECT {check_col}
FROM df 
GROUP BY {check_col}
HAVING COUNT(*) > 1
"""

result = pysqldf(query)

# Check if the result is empty
if result.empty:
    print("Data quality check passed for the '记录唯一类' script")
else:
    print("Data quality check failed for the '记录唯一类' script. Duplicate records found.")

# Output the result
print(result)
