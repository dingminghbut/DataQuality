import csv

fieldnames = ['Site_Name', 'Longitude', 'Latitude', 'Address', 'City', 'Country', 'Postal_Code', 'Status']

data = [
    ['Site 1', 40.7128, -74.0060, '123 Main St', 'New York', 'USA', '10001', 'Active'],
    ['Site 2', 34.0522, -118.2437, '456 Elm St', 'Los Angeles', 'USA', '90001', 'Active'],
    ['Site 3', None, None, '789 Oak St', 'Sydney', 'Australia', '2000', 'Inactive'],
    ['Site 4', 51.5074, -0.1278, '321 Pine St', 'London', 'UK', 'SW1A 1AA', 'Active'],
    ['Site 5', 35.6895, 139.6917, '987 Maple St', 'Tokyo', 'Japan', '100-0001', 'Active']
]

filename = '07mock_data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fieldnames)
    writer.writerows(data)

print(f"Mock data generated and saved to '{filename}'.")
