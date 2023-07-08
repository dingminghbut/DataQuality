import csv

employees = [
    {"Employee_ID": 1, "Appointment_Date": "2022-01-01"},
    {"Employee_ID": 2, "Appointment_Date": "2022-02-01"},
    {"Employee_ID": 3, "Appointment_Date": "2022-03-01"}
]

employee_onboarding = [
    {"Employee_ID": 1, "Onboarding_Date": "2022-01-15"},
    {"Employee_ID": 2, "Onboarding_Date": "2022-01-20"},
    {"Employee_ID": 3, "Onboarding_Date": "2022-02-10"}
]

employees_filename = "13employees_data.csv"
employee_onboarding_filename = "13employee_onboarding_data.csv"

fieldnames_employees = ["Employee_ID", "Appointment_Date"]
fieldnames_employee_onboarding = ["Employee_ID", "Onboarding_Date"]

with open(employees_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames_employees)
    writer.writeheader()
    writer.writerows(employees)

with open(employee_onboarding_filename, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames_employee_onboarding)
    writer.writeheader()
    writer.writerows(employee_onboarding)

print(f"Simulated data for 'Cross-Table Logical Consistency Constraint' data quality check has been saved to {employees_filename} and {employee_onboarding_filename}.")
