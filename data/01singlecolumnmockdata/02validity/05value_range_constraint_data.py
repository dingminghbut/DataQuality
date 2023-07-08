import csv

data = [
    {"ID": 1, "Contract_Type": "Sales"},
    {"ID": 2, "Contract_Type": "Support"},
    {"ID": 3, "Contract_Type": "Marketing"}
]

fieldnames = ["ID", "Contract_Type"]
filename = "05validity_value_range_constraint.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Value Range Constraint' data quality check has been saved to {filename}.")