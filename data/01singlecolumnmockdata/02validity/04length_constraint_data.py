import csv

data = [
    {"ID": 1, "Password": "pass123"},
    {"ID": 2, "Password": "securepass"},
    {"ID": 3, "Password": "password1234"}
]

fieldnames = ["ID", "Password"]
filename = "04validity_length_constraint.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Length Constraint' data quality check has been saved to {filename}.")
