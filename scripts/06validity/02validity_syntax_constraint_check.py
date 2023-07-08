import pandas as pd
import re
from pandasql import sqldf

# Read the CSV file and convert it to a DataFrame
df = pd.read_csv('../../data/01singlecolumnmockdata/02validity/02validity_syntax_constraint.csv')

# Create a pandasql object
pysqldf = lambda q: sqldf(q, globals())

# Define regular expression patterns for email and ID number validation
email_pattern = r'^[\w\.-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
id_pattern = r'^\d{17}(\d|x|X)$'

# Function to check if the email is valid
def is_valid_email(email):
    return re.match(email_pattern, email) is not None

# Function to check if the ID number is valid
def is_valid_id(id_number):
    id_number = str(id_number)  # Convert to string
    return re.match(id_pattern, id_number) is not None


# Execute SQL query for data quality check
query = """
SELECT ID, Email, ID_Number
FROM df
WHERE NOT (
    Email LIKE '%@%' AND
    ID_Number LIKE '___________[0-9xX]'
)
"""

result = pysqldf(query)

# Check if the result is empty
if result.empty:
    print("Data quality check passed for the '语法约束类' script")
else:
    # Filter out invalid emails
    invalid_emails = result[result['Email'].apply(lambda email: not is_valid_email(email))]
    # Filter out invalid ID numbers
    invalid_id_numbers = result[result['ID_Number'].apply(lambda id_number: not is_valid_id(id_number))]

    # Output the invalid records
    if not invalid_emails.empty:
        print("Invalid email addresses found:")
        print(invalid_emails)
    if not invalid_id_numbers.empty:
        print("Invalid ID numbers found:")
        print(invalid_id_numbers)
