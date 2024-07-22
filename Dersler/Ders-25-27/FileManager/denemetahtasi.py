import csv
import json

def csv_to_json(csv_file_path: str, json_file_path: str):
    """
    Converts a CSV file to a JSON file format and writes it to the given JSON file path.
    
    :param csv_file_path: Path to the input CSV file.
    :param json_file_path: Path to the output JSON file.
    """
    data = {}
    
    # Read CSV file
    with open(csv_file_path, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Extract headers
        headers = next(reader)
        
        # Initialize lists for each header
        for header in headers:
            data[header] = []
        
        # Read rows and append data to corresponding header lists
        for row in reader:
            for header, value in zip(headers, row):
                data[header].append(value)
    
    # Write JSON file
    with open(json_file_path, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage:
if __name__ == "__main__":
    csv_file_path = 'input.csv'
    json_file_path = 'output.json'
    
    # Example CSV content for demonstration
    example_csv_content = [
        ["Name", "Age", "City"],
        ["John Doe", "30", "New York"],
        ["Jane Smith", "25", "Los Angeles"],
        ["Tom Brown", "40", "Chicago"]
    ]
    
    # Write example data to CSV file for demonstration
    with open(csv_file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(example_csv_content)
    
    # Convert CSV to JSON
    csv_to_json(csv_file_path, json_file_path)
    
    # Reading and printing the JSON file to verify the output
    with open(json_file_path, 'r') as jsonfile:
        data = json.load(jsonfile)
        print(json.dumps(data, indent=4))
