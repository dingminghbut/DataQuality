import csv

data = [
    {"ID": 1, "Company": "China Telecom"},
    {"ID": 2, "Company": "ABC Corporation"},
    {"ID": 3, "Company": "XYZ Corporation"}
]

fieldnames = ["ID", "Company"]
filename = "06fact_reference_standard_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Fact Reference Standard' data quality check has been saved to {filename}.")
