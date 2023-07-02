import csv

data = [
    {"ID": 1, "Company Name": "China Mobile Communications Corporation", "Business Key": 10001, "Other Field 1": "Value 1", "Other Field 2": "Value 2"},
    {"ID": 2, "Company Name": "China Unicom Communications Co., Ltd.", "Business Key": 10002, "Other Field 1": "Value 3", "Other Field 2": "Value 4"},
    {"ID": 3, "Company Name": "China Telecom Co., Ltd.", "Business Key": 10003, "Other Field 1": "Value 5", "Other Field 2": "Value 6"}
]

fieldnames = ["ID", "Company Name", "Business Key", "Other Field 1", "Other Field 2"]
filename = "record_uniqueness_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Record Uniqueness' data quality check has been saved to {filename}.")
