import csv

data = [
    {"Contract_ID": 1, "Registration_Date": "2022-01-01", "Closure_Date": "2022-02-01"},
    {"Contract_ID": 2, "Registration_Date": "2022-03-15", "Closure_Date": "2022-02-28"},
    {"Contract_ID": 3, "Registration_Date": "2022-06-30", "Closure_Date": "2022-07-15"}
]

fieldnames = ["Contract_ID", "Registration_Date", "Closure_Date"]
filename = "09single_table_logical_consistency_constraint_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Single-Table Logical Consistency Constraint' data quality check has been saved to {filename}.")
