import json
import csv
from datetime import datetime
from filemanager import FileManager  

class JSONManager(FileManager):
    """
    Concrete subclass of FileManager for JSON file operations.
    """

    def open_file(self, file_path: str, mode: str):
        self.file = open(file_path, mode)

    def close_file(self):
        if self.file:
            self.file.close()

    def read_entire_file(self, file_path: str) -> dict:
        with open(file_path, 'r') as f:
            return json.load(f)

    def read_line_from_file(self, file_path: str) -> dict:
        print("This function is not applicable for JSON")
        return ""

    def write_to_file(self, file_path: str, data: dict):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def append_to_file(self, file_path: str, data: dict):
        with open(file_path, 'a') as f:
            f.write('\n')  # Ensure new data starts on a new line
            json.dump(data, f, indent=4)

    def json_to_csv(self, json_file_path: str, csv_file_path: str):
        """
        Converts a JSON file to a CSV file format and writes it to the given CSV file path.
        
        :param json_file_path: Path to the input JSON file.
        :param csv_file_path: Path to the output CSV file.
        """
        # Read JSON file
        with open(json_file_path, 'r') as jsonfile:
            data = json.load(jsonfile)
        
        # Check if the JSON data is in the correct format
        if not isinstance(data, dict):
            raise ValueError("JSON file must contain a dictionary at the top level")
        
        # Write CSV file
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write the headers (keys of the dictionary)
            headers = data.keys()
            writer.writerow(headers)
            
            # Transpose the dictionary values to write rows
            rows = zip(*data.values())
            writer.writerows(rows)

    def update_value_by_key(self, file_path: str, key: str, new_value):
        """
        Updates the value associated with a specific key in the JSON file.

        :param file_path: Path to the JSON file.
        :param key: The key whose value needs to be updated.
        :param new_value: The new value to set for the key.
        """
        # Read the entire JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Update the value if the key exists
        if key in data:
            data[key] = new_value
        else:
            # Optionally handle the case where the key does not exist
            print(f"Key '{key}' not found in the JSON file.")
            return

        # Write the modified JSON back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        def replace(self,old_value, data):
            if isinstance(data, dict):
                #return {k: replace(v) for k, v in data.items()}
                new_data = {}
                for k, v in data.items():
                    new_data[k] = replace(v)
                return new_data
            elif isinstance(data, list):
                result = []
                for item in data:
                    result.append(replace(item))
                return result
                #return [replace(item) for item in data]
            else: #In case it is a string
                return new_value if data == old_value else data
            
    def replace_value_in_json(self, file_path: str, old_value, new_value):
        """
        Recursively replaces all occurrences of old_value with new_value in the JSON file.

        :param file_path: Path to the JSON file.
        :param old_value: The value to be replaced.
        :param new_value: The value to replace with.
        """
        # Read the entire JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)

        # Replace values
        updated_data = self.replace(old_value, data)

        # Write the modified JSON back to the file
        with open(file_path, 'w') as file:
            json.dump(updated_data, file, indent=4)

    def create_file(self, file_path: str):
        with open(file_path, 'w') as f:
            pass  # Just create an empty file

    def delete_file(self, file_path: str):
        super().delete_file(file_path)  # Use parent method for file deletion

    def get_file_size(self, file_path: str) -> int:
        return super().get_file_size(file_path)  # Use parent method for file size

    def get_file_creation_time(self, file_path: str) -> datetime:
        return super().get_file_creation_time(file_path)  # Use parent method for creation time

    def get_file_modification_time(self, file_path: str) -> datetime:
        return super().get_file_modification_time(file_path)  # Use parent method for modification time

# Example usage
if __name__ == "__main__":
    print("This file is not meant to be run directly.")
    # exit()
    json_manager = JSONManager()

    json_manager.create_file('data.json')
    
    # Writing data to JSON
    data_to_write = {
        "users": [
            {"name": "John Doe", "age": 30, "city": "New York"},
            {"name": "Jane Smith", "age": 25, "city": "Los Angeles"}
        ]
    }
    json_manager.write_to_file('data.json', data_to_write)
    
    # Reading entire JSON
    print("Reading entire JSON:")
    data_read = json_manager.read_entire_file('data.json')
    print(data_read)
    
    # Appending data to JSON
    data_to_append = {"name": "Tom Brown", "age": 40, "city": "Chicago"}
    json_manager.append_to_file('data.json', data_to_append)
    
    # Reading line from JSON (not really applicable for JSON but mimicking for consistency)
    print("\nReading single line from JSON:")
    single_line = json_manager.read_line_from_file('data.json')
    print(single_line)
    
    json_manager.delete_file('data.json')
