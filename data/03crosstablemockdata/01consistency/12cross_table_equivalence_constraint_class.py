import csv

contracts = [
    {"Contract_ID": 1, "Total_Amount": 1000},
    {"Contract_ID": 2, "Total_Amount": 500},
    {"Contract_ID": 3, "Total_Amount": 1500}
]

product_split = [
    {"Contract_ID": 1, "Product_Split_Amount": 600},
    {"Contract_ID": 1, "Product_Split_Amount": 400},
    {"Contract_ID": 3, "Product_Split_Amount": 800}
]

contracts_filename = "12contracts_data.csv"
product_split_filename = "12product_split_data.csv"

fieldnames_contracts = ["Contract_ID", "Total_Amount"]
fieldnames_product_split = ["Contract_ID", "Product_Split_Amount"]

with open(contracts_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames_contracts)
    writer.writeheader()
    writer.writerows(contracts)

with open(product_split_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames_product_split)
    writer.writeheader()
    writer.writerows(product_split)

print(f"Simulated data for 'Cross-Table Equivalence Constraint' data quality check has been saved to {contracts_filename} and {product_split_filename}.")
