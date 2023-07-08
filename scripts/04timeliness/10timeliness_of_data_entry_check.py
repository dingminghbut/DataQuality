import pandas as pd
from pandasql import sqldf

# Read the CSV file and convert it to a DataFrame
df = pd.read_csv('../../data/02crosscolumnmockdata/03timeliness/10timeliness_of_data_entry_data.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# Execute SQL query for data quality check
query = """
SELECT *
FROM df
WHERE Hire_Date >= System_Creation_Date
"""

result = pysqldf(query)

# Check if the result is empty
if result.empty:
    print("Data quality check passed for the '入库及时类' script")
else:
    print("Data quality check failed for the '入库及时类' script. Inconsistent data found.")
    print(result)
