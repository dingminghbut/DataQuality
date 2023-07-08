import csv

data = [
    {"ID": 1, "Date": "2021-12-31"},
    {"ID": 2, "Date": "01/31/2022"},
    {"ID": 3, "Date": "2022年2月28日"}
]

fieldnames = ["ID", "Date"]
filename = "03validity_format_constraint.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Format Constraint' data quality check has been saved to {filename}.")
