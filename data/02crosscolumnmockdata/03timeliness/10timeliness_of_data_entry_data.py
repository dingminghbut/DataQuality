import csv

data = [
    {"Employee_ID": 1, "Hire_Date": "2022-01-01", "System_Creation_Date": "2022-01-02"},
    {"Employee_ID": 2, "Hire_Date": "2022-03-15", "System_Creation_Date": "2022-03-15"},
    {"Employee_ID": 3, "Hire_Date": "2022-06-30", "System_Creation_Date": "2022-07-01"}
]

fieldnames = ["Employee_ID", "Hire_Date", "System_Creation_Date"]
filename = "10timeliness_of_data_entry_data.csv"

with open(filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

print(f"Simulated data for 'Timeliness of Data Entry' data quality check has been saved to {filename}.")
