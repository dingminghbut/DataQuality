import csv

data = [
    {"Contract_ID": 1, "RMB_Amount": 1000, "USD_Amount": 7000, "Exchange_Rate": 7.0},
    {"Contract_ID": 2, "RMB_Amount": 2500, "USD_Amount": 12500, "Exchange_Rate": 5.0},
    {"Contract_ID": 3, "RMB_Amount": 500, "USD_Amount": 4500, "Exchange_Rate": 9.0}
]

fieldnames = ["Contract_ID", "RMB_Amount", "USD_Amount", "Exchange_Rate"]
filename = "08single_table_equivalence_constraint_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Single-Table Equivalence Constraint' data quality check has been saved to {filename}.")
