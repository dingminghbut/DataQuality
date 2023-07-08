import csv
import random
import string

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

# Generate mock data for Contracts table
contracts_data = []
for i in range(1, 11):
    contract_id = f"CON-{i}"
    contract_type = random.choice(["Type A", "Type B", "Type C"])
    signing_customer = random.randint(1, 10)  # Randomly select customer ID
    contract_data = [contract_id, contract_type, signing_customer]
    contracts_data.append(contract_data)

print(contracts_data)
# Generate mock data for Customers table
customers_data = []
for i in range(1, 11):
    customer_id = i
    customer_name = generate_random_string(8)
    customer_type = random.choice(["Individual", "Corporate"])
    customer_data = [customer_id, customer_name, customer_type]
    customers_data.append(customer_data)

print(customers_data)
# Save Contracts data to CSV file
contracts_filename = "11contracts.csv"
contracts_fieldnames = ["ContractID", "ContractType", "SigningCustomer"]

with open(contracts_filename, "w", newline="") as contracts_file:
    contracts_writer = csv.writer(contracts_file)
    contracts_writer.writerow(contracts_fieldnames)
    contracts_writer.writerows(contracts_data)

print(f"Mock Contracts data generated and saved to '{contracts_filename}'.")

# Save Customers data to CSV file
customers_filename = "11customers.csv"
customers_fieldnames = ["CustomerID", "CustomerName", "CustomerType"]

with open(customers_filename, "w", newline="") as customers_file:
    customers_writer = csv.writer(customers_file)
    customers_writer.writerow(customers_fieldnames)
    customers_writer.writerows(customers_data)

print(f"Mock Customers data generated and saved to '{customers_filename}'.")
