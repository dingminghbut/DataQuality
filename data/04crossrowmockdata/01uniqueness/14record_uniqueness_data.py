import csv

data = [
    {"ID": 1, "Company_Name": "China Mobile Communications Corporation", "Business_Key": 10001, "Other_Field_1": "Value 1", "Other_Field_2": "Value 2"},
    {"ID": 2, "Company_Name": "China Unicom Communications Co., Ltd.", "Business_Key": 10002, "Other_Field_1": "Value 3", "Other_Field_2": "Value 4"},
    {"ID": 3, "Company_Name": "China Telecom Co., Ltd.", "Business_Key": 10003, "Other_Field_1": "Value 5", "Other_Field_2": "Value 6"}
]

fieldnames = ["ID", "Company_Name", "Business_Key", "Other_Field_1", "Other_Field_2"]
filename = "14record_uniqueness_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Record Uniqueness' data quality check has been saved to {filename}.")
