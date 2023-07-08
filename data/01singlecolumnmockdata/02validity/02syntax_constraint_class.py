import csv

data = [
    {"ID": 1, "Email": "john@example.com", "ID_Number": "1234567890"},
    {"ID": 2, "Email": "mary@example.com", "ID_Number": "9876543210"},
    {"ID": 3, "Email": "invalid_email", "ID_Number": "12345"}
]

fieldnames = ["ID", "Email", "ID_Number"]
filename = "02validity_syntax_constraint.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Validity' data quality check has been saved to {filename}.")
