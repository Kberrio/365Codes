import json
import csv

def json_to_csv(json_file, csv_file):
    # Open JSON file and load data
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Open CSV file in write mode
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(data[0].keys())
        
        # Write data rows
        for item in data:
            writer.writerow(item.values())

# Example usage:
json_file = 'data.json'
csv_file = 'data.csv'
json_to_csv(json_file, csv_file)
print(f"Conversion complete! JSON file '{json_file}' has been converted to CSV file '{csv_file}'.")
